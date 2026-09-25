# Workflow Stages: Investment-Grade Competitor Intelligence

This reference provides the exhaustive stage-by-stage procedure for conducting an investment-grade competitive intelligence and verification engagement.

---

## High-Level Sequence

```
Stage 0: Input Classification (Idea vs. Real Company vs. Hybrid)
   │
Stage 1: Mandate & Decision Context (1-Page Research Brief)
   │
Stage 1.5: Research Depth Assessment (Light / Standard / Deep)
   │
Stage 2: Subject Definition (Hypothesis Profile vs. Verified Profile)
   │
Stage 3: Target Audience / ICP & Problem Triad
   │
Stage 4: Competitor Universe Definition (Relevance Metric -> 5–10 Shortlist)
   │
Stage 5: Deep Research across 3 Sequential Lenses:
         - Lens 1: Profiles & Pricing Reverse-Engineering
         - Lens 2: Customer Sentiment & Language Mining
         - Lens 3: GTM & Strategic Growth Signals
   │
Checkpoint: Post-Research Alignment Check (1-Message Validation with User)
   │
Stage 6: Multi-Source Verification & Triangulation (2+ Independent Sources)
   │
Stage 7: Synthesis & Strategic Pattern-Matching (Connecting the 3 Lenses)
   │
Stage 7.5: Automated Verification Pass (V1 Cross-Deliverable Audit)
   │
Stage 8: Delivery, Battlecards & Continuous Monitoring
```

---

## Stage 0: Input Classification

Before performing any research, determine what type of subject was supplied:

### Case A: Idea / Concept Only
*Example: "An AI-powered automated inventory forecasting tool for boutique bakeries."*
- **Nature**: No legal entity, no live URL, no historical revenue or team footprint.
- **Objective**: Concept validation, problem/solution alternative mapping, hypothesis testing.
- **Workflow**:
  - Do NOT hallucinate a corporate profile.
  - Create a **Hypothesis Profile** with all assumptions explicitly tagged with `[Assumption]`.
  - Target audience is hypothesized, not validated.
  - Competitors are defined primarily as: manual workarounds, spreadsheets, generic tools, and adjacent platforms that could ship the feature.
  - Baseline confidence caps at **MEDIUM** until empirical customer interviews or market traction validate hypotheses.

### Case B: Real Company / Startup
*Example: "Verify competitors for MarketMan or Linear."*
- **Nature**: Operating entity with public web footprint, products, pricing, team, and customers.
- **Objective**: Verified intelligence, market positioning, moat evaluation, win/loss battlecards.
- **Workflow**:
  - Extract the operating profile from verified public records, pricing pages, and customer case studies.
  - Infer target audience and ICP from observed customer logos, case studies, pricing tiers, and reviews.
  - Base competitor definitions on actual market positioning.
  - Confidence can reach **HIGH** when supported by regulatory filings, audited disclosures, and multiple corroborating records.

### Case C: Hybrid (Company + New Bet / Pivot)
*Example: "HubSpot launching an autonomous AI agent builder for WhatsApp support."*
- **Nature**: Established parent company entering a new category or launching a distinct product line.
- **Workflow**:
  - Isolate the existing company profile from the new bet.
  - Evaluate competitors separately: core business competitors vs. new bet competitors.
  - Clarify whether the research mandate applies to the parent, the new bet, or the strategic synergy between both.

### Ambiguity Resolution
If the input cannot be classified with certainty, pause and ask the user:
1. Is this an early-stage idea/concept or an established operating company?
2. If an operating company: what is the official website URL or company name?
3. If an idea: what is the core job-to-be-done, target customer, geography, and expected business model?
4. What specific decision will this report inform?

---

## Stage 1: Mandate & Decision Context

Define the operational parameters of the engagement:
- **Decision Context**: Why does this report exist? (e.g., Investor memo, pre-seed pitch deck, pricing redesign, sales battlecard, M&A due diligence, product roadmap prioritization).
- **Scope Boundaries**:
  - Geography (e.g., North America, EU, DACH, Global).
  - Target Segment (e.g., Solo founders, SMB, Mid-Market, Enterprise).
  - Time Horizon (e.g., immediate 12 months vs. 3-year strategic horizon).
- **Confidence Threshold**: Distinguish between claims that require verified proof (e.g., revenue, regulatory compliance, legal patents) vs. acceptable directional estimates (e.g., ARR ranges, employee growth trends).

**Deliverable**: 1-page Research Brief stating the core hypotheses, decisions to be made, and acceptance criteria.

---

## Stage 1.5: Research Depth Assessment

Not all competitive research requires the same resource expenditure. Score three complexity factors (1–3 each):

1. **Market Breadth**: Highly focused niche (1) vs. Multi-vertical vertical SaaS (2) vs. Broad horizontal platform (3).
2. **Known Competitors**: Few obvious players (1) vs. Moderate fragmented space (2) vs. Crowded landscape with 20+ tools (3).
3. **Geographic Scope**: Single country/region (1) vs. Multi-regional (2) vs. Global multi-language (3).

