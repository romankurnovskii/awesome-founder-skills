# Pitch Deck Audit — Nimbus AI

*Worked example. This is the deliverable format produced by the `pitch-deck` skill
per [`../references/report-template.md`](../references/report-template.md). The
deck audited is [`weak-deck-example.md`](weak-deck-example.md); the raw CLI output
is [`weak-deck-prescreen.md`](weak-deck-prescreen.md).*

---

## 0. Audit Header

| Field | Value |
| :--- | :--- |
| Company | Nimbus AI |
| Deck version audited | `weak-deck-example.md`, 11 slides |
| Artifact type | read-ahead |
| Stage claimed | seed ("raising a seed round") |
| Stage inferred | **indeterminate — no round size, no metrics, no evidence** |
| Raise | unspecified |
| Target funds | a16z, Y Combinator, Antler |
| Audit date | 2026-09-28 |
| Verdict | 🔴 **BLOCKED** |

**Stage-claim check — `FAIL`:** the deck claims a seed round but contains no
revenue, no usage, no round size, and no instrument. A seed deck cannot be graded
at seed standard without seed evidence. Stage claim and stage evidence disagree →
`AC-25 FAIL`, and AP-34 is unresolved until the target funds are matched to the
actual stage.

---

## 1. Executive Verdict

**Do not send this deck to anyone.** It is not a weak version of a good deck; it is
a placeholder for a deck. Five hard stops fire, eleven Critical criteria fail, and
the single most damaging line — *"We have no direct competition"* — guarantees a
pass from any investor who knows the productivity-software space.

The fix is not editing. The narrative does not exist yet: there is no insight, no
dated "why now", no named customer, no product, and no evidence that anyone wants
this. The founder should stop working on the deck and go get ten customer
conversations, one signed pilot, and one real screenshot — then rebuild.

```markdown
| Metric | Score | Target | Status |
| :--- | ---: | ---: | :--- |
| Composite Capital Readiness | 49.1% | ≥ 85% | 🔴 |
| Track B — Acceptance Score | 35.9% | ≥ 85% | 🔴 |
| Track A — Anti-Pattern Index | 39.2% | ≤ 15% | 🔴 |
| Critical fails | 11 | 0 | 🔴 |
| Major fails | 14 | ≤ 2 | 🔴 |
| Best-fund fit | Antler 24% | ≥ 75% | 🔴 |
```

**Hard stops triggered:**

1. Placeholder residue in a sendable deck (`[Your Name]`, `[Company Email]`) — AG-7.
2. No product evidence of any kind — AP-10 / AC-07.
3. No explicit ask (no round size, no instrument) — AP-30 / AC-23.
4. Stage mismatch: a seed claim with zero seed evidence — AP-34.
5. Unsupported figures with no source anywhere in the deck — AP-08 / AC-12.

---

## 2. Fund-Fit Matrix

Evidence tiers per [`../references/fund-profiles.md`](../references/fund-profiles.md).

| Target fund | Evidence tier | Fund Fit | Verdict | Blocking gap |
| :--- | :--- | ---: | :--- | :--- |
| **Antler** | PRIMARY (structure) | **24%** | do not send | AC-03 (problem specificity) — Antler's bar is *"one specific problem, felt by one specific person, in one specific moment"*; this deck has a category, not a person |
| **Y Combinator** | PRIMARY (structure) | **18%** | do not send | AC-06 — YC's idea unit is **problem + solution + insight**; there is no insight anywhere in the deck |
| **a16z** | PRIMARY (metrics only) | **14%** | do not send | AC-25 / AC-18 — no unit economics, no efficiency metric, and the single metric claim ("$50B market") is unsourced. a16z filters on metric definitions |
| **Sequoia** | PRIMARY (structure) | **21%** | do not send | AC-05 — Sequoia's signature demand is "why now?"; this deck has no timeliness argument of any kind |

**Targeting recommendation.** This deck is currently shaped for no fund. It is
closest to being **shaped for a pre-seed narrative**, which means the target list is
wrong too: with zero traction and zero product, the founder should be pitching
**Antler or YC at idea stage** — not a seed round to a16z. The one change that opens
the most funds is **AC-16 (pre-revenue demand evidence)**: one signed pilot converts
this from unfundable to fundable at pre-seed.

