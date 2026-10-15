# Triage Rules, Pitfalls & Checklist

The collector already assigns `classification` per commit — this file tells you what to do
with each class, and where the classifications are wrong.

## By classification

| Class | Meaning | Action |
| :--- | :--- | :--- |
| `breaking` | `!` after the type, or `BREAKING CHANGE:` in the body | Customer notes **and** changelog get an `Action needed:` line: surface, what changed, who is affected, what to do, deadline if there is one. Never soften into "improved". |
| `user_facing` | `feat` / `fix` / `perf` | Translate into New / Improved / Fixed, grouped by what the customer notices. |
| `internal` | `chore` / `ci` / `build` / `style` / `test` / `docs` / `refactor`, or a noise subject (deps, lint, format, typo, readme) | Out of customer-facing output. One tally line in the changelog's Internal section. |
| `needs_review` | No conventional prefix — unclassified by definition | **Open the diff (`git show <hash>`) before deciding.** Dropping an unread commit is how release notes lie. Add its hash to the fact map either way. |

Revert pairs are removed by the collector; if you pull in extra commits by hand, re-check
`Revert "..."` subjects and drop both sides.

## What to flag even when it looks internal

- **Dependency bump with a security advisory** → one `Fixed` line naming the package, no
  exploit details.
- **`perf` commit with a measurable number** → keep the number, it is the strongest line
  you have.
- **Deprecation without removal** → `Action needed` with the removal version/date if the
  commit states one; otherwise Improved + a note that it is deprecated.
- **Anything touching auth, billing, or data export** → read the diff; these are
  customer-relevant even when filed as `chore`.

## Pitfalls

- **Squash merges** hide intermediate commits — the range is still correct, but a whole
  feature can arrive as one `feat:` line. Translate the feature, not the squash.
- **Merge commits are excluded** (`--no-merges`); do not treat their absence as dropped work.
- **Multiple deploys between tags** → one release, all commits in the range, even if some
  already shipped to users. Say so if the range is unusually long.
- **Tag format** varies (`v1.4.0`, `1.4.0`, `release-2026-10-07`). The collector uses
  `git describe`; if the "tag" is not semver, the proposed version is a fresh start — say that.
- **The proposed version is a proposal.** Present `proposed_version.reason` and let the
  human decide; a breaking change in the range does not by itself authorize a major bump.
- **Two audiences, one voice** — the changelog entry is terse and factual, the customer
  notes are outcome-first. Do not copy one into the other.

## Final checklist

1. Every published line maps to a commit hash in the fact map.
2. Every `needs_review` commit was opened before being kept or dropped.
3. Every `breaking` commit produced an `Action needed` line in **all three** outputs.
4. Sections follow Action needed → New → Improved → Fixed → Internal; empty ones omitted.
5. No sentence over 20 words; no "we're excited"; no ticket numbers.
6. The announcement line is ≤ 280 characters, counted.
7. Version shown as **proposed**, with its reason, not as a decision.
8. Internal tally matches `counts.internal + counts.reverts_dropped`.
9. Product name, tone, and banned words match the project's voice config.
10. Nothing committed, tagged, or published unless the user asked for it.
