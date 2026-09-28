# Pitch Deck Patterns & Anti-Patterns Catalog

Track A of the deck audit: **42 investor-facing anti-patterns** (what to avoid), plus
seven AI-generation tells, and the
**positive patterns that replace each one**.

Sources are cited inline as `[n]` and expanded in
[`sources-and-attribution.md`](sources-and-attribution.md). Where a claim is a
published statistic, the number and its source are given. Where a claim is a
pattern observed across multiple funds' published guidance, it is marked
**(consensus)**. Where funds disagree, the disagreement is stated rather than
smoothed over.

---

## Part 1 — The 42 Anti-Patterns

Severity: **C** = Critical, **M** = Major, **m** = Minor. See
[`scoring-framework.md`](scoring-framework.md) for weights.

### Group 1 — Narrative & Positioning (AP-01 … AP-06)

**AP-01 · Feature list instead of an insight — `C`**
The deck enumerates capabilities and never states the non-obvious belief that makes
the company right. Investors are not buying features; they are buying a thesis.
*Detection:* the solution slide is a bulleted feature grid; no slide contains a
sentence of the form "We believe that ___ , which is why ___".
*Replace with:* the **Insight pattern** — one declarative sentence naming the
non-consensus belief, then the evidence that made you believe it.

**AP-02 · No "why now", or a "why" masquerading as "why now" — `C`**
DocSend found the Why Now slide appeared in **54% of successful decks vs 38% of
unsuccessful decks**, and investors spent **36% more time** on it in decks that
got funded [9]. This is a 2020 correlation, not a causal finding — see
[`sources-and-attribution.md`](sources-and-attribution.md) [9]. Sequoia's own template puts "Why now?" as a top-level required
section [2]. The tell that yours is fake: *would this slide have been equally
true five years ago, and will it be equally true five years from now?* If yes, it
is a "why", not a "why now" [5].
*Replace with:* a dated, falsifiable change — a cost curve crossing, a regulation
landing, a behaviour shift, a platform unlock — with a number and a year.
*Exception:* if the problem genuinely has no timeliness, the correct move is to
**omit the slide honestly**, not to manufacture urgency. DocSend's own guidance is
"don't stress about including this slide if your problem isn't connected to any
particular timeliness" [2].

**AP-03 · Buzzword soup — `M`**
"AI-powered end-to-end platform leveraging a proprietary algorithm to
revolutionize workflows." Every clause is a substitute for a concrete noun.
*Detection:* more than three of the deck's one-liner tokens appear in the
hype lexicon; see `scripts/score_deck.py`.
*Replace with:* the **Party Test** — a non-technical person repeats what you do
correctly after hearing it once [3].

**AP-04 · Jargon that excludes the room — `M`**
Domain jargon is fine; *internal* jargon is not. A generalist partner in the room
must be able to follow your problem. DocSend's guidance is blunt: friends, family,
and grandparents should understand the problem statement [4][5].
*Replace with:* name the customer's job-to-be-done in their words, not yours.

**AP-05 · The one-liner describes a category, not a company — `C`**
"We are a platform for the future of work." Sequoia: *"Define your company in a
single declarative sentence. This is harder than it looks. It's easy to get caught
up listing features instead of communicating your mission."* [2]
*Replace with:* `<Company> helps <specific who> <do specific thing> so they can
<outcome>` — ≤ 15 words, no adjectives you would not defend under oath.

**AP-06 · Vision with no wedge — `M`**
The deck opens on a $500B TAM and never says what the first 100 customers buy on
day one. Funds vary here: YC's seed template explicitly wants the *specific* problem
and solution before market size [1], while a16z filters on capital-to-milestone
alignment rather than a market-size slide at all [6][6b]. ("What is the secret" is
**not** an a16z criterion — see [`sources-and-attribution.md`](sources-and-attribution.md).)
*Replace with:* the **Wedge pattern** — beachhead segment → why you win there →
expansion path that ends at the big market.

### Group 2 — Market & Sizing (AP-07 … AP-09)

