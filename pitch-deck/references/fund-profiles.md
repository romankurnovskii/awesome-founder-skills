# Fund Profiles & Targeting Layer

The targeting layer answers a different question from the audit: not *is this deck
good*, but *is this deck good for this fund*.

**A deck cannot be optimal for a16z and YC at the same time.** a16z filters on
**metric vocabulary and capital-to-milestone alignment**; YC's seed template puts
traction before market and cares about insight and founder-market fit; Sequoia
ranks market before competition and wants a five-year vision. Averaging these into
one deck produces a deck that is mediocre for all three.

The skill therefore produces **one base narrative plus per-fund variants**.
See [`narrative-architecture.md`](narrative-architecture.md) §6.

---

## Read this before using any profile

Research for this skill swept the sitemaps of the funds named in the original
brief. The result matters more than any individual profile:

> **Only Sequoia and Y Combinator publish an explicit, ordered, slide-by-slide deck
> structure on their own domain.** DocSend publishes two more, but is not a fund.
>
> a16z, Bessemer, Index Ventures, Accel, Lightspeed, Greylock, Redpoint,
> Founders Fund, Benchmark, Coatue, Insight Partners, and **First Round publish no
> canonical deck structure.**

The pages that rank for "Accel / Founders Fund / Bessemer — How to Pitch" are SEO
content farms, not fund publications. Full detail and the sweep evidence:
[`sources-and-attribution.md`](sources-and-attribution.md) and
[`research-corpus.md`](research-corpus.md).

### Evidence tiers used below

| Tier | Meaning |
| :--- | :--- |
| **PRIMARY — structure** | The fund publishes an ordered deck structure. Quotable as guidance. |
| **PRIMARY — metrics** | The fund publishes metrics/process guidance but no deck structure. Quotable for the metric, **not** for a slide requirement. |
| **SECONDARY** | This skill's inference from the fund's publicly stated themes. **Must be labelled as inference in every audit output.** |
| **UNVERIFIED** | No primary source located. Attribute nothing to the fund. |

### How to read the emphasis sets

- `AC-nn` refers to [`acceptance-criteria.md`](acceptance-criteria.md).
- `×3` = heavy weight, `×2` = moderate. Fund Fit is computed over this set only;
  see [`scoring-framework.md`](scoring-framework.md) §3.
- **An emphasis set is never a claim that the fund requires a slide.** It is a
  statement about which criteria dominate the fund's public reasoning.

---

## Tier 1 — PRIMARY: fund publishes an ordered deck structure

### Sequoia Capital — `PRIMARY — structure`

- **Stage & vehicle** — Seed through growth; states a preference for partnering
  **early**: *"we love to partner early — when an idea is newly formed and has the
  maximal room to grow"* [2]. Also runs **Arc** (whose page publishes no deck
  guidance).
- **Published structure** — ten sections: company purpose, problem, solution,
  **why now**, market potential, competition / alternatives, business model, team,
  financials, vision [2].
- **Emphasis set** — `AC-01 ×3` (single declarative sentence), `AC-05 ×3` (why
  now), `AC-03 ×2`, `AC-10 ×2`, `AC-11 ×2`, `AC-20 ×2` (competition with a plan to
  win), `AC-24 ×2`.
