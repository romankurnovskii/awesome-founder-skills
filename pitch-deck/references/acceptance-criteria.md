# Deck Acceptance Criteria (Track B)

The 28 things a pitch deck must **verify and have** before it is sent to a
top-decile fund. This is Track B of the audit. Track A (what to avoid) lives in
[`patterns-and-antipatterns.md`](patterns-and-antipatterns.md).

Grading: `PASS` / `WARN` / `FAIL` / `N/A` per
[`scoring-framework.md`](scoring-framework.md). Severity: **C** Critical,
**M** Major, **m** Minor. `N/A` is not permitted on any Critical criterion.

Every criterion lists: **Requirement** → **Pass evidence** → **Fail signal** →
**Remediation**.

---

## Dimension 1 — Company Purpose & Title (AC-01 … AC-02)

### AC-01 · One-line company description — `C`
- **Requirement:** A single declarative sentence stating what the company does and
  for whom, ≤ 15 words, present on the title slide and used consistently
  throughout the deck.
- **Pass evidence:** A stranger reads it once and can repeat it correctly.
  Sequoia's first instruction is exactly this: *"define your company in a single
  declarative sentence"* [2]. DocSend's seed and pre-seed structures both open on
  the company purpose slide, target length 1 page [4][5].
- **Fail signal:** A category label, a slogan, three clauses joined by "and", or a
  sentence containing more than one abstract noun.
- **Remediation:** `<Company> helps <specific who> <do one thing> so they can
  <outcome>`. Delete every word that could appear in a competitor's deck.

### AC-02 · Title slide completeness — `M`
- **Requirement:** Company name, one-liner, founder name and role, date, and a
  reachable contact.
- **Pass evidence:** All five present; contact is an address a partner can reply to.
- **Fail signal:** Logo-only title slide, or no contact anywhere in the deck.
- **Remediation:** Add the contact to the title *and* the closing slide.

---

## Dimension 2 — Problem & Urgency (AC-03 … AC-05)

### AC-03 · Problem quantified and attributed — `C`
- **Requirement:** The problem is stated with at least one number and a named
  population that experiences it.
- **Pass evidence:** "US community banks spend 9 hours per week per analyst on
  reconciliation that regulators now require weekly."
- **Fail signal:** "It's hard for small businesses to manage finances."
- **Remediation:** Attach a count, a cost, a frequency, or a time figure; name
  whose money or hours are being burned. Cite the source.

### AC-04 · Status quo and its failure mode — `M`
- **Requirement:** The deck names what the customer does today (including
  "spreadsheet", "intern", "nothing") and states specifically why that fails.
- **Pass evidence:** Sequoia requires the problem section to cover *"how this is
  addressed today and what are the shortcomings to current solutions"* [2].
- **Fail signal:** Problem slide with no before-state; implicitly assumes the
  customer is doing nothing.
- **Remediation:** Add one line: `Today they <do X>, which fails because <reason>.`

### AC-05 · Why Now is dated and falsifiable — `C`
- **Requirement:** A specific change with a year that makes this company possible
  or necessary *now*.
- **Pass evidence:** A named event, cost crossing, model capability, platform
  policy shift, or regulation with a date. DocSend: the Why Now slide appeared in
  **54% of successful decks vs 38% of unsuccessful** ones, and got **36% more
  attention** in funded decks [5]. Sequoia lists "Why now?" as a top-level section
  [2].
- **Fail signal:** A trend statement with no date; a slide that would read
  identically in 2019 and in 2031.
- **Remediation:** Answer the two DocSend tests — *would this have been true five
  years ago? Will it be true in five years?* If yes to either, replace it with an
  event [5].

---

## Dimension 3 — Solution & Product (AC-06 … AC-09)

### AC-06 · Solution in two sentences with a concrete benefit — `C`
- **Requirement:** What the company does, in ≤ 2 sentences, expressed as an
  outcome rather than an architecture.
- **Pass evidence:** YC's seed template: *"explain what you do very clearly, in as
  few words as possible. Describe the concrete benefits you provide"* [1].
  Sequoia asks for *"your eureka moment"* and why the value is unique [2].