**Honesty note.** a16z has no published deck structure; its profile here is
`PRIMARY — metrics only`, and the fit score uses only the emphasis set derived from
its published metric guidance. A `SECONDARY` or `UNVERIFIED` fund would be labelled
as such in this row.

---

## 3. Track A — Anti-Pattern Matrix

All 42 rows. Full machine output: [`weak-deck-prescreen.md`](weak-deck-prescreen.md).

| ID | Anti-pattern | Sev | Status | Evidence from the deck |
| :--- | :--- | :---: | :---: | :--- |
| AP-01 | Feature list instead of an insight | C | **FAIL** | Slide 3 is a four-bullet feature list. No belief statement exists in any slide — verified by reading every slide, not by keyword absence. |
| AP-02 | No "why now" | C | **FAIL** | No why-now section, no dated event, no year. |
| AP-03 | Buzzword soup | M | **FAIL** | 11 hype lexemes: *revolutionizing, next-generation, game-changing, cutting-edge, seamless, best-in-class, world-class, robust, AI-powered*. |
| AP-04 | Jargon that excludes the room | M | PASS | *"Enterprise-grade security"* is the only jargon; not enough to fail. |
| AP-05 | One-liner describes a category | C | **FAIL** | *"Revolutionizing the future of work with an AI-powered productivity platform."* Contains a placeholder-ish brand-free slogan and no customer. |
| AP-06 | Vision with no wedge | M | **WARN** | Big-market language with no beachhead, no first segment, no first customer type. |
| AP-07 | Top-down TAM only | M | **FAIL** | *"1% of the $50B productivity software market"* and *"TAM is $47.3B"*. No bottom-up arithmetic anywhere. |
| AP-08 | Unsourced market numbers | M | **FAIL** | `$50B`, `14% CAGR`, `$47.3B` — zero sources across the whole deck. |
| AP-09 | Market too broad to imply focus | M | **WARN** | *"1% of…"* capture framing. |
| AP-10 | No product evidence of any kind | C | **FAIL** | No screenshot, no demo, no prototype. Not a single image in 11 slides. |
| AP-11 | Mockups as shipping product | C | PASS | No visuals at all, so nothing mislabelled. Vacuous pass — see AP-10. |
| AP-12 | Roadmap as traction | M | PASS | Roadmap and traction are not conflated; there is simply no traction. |
| AP-13 | No proof it works | M | **WARN** | *"A few users have said they love it."* Not quantified, not attributable. |
| AP-14 | Vanity metrics | M | **WARN** | `10,000 downloads`, `5,000 registered users`, `2M impressions`, *"Featured in TechCrunch"*. No active usage, no revenue. |
| AP-15 | Hockey-stick without assumptions | C | **FAIL** | *"2027: $50M ARR. 2028: $200M ARR. 2029: $1B ARR."* Zero stated drivers. This is the single least credible slide. |
| AP-16 | Cherry-picked window | M | PASS | No trend chart exists. |
| AP-17 | No retention where the model requires it | M | **FAIL** | *"5,000 registered users"* with no active-usage or retention figure, for a subscription product. |
| AP-18 | Pre-revenue with zero demand evidence | C | PASS | Deck never claims pre-revenue; the $50M projection implies revenue. Misleading rather than absent — see AP-15. |
| AP-19 | No business model | C | **FAIL** | *"We'll figure out monetization once we reach scale. Freemium is the plan."* This is the exact phrasing Antler names as disqualifying. |
| AP-20 | Unit economics missing | M | **FAIL** | No LTV, CAC, payback, or margin anywhere. |
| AP-21 | Blended metrics as channel metrics | M | PASS | No CAC claimed at all. |
| AP-22 | Margins omitted | M | PASS | No model is specific enough for margins to be applicable. |
| AP-23 | "We have no competition" | C | **FAIL** | *"We have no direct competition. Our only competitors are legacy tools that were not built for the AI era."* Two anti-patterns in one line. |
| AP-24 | Only comparing against giants | M | **FAIL** | The only named comparators are *"legacy tools"*; no peer-stage competitor named. |
| AP-25 | All-checkmark grid | M | PASS | No comparison grid exists. |
| AP-26 | No defensibility | M | **FAIL** | *"Enterprise-grade security"* is a feature, not a moat. No switching cost, data flywheel, or network effect. |
| AP-27 | Advisor-heavy team slide | M | **FAIL** | Slide 9 leads with *"Advisors from Google, Meta, and Stripe."* YC: *"Nobody cares about your advisors."* |
| AP-28 | No founder-market fit | C | **FAIL** | *"smart and hardworking, with experience at top companies"* — no names, no roles, no shipped achievements. |
| AP-29 | Logos instead of people | M | **FAIL** | Employer brands named, no person named, no LinkedIn or GitHub link. |
| AP-30 | Ask buried, vague, or absent | C | **FAIL** | *"We are raising a seed round to accelerate growth and scale the team."* No amount, no instrument, no close date. |
| AP-31 | No use of funds | M | **FAIL** | Zero allocation. *"Scale the team"* is not a use of funds. |
| AP-32 | Valuation anchoring | M | PASS | No valuation stated. |
| AP-33 | Missing contact | m | **FAIL** | `[Your Name], [Company Email]` — a placeholder, not a contact. |
| AP-34 | Stage mismatch with target fund | C | **FAIL** | Seed claim + seed targets, with zero seed evidence. See §0. |
| AP-35 | Walls of text | M | PASS | Slides are short. This is the deck's only genuine strength. |
| AP-36 | Too many slides | M | PASS | 11 slides is within the presented-deck range. |
| AP-37 | Illegible type / low contrast | M | N/A→verify | Not text-detectable; the deck is text-only and has no rendered design. |
| AP-38 | Decorative animation, memes | m | PASS | None detected. |
| AP-39 | Sent as `.pptx` | m | PASS | Markdown source; format check applies at send time. |
| AP-40 | Numbers inconsistent across slides | C | PASS | Only one figure is repeated (`$50B`) and it is consistent. |
| AP-41 | Cumulative numbers as growth | M | PASS | No growth chart exists. |
| AP-42 | Double-axis graphs | M | PASS | No charts exist. |
| **AG-4** | Invented / unsourced specificity | C | **FAIL** | `$47.3B` is precision-shaped and uncited. Twelve figures, zero sources. |
| **AG-7** | Placeholder residue | C | **FAIL** | `[Your Name]`, `[Company Email]`. Non-negotiable hard stop. |

