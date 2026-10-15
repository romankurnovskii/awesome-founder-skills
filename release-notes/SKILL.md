---
name: release-notes
description: "Turn the commits since the last release tag into three audience-specific outputs written from one set of facts: a Keep-a-Changelog entry, customer-facing release notes in the product's voice, and a 280-character announcement line, plus a proposed semver bump. Runs the deterministic collector first (commit gathering, noise classification, revert pairing, breaking-change detection) and only then translates — it never invents a change that is not in the facts. Use before tagging a release, or when asked 'what changed since vX', 'write the changelog', 'draft release notes', 'announce this version', or 'what version should we bump to'. Do not use for writing documentation, migration guides, roadmap or copywriting, or for code changes — only for summarizing commits that are already merged."
metadata:
  version: 1.0.0
---

# Release Notes

Three audiences read a release differently: a developer wants the changelog, a customer
wants to know what got better, a follower wants one line. Write all three from the same
facts — never from memory.

## Inputs

- **Start ref**: the latest release tag by default. If the repo has no tag, start from the
  root commit and say so in the output.
- **Version being released**: take it from the argument if given, otherwise use the
  collector's `proposed_version` and present it as a proposal, not a decision.
- **Product voice** (name, tone, banned words, where notes get published): read it from
  the project's own config (`CLAUDE.md`, `AGENTS.md`, `docs/release-notes.md`) if present;
  if it is missing, ask the user for name and tone instead of guessing.

## Workflow

### 1. Collect facts (deterministic first)

```bash
python3 scripts/collect_changes.py --repo <path> [--since <ref>] [--stdout]
```

Output: `scripts/data/collect_changes_latest.json` with every commit (hash, date, subject,
files), a `classification` per commit (`user_facing` / `internal` / `needs_review` /
`breaking`), revert pairs already cancelled out, counts, and a proposed version.
The script never writes prose — translating commits into customer-facing lines is the
agent's job.

Run it before drafting anything. If it fails, you are not in a git repository; stop.

### 2. Triage

- **Drop `internal`** (chores, deps, CI, lint, docs-typo) from customer-facing output, but
  keep the count in the changelog's Internal tally if the project keeps one.
- **Read every `needs_review` commit** — no conventional prefix, so nobody has classified
  it. Open the diff (`git show <hash>`) before dropping or translating it. Dropping an
  unread commit is the classic way release notes lie.
- **`breaking` commits need an `Action needed:` line** in the customer notes: what changed,
  who is affected, what to do. Do not soften a breaking change into "improved".
- Revert pairs are already removed by the collector; if you add commits by hand, check
  `Revert "..."` subjects again.

### 3. Translate

- Group customer-facing changes by what the customer notices: **New**, **Improved**,
  **Fixed** — never by commit type.
- Use the customer's words for the outcome, the developer's words only when the fix is
  about a named API/field/flag.
- One idea per sentence, 20 words maximum. No "we're excited", no internal ticket numbers.
- Anything the customer must do before or after upgrading → `Action needed:` line.
- If a commit is in the facts but does not matter to a customer, leave it out. If a
  customer-relevant change is missing from the facts, it did not happen in this range —
  do not invent it.

### 4. Compose

Follow `references/output-templates.md` exactly:

1. CHANGELOG.md entry (Keep a Changelog format, version + date, sections New/Improved/Fixed/Action needed/Internal).
2. Customer-facing release notes in the product's voice.
3. A 280-character announcement line — count the characters, no hashtags unless asked.

Then check the output against the checklist in `references/triage-rules.md`.

### 5. Deliver

- Show all three outputs in the reply; write files only where the user asked
  (`CHANGELOG.md` insertion, a notes file, a post draft).
- Report the proposed version with its reason, and the `needs_review` commits you had to
  read — that list is the part a human should confirm.
- Never commit, tag, or publish unless explicitly asked.

## Reference Files

- `references/output-templates.md` — the three output shapes and the changelog entry format.
- `references/triage-rules.md` — what to drop, what to flag, pitfalls, final checklist.
- `examples/git-log-sample.txt` and `examples/release-notes-example.md` — a worked pair.
- `scripts/collect_changes.py` — deterministic collector (canonical symlink, `v1` snapshot).

## Boundary

This skill summarizes commits that already exist in the repository. It does not write docs,
migration guides, marketing copy, or code, and it does not decide the version — it proposes
one and shows the reasoning.
