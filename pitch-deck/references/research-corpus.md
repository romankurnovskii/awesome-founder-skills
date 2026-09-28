# How Top-Tier Funds Actually Evaluate Pitch Decks

**Research report — primary-source survey of fund-published deck guidance**

Method note: 30+ URLs fetched, prioritising fund-owned domains (a16z.com, ycombinator.com, sequoiacap.com, bvp.com, antler.co, techstars.com, 500.co, a16zcrypto.com, review.firstround.com, docsend.com) plus two independent tracking datasets (Papermark, Storydoc) and one academic survey (NBER). Every claim is tagged:

- **[FUND-VERBATIM]** — the fund's own published words
- **[DATASET]** — measured/statistical
- **[SECONDARY]** — third-party reporting/interpretation of a fund
- **[UNVERIFIED]** — could not confirm against a primary source; treat as a lead, not a fact

---

## 0. Headline finding: the "every fund has a deck template" premise is mostly false

Only **three** of the funds named in the brief publish an explicit, ordered, slide-by-slide deck structure on their own domain:

| Fund | Canonical deck structure published? | Primary source |
|---|---|---|
| **Sequoia** | **Yes** — 10 sections, ordered, explicitly labelled "our guide to pitching" | [sequoiacap.com/article/writing-a-business-plan](https://sequoiacap.com/article/writing-a-business-plan/) |
| **Y Combinator** | **Yes** — two of them (seed template + Series A template), plus a design essay | [library/2u](https://www.ycombinator.com/library/2u-how-to-build-a-pitch-deck) · [library/8d](https://www.ycombinator.com/library/8d-how-to-build-a-great-series-a-pitch-and-deck) · [library/4T](https://www.ycombinator.com/library/4T-how-to-design-a-better-pitch-deck) |
| **DocSend (not a fund)** | **Yes** — two ordered structures, pre-seed and seed, with section-level time benchmarks | [pre-seed](https://www.docsend.com/blog/what-to-include-when-building-your-pre-seed-pitch-deck/) · [seed](https://www.docsend.com/blog/what-vcs-really-want-to-see-inside-your-seed-deck/) |

Funds with **no findable canonical deck structure on their own domain**: **a16z**, **Bessemer**, **Index Ventures**, **Accel**, **Lightspeed**, **Greylock**, **Redpoint**, **Founders Fund**, **Benchmark**, **Coatue**, **Insight Partners**, **First Round**.

This matters enormously for the deliverable. The pages that appear in search results as "Accel/Founders Fund/Bessemer — How to Pitch (2026)" are content-farm SEO pages (e.g. `foundra.ai/vc/accel`, `vcmatch.ai/investors/bessemer-venture-partners`), **not fund-published guidance**. Do not cite them as fund positions. **[SECONDARY]**

Two concrete negative findings worth recording:

- **First Round Review has no "pitch deck teardown series."** A full sitemap sweep of `review.firstround.com/sitemap-posts.xml` returns only four deck-related posts, none of which is a teardown or a deck-structure guide: [dont-ship-your-pitch-deck-to-your-website](https://review.firstround.com/dont-ship-your-pitch-deck-to-your-website/), [how-to-adapt-your-pitch-deck-into-your-website](https://review.firstround.com/how-to-adapt-your-pitch-deck-into-your-website/), [building-your-best-sales-deck-starts-here](https://review.firstround.com/building-your-best-sales-deck-starts-here/), [this-culture-deck-powers-the-worlds-toughest-work](https://review.firstround.com/this-culture-deck-powers-the-worlds-toughest-work/). "Pitch deck teardown" is a **TechCrunch** franchise, not a First Round one.
- **a16z has no pitch-deck page.** A full sweep of `a16z.com/post-sitemap{,2,3}.xml` and `page-sitemap.xml` (744 URLs) for `pitch|deck|fundrais|narrative|story` surfaces no deck-template article. `a16z.com/how-to-build-a-pitch-deck/` returns HTTP 404.

---

## 1. Canonical slide-by-slide structures, per source

### 1.1 Sequoia — the canonical 10-section company plan **[FUND-VERBATIM]**

Source: [sequoiacap.com/article/writing-a-business-plan](https://sequoiacap.com/article/writing-a-business-plan/)

Sequoia frames this as "our guide to pitching below (with a few refinements from years of use)" and introduces it with the Airbnb origin story. Their own framing of what mattered is important:

> "But it wasn't really the slides we liked — it was their ideas, the clarity of their thinking, and the scope of their ambition."

Order, verbatim section names:

1. **Company purpose** — "define your company in a single declarative sentence. This is harder than it looks."
2. **Problem** — "Describe the pain of your customer. How is this addressed today and what are the shortcomings to current solutions."
3. **Solution** — "Explain your eureka moment. Why is your value prop unique and compelling? Why will it endure? And where does it go from here?"
4. **Why now?** — "The best companies almost always have a clear why now? Nature hates a vacuum—so why hasn't your solution been built before now?"
5. **Market potential** — "Identify your customer and your market. Some of the best companies invent their own markets."
6. **Competition / alternatives** — "Who are your direct and indirect competitors. Show that you have a plan to win."
7. **Business model** — "How do you intend to thrive?"
8. **Team** — "Tell the story of your founders and key team members."
9. **Financials** — "If you have any, please include." *(note the deliberate hedge)*
10. **Vision** — "If all goes well, what will you have built in five years?"

**Discrepancy worth flagging.** The widely-circulated older Sequoia template (reproduced on SlideShare, referencing the now-dead `sequoiacap.com/grove/posts/6bzx/writing-a-business-plan`) has a **different** section list and includes a **Product** section that the current page omits:

> Older order: Company Purpose → Problem → Solution → Why Now → Market Size → Competition → **Product** → Business Model → Team → Financials

The older version also carried sub-bullets the current page dropped: for Market Size, "Calculate the TAM (top down), SAM (bottoms up) and SOM"; for Product, "Show where your product physically sits"; for Business Model, "Average account size and/or lifetime value, Sales & distribution model, Customer/pipeline list"; for Financials, "P&L, Balance sheet, Cash flow, Cap table, The deal." The SlideShare artifact is a **third-party reproduction** by "PitchDeckCoach," not a Sequoia upload — label it **[SECONDARY]** at [slideshare.net/slideshow/sequoiacapitalpitchdecktemplate/46231251](https://www.slideshare.net/slideshow/sequoiacapitalpitchdecktemplate/46231251).

Net: **Sequoia's current canonical order replaces "Product" with "Vision."** Any guide still showing Sequoia's ten slides as "…Competition → Product → Business Model…" is quoting the pre-2018 version.

Sequoia's Arc programme ([sequoiacap.com/arc](https://www.sequoiacap.com/arc/)) is a bi-annual open call for pre-seed/seed, but the Arc page publishes **no deck format** — it sells the four-day "Arc Intensive" and the network. No deck guidance there.

### 1.2 Y Combinator — three separate artifacts

**(a) Seed deck template — Aaron Harris, 2018 [FUND-VERBATIM]**
Source: [ycombinator.com/library/2u-how-to-build-a-pitch-deck](https://www.ycombinator.com/library/2u-how-to-build-a-pitch-deck)

Framing line: *"Focus on narrative. The rest is commentary."* and *"founders should strive for clarity and concision… The simple truth is that there isn't very much meaningful detail to explore for most seed stage companies. When founders pretend that there is, their stories get muddled, and the investors get lost."*

Order: Title (name + one-line description) → Problem → Solution → **Traction** → **More metrics** → **Insight** ("what makes you so special, what makes this work, what your insights are… might take more than one slide") → Business model → Market → Team → Ask.

Two structural rules stated explicitly: the title/one-liner is the only section allowed exactly **one** slide; every other section is "the first slide of a set," ideally n=1, and "You probably don't want any set here where n > 3. This is a seed deck, remember." Also: *"Team! So important at seed… This should be about founders. Nobody cares about your advisors."*

**(b) Series A deck — YC Series A Program [FUND-VERBATIM]**
Source: [ycombinator.com/library/8d-how-to-build-a-great-series-a-pitch-and-deck](https://www.ycombinator.com/library/8d-how-to-build-a-great-series-a-pitch-and-deck)

Order with slide counts as YC states them:

| # | Section | YC's own slide count |
|---|---|---|
| 1 | Company one-liner / description (lead with traction) | 1 |
| 2 | **Problem** | 1 |
| 3 | **Solution** | 1 |
| 4 | **Traction** | "in-depth, a few slides" |
| 5 | **Market** | 1 |
| 6 | **Competition** | 1 |
| 7 | **Vision** ("Show how you become a $10B company") | 1 |
| 8 | **Team** | 1 |
| 9 | **Use of Funds** | 1 |
| 10 | **Appendix** | "as many slides as necessary" |

Crucial conditional YC adds: *"If your team is one of your comparative advantages, then this should be your second or third slide."* YC defines a comparative advantage as (i) a successful prior exit (>$100M), or (ii) being "one of the few people in the world uniquely equipped to start this company" (biotech/hardtech). Note YC explicitly keeps Vision **after** traction and competition — the opposite of Sequoia, which puts Vision last but frames it as the five-year endpoint.

**(c) Design essay — Kevin Hale, 2016 [FUND-VERBATIM]**
Source: [ycombinator.com/library/4T-how-to-design-a-better-pitch-deck](https://www.ycombinator.com/library/4T-how-to-design-a-better-pitch-deck)

Not a structure, a filter: **legible → simple → obvious**. Explicit numbers: *"Demo Day slides ideally have only about 5-7 slides"*; Demo Day slot is *"2 minutes and 30 seconds"*; *"Since you only have 5-7 ideas you want to get across to investors, you shouldn't have too many slides."* The obviousness test: *"Show it to a stranger and ask them to tell you what it means. If they don't immediately say your idea, you lose."*

**(d) "How to pitch your startup" — Hale talk [FUND-VERBATIM]**
Source: [ycombinator.com/library/6q-how-to-pitch-your-startup](https://www.ycombinator.com/library/6q-how-to-pitch-your-startup)

This is the clearest statement of YC's underlying idea-unit. A startup idea = **Problem + Solution + Insight**, where insight = "something that's gonna make your company unique and have some kind of unfair advantage." The evaluative questions a YC partner asks are stated verbatim: *"Do I understand it? Am I excited by it? Do I like the team and do I wanna work with them?"* Also: *"you're looking at about five to six points that are really, really great about your company, maybe the investor will remember one or two of them. One of them has to be remembering what you do."*

### 1.3 DocSend — two ordered structures with per-section time **[DATASET]**

**(a) Pre-seed — 18 pages / 12 sections** ([docsend.com/blog/what-to-include-when-building-your-pre-seed-pitch-deck](https://www.docsend.com/blog/what-to-include-when-building-your-pre-seed-pitch-deck/), updated Feb 2026; originally Mar 2022)

DocSend claims "the highest engagement and conversion rates" for this order, though it does not disclose the conversion differential:

| # | Section | Target pages | Measured avg pages | **VC time** |
|---|---|---|---|---|
| 1 | Company purpose | 1 | 1.3 | 33 s |
| 2 | Problem | 1–2 | 2.15 | 39 s |
| 3 | Solution | 1–2 | 1.5 | 27 s |
| 4 | **Why now?** (optional) | 1 | 1.5 | 38 s |
| 5 | **Product** — labelled "HIGHLY SCRUTINIZED" | 3–4 | 3.3 | **77 s (longest)** |
| 6 | Market size | 1 | 1.7 | 39 s |
| 7 | Team | 1–2 | 1.5 | 46 s |
| 8 | **Business model** — labelled "MOST SCRUTINIZED" | 2–3 | 2.8 | **83 s (longest)** |
| 9 | Traction | 1–4 | — | 37 s |
| 10 | Financials (optional) | 1–2 | — | 40 s |
| 11 | Competition | 1 | — | 55 s |
| 12 | Fundraising ask | 1 | — | 40 s |

Note the internal inconsistency: DocSend labels **both** Product (77 s) and Business model (83 s) as "LONGEST!" — the business model section is genuinely the longest, and the Product "LONGEST!" callout is a copy artefact. Flag it.

Also note DocSend's ordering of pre-seed puts **Team at #7 and Business model at #8, with Competition at #11** — quite different from the seed order below and from Sequoia.

**(b) Seed — 19–20 pages / 12 sections** ([docsend.com/blog/what-vcs-really-want-to-see-inside-your-seed-deck](https://www.docsend.com/blog/what-vcs-really-want-to-see-inside-your-seed-deck/), updated Mar 2026; originally May 2022)

1. Company purpose (26 s) · 2. Problem (34 s) · 3. Solution (34 s) · 4. **Market size** · 5. **Why now?** ("optional but increasingly important," 23 s) · 6. Product (59 s) · 7. Competition (34 s) · 8. Traction (40 s) · 9. Team (38 s) · 10. Business model (64 s) · 11. Financials ("optional but recommended," 37 s) · 12. Fundraising ask (32 s)

DocSend's strongest single ordering claim, verbatim: *"Founders who open their decks with the first four sections above are more likely to raise funding than those who opt for other approaches."* The first four at seed = Company purpose, Problem, Solution, Market size. **That is a different first-four than pre-seed** (purpose, problem, solution, why now). This is an inconsistency in DocSend's own guidance across pages and is a legitimate place to flag disagreement.

### 1.4 Antler — pre-seed, 10 slides **[FUND-VERBATIM]**

Source: [antler.co/blog/what-a-vc-wants-to-see-in-your-pitch-deck](https://www.antler.co/blog/what-a-vc-wants-to-see-in-your-pitch-deck)

*"Keep it to 10 slides. A founder who can tell a compelling story in 10 slides has already proven something important: they know what matters."*

Order: 1 Problem · 2 Solution · 3 Market · 4 Traction · 5 Business model · 6 Competition · 7 Go-to-market · 8 Team · 9 Financials · 10 Ask.

Two notable deviations from everyone else: **no company-purpose slide** (it starts on the problem) and a **dedicated GTM slide at #7**. Antler explicitly relaxes order: *"The order doesn't matter; your storytelling does, and the deck should be there just to support your story… sometimes I see founders putting the team slide as the first one."* Each slide is paired with "What the VC is thinking" — e.g. on the problem slide: *"Do I believe this problem is real and painful enough that someone would pay to solve it?"*

### 1.5 Techstars — deliberate anti-template **[FUND-VERBATIM]**

Source: [techstars.com/blog/founder-advice/why-most-pitch-decks-dont-work-and-how-to-make-sure-yours-does](https://www.techstars.com/blog/founder-advice/why-most-pitch-decks-dont-work-and-how-to-make-sure-yours-does) (Tim Grace & Gabrielle Rudd, Techstars Columbus)

Techstars is the only source in this survey that **explicitly attacks the template approach**: *"A lot of people make the mistake of it being a paint-by-numbers exercise that something on the internet told them. Here's what 10 slides you should have in the slide deck."* Their prescription is to write long-form first: *"The best way, in my opinion… is just to write out the story like a script… And then once you have that, it's easier to then take a look at that and construct the slides to fit that."* And on order: *"Sometimes the team should be first… because it's an incredibly personal thing."*

No fixed order. Their content anchors are: **big future vision** ("What does the world look like when that has happened?") plus **concrete recent momentum** — with the specific instruction that momentum ≠ revenue: *"When we say momentum, we don't always mean revenue and user traction."* Their example of good specificity: *"In 87 days, they've integrated six services… tracking 500,000 artists… 130 million fan interactions."*

### 1.6 500 Global — 10 slides, with a published template **[FUND-VERBATIM]**

Sources: [latam.500.co/content/pitch-perfect-…](https://latam.500.co/content/pitch-perfect-how-to-make-a-standout-pitch-deck-for-500-global) and [ee.500.co/content/this-pitch-deck-will-rock-your-500-global-application](https://ee.500.co/content/this-pitch-deck-will-rock-your-500-global-application) (the two are near-identical content on different regional domains)

*"We typically only spend a few minutes reviewing each deck… A well-crafted pitch deck doesn't need more than 10 slides."*

1. Logo & elevator pitch · 2. Problem · 3. Solution · 4. **How it works** · 5. Traction · 6. Business model · 7. Competition · 8. Market opportunity · 9. **Progress to date** · 10. Team

500 Global is the only source here that supplies a **fill-in-the-blank pitch formula**: *"A [product type] to help [target customer] with [#1 problem] by [#1 benefit] using our [secret sauce/differentiator]."* And a competition formula: *"Unlike [existing alternatives], [your product] [primary differentiator] and [secondary differentiator]."* They also publish a free Google Slides template (linked from the article).

Their market-size bar is explicit and numeric: *"there should be either a market size of >$1B or an expansion plan that will get there."*

### 1.7 Comparison of the ordered structures

| Position | Sequoia | YC Series A | YC seed | DocSend seed | DocSend pre-seed | Antler | 500 Global |
|---|---|---|---|---|---|---|---|
| 1 | Company purpose | One-liner | Title/one-liner | Company purpose | Company purpose | **Problem** | Logo + elevator pitch |
| 2 | Problem | Problem | Problem | Problem | Problem | Solution | Problem |
| 3 | Solution | Solution | Solution | Solution | Solution | Market | Solution |
| 4 | Why now? | **Traction** | **Traction** | **Market size** | Why now? | Traction | How it works |
| 5 | Market potential | Market | More metrics | Why now? | **Product** | Business model | **Traction** |
| 6 | Competition | Competition | **Insight** | **Product** | Market size | Competition | Business model |
| 7 | Business model | **Vision** | Business model | Competition | Team | Go-to-market | Competition |
| 8 | Team | Team | Market | Traction | Business model | Team | Market opportunity |
| 9 | Financials | Use of funds | Team | Team | Traction | Financials | **Progress to date** |
| 10 | Vision | Appendix | Ask | Business model | Financials | Ask | Team |
| 11 | — | — | — | Financials | Competition | — | — |
| 12 | — | — | — | Fundraising ask | Fundraising ask | — | — |

**Where the sources genuinely disagree:**

1. **Where traction goes.** YC puts traction at slide 4 in *both* its templates, and for seed puts it before metrics/insight/business model. DocSend puts traction at **#8 of 12** at seed and **#9 of 12** at pre-seed. Antler puts it at #4; 500 Global at #5. This is the single largest structural disagreement in the corpus.
2. **Whether "Product" and "Why now" are separate slides.** DocSend separates them (Why now #5, Product #6 at seed). Sequoia has Why now (#4) but no Product slide. YC Series A has neither as a named section — product content is folded into Solution.
3. **Where Vision goes.** Sequoia puts it last (#10). YC Series A puts it at #7 (after competition, before team). YC seed has no vision slide at all — Insight (#6) is the closest analogue. Antler has neither.
4. **Whether Market comes before or after why-now.** Sequoia and DocSend-seed: market before why-now… actually Sequoia is why-now (#4) → market (#5); DocSend seed is market (#4) → why-now (#5). Directly opposed.
5. **The opening slide.** Sequoia/DocSend/YC/500 open with company purpose. Antler opens with the problem. Techstars says order is irrelevant.

---

## 2. Narrative arc patterns

**Sequoia's arc [FUND-VERBATIM]** is the most-cited: *"Company purpose → Problem → Solution → Why now → Market potential → Competition → Business model → Team → Financials → Vision."* The arc logic is: thesis → tension → resolution → **timing** → size → defensibility → economics → who → proof → ambition. Note it ends on ambition, not on the ask — Sequoia's list contains **no "Fundraising ask" section at all**, unlike DocSend, YC Series A ("Use of Funds"), Antler and 500 Global.

**YC's arc [FUND-VERBATIM]** is different in kind — it is evidence-first, not thesis-first. YC Series A: *"We help people quit smoking. Our product is so good that in just the past 2 years, we've reached 500k WAU growing at 20% m/m."* The one-liner leads with traction, then the problem is retro-fitted to explain it. YC is explicit that this is deliberate: credibility first, ambition last — *"You've spent the past 10 or so slides building your credibility by demonstrating the incredible business you've already created. Now when you talk about the future, investors are more likely to believe you."* YC's arc is credibility → then vision. Sequoia's is vision → then credibility.

**First Round's arc [SECONDARY, dated 2015]** — Oren Jacob (then ToyTalk CEO, ex-Pixar), [review.firstround.com/tell-stories-like-this-to-take-your-fundraising-pitch-from-mediocre-to-memorable](https://review.firstround.com/tell-stories-like-this-to-take-your-fundraising-pitch-from-mediocre-to-memorable/): *"You need to take the whole room on a journey together… there has to be a narrative arc with a beginning, middle and end."* His specific prescription: **lay out the map up front** — *"Lay out the map for them at the beginning: 'I am going to talk about engagement; I am going to talk about monetization; I am going to talk about our team and features and potential competitors.'"* This "agenda framing" move is unique in the corpus and directly contradicts Sequoia/YC's implicit "no table of contents" norm. **This is a 2015 source and is dated** — it references a 2011 seed raise, Siri's launch, and 60–70-slide working decks. Treat the principles as durable, the specifics as historical.

**DocSend's arc [DATASET]** is explicitly sequential-commitment: *"The first three slides — typically cover, problem, and solution — function as a filter. If the problem is not compelling after slide two, the investor closes the deck."* And: *"every slide must earn the right to the next slide's attention."* Their design implication is that the deck must work as a **standalone read**: *"approximately 30% of pitch decks that result in a meeting are shared internally before the meeting is scheduled… If a partner shows your deck to another partner without being in the room to explain it, every slide must stand on its own."*

**Techstars' arc [FUND-VERBATIM]** is vision + momentum, written as a script first. **Antler's arc** is problem → resolution → proof, deliberately opening on the customer rather than the company.

---

## 3. The "why now" / insight / wedge pattern

This is the sharpest area of agreement, and the clearest signal of fund-specific taste.

**Sequoia — "why now" is a named, required slide, and it is stated as a near-universal rule [FUND-VERBATIM]:**
> *"Why now? The best companies almost always have a clear why now? Nature hates a vacuum—so why hasn't your solution been built before now?"*

Note the framing: Sequoia's why-now is **not** "what tailwind helps you" — it is "why was this impossible/irrational before." That is a stronger, more falsifiable test.

**Y Combinator — the analogue is "insight," and it is one of three required components of an idea [FUND-VERBATIM]** ([library/6q](https://www.ycombinator.com/library/6q-how-to-pitch-your-startup)):
> *"a startup idea is a hypothesis for why your company is gonna grow really quickly. That hypothesis must compose of three different parts: the problem, the solution, and insight… you're looking to have something that's gonna make your company unique and have some kind of unfair advantage that we call an insight that will show why your company will grow faster than other companies."*

Hale's talk references **five types of unfair advantage** with benchmarks, but the talk does not enumerate them in the transcript — he says they were covered in the preceding "evaluating startup ideas" talk. **I could not verify the five types from a primary YC source in this session.** [UNVERIFIED]

In YC's seed template the insight is a literal slide: *"Tell the investor what makes you so special, what makes this work, what your insights are. This might take more than one slide."* ([library/2u](https://www.ycombinator.com/library/2u-how-to-build-a-pitch-deck))

**a16z — the "why now" test appears in a16z's own fund deck [FUND-VERBATIM]:** In the published a16z Games Fund One pitch deck, Andrew Chen labels a slide *"Here's the 'why now' slide"* — evidence that a16z applies the same structure to itself, with tailwinds + cultural/technological inflection as the content. [andrewchen.com/1-year-a16z-games](https://andrewchen.com/1-year-a16z-games/) **[SECONDARY — hosted by an a16z partner on his personal blog, not a16z.com]**

**DocSend [DATASET]** treats why-now as **optional at both stages** but growing in importance, with the explicit instruction to omit it rather than fake it:
> *"If your timing is not particularly unique, skip this section. It's better to have a strong, focused deck without it than to force a weak 'why now' argument."* ([pre-seed page](https://www.docsend.com/blog/what-to-include-when-building-your-pre-seed-pitch-deck/))

DocSend's seed page makes the constructive version explicit: *"If your company wouldn't have been possible or viable even 2-3 years ago, make that explicit."* Measured time: **23 s at seed** (the second-least-viewed section) and **38 s at pre-seed**.

**Antler does not have a why-now slide**, but plants it inside Team: *"Why you. Why now. Why is this specific combination of people uniquely positioned to solve this problem?"*

**YC on the wedge/sequence problem [FUND-VERBATIM]**, which is the practical version of why-now: on multi-stage ideas, Hale says focus only on stage one — *"I would focus only on describing what part one is and then later on, you talk about what are the other phases that are important,"* and warns that staging reads as defensive: *"it sounds almost like a defense instead of you saying your strategy… 'Hey, I'm gonna talk about what my company's doing but I'm worried that you're gonna think it's really small. So don't worry, we're gonna do parts two and three.'"*

---

## 4. Deck length, format, and design norms

### Length

| Source | Recommended length | Tag |
|---|---|---|
| YC (Demo Day, on-stage) | **5–7 slides** | [FUND-VERBATIM] |
| YC (seed, send-ahead) | ~10–11 sections, "no set where n > 3"; no page total given | [FUND-VERBATIM] |
| YC (Series A) | ~10 named slides + appendix "as many as necessary" | [FUND-VERBATIM] |
| Antler (pre-seed) | **10 slides** | [FUND-VERBATIM] |
| 500 Global | **"doesn't need more than 10 slides"** | [FUND-VERBATIM] |
| DocSend (pre-seed) | **18 pages** | [DATASET-adjacent — recommendation, not measurement] |
| DocSend (seed) | **19–20 pages** | [DATASET-adjacent] |
| Sequoia | no number given | — |
| Techstars | no number given; slides should have "the least amount of content that they could possibly have" | [FUND-VERBATIM] |
| First Round (2015) | **12 slides**; author starts at 60–70 and cuts to 12 | [SECONDARY, dated] |
| Papermark (measured) | 9–16 pages was the most common range, **49% of decks** | [DATASET] |
| Storydoc (measured) | ~10 slides → 32% completion vs 22% overall; engagement falls after 18 slides | [DATASET] |

**This is a real, unresolved disagreement: funds say 10, the send-ahead data says 18–20.** The reconciliation DocSend implies is that their 18–20 figure includes multi-page *sections* (e.g. Product 3–4 pages, Traction 1–4 pages), whereas Antler/500's "10" counts *sections*. Neither source states this explicitly. Flag it as an apparent conflict, not a solved one.

### Format and design

- **Optimise for comprehension, not beauty — YC, verbatim:** *"Optimize for clarity and understanding, not beauty… keeping it as simple and bare-bones as possible. Avoid anything that might distract from your main point. Two of the most common culprits here are fancy, complicated diagrams that are hard to understand or colorful images that look nice but don't help illustrate your point."* ([library/8d](https://www.ycombinator.com/library/8d-how-to-build-a-great-series-a-pitch-and-deck))
- **The YC legibility test:** *"even old people sitting in the back row with bad eyesight can read"* → large type, bold text, simple font, good contrast from background, text at the top. ([library/4T](https://www.ycombinator.com/library/4T-how-to-design-a-better-pitch-deck))
- **Screenshots — YC is unusually hostile:** *"I usually hate screenshots in Demo Day presentations. Screenshots are almost always illegible, complex, and non-obvious. They break all 3 rules!"* Hale's preferred substitute is *"a bulleted list of steps."* He extends this to screencasts and video: *"Think twice before trying to use either one."* **This directly contradicts DocSend's pre-seed advice**, which says the Product section should include *"multiple visual formats: wireframes, screenshots, videos, Figma mockups, feature GIFs"* and recommends embedding a demo video. Flag as a genuine fund-vs-data disagreement; note YC's advice is scoped to *on-stage Demo Day*, where DocSend's is scoped to *send-ahead reading*. That scope difference probably resolves it.
- **Text density:** Techstars/Gaby Rudd, verbatim: *"People will listen, or they will read. They will not do both."* Their appendix rule: dense information belongs in the appendix — *"Put it in an appendix. Maybe they ask for it, maybe they don't."*
- **Word count:** DocSend-derived guidance (via archival summary) is **under 50 words of copy per slide**, no table of contents, and each slide tagged with its section label. Mark this **[SECONDARY]** — see §8 for provenance caveat.
- **16:9 / font specifics:** **Not found in any primary source in this corpus.** No fund specifies aspect ratio or typeface. Anyone claiming a fund mandates 16:9 is not citing a fund. **[UNVERIFIED across all sources]**
- **PDF vs DocSend:** No fund in this corpus states a PDF-vs-DocSend preference. DocSend's own instrumented-link guidance is vendor-specific and should be read as marketing. a16z is the only one of the named funds to have published on **data rooms and document sharing** rather than decks ([a16z.com/the-insiders-guide-to-data-rooms-what-to-know-before-you-raise](https://a16z.com/the-insiders-guide-to-data-rooms-what-to-know-before-you-raise/)). **[FUND-VERBATIM on data rooms; no deck-file-format position]**
- **Appendix — this is the closest thing to consensus:** YC Series A: *"The appendix should include ammunition for the subsequent Q&A/conversation that follows the pitch… financial projections and a more detailed use of funds. This section will expand significantly once you start pitching."* First Round/Liz Wessel (2024): *"I often recommend also having a large appendix of slides for your eyes only"* with specific examples — cohort analysis (B2C), competitive landscape chart, customer breakdown by revenue (B2B), sales pipeline. First Round/Oren Jacob (2015): *"You might have 10 slides of nerdy graphs in the appendix that you can use to answer questions."* Techstars: appendix is where density goes.

### Deck vs live pitch

- **a16z is unambiguous that you still need the deck — [FUND-VERBATIM]:** *"Can't I just have a conversation with the investors? Do I really need to prepare a full slide deck?" … "Most companies… get very few opportunities to make a strong impression with potential investors. So treat each interaction as your last. Make those interactions count. Don't leave anything to chance. Take time to prepare a full deck and practice, including creating a script and doing dry-runs."* ([a16z.com/16-common-questions-about-fundraising](https://a16z.com/16-common-questions-about-fundraising/), 2015)
- **First Round (2024) on partner meetings — [FUND-VERBATIM]:** *"Some founders believe they shouldn't use slides for 1:1 pitches. However, for partner meetings, it is almost always recommended to come with slides."*
- **Techstars is more situational:** *"Ask at the beginning of the meeting, 'Would you like to see a slide deck?' and make sure that you have a slide deck."*
- **First Round/Oren Jacob (2015), the strongest "no-slides" position:** *"You should be able to give your pitch with no slides. Cold."* And: *"Never read your slides. If you find yourself doing that, you've already lost."*

---

## 5. How norms differ by stage

### Pre-seed

- **The bet is on the team and the problem, not traction — Antler, verbatim:** *"Investors at this stage are not betting on your traction. They are betting on you, your thinking, and whether the problem you've identified is real enough to build a company around."* And: *"At Pre-seed, investors are often backing the team before the idea. They know the idea will change."*
- **What counts as traction is radically relaxed — Antler:** *"At Pre-seed, traction doesn't have to mean revenue. It means evidence that the problem is real and that people want your solution. Letters of intent, pilot customers, waitlist signups, interviews conducted, prototypes tested… Even ten customer conversations with documented insights is traction."*
- **Red flag, Antler-verbatim:** *"The biggest red flag at Pre-seed is a team that has spent six months building without talking to a single customer. Conviction isn't evidence."*
- **Traction verification becomes a liability.** DocSend's most counter-intuitive finding: *"VCs spend 80% more time evaluating the traction of companies that didn't successfully raise money. If your market traction isn't immediately obvious to investors, it may raise skepticism and prompt scrutiny that may not work in your favor."* ([pre-seed page](https://www.docsend.com/blog/what-to-include-when-building-your-pre-seed-pitch-deck/))
- **Product confidence expectations:** DocSend requires pre-product companies to show *"high-fidelity Figma prototypes, detailed wireframes, user flow diagrams"* — i.e. even pre-seed must show a real artefact.
- **Read time is longer at pre-seed than seed** in DocSend's data: **4:10 pre-seed vs 3:44 seed.** This inverts most founders' intuition.
- **Financials optional:** DocSend marks Financials optional at pre-seed, and (via archival summary) notes that only **one third of successfully funded seed companies included a financials section at all**. **[SECONDARY]**

### Seed

- **Traction moves to the front.** YC seed template puts Traction at slide 4 and adds a "More metrics" slide. 500 Global puts it at 5.
- **The completion problem is quantified:** DocSend — *"only 58% of pitch decks are viewed to completion. This means nearly half of founders lose investor attention before reaching their final slides."*
- **Market size becomes a first-four slide** in DocSend's seed order.
- **The Series A is now the implied next milestone.** DocSend: *"showing 18-24 months of runway is standard. Explain what milestones you'll hit that position you for a successful Series A."*

### Series A

- **Trend data is mandatory and time-quantified — YC, verbatim:** *"Show trends. What's more important than where your traction is at this point in time is where it's going… a monthly or quarterly graph is better than a summed up annual number. You also need to show at least 4-6 months of this trend for it to be believable."* ([library/8d](https://www.ycombinator.com/library/8d-how-to-build-a-great-series-a-pitch-and-deck))
- **The deck is judged against seed promises:** *"at the Series A, you need to have data to show you've made good on the promises you made at the seed."*
- **Bottom-up market sizing is required:** *"We usually suggest a bottoms-up calculation… number of prospective customers x value of each customer to you… A bottoms-up calculation should rely on real numbers gleaned from your current business."* Note this **contradicts** Sequoia's older template, which specified *"TAM (top down), SAM (bottoms up)."*
- **Specific named traps — YC lists three, verbatim:**
  1. *"Throwing reams of numbers at investors"* → fix with "hero facts"
  2. *"Too few numbers"* — *"it feels like you're hiding your numbers because you think they're weak"*
  3. *"Unclear numbers"* → two named sub-patterns: **cumulative numbers** (*"Almost every time I've seen cumulative numbers in a Series A deck, it's because founders are trying to hide their monthly/quarterly numbers"*) and **double-axis graphs** (*"time is always wasted in clarifying which line goes with which axis"*)
- **The pitch meeting is timed:** YC prescribes *"an hour with a 20 minute pitch, a 20 minute conversation, and 20 minutes of feedback."* First Round (2024): a real partner meeting is *"usually 60 minutes"* vs *"30-45 minutes"* for a 1:1, with *"anywhere between 5-15 investors."*
- **The partner meeting is a different artefact.** First Round lists the typical **investment memo** sections, "anywhere from three to thirty pages, even at the seed round": *Founder backgrounds · Market overview and problem · Solution / Product · Big vision · GTM · Traction · Team · Competitive landscape.* The practical consequence: *"your 'audience' has often read through an investment memo and therefore will likely be more prepared to get into the weeds."* Bessemer publishes real examples of these memos at [bvp.com/memos](https://www.bvp.com/memos) (e.g. Auth0 seed check, Pinterest Series A, as cited by First Round).
- **Partner-meeting offer rates — First Round, [FUND-VERBATIM as a partner's estimate]:** *"the chances of a venture firm investing in your startup after an initial 1:1 meeting may be something like 5%… Firms often say their partner meeting 'offer rate' is anywhere from 25-60%."* Decision timing: *"Most firms will get a decision back to the founder within 24 hours of a PM."*

---

## 6. Fund-specific tells and turn-ons

### a16z

No deck structure. What a16z actually tells you, from its own publications:

- **Metrics vocabulary is the real filter.** a16z's [16 Startup Metrics](https://a16z.com/16-startup-metrics/) (2015, and still their most-cited metrics piece) is effectively a list of the mistakes they penalise. Verbatim: *"A common mistake is to use bookings and revenue interchangeably, but they aren't the same thing… Letters of intent and verbal agreements are neither revenue nor bookings."* Others: paid CAC is *"more important than blended CAC"*; *"investors prefer to measure it as CMGR (Compounded Monthly Growth Rate)"* not simple average; LTV must be **net profit**, not present-value-of-revenue or gross-margin; *"A common mistake is to estimate the LTV as a present value of revenue."*
- **The 3x LTV:CAC benchmark is a16z's own published number — [FUND-VERBATIM]:** *"Investors often use 3x LTV:CAC as a rough benchmark of a consumer company's financial health… In fact, improving your LTV:CAC from 2x to 3x can nearly triple your valuation."* ([a16z.com/why-do-investors-care-so-much-about-ltvcac](https://a16z.com/why-do-investors-care-so-much-about-ltvcac/), 2023)
- **Capital-to-milestone alignment is a16z's stated core rule — [FUND-VERBATIM]:** *"regardless of size or what a round is called (seed, series A, B, C, etc.), it's all about the alignment of capital to milestones."* ([16 Common Questions About Fundraising](https://a16z.com/16-common-questions-about-fundraising/))
- **Runway as leverage:** *"raise money when you don't need it' is true!). Runway = negotiating leverage."*
- **The three readiness criteria**, verbatim: (1) sufficient runway for flexibility, (2) milestones achieved for the valuation you want, (3) *"You're thoroughly prepared to deliver a knock-out pitch and efficiently respond to diligence requests."*
- **A live a16z pitch deck exists.** The a16z Games Fund One deck is published with commentary by a16z GP Andrew Chen ([andrewchen.com/1-year-a16z-games](https://andrewchen.com/1-year-a16z-games/)). Its structure is instructive even though it is a *fund* deck: industry overview/context → *"why now"* slide (tailwinds) → investment areas → how the team/operating model differentiates. Chen's framing: *"We structured our pitch deck into a discussion and overview about the games industry – many folks outside the industry needed some context to catch up. And then our investment areas, and then how we approached the team."* **[SECONDARY — personal blog, not a16z.com]**
- **a16z crypto's pitch primer:** *"Preparing for the pitch"* by GP Arianna Simpson — *"She covers pitching from start to finish – from crafting a narrative for your product and team to following up."* The page is a video wrapper with no written structure. [a16zcrypto.com/posts/videos/preparing-for-the-pitch](https://a16zcrypto.com/posts/videos/preparing-for-the-pitch/)
- **On the "what is the secret" claim in the brief:** I found **no a16z-published page** using "what is the secret" as an evaluation criterion. Do not attribute it. [UNVERIFIED]
- **a16z speedrun:** the application pages ([Winter/Spring 2026](https://a16z.com/a16z-speedrun-application-winter-spring-2026/), [SR007](https://a16z.com/applications-for-a16z-speedrun-sr007-are-now-open/)) publish no deck format. [UNVERIFIED for deck guidance]

### Y Combinator

- **"Make something people want" is an operating thesis, not a slide criterion.** YC does not put it on a deck slide; it appears as the underlying test. YC's deck-level substitutes are clarity and the problem/solution/insight triplet.
- **Growth rate is expressed as a **trend with a minimum duration**, and YC quantifies it: **4–6 months minimum**, monthly/quarterly granularity, CMGR-style framing implied. YC also states the "longer you've been around, the more you have to have done" rule and ties benchmarks to the **18–24 month seed→Series A** timeline. ([library/8d](https://www.ycombinator.com/library/8d-how-to-build-a-great-series-a-pitch-and-deck))
- **YC explicitly de-emphasises selling.** Hale, verbatim: *"I do not need you to sell me as a YC partner… we are really good at selling ourselves. So you don't need to do that."*
- **Banned language list — YC, verbatim:** ambiguity, complexity, mystery (jargon, indefinite pronouns, "things that you just suggest, but aren't explicit about"), and **ignorable** — *"marketing speak… MBA speak, where you kind of like, puff yourself up, talk that doesn't give any extra information, and then buzzwords."* Plus: *"No preamble."*
- **X-for-Y has three explicit tests — YC, verbatim:** is X a household name (billion-dollar company), does Y actually want X, and is Y a huge market. Counter-example YC gives: *"a company in the batch that started off by describing themselves as Buffer for Snapchat. Buffer is a nice company, but definitely smaller than Snapchat. So don't wanna do that."*
- **The "reproducible" test — YC, verbatim:** the listener must be able to picture what you'd build, which requires three nouns: *"what are you making?… What is the problem? And then who is the customer?"*
- **Team slide signalling risk — YC, unusually specific:** *"beware of signaling risk - if you include a Series A fund on the list of existing investors, you'll be asked whether or not they're leading your round. If the answer is yes, then why are you giving the pitch? If the answer is no or that you're not sure, that could be a negative signal. In general, best to leave those logos off."*
- **Presentation mechanics over video** (post-2020, still relevant): one person pitches, look into the camera not a side screen, ring light, *"You're going to have to overcompensate in energy and verve."*
- **Practice question set — YC, verbatim:** *"Were you confused? If so, when? Were you bored? If so, when? Did my deck help or hurt? What are a couple hard questions I need great answers to?"*

### Sequoia

- **"Why now" is Sequoia's signature demand** — stated above, and phrased as an obligation rather than a tailwind: *"Nature hates a vacuum—so why hasn't your solution been built before now?"*
- **Sequoia's stated screening logic is not the deck.** Verbatim: *"it wasn't really the slides we liked—it was their ideas, the clarity of their thinking, and the scope of their ambition. We love partnering with founders hell-bent on bringing an idea to life that conventional wisdom deems impossible."* This is simultaneously genuine guidance and **fund marketing** — it is a pitch for Sequoia's brand as much as advice. Flag it as both.
- **"Some of the best companies invent their own markets"** — Sequoia's Market potential guidance is explicitly permissive about non-existent categories, in contrast to 500 Global's hard *">$1B or a plan to get there"* rule.
- Sequoia's Arc page markets the "Arc Intensive" (four days, workshops, guest speakers) but publishes no deck format.

### Funds where the brief's premise is not supported

- **Bessemer:** publishes [memos](https://www.bvp.com/memos) and [roadmaps](https://www.bvp.com/atlas?type=roadmap) — no pitch deck template. A full `bvp.com/sitemap.xml` sweep for `pitch|deck` returns nothing but memos and roadmaps. The "Bessemer pitch deck template" that circulates online is not on bvp.com. [UNVERIFIED as a Bessemer artefact]
- **Greylock:** no deck guide. A full `greylock.com/post-sitemap.xml` sweep (290 posts) for `pitch|deck|rais|fundrais|series-a` returns exactly one hit — [greylock.com/blog/startup-storytelling](https://greylock.com/blog/startup-storytelling/) — and that URL **now returns HTTP 404**; it was a Greymatter podcast with Figma's comms VP about *corporate* communications, not decks. The Greylock Series A material the brief may be thinking of is a Business Insider report on a Greylock presentation by Saam Motamedi ([businessinsider.com, 2021](https://www.businessinsider.com/greylock-startup-presentation-raising-funding-saam-motamedi-successful-company-2021-7)) — **[SECONDARY], paywalled, not a Greylock publication.**
- **Index Ventures:** publishes substantial founder guides — [Rewarding Talent](https://www.indexventures.com/rewarding-talent/), [Winning in the US](https://www.indexventures.com/winning-in-the-us/) (which has a "fundraising" chapter), [Scaling Through Chaos](https://www.indexventures.com/scaling-through-chaos/) — but **no pitch deck guide**. A full sitemap sweep confirms it. The frequently-cited "Index Ventures pitch deck tips" is a [Pitch.com blog post](https://pitch.com/blog/index-ventures-pitch-deck-tips) and a [Business Insider webinar write-up](https://www.businessinsider.com/webinar-fast-index-ventures-pitch-deck-2020-7) — both **[SECONDARY]**.
- **Lightspeed:** no deck guide on lsvp.com found. Closest primary-adjacent source is a TechCrunch interview with Lightspeed's Gaurav Gupta walking through Grafana's Series A deck ([techcrunch.com, 2021](https://techcrunch.com/2021/02/05/pitch-decks-pricing-and-how-to-nail-the-narrative-with-lightspeeds-gaurav-gupta-and-grafanas-raj-dutt/)) — **[SECONDARY]**. Usable insight from it: Gupta says the slide that moved the partnership was a **visual** one showing dashboards at recognisable companies — *"That just emotionally resonates with people when you're thinking about investing in a company."*
- **Accel, Redpoint, Founders Fund, Benchmark, Coatue, Insight Partners:** no primary deck-format guidance found. **Insight Partners** has a directly relevant page — [insightpartners.com/ideas/how-should-i-prepare-for-a-fundraising-meeting-with-insight](https://www.insightpartners.com/ideas/how-should-i-prepare-for-a-fundraising-meeting-with-insight/) — but it did not render its body content through either direct fetch or a reader proxy (cookie-consent wall returned only boilerplate). **Could not verify its contents.** [UNVERIFIED]

---

## 7. Anti-patterns and red flags, with numbers

### YC — explicit "avoid" list **[FUND-VERBATIM]**

Design (from [library/4T](https://www.ycombinator.com/library/4T-how-to-design-a-better-pitch-deck)): too much text · excessive explanations and caveats · excessive branding per slide · photos with no titles or captions · **animations** · **transitions** · **memes** · subtle humor · **accidental humor**. Plus: screenshots, screencasts, videos, diagrams (*"To me, diagrams are like little mazes for ideas"*), and showing multiple ideas on one slide.

Hale's stated exception, which is worth preserving: a complex slide is acceptable *"when your point is to show complexity or to overwhelm the audience"* — his example is Magic's grid of every on-demand service, used to illustrate the discovery problem.

Idea-level (from [library/6q](https://www.ycombinator.com/library/6q-how-to-pitch-your-startup)): ambiguity · complexity · mystery · ignorable · jargon · indefinite pronouns · marketing/MBA speak · buzzwords · no preamble · non-reproducible descriptions.

Series A level (from [library/8d](https://www.ycombinator.com/library/8d-how-to-build-a-great-series-a-pitch-and-deck)): information overload · too few numbers · **cumulative numbers** ("almost every time… it's because founders are trying to hide their monthly/quarterly numbers") · **double-axis graphs** · top-down market sizing only · **future-roadmap inflation** (*"Too often I've listened to pitches where founders paint a vision of an awesome-sounding product, only to be disappointed when I poke at it and realize they've only really built the very first piece… investors will discount these hand-wavy hypotheticals to zero"*) · headshots of every employee · listing existing Series A investors as logos.

### DocSend — do/don't per section **[DATASET]**

Selected, verbatim:

- **Problem:** *"DON'T: Present multiple unrelated problems (focus on ONE core issue)."*
- **Solution:** *"DON'T: Claim you have 'no competition' (it signals lack of market research)… Use vague language like 'we leverage cutting-edge technology'."*
- **Why now:** *"DON'T: Include this section if there isn't genuine timeliness… Rely solely on COVID-19 as your 'why now' (it's 2026—move beyond pandemic references)."*
- **Product:** *"DON'T: Show only a logo or landing page design… Skip this section because you're 'too early'… Use placeholder text or 'Lorem ipsum' in mockups."*
- **Market size:** *"DON'T: Understate your market size to seem 'realistic'… Use only top-down market sizing without bottom-up validation… Present a TAM so large it's implausible ($1 trillion markets rarely exist)… Use outdated market research (nothing older than 2024)."*
- **Team:** *"DON'T: List every job title from the past 20 years… Write overly long bios that feel like LinkedIn profiles."*
- **Business model:** *"DON'T: Present vague 'we'll figure out monetization later' approaches… Assume 'we'll make it up in volume' without supporting data."*
- **Financials:** *"Investors are allergic to excessive burn rates. If you're spending $200K/month but only have $50K in revenue, you need a compelling story about why that burn is necessary."*
- **Ask:** *"DON'T: Pick an arbitrary number or present a vague allocation."*

DocSend also supplies the target unit-economics numbers decks should hit: **LTV:CAC ≥ 3:1 at scale**, **CAC payback < 12 months**.

### Antler — red flags **[FUND-VERBATIM]**

- Problem too broad: *"'Small businesses struggle with cash flow' is not a problem."* Their model of a good one: *"A founder of a 3-person agency doesn't know on Monday whether she can make payroll on Friday."*
- Top-down TAM: *"Top-down market sizing is one of the fastest ways to lose credibility in a pitch. Every investor has seen 'we are targeting a $50 billion market and just need 1% of it'. It means nothing."*
- Fake competition matrices: *"Not a 2x2 matrix where you've conveniently placed yourself in the top right corner with no one else near you."*
- No competition: *"Nothing makes an investor more suspicious than a founder who says they have no competition."*
- Vague GTM: *"'We'll use social media, content marketing and partnerships' is not a GTM strategy."*
- "We'll figure out monetisation later": *"is a founder who hasn't thought hard enough about their customer."*
- Unexplained hockey sticks: *"If your revenue projections go up with no clear explanation of what drives that growth, it tells them you don't understand your own business."*
- Non-milestones: *"'Hire 3 engineers and build the product' is not a milestone. 'Reach 50 paying customers and prove we can acquire them for under $200 each' is a milestone."*

### 500 Global — red flags **[FUND-VERBATIM]**

- *"The last thing you should do is say you have no competition—there's always competition, and saying you're the 'first' to do something often shows a lack of knowledge about your space."*
- *"don't overload it with excessive text and images."*
- Jargon: *"No expert jargon, no buzzwords—explain it like you would to a 5 year old."*

### Techstars — red flags **[FUND-VERBATIM]**

Outreach-level (directly relevant, unusually concrete): **non-personalised cold email** (*"If you have to send a cold email outreach, please, please, please make it personal"*), six-paragraph emails (*"sometimes it's going to end up in the trash"*), **email blasting** (*"Please do not email blast all of them… That is not going to work for you"*), **false urgency** (*"Lying or creating false urgency… that's going to be an immediate red flag for us"*), **boring** (*"The worst thing that we can do is just get a boring email"*), and **AI-generated mass personalisation** (*"In the age of agents and LMS, there's great temptation to do exactly what Gaby just said. Don't do it… We can tell when it comes as a mass blast."*).

Also: an intro from an investor who *passed* on you is worse than a cold email — *"You're better off doing a cold email outreach."*

Meeting-level: monologuing a 30-minute slot (*"It's a brain drain"*), over-scripted delivery (*"We don't want to hear a script. We can tell that you're reading"*), and claiming nothing is wrong (*"when you say, oh, nothing's wrong with my business, everything is great… that feels less honest to us"*).

### Sequoia — implicit red flags

Sequoia's guide is written as positives, but the inverses are explicit: listing features instead of communicating mission (Company purpose), and not knowing why your solution hasn't been built before (Why now).

### a16z — red flags are metric-level

Using bookings as revenue. Mixing LOIs/verbal agreements into either. Blended CAC instead of paid CAC. Simple-average MoM instead of CMGR. LTV computed as revenue or gross margin rather than net profit. Ignoring the LTV:CAC ratio. ([16 Startup Metrics](https://a16z.com/16-startup-metrics/))

---

## 8. Published statistics, with sources

| Statistic | Value | Source | Tag |
|---|---|---|---|
| Avg time VCs spend on a **pre-seed** deck | **4 min 10 s** | [DocSend pre-seed](https://www.docsend.com/blog/what-to-include-when-building-your-pre-seed-pitch-deck/) (updated Feb 2026) | DATASET |
| Avg time VCs spend on a **seed** deck | **3 min 44 s** | [DocSend seed](https://www.docsend.com/blog/what-vcs-really-want-to-see-inside-your-seed-deck/) (updated Mar 2026) | DATASET |
| Seed deck **completion rate** | **58%** viewed to completion | [DocSend seed](https://www.docsend.com/blog/what-vcs-really-want-to-see-inside-your-seed-deck/) | DATASET |
| Share of **pre-seed** decks that lead to a meeting | **1–2%** | [DocSend pre-seed](https://www.docsend.com/blog/what-to-include-when-building-your-pre-seed-pitch-deck/) | DATASET |
| Decks received per week by a VC | 100+ | [DocSend pre-seed](https://www.docsend.com/blog/what-to-include-when-building-your-pre-seed-pitch-deck/) | DATASET |
| Extra scrutiny on **traction** in decks that *failed* to raise | **+80%** time | [DocSend pre-seed](https://www.docsend.com/blog/what-to-include-when-building-your-pre-seed-pitch-deck/) | DATASET |
| Decks shared internally before a meeting is booked | ~**30%** | [Pitchgrade summary of DocSend](https://pitchgrade.com/blog/what-investors-read-pitch-deck-docsend-data) | SECONDARY |
| Per-section VC time, **pre-seed** (33/39/27/38/77/39/46/83/37/40/55/40 s) | Business model highest at **83 s** | [DocSend pre-seed](https://www.docsend.com/blog/what-to-include-when-building-your-pre-seed-pitch-deck/) | DATASET |
| Per-section VC time, **seed** (26/34/34/–/23/59/34/40/38/64/37/32 s) | Business model highest at **64 s** | [DocSend seed](https://www.docsend.com/blog/what-vcs-really-want-to-see-inside-your-seed-deck/) | DATASET |
| Avg view time, complete deck review | **3.2 min** (Papermark, Jan–Dec 2024, 3,000 decks) | [papermark.com/pitch-deck-metrics](https://www.papermark.com/pitch-deck-metrics) | DATASET |
| First-page view time | **23 s**; ~**15 s** for pages 2–10 | [Papermark](https://www.papermark.com/pitch-deck-metrics) | DATASET |
| Most common deck length | **9–16 pages**, 49% of decks | [Papermark](https://www.papermark.com/pitch-deck-metrics) | DATASET |
| Sessions ending within 10 s | **31%** | [Storydoc 2025](https://www.storydoc.com/blog/pitch-deck-statistics) via [hummingdeck](https://hummingdeck.com/blog/pitch-deck-benchmarks-2026) | DATASET (platform-specific) |
| Sessions reaching slide 4 that finish | **82%** | [Storydoc 2025](https://www.storydoc.com/blog/pitch-deck-statistics) via [hummingdeck](https://hummingdeck.com/blog/pitch-deck-benchmarks-2026) | DATASET (platform-specific) |
| Share of reading time on the **team slide** | **43%** | [Storydoc 2025](https://www.storydoc.com/blog/pitch-deck-statistics) via [hummingdeck](https://hummingdeck.com/blog/pitch-deck-benchmarks-2026) | DATASET (Storydoc-only; **not** a PDF benchmark) |
| Completion by deck length | ~**10 slides → 32%**; overall avg 22%; falls after 18 slides | [Storydoc 2025](https://www.storydoc.com/blog/pitch-deck-statistics) via [hummingdeck](https://hummingdeck.com/blog/pitch-deck-benchmarks-2026) | DATASET |
| VC survey: most important decision factor | **Management team** selected most often (885 VCs, 681 firms) | [NBER w22587](https://www.nber.org/papers/w22587) via [hummingdeck](https://hummingdeck.com/blog/pitch-deck-benchmarks-2026) | DATASET (stated criteria, **not** dwell time) |
| Partner-meeting offer rate | **25–60%** (firm-dependent) | [First Round, Liz Wessel, 2024](https://review.firstround.com/heres-what-you-can-really-expect-when-pitching-your-seed-stage-startup-at-a-vc-partner-meeting/) | FUND-VERBATIM (as a partner's estimate) |
| Chance of investment after a 1:1 first meeting | ~**5%** | [First Round, 2024](https://review.firstround.com/heres-what-you-can-really-expect-when-pitching-your-seed-stage-startup-at-a-vc-partner-meeting/) | FUND-VERBATIM (estimate) |
| Partner meeting length / attendees | **60 min**; **5–15 investors** | [First Round, 2024](https://review.firstround.com/heres-what-you-can-really-expect-when-pitching-your-seed-stage-startup-at-a-vc-partner-meeting/) | FUND-VERBATIM |
| YC Demo Day slot | **2 min 30 s**; ~1,000 investors in the room | [YC, Hale](https://www.ycombinator.com/library/4T-how-to-design-a-better-pitch-deck) | FUND-VERBATIM |
| YC Demo Day average raise (Hale's statement, ~2016) | **$1.5M** | [YC, Hale](https://www.ycombinator.com/library/6q-how-to-pitch-your-startup) | FUND-VERBATIM, **dated** |
| YC minimum trend window for Series A traction | **4–6 months** | [YC Series A](https://www.ycombinator.com/library/8d-how-to-build-a-great-series-a-pitch-and-deck) | FUND-VERBATIM |
| a16z consumer LTV:CAC benchmark | **3x**; 2x→3x "can nearly triple your valuation" | [a16z](https://a16z.com/why-do-investors-care-so-much-about-ltvcac/) | FUND-VERBATIM |
| 500 Global market-size floor | **>$1B** | [500 Global](https://latam.500.co/content/pitch-perfect-how-to-make-a-standout-pitch-deck-for-500-global) | FUND-VERBATIM |
| DocSend target LTV:CAC / payback | **≥3:1** / **<12 months** | [DocSend pre-seed](https://www.docsend.com/blog/what-to-include-when-building-your-pre-seed-pitch-deck/) | DATASET-adjacent recommendation |

### The statistics that are most often mis-cited

- **"VCs spend 3 min 44 s."** True, but it is **DocSend's *seed* figure**. The **pre-seed** figure is **4 min 10 s** — i.e. *longer*, not shorter. Any claim that early decks get less attention contradicts DocSend's own page. ([DocSend pre-seed](https://www.docsend.com/blog/what-to-include-when-building-your-pre-seed-pitch-deck/))
- **"The team slide gets the most attention at seed."** This claim is **not supported by DocSend**. DocSend's own seed page reports team at **38 s**, behind product (59 s) and business model (64 s). The "team slide dominates" finding comes from **Storydoc** (43% of reading time), a **different platform measuring interactive presentations**, and from the **NBER survey** about *stated* criteria — which measures what VCs say matters, not what they read. Conflating these three is the most common error in secondary pitch-deck content. ([hummingdeck's own methodology caveats](https://hummingdeck.com/blog/pitch-deck-benchmarks-2026) are a good model of how to flag this.)
- **Per-slide times in that widely-shared table** (Team 1 m 2 s, Financials 52 s, Traction 49 s, etc.) attributed to "DocSend's 2024 data" appear on [pitchgrade.com](https://pitchgrade.com/blog/what-investors-read-pitch-deck-docsend-data). They **do not match** the DocSend pages I retrieved, and pitchgrade supplies **no citation or methodology**. Treat as **[UNVERIFIED / likely unreliable]**.
- **"The 3 most-read slides."** The brief asks for this specific framing. I could not verify it from a primary DocSend source in this session. DocSend publishes per-section *times*, not a "top 3 most-read" ranking. **[UNVERIFIED]**
- **"Table of contents: almost no successful decks include one; under 50 words per slide; tag each slide with its section label."** These appear in an archival summary of a DocSend report ([venturecapitalarchive.com](https://www.venturecapitalarchive.com/archives/the-science-behind-developing-a-successful-pitch-deck-by-docsend)). They are **not** on the current DocSend pre-seed/seed pages I fetched. Provenance is a republication, not DocSend.com. Treat as **[SECONDARY / dated]** — plausible, and consistent with the DocSend house style, but not verifiable to the primary domain today.

---

## 9. What is dated, contested, or marketing

### Dated

| Source | Date | Why it matters |
|---|---|---|
| a16z, *16 Startup Metrics* | **2015** | Metric definitions remain current, but the examples (Facebook ad CAC benchmarks) and platform assumptions are dated. a16z itself re-cites it in 2023, which is some endorsement. |
| a16z, *16 Common Questions About Fundraising* | **2015** | Pre-dates SAFEs-at-scale, the 2021 bubble, and the 2022–23 correction. The capital-to-milestone rule has aged well; the "how long does a round take" content has not. |
| YC, Kevin Hale, *How to design a better pitch deck* | **2016** | Written for on-stage Demo Day with ~1,000 investors. Post-2020, most first pitches are video calls — YC's own Series A guide (2020) acknowledges this and adds video-specific advice. |
| YC, Kevin Hale, *How to pitch your startup* | ~**2017–18** | References specific companies in "the current batch" (Lumineye, Vahan). The framework is durable; the examples are stale. |
| First Round, Oren Jacob on storytelling | **2015** (Jan) | 60–70-slide working deck, 12-slide target, "projector bulb blew out," Siri launched "right after." Pre-dates every modern norm. The *lay out the map up front* and *appendix of nerdy graphs* advice is not re-endorsed in First Round's 2024 partner-meeting piece, which is a signal it may no longer be the house view. |
| Sequoia's SlideShare template | **2015 upload** (referencing an older source) | Superseded by the current sequoiacap.com page. **Stop citing the 10-slide Sequoia deck with a Product section.** |
| Bessemer *Atlas* memos | ongoing | Live, actively published. Auth0/Pinterest memos are still up. |
| YC Demo Day "$1.5M average raise" | ~2016 | Now badly outdated in both directions (2021 highs, 2023 trough). |

### Contested

1. **Traction position.** YC: slide 4. DocSend: slide 8 (seed) / 9 (pre-seed). Unresolved; likely stage- and context-dependent.
2. **Market vs why-now order.** Sequoia: why-now → market. DocSend seed: market → why-now.
3. **Deck length.** Funds say 10; tracking data says 18–20 recommended, 9–16 most common. The units (slides vs sections) are probably different and nobody says so.
4. **Screenshots and video.** YC "hate[s]" them; DocSend recommends them as the core of the Product section. Scope difference (stage pitch vs send-ahead read) likely explains it, but neither source acknowledges the other.
5. **Whether to include a table of contents / agenda.** First Round (2015) says lay out the map up front; DocSend-derived guidance says almost no successful decks include a TOC.
6. **Which slide gets the most attention.** DocSend: business model. Storydoc: team (43%). NBER: management team (stated). Three different measurements, three different answers.
7. **TAM method.** Sequoia's older template: "TAM (top down), SAM (bottoms up)." YC Series A, Antler, and DocSend all push bottom-up and warn against top-down-only. 500 Global permits either.

### Fund-specific marketing vs genuine guidance

**Reads as genuine, specific guidance:**
- YC's library pages and YC's Series A guide — these are the most operationally specific documents in the corpus, with named traps, exact trend windows, and slide counts. They read like internal curriculum, because they are.
- Sequoia's 10 sections — short, but each line is a real test rather than a platitude.
- a16z's metrics pieces and the *16 Common Questions* — concrete and falsifiable.
- DocSend's per-section do/don't lists — long, repetitive, and heavily SEO-optimised, but the benchmarks are real and the do/don'ts are concrete.
- 500 Global's 10 slides — the deck template is genuinely actionable and includes fill-in-the-blank formulas.

**Reads as brand marketing with guidance attached:**
- Sequoia's *Writing a Business Plan* opening — the Airbnb story plus *"we love partnering with founders hell-bent on bringing an idea to life that conventional wisdom deems impossible"* is a pitch to founders. Note the article's actual advice content is ~200 words; the marketing framing is comparable in length.
- Sequoia's Arc page — essentially all marketing. Zero deck guidance.
- a16z's data-room posts — genuinely useful, but they are also DocSend-adjacent SEO that happens to drive a16z's brand.
- Antler's post — well-structured and specific, but it is a recruiting funnel for Antler applications and ends with a soft CTA ("the pitch deck isn't going to secure investment. It's the conversation starter").
- Techstars' post — genuine and unusually candid, but it is explicitly *"Part 2 of a 4-Part series"* with two application-CTA links.

**Reads as pure SEO with no fund involvement** (name-check the fund in the title, no fund authorship, no fund link): `foundra.ai/vc/*`, `vcmatch.ai/investors/*`, `pitchgrade.com/blog/*`, `hummingdeck.com/blog/*`, `deckary.com`, `bestpitchdeck.com`, `inknarrates.com`. Several of these rank above the funds' own pages for "how [fund] evaluates pitch decks." They are **not** primary sources.

---

## 10. What I could not verify

1. **Insight Partners' fundraising-meeting guide.** [The page exists](https://www.insightpartners.com/ideas/how-should-i-prepare-for-a-fundraising-meeting-with-insight/) but its body did not render through direct fetch or a reader proxy (OneTrust cookie wall returned only boilerplate). **Contents unverified.**
2. **The "five types of unfair advantage"** referenced in YC's Hale talk. The adjacent talk ("evaluating startup ideas") was not located as a transcript. [UNVERIFIED]
3. **YC's `library/1k-benchmarks` and `library/1z-the-importance-of-trends`** — both are linked from YC's own Series A guide and **both now return HTTP 404**. YC's Series A benchmark numbers (the actual ARR/growth thresholds) are therefore **not currently retrievable from the primary domain**. This is a significant gap: the brief asked for YC's explicit growth-rate emphasis, and YC's own benchmark thresholds are dead-linked. [UNVERIFIED]
4. **Redpoint / Tomasz Tunguz deck guidance.** I did not retrieve a primary Redpoint or Tunguz post in this session. Given `tomasz-tunguz.com`-era content was historically on `tomtunguz.com` and much has been migrated, this needs a dedicated pass. [UNVERIFIED]
5. **Accel, Founders Fund, Benchmark, Coatue primary deck guidance.** Sitemap probes and multiple targeted searches found no fund-published deck structure. I believe this is a genuine negative, but I cannot rule out content behind JS-only navigation. [UNVERIFIED / likely absent]
6. **Any fund's position on 16:9, typeface, or PDF-vs-DocSend.** Nothing found in any primary source. [UNVERIFIED / likely no fund position exists]
7. **Greylock's Series A presentation.** Reported by Business Insider (2021) from a Greylock deck by Saam Motamedi; the underlying deck was not published by Greylock. Paywalled. [UNVERIFIED]
8. **Sequoia's original grove post** (`sequoiacap.com/grove/posts/6bzx/writing-a-business-plan`) — now dead; the SlideShare reproduction is the only accessible copy of the older template. [UNVERIFIED at original]
9. **The DocSend 2015 baseline study** (*"the science behind developing a successful pitch deck"*). The current DocSend pages carry the same headline numbers (3:44) but the original report and its "average 19.2 slides" figure were not retrievable at docsend.com (403 to non-browser clients; not archived at the URLs I tried). The archival summary at venturecapitalarchive.com is a republication. [UNVERIFIED at original]

---

## 11. Practical synthesis — what survives across sources

Wherever sources agree, they agree on this:

1. **One idea per slide.** (YC × 3 artefacts, DocSend, Techstars, 500 Global, Antler)
2. **The first three slides are the whole ballgame.** (DocSend's filter claim; YC's "what is it / is it clear"; 500 Global's "you only have seconds"; Antler's problem-specificity test)
3. **Lead with what, not why or how.** (YC, verbatim: *"Lead with what not why or how."*)
4. **Bottom-up market sizing.** (YC Series A, Antler, DocSend; Sequoia's older template is the outlier)
5. **Never say "no competition."** (500 Global, Antler, DocSend, implicitly YC)
6. **"Why now" as a real, falsifiable claim about what changed — not a tailwind list.** (Sequoia's version is the strongest test; DocSend says omit it if you can't do it honestly)
7. **An appendix that answers the questions you know are coming.** (YC, First Round × 2, Techstars)
8. **The ask must be framed as milestones, not money.** (YC's "Use of Funds… where that will get you in 18-24 months"; Techstars' *"It's not the amount of time, and it's not, I'm going to spend 50% of your money on engineers"*; a16z's capital-to-milestone rule; Antler's milestone specificity; DocSend's 18–24 month runway)
9. **Practice out loud until it's not a script.** (YC's 20/20/20 format and four practice questions; Techstars' *"We don't want to hear a script. We can tell that you're reading"*; First Round's *"practice as if the projector bulb blew out"*; a16z's *"creating a script and doing dry-runs"*)
10. **The deck is not the company.** (Sequoia: *"it wasn't really the slides we liked"*; DocSend: *"the best deck in the world won't save a fundamentally flawed business"*; Techstars: *"The pitch deck is just a vessel for a story"*; 500 Global likewise.)
