# Deck Scoring Framework & Capital Gate Thresholds

Defines the scoring mathematics, severity weighting, and go/no-go decision thresholds
for auditing a startup pitch deck across two tracks, plus the fund-targeting layer.

1. **Track A — 42 Investor-Facing Anti-Patterns (What to Avoid / Red Flags)**
2. **Track B — 28 Deck Acceptance Criteria (What to Verify & Have / Must-Haves)**
3. **Targeting Layer — Fund Profile Fit (Which fund will actually read this?)**

---

## 1. Severity Levels & Criterion Weighting

Every criterion in both tracks carries a severity tier reflecting its impact on the
investor's decision to take a first meeting.

| Severity | Weight | Description | Failure Consequence |
| :--- | :---: | :--- | :--- |
| **Critical** | **3 pts** | Fatal: the deck cannot be sent. No one-liner, no ask, no product evidence, no defensible market, "we have no competition", invented numbers, stage mismatch with the target fund. | Immediate pass. Investor closes the deck and does not reply. |
| **Major** | **2 pts** | High-friction: materially reduces meeting conversion. Hockey-stick without assumptions, vanity metrics, top-down-only TAM, walls of text, no use of funds, illegible slides. | Investor skims, loses the thread, defers. Reply rate collapses. |
| **Minor** | **1 pt** | Polish and craft. Missing font consistency, decorative clip-art, logo wall, no agenda slide, inconsistent label casing. | Weakens perceived rigor; cheap to fix. |

---

## 2. Criterion Status Definitions

For every criterion across both tracks, assign exactly one status:

- **`PASS` (100% of points)** — fully satisfied with visible evidence in the deck.
- **`WARN` (50% of points)** — partially satisfied, ambiguous, or present but weak.
- **`FAIL` (0% of points)** — missing or actively violated.
- **`N/A` (excluded)** — genuinely not applicable to this stage, business model, or
  audience (e.g. cohort retention for a pre-launch deep-tech company). Maximum
  applicable points are adjusted downward. `N/A` must be justified in one clause;
  it is not an escape hatch for missing evidence.

> **Rule:** `N/A` cannot be applied to any Critical criterion. If a Critical
> criterion is not applicable, the audit must state why the deck is still sendable
> without it, or the verdict stays capped at 🟡.

---

## 3. Metrics

Let, over a given track, `W_s` be the severity weight (3/2/1) and `n_s` the number of
criteria at that severity that are **not** `N/A`.

### Track A — Anti-Pattern Index (0–100%, lower is better)

Measures the density of investor-repelling patterns actually present in the deck.

$$\text{Anti-Pattern Index} = 100 \times \frac{\sum_{s}\left(3 \cdot \text{CritFails} + 2 \cdot \text{MajFails} + 1 \cdot \text{MinFails}\right) + 0.5\sum_{s} W_s \cdot \text{Warns}}{\sum_{s} W_s \cdot n_s}$$

| Band | Meaning |
| :--- | :--- |
| **0–12%** | Clean. Reads like a founder who has pitched before. |
| **13–30%** | Mild. Isolated tropes; fixable in one revision pass. |
| **31–55%** | Template deck. Reads like it was generated, not earned. |
| **> 55%** | Repellent. Rebuild the narrative before sending to anyone. |

### Track B — Acceptance Score (0–100%, higher is better)

Measures positive fulfillment of the things investors require.

$$\text{Acceptance Score} = 100 \times \frac{\sum_{s} W_s \cdot \text{points earned}}{\sum_{s} W_s \cdot n_s}, \quad \text{points} \in \{1, 0.5, 0\}$$

| Band | Meaning |
| :--- | :--- |
| **≥ 85%** | Sendable to a top-decile fund without apology. |
| **65–84%** | Sendable to a warm intro only, with a cover note addressing the gaps. |
| **< 65%** | Not sendable. Cold outreach here burns the warm path permanently. |

