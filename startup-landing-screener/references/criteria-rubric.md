# Startup Landing Screener: Comprehensive Criteria Rubric

Comprehensive reference for auditing startup websites and landing pages across two essential tracks:
1. **Track 1: 30 Vibe-Coded Anti-Patterns (What to Avoid / Red Flags)** — Narrative, visual, trust, and positioning signals that reveal generic wrappers or vaporware.
2. **Track 2: 20 Web QA Acceptance Criteria (What to Verify & Have / Must-Haves)** — Functional, technical, responsive, and pre-flight hygiene criteria that ensure production readiness.

---

# Track 1: 30 Vibe-Coded Anti-Patterns (What to Avoid / Red Flags)

## Dimension 1: Copywriting & Value Proposition

### 1. AI-Generated Landing Page Copy
- **Category**: Copywriting & Value Proposition
- **Severity**: Major
- **Acceptance Rule**: The copy must sound like a domain-expert human founder communicating directly with a practitioner, not standard LLM boilerplate.
- **Detection Signals**:
  - Predictable LLM transition words: *"In today's fast-paced world"*, *"Delve into"*, *"Harness the power of"*, *"Elevate your workflow"*, *"Unleash the potential"*, *"Seamlessly integrate"*.
  - Symmetrical sentence structures with high adjective-to-noun ratios.
  - Vague generalizations that could apply to any software tool.
- **Fail Example**: *"In today's rapidly evolving digital landscape, our next-generation AI platform empowers modern teams to effortlessly elevate their workflow efficiency."*
- **Pass Example**: *"Reconciles Stripe payouts against bank deposits every midnight so your accounting team stops doing manual CSV lookups."*
- **Suggestion**:
  - Delete introductory throat-clearing (*"In today's..."*).
  - Replace every abstract verb (*elevate, unleash, empower*) with the actual operational action (*reconciles, imports, blocks, alerts*).
  - Read copy aloud; if no human would say it in a live conversation with a customer, rewrite it.

---

### 2. Generic "Revolutionize" Messaging
- **Category**: Copywriting & Value Proposition
- **Severity**: Major
- **Acceptance Rule**: State the specific problem solved and the concrete mechanical difference, never generic paradigm-shifting claims.
- **Detection Signals**: Words like *"revolutionize"*, *"transform"*, *"reimagine"*, *"paradigm shift"*, *"the new era of"*.
- **Fail Example**: *"Revolutionizing the way enterprises interact with contract data."*
- **Pass Example**: *"Redlines commercial leases for non-standard indemnity clauses in under 90 seconds."*
- **Suggestion**:
  - Ban the verb "revolutionize".
  - Complete this sentence: *"Our product saves [Job Title] [X hours / $Y] by automatically [Specific Boring Task]."*

---

### 6. "Built for the Future"
- **Category**: Copywriting & Value Proposition
- **Severity**: Minor
- **Acceptance Rule**: Focus on solving an acute, urgent problem happening *today* with today's software stack.
- **Detection Signals**: Phrases like *"built for tomorrow"*, *"future-proof your business"*, *"the next frontier"*, *"ready for Web4"*.
- **Fail Example**: *"A dynamic infrastructure engineered for the future of work."*
- **Pass Example**: *"Works with your current PostgreSQL 15+ database and Kubernetes 1.28 cluster. Installs via Helm in 5 minutes."*
- **Suggestion**:
  - Replace speculative future-proofing claims with day-1 compatibility and deployment specs.

---

### 11. "Powered by AI" as the Headline
- **Category**: Copywriting & Value Proposition
- **Severity**: Major
- **Acceptance Rule**: AI is an implementation detail / engine, never the customer-facing value proposition. The headline must highlight the outcome.
- **Detection Signals**: Headlines starting or ending with *"Powered by AI"*, *"AI-First"*, *"AI-Powered"*, *"Supercharged by GenAI"*.
- **Fail Example**: *"AI-Powered Email Management for Fast Teams."*
- **Pass Example**: *"Clear your support backlog before 9 AM. Auto-drafts refunds, shipping updates, and bug reports with your team's tone."*
- **Suggestion**:
  - Demote "AI" to a supporting badge or subtitle (e.g., *"Uses fine-tuned Claude 3.5 models"*).
  - Make the H1 answer: *"What problem vanishes from my life if I click 'Sign Up'?"*

---

### 15. "10x Your Productivity"
- **Category**: Copywriting & Value Proposition
- **Severity**: Major
- **Acceptance Rule**: Replace arbitrary "10x / 100x" multiplier claims with measured, credible time/cost metrics.
- **Detection Signals**: *"10x faster"*, *"10x productivity"*, *"100x your output"*, *"Supercharge your team 10x"*.
- **Fail Example**: *"Get 10x more productive in your developer workflow."*
- **Pass Example**: *"Cuts PR review turnaround from 14 hours to 45 minutes by auto-checking linting, migration safety, and test coverage."*
- **Suggestion**:
  - Swap the multiplier for baseline vs. post-product delta measured in minutes, hours, or dollars.
  - If you lack cohort data, state the exact manual step removed rather than inventing a multiplier.

---

### 21. "The Future of X"
- **Category**: Copywriting & Value Proposition
- **Severity**: Minor
- **Acceptance Rule**: Frame the tool as a superior utility for current work, not a philosophical thesis on the future.
- **Detection Signals**: *"The future of accounting"*, *"The future of recruiting"*, *"Welcome to the future of sales"*.
- **Fail Example**: *"The future of customer relationship management."*
- **Pass Example**: *"Syncs LinkedIn DMs and WhatsApp messages straight into HubSpot deals without a Chrome extension crash."*
- **Suggestion**:
  - Replace "The future of [Industry]" with "[Specific Tool Category] that actually [Specific Solved Frustration]".

