# Pitch Deck Pre-Screen — Nimbus AI

| Field | Value |
| :--- | :--- |
| Deck file | `examples/weak-deck-example.md` |
| Artifact type | read-ahead |
| Slides detected | 11 |
| Words | 238 |
| Scored at | 2026-09-28T13:26:21+00:00 |
| Verdict | **BLOCKED** |

## Executive Verdict

BLOCKED — hard stop(s): placeholder residue in a sendable deck (AG-7); no product evidence of any kind

| Metric | Score | Target | Status |
| :--- | ---: | ---: | :--- |
| Composite Capital Readiness | 49.1% | >= 85% | REVIEW |
| Track B - Acceptance Score | 35.9% | >= 85% | REVIEW |
| Track A - Anti-Pattern Index | 37.6% | <= 15% | REVIEW |
| Critical fails | 11 | 0 | FAIL |
| Major fails | 14 | <= 2 | FAIL |

> **Hard stops triggered:** placeholder residue in a sendable deck (AG-7); no product evidence of any kind

## Track A - Anti-Pattern Matrix

| ID | Anti-pattern | Sev | Status | Evidence |
| :--- | :--- | :---: | :---: | :--- |
| AP-01 | Feature list instead of an insight | C | WARN | no explicit insight marker found — verify semantically, absence of the phrase is not proof of absence of the insight |
| AP-02 | No "why now", or a "why" masquerading as "why now" | C | FAIL | no why-now section or dated event |
| AP-03 | Buzzword soup | M | FAIL | 11 hype lexemes: ['revolutioniz', 'game-chang', 'cutting-edge', 'next-gen', 'seamless', 'best-in-class'] |
| AP-04 | Jargon that excludes the room | M | PASS | 0 internal-jargon lexemes: [] |
| AP-05 | The one-liner describes a category, not a company | C | FAIL | title statement: "Nimbus AI — Revolutionizing the future of work with an AI-powered productivity platform." (13 words) |
| AP-06 | Vision with no wedge | M | WARN | no wedge/beachhead language detected alongside large-market language |
| AP-07 | Top-down TAM only | M | PASS | top-down fragments: []; bottom-up markers: [] |
| AP-08 | Unsourced market numbers | M | PASS | 0 figure(s) with no nearby source marker |
| AP-09 | Market defined so broadly it implies no focus | M | WARN | "1% of" capture framing detected |
| AP-10 | No product evidence of any kind | C | FAIL | product markers: []; embedded images: False |
| AP-11 | Mockups presented as shipping product | C | PASS | no unlabelled mockups detected |
| AP-12 | Roadmap presented as traction | M | PASS | roadmap and traction distinguished |
| AP-13 | No proof it works | M | WARN | no usage/retention proof detected |
| AP-14 | Vanity metrics | M | WARN | vanity lexemes: ['downloads', 'impressions', 'registered users', 'featured in'] |
| AP-15 | Hockey-stick without stated assumptions | C | FAIL | projection present with no stated assumptions |
| AP-16 | Cherry-picked time window | M | PASS | no short-window framing detected |
| AP-17 | No retention or cohort evidence where the model requires it | M | PASS | retention evidence present, or model does not require it |
| AP-18 | Pre-revenue with zero demand evidence | C | PASS | demand evidence or revenue present |
| AP-19 | No business model | C | FAIL | business-model markers: ['business model'] |
| AP-20 | Unit economics missing or implausible | M | FAIL | no LTV/CAC/payback/gross-margin content |
| AP-21 | Blended metrics passed off as channel metrics | M | PASS | no undefined CAC detected |
| AP-22 | Margins omitted in a capital-intensive or marketplace model | M | PASS | margin stated, or model is not capital-intensive |
| AP-23 | "We have no competition" | C | FAIL | explicit "no competition" claim found |
| AP-24 | Only comparing against giants | M | PASS | giants named without peer competitors: ['google'] |
| AP-25 | A comparison grid where you win every row | M | PASS | no all-checkmark grid detected |
| AP-26 | No defensibility | M | FAIL | no defensibility mechanism named |
| AP-27 | Advisor-heavy team slide | M | PASS | founder content present |
| AP-28 | No founder-market fit | C | PASS | founder-market-fit language: ['built', 'led'] |
| AP-29 | Logos instead of people, or unnamed team | M | WARN | employer logos/brands without person links |
| AP-30 | Ask buried, vague, or absent | C | PASS | ask markers: ['raising', 'the ask', 'we are raising']; money figure present: True |
| AP-31 | No use of funds or milestones | M | FAIL | use-of-funds markers: []; allocation percentages found: 2 |
| AP-32 | Valuation anchoring inside the deck | M | PASS | none |
| AP-33 | Missing contact and next-step | m | FAIL | no email/contact found |
| AP-34 | Stage mismatch with the target fund | C | PASS | requires the fund-targeting layer; not text-detectable — verify against fund-profiles.md |
| AP-35 | Walls of text | M | PASS | no slide exceeds 60 words |
| AP-36 | Too many slides | M | PASS | 11 slides (60-word budget artifact; seed read-ahead target 19-20) |
| AP-37 | Illegible type or low contrast | M | PASS | not text-detectable — verify visually |
| AP-38 | Decorative animation, transitions, memes, or stock clip-art | m | PASS | none detected |
| AP-39 | Sent as .pptx instead of PDF | m | PASS | file-format check is performed on the artifact path, not on deck text |
| AP-40 | Numbers inconsistent across slides | C | PASS | no cross-slide numeric conflicts detected |
| AP-41 | Cumulative numbers presented as growth | M | PASS | no cumulative-figure framing detected |
| AP-42 | Double-axis graphs | M | PASS | no dual-axis chart framing detected |
| AG-7 | Placeholder residue | C | FAIL | placeholder patterns found: ['\\[your\\s*name\\]'] |

