# Pitch Deck Pre-Screen — Reverie

| Field | Value |
| :--- | :--- |
| Deck file | `examples/reference-deck-seed.md` |
| Artifact type | read-ahead |
| Slides detected | 12 |
| Words | 555 |
| Scored at | 2026-09-28T13:26:22+00:00 |
| Verdict | **INVESTOR-READY** |

## Executive Verdict

INVESTOR-READY — all gates cleared

| Metric | Score | Target | Status |
| :--- | ---: | ---: | :--- |
| Composite Capital Readiness | 96.1% | >= 85% | PASS |
| Track B - Acceptance Score | 96.9% | >= 85% | PASS |
| Track A - Anti-Pattern Index | 4.8% | <= 15% | PASS |
| Critical fails | 0 | 0 | PASS |
| Major fails | 2 | <= 2 | PASS |

## Track A - Anti-Pattern Matrix

| ID | Anti-pattern | Sev | Status | Evidence |
| :--- | :--- | :---: | :---: | :--- |
| AP-01 | Feature list instead of an insight | C | WARN | no explicit insight marker found — verify semantically, absence of the phrase is not proof of absence of the insight |
| AP-02 | No "why now", or a "why" masquerading as "why now" | C | PASS | markers: ['why now'] |
| AP-03 | Buzzword soup | M | PASS | 0 hype lexemes: [] |
| AP-04 | Jargon that excludes the room | M | PASS | 0 internal-jargon lexemes: [] |
| AP-05 | The one-liner describes a category, not a company | C | PASS | title statement: "Reverie helps hospital labs automate weekly compliance retesting." (8 words) |
| AP-06 | Vision with no wedge | M | PASS | wedge language present |
| AP-07 | Top-down TAM only | M | PASS | top-down fragments: []; bottom-up markers: ['bottom-up'] |
| AP-08 | Unsourced market numbers | M | PASS | 0 figure(s) with no nearby source marker |
| AP-09 | Market defined so broadly it implies no focus | M | PASS | none |
| AP-10 | No product evidence of any kind | C | PASS | product markers: []; embedded images: True |
| AP-11 | Mockups presented as shipping product | C | PASS | no unlabelled mockups detected |
| AP-12 | Roadmap presented as traction | M | PASS | roadmap and traction distinguished |
| AP-13 | No proof it works | M | PASS | usage or retention proof present |
| AP-14 | Vanity metrics | M | PASS | vanity lexemes: [] |
| AP-15 | Hockey-stick without stated assumptions | C | PASS | projection present with no stated assumptions |
| AP-16 | Cherry-picked time window | M | PASS | no short-window framing detected |
| AP-17 | No retention or cohort evidence where the model requires it | M | PASS | retention evidence present, or model does not require it |
| AP-18 | Pre-revenue with zero demand evidence | C | PASS | demand evidence or revenue present |
| AP-19 | No business model | C | PASS | business-model markers: ['business model', 'pricing', 'per month', 'annual contract'] |
| AP-20 | Unit economics missing or implausible | M | PASS | unit-economics markers: ['ltv', 'cac', 'payback', 'gross margin', 'burn multiple'] |
| AP-21 | Blended metrics passed off as channel metrics | M | PASS | no undefined CAC detected |
| AP-22 | Margins omitted in a capital-intensive or marketplace model | M | PASS | margin stated, or model is not capital-intensive |
| AP-23 | "We have no competition" | C | PASS | competition acknowledged |
| AP-24 | Only comparing against giants | M | PASS | no incumbent-giant comparisons detected |
| AP-25 | A comparison grid where you win every row | M | PASS | no all-checkmark grid detected |
| AP-26 | No defensibility | M | PASS | moat markers: ['moat', 'switching cost', 'regulatory'] |
| AP-27 | Advisor-heavy team slide | M | PASS | founder content present |
| AP-28 | No founder-market fit | C | PASS | founder-market-fit language: ['built', 'shipped', 'led', 'scaled'] |
| AP-29 | Logos instead of people, or unnamed team | M | PASS | named people with links detected |
| AP-30 | Ask buried, vague, or absent | C | PASS | ask markers: ['raising', 'the ask', 'safe', 'closing in']; money figure present: True |
| AP-31 | No use of funds or milestones | M | PASS | use-of-funds markers: ['use of funds', 'runway']; allocation percentages found: 11 |
| AP-32 | Valuation anchoring inside the deck | M | WARN | valuation anchor present in deck |
| AP-33 | Missing contact and next-step | m | PASS | contact email present |
| AP-34 | Stage mismatch with the target fund | C | PASS | requires the fund-targeting layer; not text-detectable — verify against fund-profiles.md |
| AP-35 | Walls of text | M | FAIL | slides over 60 words: [7, 9, 12] |
| AP-36 | Too many slides | M | PASS | 12 slides (60-word budget artifact; seed read-ahead target 19-20) |
| AP-37 | Illegible type or low contrast | M | PASS | not text-detectable — verify visually |
| AP-38 | Decorative animation, transitions, memes, or stock clip-art | m | PASS | none detected |
| AP-39 | Sent as .pptx instead of PDF | m | PASS | file-format check is performed on the artifact path, not on deck text |
| AP-40 | Numbers inconsistent across slides | C | PASS | no cross-slide numeric conflicts detected |
| AP-41 | Cumulative numbers presented as growth | M | PASS | no cumulative-figure framing detected |
| AP-42 | Double-axis graphs | M | PASS | no dual-axis chart framing detected |

