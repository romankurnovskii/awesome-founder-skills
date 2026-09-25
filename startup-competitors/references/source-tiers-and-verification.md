# Source Tiers, Verification & Radical Honesty Protocol

This reference provides the rigorous standards for source hierarchy, multi-source triangulation, false corroboration detection, and anti-biasing guardrails.

---

## 1. The Radical Honesty & Anti-Cheerleading Protocol

This skill exists to help founders make sound strategic and resource allocation decisions—not to flatter them. An AI assistant that cheerleads every founder thesis actively harms the business by obscuring real market obstacles.

### Core Honesty Directives
1. **Never soften bad news**: If a market is dominated by an incumbent with high switching costs and entrenched distribution, state it directly. Do not reframe "brutal incumbent dominance" as "an exciting opportunity to be a nimble disrupter."
2. **The "When They Win Over You" Rule**: Every battlecard and competitor profile must detail where the competitor is genuinely superior and in which deals they win over the founder. A battlecard that lists only competitor flaws will get the sales team crushed in live calls.
3. **Challenge confirmation bias**: When research findings confirm what the founder already believes, deliberately hunt for disconfirming evidence.
4. **Treat inertia as the primary competitor**: In B2B and SaaS, the strongest competitor is almost always "doing nothing," manual spreadsheets, or organizational inertia. Always identify the exact trigger required to force a switch.

### Competitive Intelligence Anti-Patterns

| Anti-Pattern | Manifestation | Corrective Guardrail |
| :--- | :--- | :--- |
| **Cherry-picking flaws** | Focusing exclusively on competitor negative reviews while ignoring 4.8-star satisfaction. | Represent sentiment proportionally; cite both strengths and weaknesses with verbatim quotes. |
| **Dismissing incumbents** | "They're legacy and slow; no one likes them." | "Their customers continue paying millions annually. Why? What critical compliance or workflow job are they solving?" |
| **Vanity comparisons** | Comparing your envisioned flagship feature against their neglected legacy feature. | Compare core capabilities apples-to-apples against what buyers actually prioritize during procurement. |
| **Outdated intelligence** | Relying on 2-year-old pricing or employee counts in a fast-moving market. | Date every data point; flag any finding older than 12 months as potentially shifted. |
| **Duplicate false corroboration** | Treating 3 different tech blogs syndicating the same wire release as "3 independent sources." | Trace every citation back to original source documents (Form D, primary quote, or audited release). |
| **Single-point private metrics** | Writing "Competitor ARR is \$14.2M" as an indisputable fact. | Express private metrics as calibrated ranges (e.g., "\$12M–\$16M ARR") with proxy math explicitly shown. |

---

## 2. Standardized 4-Tier Claim Labeling

Every material claim, metric, and finding across all deliverables must be prefixed or annotated with one of four standardized labels:

- **`[Data]`**: Empirically sourced finding backed by a specific Tier 1 or Tier 2 citation (e.g., *"[Data] Series B closed on 2025-11-14 for \$24.0M led by Sequoia (SEC Form D)"*).
- **`[Estimate]`**: Calculated projection derived from verified proxies with stated assumptions (e.g., *"[Estimate] ARR is \$6M–\$9M based on 45 FTEs and \$150k ARR/FTE SaaS benchmark"*).
- **`[Assumption]`**: Unverified hypothesis or founder assertion requiring validation (e.g., *"[Assumption] Target enterprise buyers will replace bespoke spreadsheets with self-serve SaaS"*).
- **`[Opinion]`**: Analytical interpretation or strategic judgment rendered by the agent or founder (e.g., *"[Opinion] Competitor's lack of an API ecosystem leaves them vulnerable to vertical entrants"*).

---

## 3. Source Tier Hierarchy

Classify all evidence into the following four tiers:

```
┌────────────────────────────────────────────────────────┐
│ Tier 1 (T1): Statutory, Audited & Primary Records      │
├────────────────────────────────────────────────────────┤
│ Tier 2 (T2): Institutional Databases & Reputable Media │
├────────────────────────────────────────────────────────┤
│ Tier 3 (T3): Company Self-Reported Marketing & PR      │
├────────────────────────────────────────────────────────┤
│ Tier 4 (T4): Anonymous Forums, Speculative & Stale Data│
└────────────────────────────────────────────────────────┘
```

### Tier 1 (T1): Statutory, Audited & Primary Records
*Highest authority; legally binding or direct firsthand disclosure.*
- **Regulatory Registries**: SEC EDGAR filings (Form D for financings, 10-K, S-1), UK Companies House, EU commercial registries.
- **Intellectual Property Registries**: USPTO, EPO, Google Patents, WIPO registrations.
- **Audited Financial Statements**: Disclosed investor reports with auditor sign-off.
- **Direct Primary Interviews**: Verifiable customer win/loss interviews, ex-executive interviews, or customer contract excerpts (redacted).
- **Official Documentation**: Technical documentation, developer API specs, published changelogs with git timestamps.