---

### 25. Buzzwords Everywhere
- **Category**: Copywriting & Value Proposition
- **Severity**: Major
- **Acceptance Rule**: Technical and business terms must be domain-accurate and sparse; eliminate fluff adjectives.
- **Detection Signals**: Dense clusters of: *"synergy"*, *"hyper-scalable"*, *"agentic orchestration"*, *"autonomous workflows"*, *"next-gen"*, *"state-of-the-art"*, *"holistic"*, *"frictionless"*.
- **Fail Example**: *"Hyper-scalable agentic cognitive orchestration fabric delivering seamless, frictionless enterprise synergy."*
- **Pass Example**: *"Runs scheduled Python scrapers across 50 e-commerce sites, extracts clean JSON prices, and pushes updates to BigQuery."*
- **Suggestion**:
  - Run the "Explain to a 10-Year-Old Engineer" test. If a junior developer cannot draw the system based on your description, strip the buzzwords.

---

## Dimension 2: Visual Design & Layout

### 3. 3 Feature Cards in a Row
- **Category**: Visual Design & Layout
- **Severity**: Minor
- **Acceptance Rule**: Features should be presented with rich contextual detail, workflow progression, or tabbed deep-dives—not identical generic icon boxes.
- **Detection Signals**: A 3-column layout containing [Lucide Icon] + [3-word Title] + [1 generic sentence] (e.g., "Fast", "Secure", "Smart").
- **Fail Example**: Three boxes: ⚡ *Lightning Fast* / 🔒 *Enterprise Security* / 🧠 *Smart AI*.
- **Pass Example**: Interactive split-screen layout showing: Step 1 (Trigger input) -> Step 2 (Product logic & real preview) -> Step 3 (Output destination with webhook ping).
- **Suggestion**:
  - Replace 3 generic cards with an interactive product walkthrough, a comparative timeline, or asymmetric cards with actual UI widgets embedded.

---

### 7. Purple + Black Everything
- **Category**: Visual Design & Layout
- **Severity**: Major
- **Acceptance Rule**: Establish a distinctive brand identity; avoid the generic "AI dark mode with neon purple/violet neon glows".
- **Detection Signals**: Background `#000000` or `#09090b` with primary accent `#8b5cf6` / `#a855f7` / `#7c3aed` and purple radial gradient blurs.
- **Fail Example**: Pitch black background with `#a855f7` glowing border buttons and purple hero text gradient.
- **Pass Example**: Brand-informed palette (e.g., crisp warm neutrals, slate blue, forest dark, or clean high-contrast light mode with deliberate editorial typography).
- **Suggestion**:
  - Audit CSS for `#8b5cf6` and `rgb(139, 92, 246)`. Shift to an authentic color palette matching the target industry (e.g., fintech prefers slate/navy/emerald; devtools prefers terminal greens/grays/monochrome).

---

### 8. Too Many Gradients
- **Category**: Visual Design & Layout
- **Severity**: Minor
- **Acceptance Rule**: Use gradients sparingly for depth or subtle lighting, not on every headline, card border, button, and background blur.
- **Detection Signals**: Multiple `linear-gradient` declarations applied to text (`background-clip: text`), glowing borders, and background meshes simultaneously.
- **Fail Example**: Gradient H1, gradient H2, gradient pill badge, gradient card borders, and gradient floating background spheres.
- **Pass Example**: Solid typography with crisp contrast; maximum 1 subtle atmospheric gradient or flat editorial styling.
- **Suggestion**:
  - Make headlines solid white or black. Remove gradient text fills. Reserve color accents exclusively for interactive CTAs.

---

### 9. Bento Grids Everywhere
- **Category**: Visual Design & Layout
- **Severity**: Minor
- **Acceptance Rule**: Use bento grids only when displaying diverse, disparate data cards—not as a substitute for explaining how the product works.
- **Detection Signals**: Heavy reliance on CSS grid with asymmetric spans (col-span-2, row-span-2) containing animated counters, random toggle switches, and miniature dummy charts.
- **Fail Example**: 6 mismatched rounded boxes with fake toggle buttons, a spinning 3D cube, and a fake CPU usage graph.
- **Pass Example**: A clear chronological story showing the user journey from problem state to resolved state, supported by full-width product UI views.
- **Suggestion**:
  - Ask: *"Does this box show something the user will actually see or configure in the product?"* If it's a dummy widget, replace it with real screenshots or workflows.

---

### 20. Generic AI-Generated Illustrations
- **Category**: Visual Design & Layout
- **Severity**: Major
- **Acceptance Rule**: Replace Midjourney/DALL-E surreal illustrations (floating glowing brains, neon cyborg hands, glossy 3D spheres) with actual software visuals.
- **Detection Signals**: Stock AI imagery depicting floating geometric shapes, glowing synaptic networks, or synthetic humanoid avatars.
- **Fail Example**: A glowing blue brain floating above a robotic hand with floating particle lights.
- **Pass Example**: High-resolution screenshot of the actual product dashboard, terminal CLI session, or workflow diagram.
- **Suggestion**:
  - Remove all AI-generated conceptual art. Replace with clean SVG architecture diagrams, real UI crops, or screen captures.

---

