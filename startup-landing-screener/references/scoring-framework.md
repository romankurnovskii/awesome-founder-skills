# Launch Gate Scoring Framework & Readiness Thresholds

Defines the scoring mathematics, weighting hierarchy, and launch decision thresholds for evaluating landing pages across two essential tracks:
1. **Track 1: 30 Vibe-Coded Anti-Patterns (What to Avoid / Red Flags)**
2. **Track 2: 20 Web QA Acceptance Criteria (What to Verify & Have / Must-Haves)**

---

## 1. Severity Levels & Criterion Weighting

Every criterion in both Track 1 (Anti-Patterns) and Track 2 (Acceptance Criteria) is assigned a severity tier reflecting its negative impact on conversion, user trust, functionality, and founder credibility:

| Severity Level | Weight | Description | Failure Consequence |
| :--- | :---: | :--- | :--- |
| **Critical** | **3 pts** | Fatal credibility, functional, or conversion dealbreaker (e.g. no real demo, fake testimonials, horizontal scrolling, broken buttons, placeholder copy, no clear ICP). | Immediate public launch blocker; destroys first-visit conversion and brand trust. |
| **Major** | **2 pts** | High-friction defect or conversion killer (e.g. generic AI copy, no pricing clarity, broken footer links, missing meta descriptions/titles, mobile menu missing). | Degrades conversion rate by 40–70%; creates visitor skepticism or navigation failure. |
| **Minor** | **1 pt** | Aesthetic, brand, or layout polish item (e.g. 3 feature cards, outdated copyright year, missing favicon, unclickable logo/phone/email). | Weakens polish and domain authority; quick remediation. |

---

## 2. Criterion Status Definitions

For every criterion evaluated across both tracks, assign one of four statuses:

- **`PASS` (100% of points earned)**:
  - Clean compliance with visible evidence, functional verification, and authentic presentation.
- **`WARN` (50% of points earned)**:
  - Partial compliance, mild ambiguity, or minor trace of an anti-pattern present.
  - Generates an actionable suggestion before pushing.
- **`FAIL` (0% of points earned)**:
  - Clear presence of a red flag / anti-pattern, or failure to fulfill the required functional acceptance criterion.
  - Must include concrete remediation recommendations.
- **`N/A` (Excluded from calculation)**:
  - Criterion does not apply to this specific product type (e.g. API docs for a consumer mobile app). The maximum possible points are adjusted accordingly.

---

## 3. Mathematical Metrics & Dual-Track Scoring

### 1. Track 1: Vibe-Coded Index (0% – 100%)
Measures the density of AI-startup clichés and positioning anti-patterns (lower is better):

$$\text{Vibe-Coded Index} = \left( \frac{\sum (\text{Critical Fails} \times 3) + \sum (\text{Major Fails} \times 2) + \sum (\text{Minor Fails} \times 1) + 0.5 \times \text{Warns}}{\text{Total Max Penalty Points (Track 1)}} \right) \times 100$$

- **0% – 15% (Clean)**: Authentic, grounded, human, and professional.
- **16% – 35% (Mild Hype)**: Contains isolated template tropes; easily cleaned up.
- **36% – 60% (Vibe-Coded)**: Noticeable clone characteristics; reads like an LLM wrapper.
- **> 60% (Vibe-Coded Trap)**: Total aesthetic and copy clone; urgent rebuild required.

### 2. Track 2: Technical QA Acceptance Score (0% – 100%)
Measures positive adherence to functional, responsive, and pre-flight hygiene standards (higher is better):

$$\text{Technical QA Score} = \left( \frac{\sum \text{Points Earned (Track 2)}}{\sum \text{Max Applicable Points (Track 2)}} \right) \times 100$$

- **High (> 85%)**: Production-ready engineering; mobile-responsive, zero broken paths, solid metadata.
- **Moderate (65% – 84%)**: Usable but contains notable UX or navigation defects.
- **Low (< 65%)**: Broken links, viewport blowout, uncompressed assets, or broken buttons.

### 3. Composite Launch Readiness Score (0% – 100%)
Composite metric blending positioning integrity with functional execution:

$$\text{Launch Readiness Score} = 0.5 \times \left(100 - \text{Vibe-Coded Index}\right) + 0.5 \times \text{Technical QA Score}$$

- **High (> 85%)**: High conversion readiness, authentic positioning, defensible value, and solid engineering.
- **Moderate (65% – 84%)**: Promising foundation but requires targeted copy, proof, or technical fixes before launch.
- **Low (< 65%)**: Serious blockers present on either positioning or technical execution.

---

## 4. The Unified "Ready to Push" Launch Gates

Before a founder pushes their landing page to production, Hacker News, Product Hunt, or paid ads, evaluate against these strict gating rules:

```
┌──────────────────────────────────────────────────────────┐
│                   LAUNCH DECISION GATE                   │
└──────────────────────────────────────────────────────────┘
                             │
     ┌───────────────────────┴───────────────────────┐
     │ Any Critical Failures in Track 1 or Track 2?  │
     └───────────────────────┬───────────────────────┘
                            / \
                          YES  NO
                          /     \
                         ▼       ▼
             ┌───────────────┐  ┌──────────────────────────────────────────────┐
             │ BLOCKED (🔴)  │  │ Launch Readiness >= 85% & Tech QA >= 85%?    │
             └───────────────┘  └──────────────────────┬───────────────────────┘
                                                      / \
                                                    YES  NO
                                                    /     \
                                                   ▼       ▼
                                     ┌──────────────────┐  ┌───────────────────┐
                                     │ READY TO PUSH 🟢 │  │  NEEDS WORK 🟡    │
                                     └──────────────────┘  └───────────────────┘
```

### Gate 1: 🟢 READY TO PUSH (Full Launch Approval)
- **Conditions**:
  - Composite Launch Readiness Score $\ge 85\%$
  - Technical QA Acceptance Score $\ge 85\%$
  - Vibe-Coded Index $\le 20\%$
  - **Zero (0) Critical Fails** across both tracks
  - $\le 2$ Major Fails total
- **Verdict**: The site communicates authentic value, displays concrete product proof, targets a sharp ICP, avoids generic AI clichés, and is technically rock-solid on mobile and desktop. Safe to push to production and public distribution.

### Gate 2: 🟡 CONDITIONAL / NEEDS WORK (Pre-Push Remediation)
- **Conditions**:
  - Composite Launch Readiness Score between $65\%$ and $84\%$
  - $\le 1$ Critical Fail
  - $\le 5$ Major Fails total
  - Vibe-Coded Index between $21\%$ and $40\%$
- **Verdict**: Do NOT launch paid traffic or high-stakes announcements yet. Execute the prioritized remediation plan (top 3–5 suggestions) first to prevent conversion leakage and bounce rates.

### Gate 3: 🔴 BLOCKED (Do Not Push)
- **Conditions**:
  - Composite Launch Readiness Score $< 65\%$
  - **$\ge 2$ Critical Fails** on either track (e.g. horizontal scroll blowout, broken buttons, fake testimonials, no real demo)
  - Vibe-Coded Index $> 40\%$ OR Technical QA Score $< 65\%$
- **Verdict**: **DO NOT PUSH**. The landing page exhibits multiple systemic defects (positioning clichés, broken links, placeholder copy, or responsive failures). Launching in this state will damage founder reputation, waste paid ad spend, and ruin initial traction.
