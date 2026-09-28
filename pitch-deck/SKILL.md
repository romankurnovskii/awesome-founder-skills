---
name: pitch-deck
description: "Build, audit, and target an investor pitch deck to what venture funds actually read. Track A screens 42 anti-patterns (missing why-now, no-competition claims, top-down-only TAM, vanity metrics, unexplained hockey sticks, no explicit ask, placeholders or invented numbers). Track B verifies 28 acceptance criteria (one-liner, quantified problem, product evidence, bottom-up TAM, traction, retention, unit economics, defensible competition, founder-market fit, the ask, use of funds, consistency). Scores Fund Fit against the published emphasis of a16z, Y Combinator, Sequoia, Antler, and 500 Global at pre-seed, seed, or Series A. Produces a Capital Gate verdict (INVESTOR-READY, NEEDS WORK, BLOCKED), anti-pattern and acceptance matrices, a missing-numbers ledger, per-fund variants, and slide-by-slide rewrites. Use when writing, reviewing, or fixing a pitch deck, prepping a seed or Series A raise, tailoring a deck to a16z or YC, or asking 'is my pitch deck ready' or 'review my deck'."
metadata:
  version: 1.0.0
  license: MIT
---

# Pitch Deck: Narrative Build, Acceptance Audit & Fund Targeting

Build and audit a startup pitch deck against what venture funds actually do with
one — and target it to a specific firm.

The deck is not a document. It is an argument delivered to a distracted reader
under time pressure. DocSend's tracking research found investors spend an average
of **3 minutes 44 seconds** on a seed deck and **4 minutes 10 seconds** on a
pre-seed deck, out of **19–20** and **18** pages respectively, and only **58%** of
decks are read to completion [4][5]. Everything
below exists to survive that read.

> **Source numbering.** Bracketed numbers (`[1]`–`[17]`) refer to
> [`references/sources-and-attribution.md`](references/sources-and-attribution.md),
> which records the evidence tier for each source. Two rules follow from it:
> only **Sequoia** and **Y Combinator** publish an ordered, slide-by-slide deck
> structure on their own domain, and every claim about a fund that does not is
> labelled `SECONDARY` or `UNVERIFIED` and must be presented as inference, never as
> the fund's own instruction.

This skill runs a **three-layer protocol**:

1. **Track A — 42 Investor-Facing Anti-Patterns (What to Avoid / Red Flags)**:
   buzzword soup, no "why now", top-down-only TAM, vanity metrics, hockey-stick
   projections without assumptions, "we have no competition", advisor-heavy team
   slides, no explicit ask, walls of text, placeholder and invented numbers.
2. **Track B — 28 Deck Acceptance Criteria (What to Verify & Have / Must-Haves)**:
   one-liner, quantified problem, dated why-now, product evidence, bottom-up
   sizing, sourced figures, traction, retention cohorts, complete business model,
   unit economics, honest competition, defensibility, founder-market fit, the ask,
   use of funds, numerical consistency, legibility, appendix.
3. **Targeting Layer — Fund Fit**: the same deck cannot be optimal for a16z and
   YC simultaneously. Fit is scored per fund against that fund's published
   emphases, and the skill produces **one base narrative plus per-fund variants**.

---

## Non-Negotiable Operating Rules

1. **Never invent a number.** If the deck lacks a figure, the output is a
   bracketed placeholder **and** a line in the Missing-Numbers Ledger. Fabricated
   diligence is worse than no diligence. A **confirmed** invented figure forces the
   verdict to 🔴; the automated pre-screen flags unsourced figures for the agent to
   adjudicate, and any flagged figure it cannot source stays flagged.
2. **Ask before authoring.** If the founder has not supplied the company, stage,
   raise, traction, and team, ask for them. Do not generate a fictional company.
3. **Quote the deck.** Every `FAIL` and `WARN` in an audit cites the exact slide
   text, figure, or the explicit absence of an element.
4. **Score the deck as sent, not as intended.** Verbal context does not move a
   score.
5. **No cheerleading.** The output is a gate decision and a fix list, not
   encouragement. Flattery in a deck audit costs the founder a round.
6. **Fit is not readiness.** Report Fund Fit and Capital Readiness separately.
   Never average them into one number.

---

## The Capital Gate

| Verdict | Conditions | What the founder may do next |
| :--- | :--- | :--- |
| 🟢 **INVESTOR-READY** | 0 Critical fails; Acceptance ≥ 85%; Anti-Pattern Index ≤ 15%; ≤ 2 Major fails; ≥ 1 target fund with Fund Fit ≥ 75%. | Send cold and warm. Run the per-fund variants. |
| 🟡 **NEEDS WORK** | Acceptance 65–84%; ≤ 1 Critical fail; Composite ≥ 65%. | Warm intros only, with a cover note naming the gap. Do not cold-email a top-decile fund. |
| 🔴 **BLOCKED** | ≥ 2 Critical fails, **or** Acceptance < 65%, **or** Anti-Pattern Index > 40%, **or** zero funds above Fund Fit 50%. | Rebuild the narrative before sending. |