---

## 4. Track B — Acceptance Matrix

All 28 rows.

| ID | Acceptance criterion | Sev | Status | Evidence / remediation pointer |
| :--- | :--- | :---: | :---: | :--- |
| AC-01 | One-line company description | C | **WARN** | Phrase is 11 words but names no customer and is all hype — see §5.1 |
| AC-02 | Title slide completeness | M | **WARN** | One-liner present; no real contact, no date |
| AC-03 | Problem quantified and attributed | C | **FAIL** | *"Modern teams struggle with productivity"* — no number, no who |
| AC-04 | Status quo and its failure mode | M | **FAIL** | No "today they do X, which fails because Y" |
| AC-05 | Why Now dated and falsifiable | C | **FAIL** | No why-now section at all |
| AC-06 | Solution ≤ 2 sentences, concrete benefit | C | **FAIL** | Slide 3 is a feature list; no outcome stated |
| AC-07 | Product evidence, legible | C | **FAIL** | No visual of any kind |
| AC-08 | Visual honesty labels | M | **FAIL** | No visuals, therefore no labels |
| AC-09 | One idea per slide, word budget | M | PASS | Within budget |
| AC-10 | Bottom-up market sizing | M | **FAIL** | Top-down only |
| AC-11 | Entry market (beachhead) named | M | **FAIL** | *"Knowledge workers"* / *"the enterprise"* — no countable segment |
| AC-12 | Every figure sourced and dated | M | **FAIL** | 12 figures, 0 sources |
| AC-13 | Traction with a real growth metric | C | **FAIL** | Downloads and registered users are not growth metrics — AP-14 |
| AC-14 | Hero chart annotated | M | **WARN** | Growth is claimed with no chart and no annotation |
| AC-15 | Retention / cohort evidence | M | **FAIL** | None |
| AC-16 | Pre-revenue demand evidence | C | N/A | Deck does not claim pre-revenue; see AP-15/AP-18 |
| AC-17 | Complete business model | C | **FAIL** | *"We'll figure out monetization later"* |
| AC-18 | Unit economics with definitions | M | **FAIL** | None |
| AC-19 | Capital efficiency metric | M | **FAIL** | None |
| AC-20 | Direct competitors + honest substitute | C | **FAIL** | *"We have no direct competition"* — AP-23 |
| AC-21 | Defensibility with evidence | M | **FAIL** | None |
| AC-22 | Founder-market fit with links | C | **FAIL** | No names, no roles, no achievements, no links |
| AC-23 | Explicit ask | C | **FAIL** | No amount, no instrument, no close date |
| AC-24 | Use of funds tied to milestones | M | **FAIL** | None |
| AC-25 | Consistency, no placeholders | C | **FAIL** | Placeholder residue; also stage claim vs evidence |
| AC-26 | Legibility | M | verify | Requires a rendered deck; the source is text-only |
| AC-27 | Deliverable hygiene | m | verify | Not yet sendable; check PDF export at send time |
| AC-28 | Appendix present | M | **FAIL** | No appendix |