### Composite Capital Readiness Score (0–100%)

$$\text{Capital Readiness} = 0.5 \times (100 - \text{Anti-Pattern Index}) + 0.5 \times \text{Acceptance Score}$$

### Fund-Fit Score (targeting layer, 0–100%)

For each target fund on the shortlist, score the deck against that fund's
**emphasis weights** from [`fund-profiles.md`](fund-profiles.md):

$$\text{FundFit}_f = 100 \times \frac{\sum_{c \in \text{emphasis}(f)} W_c \cdot \text{points}_c}{\sum_{c \in \text{emphasis}(f)} W_c}$$

A deck can be 90% ready and 45% fit for a specific fund. **Fit is not readiness.**
Report them separately and never average them into one number — the founder must
see that the same deck cannot be optimal for a16z and YC simultaneously.

---

## 4. The Capital Gate

```
┌──────────────────────────────────────────────────────────────┐
│                      CAPITAL GATE                            │
└──────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┴─────────────────────┐
        │  Any Critical FAIL in Track A or Track B? │
        └─────────────────────┬─────────────────────┘
                    YES ──────┴────── NO
                     │                │
                     ▼                ▼
              🔴 BLOCKED      Composite ≥ 85%, Acceptance ≥ 85%,
              (fix first)     Anti-Pattern Index ≤ 15%,
                              ≤ 2 Major fails, 0 Critical?
                                       │
                          YES ─────────┴───────── NO
                           │                      │
                           ▼                      ▼
                  🟢 INVESTOR-READY       Acceptance ≥ 65%,
                  (send, tailor per fund) ≤ 1 Critical fail,
                                          Composite ≥ 65%?
                                              │
                                 YES ─────────┴───────── NO
                                  │                      │
                                  ▼                      ▼
                          🟡 NEEDS WORK           🔴 BLOCKED
                          (warm intros only)      (rebuild)
```

### Verdict definitions

| Verdict | Conditions | What the founder may do next |
| :--- | :--- | :--- |
| 🟢 **INVESTOR-READY** | 0 Critical fails; Acceptance ≥ 85%; Anti-Pattern Index ≤ 15%; ≤ 2 Major fails; ≥ 1 target fund with FundFit ≥ 75%. | Send cold and warm. Run the fund-specific variants. |
| 🟡 **NEEDS WORK** | Acceptance 65–84%; ≤ 1 Critical fail; Composite ≥ 65%. | Warm intros only, with a cover note naming the gap. Do not cold-email a top-decile fund. |
| 🔴 **BLOCKED** | ≥ 2 Critical fails, **or** Acceptance < 65%, **or** Anti-Pattern Index > 40%, **or** zero target funds above FundFit 50%. | Rebuild the narrative. Do not send. |

### Hard stops that force 🔴 regardless of arithmetic

1. Any **invented or unsourced number** (the audit fails the deck, not the number).
2. **Stage mismatch** — the deck pitches a Series A round to a pre-seed fund, or a
   pre-revenue idea to a fund that only leads revenue rounds.
3. **Ask missing** — no round size, no instrument, no use of funds.
4. **No product evidence of any kind** — no screenshot, demo, prototype, LOI, or user.
5. **Regulatory or legal claims presented as certainties** without a cited basis.

---

## 5. Score Interpretation Rules for the Auditor

- **Never award a partial credit for effort.** A bullet that says "huge market"
  is a `FAIL` on sizing, not a `WARN`.
- **WARN requires a specific defect.** "Slightly generic" is not a WARN; name the
  generic clause and quote it.
- **Quote the deck.** Every `FAIL`/`WARN` in the report must reference the exact
  slide text, figure, or missing element. No anonymous findings.
- **Score the deck as sent, not as intended.** If the founder explains the missing
  metric verbally, that does not move the score.
- **Fund fit uses per-fund emphasis, not the global weight.** See
  [`fund-profiles.md`](fund-profiles.md) for each fund's emphasis set.