**Hard stops that force 🔴 regardless of arithmetic:** any invented or unsourced
figure; stage mismatch with the target fund; missing ask; no product evidence of
any kind; regulatory or legal claims stated as certainties.

Full mathematics: [`references/scoring-framework.md`](references/scoring-framework.md).

---

## Operational Execution Sequence

```
Stage 0  Intake & mode selection (audit an existing deck / author a new one / both)
   │
Stage 1  Fact capture — company, stage, raise, metrics, team, target funds.
   │      Anything unknown becomes a placeholder, never a guess.
   │
Stage 2  Automated pre-screen — run scripts/score_deck.py on the deck.
   │      Populates Track A and Track B heuristics, the missing-numbers ledger,
   │      and the cross-slide numeric consistency check.
   │
Stage 3  Semantic audit — the agent completes every criterion the script marks
   │      "not text-detectable", and re-grades every script FAIL/WARN by reading
   │      the actual slides. The script is a pre-screen, not the verdict.
   │
Stage 4  Fund targeting — score Fund Fit per target fund and name the gap that
   │      blocks each one.
   │
Stage 5  Authoring — write the fixes, the base deck, and the per-fund variants.
   │      Rewrites are finished artifacts, ready to paste.
   │
Stage 6  Delivery — the audit report, the deck, and the next actions.
```

---

### Stage 0 — Intake & Mode Selection

Determine which of three jobs is being done:

| Mode | Trigger | Output |
| :--- | :--- | :--- |
| **Audit** | "review my deck", "is it ready", "why are VCs passing" | Audit report per [`references/report-template.md`](references/report-template.md) |
| **Author** | "build me a pitch deck", "write my deck" | Deck outline + the ask for missing facts |
| **Target** | "which funds fit", "tailor this for a16z" | Fund-fit matrix + per-fund variants |

### Stage 1 — Fact Capture

Collect, before writing a single slide:

- Company name and the one-line description (or the raw idea)
- Stage (pre-seed / seed / Series A) and the round: size, instrument, committed
- Traction: revenue, growth, retention, usage, or the honest absence of it
- Business model: price, unit, buyer, motion, gross margin
- Competition: the direct peers the founder actually loses deals to
- Team: names, roles, what each shipped at what scale
- Target funds

**If any of these is missing, ask.** Missing facts become
`[placeholder — needs <specific fact>]` plus a ledger entry. They never become
invented numbers.

### Stage 2 — Automated Pre-Screen

Run the deterministic screener:

```bash
# Read-ahead deck (default; 60-word/slide tolerance)
python3 scripts/score_deck.py --file deck.md --company "Acme"

# Presented deck (30-word/slide tolerance)
python3 scripts/score_deck.py --file deck.md --company "Acme" --artifact presented

# PDF or PPTX input (pdftotext for PDF; PPTX parsed with stdlib)
python3 scripts/score_deck.py --file deck.pdf --company "Acme"

# Structured JSON for automation
python3 scripts/score_deck.py --file deck.md --json --out audit.json

# Self-diagnostic
python3 scripts/score_deck.py --doctor
```

The script reconstructs the slides, evaluates what is text-detectable in both
tracks, builds the missing-numbers ledger, and applies the Capital Gate.

> **The script is a pre-screen, not the verdict.** It cannot see design,
> legibility, or whether a claim is true. Criteria it marks
> "not text-detectable" — legibility, visual honesty labels, PDF hygiene, stage
> mismatch — must be graded by reading the deck.

### Stage 3 — Semantic Audit

For every criterion the script could not settle, and every script result, read the
actual slides and decide:

1. **The 5-second test.** A stranger reads slide 1 for five seconds. Can they say
   back who the customer is and what changes for them? Kevin Hale's rule: *"If
   they don't immediately say your idea, you lose."* [3]
2. **The Why-Now test.** Would this slide have been equally true five years ago,
   and will it be equally true in five years? If yes to either, it is a "why", not
   a "why now" [4].
3. **The competition test.** Can you name three real competitors in thirty
   seconds? If yes and the deck claims none, that is AP-23.
4. **The proof test.** Is there anything in this deck that would hurt if it
   stopped being true? If not, there is no traction.
5. **The ask test.** Does one slide state the amount, the instrument, what is
   committed, and when it closes?
6. **The consistency test.** Does every figure that appears twice agree?

### Stage 4 — Fund Targeting

Load [`references/fund-profiles.md`](references/fund-profiles.md). For each target
fund, score Fund Fit against that fund's emphasis set and state the single gap
that blocks it. Then give the honest recommendation: which fund this deck is
currently shaped for, and the one change that opens the next one.

Fund Fit is **not** averaged with Capital Readiness. A deck can be 90% ready and
45% fit.

### Stage 5 — Authoring