### 24. Too Many Animations
- **Category**: Visual Design & Layout
- **Severity**: Minor
- **Acceptance Rule**: Animations must serve a functional purpose (guiding focus, revealing progressive disclosure); avoid scroll-jacking and dizzying loops.
- **Detection Signals**: Infinite rotating borders, bouncy scroll-reveals on every paragraph, particles canvas in hero, marquee tickers of fake badges.
- **Fail Example**: Elements fade in from 4 different directions, buttons pulse continuously, background canvas runs WebGL particles at 60fps draining CPU.
- **Pass Example**: Fast, subtle micro-interactions (e.g. 150ms hover state transitions, smooth tab switches) with zero scroll delays.
- **Suggestion**:
  - Disable scroll-jacking. Enforce `prefers-reduced-motion`. Let content load instantly without waiting for staggered fade-in triggers.

---

## Dimension 3: Product Authenticity & Technical Depth

### 5. No Real Product Demo
- **Category**: Product Authenticity & Technical Depth
- **Severity**: Critical
- **Acceptance Rule**: Visitors must be able to see the product working within 10 seconds of landing on the page—via an embedded video, interactive sandbox, or animated GIF/WebM.
- **Detection Signals**: Absence of `<video>`, Loom embed, interactive demo iframe, or step-by-step UI capture above the fold.
- **Fail Example**: Landing page has only text, a static stock graphic, and a "Request Access" button with no preview of the app.
- **Pass Example**: 45-second high-density video demo showing real inputs, live processing, and actual output, playable with one click.
- **Suggestion**:
  - Record a 30–60 second screen recording of the actual software solving a real task. Embed it in the hero or directly beneath it.

---

### 14. Chatbot as the Entire Product
- **Category**: Product Authenticity & Technical Depth
- **Severity**: Major
- **Acceptance Rule**: If the product uses conversational AI, demonstrate that it is a specialized workflow, system of record, or domain tool—not just an OpenAI API wrapper with a prompt.
- **Detection Signals**: Hero visual is a standard message bubble interface (User: "Help me do X" / Bot: "Here is your response...").
- **Fail Example**: Screenshot of a chat box asking *"Ask me anything about your business"* with standard prompt suggestions.
- **Pass Example**: Specialized workflow interface showing structured inputs, canvas views, diff inspectors, tables, or export pipelines alongside the assistant.
- **Suggestion**:
  - Highlight the non-chat features: integrations, data synchronization, audit trails, permission controls, and structured outputs.

---

### 16. No Technical Details
- **Category**: Product Authenticity & Technical Depth
- **Severity**: Major
- **Acceptance Rule**: Provide concrete technical parameters (architecture, latency, models, compliance, hosting options) so technical buyers can evaluate feasibility.
- **Detection Signals**: Zero mention of infrastructure, security (SOC2, HIPAA, encryption), latency specs, deployment models (SaaS, VPC, on-prem), or data handling.
- **Fail Example**: *"Our proprietary intelligence engine handles everything behind the scenes with enterprise grade robustness."*
- **Pass Example**: *"Deploys in your AWS VPC or GCP project. Zero customer data retention policy on model inference. P95 latency < 120ms via edge caching."*
- **Suggestion**:
  - Add an "Architecture & Security" section specifying hosting requirements, data isolation, encryption standards, and supported protocols.

---

### 17. No API Docs
- **Category**: Product Authenticity & Technical Depth
- **Severity**: Major (Critical for devtools/B2B infrastructure)
- **Acceptance Rule**: For any developer, API, or B2B infrastructure startup, an accessible link to interactive API docs or sample code snippets is mandatory.
- **Detection Signals**: No "Docs" link in navigation, no code snippets in hero or feature sections, no curl/SDK examples.
- **Fail Example**: Claims to be a developer platform but has no documentation link or code snippet anywhere on the page.
- **Pass Example**: Visible navigation link to docs, plus a real-world code snippet (Python/TypeScript/cURL) directly on the landing page showing request/response payloads.
- **Suggestion**:
  - Embed an interactive code snippet tab (TypeScript / Python / cURL) showing the exact 3 lines of code needed to integrate. Add a prominent "Documentation" link in header and footer.

---

### 19. No Screenshots of the Actual Product
- **Category**: Product Authenticity & Technical Depth
- **Severity**: Critical
- **Acceptance Rule**: Show genuine, un-stylized screenshots or screen-recordings of the application UI with real data.
- **Detection Signals**: Only 3D mockups, isometric abstract shapes, or heavily blurred/cropped mockups that conceal what the product actually looks like.
- **Fail Example**: An angled isometric laptop render tilted at 45 degrees with fake placeholder text blurred out.
- **Pass Example**: Crisp, full-width, 2x retina screenshots of the application dashboard displaying realistic domain data.
- **Suggestion**:
  - Take high-resolution screenshots of the 3 most important screens. Embed them with zoom capability and descriptive captions explaining the user action.

---

### 29. No Proof It Actually Works
- **Category**: Product Authenticity & Technical Depth
- **Severity**: Critical
- **Acceptance Rule**: Provide empirical proof of accuracy, benchmark results, latency measurements, or auditable outcomes.
- **Detection Signals**: High-stakes claims (e.g. "99.9% accuracy", "halves customer churn") with zero supporting citations, test logs, or methodology notes.
- **Fail Example**: *"Delivers 99.9% flawless automated legal analysis without human errors."*
- **Pass Example**: *"Benchmarked across 1,200 SEC 10-K filings: 94.2% precision on debt covenant extraction vs. 71.8% for GPT-4 baseline. View our evaluation dataset on GitHub."*
- **Suggestion**:
  - Link to a public benchmark, technical whitepaper, evaluation methodology, or GitHub repo validating your claims.

