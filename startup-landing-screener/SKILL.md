---
name: startup-landing-screener
description: "Audit and screen a startup website or landing page against dual-track acceptance criteria before public launch. Evaluates both Track 1 (the '30 reasons your AI startup looks vibe-coded' anti-patterns across copywriting, visual design, product reality, social proof, commercial clarity, and differentiation) and Track 2 (the 20 technical & functional Web QA acceptance criteria across viewport responsiveness, mobile overflow, link integrity, SEO metadata, contact wiring, and content hygiene). Computes Composite Launch Readiness Score, Vibe-Coded Index, Technical QA Score, and strict Launch Gate Verdict (READY TO PUSH, NEEDS WORK, or BLOCKED). Produces two comprehensive comparison matrices and actionable before-and-after suggestions for every flagged item. Use when reviewing a landing page, auditing website copy, design, or technical QA, checking if a site is ready to push or launch, screening for vibe-coded clichés, or asking 'is my landing page ready to launch?' or 'review my startup website'."
metadata:
  version: 2.0.0
---

# Startup Landing Screener: Launch Gate & Acceptance Protocol

Perform an unsparing, high-rigor acceptance audit of a startup landing page or website to determine whether it is genuinely **Ready to Push** to production, Hacker News, Product Hunt, and paid acquisition.

This skill evaluates landing pages through a **Two-Track Audit Protocol**:
1. **Track 1: 30 Vibe-Coded Anti-Patterns (What to Avoid / Red Flags)**: Detects positioning tropes, LLM boilerplate copy, vaporware signals, purple template clones, and missing product proof.
2. **Track 2: 20 Web QA Acceptance Criteria (What to Verify & Have / Must-Haves)**: Enforces technical and functional hygiene—mobile responsiveness, zero horizontal scrolling, active buttons, unbroken links, valid metadata, and accessible contact methods.

Every audit produces dual line-by-line comparison matrices, an objective Launch Gate verdict, and concrete, founder-level remediation suggestions for every flagged criterion.

---

## The Launch Gate Philosophy

1. **Zero Flattery, Maximum Conversion Protection**: A premature public launch burns brand credibility, wastes irreplaceable first-visit attention, and squanders ad spend.
2. **Dual-Track Non-Negotiable Acceptance Tests**:
   - *Track 1*: 30 Anti-Patterns evaluated as `PASS` (clean), `WARN` (mild hype), or `FAIL` (anti-pattern present).
   - *Track 2*: 20 Acceptance Criteria evaluated as `PASS` (verified), `WARN` (partial), or `FAIL` (broken/missing).
3. **Every Flag Gets a Fix**: Do not just tell the founder their copy sounds like an LLM; write the replacement copy. Do not just complain about mobile overflow; specify the exact CSS fix or container constraint.
4. **Binary Launch Gate Authority**: The audit outputs one of three clear states:
   - 🟢 **READY TO PUSH**: Composite Score $\ge 85\%$, Tech QA $\ge 85\%$, Vibe Index $\le 20\%$, 0 Critical blockers, $\le 2$ Major flags.
   - 🟡 **NEEDS WORK**: Composite Score $65\%–84\%$, $\le 1$ Critical blocker. Pre-push fixes required.
   - 🔴 **BLOCKED**: Composite Score $< 65\%$, $> 1$ Critical blocker, Tech QA $< 65\%$, or Vibe Index $> 40\%$.

---

## The 50 Criteria Across 11 Dimensions

### Track 1: 30 Anti-Patterns (What to Avoid / Red Flags)

1. **Copywriting & Messaging**:
   - `#1` AI-generated landing page copy
   - `#2` Generic "revolutionize" messaging
   - `#6` "Built for the future"
   - `#11` "Powered by AI" as the headline
   - `#15` "10x your productivity"
   - `#21` "The future of X"
   - `#25` Buzzwords everywhere
