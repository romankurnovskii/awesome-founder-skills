# How to Use: Release Notes

## What This Skill Does

Turns `git log` since the last release tag into three outputs written from one set of
facts: a Keep a Changelog entry, customer-facing release notes in the product's voice, and
a 280-character announcement line — plus a proposed semver bump with its reasoning.

It splits the work on purpose: `scripts/collect_changes.py` does the mechanical half
(collect commits, classify them, cancel revert pairs, detect breaking changes, propose a
version), and the agent does the half machines cannot do well (drop noise a customer never
sees, translate commits into outcomes, hold one voice across three formats). The script
never writes prose; the agent never invents a change that is not in the facts.

## When to Use

- Before tagging a release: `what changed since v1.3.9`.
- `write the changelog`, `draft release notes`, `announce this version`.
- `what version should we bump to` — the collector proposes, you decide.
- Any time release notes were written from memory and someone found a missing change.

Do not use it for documentation, migration guides, marketing copy, or code changes.

## Prompt Examples

```
release-notes for the current repo, since the last tag, voice from CLAUDE.md
```

```
What changed since v0.9.0? Give me the changelog entry and a tweet-length line,
and tell me which commits you actually had to open the diff for.
```

## What You Get

1. `CHANGELOG.md` entry — `## [1.4.0] - date`, sections Action needed / New / Improved /
   Fixed / Internal.
2. Customer-facing notes — title with a plain-language promise, `Action needed` on top,
   3–7 outcome-first bullets.
3. Announcement line — ≤ 280 characters, counted.
4. `proposed_version` with `reason` (major if breaking, minor if feat, else patch).
5. The `needs_review` hash list — commits with no conventional prefix that had to be read
   by hand. That list is the part worth a human look.

## Key Rules

- Facts first: run `python3 scripts/collect_changes.py --repo <path> [--since <ref>]`
  before drafting; output lands in `scripts/data/collect_changes_latest.json`.
- Never publish a line that is not in the facts; never drop an unread `needs_review` commit.
- Breaking change → `Action needed` in all three outputs, never "improved".
- Ask for product voice (name, tone, banned words, publish target) if the project config
  does not carry it — do not guess.
- Nothing is committed, tagged, or published unless you explicitly ask.

## Files

| File | Role |
| :--- | :--- |
| `scripts/collect_changes.py` | Canonical entry (relative symlink) |
| `scripts/collect_changes.v1.py` | Immutable snapshot — commit collection and classification |
| `references/output-templates.md` | The three output shapes + private fact map |
| `references/triage-rules.md` | Drop/flag rules, pitfalls, 10-item checklist |
| `examples/git-log-sample.txt` | Raw commit list to practise on |
| `examples/release-notes-example.md` | A finished three-part output |