---

## Dimension 4: Social Proof, Trust & Founder Voice

### 4. Fake Testimonials
- **Category**: Social Proof & Trust
- **Severity**: Critical
- **Acceptance Rule**: Testimonials must have full verifiable attribution (real person, real photo, job title, company name, linked LinkedIn/Twitter/website). If pre-launch, do not use fake testimonials.
- **Detection Signals**:
  - AI-generated avatar photos (e.g., ThisPersonDoesNotExist artifacts).
  - Vague names: *"John D., Tech Enthusiast"*, *"Sarah M., Marketing Director"*.
  - Generic praise with no specific product feature or metric: *"This app changed my life! Amazing tool!"*
- **Fail Example**: Headshot of an AI-generated person labeled *"Alex T., Startup Founder - 'Incredible experience, literally 10x our growth!' "*
- **Pass Example**: Headshot, full name, verified LinkedIn link: *"David Chen, Head of Data Engineering at Acme Logistics - 'Migrated 40 Redshift pipelines to Snowflake in 3 days using their auto-transpiler.' "*
- **Suggestion**:
  - If you don't have real customers yet, **remove the testimonial section entirely**. Replace it with founder credentials, early beta test logs, or open-source stars.

---

### 13. No Real Customer Stories
- **Category**: Social Proof & Trust
- **Severity**: Major
- **Acceptance Rule**: Showcase in-depth case studies or specific problem-solution-result stories, not just isolated quote snippets.
- **Detection Signals**: Customer logos or quotes present without any narrative describing their baseline, how they deployed, or the measured outcome.
- **Fail Example**: A carousel of 5 company logos with zero context on what those companies do with your software.
- **Pass Example**: Mini case study card: *"How FinTechCorp cut compliance audit prep from 3 weeks to 4 hours (includes before/after workflow diagram and quote from VP of Compliance)."*
- **Suggestion**:
  - Build at least one "Customer Spotlight" or "Beta Tester Journey" card showing: Problem -> Implementation -> Quantified Result.

---

### 18. No Visible Users
- **Category**: Social Proof & Trust
- **Severity**: Major
- **Acceptance Rule**: Demonstrate that real humans actively use the product (live activity metrics, community links, public reviews, or verified user counters).
- **Detection Signals**: Zero public presence: no link to Discord/Slack community, no GitHub star counter, no Product Hunt badge, no reviews on G2/Capterra.
- **Fail Example**: Claims to be *"Loved by 10,000+ teams"* but has zero links to external reviews, public community, or named customer accounts.
- **Pass Example**: *"Join 1,420 engineers in our Discord"*, live GitHub badge with 2.8k stars, or direct links to G2 reviews.
- **Suggestion**:
  - Link directly to your public community (Discord, Slack, GitHub Discussions) or display verified third-party review widgets.

---

### 23. No Proof of ROI
- **Category**: Social Proof & Trust
- **Severity**: Major
- **Acceptance Rule**: Justify why paying for the software generates more value than it costs. Provide clear unit economics or payback math.
- **Detection Signals**: Expensive pricing tiers without any explanation of hours saved, revenue recovered, or headcount cost avoided.
- **Fail Example**: Pricing card says "$499/mo" with a bullet list of features, but no context on what buying it displaces.
- **Pass Example**: *"At $199/month, preventing just one incorrect international wire transfer ($45 fee + 3 hours of support time) pays for the tool twice over."*
- **Suggestion**:
  - Add an ROI breakdown or simple interactive calculator (e.g., *"Number of engineers x Hours spent on manual QA = Money saved per month"*).

---

### 26. No Founder Perspective
- **Category**: Social Proof & Trust
- **Severity**: Major
- **Acceptance Rule**: Landing page must convey a clear point of view from the creators: who built this, why it was built, and what unfair insight inspired it.
- **Detection Signals**: Faceless corporate entity with no "About" note, no founder letter, no creator signatures, no link to founders' personal profiles.
- **Fail Example**: Entire site reads like an anonymous venture-backed enterprise conglomerate with zero human voice.
- **Pass Example**: *"We spent 6 years managing AWS cloud bills at ScaleCo. We built CloudCut because existing tools only alerted you after the bill skyrocketed. Here's how we fix it before billing hits." — Roman & Team.*
- **Suggestion**:
  - Add a short "Why We Built This" note from the founders with authentic headshots and links to personal profiles (X/Twitter, LinkedIn, GitHub).

---

## Dimension 5: ICP & Commercial Viability

### 10. No Clear ICP (Ideal Customer Profile)
- **Category**: ICP & Commercial Viability
- **Severity**: Critical
- **Acceptance Rule**: Within 5 seconds, a visitor must know whether this product is made specifically for them or someone else.
- **Detection Signals**: Copy addresses *"everyone"*, *"businesses"*, *"creators and enterprises alike"*, *"teams of all sizes"*.
- **Fail Example**: *"The all-in-one AI platform for individuals, creators, small teams, and Fortune 500 enterprises."*
- **Pass Example**: *"Built specifically for Series A B2B SaaS heads of sales running outbound on Apollo and HubSpot."*
- **Suggestion**:
  - Explicitly name the role and company stage in the hero or subheadline (e.g., *"For DevOps teams managing 50+ microservices on EKS"*).

---