- **Fail signal:** A feature list, a technology stack, or a diagram of the
  architecture on the solution slide.
- **Remediation:** One sentence for the mechanism, one for the benefit.

### AC-07 · Product evidence, legible, at least one — `C`
- **Requirement:** At least one real product visual or demo reference — cropped,
  captioned, and readable at presentation scale.
- **Pass evidence:** DocSend found investors spend **59 s on the product section at
  seed** and **77 s at pre-seed**, the largest single block for pre-seed, so the
  product must be inspectable [4][5]. Kevin Hale's test: legible, simple, obvious
  [3].
- **Fail signal:** No product anywhere; or a full-UI screenshot shrunk so text is
  unreadable; or stock illustrations standing in for the product.
- **Remediation:** One screenshot per idea, cropped to the relevant region, with a
  caption that states the takeaway in words.

### AC-08 · Visual honesty labels — `M`
- **Requirement:** Every product visual is labelled `Live`, `Private beta`, or
  `Design concept`.
- **Pass evidence:** Labels present and consistent with the traction slide.
- **Fail signal:** Figma mockups presented as shipping product; roadmap UI shown
  unlabelled. See AP-11.
- **Remediation:** Add the label. This costs nothing and protects the whole
  diligence process.

### AC-09 · One idea per slide and a word budget — `M`
- **Requirement:** Every slide carries exactly one idea; presented-deck body copy
  stays under roughly 30 words.
- **Pass evidence:** Slide headline states the takeaway; body is ≤ 3 short lines
  or one chart with an annotation.
- **Fail signal:** Two ideas sharing a slide; paragraph text; a 12-bullet slide.
  YC's Kevin Hale: *"A simple slide expresses one idea. Do not crowd your slides
  with multiple ideas."* He lists too much text, excessive explanations, excessive
  branding, captions-less photos, animations, transitions, memes, and humour as
  distractions to remove [3].
- **Remediation:** Split the slide. Move detail to speaker notes or the appendix.

---

## Dimension 4 — Market (AC-10 … AC-12)

### AC-10 · Bottom-up market sizing with sourced inputs — `M`
- **Requirement:** A calculation of the form `reachable customers × realistic ACV
  × realistic attach rate`, with each input cited.
- **Pass evidence:** DocSend's market-size section targets 1–3 pages and expects
  TAM/SAM/SOM analysis [4][5]. The accepted practice across fund guidance is that
  the bottom-up number is the argument and the top-down number is only the ceiling.
- **Fail signal:** "1% of a $50B market." See AP-07.
- **Remediation:** Build the bottom-up model and show the arithmetic on the slide.

### AC-11 · Entry market (beachhead) named — `M`
- **Requirement:** The first segment you will win, narrow enough to name real
  accounts in.
- **Pass evidence:** A specific vertical, geography, or workflow with a countable
  population.
- **Fail signal:** "Enterprise" or "SMBs" as the beachhead; market defined so
  broadly that no go-to-market follows.
- **Remediation:** Name the segment and one real example customer in it.

### AC-12 · Every figure sourced and dated — `M`
- **Requirement:** Each market, traction, and benchmark number carries a source and
  a year — including self-computed figures, which must say so.
- **Pass evidence:** Footnote or inline `(Source, Year)` on each figure.
- **Fail signal:** Any unsourced number. **A single invented figure is a hard stop
  that forces 🔴** in [`scoring-framework.md`](scoring-framework.md).
- **Remediation:** Cite, or replace with the honest measurement you do have.

---

## Dimension 5 — Traction & Evidence (AC-13 … AC-16)

### AC-13 · Traction with a real growth metric — `C`
- **Requirement:** At least one metric that would hurt if it stopped growing —
  revenue, active usage, retention, gross margin, signed pipeline.
- **Pass evidence:** DocSend's traction section targets 1–4 pages and notes that
  investor scrutiny of traction rises **80% for companies that have not yet
  raised** [5].