## Track B - Acceptance Matrix

| ID | Criterion | Sev | Status | Evidence |
| :--- | :--- | :---: | :---: | :--- |
| AC-01 | One-line company description | C | WARN | "Nimbus AI — Revolutionizing the future of work with an AI-powered productivity platform." (13 words) |
| AC-02 | Title slide completeness | M | WARN | one-liner: True, contact: False |
| AC-03 | Problem quantified and attributed | C | FAIL | problem not quantified |
| AC-04 | Status quo and its failure mode | M | FAIL | status-quo markers: [] |
| AC-05 | Why Now is dated and falsifiable | C | FAIL | no explicit why-now section |
| AC-06 | Solution in two sentences with a concrete benefit | C | PASS | solution content detected |
| AC-07 | Product evidence, legible, at least one | C | FAIL | product markers/images: False |
| AC-08 | Visual honesty labels | M | FAIL | honesty labels: [] |
| AC-09 | One idea per slide and a word budget | M | PASS | within the 45-word budget |
| AC-10 | Bottom-up market sizing with sourced inputs | M | FAIL | bottom-up markers: [] |
| AC-11 | Entry market (beachhead) named | M | FAIL | no entry-market definition found |
| AC-12 | Every figure sourced and dated | M | FAIL | 0 source markers across 12 figure(s) |
| AC-13 | Traction with a real growth metric | C | PASS | traction markers: ['traction', 'arr', 'growth'] |
| AC-14 | Hero chart annotated with its conclusion | M | WARN | growth metrics present without an annotated conclusion |
| AC-15 | Retention, cohort, or repeat-usage evidence | M | FAIL | no retention/cohort evidence |
| AC-16 | Pre-revenue demand evidence | C | N/A | revenue present or stage not flagged pre-revenue |
| AC-17 | Complete business model | C | WARN | business-model markers: ['business model'] |
| AC-18 | Unit economics with stated definitions | M | FAIL | unit-economics: []; definition markers: [] |
| AC-19 | Capital efficiency metric | M | FAIL | efficiency markers: [] |
| AC-20 | Direct competitors at your stage, plus the honest substitute | C | WARN | competition markers: ['competitor', 'competition']; honest-loss markers: [] |
| AC-21 | Defensibility mechanism with evidence | M | FAIL | no defensibility mechanism |
| AC-22 | Founder-market fit with achievements and links | C | WARN | fit markers: ['built', 'led']; links: [] |
| AC-23 | Explicit ask | C | PASS | ask markers: ['raising', 'the ask', 'we are raising']; money figure: True |
| AC-24 | Use of funds tied to milestones | M | WARN | use-of-funds markers: []; percentages: 2 |
| AC-25 | Numerical consistency and no placeholder residue | C | FAIL | conflicts: []; placeholders: ['\\[your\\s*name\\]'] |
| AC-26 | Legibility | M | PASS | not text-detectable — requires visual inspection of the rendered deck |
| AC-27 | Deliverable hygiene | m | PASS | verify the exported artifact is PDF, <= 10 MB, no leaked speaker notes |
| AC-28 | Appendix present for Q&A depth | M | FAIL | no appendix section found |

## Next Steps

1. Fix every Critical row before sending this deck to anyone.
2. Run the semantic audit against `references/acceptance-criteria.md` for the criteria marked "not text-detectable".
3. Score fund fit per `references/fund-profiles.md` for each target fund.
4. Re-run this screener after each revision and diff the verdict.

> This is a heuristic pre-screen. It cannot see design, verify claims, or judge whether the business is good. It cannot be used as a substitute for the full audit in `SKILL.md`.