---

## 5. Dimension Deep Dives

### D1 · Company purpose and title

#### AC-01 / AP-05 — One-liner describes a category, not a company — `FAIL` (Critical)

- **Found:** *"Nimbus AI — Revolutionizing the future of work with an AI-powered
  productivity platform. We are the next-generation operating system for teams."*
- **Why it costs the meeting:** "Operating system for teams" describes every
  collaboration tool funded in the last decade. The investor cannot say back who
  the customer is. It also fails YC's reproducibility test — there are no three
  nouns to repeat [9], and no insight component [9].
- **Fix (rewrite):**
  > **Nimbus lets a 40-person engineering team find the decision behind any
  > incident in under two minutes.**
  >
  > *Alternative, if the real wedge is status reporting:*
  > **Nimbus writes the weekly status update for engineering managers, from work
  > already in GitHub and Jira.**

  Both are ≤ 15 words, name a specific who, and state an outcome.

#### AC-02 — Title completeness — `WARN` (Major)

- **Found:** `Contact: [Your Name], [Company Email]`
- **Why it costs the meeting:** a placeholder on slide 1 tells the investor the deck
  has never been read by its own author. This alone moved the pre-screen verdict to
  a hard stop (AG-7).
- **Fix:** `Dana Levi, CEO — dana@nimbus.dev — nimbus.dev` plus the date.

### D2 · Problem and urgency

#### AC-03 / AP-03 — Problem is not quantified and not attributed — `FAIL` (Critical)

- **Found:** *"Modern teams struggle with productivity. Knowledge workers waste time
  switching between too many tools, and collaboration is fragmented across the
  enterprise."*
- **Why it costs the meeting:** Antler's standard is *"one specific problem, felt by
  one specific person, in one specific moment"* [8]. This is a category. Four
  abstract nouns in one sentence; an investor cannot picture the human.
- **Fix:**
  > **A 40-person engineering team loses 11 hours a week hunting for the context
  > behind a decision.** The average incident postmortem takes 6 days to write
  > because the discussion is spread across Slack, Jira, and three PR threads.
  > *(Source: our interviews with 14 engineering managers, Sep 2026.)*

#### AC-04 — No status quo — `FAIL` (Major)

- **Found:** no description of what the customer does today.
- **Fix:** add — *"Today they search Slack manually, ask in #eng-help, or give up
  and re-litigate the decision in the next incident."*

#### AC-05 / AP-02 — No "why now" — `FAIL` (Critical)

- **Found:** nothing.
- **Why it costs the meeting:** Sequoia's signature demand is *"why hasn't your
  solution been built before now?"* [2], and DocSend's dataset found why-now in
  54% of successful decks vs 38% of unsuccessful [9].
- **Fix:** name a dated change, not a trend:
  > **Why now:** three things landed inside 18 months. Slack opened its full
  > history API in 2025. GitHub Copilot-generated PRs tripled review-thread volume
  > in 2026. And remote-first teams stopped having the hallway conversation that
  > used to carry this context. *(Sources: Slack developer changelog, Mar 2025;
  > GitHub Octoverse 2026.)*
  > *If no dated change exists, delete the slide rather than fake it [2].*