**AP-07 · Top-down TAM only — `M`**
"1% of a $50B market." This is the single most consistent complaint across fund
guidance and founder forums. It answers "how big could this be" while refusing to
answer "how do you get the first dollar".
*Replace with:* **bottom-up sizing** — (number of reachable customers) × (realistic
annual price) × (realistic attach rate), with each input sourced. Then show the
top-down number only as the ceiling.

**AP-08 · Unsourced market numbers — `M`**
Any figure without a citation is treated as invented by a diligence-minded
investor. The hard stop in [`scoring-framework.md`](scoring-framework.md) applies:
one invented number fails the deck.
*Replace with:* every market figure carries source + year, even if the source is
"our own bottom-up calculation from X and Y".

**AP-09 · Market defined so broadly it implies no focus — `M`**
"If we capture 1% of global logistics…" A market that includes everyone excludes
no one, and therefore implies no go-to-market.
*Replace with:* define the **entry market** narrowly enough that a competitor could
name your first 50 target accounts.

### Group 3 — Product & Proof (AP-10 … AP-13)

**AP-10 · No product evidence of any kind — `C`**
No screenshot, no demo, no prototype, no design partner, no user. YC's Kevin Hale
is unusually direct that screenshots are usually *bad* slides — illegible, complex,
non-obvious — but the answer is not to omit the product, it is to show **one idea
per slide** with the product large and captioned [3]. DocSend found investors spend
**59 seconds on the product section at seed** and **77 seconds at pre-seed** — the
single largest time sink in the pre-seed deck [4][5].
*Replace with:* a captioned, cropped, legible product visual per idea. Never a
full-UI screenshot shrunk to fit.

**AP-11 · Mockups presented as shipping product — `C`**
Figma renders of a roadmap item, labelled as if live. If an investor discovers this
in diligence, the deal is over and the relationship is over.
*Replace with:* label every visual `Live`, `Private beta`, or `Design concept`.
Honest labels cost nothing.

**AP-12 · Roadmap presented as traction — `M`**
"Q3: launch. Q4: 10k users." That is a plan. Traction is evidence that has already
happened.
*Replace with:* split the two explicitly — **Traction (happened)** and **Plan
(next 12 months)**.

**AP-13 · No proof it works — `M`**
No usage frequency, no retention, no repeat purchase, no completed workflow.
*Replace with:* the smallest honest proof of value — "412 of 500 invited beta users
ran a second reconciliation within 7 days".

### Group 4 — Traction & Metrics (AP-14 … AP-18)

**AP-14 · Vanity metrics — `M`**
Registered users, downloads, impressions, waitlist size, social followers, "LOIs
worth $2M". DocSend's deck structure research places traction as a distinct section
investors read closely, and reports that in decks that **failed** to raise,
investors spent **80% more time** on the traction section [2].
*Replace with:* metrics that would hurt if they stopped growing — revenue, active
usage, retention, gross margin, pipeline with signed contracts.

