# Scoring Models & Metrics Rubrics

This reference documents the quantitative scoring formulas, confidence rubrics, research depth assessment, and threat classification models.

---

## 1. Research Depth Assessment Matrix

Before launching research, score three market complexity dimensions (1–3 scale):

| Dimension | 1 Point (Low) | 2 Points (Moderate) | 3 Points (High) |
| :--- | :--- | :--- | :--- |
| **Market Breadth** | Focused micro-niche / single vertical | Multi-vertical vertical SaaS | Broad horizontal platform |
| **Competitor Volume** | 2–4 obvious players | 5–10 fragmented players | Crowded market with 20+ tools |
| **Geographic Scope** | Single country / localized | Multi-regional (e.g. US + UK) | Global, multi-currency, multi-language |

### Tier Mapping

| Total Score | Depth Tier | Research Configuration | Expected Turnaround |
| :---: | :---: | :--- | :--- |
| **3 – 4** | **Light** | 3–5 core competitors; 2 pricing tiers; review platforms only. | Rapid (10–15 min) |
| **5 – 7** | **Standard** | 5–8 competitors; full 3-lens research (pricing, sentiment, GTM). | Thorough (20–30 min) |
| **8 – 9** | **Deep** | 8–10 competitors; deep forum mining, hiring signals, language maps. | Exhaustive (35–50 min) |

---

## 2. Competitor Relevance Scoring Model

To avoid arbitrary competitor lists, evaluate candidate entities using the **Competitor Relevance Metric**:

$$\text{Relevance Score} = 0.30 \cdot C + 0.25 \cdot P + 0.15 \cdot G + 0.15 \cdot M + 0.15 \cdot F$$

Where:
- $C$ = **Customer Overlap** (0–100): Alignment with target buyer persona, company scale, and vertical.
- $P$ = **Problem Overlap** (0–100): Alignment with primary job-to-be-done and acute pain point.
- $G$ = **Geography Overlap** (0–100): Operational regions, regulatory compliance, language support.
- $M$ = **Business Model Overlap** (0–100): Alignment in monetization structure (SaaS, usage-based, marketplace) and contract tier (SMB vs. Enterprise ACV).
- $F$ = **Product / Feature Overlap** (0–100): Overlap in functional capabilities, architecture, and workflow scope.

### Score Thresholds & Classifications

| Total Score | Classification | Strategic Action |
| :---: | :--- | :--- |
| **70 – 100** | **DIRECT Competitor** | Mandatory deep-dive in evidence log, feature matrix, and dedicated 1-page battlecard. |
| **40 – 69** | **INDIRECT / ADJACENT** | Evaluate 2–3 key representatives to assess expansion risk and shared budget competition. |
| **0 – 39** | **SUBSTITUTE / WATCHLIST** | Note as manual workaround, status quo inertia, or enterprise incumbent on watchlist. |

---

## 3. Claim Confidence Scoring Model

Every material claim in the competitive audit must have an attached **Confidence Score** (1.0 to 5.0 scale):

$$\text{Confidence} = 0.40 \cdot S + 0.30 \cdot K + 0.20 \cdot R + 0.10 \cdot Q$$

Where:
- $S$ = **Source Credibility** (1.0–5.0): Authority and objectivity of the publishing source (Tier 1 = 5.0, Tier 4 = 1.0).
- $K$ = **Corroboration** (1.0–5.0): Multi-source independent agreement (3+ sources = 5.0, uncorroborated single source = 1.0).
- $R$ = **Recency** (1.0–5.0): Timeliness of the underlying observation (<90 days = 5.0, >24 months = 1.0).
- $Q$ = **Completeness** (1.0–5.0): Depth of detail vs. vague headline assertion (Full terms = 5.0, partial = 3.0, vague = 1.0).

### Confidence Levels

| Confidence Score | Level | Meaning | Usage in Deliverables |
| :---: | :---: | :--- | :--- |
| **4.0 – 5.0** | **HIGH** | Traceable, corroborated by reputable sources, recent. | Stated as factual evidence (`[Data]`). |
| **2.5 – 3.9** | **MEDIUM** | Credible single source or minor data gaps. | Stated as probable estimate (`[Estimate]`). |
| **1.0 – 2.4** | **LOW** | Self-reported, stale, or unverified single point. | Flagged as unverified hypothesis (`[Assumption]`). |

---

## 4. Competitor Threat Level Rating Model

Evaluate each profiled competitor on their existential and commercial threat level:

### High Threat
- **Characteristics**: Fast-growing revenue or user base, well-funded (Tier 1 investors, >18 months runway), direct ICP overlap, strong product velocity, high customer satisfaction (>4.5 stars on G2 with >100 reviews).
- **Strategic Impact**: Direct head-to-head collision in sales calls; actively winning deals against the founder's target segment.

### Medium Threat
- **Characteristics**: Competitive on core features but notable gaps in UX, enterprise compliance, or integrations; slow release velocity; targeting adjacent customer segment but slowly moving into the space.
- **Strategic Impact**: Encroachment risk; occasionally seen in sales evaluations or competitive RFPs.

### Low Threat
- **Characteristics**: Stagnant product (no major changelog updates in >12 months); poor customer sentiment (frequent complaints regarding downtime or support); or pivoting upmarket to enterprise, abandoning SMBs.
- **Strategic Impact**: Minimal immediate sales pressure; potential customer churn source to actively target.

---

## 5. Financial Estimation Rules (Eliminating False Precision)

When analyzing privately held startups where audited financial statements are inaccessible:

1. **Mandatory Ranges**:
   - **Incorrect**: *"Competitor X ARR is \$14.2M."* (False precision).
   - **Correct**: *"[Estimate] Competitor X ARR is \$12M–\$16M based on 85 FTEs (\$140k–\$190k ARR/FTE SaaS benchmark) and ~450 customer logos at \$30k ACV."*
2. **Headcount Benchmark Multipliers**:
   - Seed / Pre-A: \$80k–\$120k ARR per employee.
   - Series A / B SaaS: \$120k–\$180k ARR per employee.
   - Efficient Growth / Late-Stage: \$180k–\$250k+ ARR per employee.
3. **Always Document Underlying Assumptions**:
   State the baseline headcount, estimated blended ACV, and source of employee counts (LinkedIn Insights vs. website team page).