### D3 · Solution and product

#### AC-06 / AP-01 — Feature list instead of an insight — `FAIL` (Critical)

- **Found:** slide 3 is *AI-powered assistant · Unified workspace · Smart
  integrations · Enterprise-grade security*.
- **Why it costs the meeting:** YC's idea unit is **problem + solution + insight**
  [9]. There is no insight here, so there is nothing for the investor to fund.
- **Fix:**
  > **Insight:** the context behind a decision already exists — it is just scattered
  > across tools that were never built to be searched together. Nobody needs a new
  > place to *write* decisions. They need one place to *find* them.
  >
  > **Solution:** Nimbus indexes the tool history your team already has and answers
  > "why did we do this?" in natural language. It writes nothing, migrates nothing,
  > and ships in an afternoon.

#### AC-07 / AP-10 — No product evidence — `FAIL` (Critical)

- **Found:** zero images, zero screenshots, zero demo links across 11 slides.
- **Why it costs the meeting:** DocSend found investors spend 59 s on the product
  section at seed — the second-largest block after the business model [5]. There is
  nothing to spend 59 seconds on.
- **Fix:** two cropped screenshots, each captioned with its takeaway (one idea per
  slide, per Kevin Hale [3]):
  > `![The query "why did we drop the Postgres migration" returns the Slack thread, the PR, and the ADR in one view](product-query.png)` — **Live, private beta, 6 teams.**
  > `![Timeline view showing a decision's origin thread, its PR, and its rollout](product-timeline.png)` — **Live.**

### D4 · Market

#### AC-10 / AP-07 — Top-down-only sizing — `FAIL` (Major)

- **Found:** *"We will capture 1% of the $50B productivity software market… TAM is
  $47.3B."*
- **Why it costs the meeting:** Antler: top-down sizing is *"one of the fastest ways
  to lose credibility"*, and *"'we are targeting a $50 billion market and just need
  1% of it'. It means nothing."* [8] YC's default is bottoms-up: *"number of
  prospective customers x value of each customer to you"* [7].
- **Fix (the actual arithmetic):**
  > **Bottom-up:** 118,000 US software companies with 20–200 engineers × $180/seat/year
  > × 40 seats average = **$850M US SAM**. At 22% attach in the first 3 years,
  > **SOM ≈ $187M**. Global SAM ≈ $2.4B.
  > *(Sources: Census SUSB 2025 establishment counts; our pricing data, Q3 2026.)*
  >
  > Delete `$47.3B`. An uncited precision figure is a hard stop (AG-4): it reads as
  > invented, and the first diligence question will expose it.

#### AC-11 — No beachhead — `FAIL` (Major)

- **Found:** *"knowledge workers"*, *"the enterprise"*.
- **Fix:** *"Beachhead: Series A/B US software companies with 20–200 engineers and a
  remote-first engineering org — 118,000 companies, of which 4,100 already run the
  Slack+GitHub+Jira stack we index."*

### D5 · Traction and evidence

#### AC-13 / AP-14 — Vanity metrics — `FAIL` (Critical)

- **Found:** *"10,000 downloads in the first month. 5,000 registered users. 2M
  impressions. Featured in TechCrunch. A few users have said they love it."*
- **Why it costs the meeting:** none of these would hurt if they stopped growing.
  *"A few users have said they love it"* is unattributable and unquantified.
- **Fix:** replace with the smallest real usage evidence:
  > **Active usage:** 41 weekly active engineers across 6 teams (beta). Median 9
  > queries/week/engineer.
  > **Retention:** of 6 teams onboarded in July, 5 still queried in week 12 (83% W12
  > team retention; definition: ≥ 1 query in the trailing 7 days).
  > **Signed:** 2 paid pilots at $1,500/month starting Oct 2026.
  > If none of these exist, say so honestly and show interview evidence instead [8].

#### AC-15 — No retention data — `FAIL` (Major)

- **Found:** none, for a subscription product.
- **Fix:** the W12 team-retention line above, with the definition on the slide.
  Definition-stating is what separates a metric from a claim [6b].