### 12. No Pricing Clarity
- **Category**: ICP & Commercial Viability
- **Severity**: Major
- **Acceptance Rule**: Pricing must be transparent, predictable, and explain what happens when usage limits are reached. If enterprise-only, give a starting tier.
- **Detection Signals**: Only a "Contact Sales" button with zero indication of price range, or confusing "credits" without dollar conversions.
- **Fail Example**: Single button: *"Contact Sales for Custom Enterprise Pricing"* on a simple B2B SaaS tool.
- **Pass Example**: Clear 3-tier matrix: Starter ($29/mo), Pro ($79/mo), Enterprise (Starts at $499/mo with dedicated VPC). Clear credit explanation: *"1 credit = 1 scanned document"*.
- **Suggestion**:
  - Publish transparent pricing or a self-serve tier. If enterprise-only, state *"Plans start at $X,000/year"*. Explain overage costs clearly.

---

### 27. No Clear Use Case
- **Category**: ICP & Commercial Viability
- **Severity**: Critical
- **Acceptance Rule**: Illustrate the exact operational trigger, input, process, and output of the product.
- **Detection Signals**: High-level abstract benefit statements with zero concrete operational use cases.
- **Fail Example**: *"Unleash intelligent document comprehension for seamless business agility."*
- **Pass Example**: *"Upload a 50-page commercial lease PDF -> Extract rent escalation schedules -> Export formatted table straight into Excel/Yardi."*
- **Suggestion**:
  - Provide a "Top 3 Use Cases" section with concrete step-by-step inputs and outputs for each scenario.

---

### 28. No Reason to Switch
- **Category**: ICP & Commercial Viability
- **Severity**: Critical
- **Acceptance Rule**: Directly confront the status quo (e.g. manual spreadsheets, existing incumbents, built-in LLM chat) and give a compelling reason to migrate.
- **Detection Signals**: No mention of existing tools, migration effort, or why a user shouldn't just use ChatGPT / Zapier / Google Sheets.
- **Fail Example**: Does not acknowledge that customers already use Notion or Excel for this task.
- **Pass Example**: *"Why switch from ChatGPT Plus? ChatGPT doesn't integrate with your live Postgres schema, doesn't respect HIPAA compliance, and loses context after 30 messages. We maintain permanent project memory and SOC2 isolation."*
- **Suggestion**:
  - Add a "Compare with Status Quo / Incumbents" matrix addressing switching friction, data import, and specific superiority vectors.

---

## Dimension 6: Market Differentiation & Positioning

### 22. No Differentiation
- **Category**: Market Differentiation & Positioning
- **Severity**: Critical
- **Acceptance Rule**: Articulate an unfair technical moat, workflow innovation, proprietary dataset, or architectural advantage.
- **Detection Signals**: Features match the standard baseline of every generic AI wrapper in the niche with zero proprietary edge.
- **Fail Example**: Feature list: 1) AI Writing Assistant, 2) Summarization, 3) Chat with Docs.
- **Pass Example**: *"Trained on 400,000 anonymized tax court filings to detect IRS audit triggers. Standard LLMs hallucinate on state tax law; our deterministic verification engine validates every deduction against IRC §162 rules."*
- **Suggestion**:
  - Identify your singular proprietary edge: Is it proprietary data? Faster execution? Deterministic accuracy? Deep integration? Highlight this edge prominently.

---

### 30. It Looks Like Every Other AI Startup
- **Category**: Market Differentiation & Positioning
- **Severity**: Major
- **Acceptance Rule**: The site must have a unique brand voice, memorable design choices, and distinctive layout that stands out from the generic template herd.
- **Detection Signals**: Combines purple/black dark mode + bento grid + generic "revolutionize" headline + Midjourney glowing brain + fake 5-star reviews + "Powered by AI" badge.
- **Fail Example**: The page could swap its logo with 50 other AI landing pages without anyone noticing a difference.
- **Pass Example**: Memorable visual identity, opinionated founder voice, custom typography, authentic product snapshots, and zero generic buzzwords.
- **Suggestion**:
  - Conduct the "Logo Swap Test": If you paste a competitor's logo on your page, does it still make sense? If yes, strip the generic components and inject domain-specific substance.

---

# Track 2: 20 Web QA Acceptance Criteria (What to Verify & Have / Must-Haves)

Comprehensive functional and technical pre-flight criteria that every production-grade website or landing page must pass before public launch.

---

## Dimension 7: Viewport & Mobile Responsiveness

### AC-01. Remove Horizontal Scrolling
- **Category**: Viewport & Mobile Responsiveness
- **Severity**: Critical
- **Acceptance Rule**: The page must have zero unintended horizontal scrolling at any viewport width (375px mobile through 2560px ultra-wide).
- **Detection Signals**: `document.documentElement.scrollWidth > window.innerWidth`, unconstrained `width: 100vw` with vertical scrollbars, fixed pixel widths exceeding 360px on inner containers, or missing `overflow-x: clip / hidden` on the root container.
- **Fail Example**: Viewing the hero section on an iPhone 13 causes the entire page to pan 30px horizontally, revealing blank white margins.
- **Pass Example**: Layout is strictly bounded: all rows wrap smoothly, media uses `max-width: 100%`, and touch-dragging horizontally does not wobble the viewport.
- **Suggestion**:
  - Add `overflow-x: hidden` (or modern `overflow-x: clip`) to `html, body`.
  - Inspect elements exceeding 100% parent width using browser devtools: `$$('*').filter(el => el.scrollWidth > document.documentElement.clientWidth)`.

---

