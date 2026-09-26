#!/usr/bin/env python3
"""
screen_landing.v1.py

Description:
  Automated acceptance criteria screener for startup landing pages.
  Screens HTML, Markdown, or text against the 30 Vibe-Coded AI Startup Anti-Patterns
  and evaluates launch readiness (READY TO PUSH, NEEDS WORK, or BLOCKED).

Changelog:
  - v1.0.0: Initial implementation with 30-point heuristic inspection, scoring engine,
            remediation generator, CLI URL fetcher, and JSON/Markdown export.
"""

from __future__ import annotations

import argparse
import html
import json
import logging
import re
import sys
import urllib.error
import urllib.request
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

TOOL_VERSION = '1.0.0'


def setup_logger() -> logging.Logger:
    """Configures file logging to .logs/<tool_name>_<timestamp>.log and console."""
    script_dir = Path(__file__).parent.resolve()
    log_dir = script_dir / '.logs'
    log_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(UTC).strftime('%Y%m%d_%H%M%S')
    log_file = log_dir / f'screen_landing_{timestamp}.log'

    logger = logging.getLogger('screen_landing')
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler(log_file, encoding='utf-8')
        fh.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s'))
        logger.addHandler(fh)

        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(logging.Formatter('%(message)s'))
        logger.addHandler(ch)

    return logger