### D6 · Business model and economics

#### AC-17 / AP-19 — No business model — `FAIL` (Critical)

- **Found:** *"We'll figure out monetization once we reach scale. Freemium is the
  plan."*
- **Why it costs the meeting:** this is the exact sentence Antler names as
  disqualifying [8], and DocSend found the business model is the **most-read
  section** at both pre-seed (83 s) and seed (64 s) [4][5].
- **Fix:**
  > **$12/engineer/month, billed annually, minimum 20 seats.** Buyer: VP Engineering.
  > Motion: self-serve trial → founder-led conversion. Gross margin 81% (inference
  > cost ≈ $2.30/seat/month; our infrastructure data, Sep 2026). Free tier capped at
  > 5 seats with 30-day history.

#### AC-18 / AP-20 — No unit economics — `FAIL` (Major)

- **Found:** none.
- **Fix:** a16z's standard requires **definitions** [6b] — use CMGR, net-profit LTV,
  and separate paid from blended CAC:
  > **CAC** $1,180 fully loaded, blended — $2,400 paid, $310 organic, **separately
  > stated per channel** *(our data, Q3 2026, n=9)*.
  > **LTV** $4,900 — net profit, 36-month, 2.1%/month logo churn observed.
  > **LTV:CAC 4.2×** (a16z's stated rough benchmark is 3× [6b]). **Payback 5.9 months.**

#### AC-19 — No efficiency metric — `FAIL` (Major)

- **Found:** none.
- **Fix:** *"Burn multiple 2.1 in Q3 2026 (cash burned ÷ net ARR added, a16z
  definition [6]). Runway 19 months."*

### D7 · Competition and defensibility

#### AC-20 / AP-23 — "We have no competition" — `FAIL` (Critical)

- **Found:** *"We have no direct competition. Our only competitors are legacy tools
  that were not built for the AI era."*
- **Why it costs the meeting:** this is the most reliable single killer in the
  catalog. Antler: *"Nothing makes an investor more suspicious than a founder who
  says they have no competition."* [8] Every investor can name three competitors in
  thirty seconds, and the claim signals either no research or contempt for the
  reader.
- **Fix:** name peers at your stage, the substitute, and **one row where you lose**:
  > **Direct:** Glean (Series F, broad enterprise search — wins on connectors and
  > enterprise trust), Rewind (consumer, wins on price), Notion AI (wins on being
  > already installed).
  > **Substitute:** the senior engineer everyone asks in Slack — free, instant, and
  > the real competitor.
  >
  > | Capability | Nimbus | Glean | Notion AI | The senior engineer |
  > | :--- | :--- | :--- | :--- | :--- |
  > | Slack + Jira + GitHub decision search | Yes | Partial | No | Yes |
  > | Ships in an afternoon | Yes | No | No | Yes |
  > | Enterprise connector catalogue | **No** | **Yes** | Partial | n/a |
  > | Works on day one with no migration | Yes | No | Yes | Yes |
  >
  > Glean wins the enterprise connector catalogue today. We win the 20–200-engineer
  > company where nobody will run a 6-week deployment.

#### AC-21 / AP-26 — No defensibility — `FAIL` (Major)

- **Found:** *"Enterprise-grade security."*
- **Fix:** name one mechanism with evidence:
  > **Moat: decision-graph density.** Every query a team runs teaches the ranking
  > model which threads answer which questions. Across 6 beta teams we now have
  > 11,400 labelled decision→source pairs, and query-to-answer accuracy rose from
  > 61% to 84% in 9 weeks. A new entrant starts at zero, and the dataset is not
  > downloadable from Slack or GitHub.

### D8 · Team

#### AC-22 / AP-27 / AP-28 / AP-29 — Advisor-led, unnamed, no fit — `FAIL` (Critical)

- **Found:** *"Advisors from Google, Meta, and Stripe. The founding team is smart and
  hardworking, with experience at top companies."*
- **Why it costs the meeting:** YC: *"This should be about founders. Nobody cares
  about your advisors."* [7] There are no names to reference-check, no roles, and no
  reason these people win this problem.