### AC-02. Fix Mobile Overflow
- **Category**: Viewport & Mobile Responsiveness
- **Severity**: Critical
- **Acceptance Rule**: Text blocks, wide data tables, code snippets, pre elements, and oversized SVG/images must never clip or bleed outside screen boundaries on mobile devices.
- **Detection Signals**: Unwrapped `<table>` elements with fixed column widths, un-wrapped `<pre>` or `<code>` blocks without `overflow-x: auto`, absolute-positioned floating badges overflowing parent boundaries on small viewports.
- **Fail Example**: A code snippet in the feature breakdown section pushes the container 200px off the right edge of a 390px smartphone display.
- **Pass Example**: Code blocks and tables are wrapped in dedicated horizontally-scrollable containers (`overflow-x: auto; -webkit-overflow-scrolling: touch;`) while the parent page maintains rigid 100% viewport width.
- **Suggestion**:
  - Set `max-width: 100%; word-break: break-word;` on text containers.
  - Wrap tables and code blocks in `<div class="overflow-x-auto w-full">`.

---

### AC-03. Make Every Page Mobile-Optimized
- **Category**: Viewport & Mobile Responsiveness
- **Severity**: Critical
- **Acceptance Rule**: Every public page (home, pricing, docs, blog, legal) must be fully responsive, with tap targets $\ge 44 \times 44\text{px}$, legible font sizes ($\ge 16\text{px}$ base body), and proper viewport meta tags.
- **Detection Signals**: Missing `<meta name="viewport" content="width=device-width, initial-scale=1">`, body text shrinking to micro-scale requiring pinch-to-zoom, tap targets spaced closer than 8px apart.
- **Fail Example**: Pricing table renders as an unreadable miniature desktop spreadsheet on mobile screens, forcing users to pinch-zoom to read tier limits.
- **Pass Example**: Responsive CSS grid/flexbox stacks pricing cards vertically on screens $< 768\text{px}$, with large primary CTA buttons spanning full mobile width.
- **Suggestion**:
  - Verify `<meta name="viewport" content="width=device-width, initial-scale=1.0">` is present in `<head>`.
  - Test all pages at 375px, 414px, 768px, 1024px, and 1440px viewports. Ensure font sizes never drop below 14px on mobile.

---

### AC-04. Add a Mobile Menu
- **Category**: Viewport & Mobile Responsiveness
- **Severity**: Major
- **Acceptance Rule**: Viewports under 768px/1024px must offer a clean, functional mobile navigation drawer, hamburger sheet, or sticky bottom bar rather than wrapping 6+ desktop links across three lines.
- **Detection Signals**: Desktop navigation links wrapping into chaotic multi-line headers, hamburger icon that fails to open on touch/click, missing close button/overlay dismissal, or mobile menu trapping tab focus without escape.
- **Fail Example**: Header links (Features, Pricing, Docs, About, Blog, Sign In, Get Started) crowd the mobile hero, pushing the main value proposition below the fold.
- **Pass Example**: Clean hamburger icon reveals an accessible animated slide-over drawer with clear hierarchy, large tap targets, and an active close/escape trigger.
- **Suggestion**:
  - Implement a mobile dialog/drawer triggered by a hamburger button when viewport $< 768\text{px}$.
  - Ensure tapping outside the drawer, clicking a destination link, or pressing `Esc` immediately closes the menu.

---

## Dimension 8: Navigation & Link Integrity

### AC-05. Find Broken Links
- **Category**: Navigation & Link Integrity
- **Severity**: Critical
- **Acceptance Rule**: Zero dead, orphaned, or 404 links across both internal routes and outbound external resources.
- **Detection Signals**: Anchors with `href="#"`, `href=""`, links pointing to non-existent subpaths (e.g. `/features/v2` returning 404), or dead external links (e.g. invalid GitHub/Twitter handles).
- **Fail Example**: Clicking "Read Docs" in the navigation returns a browser `404 Not Found` error.
- **Pass Example**: All internal links resolve with HTTP 200, and external links resolve to active live endpoints with `target="_blank" rel="noopener noreferrer"`.
- **Suggestion**:
  - Run an automated link crawler: verify every `<a>` tag returns HTTP 200 or 301/302.
  - Ban placeholder `href="#"` or replace with functional modal triggers or valid target anchors.

---

### AC-06. Fix Footer Links
- **Category**: Navigation & Link Integrity
- **Severity**: Major
- **Acceptance Rule**: Every link listed in the footer—especially Privacy Policy, Terms of Service, Security, Status, Docs, and Contact—must resolve to a genuine, published destination.
- **Detection Signals**: Footer columns populated with generic template links (e.g. "Careers", "Press Kit", "Privacy") all pointing to `href="#"` or throwing 404s.
- **Fail Example**: Clicking "Privacy Policy" in the footer reloads the top of the homepage because `href="#"`.
- **Pass Example**: Dedicated, complete `/privacy`, `/terms`, and `/security` pages written or generated with real company details.
- **Suggestion**:
  - Either create valid minimal legal pages or delete unpopulated footer links. Never launch with dummy `#` links in the footer.

---

### AC-07. Make the Logo Clickable
- **Category**: Navigation & Link Integrity
- **Severity**: Minor
- **Acceptance Rule**: The primary logo or brand icon located in the site header must be wrapped in a functional link directing users back to the root (`/`) homepage.
- **Detection Signals**: Logo rendered as an inert `<img>`, `<svg>`, or `<span>` without an enclosing `<a href="/">` anchor tag.
- **Fail Example**: User navigates to `/pricing`, clicks the brand logo expecting to return home, but nothing happens.
- **Pass Example**: `<a href="/" aria-label="Acme Home" class="flex items-center gap-2"><img src="/logo.svg" alt="Acme Logo" /></a>`.
- **Suggestion**:
  - Wrap the header logo element in `<a href="/" aria-label="[Brand] Home">`.