- **Fail signal:** Downloads, registered users, impressions, waitlist size,
  followers, or "LOIs worth $X" as the headline metric. See AP-14.
- **Remediation:** Lead with revenue or usage; if pre-revenue, use AC-16.

### AC-14 · Hero chart annotated with its conclusion — `M`
- **Requirement:** The growth chart carries a written takeaway beside it, not just
  an axis.
- **Pass evidence:** Kevin Hale's "obvious/explicit" principle — *"It's like I put
  CliffsNotes right on the slide"*; without the caption the investor has to study
  the graph to reach the conclusion [3].
- **Fail signal:** An unannotated line chart; a chart whose takeaway requires
  mental arithmetic.
- **Remediation:** Write the conclusion in words on the slide.

### AC-15 · Retention, cohort, or repeat-usage evidence — `M`
- **Requirement:** For subscription, marketplace, consumer, or usage-based
  businesses: cohort retention or net revenue retention, with the definition of
  "retained" stated on the slide.
- **Pass evidence:** A cohort curve, or NRR/GRR with the measurement window.
- **Fail signal:** A growth chart with no retention data in a model where retention
  determines LTV. `N/A` only for genuinely one-shot-purchase models, justified in
  one clause.
- **Remediation:** Pull the cohort data even if it is ugly; an honest 71% M6 curve
  beats no curve (see P-13, the honest gap slide).

### AC-16 · Pre-revenue demand evidence — `C` *(mandatory when revenue = 0)*
- **Requirement:** At least one of — signed LOIs, paid pilots, a waitlist with
  conversion data, design-partner usage, or a working prototype with external
  users.
