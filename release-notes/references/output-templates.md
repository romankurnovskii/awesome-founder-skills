# Output Templates

Same facts, three shapes. Every published line must map to a commit in
`scripts/data/collect_changes_latest.json` — keep that mapping as a private fact map
(see the end) and never publish it.

## 1. CHANGELOG.md entry (Keep a Changelog)

```markdown
## [1.4.0] - 2026-10-07

### Action needed
- **Data export**: `amount` was renamed to `total`. Update your field mapping
  before 2026-10-20.

### New
- Export transactions as CSV with one click from the dashboard.

### Improved
- Monthly review loads about 3x faster for accounts with a year of history.

### Fixed
- Duplicate rows no longer appear after a failed import is retried.

### Internal
- 7 dependency bumps, CI and lint changes not listed here
  (`git log 1.3.9..1.4.0`).
```

Rules:

- `## [version] - YYYY-MM-DD` — the date is the tag date, not "today" if they differ.
- Section order is fixed: **Action needed → New → Improved → Fixed → Internal**. Omit
  empty sections; never create a section for one trivial line.
- `### Action needed` appears only when a `breaking` commit exists. Its bullets start with
  the affected surface in bold, then what changed, then what to do.
- Append under the repo's existing `## [Unreleased]` heading if the CHANGELOG keeps one,
  and never rewrite published entries.
- Link-style (`[1.4.0]: https://...`) only if the CHANGELOG already uses it.

## 2. Customer-facing release notes

```markdown
# Version 1.4.0 — faster exports, fewer surprises

**Action needed:** Data export renamed `amount` → `total`. Update your field
mapping before 2026-10-20.

## What's new
- Export any account as CSV straight from the dashboard.

## What got better
- Monthly reviews now open in under a second, even with a year of history.

## What we fixed
- Retrying a failed import no longer duplicates rows.
```

Rules:

- Title = version + a plain-language promise (no adjectives you cannot support).
- Customer's words for the outcome; developer's words only when the fix is about a named
  API, field, or flag.
- One idea per sentence, 20 words maximum, active voice, no "we're excited", no ticket
  numbers, no internal project codenames.
- 3–7 bullets total. If the range has more, it should have been two releases.
- `Action needed` sits at the top, above everything — a migration note nobody reads is
  worse than no note.

## 3. Announcement line (280 characters)

```markdown
v1.4.0 is out: one-click CSV exports, monthly reviews 3x faster, and no more
duplicate rows on import retry. Action needed: export field `amount` → `total`.
```

Rules:

- Count the characters. 280 max, including the version, the link, and every space.
- One line, one promise plus at most two specifics. No hashtag stacks, no emoji lists
  unless the account's voice uses them.
- Breaking change? The `Action needed` hint is mandatory in the line too.

## Fact map (private, never published)

```text
Action needed: amount -> total        <- 8b44204 feat(api)!
CSV export from dashboard             <- fafbde8 feat
3x faster monthly review              <- f948cb9 perf
duplicate rows on import retry        <- 1d2c3a9 fix
```

Reviewers use it to verify the notes in seconds. Strip it before publishing.