### Tier 2 (T2): Institutional Databases & Reputable Media
*High credibility; independent editorial or vetted data aggregation.*
- **Intelligence Platforms**: PitchBook, CB Insights, Dealroom, Tracxn, Crunchbase Pro (curated data).
- **Vetted Software Review Platforms**: G2, Capterra, Gartner Peer Insights (where review count > 30 and verified reviewer identities).
- **Reputable Business Media**: Bloomberg, Financial Times, Wall Street Journal, Reuters, Forbes/TechCrunch (when independently reporting rather than syndicating PR).
- **Industry Analyst Reports**: Gartner Magic Quadrants, Forrester Waves, IDC MarketScapes.
- **Digital Footprint Aggregators**: SimilarWeb Pro, Semrush, Sensor Tower, LinkedIn Talent Insights.

### Tier 3 (T3): Company Self-Reported Marketing & PR
*Useful for positioning and features, but inherently biased.*
- **Company Website**: Homepage copy, feature comparison pages, case studies, landing pages.
- **Corporate Press Releases**: Wire releases (PR Newswire, BusinessWire) announcing funding, partnerships, or executive appointments.
- **Corporate Communications**: Official company blogs, podcasts featuring founders, YouTube product walkthroughs, social media announcements.
- **Founder Statements**: Podcasts, conference keynotes, AMAs, Twitter/X threads.

### Tier 4 (T4): Anonymous, Uncurated, or Stale Data
*Directional clues only; never used as standalone proof.*
- **Anonymous Forums**: Reddit discussions, Blind posts, Hacker News comments, Quora answers. (Valuable for customer voice and sentiment, but not for hard numbers).
- **Anonymous Employee Reviews**: Glassdoor, Indeed anonymous reviews (useful for culture/turnover sentiment, not financial facts).
- **Stale Disclosures**: Any directory listing, press article, or website snapshot that is older than 18 months without re-verification.
- **Unverified Third-Party Aggregators**: Low-quality SEO content farms, auto-generated competitor comparison sites.

---

## 4. Multi-Source Triangulation Protocols

### The 2-Source Corroboration Rule
Every material assertion labeled as **Fact** must be corroborated by **at least 2 independent sources**. If a fact cannot be confirmed by a second independent source, it must be downgraded to **`[Estimate]`** or **`[Assumption]`** with the single source explicitly cited.

### Duplicate-Source False Corroboration Check
A common trap is treating three media write-ups as three independent sources when all three merely rephrased the exact same BusinessWire press release.
- **Test**: Does Source B quote Source A, or do both cite the identical PR quote?
- **Rule**: If all articles trace back to a single company-issued announcement, they count as **one Tier 3 source**, not independent corroboration.

### Protocol: Private ARR & Financial Scale Triangulation
Triangulate private financial scale using the **Three-Angle Formula**:
1. **Angle 1 (Headcount Proxy)**:
   - Identify active engineering, sales, and total FTE headcount via LinkedIn.
   - Apply SaaS benchmark multipliers:
     - Seed / Series A: \$100k–\$150k ARR/employee.
     - Series B / Growth: \$140k–\$200k ARR/employee.
     - Mature / Scale: \$200k–\$280k+ ARR/employee.
2. **Angle 2 (Customer Count × Blended ACV)**:
   - Estimate customer accounts based on verified case studies, review counts, and customer segment focus.
   - Multiply by published starting or mid-tier pricing.
3. **Angle 3 (Capital Raised & Timing)**:
   - Analyze latest funding valuation and round size. If a company raised a \$20M Series A at an \$80M post-money valuation 18 months ago, ARR is likely in the \$3M–\$6M band.
- *Output*: Report ARR as a **bounded range** (e.g., *"[Estimate] \$4M–\$7M ARR"*) with all three triangulation angles documented.

---

## 5. Handling Data Gaps & Research Failures

When data cannot be found after thorough searching:
1. **Never fabricate or extrapolate without data**: An empty cell or honest declaration is infinitely more valuable than a fabricated number that misguides strategy.
2. **Explicitly declare the gap**: Write:
   > `DATA GAP: Could not find verified pricing for Competitor X. Published plans require 'Contact Sales'. Closest proxy: G2 user review from 2025-10 reports $18,000/year base for 25 seats [Estimate - Medium Confidence].`
3. **Suggest gap resolution actions**: Recommend specific follow-up actions (e.g., conducting customer win/loss interviews or mystery shopping).