- **Pass evidence:** Named evidence with a count ("6 signed paid pilots at
  $2k/month starting March").
- **Fail signal:** "Pre-revenue and pre-evidence." See AP-18.
- **Remediation:** Convert one warm relationship into a signed paid pilot before
  sending the deck. This is the single highest-leverage pre-send action.

---

## Dimension 6 — Business Model & Economics (AC-17 … AC-19)

### AC-17 · Complete business model — `C`
- **Requirement:** Price point, unit sold, buyer, sales motion, and gross margin.
- **Pass evidence:** DocSend found the **business model is the most-read section**
  at both pre-seed (83 s) and seed (64 s) [4][5]. Sequoia asks *"how do you intend
  to thrive?"* [2].
- **Fail signal:** "We'll monetize later." See AP-19.
- **Remediation:** State the provisional model and mark it provisional. Investors
  prefer a labelled hypothesis to silence.

### AC-18 · Unit economics with stated definitions — `M`
- **Requirement:** LTV, CAC, payback months, and gross margin — each with its
  definition, measurement window, and whether it is observed or modelled.
- **Pass evidence:** "CAC $1,840 (fully loaded, includes sales comp, Q3 actual);
  LTV $9,200 (36-month, 4% monthly churn observed); payback 9.4 months."
- **Fail signal:** A single unexplained LTV/CAC ratio; blended CAC presented as
  channel CAC. See AP-20, AP-21.
- **Remediation:** Separate paid from organic; state what is included in CAC.

### AC-19 · Capital efficiency metric — `M`
- **Requirement:** Burn multiple (cash burned ÷ net ARR added), runway months, or
  equivalent efficiency metric.
- **Pass evidence:** a16z explicitly asks founders to **pressure-test the burn
  multiple** and to distinguish **burn-sinks from burn-investments** with a stated
  rationale [6].
- **Fail signal:** Growth described with no reference to cash consumed.
- **Remediation:** Add burn multiple trend across the last 3 quarters.

---

## Dimension 7 — Competition & Defensibility (AC-20 … AC-21)

### AC-20 · Direct competitors at your stage, plus the honest substitute — `C`
- **Requirement:** Named direct competitors at a similar stage, plus the real
  substitute (spreadsheet, agency, do-nothing), plus at least one row where a
  competitor wins.
- **Pass evidence:** DocSend's guidance: focus on companies comparable to yours or
  that recently raised in your space, use a comparison table, and *"do not make
  comparisons with the giants of the industry"* [4][5]. Sequoia requires the
  competition/alternatives section to *"show that you have a plan to win"* [2].
- **Fail signal:** "We have no competition" (AP-23); comparing only to
  Salesforce/Uber/Google (AP-24); an all-checkmarks grid (AP-25).
- **Remediation:** Build a 2×2 or table of true peers and include the losing row.

### AC-21 · Defensibility mechanism with evidence — `M`
- **Requirement:** A named reason this is hard to copy, with evidence.
- **Pass evidence:** Data flywheel, switching cost, network density, regulatory
  position, or distribution lock-up — each with a supporting number.
- **Fail signal:** "First-mover advantage", "our team is faster", or nothing at
  all. See AP-26.
- **Remediation:** Name the mechanism and give the measurement that shows it is
  accruing (e.g. "density: 62% of target accounts have ≥ 3 connections on the
  network").

---

## Dimension 8 — Team (AC-22)

### AC-22 · Founder-market fit with achievements and links — `C`
- **Requirement:** For each founder: name, role, a shipped achievement with scale,
  and the one-line link to this problem. Links to LinkedIn/GitHub.
- **Pass evidence:** YC's seed template: *"Talk about what makes your team
  particularly well suited to the problem. This should be about founders. Nobody
  cares about your advisors."* [1] DocSend's team section is 1–2 pages and should
  explain why these people are the right ones [4][5].
- **Fail signal:** Job titles only; advisors given equal space (AP-27); logos
  instead of people (AP-29).
- **Remediation:** Rewrite each line as `shipped <thing> at <scale> → therefore
  <link to this problem>`.

---

## Dimension 9 — The Ask (AC-23 … AC-24)

### AC-23 · Explicit ask — `C`
- **Requirement:** Round size, instrument, amount already committed, and expected
  close date.
- **Pass evidence:** Both DocSend structures close on a dedicated fundraising-ask
  section with a one-page target [4][5].
- **Fail signal:** No round size; "raising a round"; ask only delivered verbally.
  See AP-30.
- **Remediation:** One slide: `Raising $X <instrument>, $Y committed, closing
  <date>.` a16z's caution applies to the *conversation*: do not open with a price
  expectation or anchor on last round's valuation [6]. Round size is different from
  valuation — state the former, discuss the latter live.

### AC-24 · Use of funds tied to milestones — `M`
- **Requirement:** 3–4 allocation buckets with percentages, each mapped to the
  milestone it buys and the runway it provides.
- **Pass evidence:** a16z: *"Be deliberate and precise on use of proceeds… It is
  not enough to show how much and where you plan to allocate future capital; you
  must also demonstrate that the juice is going to be worth the squeeze."*
  Identify the highest-ROI levers and deprioritized segments [6].
- **Fail signal:** "40% engineering, 30% sales" with no milestone attached.
- **Remediation:** Attach a milestone and a round-readiness claim to each bucket.

---

## Dimension 10 — Integrity (AC-25)

### AC-25 · Numerical consistency and no placeholder residue — `C`
- **Requirement:** Every figure that appears on more than one slide agrees, and no
  `[bracketed]`, `TBD`, `Lorem`, or template text survives.
- **Pass evidence:** One canonical metrics sheet; the deck derives from it.
- **Fail signal:** Market slide says 40M users, financials imply 12M; or
  `[Company Name]` on the title slide. See AP-40 and AG-4/AG-7.
- **Remediation:** Build the metrics sheet, regenerate every figure from it, and
  run `scripts/score_deck.py --check-consistency`.

---

## Dimension 11 — Craft & Deliverable Hygiene (AC-26 … AC-28)

### AC-26 · Legibility — `M`
- **Requirement:** Body type readable from the back of a room; high contrast;
  simple font; headings anchored top.
- **Pass evidence:** Kevin Hale: legible slides are ones *"even old people sitting
  in the back row with bad eyesight can read"* — large type, bold, simple font,
  good contrast, text at the top [3].
- **Fail signal:** Sub-24pt body text, low-contrast grey on grey, text at the
  bottom of the slide. See AP-37.
- **Remediation:** Raise body type, increase contrast, move text up.

### AC-27 · Deliverable hygiene — `m`
- **Requirement:** Sent as PDF, ≤ 10 MB, descriptive filename, no leaked speaker
  notes or hidden slides.
- **Pass evidence:** `Company — Seed — 2026-01.pdf`. PDF export stops font reflow
  and note leakage. See AP-39.
- **Fail signal:** `.pptx` attachment; `deck_final_v7.pptx`; notes pages included.
- **Remediation:** Export to PDF, strip notes, rename.

### AC-28 · Appendix present for Q&A depth — `M`
- **Requirement:** 5–8 backup slides: financial model, cohort/retention detail,
  architecture, pipeline, competitor teardowns, references.
- **Pass evidence:** The main deck stays at 10–12 (presented) or 18–20 (read-ahead)
  while the appendix carries the diligence surface. DocSend's own benchmark deck
  lengths are 18 pages (pre-seed) and 19–20 pages (seed) [4][5].
- **Fail signal:** A 34-slide main deck with everything crammed in the flow, or no
  appendix at all.
- **Remediation:** Move every "detail" slide behind the appendix divider.

---

## Stage applicability matrix

| Criterion | Pre-seed | Seed | Series A |
| :--- | :---: | :---: | :---: |
| AC-01 one-liner | ✅ | ✅ | ✅ |
| AC-02 title completeness | ✅ | ✅ | ✅ |
| AC-03 problem quantified | ✅ | ✅ | ✅ |
| AC-04 status quo | ✅ | ✅ | ✅ |
| AC-05 why now | ✅ | ✅ | ✅ |
| AC-06 solution ≤ 2 sentences | ✅ | ✅ | ✅ |
| AC-07 product evidence | ⚠️ prototype/demo accepted | ✅ | ✅ |
| AC-08 visual honesty labels | ✅ | ✅ | ✅ |
| AC-09 one idea / word budget | ✅ | ✅ | ✅ |
| AC-10 bottom-up sizing | ⚠️ rough accepted | ✅ | ✅ required |
| AC-11 beachhead | ✅ | ✅ | ✅ |
| AC-12 sourced figures | ✅ | ✅ | ✅ |
| AC-13 growth metric | ⚠️ engagement accepted | ✅ | ✅ required |
| AC-14 annotated chart | ✅ | ✅ | ✅ |
| AC-15 retention cohorts | ➖ usually N/A | ✅ | ✅ required |
| AC-16 pre-revenue demand | ✅ mandatory | ✅ if pre-revenue | ➖ must have revenue |
| AC-17 business model | ⚠️ hypothesis labelled | ✅ | ✅ required |
| AC-18 unit economics | ⚠️ modelled accepted | ✅ | ✅ actuals required |
| AC-19 burn multiple | ➖ | ✅ | ✅ required |
| AC-20 competition | ✅ | ✅ | ✅ |
| AC-21 defensibility | ⚠️ thesis accepted | ✅ | ✅ evidence required |
| AC-22 founder-market fit | ✅ critical | ✅ critical | ✅ critical |
| AC-23 explicit ask | ✅ | ✅ | ✅ |
| AC-24 use of funds | ✅ | ✅ | ✅ |
| AC-25 consistency | ✅ | ✅ | ✅ |
| AC-26 legibility | ✅ | ✅ | ✅ |
| AC-27 deliverable hygiene | ✅ | ✅ | ✅ |
| AC-28 appendix | ⚠️ 3–4 slides | ✅ | ✅ required |

✅ required · ⚠️ relaxed standard at this stage · ➖ typically `N/A`

**Stage is not self-declared into a softer rubric.** The auditor must infer stage
from the ask, the metrics, and the target fund — an inconsistent stage claim (e.g.
"pre-seed" with $2M ARR and a Series A ask) is itself a `FAIL` under AC-23/AC-25.
