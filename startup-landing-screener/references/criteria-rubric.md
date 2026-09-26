# 30 Vibe-Coded Acceptance Criteria & Remediation Rubric

Comprehensive criteria reference for screening startup landing pages. Each criterion defines the red flag to avoid, detection heuristics, impact on conversion/credibility, failure/pass examples, and actionable suggestions.

---

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
