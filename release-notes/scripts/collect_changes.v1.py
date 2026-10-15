#!/usr/bin/env python3
"""
collect_changes.v1.py

Collect the raw facts a release-notes pass needs, and nothing else:
commits since the last release tag, their classification, internal-noise
candidates, revert pairs, and a proposed semver bump. It never writes prose —
translating commits into customer-facing lines stays with the agent.

Changelog:
  - v1.0.0: Initial implementation.
"""

import argparse
import json
import logging
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

TOOL = 'collect_changes/1.0.0'

CONVENTIONAL = re.compile(r'^(?P<type>[a-z]+)(?:\([^)]+\))?(?P<bang>!)?:\s*(?P<subject>.+)$')
BREAKING_BODY = re.compile(r'^\s*BREAKING CHANGE\s*:', re.MULTILINE)
NOISE_SUBJECT = re.compile(
    r'\b(deps?|dependencies|dependabot|renovate|bump|linter?|lint|format|prettier|ruff|biome|typo|readme|changelog|\bci\b)\b',
    re.IGNORECASE,
)
INTERNAL_TYPES = {'chore', 'ci', 'build', 'style', 'test', 'docs', 'refactor'}
USER_FACING_TYPES = {'feat', 'fix', 'perf'}
SEMVER = re.compile(r'^v?(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)$')


