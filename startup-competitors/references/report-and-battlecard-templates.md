# Report & Battlecard Templates

This reference provides production-ready Markdown templates for every deliverable produced by this skill. Every deliverable enforces the standardized header, 4-tier claim labeling, and trailing Red/Yellow Flags.

---

## 1. One-Page Research Brief Template

```markdown
# Competitive Intelligence Research Brief: [Subject Name]
*Skill: startup-competitors | Date: [YYYY-MM-DD]*

- **Subject Type**: [Idea / Concept | Real Company | Hybrid]
- **Target Audience / ICP**: [Primary buyer persona, company size, vertical]
- **Decision Mandate**: [Why this report exists; e.g., Pre-Series A Fundraising, Pricing Pivot, Product Roadmap]
- **Recommended Depth Tier**: [Light (3-4) | Standard (5-7) | Deep (8-9)]

---

### 1. Scope & Boundaries
- **Geographic Scope**: [e.g., North America & Europe | Global]
- **Target Customer Segment**: [e.g., Mid-Market B2B SaaS (100–1,000 employees)]
- **Time Horizon**: [e.g., Immediate 12 months vs. 3-year strategic horizon]

### 2. Core Hypotheses to Test
1. **[Assumption] Hypothesis 1**: [e.g., Competitors are locked into high-touch enterprise sales, leaving self-serve underserved.]
2. **[Assumption] Hypothesis 2**: [e.g., No competitor offers automated multi-currency reconciliation without custom integrations.]
3. **[Assumption] Hypothesis 3**: [e.g., Incumbent pricing creates an exploitable wedge for usage-based competitors.]

### 3. Deliverables & Acceptance Criteria
- [ ] Preliminary Competitor Longlist (15–20 candidates)
- [ ] Priority Competitor Shortlist (5–10 scored via Competitor Relevance Metric)
- [ ] Evidence Log with 2+ independent sources for all material claims
- [ ] Comparative Feature & Pricing Matrix
- [ ] One-Page Battlecards for Top 3 Direct Competitors
- [ ] Executive Summary with clear strategic recommendations
```

---

## 2. Customer Language Map Template

```markdown
# Customer Language Map: [Category Name]
*Skill: startup-competitors | Generated: [YYYY-MM-DD]*

This document captures verbatim quotes mined from Reddit, G2, Capterra, and developer forums to drive landing page copy, pitch hooks, and objection counters.

### 1. How Customers Describe the Core Problem
- *"[Verbatim quote from customer]"* — [Source platform, Date]
- *"[Verbatim quote from customer]"* — [Source platform, Date]

### 2. Frustrations with Existing Competitors
- *"[Verbatim quote attacking competitor X]"* — [Source platform, Date]
- *"[Verbatim quote attacking competitor Y]"* — [Source platform, Date]

### 3. How Customers Describe the "Ideal Solution"
- *"[Verbatim quote describing dream feature or workflow]"* — [Source platform, Date]

### 4. Switching Triggers ("Why I Decided to Leave")
- *"[Verbatim quote describing the breaking point event]"* — [Source platform, Date]

---

### Red Flags
- [Severe structural market reality; e.g., buyers are locked into 3-year master service agreements]

### Yellow Flags
- [Emerging risk; e.g., buyers are increasingly sensitive to per-seat pricing inflation]
```

---

## 3. One-Page Competitor Battlecard Template

```markdown
# Competitor Battlecard: [Competitor Name]
*Skill: startup-competitors | Generated: [YYYY-MM-DD]*

| Metric | Details | Label |
| :--- | :--- | :---: |
| **Relevance Score** | [XX / 100] (`DIRECT` / `INDIRECT_ADJACENT`) | `[Data]` |
| **Threat Level** | `HIGH` / `MEDIUM` / `LOW` | `[Opinion]` |
| **Headquarters & Year** | [City, Country] | Founded [YYYY] | `[Data]` |
| **Estimated Scale** | [XX] FTEs | [$XM–$YM ARR est.] | [$ZM Funding] | `[Estimate]` |
| **Target Customer** | [Ideal buyer persona and company size] | `[Data]` |
| **Primary Pricing** | [e.g., $99/mo base + $15/seat or Contact Sales] | `[Data]` |
| **Overall Confidence** | [`HIGH` / `MEDIUM` / `LOW`] ([X.X] / 5.0) | `[Estimate]` |

---

### Core Value Proposition & Positioning
- **How they describe themselves**: *"[Quote their one-line pitch]"*
- **Real-world positioning**: [Objective description of where they sit in market]

### Key Strengths (Where They Genuinely Win)
- **Strength 1**: [e.g., Deep enterprise compliance (SOC2, HIPAA, ISO27001 ready)].
- **Strength 2**: [e.g., Extensive native integration marketplace (200+ connectors)].
- **Strength 3**: [e.g., Established brand trust with Fortune 500 procurement].

### When They Win Over You (Honest Assessment)
- **Scenario A**: When the prospect requires legacy on-premise deployments or custom SLAs.
- **Scenario B**: When procurement demands an established vendor with >$50M balance sheet.
- **Scenario C**: When the buyer is already standardized on their broader parent suite.

### Critical Vulnerabilities (Where They Lose)
- **Vulnerability 1**: [e.g., Rigid 6-week onboarding requiring professional services].
- **Vulnerability 2**: [e.g., Unpredictable usage overage spikes causing budget anxiety].
- **Vulnerability 3**: [e.g., Cluttered, legacy UI with frequent latency complaints].

### Switching Costs Breakdown
- **Technical**: [e.g., High — proprietary database schemas require manual export].
- **Contractual**: [e.g., Medium — annual contracts with auto-renewal clauses].
- **Emotional / Habitual**: [e.g., Low — end users actively dislike the software].

### How to Win Against Them (Sales Objection Handling)
1. **The Wedge**: [Specific differentiated capability or speed advantage to lead with].
2. **Objection Counter**:
   - *Prospect Objection*: *"Competitor X has been in the market for 10 years and has 500 integrations."*
   - *Factual Response*: *"They do, but 80% of those integrations rely on legacy batch syncing that lags by 24 hours. Our architecture syncs sub-second via webhooks without custom maintenance."*
3. **Disqualification Cue**: Disqualify early if the prospect insists on [specific legacy feature that would bloat the roadmap].

---

### Red Flags
- [e.g., Competitor holds exclusive OEM partnership with major market distributor.]

### Yellow Flags
- [e.g., Recent engineering hiring spree signals upcoming V2 release.]
```