**AP-15 · Hockey-stick without stated assumptions — `C`**
A revenue curve that inflects with no driver labelled. Antler: *"If your revenue
projections go up with no clear explanation of what drives that growth, it tells
them you don't understand your own business."* [8] YC is blunter: investors
*"will discount these hand-wavy hypotheticals to zero because you haven't actually
done it."* [7]
*Replace with:* every projection slide states the three assumptions that produce
the curve (e.g. "assumes 4% monthly net revenue retention, 1 AE ramping per
quarter, 22% paid CAC improvement").

**AP-16 · Cherry-picked time window — `M`**
A 3-month chart chosen because it slopes up, when the 12-month chart is flat.
*Replace with:* the longest honest window, annotated with the events that explain
the shape. If the shape is bad, explain the cause and what changed.

**AP-17 · No retention or cohort evidence where the model requires it — `M`**
For subscription, marketplace, consumer, or usage-based businesses, a growth chart
without a cohort curve is unanswered. The best funds ask for the retention curve
before they ask for anything else.
*Replace with:* monthly cohort retention or net revenue retention, with the
definition of "retained" stated on the slide.

**AP-18 · Pre-revenue with zero demand evidence — `C`**
"Pre-revenue" is honest and acceptable at pre-seed. "Pre-revenue and pre-evidence"
is not investable at any price.
*Replace with:* at minimum, one of — signed LOIs, paid pilots, a waitlist with
conversion data, design-partner usage, or a working prototype with external users.

### Group 5 — Business Model & Unit Economics (AP-19 … AP-22)

**AP-19 · No business model — `C`**
"How will you make money?" answered with "we'll figure it out at scale".
DocSend research found **investors spend more time on the business model than on
any other section** — 83 s at pre-seed and 64 s at seed [1][2].
*Replace with:* current price points, the unit sold, the buyer, the sales motion,
and gross margin — even if provisional.

**AP-20 · Unit economics missing or implausible — `M`**
LTV/CAC of 12× with no explanation is a red flag, not a strength. a16z explicitly
asks founders to **pressure-test the burn multiple** (cash burned ÷ net ARR added)
and to know which spend is a burn-sink vs a burn-investment [6].
*Replace with:* LTV, CAC, payback months, gross margin, burn multiple — each with
its definition and its measurement window.

**AP-21 · Blended metrics passed off as channel metrics — `M`**
Blended CAC hiding a paid channel that never pays back.
*Replace with:* CAC per channel, with paid and organic separated. State whether CAC
includes sales compensation.

**AP-22 · Margins omitted in a capital-intensive or marketplace model — `M`**
Revenue growth with unstated gross margin is not a business case.
*Replace with:* contribution margin per transaction and the take rate.

### Group 6 — Competition & Defensibility (AP-23 … AP-26)

**AP-23 · "We have no competition" — `C`**
The most reliable single killer in the whole catalog. Every deck claiming this is
read by an investor who can name three competitors in thirty seconds. It signals
either that you have not done the work or that you believe the investor has not.
*Replace with:* name your **direct** competitors at your stage, plus the honest
**substitute** (spreadsheet, intern, do-nothing), and say where each one beats you.

**AP-24 · Only comparing against giants — `M`**
A competitive slide that lists Salesforce/Uber/Google. DocSend's guidance: focus on
companies at a **similar stage**, or ones that recently raised in your space —
*"Do not make comparisons with the giants of the industry"* [4][5].
*Replace with:* a 2×2 or table of true peers, plus one clause on "why now beats
the incumbent".

**AP-25 · A comparison grid where you win every row — `M`**
All-checkmarks-for-us grids are read as marketing, not analysis, and they invite
the investor to find the row you are hiding.
*Replace with:* include at least one row where a competitor genuinely wins, and
explain why that does not decide the market.

**AP-26 · No defensibility — `M`**
No answer to "what stops a well-funded team from copying this in six months?"
*Replace with:* one named moat with evidence — data flywheel, switching cost,
network density, regulatory position, distribution lock-up. Name the mechanism,
not the vibe.

### Group 7 — Team (AP-27 … AP-29)

**AP-27 · Advisor-heavy team slide — `M`**
YC: *"Talk about what makes your team particularly well suited to the problem.
This should be about founders. Nobody cares about your advisors."* [1]
*Replace with:* founders first, with a one-line **founder-market fit** proof each.

**AP-28 · No founder-market fit — `C`**
Titles are listed; the reason *these* people win *this* problem is absent.
*Replace with:* for each founder: what they shipped, at what scale, and the direct
link to the problem — "built and sold the reconciliation engine at X" beats
"ex-Google".

**AP-29 · Logos instead of people, or unnamed team — `M`**
A wall of employer logos with no names, roles, or links. Investors cannot do
reference checks on a logo.
*Replace with:* photo, full name, role, one achievement, LinkedIn/GitHub link.

### Group 8 — Ask & Mechanics (AP-30 … AP-34)

**AP-30 · Ask buried, vague, or absent — `C`**
No round size, no instrument, no timeline. DocSend's seed and pre-seed structures
both end on an explicit fundraising ask section with a target length of one slide
[4][5]. a16z advises founders to **prepare well, rehearse, and not to anchor on a
price expectation at the start of the conversation** [6].
*Replace with:* one slide: "Raising $2.5M SAFE at $20M post-cap. $1.4M committed.
Closing in 8 weeks."

**AP-31 · No use of funds or milestones — `M`**
a16z: *"Be deliberate and precise on use of proceeds… demonstrate that the juice is
going to be worth the squeeze"* and name which spend is a burn-investment [6].
*Replace with:* 3–4 buckets with percentages, each tied to a milestone that makes
the next round possible.

**AP-32 · Valuation anchoring inside the deck — `M`**
Putting a price expectation on a slide removes your ability to discover price and
invites an early pass. a16z explicitly warns against opening conversations with
price expectations [6].
*Replace with:* runway, milestones, and round size. Discuss valuation live.

**AP-33 · Missing contact and next-step — `m`**
No email, no calendar link, no named ask of the reader.
*Replace with:* a closing slide with a single next action and a reachable address.

**AP-34 · Stage mismatch with the target fund — `C`**
Sending a pre-revenue idea to a fund that requires proven revenue, or a Series A
deck to a pre-seed program. This is a hard stop in
[`scoring-framework.md`](scoring-framework.md).
*Replace with:* run the fund-fit scoring layer before sending anything; see
[`fund-profiles.md`](fund-profiles.md).

### Group 9 — Craft & Design (AP-35 … AP-40 — minor tier, counted in Track A)

**AP-35 · Walls of text — `M`**
Body copy above roughly 30 words per slide on a live deck. YC's design guidance:
legible, simple, obvious — one idea per slide [3].
*Replace with:* headline = the takeaway; body ≤ 3 short lines; detail moves to
speaker notes or appendix.

**AP-36 · Too many slides — `M`**
DocSend's research points to an **18-page pre-seed deck** and a **19–20-page seed
deck** as the structures most likely to hold investor attention [4][5]. YC's demo
day guidance is far more aggressive — **5–7 slides, 2 minutes 30 seconds** [3].
These are different artifacts: a *read-ahead* deck vs a *presented* deck. Confusing
them is itself an anti-pattern.
*Replace with:* two artifacts from one source of truth — a 10–12 slide presented
deck and a 18–20 slide read-ahead.

**AP-37 · Illegible type or low contrast — `M`**
Kevin Hale: legible slides are ones *"even old people sitting in the back row with
bad eyesight can read"* — large type, bold, simple font, good contrast [3].
*Replace with:* minimum 24pt body, high-contrast palette, text anchored top.

**AP-38 · Decorative animation, transitions, memes, stock clip-art — `m`**
YC lists animations, transitions, memes, subtle humour, and accidental humour as
distractions to avoid outright [3].
*Replace with:* white space and one captioned image.

**AP-39 · Sent as `.pptx` instead of PDF — `m`**
Editable files reflow, break fonts, and leak speaker notes. Send a PDF; share a
tracked link if you want read analytics.
*Replace with:* PDF export, ≤ 10 MB, descriptive filename
`Company — Seed — 2026-01.pdf`.

**AP-40 · Numbers inconsistent across slides — `C`**
The market slide says 40M users, the traction slide implies 12M, the financials
imply a different price point. This is the fastest way to lose a technical
investor.
*Replace with:* one canonical metrics sheet, single source, every slide derived
from it. The audit's `check_consistency` pass in `scripts/score_deck.py`
flags repeated figures that disagree.

**AP-41 · Cumulative numbers presented as growth — `M`** *(Series A)*
YC: *"almost every time I've seen cumulative numbers in a Series A deck, it's
because founders are trying to hide their monthly/quarterly numbers because they
don't think they're strong enough."* [7]
*Replace with:* absolute monthly/quarterly values, plus the growth rate.

**AP-42 · Double-axis graphs — `M`** *(Series A)*
YC: *"time is always wasted in clarifying which line goes with which axis, and
then figuring out what those lines mean."* [7]
*Replace with:* two separate single-axis charts, or index both series to 100.

> Note: AP-35 … AP-42 are graded at the Minor/Major tier except AP-40, which is
> Critical because inconsistency is a credibility event rather than a craft issue.

---

## Part 2 — The Positive Patterns (What Actually Works)

These are the replacements, promoted to first-class patterns. They are the
inventory the skill draws on when *authoring* a deck, not just auditing one.

### P-1 · The Insight Lead
Open with the non-consensus belief, then the product. Structure:
`Most people think X. We found Y. That is why Z is now buildable.`
Requires the founder to be able to state what has to be true for them to be wrong.

### P-2 · The Wedge
Beachhead → dominance → expansion → end state. Every successful deck answers
"why this first market" before "how big is the whole market".

### P-3 · Why Now as a dated event
Not a trend. An event with a year: a model release, a price crossing, a rule
change, a platform policy shift. Test: would this slide have been true two years
ago? If yes, rewrite it [5].

### P-4 · Takeaway headline instead of a label
"Market size" is a label. "38,000 US labs spend 11 hours/week on a task that
regulation now requires weekly" is a takeaway. Every slide headline should be
readable on its own as a claim.

### P-5 · Bottom-up sizing with sourced inputs
`reachable accounts × realistic ACV × realistic attach rate`, each input cited.
Then show the top-down ceiling, clearly labelled as the ceiling.

### P-6 · The single hero chart
One chart on the traction slide, annotated with the takeaway written out in words
next to it. Kevin Hale's "explicit" principle: put the conclusion on the slide so
the investor does not have to derive it [3].

### P-7 · Honest competitive positioning
Name direct competitors at your stage, name the substitute (spreadsheet or
do-nothing), and include one row where a competitor wins. This is the pattern that
buys credibility for every other claim in the deck.

### P-8 · Founder-market fit as an achievement line
`Name — Role — what they shipped at what scale, and the one-line link to this
problem.` Not titles; evidence.

### P-9 · Explicit ask with milestones
Round size + instrument + committed amount + close date + use-of-funds buckets
(%) + the milestone each bucket buys.

### P-10 · Unit economics with definitions
LTV, CAC, payback months, gross margin, burn multiple — each with a stated
definition, measurement window, and whether it is observed or modelled.

### P-11 · Two artifacts, one narrative
A 10–12 slide **presented** deck (≤ 30 words per slide, heavy speaker notes) and an
18–20 slide **read-ahead** deck (self-explanatory, appendix depth). Same story,
different information density. See [`narrative-architecture.md`](narrative-architecture.md).

### P-12 · The appendix as the diligence surface
5–8 backup slides: financial model, cohort data, architecture, pipeline detail,
competitor teardowns, reference customers. The appendix is where a sceptical
partner's questions get pre-answered, so it never becomes a slide in the main flow.

### P-13 · The honest gap slide
One slide that names the biggest known weakness and the plan to close it
("retention is 71% M6; the fix ships in March"). Counter-intuitive, and the single
highest-trust move available to a founder, because every investor has already
found the weakness and is watching to see whether you have.

### P-14 · The 5-second test
A stranger reads the first slide for 5 seconds and can say back who the customer
is and what changes for them. Failing this predicts a pass regardless of the rest
of the deck's quality [3].

---

## Part 3 — Where Funds Disagree (Do Not Average These Away)

| Question | a16z | YC | Sequoia |
| :--- | :--- | :--- | :--- |
| Deck length | Long-form thesis tolerated; partner meeting is the artifact [6] | 5–7 slides for demo day; short seed template [1][3] | 10 sections, "if you have financials, include" [2] |
| Market slide | No published market slide; filters on capital-to-milestone alignment and metric definitions [6][6b] | Comes *after* traction in the seed template [1] | "Market potential" is its own required section [2] |
| Competition | Positioning against incumbents is central | Traction and insight outrank competitor grids | "Competition / alternatives" is a named section [2] |
| Financials in deck | Burn multiple pressure-tested pre-meeting [6] | Optional at seed — "if you have it" [1] | "If you have any, please include" [2] |
| Primary gate | Capital-to-milestone alignment + metric vocabulary [6][9] | Growth rate + insight + team [1][6b] | Clarity of thinking + why now + ambition scope [2] |
| Where traction goes | Late; efficiency metrics carry it | Slide 4 (seed), several slides (Series A) [1][7] | Traction is not a named section at all [2] |

**Two more disagreements that must not be smoothed over:**

- **Deck length: 10 vs 18–20.** Funds say 10 slides (YC demo day 5–7, Antler 10,
  500 Global ≤10); the tracking data says 18 pages (pre-seed) and 19–20 (seed).
  The likeliest reconciliation is *sections vs slides* — an 18-page deck of ~10
  content sections plus dividers and appendix. **No source states this**, so this
  skill treats the reconciliation as a hypothesis and reports both numbers.
- **Screenshots: required vs hated.** DocSend's product section is built on
  screenshots, wireframes, and Figma mockups [1][2]; YC's Kevin Hale calls
  screenshots *"almost always illegible, complex, and non-obvious. They break all
  3 rules!"* [3] The scope difference (send-ahead vs on-stage) likely resolves it,
  but neither source acknowledges the other.
- **Agenda slide.** A 2015 First Round piece recommended laying out the map up
  front [11]; modern deck guidance generally does not.

**Implication for the skill:** a single "perfect deck" does not exist. The skill
must produce a **base narrative plus per-fund variants**, never one file for all
targets.

---

## Part 3b — The Survivorship Trap (a warning about studying famous decks)

Libraries of "754 real pitch decks" and "600 decks from the world's best startups"
are widely recommended, and they are dangerous in a specific way. The top comment
on the Hacker News thread that surfaced one such collection:

> *"The archive of pitch decks is really just post hoc confirmation of what were
> excellent, well-timed, and well-executed business plans. Imagine the thousands of
> great pitches that didn't end so well."*

The same thread documents that the collection contained decks that were **not
genuine**, which the curator later removed.

**Rules for using deck libraries:**

1. **Never derive a criterion from a company's success.** Airbnb's deck "worked"
   because Airbnb worked. This skill's criteria come from published fund guidance
   and tracking datasets, not from reverse-engineering winners.
2. **Verify provenance** before treating any deck as exemplary. Indexes
   (`midovislam/awesome-pitch-decks`, `rafaecheve/Awesome-Decks`,
   `starthouse.xyz`, `searchthedeck.com`) host third-party material.
3. **Study decks for structure and craft, not for evidence of causation.** A deck
   is a necessary condition at best. Most passes happen for reasons no deck shows.

Full citation: [`sources-and-attribution.md`](sources-and-attribution.md).

---

## Part 4 — Anti-Patterns Specific to AI-Generated Decks (2024–2026)

Because a large share of decks are now LLM-assisted, these have become reliable
tells of an unedited generation. They are graded as Major.

- **AG-1 · Symmetric bullet triads.** Every slide has exactly three bullets of
  near-identical length. Human decks are lumpy.
- **AG-2 · Em-dash and "not just X, but Y" cadence.** Repeated sentence scaffold
  across slides.
- **AG-3 · Adjective inflation without numbers.** "Significant", "robust",
  "seamless", "cutting-edge" with no unit attached.
- **AG-4 · Invented specificity.** Plausible-looking but uncited statistics
  ("the market is $47.3B"). *Hard stop — fails the deck.*
- **AG-5 · Uniform tone across all slides.** Problem, market, and team written in
  the same register; no voice, no stakes.
- **AG-6 · The generic closing vision.** "We envision a world where…" with no
  connection to the wedge.
- **AG-7 · Placeholder residue.** `[Company Name]`, `[X]%`, `TBD`, `Lorem ipsum`,
  `Insert metric here` surviving into a sent deck. *Critical when sent.*