---

### AC-08. Fix Broken Buttons
- **Category**: Navigation & Link Integrity
- **Severity**: Critical
- **Acceptance Rule**: Every button or button-styled element must perform an active, observable function (submit form, open modal, trigger checkout, copy code, or navigate to a destination).
- **Detection Signals**: `<button>` tags without `onClick` handlers, empty `<button></button>` containers, or anchor tags styled as buttons that lack an `href`.
- **Fail Example**: User clicks the prominent "Start Free Trial" button in the hero section and nothing happens.
- **Pass Example**: "Start Free Trial" immediately redirects to `/signup` or opens a focused onboarding modal with autofocus on the email input.
- **Suggestion**:
  - Audit all `<button>` and `.btn` classes: ensure each has a wired `type="submit"`, valid `href`, or active click listener with visual feedback.

---

### AC-09. Remove Unused Navigation
- **Category**: Navigation & Link Integrity
- **Severity**: Minor
- **Acceptance Rule**: Strip all placeholder, empty, or unmaintained navigation tabs (e.g., "Blog", "Community", "Changelog" when no content exists).
- **Detection Signals**: Navigation items leading to empty "Coming Soon" stubs, disabled dropdown menus with zero items, or redundant multiple links pointing to the same section.
- **Fail Example**: Top navigation includes "Blog", which links to a blank page containing 1 sample post from 6 months ago titled "Hello World".
- **Pass Example**: Streamlined navigation containing only active, essential links: Product, Pricing, Docs, and Sign In.
- **Suggestion**:
  - Prune pre-launch navigation down to the bare essentials: 3–4 high-intent links only.

---

## Dimension 9: Metadata, SEO & Brand Basics

### AC-10. Fix Page Titles
- **Category**: Metadata, SEO & Brand Basics
- **Severity**: Major
- **Acceptance Rule**: Every page must have a distinct, descriptive, branded `<title>` tag (50–60 characters) stating the product name and primary value proposition.
- **Detection Signals**: Default framework titles like `<title>Vite + React</title>`, `<title>Create Next App</title>`, `<title>Untitled Document</title>`, or generic `<title>Home</title>`.
- **Fail Example**: Browser tab displays: *"Vite + React + TS"* or *"Home - My Web Project"*.
- **Pass Example**: `<title>CloudCut — Deterministic AWS Cost Reduction & Anomaly Alerts</title>`.
- **Suggestion**:
  - Set specific page titles following the pattern: `[Product Name] — [Primary Value Proposition / Action]`.

---

### AC-11. Add Meta Descriptions
- **Category**: Metadata, SEO & Brand Basics
- **Severity**: Major
- **Acceptance Rule**: Provide an enticing, concise `<meta name="description">` (120–160 characters) and OpenGraph/Twitter card tags (`og:title`, `og:image`, `og:description`) so links unfurl attractively on Slack, X/Twitter, and LinkedIn.
- **Detection Signals**: Missing `<meta name="description">`, default boilerplate descriptions (*"Generated by create next app"*), or missing `og:image`.
- **Fail Example**: Sharing the URL in a Slack channel or tweet produces a blank grey card with no preview image and text reading *"Web site created using create-react-app"*.
- **Pass Example**: Sharing produces a high-res 1200x630px branded preview card highlighting the product screenshot and a 140-character summary.
- **Suggestion**:
  - Add `<meta name="description" content="...">`.
  - Add `<meta property="og:image" content="https://domain.com/og-image.png">` with a custom 1200x630 graphic.

---

### AC-12. Add a Favicon
- **Category**: Metadata, SEO & Brand Basics
- **Severity**: Minor
- **Acceptance Rule**: Include a custom brand favicon in SVG/PNG/ICO formats with high-resolution Apple touch icons to prevent default browser globe icons or framework logos.
- **Detection Signals**: Default Vercel triangle, Vite lightning bolt, Create-React-App atom, or browser console 404 for `/favicon.ico`.
- **Fail Example**: Browser tab shows the default Vercel or React spinning atom icon.
- **Pass Example**: Custom SVG/ICO favicon matching the brand mark, supported by `<link rel="icon" href="/favicon.svg" type="image/svg+xml">`.
- **Suggestion**:
  - Generate a 32x32 `.ico`, 192x192 `.png`, and SVG vector icon. Place `favicon.ico` in the web root.

---

### AC-13. Add a Custom 404 Page
- **Category**: Metadata, SEO & Brand Basics
- **Severity**: Minor
- **Acceptance Rule**: A branded 404 page that maintains site styling, explains the missing route, and provides an immediate CTA back to the homepage or documentation.
- **Detection Signals**: Default Nginx 404, Apache error, raw JSON `{ "statusCode": 404, "message": "Not Found" }`, or blank unstyled text.
- **Fail Example**: Mistyping a URL path shows a terrifying stark white Nginx default error screen: *"404 Not Found - nginx/1.18.0"*.
- **Pass Example**: Clean page displaying *"Page not found. The link might be outdated or mistyped."* with a prominent "Return to Homepage" button.
- **Suggestion**:
  - Implement a custom `404.html` (or `not-found.tsx` in Next.js / Astro) containing the site header, footer, and a prominent "Return Home" button.

---

