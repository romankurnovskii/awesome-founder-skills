# Deck Audit Report Template

Deliver the audit in exactly this structure. Every section is mandatory. Omit no
table rows: a partial matrix is a failed audit.

---

## 0. Audit Header

```markdown
# Pitch Deck Audit — <Company>

| Field | Value |
| :--- | :--- |
| Company | <name> |
| Deck version audited | <filename / date / slide count> |
| Artifact type | read-ahead / presented / both |
| Stage claimed | pre-seed / seed / Series A |
| Stage inferred | <from ask, metrics, and target fund> |
| Raise | <amount> <instrument> |
| Target funds | <a16z / YC / Sequoia / …> |
| Audit date | <YYYY-MM-DD> |
| Verdict | 🟢 INVESTOR-READY / 🟡 NEEDS WORK / 🔴 BLOCKED |
```

**Stage-claim check:** state explicitly whether the claimed stage matches the
inferred stage. If it does not, say so here and `FAIL` AC-25.

---

## 1. Executive Verdict

One paragraph, no hedging. Answer: *can this be sent to the stated target funds
tomorrow, and if not, what is the single blocking thing?*

Then:

```markdown
| Metric | Score | Target | Status |
| :--- | ---: | ---: | :--- |
| Composite Capital Readiness | XX% | ≥ 85% | 🟢/🟡/🔴 |
| Track B — Acceptance Score | XX% | ≥ 85% | 🟢/🟡/🔴 |
| Track A — Anti-Pattern Index | XX% | ≤ 15% | 🟢/🟡/🔴 |
| Critical fails | N | 0 | 🟢/🟡/🔴 |
| Major fails | N | ≤ 2 | 🟢/🟡/🔴 |
| Best-fund fit | <fund> XX% | ≥ 75% | 🟢/🟡/🔴 |
```

---

## 2. Fund-Fit Matrix

| Target fund | Fund Fit | Fit verdict | What this fund needs that the deck lacks |
| :--- | ---: | :--- | :--- |
| a16z | XX% | send / warm only / don't send | <gap> |
| YC | XX% | … | <gap> |
| Sequoia | XX% | … | <gap> |
| <other> | XX% | … | <gap> |

**Targeting recommendation:** name the one fund this deck is currently best shaped
for, and the one change that would open the second-best fund.

---

## 3. Track A — Anti-Pattern Matrix (all 42 rows)

```markdown
| ID | Anti-pattern | Sev | Status | Evidence from the deck |
| :--- | :--- | :---: | :---: | :--- |
| AP-01 | Feature list instead of insight | C | FAIL | Solution slide is 7 feature bullets; no belief statement anywhere |
| … | … | … | … | … |
```

Rules: quote the deck. "Nothing found" is a valid evidence cell for `PASS`.
Every `FAIL`/`WARN` row must be expanded in §5.

---

## 4. Track B — Acceptance Checklist Matrix (all 28 rows)

```markdown
| ID | Acceptance criterion | Sev | Status | Evidence / remediation pointer |
| :--- | :--- | :---: | :---: | :--- |
| AC-01 | One-line company description | C | PASS | "Helps labs automate weekly compliance retesting." |
| … | … | … | … | … |
```

---

## 5. Dimension Deep Dives

Group findings by the eleven dimensions of
[`acceptance-criteria.md`](acceptance-criteria.md). For every `FAIL` and `WARN`:

```markdown
### D<n> · <Dimension name>

#### <ID> · <Criterion> — `FAIL` (Critical)

- **Found:** <exact quote or explicit statement of absence>
- **Why it costs the meeting:** <the investor's actual reaction>
- **Fix:** <the replacement, written out, ready to paste>
```

The **Fix** must be a finished artifact — the rewritten one-liner, the actual
bottom-up arithmetic, the real use-of-funds table. Never "add a slide about X".

---

## 6. The Missing-Numbers Ledger

Every place the deck asserts something it cannot support.

```markdown
| # | Slide | Claim | Status | How to source it |
| :-- | :--- | :--- | :--- | :--- |
| 1 | 6 | "market is $47B" | UNSOURCED — hard stop | Replace with bottom-up; source each input |
| 2 | 9 | "LTV/CAC 11x" | UNDEFINED | State LTV window + whether CAC is fully loaded |
```

If this table is non-empty with an `UNSOURCED` row, the verdict floor is 🔴.

---

## 7. Prioritised Remediation Plan

Ranked by (gate-clearing impact ÷ effort). Ten items maximum.

```markdown
| Rank | Fix | Clears | Effort | Owner | Done? |
| ---: | :--- | :--- | :--- | :--- | :---: |
| 1 | Rewrite one-liner to pass the Party Test | AC-01 (C), AP-05 | 30 min | founder | ☐ |
| … | … | … | … | … | ☐ |
```

Split by time-to-send:

- **Before sending anything:** all Critical rows.
- **Before sending to a top-decile fund:** all Major rows.
- **Before the partner meeting:** the appendix gaps and the honest-gap slide.

---

## 8. Per-Fund Variant Notes

For each target fund, list the specific slide-order and emphasis changes:

```markdown
### Variant — <fund>
- Reorder: <x> before <y>
- Promote from appendix: <slides>
- Expand: <slides>
- Framing line on title/closing: "<sentence>"
- Do NOT send if: <hard gap>
```

---

## 9. Attestation

```markdown
- Every number in this audit is either quoted from the deck or absent from it.
- No estimate, benchmark, or market figure has been introduced by this audit.
- Audited artifact: <filename>, <n> slides, <hash if available>.
- Audit performed against acceptance-criteria.md v<x> and
  patterns-and-antipatterns.md v<x>.
```

> **Non-negotiable:** if the founder's deck is missing a number, the audit reports
> the gap. It never fills it. Fabricated diligence is worse than no diligence.