| Total Score | Depth Tier | Configuration |
| :---: | :--- | :--- |
| **3 – 4** | **Light** | 3–5 core competitors profiled; 2 key pricing tears; review platforms only; fast turnaround. |
| **5 – 7** | **Standard** | 5–8 competitors profiled; full pricing breakdown; review + forum mining; GTM & hiring signals. |
| **8 – 9** | **Deep** | 8–10 competitors; deep secondary & primary triangulation; full language maps; channel opportunity maps; comprehensive battlecards. |

Present the recommended tier to the user and confirm before running deep research rounds.

---

## Stage 2: Subject Definition

Synthesize the core subject into a clean factual profile:
- **For an Idea**:
  - Problem statement & core value proposition.
  - Target buyer persona & hypothesized willingness-to-pay.
  - Hypothesized delivery mechanism (SaaS, marketplace, mobile app, API).
- **For a Real Company**:
  - Core products, pricing tiers, and stated packaging.
  - Headcount, headquarters, founding year, key leadership.
  - Known capital raised, key institutional investors, latest valuation.
  - Publicly visible customer proof points (logos, testimonials, App Store ratings).

---

## Stage 3: Target Audience / ICP & Problem

Competitors cannot be established in a vacuum. Define the exact customer problem triad:
1. **Ideal Customer Profile (ICP)**: Firmographics (employee count, revenue, vertical), tech stack prerequisites, buyer persona (e.g., Head of Ops vs. VP Eng).
2. **Core Job-to-be-Done**: What acute pain point triggers budget allocation?
3. **Budget Source & Status Quo**: From which existing budget line item does the spend originate? What is the current manual workaround or "do nothing" inertia?

---

## Stage 4: Competitor Universe Definition

Map the market into five distinct competitor quadrants:

1. **Direct Competitors**: Same core problem, same target customer, same product form factor.
2. **Indirect Competitors**: Different product or technology approach solving the same underlying problem for the same budget.
3. **Adjacent / Emerging Entrants**: Fast-moving startups or platform providers in neighboring categories expanding into this space.
4. **Incumbents**: Large enterprise platforms that possess distribution and could commoditize the capability as a feature.
5. **Substitutes & Status Quo**: Manual spreadsheets, internal scripts, outsourced agencies, or "doing nothing".

### Shortlisting Heuristic
Apply the quantitative **Competitor Relevance Metric** (see `scoring-and-rubrics.md`):
$$\text{Relevance} = 0.30 \times \text{Customer} + 0.25 \times \text{Problem} + 0.15 \times \text{Geography} + 0.15 \times \text{Model} + 0.15 \times \text{Product}$$
- **70–100**: Direct Competitor (mandatory deep-dive).
- **40–69**: Indirect / Adjacent (include key representatives).
- **0–39**: Substitute / Incumbent watchlist (monitor high-risk entities).

Select **5 to 10 priority competitors** for deep evaluation.

---

## Stage 5: Deep Research Across Three Lenses

Execute structured research across three sequential lenses to build a 360-degree intelligence picture:

### Lens 1: Competitor Profiles & Pricing Reverse-Engineering
- **Company Profile**: Founding date, headquarters, team size, funding trajectory, stage, core product offering.
- **Value Metric Analysis**: What do they charge for? (Per seat, per usage/compute, flat subscription, or hybrid). Does the metric align with delivered customer value?
- **Pricing Psychology & Packaging**:
  - Anchoring tiers, decoy pricing, charm pricing ($49 vs. $50).
  - Freemium strategy (what is free vs. what is gated behind enterprise paywalls).
  - Annual prepay discounts and refund lock-ins.
- **Three-Tier Switching Costs**:
  - *Technical*: Data portability, schema migration, API rewiring effort.
  - *Contractual*: Annual commitments, termination fees, seat minimums.
  - *Emotional / Workflow*: Team habituation, retraining burden, internal champion risk.

### Lens 2: Customer Sentiment & Language Mining
- **Review Mining (G2, Capterra, Trustpilot, App Stores)**:
  - What users genuinely praise (recurring themes with verbatim quotes).
  - What users hate (friction points, customer support drop-offs, pricing backlash).
  - Most requested missing features.
  - *Handling Scarce Reviews*: In emerging or niche B2B categories, note low review counts as a signal of early market stage or high switching friction; pivot to case studies, developer forums, and blog discussions.
- **Forum & Community Mining (Reddit, Indie Hackers, Hacker News, Discord)**:
  - **Language Map**: Extract exact verbatim phrases customers use to describe: (1) the core problem, (2) frustrations with existing tools, (3) their ideal solution, and (4) switching triggers.
  - **Migration Stories**: Analyze "switched from X to Y" threads: Why did they switch? What did they gain? What trade-offs did they make?
  - **Cross-Competitor Structural Pains**: Identify pain themes shared across 3+ competitors—these represent systemic market failures and prime wedge opportunities.