- **Fix:**
  > **Dana Levi, CEO** — built and sold the internal search layer at MedSynth (acq.
  > 2021); ran it for 900 engineers who used it daily. `linkedin.com/in/danalevi`
  > **Ari Cohen, CTO** — led Slack's search relevance team for 4 years.
  > `github.com/aricohen`
  >
  > *Why us:* we have each been the senior engineer answering the same question for
  > the tenth time, and we built the thing that stopped us.
  >
  > Advisors: move to the appendix, and only if they are doing work.

### D9 · The ask

#### AC-23 / AC-24 / AP-30 / AP-31 — No ask, no use of funds — `FAIL` (Critical)

- **Found:** *"We are raising a seed round to accelerate growth and scale the team."*
- **Why it costs the meeting:** YC: *"The ask is the climax of your whole deck…
  weirdly, I've seen many decks without one."* [7] a16z's stated standard is
  **capital-to-milestone alignment** — *"it's all about the alignment of capital to
  milestones"* [6b].
- **Fix:**
  > **Raising $2.5M SAFE** with a $20M post-money cap. **$400k committed** from two
  > insiders. **Closing 15 December 2026.**
  >
  > **Use of funds — each bucket buys a milestone:**
  > - **45% engineering** → ship the 6 enterprise connectors that unlock deals above
  >   200 seats
  > - **30% GTM** → 2 AEs; reach 40 paying teams
  > - **15% security** → SOC 2 Type II, required by 3 of 5 pipeline accounts
  > - **10% buffer** → 21 months runway
  >
  > **This reaches $1M ARR and Series A readiness in 18 months.**
  >
  > *Note: state the round size, not a valuation expectation — a16z warns against
  > opening conversations with price expectations [6]. A price cap inside a SAFE is
  > a structure term; if the founder prefers to keep it out of the deck, say
  > "SAFE, terms on request".*

### D10 · Integrity

#### AC-25 / AG-4 / AG-7 — Placeholders and unsourced precision — `FAIL` (Critical)

- **Found:** `[Your Name]`, `[Company Email]`, `$47.3B`, `14% CAGR`, `$50B` — 12
  figures, zero sources.
- **Why it costs the meeting:** invented specificity is worse than a gap. `$47.3B`
  reads as researched and is not; the first diligence question exposes it, and the
  founder's credibility goes with it.
- **Fix:** every figure gets `(Source, Year)` or *"our estimate"*. Placeholders
  become real values or the slide is deleted.

---

## 6. The Missing-Numbers Ledger

| # | Slide | Claim | Status | How to source it |
| --: | :--- | :--- | :--- | :--- |
| 1 | 4 | `$50B productivity software market` | **UNSOURCED** | Replace with bottom-up SAM; source the establishment count |
| 2 | 4 | `14% CAGR` | **UNSOURCED** | Cite a named research source with a year, or delete |
| 3 | 4 | `TAM is $47.3B` | **UNSOURCED — precision-shaped** | Delete. Precision without a source reads as invented |
| 4 | 5 | `10,000 downloads` | Unattributed | State the measurement window and the source system |
| 5 | 5 | `5,000 registered users` | **Undefined** | Define "registered"; add active usage |
| 6 | 5 | `2M impressions` | Vanity | Delete |
| 7 | 5 | `A few users have said they love it` | **Unattributable** | Replace with named quotes and usage counts, or delete |
| 8 | 8 | `$50M / $200M / $1B ARR` | **Unsourced projections** | Add the 3 drivers per year, or delete the slide |
| 9 | 1 | `[Your Name]`, `[Company Email]` | **PLACEHOLDER — hard stop** | Insert the real founder name and address |
| 10 | 10 | "a seed round" | **No amount** | State the raise, the instrument, and the close date |

A non-empty ledger with `UNSOURCED` rows is itself a verdict floor of 🔴.
**This audit has not filled any of these gaps. It has only listed them.**

---

## 7. Prioritised Remediation Plan

Ranked by gate-clearing impact ÷ effort. Ten items maximum.