def setup_logger() -> logging.Logger:
    """Configures dual logging: timestamped audit file in .logs/ and clean console output."""
    script_path = Path(__file__).resolve()
    tool_name = script_path.stem.split('.')[0]

    log_dir = script_path.parent / '.logs'
    log_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = log_dir / f'{tool_name}_{timestamp}.log'

    logger = logging.getLogger(tool_name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler(log_file, encoding='utf-8')
        fh.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s'))
        logger.addHandler(fh)

        ch = logging.StreamHandler(sys.stderr)  # keep stdout clean for --stdout JSON
        ch.setFormatter(logging.Formatter('%(message)s'))
        logger.addHandler(ch)

    return logger


def git(repo: Path, *args: str) -> str:
    """Runs a read-only git command and returns stdout (empty string on failure)."""
    result = subprocess.run(
        ['git', '-C', str(repo), *args],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f'git {" ".join(args)} failed: {result.stderr.strip()}')
    return result.stdout


def resolve_since(repo: Path, since: str | None) -> tuple[str, str, str | None]:
    """Returns (ref, source, latest_tag). source is arg | tag | root."""
    try:
        latest = git(repo, 'describe', '--tags', '--abbrev=0').strip() or None
    except RuntimeError:
        latest = None

    if since:
        git(repo, 'rev-parse', '--verify', f'{since}^{{commit}}')
        return since, 'arg', latest

    if latest:
        return latest, 'tag', latest

    root = git(repo, 'rev-list', '--max-parents=0', 'HEAD').strip().splitlines()
    return root[-1], 'root', None


def parse_commits(repo: Path, range_ref: str) -> list[dict]:
    """One pass for commit fields, one pass for files — bodies never mix with paths."""
    raw = git(repo, 'log', '--no-merges', '--date=short', '--format=%H%x1f%h%x1f%ad%x1f%s%x1f%b%x1e', range_ref)
    commits: list[dict] = []
    for chunk in raw.split('\x1e'):
        chunk = chunk.strip('\n')
        if not chunk.strip():
            continue
        fields = chunk.split('\x1f', 4)
        if len(fields) < 5:
            continue
        full, short, date, subject, body = fields
        commits.append(
            {
                'hash': full.strip(),
                'short': short.strip(),
                'date': date.strip(),
                'subject': subject.strip(),
                'body': body.strip(),
                'files': [],
            }
        )

    if commits:
        names = git(repo, 'log', '--no-merges', '--name-only', '--format=%x1e%H', range_ref)
        files_by_hash: dict[str, list[str]] = {}
        for chunk in names.split('\x1e'):
            lines = [line for line in chunk.splitlines() if line.strip()]
            if not lines:
                continue
            files_by_hash[lines[0].strip()] = lines[1:]
        for commit in commits:
            commit['files'] = files_by_hash.get(commit['hash'], [])
    return commits


def classify(commit: dict) -> tuple[str, str, bool]:
    """Returns (type, classification, breaking)."""
    subject = commit['subject']
    match = CONVENTIONAL.match(subject)
    ctype = match.group('type') if match else ''
    breaking = bool(match and match.group('bang')) or bool(BREAKING_BODY.search(commit['body']))

    if breaking:
        classification = 'breaking'
    elif ctype in USER_FACING_TYPES:
        classification = 'user_facing'
    elif ctype in INTERNAL_TYPES:
        classification = 'internal'
    elif NOISE_SUBJECT.search(subject):
        classification = 'internal'
    else:
        classification = 'needs_review'
    return ctype, classification, breaking


def pair_reverts(commits: list[dict]) -> tuple[list[dict], int]:
    """Drops a `Revert "X"` and the commit it reverts; both cancel out."""
    by_subject = {c['subject']: c for c in commits}
    dropped: set[str] = set()
    for commit in commits:
        match = re.match(r'^Revert\s+"(.+)"\s*$', commit['subject'])
        if not match:
            continue
        original = by_subject.get(match.group(1))
        if original and original['hash'] not in dropped:
            dropped.update({commit['hash'], original['hash']})
    kept = [c for c in commits if c['hash'] not in dropped]
    return kept, len(dropped)


def propose_version(latest_tag: str | None, commits: list[dict], source: str) -> dict:
    """Semver bump from the actual content: breaking > feat > fix."""
    breaking = [c for c in commits if classify(c)[2]]
    feats = [c for c in commits if classify(c)[0] in {'feat', 'fix', 'perf'} and classify(c)[1] != 'breaking']
    fixes = [c for c in commits if classify(c)[0] == 'fix']

    if breaking:
        bump, reason = 'major', f'{len(breaking)} breaking change(s)'
    elif feats:
        bump, reason = 'minor', f'{len([c for c in feats if classify(c)[0] == "feat"])} feature(s)'
    else:
        bump, reason = 'patch', f'{len(fixes)} fix(es), no features'

    if latest_tag and SEMVER.match(latest_tag):
        match = SEMVER.match(latest_tag)
        current = latest_tag.lstrip('v')
        major, minor, patch = (int(match.group(k)) for k in ('major', 'minor', 'patch'))
        if bump == 'major':
            proposed = f'{major + 1}.0.0'
        elif bump == 'minor':
            proposed = f'{major}.{minor + 1}.0'
        else:
            proposed = f'{major}.{minor}.{patch + 1}'
        return {'current': current, 'bump': bump, 'proposed': proposed, 'reason': reason, 'mark': 'proposed'}

    starting = '0.1.0' if source == 'root' else '1.0.0'
    return {
        'current': None,
        'bump': bump,
        'proposed': starting,
        'reason': f'no semver tag to increment yet (bump would be {bump})',
        'mark': 'proposed',
    }


def main() -> int:
    default_data_dir = Path(__file__).parent.resolve() / 'data'

    parser = argparse.ArgumentParser(description='Collect commits since the last release tag and classify them for release notes.')
    parser.add_argument('--repo', '-r', type=str, default='.', help='Git repository path (default: current directory)')
    parser.add_argument('--since', '-s', type=str, default=None, help='Start ref (default: latest tag, else root commit)')
    parser.add_argument('--stdout', action='store_true', help='Print the full JSON facts file instead of only the summary')
    parser.add_argument(
        '--output-dir',
        '-o',
        type=str,
        default=str(default_data_dir),
        help='Target output directory (defaults to scripts/data/ unless explicitly specified)',
    )
    args = parser.parse_args()

    logger = setup_logger()
    logger.info(f'Executing collect_changes v1 against {args.repo}...')

    repo = Path(args.repo).resolve()
    try:
        ref, source, latest_tag = resolve_since(repo, args.since)
    except RuntimeError as exc:
        logger.error(f'{exc} — is this a git repository?')
        return 1

    range_ref = f'{ref}..HEAD'
    try:
        commits = parse_commits(repo, range_ref)
    except RuntimeError as exc:
        logger.error(str(exc))
        return 1

    if source == 'root':
        logger.info('No release tag found — collecting every commit from the root commit.')

    commits, reverts_dropped = pair_reverts(commits)
    for commit in commits:
        ctype, classification, breaking = classify(commit)
        commit['type'] = ctype
        commit['classification'] = classification
        commit['breaking'] = breaking

    counts = {
        'commits': len(commits),
        'user_facing': sum(c['classification'] == 'user_facing' for c in commits),
        'breaking': sum(c['breaking'] for c in commits),
        'internal': sum(c['classification'] == 'internal' for c in commits),
        'needs_review': sum(c['classification'] == 'needs_review' for c in commits),
        'reverts_dropped': reverts_dropped,
    }
    version = propose_version(latest_tag, commits, source)

    facts = {
        'tool': TOOL,
        'generated': datetime.now().isoformat(timespec='seconds'),
        'repo': str(repo),
        'range': range_ref,
        'since': {'ref': ref, 'source': source, 'tag': latest_tag},
        'head': git(repo, 'rev-parse', '--short', 'HEAD').strip(),
        'counts': counts,
        'proposed_version': version,
        'needs_review': [c['short'] for c in commits if c['classification'] == 'needs_review'],
        'breaking': [c['short'] for c in commits if c['breaking']],
        'commits': commits,
        'notes': [
            'Facts only — no prose. Every customer-facing line must map to a commit here.',
            'classification=needs_review means no conventional prefix: read the diff before dropping or translating it.',
        ],
    }

    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    out_file = output_dir / 'collect_changes_latest.json'
    out_file.write_text(json.dumps(facts, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

    logger.info(f'Range: {range_ref} (since: {source}, tag: {latest_tag or "none"})')
    logger.info(
        f'Commits: {counts["commits"]} — user-facing {counts["user_facing"]}, '
        f'breaking {counts["breaking"]}, internal {counts["internal"]}, '
        f'needs review {counts["needs_review"]}, revert-pair dropped {counts["reverts_dropped"]}'
    )
    logger.info(f'Proposed version: {version["proposed"]} ({version["bump"]}, {version["reason"]})')
    logger.info(f'Facts written to {out_file}')

    if args.stdout:
        print(json.dumps(facts, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