2. **Visual Design & Layout**:
   - `#3` 3 feature cards in a row
   - `#7` Purple + black everything
   - `#8` Too many gradients
   - `#9` Bento grids everywhere
   - `#20` Generic AI-generated illustrations
   - `#24` Too many animations
3. **Product Reality & Technical Depth**:
   - `#5` No real product demo *(Critical)*
   - `#14` Chatbot as the entire product
   - `#16` No technical details
   - `#17` No API docs
   - `#19` No screenshots of the actual product *(Critical)*
   - `#29` No proof it actually works *(Critical)*
4. **Social Proof, Trust & Founder Voice**:
   - `#4` Fake testimonials *(Critical)*
   - `#13` No real customer stories
   - `#18` No visible users
   - `#23` No proof of ROI
   - `#26` No founder perspective
5. **ICP & Commercial Viability**:
   - `#10` No clear ICP *(Critical)*
   - `#12` No pricing clarity
   - `#27` No clear use case *(Critical)*
   - `#28` No reason to switch *(Critical)*
6. **Market Differentiation & Positioning**:
   - `#22` No differentiation *(Critical)*
   - `#30` It looks like every other AI startup

---

### Track 2: 20 Web QA Acceptance Criteria (What to Verify & Have / Must-Haves)

7. **Viewport & Mobile Responsiveness**:
   - `AC-01` Remove horizontal scrolling *(Critical)*
   - `AC-02` Fix mobile overflow *(Critical)*
   - `AC-03` Make every page mobile optimized *(Critical)*
   - `AC-04` Add a mobile menu *(Major)*
8. **Navigation & Link Integrity**:
   - `AC-05` Find broken links *(Critical)*
   - `AC-06` Fix footer links *(Major)*
   - `AC-07` Make the logo clickable *(Minor)*
   - `AC-08` Fix broken buttons *(Critical)*
   - `AC-09` Remove unused navigation *(Minor)*
9. **Metadata, SEO & Brand Basics**:
   - `AC-10` Fix page titles *(Major)*
   - `AC-11` Add meta descriptions *(Major)*
   - `AC-12` Add a favicon *(Minor)*
   - `AC-13` Add a custom 404 page *(Minor)*
   - `AC-14` Fix the copyright year *(Minor)*
10. **Contact & Lead Conversions**:
    - `AC-15` Make the phone number clickable *(Minor)*
    - `AC-16` Make the email clickable *(Minor)*
    - `AC-17` Add success messages *(Major)*
    - `AC-18` Add error messages *(Major)*
11. **Content Hygiene & Performance**:
    - `AC-19` Remove placeholder text *(Critical)*
    - `AC-20` Compress images *(Major)*

👉 **Detailed Criteria Rubric**: See [`references/criteria-rubric.md`](references/criteria-rubric.md) for full detection signals, fail/pass examples, and remediation rules.  
👉 **Scoring & Gating Math**: See [`references/scoring-framework.md`](references/scoring-framework.md).  
👉 **Report Template**: See [`references/report-template.md`](references/report-template.md).

---

## Operational Execution Sequence

```
Stage 0: Input Capture & Ingestion (URL, local file, or raw pitch copy)
   │
Stage 1: Automated Pre-Screen (Execute screen_landing.py CLI)
   │  ├── Track 1: Anti-Pattern heuristic scan (copy, colors, bento, buzzwords)
   │  └── Track 2: Technical QA DOM scan (meta tags, links, viewport, placeholders)
   │
Stage 2: Deep Semantic & Multimodal Audit (Agent review of positioning & mobile UX)
   │
Stage 3: Scoring & Launch Gate Verdict (Dual-track calculations & composite readiness)
   │
Stage 4: Detailed Remediation Authoring (Before vs After fixes for copy and code)
   │
Stage 5: Final Delivery (Markdown Audit Report following report-template.md)
```

---

### Stage 0: Input Capture & Ingestion