- **Punishes** — feature lists instead of mission (*"It's easy to get caught up
  listing features instead of communicating your mission"* [2]); a why-now that is
  actually a why (*"Nature hates a vacuum—so why hasn't your solution been built
  before now?"* [2]); a competition slide with no plan to win [2].
- **Version warning** — the 2015 SlideShare version of this template had a
  **Product** section; the current order **replaced Product with Vision**. Do not
  tell a founder Sequoia requires a Product slide.
- **Fit gate** — Sequoia frames the template as a container for thinking: *"it
  wasn't really the slides we liked—it was their ideas, the clarity of their
  thinking, and the scope of their ambition"* [2]. A deck that reproduces the ten
  sections without a defensible insight is a fit failure that no criterion fully
  captures. Score AP-01 and the vision slide manually for Sequoia.
- **Ambition scope** — Sequoia is permissive on new categories: *"Some of the best
  companies invent their own markets"* [2]. This directly contradicts 500 Global's
  hard > $1B floor (below) and is a real disagreement.

### Y Combinator — `PRIMARY — structure`

Three separate artifacts. **Confusing them is itself an error.**

| Artifact | Shape | Source |
| :--- | :--- | :--- |
| **Seed read-ahead deck** | 11 slides: title, problem, solution, traction, more metrics, insight, business model, market, team, ask | [1] |
| **Series A deck** | one-liner, problem, solution, traction (several slides), market, competition, vision, team, use of funds, appendix | [7] |
| **Demo-day / presented deck** | 5–7 slides, 2 min 30 s, one idea per slide | [3] |

- **Stage & vehicle** — YC funds at idea stage (*"40% of our companies joined with
  just an idea"* [1]); standard deal; also runs a Series A program.
- **Emphasis set (seed / application)** — `AC-01 ×3`, `AC-03 ×3`, `AC-06 ×3`
  (problem + solution + **insight** [9]), `AC-13 ×3`, `AC-16 ×3`, `AC-22 ×3`,
  `AC-23 ×2`, `AC-10 ×2`.
- **Emphasis set (Series A)** — `AC-13 ×3`, `AC-15 ×3`, `AC-14 ×3` (annotated
  trends), `AC-18 ×3`, `AC-19 ×2`, `AC-20 ×2`, `AC-28 ×3` (appendix), `AC-06 ×2`.
- **Punishes** — advisors on the team slide (*"This should be about founders.
  Nobody cares about your advisors."* [1]); feature lists and raw screenshots over
  customer outcomes [7]; **cumulative numbers** and **double-axis graphs** (AP-41,
  AP-42) [7]; diagrams and decorative images [7]; decks with no ask (*"weirdly,
  I've seen many decks without one"* [7]); listing existing investors' logos on the
  team slide (signalling risk) [7].
- **Fit gates from YC's own words:**
  - **Insight is required, not optional.** YC's idea unit is **problem + solution +
    insight**: *"what we call an insight that will show why your company will grow
    faster than other companies"* [9]. AP-01 is a fit gate, not a polish item.
  - **At least 4–6 months of trend** before growth is believable; a monthly or
    quarterly graph beats a summed annual number; the 18–24 month seed→Series A
    timeline is the assumed horizon [7].
  - **Bottoms-up market sizing** is the default: *"number of prospective customers x
    value of each customer to you"* [7].
  - **Reproducibility test:** a listener should be able to repeat three nouns — what
    you're making, the problem, the customer [9].
  - **X-for-Y has three tests:** X must be a household name; Y must want X; Y must
    be huge. YC's counter-example: *"Buffer for Snapchat. Buffer is a nice company,
    but definitely smaller than Snapchat."* [9]
  - **Speed of execution is a live variable:** *"the longer they've been around, the
    more they have to have done"* [7]. Traction slides should carry elapsed time.
- **Dead-linked benchmarks** — YC's Series A guide links two internal benchmark
  pages that now return **HTTP 404**. YC's numeric ARR/growth thresholds are
  therefore **not stated in this skill**.

### Antler — `PRIMARY — structure`

- **Stage & vehicle** — Pre-seed and day-zero. Antler invests at company formation
  and runs a global residency.
- **Published structure** — **10 slides**, and the writer explicitly notes *"the
  order doesn't matter; your storytelling does"* [8]: problem · solution · market ·
  traction · business model · competition · **go-to-market** · team · financials ·
  ask. **There is no company-purpose slide; it opens on the problem.**
- **Emphasis set** — `AC-03 ×3`, `AC-10 ×3`, `AC-04 ×2`, `AC-16 ×3`, `AC-17 ×2`,
  `AC-20 ×3`, `AC-22 ×3`, `AC-24 ×3`.
- **Punishes** — the generic problem (*"'Small businesses struggle with cash flow'
  is not a problem."* [8]); top-down sizing (*"one of the fastest ways to lose
  credibility… 'we are targeting a $50 billion market and just need 1% of it'. It
  means nothing."* [8]); "we have no competition" (*"Nothing makes an investor more
  suspicious"* [8]); a fake 2×2 with you alone in the top right [8]; *"'We'll use
  social media, content marketing and partnerships' is not a GTM strategy."* [8];
  "we'll figure out monetisation later" [8]; credential lists instead of a
  why-this-team narrative [8].
- **Fit gates from Antler's own words:**
  - **Problem standard — the strictest in this file:** *"One specific problem, felt
    by one specific person, in one specific moment"*, with a person, a moment, and a
    cost named [8]. AC-03 and AP-05 are the gates.
  - **Market: bottom-up only** [8].
  - **Ask: milestones that de-risk the next round specifically.** *"'Hire 3
    engineers and build the product' is not a milestone."* [8]
  - **Pre-seed traction is broader than revenue:** LOIs, pilots, waitlists,
    interviews, prototypes — *"Even ten customer conversations with documented
    insights is traction."* [8]
- **Pre-seed reality check (Antler's own framing)** — *"Investors at this stage are
  not betting on your traction. They are betting on you."* The biggest red flag they
  name: *"a team that has spent six months building without talking to a single
  potential customer. Conviction isn't evidence."* [8]
- **Caveat** — published on Antler's marketing blog, first-person from one investor.
  Antler is an accelerator, not a top-decile US venture fund. Its value here is the
  specificity of the pre-seed problem standard.

### 500 Global — `PRIMARY — structure`

- **Stage & vehicle** — Pre-seed/seed accelerator and fund. Publishes a free deck
  template.
- **Published structure** — **≤ 10 slides**: logo + elevator pitch · problem ·
  solution · how it works · traction · business model · competition · market
  opportunity · **progress to date** · team [13]. They state: *"We typically only
  spend a few minutes reviewing each deck."*
- **Emphasis set** — `AC-01 ×3`, `AC-03 ×2`, `AC-13 ×2`, `AC-17 ×2`, `AC-20 ×2`,
  `AC-22 ×2`, `AC-24 ×2`.
- **Reusable copy formulas they publish** [13]:
  - *"A [product type] to help [target customer] with [#1 problem] by [#1 benefit]
    using our [secret sauce/differentiator]."*
  - *"Unlike [existing alternatives], [your product] [primary differentiator] and
    [secondary differentiator]."*
- **Fit gate** — a hard market floor of **> $1B**, or a credible expansion plan to
  reach it [13]. This is **stricter than Sequoia** and is a genuine disagreement,
  not a nuance.
- **Punishes** — *"saying you're the 'first' to do something often shows a lack of
  knowledge about your space"* [13]; excessive text and images; jargon.

### Techstars — `PRIMARY — anti-template`

- **Stage & vehicle** — Pre-seed, idea to early traction; 13-week programme.
- **Published position** — Techstars publishes the **opposite** advice to everyone
  else, and it is worth taking seriously because it attacks the failure mode AP-01
  describes: *"A lot of people make the mistake of it being a paint-by-numbers
  exercise that something on the internet told them. Here's what 10 slides you
  should have."* [12]
- **Their prescription** [12]:
  1. **Write the long-form script first**, then build slides to fit the story.
  2. **No fixed order** — *"Sometimes the team should be first."*
  3. Anchor on a **big future vision** plus **concrete recent momentum**, where
     momentum is explicitly not only revenue: *"When we say momentum, we don't
     always mean revenue and user traction."*
  4. **Text density rule**: *"People will listen, or they will read. They will not
     do both."* Dense content goes to the appendix.
- **Emphasis set** — `AC-01 ×3`, `AC-22 ×3`, `AC-13 ×3` (momentum, broadly defined),
  `AC-03 ×2`, `AC-16 ×2`, `AC-28 ×2`.
- **Implication for the audit** — a deck with no template compliance but a script, a
  vision, and dated momentum is **not deficient**. The audit scores criteria, not
  structural conformity.
- **Outreach anti-patterns (T1, not deck-specific)** [12] — non-personalised cold
  email; six-paragraph emails (*"ends up in the trash"*); email blasting; **false
  urgency** (*"immediate red flag for us"*); **AI mass personalisation** (*"In the
  age of agents and LLMs… Don't do it. We can tell when it comes as a mass blast."*).

---

## Tier 2 — PRIMARY (metrics only): quotable for metrics, not for slides

### a16z (Andreessen Horowitz) — `PRIMARY — metrics; NO deck structure`

- **Stage & vehicle** — Seed through growth; leads priced rounds. Vertical funds
  (AI, enterprise, consumer, bio, crypto, American Dynamism) plus **Speedrun** for
  very early companies.
- **Critical correction:** **a16z publishes no canonical public deck template.** A
  full sitemap sweep of 744 a16z.com URLs found no deck article;
  `a16z.com/how-to-build-a-pitch-deck/` returns HTTP 404. **The phrase "what is the
  secret" is not an a16z criterion** — it does not appear on any a16z page located
  in this research. Attributing it to a16z is a fabrication.
- **What a16z does publish, and how it filters:** **metric vocabulary.** a16z
  evaluates decks through definitions, which is a different filter from slide order
  [6b]:
  - *"A common mistake is to use bookings and revenue interchangeably… Letters of
    intent and verbal agreements are neither revenue nor bookings."*
  - **Paid CAC must be distinguished from blended CAC.**
  - Use **CMGR**, not a simple-average MoM growth rate.
  - **LTV must be net profit** — not revenue, not gross margin.
  - **3× LTV:CAC is a16z's own stated rough benchmark:** *"Investors often use 3x
    LTV/CAC as a rough benchmark… improving your LTV/CAC from 2x to 3x can nearly
    triple your valuation."*
  - **Capital-to-milestone alignment:** *"regardless of what a round is called
    (seed, series A, B, C, etc.), it's all about the alignment of capital to
    milestones."*
  - **A deck is mandatory:** *"Do I really need to prepare a full slide deck? …
    Don't leave anything to chance. Take time to prepare a full deck and practice,
    including creating a script and doing dry-runs."*
- **Also primary, on process** [6]: burn multiple (cash burned ÷ net ARR added);
  distinguish **burn-sinks from burn-investments** with a stated rationale; be
  *"deliberate and precise on use of proceeds"*; do not open conversations with
  price expectations (AP-32); *"ask yourself the difficult questions"* — anticipate
  retention and CAC objections (P-13).
- **Emphasis set** — `AC-18 ×3` (unit economics **with definitions**), `AC-19 ×3`
  (burn multiple / capital efficiency), `AC-25 ×3` (metric integrity: no
  bookings-as-revenue), `AC-17 ×2`, `AC-24 ×3` (capital-to-milestone), `AC-10 ×2`,
  `AC-11 ×2`, `AC-21 ×2`.
- **Fit gates** — a deck with no efficiency metric, an undefined CAC or LTV, a
  blended CAC presented as channel CAC, or a use-of-funds slide with no milestone
  attached has no answer to a16z's stated questions.
- **Existence proof** — the a16z Games Fund One deck was published with GP Andrew
  Chen's commentary: industry context → **"why now" slide** → investment areas →
  team/operating model. **Secondary** for structure; useful as a live example, not a
  template.
- **Caveat** — the two metrics pieces are from **2015**. Definitions aged well;
  round-timing content did not. The 16 Commandments is from **May 2023**; the
  structural advice is durable, the market framing dated.

---

## Tier 3 — SECONDARY: inference only, must be labelled

For every fund below, **no canonical public deck structure was located.** The
emphasis sets are this skill's inference from the fund's publicly stated investment
themes. **Every audit output that uses one of these profiles must label it as
inference.**

### Bessemer Venture Partners — `SECONDARY` (research is primary)

- **Stage & vehicle** — Seed through growth; cloud, consumer, healthcare, deep tech.
- **Emphasis set (inferred)** — `AC-15 ×3` (net revenue retention and cohorts),
  `AC-18 ×3`, `AC-19 ×3` (cloud efficiency), `AC-17 ×2`, `AC-13 ×2`.
- **Basis** — Bessemer publishes cloud-efficiency frameworks (net revenue
  retention, burn multiple, CAC ratio, magic number, gross margin) and memos [15].
  A sitemap check of bvp.com returns only memos and roadmaps.
- **Explicit correction** — the "**Bessemer pitch deck template**" circulating
  online **is not a bvp.com artifact.** Do not present it as Bessemer's.

### Greylock — `SECONDARY / UNVERIFIED`

- **Emphasis set (inferred)** — `AC-13 ×3`, `AC-15 ×3`, `AC-18 ×3`, `AC-19 ×3`,
  `AC-10 ×2`.
- **Basis** — widely reported Series A readiness material oriented to the seed →
  Series A transition. **The frequently cited Greylock presentation is Business
  Insider reporting (2021, paywalled), not a Greylock publication** [16].
- **Do not** attribute specific slide requirements to Greylock.

### First Round Capital — `SECONDARY` (process is primary)

- **Stage & vehicle** — Seed and early Series A.
- **What is actually primary** [16] — First Round publishes **no deck-structure
  guide and no teardown series** (the "pitch deck teardown" franchise is
  **TechCrunch's**). What it does publish is a **2024 partner-meeting piece**:
  - A partner meeting is **60 minutes with 5–15 investors** (vs 30–45 min for 1:1).
  - *"for partner meetings, it is almost always recommended to come with slides"*,
    plus *"a large appendix of slides for your eyes only."*
  - Offer rate **25–60%** after a partner meeting, versus roughly **5%** conversion
    after a 1:1.
  - The **investment memo** the partner writes has these sections: founder
    backgrounds · market overview and problem · solution/product · big vision · GTM ·
    traction · team · competitive landscape.
  - A 2015 storytelling piece recommended **12 slides** and *"Lay out the map for
    them at the beginning"* — **dated, and not re-endorsed in 2024.**
- **Emphasis set (inferred)** — `AC-22 ×3` (founder backgrounds are the first memo
  section), `AC-03 ×2`, `AC-06 ×2`, `AC-13 ×2`, `AC-28 ×3` (the appendix, which
  First Round names explicitly).
- **Strongest usable insight** — because the partner writes an **investment memo**
  with a named section list, the deck should make each of those eight sections
  trivially extractable.

### Founders Fund — `SECONDARY / UNVERIFIED`

- **Emphasis set (inferred)** — `AC-21 ×3` (monopoly/defensibility), `AC-05 ×3`,
  `AC-06 ×3` (a non-consensus belief), `AC-17 ×2`, `AC-11 ×2`.
- **Basis** — Founders Fund's public positioning descends from Thiel's contrarian
  framework. **No primary deck guidance was located.** Do not attribute slides.

### Index Ventures — `SECONDARY / UNVERIFIED`

- **Emphasis set (inferred)** — `AC-22 ×2`, `AC-10 ×2`, `AC-17 ×2`.
- **Basis** — Index publishes *Rewarding Talent*, *Winning in the US* (which has a
  fundraising chapter), and *Scaling Through Chaos*. Deck tips attributed to Index
  come from **Pitch.com and Business Insider**, not from Index [17].

### Lightspeed — `SECONDARY / UNVERIFIED`

- **Emphasis set (inferred)** — `AC-07 ×2` (product visual), `AC-13 ×2`.
- **Basis** — the closest primary-adjacent item is a **TechCrunch** interview about
  Grafana's Series A deck. Usable detail: the slide that moved the partnership was
  a **visual** showing dashboards at recognisable brands — *"That just emotionally
  resonates with people when you're thinking about investing in a company."* [17]

### Accel, Redpoint, Benchmark, Coatue, Insight Partners — `UNVERIFIED`

- **No primary deck guidance located.** Sitemap sweeps and targeted fetches found
  nothing on the fund domains. The Insight Partners page that exists
  (a fundraising-meeting guide) **did not render past a cookie wall**, so its
  contents are unverified.
- **Fallback:** for these funds, use the **global weighting** in
  [`scoring-framework.md`](scoring-framework.md) and say so. **Do not invent an
  emphasis set.**

---

## Stage → Fund Fit Routing

Use this to avoid the stage-mismatch hard stop (AP-34).

| Stage | Funds that actually lead at this stage | Critical evidence required |
| :--- | :--- | :--- |
| **Idea / pre-company** | YC, Antler, Techstars, 500 Global, Speedrun (a16z) | Founder-market fit, insight, problem specificity. Revenue is not expected. |
| **Pre-seed** | Antler, YC, Speedrun, First Round, angels | Problem specificity, insight, LOIs/pilots/design partners, 18–24 month model |
| **Seed** | a16z seed, Sequoia (early), First Round, Index, Accel, Lightspeed, Bessemer, Greylock, Founders Fund | Traction or strong pre-revenue demand, bottom-up market, unit economics (modelled acceptable), the ask |
| **Series A** | All of the above plus growth funds | $1–3M+ ARR, **4–6 months of trend**, cohort retention, actual unit economics, burn multiple, appendix depth |

**Rule:** if the deck's stage claim and the fund's stage do not overlap, that is a
`FAIL` on AC-23 and a hard stop. Do not send it and hope.

---

## The Fund-Fit Output Format

For each target fund, produce exactly this:

```markdown
### <Fund> — Fund Fit: XX% (verdict: send / warm only / do not send)

- **Evidence tier:** PRIMARY (structure) | PRIMARY (metrics) | SECONDARY | UNVERIFIED
- **Stage match:** <yes/no, with the round and vehicle>
- **Strong on:** <AC IDs the deck already satisfies for this fund>
- **Blocking gap:** <the single criterion that most suppresses fit>
- **Variant changes:** <slide reorder, emphasis, framing line>
- **Do not send if:** <the hard gap, if any>
```

If a target fund is `SECONDARY` or `UNVERIFIED`, the output **must** say so in the
Evidence tier line. If a fund has no published emphasis, use the global weighting
and state that explicitly.

If the founder's target list includes a fund the deck cannot satisfy without
inventing evidence, the correct output is: **state the gap, do not build the
variant.**

---

## Honesty Rules for This File

1. **Never quote a `SECONDARY` or `UNVERIFIED` profile as if it were the fund's own
   instruction.** Label it in the audit output.
2. **Never invent a fund's emphasis set.** If a fund's emphasis is unknown, say
   "no published emphasis found" and fall back to the global weighting.
3. **Never claim a fund uses a template it does not publish.** a16z, Bessemer,
   Index, Accel, Lightspeed, Greylock, Redpoint, Founders Fund, Benchmark, Coatue,
   First Round, and Insight Partners have **no** canonical public deck structure.
4. **Never attribute "what is the secret" to a16z**, or "pitch deck teardowns" to
   First Round. Both are misattributions documented in
   [`sources-and-attribution.md`](sources-and-attribution.md).
5. **Fund emphasis changes.** This file records what was published at the retrieval
   date. A founder pitching in a later cycle should re-verify anything load-bearing.