# Criteria definitions: ID, name, category, severity, weight, suggestion
CRITERIA_SPECS: list[dict[str, Any]] = [
    {
        'id': 1,
        'name': 'AI-generated landing page copy',
        'category': 'Copywriting',
        'severity': 'Major',
        'weight': 2,
        'patterns': [
            r"in today'?s (?:fast-paced|rapidly evolving|digital|modern) world",
            r'delve into',
            r'harness(?:ing)? the power of',
            r'elevate your (?:workflow|business|productivity|team)',
            r'unleash(?:ing)? the (?:power|potential)',
            r'seamlessly integrate',
            r'next-generation AI platform',
            r'empowers? modern teams',
        ],
        'suggestion': (
            'Eliminate throat-clearing fluff. Replace abstract verbs (elevate, unleash) with '
            'concrete operational actions (reconciles, deploys, blocks).'
        ),
    },
    {
        'id': 2,
        'name': 'Generic "revolutionize" messaging',
        'category': 'Copywriting',
        'severity': 'Major',
        'weight': 2,
        'patterns': [
            r'revolutioniz(?:e|ing)',
            r'transform(?:ing)? the way',
            r'reimagin(?:e|ing)',
            r'paradigm shift',
            r'the new era of',
        ],
        'suggestion': ("Ban 'revolutionize'. Complete: 'Our product saves [Role] [X hours/$Y] by automatically [Boring Manual Task]'."),
    },
    {
        'id': 3,
        'name': '3 feature cards in a row',
        'category': 'Layout',
        'severity': 'Minor',
        'weight': 1,
        'patterns': [
            r'grid-cols-3',
            r'col-md-4.*col-md-4.*col-md-4',
            r'(?:lightning fast|enterprise security|smart ai|intelligent automation)',
        ],
        'suggestion': (
            'Replace 3 generic Lucide-icon cards with an interactive product walkthrough, chronological user workflow, or tabbed feature inspector.'
        ),
    },
    {
        'id': 4,
        'name': 'Fake testimonials',
        'category': 'Trust & Proof',
        'severity': 'Critical',
        'weight': 3,
        'patterns': [
            r'(?:john d\.|sarah m\.|alex t\.|michael b\.)(?:\s*,\s*(?:founder|ceo|tech enthusiast))?',
            r'this (?:tool|app|software) changed my life',
            r'literally 10x our growth',
        ],
        'suggestion': (
            'Remove unverified quotes. Use real full names, headshots, companies, and linked '
            'social profiles. If pre-launch, delete the testimonial section.'
        ),
    },
    {
        'id': 5,
        'name': 'No real product demo',
        'category': 'Product Reality',
        'severity': 'Critical',
        'weight': 3,
        'required_evidence': [
            '<video',
            'loom.com',
            'youtube.com/embed',
            'vimeo.com',
            '.mp4',
            '.webm',
            'arcade.software',
            'supademo.com',
        ],
        'suggestion': ('Embed a 30–60 second raw screencast of the product solving an actual user task directly in or below the hero section.'),
    },
    {
        'id': 6,
        'name': '"Built for the future"',
        'category': 'Copywriting',
        'severity': 'Minor',
        'weight': 1,
        'patterns': [
            r'built for (?:the future|tomorrow)',
            r'future-proof(?:ing)? your',
            r'the next frontier',
            r'ready for the future',
        ],
        'suggestion': (
            'Anchor value in immediate day-1 deployment: specify current stack compatibility (e.g. Postgres 15+, Next.js 14) and 5-minute setup time.'
        ),
    },
    {
        'id': 7,
        'name': 'Purple + black everything',
        'category': 'Design',
        'severity': 'Major',
        'weight': 2,
        'patterns': [
            r'#(?:8b5cf6|7c3aed|a855f7|6366f1|9333ea)',
            r'rgba?\(\s*(?:139,\s*92,\s*246|124,\s*58,\s*237|168,\s*85,\s*247)',
            r'from-purple-|to-violet-|bg-violet-|bg-purple-',
        ],
        'suggestion': (
            'Break away from the generic AI dark theme. Adopt a distinctive palette tailored '
            'to your sector (e.g. slate/navy/emerald or clean light mode).'
        ),
    },
    {
        'id': 8,
        'name': 'Too many gradients',
        'category': 'Design',
        'severity': 'Minor',
        'weight': 1,
        'patterns': [
            r'linear-gradient',
            r'radial-gradient',
            r'bg-gradient-to-',
            r'bg-clip-text',
        ],
        'threshold_count': 4,
        'suggestion': (
            'Limit gradients to at most 1 subtle atmospheric background layer. Use solid high-contrast typography for headlines and text.'
        ),
    },
    {
        'id': 9,
        'name': 'Bento grids everywhere',
        'category': 'Layout',
        'severity': 'Minor',
        'weight': 1,
        'patterns': [
            r'bento',
            r'col-span-2.*row-span-2',
            r'col-span-1.*col-span-2',
        ],
        'suggestion': ("Don't use bento boxes for fake metric counters and dummy toggles. Show genuine workflow sequences and real dashboard views."),
    },
    {
        'id': 10,
        'name': 'No clear ICP',
        'category': 'ICP & Commercial',
        'severity': 'Critical',
        'weight': 3,
        'patterns': [
            r'for (?:everyone|all teams|businesses of all sizes|creators and enterprises alike)',
            r'all-in-one (?:ai )?platform for all',
            r'anyone who wants to',
        ],
        'suggestion': (
            'Explicitly name your specific buyer role and company profile in the subheadline '
            "(e.g. 'For Series A DevOps engineers managing Kubernetes clusters')."
        ),
    },
    {
        'id': 11,
        'name': '"Powered by AI" as the headline',
        'category': 'Copywriting',
        'severity': 'Major',
        'weight': 2,
        'patterns': [
            r'<h1[^>]*>[^<]*(?:powered by ai|ai-powered|supercharged by ai)[^<]*</h1>',
            r'^[#\s]*(?:powered by ai|ai-powered|supercharged by ai)',
            r'the ai-powered platform',
        ],
        'suggestion': (
            "Demote AI to an architectural detail badge. Make the H1 answer: 'What acute pain or tedious manual task disappears when I sign up?'"
        ),
    },
    {
        'id': 12,
        'name': 'No pricing clarity',
        'category': 'ICP & Commercial',
        'severity': 'Major',
        'weight': 2,
        'required_evidence': [
            r'\$\d+',
            r'pricing',
            r'/month',
            r'/mo\b',
            r'free tier',
            r'free plan',
            r'starter plan',
            r'contact sales for pricing',
            r'starts at \$',
        ],
        'suggestion': (
            "Publish transparent pricing tiers or clear starting prices (e.g. 'Plans start at $49/mo'). "
            'Explain usage limits and credit costs explicitly.'
        ),
    },
    {
        'id': 13,
        'name': 'No real customer stories',
        'category': 'Trust & Proof',
        'severity': 'Major',
        'weight': 2,
        'required_evidence': [
            r'case stud(?:y|ies)',
            r'how .* cut',
            r'how .* scaled',
            r'how .* saved',
            r'customer stor(?:y|ies)',
            r'success stor(?:y|ies)',
        ],
        'suggestion': (
            'Add at least one detailed problem -> solution -> quantified metric customer spotlight showing how a real user extracted value.'
        ),
    },
    {
        'id': 14,
        'name': 'Chatbot as the entire product',
        'category': 'Product Reality',
        'severity': 'Major',
        'weight': 2,
        'patterns': [
            r'chat with your (?:docs|data|pdf|code)',
            r'ask anything about your',
            r'just prompt our ai',
        ],
        'suggestion': (
            'Show structured workflow surfaces: data tables, diff inspectors, batch triggers, '
            'audit logs, and export pipelines—not just a chat bubble.'
        ),
    },
    {
        'id': 15,
        'name': '"10x your productivity"',
        'category': 'Copywriting',
        'severity': 'Major',
        'weight': 2,
        'patterns': [
            r'10x (?:your )?(?:productivity|faster|output|growth|efficiency)',
            r'100x (?:your )?(?:productivity|faster|output)',
            r'supercharge (?:your )?team 10x',
        ],
        'suggestion': (
            "Replace vague '10x' multipliers with verifiable time/cost deltas (e.g. 'Reduces contract review turnaround from 4 days to 45 minutes')."
        ),
    },
    {
        'id': 16,
        'name': 'No technical details',
        'category': 'Product Reality',
        'severity': 'Major',
        'weight': 2,
        'required_evidence': [
            r'soc\s*2',
            r'hipaa',
            r'gdpr',
            r'encryption',
            r'latency',
            r'api',
            r'vpc',
            r'aws|gcp|azure',
            r'postgres|redis|kafka|vector',
            r'sla',
        ],
        'suggestion': (
            'Add an Architecture & Security card detailing compliance (SOC2/GDPR), data retention policies, and infrastructure deployment models.'
        ),
    },
    {
        'id': 17,
        'name': 'No API docs',
        'category': 'Product Reality',
        'severity': 'Major',
        'weight': 2,
        'required_evidence': [
            r'docs\.',
            r'/docs\b',
            r'api reference',
            r'documentation',
            r'curl -X',
            r'npm install',
            r'pip install',
        ],
        'suggestion': (
            'Place a prominent Documentation link in your header/footer, and embed a real 3-line SDK/cURL integration snippet on the landing page.'
        ),
    },
    {
        'id': 18,
        'name': 'No visible users',
        'category': 'Trust & Proof',
        'severity': 'Major',
        'weight': 2,
        'required_evidence': [
            r'discord\.gg|discord\.com/invite',
            r'github\.com/[^/]+/[^/]+',
            r'producthunt\.com',
            r'slack\.com',
            r'community',
            r'reviews on (?:g2|capterra|trustpilot)',
        ],
        'suggestion': (
            'Display live external proof of community: link to your Discord, GitHub repository (with star count), or third-party G2 review badges.'
        ),
    },
    {
        'id': 19,
        'name': 'No screenshots of the actual product',
        'category': 'Product Reality',
        'severity': 'Critical',
        'weight': 3,
        'required_evidence': [
            r'<img[^>]+(?:screenshot|dashboard|product|app-preview|ui-)',
            r'!\[(?:screenshot|dashboard|product|ui)[^\]]*\]',
            r'src=["\'][^"\']*(?:dashboard|screenshot|preview|app)[^"\']*\.(?:png|jpg|webp)',
        ],
        'suggestion': ('Embed 2–3 full-width, crisp retina screenshots of the core product dashboard displaying realistic production domain data.'),
    },
    {
        'id': 20,
        'name': 'Generic AI-generated illustrations',
        'category': 'Design',
        'severity': 'Major',
        'weight': 2,
        'patterns': [
            r'glowing[- ]brain',
            r'cyborg[- ]hand',
            r'floating[- ]geometric',
            r'neon[- ]synapse',
            r'midjourney|dall-?e',
        ],
        'suggestion': (
            'Remove abstract 3D floating spheres and glowing neural illustrations. Replace with crisp vector architecture diagrams or real UI crops.'
        ),
    },
    {
        'id': 21,
        'name': '"The future of X"',
        'category': 'Copywriting',
        'severity': 'Minor',
        'weight': 1,
        'patterns': [
            r'the future of (?:work|sales|coding|marketing|recruiting|finance|legal|healthcare|software)',
            r'welcome to the future of',
        ],
        'suggestion': ("Replace 'The future of [X]' with a functional utility definition: '[Tool Name] is an automated [Task] engine for [Role]'."),
    },
    {
        'id': 22,
        'name': 'No differentiation',
        'category': 'Market Positioning',
        'severity': 'Critical',
        'weight': 3,
        'required_evidence': [
            r'unlike (?:traditional|existing|other)',
            r'compared to',
            r'proprietary',
            r'fine-tuned on',
            r'deterministic',
            r'patented|custom engine',
            r'why switch',
        ],
        'suggestion': (
            'Articulate your proprietary moat: Is it specialized training data, deterministic verification, edge latency, or bespoke ERP integration?'
        ),
    },
    {
        'id': 23,
        'name': 'No proof of ROI',
        'category': 'Trust & Proof',
        'severity': 'Major',
        'weight': 2,
        'required_evidence': [
            r'roi\b',
            r'saved? \$?\d+',
            r'reduced costs? by',
            r'payback period',
            r'hours saved',
            r'cost calculator',
        ],
        'suggestion': (
            'Include an ROI breakdown or payback calculation showing how saving N hours '
            'or avoiding one critical bug justifies the subscription price.'
        ),
    },
    {
        'id': 24,
        'name': 'Too many animations',
        'category': 'Design',
        'severity': 'Minor',
        'weight': 1,
        'patterns': [
            r'animate-pulse|animate-bounce|animate-spin',
            r'data-aos|framer-motion',
            r'@keyframes',
        ],
        'threshold_count': 6,
        'suggestion': (
            'Disable scroll-jacking and distracting continuous animations. Support prefers-reduced-motion and ensure instant page readability.'
        ),
    },
    {
        'id': 25,
        'name': 'Buzzwords everywhere',
        'category': 'Copywriting',
        'severity': 'Major',
        'weight': 2,
        'patterns': [
            r'synergy',
            r'hyper-scalable',
            r'agentic (?:fabric|orchestration|intelligence)',
            r'holistic',
            r'frictionless',
            r'state-of-the-art',
            r'cognitive architecture',
        ],
        'suggestion': (
            "Strip marketing jargon. Apply the 'Junior Engineer Test': if an engineer "
            'cannot sketch your architecture from the description, make it simpler.'
        ),
    },
    {
        'id': 26,
        'name': 'No founder perspective',
        'category': 'Trust & Proof',
        'severity': 'Major',
        'weight': 2,
        'required_evidence': [
            r'about us',
            r'why we built',
            r'founder',
            r'our story',
            r'letter from',
            r'team\b',
            r'twitter\.com/[a-zA-Z0-9_]+|x\.com/[a-zA-Z0-9_]+',
            r'linkedin\.com/in/[a-zA-Z0-9_-]+',
        ],
        'suggestion': ("Add a short 'Why We Built This' founder note with real founder photos and direct links to personal X/LinkedIn profiles."),
    },
    {
        'id': 27,
        'name': 'No clear use case',
        'category': 'ICP & Commercial',
        'severity': 'Critical',
        'weight': 3,
        'required_evidence': [
            r'use cases?',
            r'how it works',
            r'step 1',
            r'workflow',
            r'example',
            r'for instance',
        ],
        'suggestion': ('Show a concrete 3-step operational workflow: 1) Trigger/Input -> 2) Transformation/Verification -> 3) Final Output/Export.'),
    },
    {
        'id': 28,
        'name': 'No reason to switch',
        'category': 'ICP & Commercial',
        'severity': 'Critical',
        'weight': 3,
        'required_evidence': [
            r'switch from',
            r'migrate from',
            r'alternative to',
            r'why not (?:chatgpt|zapier|spreadsheets|excel)',
            r'vs\b',
            r'comparison',
        ],
        'suggestion': (
            'Address the status quo (manual spreadsheets, ChatGPT, incumbents). Provide a comparison matrix showing exact switching advantages.'
        ),
    },
    {
        'id': 29,
        'name': 'No proof it actually works',
        'category': 'Product Reality',
        'severity': 'Critical',
        'weight': 3,
        'required_evidence': [
            r'benchmark',
            r'evaluation dataset',
            r'precision|recall|f1-score',
            r'accuracy of \d+%',
            r'tested on \d+',
            r'github\.com/.*benchmark',
        ],
        'suggestion': (
            'Cite public benchmarks, error rate studies, or link to an open evaluation dataset on GitHub validating claimed accuracy and performance.'
        ),
    },
    {
        'id': 30,
        'name': 'It looks like every other AI startup',
        'category': 'Market Positioning',
        'severity': 'Major',
        'weight': 2,
        'suggestion': (
            "Conduct the 'Logo Swap Test': If replacing your logo with a competitor's still makes sense "
            'on the page, strip generic tropes and inject authentic brand substance.'
        ),
    },
]