Identify the landing page input provided by the user:
- **Live URL**: e.g., `https://example.com`
- **Local File**: HTML, JSX/TSX, Astro, or Markdown landing page draft
- **Pasted Text**: Hero copy, feature list, pricing, and testimonial draft

---

### Stage 1: Automated Pre-Screening

Run the deterministic CLI screener located in `scripts/`:

```bash
# For a live URL:
python3 scripts/screen_landing.py --url "https://example.com" --name "ExampleApp"

# For a local file:
python3 scripts/screen_landing.py --file "path/to/page.html" --name "ExampleApp"

# Emit JSON for structured programmatic handling:
python3 scripts/screen_landing.py --url "https://example.com" --json

# Run doctor self-diagnostic
python3 scripts/screen_landing.py --doctor
```

The script parses DOM elements, metadata headers, link destinations, color hexes, and text heuristics to populate the baseline status for all 50 criteria across both tracks.

---

### Stage 2: Deep Semantic & Multimodal Audit

Supplement the automated pre-screen with direct analytical inspection:
1. **The Hero 5-Second Test**: Does the page explicitly state *who* uses this and *what acute pain* disappears?
2. **Product Tangibility**: Can a visitor see the real interface and actual workflow within 10 seconds? Or are there only abstract 3D shapes and fake mockups?
3. **Mobile & Viewport Reality**: Does the site render without horizontal panning on a 375px viewport? Does the mobile menu work?
4. **Interactive Reliability**: Do CTAs trigger active workflows or lead to dead `#` anchors? Are forms backed by clear success/error states?

---

### Stage 3: Scoring & Launch Gate Determination

Calculate metrics per [`references/scoring-framework.md`](references/scoring-framework.md):
- **Track 1 Vibe-Coded Index**: Penalty density of detected anti-patterns ($\le 20\%$ target).
- **Track 2 Technical QA Score**: Positive fulfillment of engineering standards ($\ge 85\%$ target).
- **Composite Launch Readiness Score**: $0.5 \times (100 - \text{Vibe Index}) + 0.5 \times \text{Tech QA Score}$.
- **Verdict Gate**:
  - `READY TO PUSH`: Composite $\ge 85\%$, Tech QA $\ge 85\%$, Vibe Index $\le 20\%$, 0 Critical fails, $\le 2$ Major fails.
  - `NEEDS WORK`: Composite $65\%–84\%$, $\le 1$ Critical fail.
  - `BLOCKED`: Composite $< 65\%$, $\ge 2$ Critical fails, Tech QA $< 65\%$, or Vibe Index $> 40\%$.

---

### Stage 4: Authoring Detailed Comparisons & Suggestions

For every criterion marked `FAIL` or `WARN` across both tracks:
1. **Document Current State**: Quote the exact copy or cite the observed DOM/layout defect.
2. **Compare to Launch-Ready Standard**: Explain why the current approach triggers skepticism or UX drop-off.
3. **Provide Concrete Fix**: Deliver the exact replacement copy or specific HTML/CSS patch.
   ```text
   BEFORE: "Revolutionizing modern workflows with next-gen AI cognitive fabric."
   AFTER:  "Reconciles 500 bank transactions against Xero invoices in 3 minutes."
   ```
   ```html
   <!-- Before: <a href="#">Privacy Policy</a> -->
   <!-- After: -->
   <a href="/privacy" class="hover:underline">Privacy Policy</a>
   ```

---

### Stage 5: Final Delivery

Format the deliverable strictly using [`references/report-template.md`](references/report-template.md):
- Executive Launch Verdict badge & dual-track summary table.
- Complete 30-criteria Track 1 comparison matrix (no missing rows).
- Complete 20-criteria Track 2 acceptance checklist matrix (no missing rows).
- Dimension-grouped deep dives with actionable before/after suggestions.
- Top 5 prioritized fixes before pushing to production.
- Final launch push checklist.