---

## 4. Comprehensive Investment-Grade Report Template

```markdown
# Investment-Grade Competitive Intelligence Report: [Subject Name]
*Skill: startup-competitors | Generated: [YYYY-MM-DD]*

## 1. Executive Summary
- Synthesis of competitive landscape, primary threats, and market concentration (fragmented / consolidating / dominated).
- Top direct competitors and key strategic takeaways.

## 2. Research Methodology & Confidence Auditing
- Source tiers utilized (T1 Statutory, T2 Curated Intelligence, T3 Corporate Disclosures, T4 Community).
- Verification threshold applied (2+ independent sources for material facts).
- Data gaps and research blind spots explicitly documented.

## 3. Market Definition & Competitor Universe
- Taxonomy: Direct, Indirect, Adjacent, Incumbents, and Substitutes.
- Competitor Relevance Ranking Table (scored via Competitor Relevance Metric).

## 4. In-Depth Competitor Profiles
- Comprehensive teardown for each top-tier competitor (Product, GTM, Pricing, Capital, Traction).

## 5. Comparative Metrics Dashboard
- Structured comparison across 6 metric buckets: Market, Company, Product, GTM, Traction, and Moats.

## 6. Analytical Frameworks
- **Feature/Function Parity Matrix** (Strong / Adequate / Weak / Missing)
- **Pricing Whitespace & Switching Cost Curve**
- **2x2 Strategic Positioning Map**
- **Cross-Competitor Structural Pain Map**

## 7. Strategic Implications for [Subject Name]
- Defensible moats to build.
- Vulnerabilities in existing incumbents to exploit.
- GTM positioning recommendations.

## 8. Competitive Scenarios & Risk Watchlist
- **Base Case**: Expected competitive response over 12 months.
- **Bull Case**: Subject executes wedge successfully and captures market segment.
- **Bear Case**: Incumbent commoditizes the feature or competitor raises massive war chest.
- **Watchlist Triggers**: Specific events that trigger immediate reassessment.

## 9. Actionable Recommendations
- Prioritized tactical checklist (Product, Positioning, Sales Battlecards).

## 10. Appendix: Full Evidence Log & Source Citations
- Verifiable evidence table with claim labels (`[Data]`, `[Estimate]`, `[Assumption]`, `[Opinion]`), source tiers, and confidence scores.

---

### Red Flags
- [Critical threats that could invalidate the business model]

### Yellow Flags
- [Areas of ongoing monitoring or operational risk]
```

---

## 5. Verification Report Template (`verification-report.md`)

```markdown
# Verification Report: [Subject Name]
*Skill: startup-competitors | Generated: [YYYY-MM-DD]*

## Summary
- **Critical Issues**: [Count]
- **Warnings**: [Count]
- **Info Items**: [Count]

## Critical Issues (Decision-Blocking)
- **Issue 1**: [Description, affected files, suggested resolution]

## Warnings (Non-Blocking)
- **Warning 1**: [Description, affected files, suggested resolution]

## Verification Checklist
- [ ] All quantitative claims labeled (`[Data]`, `[Estimate]`, `[Assumption]`, `[Opinion]`)
- [ ] No internal contradictions between report, matrix, and battlecards
- [ ] Confidence ratings consistent with source tiers
- [ ] No duplicate-source false corroboration
- [ ] Stale data (>18 months) explicitly flagged
- [ ] Red Flags and Yellow Flags present in every deliverable
- [ ] Data gaps explicitly declared
```