### AC-14. Fix the Copyright Year
- **Category**: Metadata, SEO & Brand Basics
- **Severity**: Minor
- **Acceptance Rule**: The copyright notice in the footer must display the current calendar year.
- **Detection Signals**: Outdated hardcoded years (e.g., `© 2021` or `© 2023`), or missing copyright line.
- **Fail Example**: Footer displays: *"© 2022 Acme Inc. All rights reserved."* on a site launching in 2026.
- **Pass Example**: *"© 2026 Acme Corp. All rights reserved."* or dynamically computed `© {new Date().getFullYear()} Acme Corp.`
- **Suggestion**:
  - Replace hardcoded static years with dynamic `{new Date().getFullYear()}` or manually update to current calendar year.

---

## Dimension 10: Contact & Lead Conversions

### AC-15. Make the Phone Number Clickable
- **Category**: Contact & Lead Conversions
- **Severity**: Minor
- **Acceptance Rule**: Whenever a customer phone number is displayed on the site, wrap it in a proper `tel:` URI scheme so mobile visitors can tap to call instantly.
- **Detection Signals**: Raw plain-text phone numbers (e.g. `+1 (555) 019-2834`) without an `<a href="tel:+15550192834">` wrapper.
- **Fail Example**: Mobile visitor sees a sales phone number but cannot tap it; must manually copy, switch apps, and paste into phone dialer.
- **Pass Example**: `<a href="tel:+15550192834" class="underline">+1 (555) 019-2834</a>`.
- **Suggestion**:
  - Wrap any visible telephone string in `<a href="tel:+[country_code][number]">`.

---

### AC-16. Make the Email Clickable
- **Category**: Contact & Lead Conversions
- **Severity**: Minor
- **Acceptance Rule**: Whenever a contact, support, or founder email address is displayed, wrap it in an accessible `mailto:` hyperlink.
- **Detection Signals**: Unlinked plain-text email strings (e.g., `team@acme.ai`) or email addresses wrapped in dead `href="#"`.
- **Fail Example**: Visitor reads: *"For custom deployment, email us at sales@company.com"*, but clicking does nothing.
- **Pass Example**: `<a href="mailto:sales@company.com" class="hover:underline">sales@company.com</a>`.
- **Suggestion**:
  - Wrap all contact emails in `<a href="mailto:address@domain.com">`.

---

### AC-17. Add Success Messages
- **Category**: Contact & Lead Conversions
- **Severity**: Major
- **Acceptance Rule**: When a visitor submits a contact form, waitlist, or newsletter input, the interface must immediately display a reassuring, high-contrast success state.
- **Detection Signals**: Form button freezes indefinitely without feedback, page refreshes to blank state without confirmation, or submission logs to console only.
- **Fail Example**: User enters their email for the beta waitlist, clicks "Join", the button returns to default state, and the user has no idea if the submission succeeded.
- **Pass Example**: Form smoothly transitions to: *"🎉 You're on the list! Check your inbox for confirmation. We onboard 25 new teams every Tuesday."*
- **Suggestion**:
  - Wire a clear, affirmative success state banner/modal that explains what happens next (e.g. *"Check your email for invite link"*).

---

### AC-18. Add Error Messages
- **Category**: Contact & Lead Conversions
- **Severity**: Major
- **Acceptance Rule**: If form validation fails or a network request errors out, display explicit, user-friendly inline error messages indicating exactly what went wrong and how to correct it.
- **Detection Signals**: Silent failures where the user clicks submit and nothing happens, or generic unhelpful alerts like *"Error: Request failed with status code 500"*.
- **Fail Example**: User enters an invalid email format; the form quietly blocks submission without highlighting the email field or explaining the error.
- **Pass Example**: Red outline on the email field with helper text: *"Please enter a valid work email address (e.g. name@company.com)."*
- **Suggestion**:
  - Provide client-side validation for email formats and required fields before submission.
  - Display accessible error notices above or inline with inputs.

---

## Dimension 11: Content Hygiene & Performance

### AC-19. Remove Placeholder Text
- **Category**: Content Hygiene & Performance
- **Severity**: Critical
- **Acceptance Rule**: Total absence of dummy placeholder copy, Latin filler, developer notes, or unfinished template tokens.
- **Detection Signals**: Matches for *"Lorem Ipsum"*, *"dolor sit amet"*, *"TODO"*, *"TBD"*, *"Insert headline here"*, *"Company Name"*, *"John Doe"*.
- **Fail Example**: Subheadline of a feature card reads: *"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt."*
- **Pass Example**: Every sentence is finished, edited, and conveys authentic product value.
- **Suggestion**:
  - Perform a global case-insensitive search across all codebase templates for `lorem`, `ipsum`, `todo`, `tbd`, and `insert`.

---

### AC-20. Compress Images
- **Category**: Content Hygiene & Performance
- **Severity**: Major
- **Acceptance Rule**: All hero images, screenshots, and visual assets must be compressed, sized appropriately, and preferably served in modern formats (WebP or AVIF) under 250KB per image.
- **Detection Signals**: Raw uncompressed PNG/JPEG files exceeding 1.5MB in size, full 4K screenshots scaled down to 400px width with CSS, missing `loading="lazy"` on below-the-fold assets.
- **Fail Example**: Hero background loads a 6.2MB uncompressed PNG, causing a noticeable 3-second blank white flash on 4G connections (LCP > 4.5s).
- **Pass Example**: Hero screenshot is a 140KB WebP image with explicit `width="1200" height="675"` and `<link rel="preload">` priority.
- **Suggestion**:
  - Convert images to WebP/AVIF via `squoosh`, `sharp`, or ImageMagick.
  - Add `loading="lazy"` and `decoding="async"` to all below-the-fold images.