### Lens 3: Go-to-Market (GTM) & Strategic Growth Signals
- **Acquisition Channels & Sales Motion**:
  - Primary driver: Product-Led Growth (self-serve) vs. Inside Sales vs. Enterprise Field Sales.
  - Signup friction: Instant free trial vs. mandatory sales demo vs. gated contact form.
  - Paid advertising footprint (Google Ads Transparency, Meta Ad Library).
  - Content & SEO footprint (which category keywords they own vs. unclaimed content pillars).
- **Strategic Trajectory & Hiring Signals**:
  - *Engineering-heavy hiring*: Rebuilding infrastructure, building major new product lines, or entering AI.
  - *Sales/Marketing-heavy hiring*: Proven PMF, aggressively scaling distribution.
  - *Support/CS-heavy hiring*: High post-sale churn, onboarding complexity, or customer firefighting.
  - *Funding Velocity*: Time between capital raises; runway burn signals.
  - *Roadmap signals*: Recent changelogs, patent filings, and senior leadership hires.

---

## Post-Research Alignment Checkpoint

Before proceeding to synthesis, present a **1-message alignment checkpoint** to the user:
> *"Research pass complete across [X] competitors. Key findings: Top direct competitors are [A, B, C]; primary customer pain theme across all players is [Pain]; dominant pricing metric is [Metric]. Does this align with your market view? Are there any specific competitors you want added or removed before I synthesize the final deliverables?"*

This ensures the founder validates the competitive universe before extensive battlecard and report writing.

---

## Stage 6: Verification & Triangulation

Verification separates investment-grade research from internet gossip:

1. **The 2-Source Corroboration Rule**:
   Every material claim labeled as **Fact** must be verified by **at least 2 independent sources**.
2. **Duplicate-Source False Corroboration Check**:
   Confirm that two different articles are not merely syndicating the exact same press release or single wire statement. Multiple outlets repeating one company PR release count as **one source**, not two.
3. **No False Precision**:
   Never provide single-point estimates for private company financials (e.g., "ARR is \$14.2M"). Always express estimates as **calibrated ranges** (e.g., "Estimated ARR: \$12M–\$16M based on 85 FTEs and \$150k ARR/FTE benchmark").
4. **Contradiction Auditing**:
   If sources conflict (e.g., website claims "10,000 customers" while LinkedIn shows 4 sales reps and G2 has 12 reviews), highlight the discrepancy explicitly and downgrade the claim to an unverified estimate.

---

## Stage 7: Synthesis & Strategic Pattern-Matching

Synthesis turns raw observations into strategic advantages:
1. **Connect Findings Across Lenses**:
   A pricing gap becomes a definitive wedge only when tied to a customer complaint and a hiring gap (e.g., Competitor charges high minimum seats + users complain of rigidity + competitor is not hiring mid-market sales = clear wedge for self-serve pricing).
2. **The "When They Win Over You" Test**:
   Objectively document where competitors are superior. Honest battlecards acknowledge competitor strengths so founders can train sales teams on counter-positioning.
3. **Pricing Whitespace & Switching Barrier Map**:
   Identify unserved price tiers and document the specific switching friction founders must neutralize (e.g., building automated 1-click import tools).
4. **Threat Level Assessment**:
   Assign an evidence-backed threat rating per competitor:
   - **High Threat**: Well-funded, fast-growing, heavy customer overlap, strong product velocity.
   - **Medium Threat**: Competitive on some dimensions, clear product or distribution gaps on others.
   - **Low Threat**: Stagnant, weak product ratings, or moving upmarket away from this segment.

---

## Stage 7.5: Automated Verification Pass (V1 Protocol)

Before presenting the final deliverables, execute an internal cross-deliverable consistency audit:
- [ ] **Battlecard vs. Report Alignment**: Strengths, weaknesses, and threat levels in battlecards must match competitor profiles in the main report.
- [ ] **Feature Matrix vs. Sentiment Evidence**: Feature parity ratings (`Strong`, `Adequate`, `Weak`, `Missing`) must be supported by review quotes or documentation, not guesses.
- [ ] **Labeling Compliance**: Every quantitative claim and metric must be labeled with `[Data]`, `[Estimate]`, `[Assumption]`, or `[Opinion]`.
- [ ] **Mandatory Flags Present**: Every deliverable file must end with a **Red Flags** and **Yellow Flags** section.
- [ ] **Data Gaps Declared**: Every unknown or unverified metric must be openly declared in a dedicated Data Gaps section.

---

## Stage 8: Delivery, Battlecards & Continuous Monitoring

1. **Deliver the Complete Suite**:
   - Main Investment-Grade Competitor Report (`competitors-report.md`).
   - Feature Comparison Matrix (`competitive-matrix.md`).
   - Pricing & Switching Cost Landscape (`pricing-landscape.md`).
   - One-Page Battlecards for Top Direct Competitors (`battle-cards/{competitor}.md`).
2. **Review Flags with Founder**:
   Walk through the Red Flags (critical existential threats) and Yellow Flags (areas requiring founder investigation).
3. **Set Up Continuous Watchlist**:
   Define specific trigger events for re-evaluating the competitive landscape (e.g., Competitor Series B announcement, core executive departure, pricing page revamp).
