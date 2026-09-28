# Sources & Attribution

Every claim in this skill's references traces to one of the sources below. This
file states what each source is, what tier of evidence it provides, and what it
does **not** support.

Retrieval date for all sources: **2026-09-28**.

The full raw research corpus — including the sitemap sweeps that produced the
negative findings below — is preserved in
[`research-corpus.md`](research-corpus.md).

---

## Evidence tiers

| Tier | Meaning | How it may be cited |
| :--- | :--- | :--- |
| **T1 — Fund's own words** | Published directly by the fund, verbatim | May be quoted as the fund's guidance |
| **T2 — Dataset research** | Quantitative research on decks, with a stated method | May be cited with the number and the source; do not generalise beyond the sample |
| **T3 — Fund's research, not deck guidance** | The fund publishes metrics/frameworks, not slide instructions | May be used to infer emphasis, **must be labelled as inference** |
| **T4 — Third-party / community** | Aggregators, repos, forums, secondary reporting, SEO content | Context only; never cited as a fund's requirement |

---

## The headline negative finding

**Only three sources publish an explicit, ordered, slide-by-slide deck structure
on their own domain: Sequoia, Y Combinator, and DocSend (which is not a fund).**

The following named funds were checked by full sitemap sweep and publish **no
canonical deck structure**: a16z, Bessemer, Index Ventures, Accel, Lightspeed,
Greylock, Redpoint, Founders Fund, Benchmark, Coatue, Insight Partners, and
First Round.

This matters because the search results that dominate for "Accel / Founders Fund /
Bessemer — How to Pitch" are SEO content farms (`foundra.ai/vc/*`,
`vcmatch.ai/investors/*`, `pitchgrade.com/blog/*`, `hummingdeck.com/blog/*`,
`inknarrates.com`, `deckary.com`, `bestpitchdeck.com`), **not fund publications**.
Citing them as fund positions is a fabrication.

Two concrete negative findings:

- **a16z has no pitch-deck page.** A sweep of `a16z.com/post-sitemap{,2,3}.xml` and
  `page-sitemap.xml` (744 URLs) for `pitch|deck|fundrais|narrative|story` found no
  deck-template article. `a16z.com/how-to-build-a-pitch-deck/` returns HTTP 404.
- **First Round Review has no pitch-deck teardown series.** A sitemap sweep of
  `review.firstround.com/sitemap-posts.xml` returns four deck-adjacent posts, none
  a teardown. "Pitch deck teardown" is a **TechCrunch** franchise, not First
  Round's.

---

## T1 — Fund's own published words

### [1] Y Combinator — *How to build your seed round pitch deck* (Aaron Harris)
<https://www.ycombinator.com/library/2u-how-to-build-your-seed-round-pitch-deck>

- **Type:** T1. The 11-slide seed template with the author's commentary per slide.
- **Supports:** the seed slide order in
  [`narrative-architecture.md`](narrative-architecture.md) §1.2; the "slide set
  n ≤ 3" rule; "nobody cares about your advisors" (AP-27, AC-22).
- **Verbatim anchors:** *"Focus on narrative. The rest is commentary."*;
  *"This should be about founders. Nobody cares about your advisors."*
- **Does not support:** the Series A bar (see [7]) or any claim that YC requires a
  specific deck length. The template is a suggested layout, not a rule.
- **Caveat:** published 2018. Still the canonical published YC seed structure, but
  it predates the current AI-cycle deck norms.

### [2] Sequoia Capital — *Writing a Business Plan*
<https://sequoiacap.com/article/writing-a-business-plan/>