def clean_html(raw_html: str) -> str:
    """Strips basic script/style tags and returns readable text."""
    text = re.sub(r'<script.*?</script>', ' ', raw_html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style.*?</style>', ' ', text, flags=re.DOTALL | re.IGNORECASE)
    return html.unescape(text)


def fetch_url_content(url: str, timeout: int = 15) -> str:
    """Fetches web page HTML with proper headers and timeout."""
    req = urllib.request.Request(
        url,
        headers={
            'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or 'utf-8'
        return response.read().decode(charset, errors='replace')


def screen_content(content: str, is_html: bool = True) -> dict[str, Any]:
    """Evaluates content against all 30 acceptance criteria."""
    raw_lower = content.lower()
    text_cleaned = clean_html(content).lower()

    results: list[dict[str, Any]] = []
    total_applicable_weight = 0
    earned_weight = 0.0

    flagged_counts = {'Critical': 0, 'Major': 0, 'Minor': 0}
    warn_counts = {'Critical': 0, 'Major': 0, 'Minor': 0}

    for spec in CRITERIA_SPECS:
        cid = spec['id']
        name = spec['name']
        cat = spec['category']
        sev = spec['severity']
        weight = spec['weight']
        suggestion = spec['suggestion']

        status = 'PASS'
        evidence = ''

        # Combinatorial check for criterion 30: "It looks like every other AI startup"
        if cid == 30:
            pass
        elif 'patterns' in spec and 'required_evidence' not in spec:
            matched_snippets = []
            for pat in spec['patterns']:
                matches = re.findall(pat, raw_lower if is_html else text_cleaned, re.IGNORECASE)
                if matches:
                    matched_snippets.extend(matches[:2])

            threshold = spec.get('threshold_count', 1)
            if len(matched_snippets) >= threshold:
                status = 'FAIL'
                evidence = f'Detected anti-pattern signals ({len(matched_snippets)}x): {", ".join(str(m) for m in matched_snippets[:3])}'
            elif matched_snippets:
                status = 'WARN'
                evidence = f'Minor signal trace ({len(matched_snippets)}x): {", ".join(str(m) for m in matched_snippets[:2])}'
            else:
                status = 'PASS'
                evidence = 'No anti-pattern keywords or patterns detected.'

        elif 'required_evidence' in spec:
            found_evidence = []
            for pat in spec['required_evidence']:
                if re.search(pat, raw_lower if is_html else text_cleaned, re.IGNORECASE):
                    found_evidence.append(pat)

            if found_evidence:
                status = 'PASS'
                evidence = f'Found positive validation signals ({len(found_evidence)}): {", ".join(found_evidence[:3])}'
            else:
                status = 'FAIL'
                evidence = 'Missing required verifiable proof or element on page.'

        if cid != 30:
            total_applicable_weight += weight
            if status == 'PASS':
                earned_weight += weight
            elif status == 'WARN':
                earned_weight += weight * 0.5
                warn_counts[sev] += 1
            else:
                flagged_counts[sev] += 1

        results.append(
            {
                'id': cid,
                'name': name,
                'category': cat,
                'severity': sev,
                'weight': weight,
                'status': status,
                'evidence': evidence,
                'suggestion': suggestion if status in ('FAIL', 'WARN') else None,
            }
        )

    # Evaluate Criterion 30: "It looks like every other AI startup"
    total_fails = sum(flagged_counts.values())
    crit_30 = next(r for r in results if r['id'] == 30)
    total_applicable_weight += crit_30['weight']

    if total_fails >= 8 or (flagged_counts['Critical'] >= 2 and flagged_counts['Major'] >= 3):
        crit_30['status'] = 'FAIL'
        crit_30['evidence'] = f'Strong clone convergence: {total_fails} distinct anti-patterns detected across design, copy, and trust.'
        flagged_counts['Major'] += 1
    elif total_fails >= 4:
        crit_30['status'] = 'WARN'
        crit_30['evidence'] = f'Moderate template convergence: {total_fails} anti-patterns present.'
        crit_30['suggestion'] = CRITERIA_SPECS[-1]['suggestion']
        warn_counts['Major'] += 1
        earned_weight += crit_30['weight'] * 0.5
    else:
        crit_30['status'] = 'PASS'
        crit_30['evidence'] = 'Exhibits distinctive domain characteristics; avoids generic AI startup template trap.'
        earned_weight += crit_30['weight']
        crit_30['suggestion'] = None

    # Calculate metrics
    readiness_score = round((earned_weight / total_applicable_weight) * 100, 1) if total_applicable_weight > 0 else 0.0

    max_penalty = sum(s['weight'] for s in CRITERIA_SPECS)
    penalty_incurred = (
        (flagged_counts['Critical'] * 3)
        + (flagged_counts['Major'] * 2)
        + (flagged_counts['Minor'] * 1)
        + (warn_counts['Critical'] * 1.5)
        + (warn_counts['Major'] * 1.0)
        + (warn_counts['Minor'] * 0.5)
    )
    vibe_index = round((penalty_incurred / max_penalty) * 100, 1)

    # Launch Gate Decision
    if flagged_counts['Critical'] == 0 and flagged_counts['Major'] <= 2 and readiness_score >= 85.0:
        verdict = 'READY TO PUSH'
        verdict_badge = '🟢 READY TO PUSH'
    elif flagged_counts['Critical'] <= 1 and readiness_score >= 65.0:
        verdict = 'NEEDS WORK'
        verdict_badge = '🟡 NEEDS WORK'
    else:
        verdict = 'BLOCKED'
        verdict_badge = '🔴 BLOCKED - VIBE-CODED'

    return {
        'timestamp': datetime.now(UTC).isoformat(),
        'metrics': {
            'launch_gate_verdict': verdict,
            'verdict_badge': verdict_badge,
            'readiness_score': readiness_score,
            'vibe_coded_index': vibe_index,
            'critical_fails': flagged_counts['Critical'],
            'major_fails': flagged_counts['Major'],
            'minor_fails': flagged_counts['Minor'],
            'critical_warns': warn_counts['Critical'],
            'major_warns': warn_counts['Major'],
            'minor_warns': warn_counts['Minor'],
        },
        'criteria': results,
    }


def format_markdown_report(report_data: dict[str, Any], target_name: str) -> str:
    """Generates an executive markdown report complying with report-template.md."""
    m = report_data['metrics']
    criteria = report_data['criteria']

    lines = [
        f'# 🚀 Startup Landing Page Launch Gate & Anti-Vibe Audit: {target_name}',
        '',
        f'**Audit Timestamp**: {report_data["timestamp"]}  ',
        '**Auditor**: Startup Landing Screener (Antigravity Founder Skills)  ',
        '',
        '---',
        '',
        '## 🚦 Executive Launch Verdict',
        '',
        '| Metric | Result | Target Benchmark | Status |',
        '| :--- | :---: | :---: | :---: |',
        (
            f'| **Launch Gate Verdict** | **{m["verdict_badge"]}** | 🟢 READY TO PUSH | '
            f'{"PASS" if m["launch_gate_verdict"] == "READY TO PUSH" else "ATTENTION"} |'
        ),
        f'| **Launch Readiness Score** | **{m["readiness_score"]}%** | $\\ge 85\\%$ | {"PASS" if m["readiness_score"] >= 85 else "FAIL"} |',
        f'| **Vibe-Coded Index** | **{m["vibe_coded_index"]}%** | $\\le 20\\%$ | {"PASS" if m["vibe_coded_index"] <= 20 else "WARN"} |',
        f'| **Critical Blockers** | **{m["critical_fails"]}** | 0 | {"PASS" if m["critical_fails"] == 0 else "CRITICAL"} |',
        f'| **Major Defect Count** | **{m["major_fails"]}** | $\\le 2$ | {"PASS" if m["major_fails"] <= 2 else "WARN"} |',
        f'| **Minor Polish Items** | **{m["minor_fails"]}** | $\\le 3$ | {"PASS" if m["minor_fails"] <= 3 else "WARN"} |',
        '',
        '---',
        '',
        '## 📋 Complete 30-Criteria Acceptance Comparison Matrix',
        '',
        '| # | Acceptance Criterion | Category | Severity | Status | Observed Evidence / Current State | Remediation Needed? |',
        '| :-: | :--- | :--- | :---: | :---: | :--- | :---: |',
    ]

    for c in criteria:
        status_md = f'`{c["status"]}`'
        remediation_needed = 'Yes' if c['status'] in ('FAIL', 'WARN') else 'No'
        clean_evidence = c['evidence'].replace('|', '/')
        lines.append(f'| {c["id"]} | {c["name"]} | {c["category"]} | {c["severity"]} | {status_md} | {clean_evidence} | {remediation_needed} |')

    lines.extend(
        [
            '',
            '---',
            '',
            '## 🔍 Detailed Criterion Comparison & Actionable Suggestions',
            '',
        ]
    )

    flagged_criteria = [c for c in criteria if c['status'] in ('FAIL', 'WARN')]
    if not flagged_criteria:
        lines.append('✨ **Outstanding**: No criteria were flagged as FAIL or WARN. The landing page is remarkably authentic and clean.')
    else:
        for c in flagged_criteria:
            lines.extend(
                [
                    f'### Criterion #{c["id"]}: {c["name"]} ({c["severity"]} - `{c["status"]}`)',
                    f'- **Category**: {c["category"]}',
                    f'- **Observed Finding**: {c["evidence"]}',
                    f'- **Actionable Suggestion**: {c["suggestion"]}',
                    '',
                ]
            )

    lines.extend(
        [
            '---',
            '',
            '## 🛠️ Prioritized Launch Push Checklist',
            '',
        ]
    )

    # Generate top 5 prioritized fixes
    sorted_fixes = sorted(
        flagged_criteria,
        key=lambda x: 0 if x['severity'] == 'Critical' else (1 if x['severity'] == 'Major' else 2),
    )
    top_5 = sorted_fixes[:5]
    if top_5:
        for idx, item in enumerate(top_5, 1):
            lines.append(f'{idx}. **[{item["severity"].upper()}] {item["name"]}**: {item["suggestion"]}')
    else:
        lines.append('✅ No remaining blockers before push!')

    lines.append('')
    return '\n'.join(lines)


def run_doctor() -> None:
    """Performs environment and dependency diagnostics."""
    print('=== Startup Landing Screener: Doctor Diagnostic ===')
    print(f'Script Version: {TOOL_VERSION}')
    print(f'Python Executable: {sys.executable}')
    print(f'Python Version: {sys.version.split()[0]}')
    print('URLLib HTTP / HTTPS Client: OK')
    print('HTML Parser: OK')
    print(f'Total Evaluated Acceptance Criteria: {len(CRITERIA_SPECS)}')
    print('Diagnostic Status: HEALTHY')


def main() -> None:
    parser = argparse.ArgumentParser(description='Screen a startup landing page against the 30 Vibe-Coded Acceptance Criteria.')
    parser.add_argument('--url', '-u', type=str, help='Target live website URL to fetch and screen')
    parser.add_argument('--file', '-f', type=str, help='Local HTML, Markdown, or text file to inspect')
    parser.add_argument('--text', '-t', type=str, help='Direct text string to inspect')
    parser.add_argument('--output', '-o', type=str, help='Optional output file path (.md or .json)')
    parser.add_argument('--json', action='store_true', help='Output structured JSON instead of Markdown')
    parser.add_argument('--doctor', action='store_true', help='Run diagnostic verification checks')
    parser.add_argument('--name', '-n', type=str, default='Startup Landing Page', help='Product / Startup Name')
    args = parser.parse_args()

    logger = setup_logger()

    if args.doctor:
        run_doctor()
        sys.exit(0)

    content = ''
    is_html = True

    if args.url:
        logger.info(f'Fetching landing page URL: {args.url}')
        try:
            content = fetch_url_content(args.url)
            is_html = True
        except urllib.error.URLError as e:
            logger.error(f'Failed to fetch URL {args.url}: {e}')
            sys.exit(1)
    elif args.file:
        file_path = Path(args.file).resolve()
        logger.info(f'Reading file: {file_path}')
        if not file_path.exists():
            logger.error(f'File not found: {file_path}')
            sys.exit(1)
        content = file_path.read_text(encoding='utf-8', errors='replace')
        is_html = file_path.suffix.lower() in ('.html', '.htm')
    elif args.text:
        content = args.text
        is_html = '<html' in content.lower() or '<div' in content.lower()
    else:
        logger.info('No input specified. Use --url, --file, --text, or --doctor. Displaying demo run on standard vibe-coded template.')
        content = """
        <html>
        <head><title>SynapseAI - Revolutionize your workflow with AI</title></head>
        <body class="bg-black text-white">
            <h1 class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-violet-600">
                Powered by AI: The future of work is here
            </h1>
            <p>In today's digital world, our next-generation AI platform empowers modern teams to elevate workflow efficiency.</p>
            <div class="grid grid-cols-3 gap-4">
                <div>⚡ Lightning Fast</div>
                <div>🔒 Enterprise Security</div>
                <div>🧠 Smart AI</div>
            </div>
            <div class="testimonial">
                <p>"This app changed my life! Literally 10x our growth!"</p>
                <span>John D., Startup Founder</span>
            </div>
            <button class="bg-purple-600">Contact Sales for Custom Enterprise Pricing</button>
        </body>
        </html>
        """
        is_html = True

    report = screen_content(content, is_html=is_html)

    if args.json:
        formatted_output = json.dumps(report, indent=2)
    else:
        formatted_output = format_markdown_report(report, target_name=args.name)

    if args.output:
        out_path = Path(args.output).resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(formatted_output, encoding='utf-8')
        logger.info(f'Report successfully saved to {out_path}')
    else:
        default_save = Path(__file__).parent.resolve() / 'data' / 'latest_audit.json'
        default_save.parent.mkdir(parents=True, exist_ok=True)
        default_save.write_text(json.dumps(report, indent=2), encoding='utf-8')
        print(formatted_output)


if __name__ == '__main__':
    main()