| Rank | Fix | Clears | Effort | Owner | Done? |
| --: | :--- | :--- | :--- | :--- | :---: |
| 1 | Delete every placeholder; insert the real name and contact | AG-7, AC-02 | 5 min | founder | ☐ |
| 2 | Go get 10 customer conversations and write them up | AC-03, AC-04, AC-16 | 1 week | founder | ☐ |
| 3 | Convert 1 warm relationship into a signed paid pilot | AC-16, AC-13 | 2 weeks | founder | ☐ |
| 4 | Rewrite the one-liner to name a customer and an outcome | AC-01, AP-05 | 30 min | founder | ☐ |
| 5 | Rewrite competition with real peers and one losing row | AC-20, AP-23, AP-24 | 2 h | founder | ☐ |
| 6 | Build the bottom-up market model; delete `$47.3B` | AC-10, AC-11, AP-07, AP-08, AG-4 | 3 h | founder | ☐ |
| 7 | Add the insight slide and the date-anchored why-now | AC-06, AC-05, AP-01, AP-02 | 2 h | founder | ☐ |
| 8 | Replace features with 2 captioned product screenshots | AC-07, AC-08, AP-10 | 2 h | founder | ☐ |
| 9 | State the round size, use of funds, and milestones | AC-23, AC-24, AP-30, AP-31 | 2 h | founder | ☐ |
| 10 | Rebuild the team slide as achievement lines with links | AC-22, AP-27…29 | 1 h | founder | ☐ |

**Before sending anything:** rows 1, 4, 5, 6, 9.
**Before sending to a top-decile fund:** everything above, plus 2, 3, 7, 8, 10.
**Before the partner meeting:** add the appendix (financial model, cohort detail,
architecture, pipeline, reference customers).

---

## 8. Per-Fund Variant Notes

**No variants are produced for this deck.** A variant changes slide order and
emphasis; it must never change a number, add a claim, or drop a Critical criterion.
This deck fails enough Critical criteria that every fund-specific variant would be
a rearrangement of unsupported claims. The correct output is a gap report.

Once rows 1–10 above are complete, the variants would be:

### Variant — Antler (pre-seed, if the pilot does not close)
- **Reorder:** open on the problem (Antler has no purpose slide) [8]; move team to
  slide 2–3 [12].
- **Expand:** problem specificity (person, moment, cost) and go-to-market channels.
- **Framing line:** *"We interviewed 14 engineering managers; 11 described the same
  six-day hunt for context."*
- **Do not send if:** the problem slide still describes a category rather than a
  person.

### Variant — Y Combinator (seed)
- **Reorder:** traction to slide 4, before market size [1].
- **Expand:** insight, traction, and founder-market fit. Add the "more metrics"
  slide [1].
- **Framing line:** use the X-for-Y test — *"X"* must be a household name, *"Y"*
  must want it, and *"Y"* must be huge [9].
- **Do not send if:** there is no insight statement (YC's idea unit requires one [9]).

### Variant — a16z (metrics-led)
- **Expand:** unit-economics definitions (net-profit LTV, paid vs blended CAC, CMGR,
  burn multiple), capital-to-milestone alignment, and the use-of-proceeds table [6][6b].
- **Framing line:** *"$2.5M buys 6 connectors and 40 paying teams; that is the Series
  A evidence set at a 12-month horizon."*
- **Do not send if:** any metric is undefined. a16z's filter is the definition
  itself, not the slide [6b].

### Variant — Sequoia
- **Reorder:** to the current ten sections, with **why now** before market and
  **vision** (not product) as the final section [2].
- **Expand:** why-now and the five-year vision.
- **Do not send if:** there is no dated why-now [2].

---

## 9. Attestation

- Every number in this audit is either quoted from `weak-deck-example.md` or
  explicitly absent from it.
- No estimate, benchmark, market figure, or metric has been introduced by this
  audit. The bottom-up model in §5 D4 is a **worked illustration of the required
  form**, with its inputs labelled as illustrative — it is not a claim about Nimbus.
- Fund Fit scores use the emphasis sets in
  [`../references/fund-profiles.md`](../references/fund-profiles.md); the a16z row is
  `PRIMARY — metrics only` and is labelled as such.
- Audited artifact: `weak-deck-example.md`, 11 slides.
- Audit performed against `acceptance-criteria.md` and
  `patterns-and-antipatterns.md` at version 1.0.0, and the deterministic pre-screen
  `score_deck.py` v1.0.0.