- **Type:** T1. Sequoia's ten-section structure, republished with refinements.
- **Supports:** the ten sections in
  [`narrative-architecture.md`](narrative-architecture.md) §1.1; company purpose as
  a single declarative sentence (AC-01); "why now" as a named section (AC-05);
  competition with "a plan to win" (AC-20); financials optional (*"If you have any,
  please include"*).
- **Version warning (material):** the widely circulated **2015 SlideShare version**
  of this template had a different order and a separate **Product** section. The
  current published order **replaces Product with Vision**. Most third-party guides
  still reproduce the superseded 2015 order. **Do not tell a founder Sequoia
  requires a Product slide — the current template does not.**
- **Does not support:** any claim that Sequoia scores decks on template
  completeness. Sequoia de-emphasises the slides in the same article.
- **Caveat:** the article is partly brand marketing around the AirBnB story. The
  template is T1; the causal claim about AirBnB is not evidence that the template
  causes funding.

### [3] Y Combinator — *How to design a better pitch deck* (Kevin Hale)
<https://www.ycombinator.com/library/4T-how-to-design-a-better-pitch-deck>

- **Type:** T1, scoped to **demo-day / presented** decks, not read-ahead decks.
- **Supports:** the legible/simple/obvious/explicit framework (AC-26, AC-14,
  AC-09); the 5–7 slide demo-day target; the distraction list to remove
  (AP-38); the hostility to raw screenshots; the 5-second stranger test.
- **Does not support:** the 18–20 slide read-ahead length. Hale's guidance is about
  a **2 min 30 s stage presentation to ~1,000 investors**. Applying his slide-count
  advice to a read-ahead deck is a documented misreading, and this skill explicitly
  separates the two artifacts (AP-36, P-11).
- **Caveat:** written in **2016**, for on-stage Demo Day. YC's own 2020 Series A
  guide supersedes it for video-call pitching [7].

### [6] a16z — *The 16 Commandments of Raising Equity in a Challenging Market*
<https://a16z.com/the-16-commandments-of-raising-equity-in-a-challenging-market/>

- **Type:** T1 for fundraising process; **T3 for deck structure** — it prescribes no
  slides.
- **Supports:** burn multiple as a pressure-test (AC-19); "be deliberate and precise
  on use of proceeds", burn-sinks vs burn-investments (AC-24); "don't begin
  conversations with price expectations" (AP-32); "ask yourself the difficult
  questions" — anticipating retention and CAC objections (P-13).
- **Explicit a16z definition used in this skill:** burn multiple = **cash burned
  divided by net ARR added** [6].
- **Does not support:** any slide-by-slide a16z deck template. **a16z publishes no
  canonical public deck template**, and **the phrase "what is the secret" is not an
  a16z criterion** — it does not appear on any a16z page located in this research.
  Attributing it to a16z is a fabrication.
- **Caveat:** published May 2023 in a specific market environment (post-2022
  correction, SVB). The structural advice is durable; the timing framing is dated.

### [6b] a16z — *16 Startup Metrics*, *Why do investors care so much about LTV/CAC?*, and *16 Common Questions About Fundraising*
<https://a16z.com/16-startup-metrics/> ·
<https://a16z.com/why-do-investors-care-so-much-about-ltvcac/> ·
<https://a16z.com/16-common-questions-about-fundraising/>

- **Type:** T1 for metrics vocabulary; **T3 for deck structure.**
- **Supports:** a16z evaluates decks through **metric definitions**, which is a
  different filter from slide order. Specific positions:
  - *"A common mistake is to use bookings and revenue interchangeably… Letters of
    intent and verbal agreements are neither revenue nor bookings."* → AC-25,
    AC-13.
  - **Paid CAC should be distinguished from blended CAC.** → AP-21, AC-18.
  - Use **CMGR**, not a simple-average MoM growth rate. → AC-14.
  - **LTV must be net profit**, not revenue or gross margin. → AC-18.
  - **3x LTV:CAC is a16z's own stated rough benchmark:** *"Investors often use 3x
    LTV/CAC as a rough benchmark… improving your LTV/CAC from 2x to 3x can nearly
    triple your valuation."* → AC-18 threshold.
  - **Capital-to-milestone alignment:** *"regardless of what a round is called
    (seed, series A, B, C, etc.), it's all about the alignment of capital to
    milestones."* → AC-24.
  - **A deck is mandatory:** *"Do I really need to prepare a full slide deck? …
    Don't leave anything to chance. Take time to prepare a full deck and practice,
    including creating a script and doing dry-runs."* → AP-30 is never optional.
- **Caveat:** the first two pieces are from **2015**. The metric definitions aged
  well; the round-timing content did not.
- **Also:** the a16z Games Fund One deck, published with GP Andrew Chen's
  commentary, is a rare live a16z deck — structure: industry context → **"why now"
  slide** → investment areas → team/operating model. **T4/secondary** for
  structure; useful as an existence proof, not a template.

### [7] Y Combinator — *How to build a great Series A pitch and deck*
<https://www.ycombinator.com/library/8d-how-to-raise-a-series-a>

- **Type:** T1. The Series A structure, slide by slide, with quantified standards.
- **Supports:** the Series A structure in
  [`narrative-architecture.md`](narrative-architecture.md) §1.7; **at least 4–6
  months of trend** for believable growth; the bottoms-up market formula
  (*"number of prospective customers x value of each customer to you"*, AC-10);
  the prohibition on **cumulative numbers** and **double-axis graphs** (AP-41,
  AP-42); "the ask is the climax of your whole deck… weirdly, I've seen many decks
  without one" (AP-30, AC-23); the appendix as the Q&A surface (AC-28); "optimize
  for clarity and understanding, not beauty" (AC-26).
- **Verbatim anchors:** *"almost every time I've seen cumulative numbers in a
  Series A deck, it's because founders are trying to hide their monthly/quarterly
  numbers"*; *"Remove anything else - yes, this means leaving off the headshots for
  every employee in your 12 person team"*; *"Two of the most common culprits here
  are fancy, complicated diagrams that are hard to understand or colorful images
  that look nice but don't help illustrate your point."*
- **Team-slide signalling risk (unusually specific):** *"if you include a Series A
  fund on the list of existing investors, you'll be asked whether or not they're
  leading your round… In general, best to leave those logos off."* → AP-29.
- **Dead-linked benchmark pages (significant gap):** YC's Series A guide links
  `library/1k-benchmarks` and `library/1z-the-importance-of-trends`; **both now
  return HTTP 404.** YC's actual ARR/growth thresholds are therefore **not
  currently retrievable from the primary domain**, and this skill does not state
  them.
- **Does not support:** pre-seed or seed norms. This is a Series A artifact.

### [8] Antler — *What a VC Wants to See in Your Pitch Deck*
<https://www.antler.co/blog/what-a-vc-wants-to-see-in-your-pitch-deck>

- **Type:** T1. A pre-seed-specific, 10-slide structure written by an Antler
  investor, interleaving slide content with "what the VC is thinking".
- **Supports:** the pre-seed slide set in [`fund-profiles.md`](fund-profiles.md);
  the problem standard — *"One specific problem, felt by one specific person, in
  one specific moment"* (AC-03, AP-05); rejection of top-down sizing (AP-07);
  rejection of "we have no competition" (AP-23); the milestone bar for the ask
  (AC-24); *"the order doesn't matter; your storytelling does."*
- **Verbatim anchors:** *"'Small businesses struggle with cash flow' is not a
  problem."*; *"Top-down market sizing is one of the fastest ways to lose
  credibility in a pitch."*; *"Every investor has seen 'we are targeting a $50
  billion market and just need 1% of it'. It means nothing."*; *"A founder who says
  'we'll figure out monetisation later' is a founder who hasn't thought hard enough
  about their customer."*
- **Structural note:** Antler's order has **no company-purpose slide**; it opens on
  the problem. Their order is: problem · solution · market · traction · business
  model · competition · **go-to-market** · team · financials · ask.
- **Caveat:** published on Antler's marketing blog, first-person from one investor.
  It reflects stated practice, and Antler is an accelerator rather than a
  top-decile US venture fund. Its value here is that it publishes the **most
  specific pre-seed problem standard** located in this research.

### [9] Y Combinator — *How to pitch your startup*
<https://www.ycombinator.com/library/6q-how-to-pitch-your-startup>

- **Type:** T1.
- **Supports:** the **idea unit = problem + solution + insight** framing; the
  evaluative questions a partner actually asks (*"Do I understand it? Am I excited
  by it? Do I like the team and do I wanna work with them?"*); the **X-for-Y three
  tests** (X must be a household name; Y must want X; Y must be huge — with
  *"Buffer for Snapchat"* as the failure case); the **reproducibility test** (a
  listener should be able to repeat three nouns: what you're making, the problem,
  the customer); de-emphasis on selling (*"I do not need you to sell me as a YC
  partner"*).
- **Supports AP-01/AC-06** directly: the insight is a required component of the
  idea, not a nice-to-have.
- **Caveat:** ~2017–18, references then-current batch companies. Framework durable,
  examples stale.

### [12] Techstars — *Why most pitch decks don't work*
<https://www.techstars.com/blog/founder-advice/why-most-pitch-decks-dont-work-and-how-to-make-sure-yours-does>

- **Type:** T1.
- **Supports:** the deliberate anti-template position described in
  [`narrative-architecture.md`](narrative-architecture.md) §1.4 — write the
  long-form script first, no fixed order (*"Sometimes the team should be first"*),
  vision + dated momentum, and the text-density rule (*"People will listen, or they
  will read. They will not do both."*).
- **Supports AP-14** by broadening momentum beyond revenue: *"When we say momentum,
  we don't always mean revenue and user traction."*
- **Outreach anti-patterns (T1, not deck-specific):** non-personalised cold email,
  six-paragraph emails, email blasting, **false urgency** (*"immediate red flag for
  us"*), and **AI mass personalisation** (*"In the age of agents and LLMs… Don't do
  it. We can tell when it comes as a mass blast."*).
- **Caveat:** part 2 of a 4-part marketing series with application CTAs.

### [13] 500 Global — *Pitch Perfect: how to make a standout pitch deck for 500 Global*
<https://latam.500.co/content/pitch-perfect-how-to-make-a-standout-pitch-deck-for-500-global>

- **Type:** T1.
- **Supports:** the 10-slide structure in
  [`narrative-architecture.md`](narrative-architecture.md) §1.5; the two copy
  formulas; the **> $1B market floor**; the anti-pattern *"saying you're the 'first'
  to do something often shows a lack of knowledge about your space"* (AP-05/AP-24).
- **Caveat:** a regional site (LATAM) with an application funnel; the market floor
  is a programme-specific rule, not an industry standard.

---

## T2 — Dataset research

### [4] DocSend — *Building your pre-seed pitch deck*
<https://www.docsend.com/blog/what-to-include-when-building-your-pre-seed-pitch-deck/>

### [5] DocSend — *What VCs really want to see inside your seed deck*
<https://www.docsend.com/blog/what-vcs-really-want-to-see-inside-your-seed-deck/>

- **Type:** T2. Deck-structure benchmarks from DocSend's document-tracking data
  (time per section, pages per section, read time), published as aggregate guidance.
- **Numbers used in this skill:**

  | Figure | Value | Source |
  | :--- | :--- | :--- |
  | Average VC read time, **seed** deck | **3 min 44 s** | [5] |
  | Average VC read time, **pre-seed** deck | **4 min 10 s** | [4] |
  | Seed deck **completion rate** | **58% viewed to completion** | [5] |
  | Pre-seed deck → meeting rate | **1–2%** | [4] |
  | Decks per VC per week | **100+** | [4] |
  | Extra traction scrutiny in decks that **failed** to raise | **+80%** time | [4] |
  | Target deck length, seed | **19–20 pages**, 12 sections | [5] |
  | Target deck length, pre-seed | **18 pages**, 12 sections | [4] |
  | Most-read seed sections | **business model 64 s**, product 59 s | [5] |
  | Most-read pre-seed sections | **business model 83 s**, product 77 s | [4] |
  | Section-order correlation | decks opening purpose → problem → solution → market raised at a higher rate | [5] |
  | DocSend's own unit-economics targets | LTV:CAC **≥ 3:1**; CAC payback **< 12 months** | [4] |

- **Version caveat (material):** an **older snapshot of the seed page**, served via
  a migrated `/twi/` URL, states **3 min 20 s**. The current page states **3 min
  44 s**. This skill uses the current figure and flags the discrepancy rather than
  picking the more flattering number.
- **Method caveat:** the data comes from decks **sent through DocSend**, biasing the
  sample toward founders and investors who use DocSend link tracking. It measures
  *attention*, not *outcomes*, except the ordering finding, which is reported as a
  raise-rate correlation.
- **Does not support:** any causal claim that a 19-page deck *causes* funding, or
  that a 10-slide deck is worse.

### [9] DocSend — *Why the "Why Now" slide is more important than ever*
<https://www.docsend.com/blog/why-now-slide>

- **Type:** T2, from the **2020 DocSend Startup Index**.
- **Numbers used in this skill:**

  | Figure | Value |
  | :--- | :--- |
  | "Why Now" slide present in successful decks | **54%** |
  | "Why Now" slide present in unsuccessful decks | **38%** |
  | Additional time on Why Now in funded decks | **+36%** |
  | Recommended position | between the Problem and Solution slides |

- **Method caveat (material):** a **correlation from a single market period (2020,
  COVID-era)**. Deck-level editorial choices correlate with unobserved
  founder-quality variables. This is a strong reason to *include* a why-now slide,
  and **not** evidence that adding one improves your odds.

### [10] Papermark — *Pitch deck metrics*
<https://www.papermark.com/pitch-deck-metrics>

- **Type:** T2, independent of DocSend. ~3,000 decks tracked Jan–Dec 2024.
- **Numbers used:** **3.2 min** average complete review; **page 1 = 23 s**;
  **pages 2–10 ≈ 15 s each**; **9–16 pages = 49% of decks**.
- **Caveat:** platform-specific sample. The page-1/page-2-10 split is a more
  actionable shape than the aggregates, but it is not a benchmark any fund endorses.

### [11] Storydoc — *Pitch deck statistics* (via hummingdeck's 2026 benchmark summary)
<https://www.storydoc.com/blog/pitch-deck-statistics>

- **Type:** T2, platform-specific and interactive-deck-shaped.
- **Numbers used:** **31%** of sessions end within 10 s; **82%** of sessions that
  reach slide 4 finish; **team slide = 43%** of reading time.
- **Critical caveat:** Storydoc measures **interactive decks on Storydoc**, a
  different artifact from a PDF read-ahead. **Its "team slide dominates" finding is
  not DocSend's** — see the mis-citation list below.

### [14] NBER — *Survey of VC decision criteria* (Working Paper 22587)
<https://www.nber.org/papers/w22587>

- **Type:** T2, academic. 885 VCs across 681 firms.
- **Finding used:** the **management team** is selected most often as the most
  important factor in investment decisions.
- **Critical distinction:** this is a survey of **stated criteria**, not measured
  reading time. It does not say VCs spend the most *time* on the team slide.

---

## T3 — Fund research that informs but does not prescribe the deck

### [15] Bessemer Venture Partners — cloud metrics research
*Scaling to $100M*, *From Start to Centaur*, *State of the Cloud* —
<https://www.bvp.com/atlas>,
<https://www.bvp.com/assets/uploads/2024/04/From-Start-to-Centaur-The-founders-roadmap-to-100-million-ARR-Bessemer-Books-Edition-040924.pdf>

- **Type:** T3. Bessemer publishes cloud-efficiency frameworks (net revenue
  retention, burn multiple, CAC ratio, magic number, gross margin) and memos —
  **not a deck template.** A sitemap check of bvp.com returns only memos and
  roadmaps.
- **Explicit correction:** the "**Bessemer pitch deck template**" that circulates
  online **is not a bvp.com artifact**. Treat it as unverified.
- **Used in this skill for:** the *inference* that Bessemer-weighted decks should
  carry cohort retention and an efficiency metric
  ([`fund-profiles.md`](fund-profiles.md) Tier 2). **That mapping is this skill's
  inference and is labelled `SECONDARY` there.**

### [16] First Round — partner meeting and storytelling
- *What you can really expect when pitching at a VC partner meeting* (2024) —
  <https://review.firstround.com/heres-what-you-can-really-expect-when-pitching-your-seed-stage-startup-at-a-vc-partner-meeting/>
  — **T1**. A partner meeting is **60 minutes with 5–15 investors** (vs 30–45 min
  for a 1:1); offer rate **25–60%** after a partner meeting, with roughly **5%**
  conversion after a 1:1. Bring slides: *"for partner meetings, it is almost always
  recommended to come with slides"* plus *"a large appendix of slides for your eyes
  only."* The **investment memo** structure (the artifact the partner actually
  writes) is: founder backgrounds · market overview and problem · solution/product ·
  big vision · GTM · traction · team · competitive landscape.
- *Tell stories like this* (Oren Jacob, **2015**) —
  <https://review.firstround.com/tell-stories-like-this-to-take-your-fundraising-pitch-from-mediocre-to-memorable/>
  — **T3, dated**. **12 slides** (starts at 60–70), *"Lay out the map for them at
  the beginning"*, *"10 slides of nerdy graphs in the appendix"*, *"You should be
  able to give your pitch with no slides. Cold."*, *"Never read your slides."*
  This is the origin of the agenda-slide advice, and it is **not re-endorsed** in
  First Round's 2024 piece.
- **Explicit correction:** First Round publishes **no deck-structure guide and no
  teardown series**.

### [17] Greylock, Index Ventures, Lightspeed, Accel, Founders Fund, Redpoint, Benchmark, Coatue, Insight Partners
- **Type:** T3/T4 — **no canonical public deck template located** for any of these.
- Greylock: a sitemap sweep of 290 posts found one deck-adjacent hit, a
  `startup-storytelling` post that **now 404s** and concerned corporate comms. The
  frequently cited Greylock Series A presentation is **Business Insider reporting**
  (2021, paywalled), not a Greylock publication. **Unverified.**
- Index Ventures: their published guides are *Rewarding Talent*, *Winning in the
  US*, and *Scaling Through Chaos*. Deck tips attributed to them come from
  Pitch.com and Business Insider. **Secondary.**
- Lightspeed: closest is a **TechCrunch** interview about Grafana's Series A deck.
  Usable detail: the slide that moved the partnership was a **visual** showing
  dashboards at recognisable brands — *"That just emotionally resonates with people
  when you're thinking about investing in a company."* **Secondary.**
- Insight Partners: a relevant page exists
  (<https://www.insightpartners.com/ideas/how-should-i-prepare-for-a-fundraising-meeting-with-insight/>)
  but its body **did not render** past a cookie wall. **Contents unverified.**
- **Explicit statement:** this skill does **not** claim these funds require
  particular slides. Where [`fund-profiles.md`](fund-profiles.md) lists an emphasis
  set for them, it is an inference from publicly stated investment themes and is
  labelled `SECONDARY`. Every such inference must be labelled in audit output.

---

## T4 — Community and third-party resources

Informed the catalog's exhaustiveness; **not** cited as authoritative.

| Source | URL | What it is | Caveat |
| :--- | :--- | :--- | :--- |
| `joelparkerhenderson/pitch-deck` | <https://github.com/joelparkerhenderson/pitch-deck> | Index of deck advice, templates, and readings | Aggregator; repository v4.1.0, updated 2022 |
| `midovislam/awesome-pitch-decks` | <https://github.com/midovislam/awesome-pitch-decks> | **754 real decks** (Airbnb 2008 → Series E), Google Drive index | Third-party property; study only |
| `rafaecheve/Awesome-Decks` | <https://github.com/rafaecheve/Awesome-Decks> | Curated list of public deck slides | Verify provenance before treating any deck as exemplary |
| `emotixco/claude-skills-founder` | <https://github.com/emotixco/claude-skills-founder> | Agent-skill pack with a `/pitch-deck` skill producing a 12-slide outline | **Prior art, not a source.** Its contribution is the "ask before inventing" eval — a skill that invents a company when given none is deemed to have failed. This skill adopts that as a non-negotiable rule. |
| `len5ky/synth-personas` | <https://github.com/len5ky/synth-personas> | Fans out LLM calls across ~150 personas to score a deck | Prior art for multi-persona review; not used as evidence |
| `SixArm/pitch-deck-template` | <https://github.com/sixarm/pitch-deck-template> | A deck template | Community template |

### Community discussions (Hacker News)

Retrieved via the HN Algolia API on 2026-09-28.

| Thread | Points / comments | URL |
| :--- | :--- | :--- |
| I've collected over 600 pitch decks | 606 / 87 | <https://news.ycombinator.com/item?id=23305196> |
| How to Build a Great Series A Pitch and Deck | 377 / 37 | <https://news.ycombinator.com/item?id=24780152> |
| The pitch deck that helped us get an $865M valuation | 301 / 79 | <https://news.ycombinator.com/item?id=8768372> |
| Presentations and pitch decks by failures and frauds | 163 / 34 | <https://news.ycombinator.com/item?id=35743778> |
| Show HN: Search inside 15,000 pitch deck slides | 219 / 36 | <https://news.ycombinator.com/item?id=34551000> |

**Two community findings that materially qualify the rest of this skill:**

1. **Survivorship bias in deck archives.** The top comment on the 600-deck thread:
   > *"The archive of pitch decks is really just post hoc confirmation of what were
   > excellent, well-timed, and well-executed business plans. Imagine the thousands
   > of great pitches that didn't end so well. I have seen many excellent teams with
   > great pitches that failed for reasons entirely outside their control."*

   **Implication:** studying 754 famous decks teaches you what funded companies
   happened to have, not what caused funding. This skill does not derive any
   criterion from the success of a deck's company, and neither should a founder.
   The criteria here come from published fund guidance and tracking datasets, not
   from reverse-engineering winners.

2. **Deck archives contain misattributed material.** In the same thread, the
   collection's author conceded the set contained decks that were not genuine:
   *"I've taken the FB deck down. It was a mistake for me not to properly vet each
   of them before uploading them and it does look pretty dubious."*

   **Implication:** verify provenance before treating any "famous deck" as
   exemplary. `midovislam/awesome-pitch-decks` and `rafaecheve/Awesome-Decks` are
   indexes of third-party material and carry the same risk.

**Reddit: not retrieved.** `agent-reach`'s Reddit backends (OpenCLI / rdt-cli)
require a login session and a writable config directory outside this session's
sandbox, so no Reddit thread was fetched directly. Rather than paraphrase
search-result snippets as if they were threads, **this skill records no Reddit
findings.** The community signal above is from Hacker News, which was retrievable
via a public API. Any Reddit-derived claim added later must be fetched and cited
directly.

---

## Statistics commonly mis-cited (do not repeat these)

This section exists because the most-quoted deck statistics in circulation are
wrong or misattributed.

1. **"VCs spend 3 min 44 s reviewing a deck."** True — but that is the **seed**
   figure. **Pre-seed is 4 min 10 s, i.e. *longer*.** Any claim that earlier-stage
   decks get *less* attention contradicts DocSend's own page [4][5].
2. **"The team slide gets the most attention at seed."** **Not a DocSend finding.**
   DocSend's seed section table puts team at **38 s**, behind product (59 s) and
   business model (64 s). The team-dominates claim comes from **Storydoc** (43% of
   reading time, a different platform measuring interactive decks) and from the
   **NBER survey** (stated criteria, not dwell time). Conflating the three is the
   single most common error in secondary deck content [5][11][14].
3. **"DocSend's 2024 per-slide table: Team 1m 2s, Financials 52s, Traction 49s…"**
   Circulates on SEO pages with **no citation or methodology** and **does not match**
   DocSend's published tables. **Unverified — do not use.**
4. **"The 3 most-read slides."** DocSend publishes per-section *times*, not a
   ranking. **Unverified.**
5. **"Keep it under 50 words per slide, no table of contents, tag each slide with
   its section label."** Appears only in an archival republication, not on current
   DocSend pages. **Secondary/dated.**
6. **"Sequoia's 10-slide deck includes a Product slide."** The 2015 version did;
   the current published order replaced Product with **Vision** [2].
7. **"a16z looks for 'the secret' in your deck."** **Not an a16z criterion.** No
   a16z page uses it. Do not attribute it [6][6b].
8. **"16:9 and a specific typeface are required."** **No primary source specifies
   either.** No fund position exists that this research could locate.
9. **"Send PDF, not DocSend / not PPTX."** **No fund states a file-format
   preference.** The PDF recommendation in this skill is craft advice (AP-39), not a
   fund requirement. a16z publishes on data rooms but takes no file-format position.
10. **"Pitch deck teardowns by First Round."** It is a **TechCrunch** franchise.

---

## What survives across sources (consensus)

Where sources from different tiers agree, the agreement is the strongest guidance
available. These ten points are corroborated across T1 fund guidance, T2 datasets,
and T3 research:

1. **One idea per slide.**
2. **The first three or four slides decide the read.**
3. **Lead with what you do, not why or how.**
4. **Market sizing must be bottom-up.**
5. **Never say "no competition."**
6. **"Why now" must be a falsifiable claim about what changed** — or be omitted
   honestly rather than faked.
7. **An appendix answers the predictable questions.**
8. **The ask is framed as milestones, not money.**
9. **Practice out loud until it is not a script.**
10. **The deck is not the company.** No deck audit can see the business.

---

## What this skill does NOT claim

1. **No success probability is ever produced.** This skill scores conformance to
   published standards. It does not predict whether a raise succeeds.
2. **No single "perfect deck" exists.** The sources disagree on slide order, length,
   screenshot use, and agenda slides
   ([`patterns-and-antipatterns.md`](patterns-and-antipatterns.md) Part 3). The
   disagreements are reproduced, not smoothed away.
3. **No fund's unstated preferences are claimed.** Where a fund has not published
   deck guidance, this skill says so and labels any emphasis set as inference.
4. **DocSend's numbers are attention data, not outcome data** (except the ordering
   finding, which is a reported correlation).
5. **a16z has no public canonical deck template**, and no "secret" criterion.
   Repeating the contrary is a fabrication.
6. **The anti-pattern catalog is synthesis, not any fund's list.** No fund publishes
   "42 anti-patterns". The catalog and its severity assignments are this skill's
   judgement over the cited sources.
7. **YC's own Series A benchmark pages are dead-linked.** YC's numeric ARR/growth
   thresholds are not stated here because they are not currently retrievable from
   the primary domain.