## Track B - Acceptance Matrix

| ID | Criterion | Sev | Status | Evidence |
| :--- | :--- | :---: | :---: | :--- |
| AC-01 | One-line company description | C | PASS | "Reverie helps hospital labs automate weekly compliance retesting." (8 words) |
| AC-02 | Title slide completeness | M | PASS | one-liner: True, contact: True |
| AC-03 | Problem quantified and attributed | C | PASS | quantified pain language detected |
| AC-04 | Status quo and its failure mode | M | PASS | status-quo markers: ['today', 'spreadsheet', 'manual'] |
| AC-05 | Why Now is dated and falsifiable | C | PASS | why-now section present |
| AC-06 | Solution in two sentences with a concrete benefit | C | PASS | solution content detected |
| AC-07 | Product evidence, legible, at least one | C | PASS | product markers/images: True |
| AC-08 | Visual honesty labels | M | PASS | honesty labels: ['live'] |
| AC-09 | One idea per slide and a word budget | M | FAIL | slides over 45 words: [6, 7, 8, 9, 11, 12] |
| AC-10 | Bottom-up market sizing with sourced inputs | M | PASS | bottom-up markers: ['bottom-up'] |
| AC-11 | Entry market (beachhead) named | M | PASS | beachhead markers: ['beachhead'] |
| AC-12 | Every figure sourced and dated | M | PASS | 4 source markers across 43 figure(s) |
| AC-13 | Traction with a real growth metric | C | PASS | traction markers: ['traction', 'arr', 'revenue'] |
| AC-14 | Hero chart annotated with its conclusion | M | PASS | chart annotation/takeaway language detected |
| AC-15 | Retention, cohort, or repeat-usage evidence | M | PASS | retention markers: ['retention', 'cohort', 'churn', 'net revenue retention', 'm6'] |
| AC-16 | Pre-revenue demand evidence | C | N/A | revenue present or stage not flagged pre-revenue |
| AC-17 | Complete business model | C | PASS | business-model markers: ['business model', 'pricing', 'per month'] |
| AC-18 | Unit economics with stated definitions | M | PASS | unit-economics: ['ltv', 'cac', 'payback', 'gross margin', 'burn multiple']; definition markers: ['fully loaded', 'per channel', 'observed', 'definition'] |
| AC-19 | Capital efficiency metric | M | PASS | efficiency markers: ['burn multiple', 'runway'] |
| AC-20 | Direct competitors at your stage, plus the honest substitute | C | PASS | competition markers: ['competition', 'substitute']; honest-loss markers: ['they win'] |
| AC-21 | Defensibility mechanism with evidence | M | PASS | moat markers: ['moat', 'switching cost', 'regulatory'] |
| AC-22 | Founder-market fit with achievements and links | C | PASS | fit markers: ['built', 'shipped', 'led', 'scaled']; links: ['linkedin', 'github'] |
| AC-23 | Explicit ask | C | PASS | ask markers: ['raising', 'the ask', 'safe', 'closing in']; money figure: True |
| AC-24 | Use of funds tied to milestones | M | PASS | use-of-funds markers: ['use of funds', 'runway']; percentages: 11 |
| AC-25 | Numerical consistency and no placeholder residue | C | PASS | conflicts: []; placeholders: [] |
| AC-26 | Legibility | M | PASS | not text-detectable — requires visual inspection of the rendered deck |
| AC-27 | Deliverable hygiene | m | PASS | verify the exported artifact is PDF, <= 10 MB, no leaked speaker notes |
| AC-28 | Appendix present for Q&A depth | M | PASS | appendix section present |

## Next Steps

1. Fix every Critical row before sending this deck to anyone.
2. Run the semantic audit against `references/acceptance-criteria.md` for the criteria marked "not text-detectable".
3. Score fund fit per `references/fund-profiles.md` for each target fund.
4. Re-run this screener after each revision and diff the verdict.

> This is a heuristic pre-screen. It cannot see design, verify claims, or judge whether the business is good. It cannot be used as a substitute for the full audit in `SKILL.md`.