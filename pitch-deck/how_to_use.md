# How to Use: Pitch Deck

## What This Skill Does

Builds, audits, and targets a startup pitch deck to a specific venture fund.

It runs a **three-layer protocol**:

1. **Track A — 42 Investor-Facing Anti-Patterns (What to Avoid / Red Flags)**:
   catches buzzword soup, a missing or fake "why now", top-down-only TAM,
   vanity metrics, hockey-stick projections with no assumptions, "we have no
   competition", advisor-heavy team slides, a buried ask, walls of text, and
   placeholder or invented numbers.
2. **Track B — 28 Deck Acceptance Criteria (What to Verify & Have / Must-Haves)**:
   verifies the one-liner, quantified problem, dated why-now, product evidence,
   bottom-up sizing, sourced figures, traction, retention cohorts, a complete
   business model, unit economics, honest competition, defensibility,
   founder-market fit, the ask, use of funds, numerical consistency, legibility,
   and the appendix.
3. **Targeting Layer — Fund Fit**: scores the deck against the published emphases
   of a16z, Y Combinator, Sequoia, First Round, Bessemer, Accel, Index Ventures,
   Lightspeed, Greylock, Founders Fund, Antler, and Techstars — and produces
   **one base narrative plus per-fund variants**.

Output: a Capital Gate verdict (`🟢 INVESTOR-READY`, `🟡 NEEDS WORK`,
`🔴 BLOCKED`), the complete anti-pattern and acceptance matrices, a
missing-numbers ledger, and finished slide-by-slide rewrites.

## When to Use

- Writing a deck for a pre-seed, seed, or Series A raise.
- Reviewing a deck before sending it to anyone.
- Diagnosing why investors are passing without replying.
- Tailoring one deck to several funds with very different emphases.
- Preparing the read-ahead deck and the presented deck from one narrative.
- Stress-testing market sizing, unit economics, or the competition slide.

## Prompt Examples

```
Review my pitch deck at ./deck.md and tell me if it is ready to send.
Here is my deck. Audit it against the anti-patterns and acceptance criteria,
then tell me which of a16z, YC, and Sequoia it actually fits.
Build me a seed deck for [company]. I'm raising $2.5M. Here are my metrics: ...
Why are VCs passing on my deck? Score it and rank the fixes.
Tailor this deck for YC. Keep every number the same.
```

## Running the CLI Directly

```bash
# Audit a Markdown or text deck (read-ahead budget)
python3 pitch-deck/scripts/score_deck.py --file deck.md --company "Acme"

# Audit a presented deck (30-word-per-slide budget)
python3 pitch-deck/scripts/score_deck.py --file deck.md --company "Acme" --artifact presented

# PDF and PPTX input (PDF needs pdftotext from poppler; PPTX uses stdlib only)
python3 pitch-deck/scripts/score_deck.py --file deck.pdf --company "Acme"
python3 pitch-deck/scripts/score_deck.py --file deck.pptx --company "Acme"

# Machine-readable output
python3 pitch-deck/scripts/score_deck.py --file deck.md --json --out audit.json

# Self-diagnostic
python3 pitch-deck/scripts/score_deck.py --doctor
```

Exit code is `0` for `INVESTOR-READY` and `NEEDS WORK`, and `1` for `BLOCKED`,
so it can gate a CI step or a pre-send check.

> The CLI is a **heuristic pre-screen**, not the verdict. It cannot see design or
> verify whether a number is true. Criteria it marks "not text-detectable" must be
> graded by reading the deck.

## What You Get

1. **Capital Gate verdict** — `🟢 INVESTOR-READY`, `🟡 NEEDS WORK`, `🔴 BLOCKED`,
   with the exact condition that decided it.
2. **Readiness metrics** — Composite Capital Readiness, Track B Acceptance Score,
   Track A Anti-Pattern Index, and Critical/Major/Minor fail counts.
3. **Track A matrix** — all 42 anti-patterns with status, severity, and the
   evidence quoted from the deck.
4. **Track B matrix** — all 28 acceptance criteria with pass evidence and a
   remediation pointer.
5. **Fund-Fit matrix** — per-fund fit score and the single gap blocking each fund.
6. **Missing-Numbers Ledger** — every claim the deck cannot currently support, and
   how to source it.
7. **Prioritised remediation plan** — split into *before sending anything*,
   *before sending to a top-decile fund*, and *before the partner meeting*.
8. **Per-fund variants** — slide-order and emphasis changes, without changing a
   single number.

## Tips

- **Never let the tool fill a gap.** If a number is missing, it stays a
  `[placeholder]`. Fabricated diligence is worse than no diligence.
- Run the screener before and after every revision and diff the verdict — the
  score moving is the fastest signal that a rewrite helped.
- Fix every Critical row before sending anything, even to a warm intro. One
  Critical fail turns a warm path into a closed one.
- Do not optimise one deck for every fund. Build the base narrative, then export
  variants. The same deck cannot be optimal for a16z and YC at the same time.
- The read-ahead deck and the presented deck are different artifacts. Never send
  the demo-day deck as a read-ahead.