Use [`references/narrative-architecture.md`](references/narrative-architecture.md)
for the canonical structures and the assembly recipe, and
[`references/patterns-and-antipatterns.md`](references/patterns-and-antipatterns.md)
Part 2 for the positive patterns.

**Every fix is a finished artifact.** Not "add a market slide" — the actual
bottom-up arithmetic. Not "tighten the one-liner" — the rewritten one-liner.
Compare:

```text
BEFORE: "Revolutionizing modern workflows with next-gen AI cognitive fabric."
AFTER:  "Reverie files hospital lab compliance retests automatically — 9 hours
         of analyst work per week becomes 40 minutes."
```

```text
BEFORE: "We will capture 1% of a $50B market."
AFTER:  "38,000 US labs × $18,000 ACV × 22% attach = $150M SOM.
         (Source: CDC CLIA registry 2025; our Q4 2025 pricing.)"
```

### Stage 6 — Delivery

Format the audit per [`references/report-template.md`](references/report-template.md):
verdict header, fund-fit matrix, the complete 30-row Track A matrix, the complete
28-row Track B matrix, dimension deep dives with finished fixes, the
missing-numbers ledger, and a prioritised remediation plan split by
*before sending anything* / *before sending to a top-decile fund* / *before the
partner meeting*.

---

## The Eleven Dimensions

Track A and Track B criteria are grouped across these dimensions. See
[`references/acceptance-criteria.md`](references/acceptance-criteria.md) for the
full Track B rubric and
[`references/patterns-and-antipatterns.md`](references/patterns-and-antipatterns.md)
for Track A.

1. Company purpose & title
2. Problem & urgency
3. Solution & product
4. Market
5. Traction & evidence
6. Business model & economics
7. Competition & defensibility
8. Team
9. The ask
10. Integrity (consistency, sourcing, placeholders)
11. Craft & deliverable hygiene

---

## Two Artifacts, One Narrative

An AP-36 failure and a P-11 pattern are the same insight from opposite sides:

| | Presented deck | Read-ahead deck |
| :--- | :--- | :--- |
| Length | 5–7 slides (demo day) to 10–12 (partner meeting) [3] | 18 (pre-seed) to 19–20 (seed) [4][5] |
| Words per slide | ≤ 30 | ≤ 45–60 |
| Detail | Speaker notes carry it | Slides must be self-explanatory |
| Appendix | 3–4 slides | 5–8 slides |
| Read time | 2 min 30 s to 7 min | 3 min 44 s to 4 min 10 s [4][5] |

Never send the demo-day deck as a read-ahead, and never present the read-ahead.
Build one narrative, export both.

---

## Reference Map

- [`references/patterns-and-antipatterns.md`](references/patterns-and-antipatterns.md) — the 42 anti-patterns, the 14 positive patterns, where funds disagree, and AI-generation tells.
- [`references/acceptance-criteria.md`](references/acceptance-criteria.md) — the 28 acceptance criteria with pass evidence, fail signals, remediation, and a stage applicability matrix.
- [`references/narrative-architecture.md`](references/narrative-architecture.md) — the four canonical structures (Sequoia, YC seed, DocSend seed, DocSend pre-seed), the five-beat arc, stage deltas, and the assembly recipe.
- [`references/fund-profiles.md`](references/fund-profiles.md) — a16z, YC, Sequoia, First Round, Bessemer, Accel, Index, Lightspeed, Greylock, Founders Fund, Antler, Techstars: emphasis sets and what each punishes.
- [`references/scoring-framework.md`](references/scoring-framework.md) — severity weights, status definitions, the mathematics, the Capital Gate, and the hard stops.
- [`references/report-template.md`](references/report-template.md) — the mandatory audit deliverable structure.
- [`references/sources-and-attribution.md`](references/sources-and-attribution.md) — every citation, with what is verbatim guidance, what is dataset research, and what is contested.
- [`scripts/score_deck.py`](scripts/score_deck.py) — the deterministic pre-screen CLI.
- [`references/research-corpus.md`](references/research-corpus.md) — the raw primary-source research corpus, including the sitemap sweeps behind the negative findings and every `UNVERIFIED` flag.
- [`examples/`](examples/) — a full worked audit and a clean reference deck.

---

## Scope Boundary

This skill audits the **deck as an artifact**. It does not audit the business.

- It cannot judge whether the market is real, whether the unit economics are
  achievable, or whether the team will win.
- It does not value the company or recommend terms.
- It does not replace legal, tax, or securities advice.
- A 🟢 INVESTOR-READY verdict means **this deck is ready to be read**, not that the
  raise will succeed. Most passes happen for reasons no deck audit can see.
- **Beware survivorship bias when told to study famous decks.** A library of "754
  real pitch decks" is post-hoc confirmation of companies that already won, and at
  least one widely shared collection was found to contain non-genuine decks. This
  skill derives no criterion from a company's success.
- It does not value the company or recommend terms.
- It does not replace legal, tax, or securities advice.
- **Not investment advice.**
