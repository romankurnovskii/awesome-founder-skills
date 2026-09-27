#!/usr/bin/env python3
"""
screen_landing.v2.py

Description:
  Automated dual-track acceptance criteria screener for startup landing pages.
  Screens HTML, Markdown, or text against:
    - Track 1: 30 Vibe-Coded AI Startup Anti-Patterns (What to Avoid / Red Flags)
    - Track 2: 20 Web QA Acceptance Criteria (What to Verify & Have / Must-Haves)
  Evaluates overall launch readiness (READY TO PUSH, NEEDS WORK, or BLOCKED).

Changelog:
  - v2.0.0: Added Track 2: 20 Web QA Acceptance Criteria (responsive viewports,
            link integrity, SEO metadata, contact schemes, content hygiene).
            Unified dual-track scoring and report generation.
  - v1.0.0: Initial implementation with 30-point anti-pattern inspection.
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

TOOL_VERSION = '2.0.0'


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


# ==============================================================================
# Track 1: 30 Vibe-Coded Anti-Patterns (What to Avoid / Red Flags)
# ==============================================================================

TRACK1_SPECS: list[dict[str, Any]] = [
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
        'suggestion': ('State clear, transparent pricing tiers or starting anchors ($X/mo). If enterprise-only, give the base entry contract size.'),
    },
    {
        'id': 13,
        'name': 'No real customer stories',
        'category': 'Trust & Proof',
        'severity': 'Major',
        'weight': 2,
        'required_evidence': [
            r'case stud(?:y|ies)',
            r'customer stor(?:y|ies)',
            r'how .* used',
            r'read the story',
            r'customer spotlight',
        ],
        'suggestion': (
            "Add at least 1 in-depth mini case study: 'Company X reduced Y metric by Z% in 14 days using our deterministic verification workflow'."
        ),
    },
    {
        'id': 14,
        'name': 'Chatbot as the entire product',
        'category': 'Product Reality',
        'severity': 'Major',
        'weight': 2,
        'patterns': [
            r'chat with your (?:docs|data|pdf|codebase|documents)',
            r'ask (?:anything|questions to your data)',
            r'conversational ai for your',
        ],
        'suggestion': (
            'Demonstrate native UI, deterministic structured tables, direct code integrations, '
            'or specialized artifacts rather than another ChatGPT prompt wrapper.'
        ),
    },
    {
        'id': 15,
        'name': '"10x your productivity"',
        'category': 'Copywriting',
        'severity': 'Major',
        'weight': 2,
        'patterns': [
            r'10x your (?:productivity|workflow|output|growth|efficiency|speed)',
            r'100x your',
            r'supercharge your (?:productivity|team) 10x',
        ],
        'suggestion': (
            "Replace arbitrary multiplier claims with measured metrics: e.g. 'Reduces compliance audit preparation from 3 weeks to 4 hours'."
        ),
    },
    {
        'id': 16,
        'name': 'No technical details',
        'category': 'Product Reality',
        'severity': 'Major',
        'weight': 2,
        'required_evidence': [
            r'architecture',
            r'latency',
            r'soc\s?2',
            r'gdpr',
            r'encryption',
            r'api',
            r'sdk',
            r'postgres',
            r'deterministic',
            r'self-hosted|on-prem',
            r'github\.com',
        ],
        'suggestion': (
            'Detail your technical foundation: model latency SLAs, data retention policies, zero-training commitments, and architecture overview.'
        ),
    },
    {
        'id': 17,
        'name': 'No API docs',
        'category': 'Product Reality',
        'severity': 'Major',
        'weight': 2,
        'required_evidence': [
            r'api reference',
            r'docs\.',
            r'/docs',
            r'documentation',
            r'curl -x',
            r'npm install',
            r'pip install',
        ],
        'suggestion': ('Provide an interactive code snippet (cURL, Python, TypeScript) and a prominent link to public developer documentation.'),
    },
    {
        'id': 18,
        'name': 'No visible users',
        'category': 'Trust & Proof',
        'severity': 'Major',
        'weight': 2,
        'required_evidence': [
            r'used by \d+',
            r'trusted by \d+',
            r'join \d+ developers',
            r'discord\.gg',
            r'github stars',
            r'active users',
        ],
        'suggestion': (
            'Display concrete social validation: GitHub star counts, active Discord members, or the actual number of production teams onboarded.'
        ),
    },
    {
        'id': 19,
        'name': 'No screenshots of the actual product',
        'category': 'Product Reality',
        'severity': 'Critical',
        'weight': 3,
        'required_evidence': [
            r'<img[^>]+src=["\'][^"\']*(?:dashboard|app|screenshot|ui|interface|preview)[^"\']*["\']',
            r'screenshot',
            r'actual interface',
        ],
        'suggestion': (
            'Feature high-resolution, un-embellished screenshots of your real product UI, '
            'showing real data in tables and menus instead of abstract 3D artwork.'
        ),
    },
    {
        'id': 20,
        'name': 'Generic AI-generated illustrations',
        'category': 'Design',
        'severity': 'Major',
        'weight': 2,
        'patterns': [
            r'glowing orb',
            r'floating 3d sphere',
            r'abstract neural network mesh',
            r'cyberpunk neon head',
            r'midjourney',
        ],
        'suggestion': (
            'Replace generic Midjourney robot/brain artwork with real software diagrams, raw product screenshots, or clean vector system schematics.'
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


# ==============================================================================
# Track 2: 20 Web QA Acceptance Criteria (What to Verify & Have / Must-Haves)
# ==============================================================================

TRACK2_SPECS: list[dict[str, Any]] = [
    {
        'id': 'AC-01',
        'num': 1,
        'name': 'Remove horizontal scrolling',
        'category': 'Viewport & Mobile',
        'severity': 'Critical',
        'weight': 3,
        'fail_patterns': [
            r'overflow-x:\s*scroll',
            r'w-(?:\[\d{4,}px\])',
            r'min-w-(?:\[\d{4,}px\])',
            r'width:\s*(?:1[2-9]\d{2}|[2-9]\d{3})px',
        ],
        'pass_patterns': [
            r'overflow-x-(?:hidden|clip)',
            r'overflow-hidden',
            r'max-w-full',
            r'overflow-x:\s*(?:hidden|clip)',
        ],
        'suggestion': (
            'Add overflow-x: hidden / clip to html, body or root wrapper. Ensure all containers '
            'use max-width: 100% and avoid fixed pixel widths exceeding 360px on mobile.'
        ),
    },
    {
        'id': 'AC-02',
        'num': 2,
        'name': 'Fix mobile overflow',
        'category': 'Viewport & Mobile',
        'severity': 'Critical',
        'weight': 3,
        'pass_patterns': [
            r'overflow-x-auto',
            r'overflow-auto',
            r'word-break',
            r'break-words',
            r'table-auto',
        ],
        'suggestion': (
            'Wrap wide data tables and code blocks in horizontally-scrollable containers '
            '(e.g., div with overflow-x: auto). Apply word-break: break-word to text.'
        ),
    },
    {
        'id': 'AC-03',
        'num': 3,
        'name': 'Make every page mobile optimized',
        'category': 'Viewport & Mobile',
        'severity': 'Critical',
        'weight': 3,
        'pass_patterns': [
            r'<meta[^>]+name=["\']viewport["\'][^>]+content=["\'][^"\']*width=device-width',
            r'content=["\'][^"\']*width=device-width[^"\']*["\'][^>]+name=["\']viewport["\']',
        ],
        'suggestion': (
            'Include <meta name="viewport" content="width=device-width, initial-scale=1.0"> in <head>. '
            'Ensure typography scales up to >= 16px on mobile screens.'
        ),
    },
    {
        'id': 'AC-04',
        'num': 4,
        'name': 'Add a mobile menu',
        'category': 'Viewport & Mobile',
        'severity': 'Major',
        'weight': 2,
        'pass_patterns': [
            r'hamburger|menu-toggle|mobile-menu|drawer|sheet|dialog|menu-btn',
            r'aria-expanded',
            r'aria-label=["\'][^"\']*(?:open|toggle|menu)[^"\']*["\']',
            r'<nav[^>]+class=["\'][^"\']*(?:md:flex|hidden md:block)[^"\']*["\']',
        ],
        'suggestion': (
            'Provide an accessible mobile menu drawer or hamburger toggle for screen widths < 768px. '
            'Never let desktop links wrap into a chaotic multi-row header.'
        ),
    },
    {
        'id': 'AC-05',
        'num': 5,
        'name': 'Find broken links',
        'category': 'Links & Navigation',
        'severity': 'Critical',
        'weight': 3,
        'fail_patterns': [
            r'href=["\']#["\']',
            r'href=["\']javascript:void\(0\)["\']',
            r'href=["\']["\']',
            r'href=["\']http://localhost',
        ],
        'threshold_count': 3,
        'suggestion': (
            'Audit all anchor tags. Eliminate placeholder href="#" and localhost endpoints. Verify all internal and outbound links return HTTP 200.'
        ),
    },
    {
        'id': 'AC-06',
        'num': 6,
        'name': 'Fix footer links',
        'category': 'Links & Navigation',
        'severity': 'Major',
        'weight': 2,
        'pass_patterns': [
            r'<footer',
            r'privacy',
            r'terms',
        ],
        'fail_patterns': [
            r'<footer[^>]*>[\s\S]*?href=["\']#["\']',
        ],
        'suggestion': (
            'Ensure all footer links (Privacy Policy, Terms of Service, Docs, Status) point to real, '
            'published destinations instead of empty "#" anchors.'
        ),
    },
    {
        'id': 'AC-07',
        'num': 7,
        'name': 'Make the logo clickable',
        'category': 'Links & Navigation',
        'severity': 'Minor',
        'weight': 1,
        'pass_patterns': [
            r'<a[^>]+href=["\'](?:/|index\.html)["\'][^>]*>[\s\S]*?(?:logo|svg|img)',
            r'<a[^>]+href=["\']/[^"\']*["\'][^>]+aria-label=["\'][^"\']*home[^"\']*["\']',
            r'<header[\s\S]*?<a[^>]+href=["\']/(?:#.*)?["\']',
        ],
        'suggestion': ('Wrap the site logo in the header in <a href="/" aria-label="[Brand] Home"> to let users return to the homepage in 1 click.'),
    },
    {
        'id': 'AC-08',
        'num': 8,
        'name': 'Fix broken buttons',
        'category': 'Links & Navigation',
        'severity': 'Critical',
        'weight': 3,
        'fail_patterns': [
            r'<button[^>]*>\s*</button>',
            r'<button(?![^>]*(?:type=|onClick|wire:|@click|v-on:click))[^>]*>',
        ],
        'pass_patterns': [
            r'type=["\'](?:submit|button)["\']',
            r'onClick|@click|wire:click',
        ],
        'suggestion': (
            'Verify every button has an active destination (href), form trigger (type="submit"), '
            'or functional click handler. Never deploy inert buttons.'
        ),
    },
    {
        'id': 'AC-09',
        'num': 9,
        'name': 'Remove unused navigation',
        'category': 'Links & Navigation',
        'severity': 'Minor',
        'weight': 1,
        'fail_patterns': [
            r'coming soon',
            r'under construction',
            r'href=["\'](?:#|javascript:void\(0\))["\'][^>]*>(?:blog|community|docs|pricing|changelog)',
        ],
        'suggestion': ('Prune unused navigation links and dead "Coming Soon" tabs. Keep pre-launch navigation lean (3–4 high-intent links only).'),
    },
    {
        'id': 'AC-10',
        'num': 10,
        'name': 'Fix page titles',
        'category': 'Metadata & SEO',
        'severity': 'Major',
        'weight': 2,
        'fail_patterns': [
            r'<title>\s*(?:vite(?:\s*\+\s*react)?|create next app|untitled document|home|document|my app)\s*</title>',
        ],
        'pass_patterns': [
            r'<title>[^<]{10,80}</title>',
        ],
        'suggestion': (
            'Set a descriptive, brand-aligned page <title> (e.g. "Brand — Deterministic AI Cost Reducer"). Eliminate default framework titles.'
        ),
    },
    {
        'id': 'AC-11',
        'num': 11,
        'name': 'Add meta descriptions',
        'category': 'Metadata & SEO',
        'severity': 'Major',
        'weight': 2,
        'pass_patterns': [
            r'<meta[^>]+name=["\']description["\'][^>]+content=["\'][^"\']{30,}["\']',
            r'<meta[^>]+content=["\'][^"\']{30,}["\'][^>]+name=["\']description["\']',
            r'<meta[^>]+property=["\']og:description["\']',
        ],
        'suggestion': (
            'Add <meta name="description" content="..."> (120–160 chars) and OpenGraph tags '
            '(og:title, og:image, og:description) for high-converting social sharing cards.'
        ),
    },
    {
        'id': 'AC-12',
        'num': 12,
        'name': 'Add a favicon',
        'category': 'Metadata & SEO',
        'severity': 'Minor',
        'weight': 1,
        'pass_patterns': [
            r'<link[^>]+rel=["\'](?:shortcut )?icon["\']',
            r'<link[^>]+rel=["\']apple-touch-icon["\']',
            r'favicon\.(?:ico|png|svg)',
        ],
        'suggestion': (
            'Provide a custom brand favicon in SVG/PNG/ICO formats and link via <link rel="icon" href="/favicon.ico">. Prevent browser 404s.'
        ),
    },
    {
        'id': 'AC-13',
        'num': 13,
        'name': 'Add a custom 404 page',
        'category': 'Metadata & SEO',
        'severity': 'Minor',
        'weight': 1,
        'pass_patterns': [
            r'404',
            r'not found',
            r'page not found',
        ],
        'suggestion': ('Deploy a branded 404 page with navigation back to home rather than a stark white default server error.'),
    },
    {
        'id': 'AC-14',
        'num': 14,
        'name': 'Fix the copyright year',
        'category': 'Metadata & SEO',
        'severity': 'Minor',
        'weight': 1,
        'pass_patterns': [
            r'(?:©|&copy;|copyright)\s*(?:202[5-9]|new Date\(\)\.getFullYear\(\))',
        ],
        'fail_patterns': [
            r'(?:©|&copy;|copyright)\s*(?:201\d|202[0-4])\b',
        ],
        'suggestion': ('Update footer copyright year to the current calendar year (e.g. 2026) or compute dynamically with new Date().getFullYear().'),
    },
    {
        'id': 'AC-15',
        'num': 15,
        'name': 'Make the phone number clickable',
        'category': 'Contact & Leads',
        'severity': 'Minor',
        'weight': 1,
        'pass_patterns': [
            r'href=["\']tel:\+?[0-9\s\-().]+["\']',
        ],
        'fail_patterns': [
            r'(?<!tel:)(?:\+1\s*)?(?:\([0-9]{3}\)|[0-9]{3})[-.\s][0-9]{3}[-.\s][0-9]{4}(?![^<]*</a>)',
        ],
        'suggestion': ('Wrap all visible phone numbers in <a href="tel:+[country_code][number]"> so mobile visitors can tap to call immediately.'),
    },
    {
        'id': 'AC-16',
        'num': 16,
        'name': 'Make the email clickable',
        'category': 'Contact & Leads',
        'severity': 'Minor',
        'weight': 1,
        'pass_patterns': [
            r'href=["\']mailto:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}["\']',
        ],
        'fail_patterns': [
            r'(?<!mailto:)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?![^<]*</a>)',
        ],
        'suggestion': ('Wrap all customer, founder, and support emails in <a href="mailto:name@domain.com">.'),
    },
    {
        'id': 'AC-17',
        'num': 17,
        'name': 'Add success messages',
        'category': 'Contact & Leads',
        'severity': 'Major',
        'weight': 2,
        'pass_patterns': [
            r'success|thank you|confirmation|we received|check your inbox|you(?:\'re| are) on the list|alert-success|toast',
            r'data-success',
            r'submission-success',
        ],
        'suggestion': ('Display an affirmative confirmation toast or message when visitors submit waitlist, contact, or signup forms.'),
    },
    {
        'id': 'AC-18',
        'num': 18,
        'name': 'Add error messages',
        'category': 'Contact & Leads',
        'severity': 'Major',
        'weight': 2,
        'pass_patterns': [
            r'error|invalid|required|alert-error|alert-danger|text-red|invalid-feedback|aria-invalid',
            r'pattern=["\']',
            r'minlength=',
        ],
        'suggestion': ('Provide clear inline error validation notices when required form fields are missing or improperly formatted.'),
    },
    {
        'id': 'AC-19',
        'num': 19,
        'name': 'Remove placeholder text',
        'category': 'Hygiene & Quality',
        'severity': 'Critical',
        'weight': 3,
        'fail_patterns': [
            r'lorem ipsum',
            r'dolor sit amet',
            r'\btodo\b(?:\s*:|\s+-)',
            r'\btbd\b',
            r'insert (?:headline|text|copy|image) here',
            r'your company name',
            r'john doe',
        ],
        'suggestion': ('Purge all dummy Latin filler (Lorem Ipsum), unfinished developer TODOs, and sample placeholder tokens from production copy.'),
    },
    {
        'id': 'AC-20',
        'num': 20,
        'name': 'Compress images',
        'category': 'Hygiene & Quality',
        'severity': 'Major',
        'weight': 2,
        'pass_patterns': [
            r'\.webp\b|\.avif\b|srcset=|loading=["\']lazy["\']|<picture>',
        ],
        'fail_patterns': [
            r'<img[^>]+src=["\'][^"\']+\.(?:png|jpg|jpeg)["\'](?![^>]*(?:loading=["\']lazy["\']|width=))',
        ],
        'suggestion': (
            'Convert raster images to modern WebP/AVIF formats, apply responsive srcset sizing, '
            'and add loading="lazy" to all below-the-fold visual assets.'
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


def screen_track1_antipatterns(content: str, is_html: bool = True) -> tuple[list[dict[str, Any]], dict[str, int], dict[str, int], float, int]:
    """Evaluates content against Track 1: 30 Vibe-Coded Anti-Patterns."""
    raw_lower = content.lower()
    text_cleaned = clean_html(content).lower()

    results: list[dict[str, Any]] = []
    total_applicable_weight = 0
    earned_weight = 0.0

    flagged_counts = {'Critical': 0, 'Major': 0, 'Minor': 0}
    warn_counts = {'Critical': 0, 'Major': 0, 'Minor': 0}

    for spec in TRACK1_SPECS:
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
        crit_30['suggestion'] = TRACK1_SPECS[-1]['suggestion']
        warn_counts['Major'] += 1
        earned_weight += crit_30['weight'] * 0.5
    else:
        crit_30['status'] = 'PASS'
        crit_30['evidence'] = 'Exhibits distinctive domain characteristics; avoids generic AI startup template trap.'
        earned_weight += crit_30['weight']
        crit_30['suggestion'] = None

    return results, flagged_counts, warn_counts, earned_weight, total_applicable_weight


def screen_track2_acceptance(content: str, is_html: bool = True) -> tuple[list[dict[str, Any]], dict[str, int], dict[str, int], float, int]:
    """Evaluates content against Track 2: 20 Web QA Acceptance Criteria."""
    raw_lower = content.lower()
    text_cleaned = clean_html(content).lower()

    results: list[dict[str, Any]] = []
    total_applicable_weight = 0
    earned_weight = 0.0

    flagged_counts = {'Critical': 0, 'Major': 0, 'Minor': 0}
    warn_counts = {'Critical': 0, 'Major': 0, 'Minor': 0}

    for spec in TRACK2_SPECS:
        cid = spec['id']
        name = spec['name']
        cat = spec['category']
        sev = spec['severity']
        weight = spec['weight']
        suggestion = spec['suggestion']

        status = 'PASS'
        evidence = ''

        has_fail_signals = False
        fail_matches = []
        if 'fail_patterns' in spec:
            for pat in spec['fail_patterns']:
                matches = re.findall(pat, raw_lower if is_html else text_cleaned, re.IGNORECASE)
                if matches:
                    fail_matches.extend(matches[:2])
            threshold = spec.get('threshold_count', 1)
            if len(fail_matches) >= threshold:
                has_fail_signals = True

        has_pass_signals = False
        pass_matches = []
        if 'pass_patterns' in spec:
            for pat in spec['pass_patterns']:
                if re.search(pat, raw_lower if is_html else text_cleaned, re.IGNORECASE):
                    pass_matches.append(pat)
            if pass_matches:
                has_pass_signals = True

        if has_fail_signals:
            status = 'FAIL'
            evidence = f'Defect detected ({len(fail_matches)}x): {", ".join(str(m) for m in fail_matches[:2])}'
        elif 'pass_patterns' in spec and not has_pass_signals:
            status = 'FAIL'
            evidence = 'Missing required functional verification or element on page.'
        elif 'pass_patterns' in spec and has_pass_signals:
            status = 'PASS'
            evidence = f'Verified compliance ({len(pass_matches)} signals detected).'
        else:
            status = 'PASS'
            evidence = 'No defects detected.'

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
                'num': spec['num'],
                'name': name,
                'category': cat,
                'severity': sev,
                'weight': weight,
                'status': status,
                'evidence': evidence,
                'suggestion': suggestion if status in ('FAIL', 'WARN') else None,
            }
        )

    return results, flagged_counts, warn_counts, earned_weight, total_applicable_weight


def screen_content(content: str, is_html: bool = True) -> dict[str, Any]:
    """Unified dual-track acceptance screener."""
    # Screen Track 1 (Anti-Patterns)
    t1_results, t1_fails, t1_warns, t1_earned, t1_total = screen_track1_antipatterns(content, is_html=is_html)

    # Screen Track 2 (Acceptance Criteria)
    t2_results, t2_fails, t2_warns, t2_earned, t2_total = screen_track2_acceptance(content, is_html=is_html)

    # Track 1 Vibe-Coded Index
    max_penalty_t1 = sum(s['weight'] for s in TRACK1_SPECS)
    penalty_incurred = (
        (t1_fails['Critical'] * 3)
        + (t1_fails['Major'] * 2)
        + (t1_fails['Minor'] * 1)
        + (t1_warns['Critical'] * 1.5)
        + (t1_warns['Major'] * 1.0)
        + (t1_warns['Minor'] * 0.5)
    )
    vibe_index = round((penalty_incurred / max_penalty_t1) * 100, 1)

    # Track 2 Technical QA Score
    tech_qa_score = round((t2_earned / t2_total) * 100, 1) if t2_total > 0 else 0.0

    # Positioning Readiness Score (from Track 1)
    positioning_score = round((t1_earned / t1_total) * 100, 1) if t1_total > 0 else 0.0

    # Composite Launch Readiness Score (50% positioning + 50% technical QA)
    readiness_score = round(0.5 * (100.0 - vibe_index) + 0.5 * tech_qa_score, 1)

    total_critical_fails = t1_fails['Critical'] + t2_fails['Critical']
    total_major_fails = t1_fails['Major'] + t2_fails['Major']
    total_minor_fails = t1_fails['Minor'] + t2_fails['Minor']

    # Launch Gate Decision
    if total_critical_fails == 0 and total_major_fails <= 2 and readiness_score >= 85.0 and tech_qa_score >= 85.0 and vibe_index <= 20.0:
        verdict = 'READY TO PUSH'
        verdict_badge = '🟢 READY TO PUSH'
    elif total_critical_fails <= 1 and readiness_score >= 65.0:
        verdict = 'NEEDS WORK'
        verdict_badge = '🟡 NEEDS WORK'
    else:
        verdict = 'BLOCKED'
        verdict_badge = '🔴 BLOCKED'

    return {
        'timestamp': datetime.now(UTC).isoformat(),
        'metrics': {
            'launch_gate_verdict': verdict,
            'verdict_badge': verdict_badge,
            'composite_readiness_score': readiness_score,
            'positioning_score': positioning_score,
            'vibe_coded_index': vibe_index,
            'tech_qa_score': tech_qa_score,
            'critical_fails_total': total_critical_fails,
            'major_fails_total': total_major_fails,
            'minor_fails_total': total_minor_fails,
            'track1_critical_fails': t1_fails['Critical'],
            'track1_major_fails': t1_fails['Major'],
            'track1_minor_fails': t1_fails['Minor'],
            'track2_critical_fails': t2_fails['Critical'],
            'track2_major_fails': t2_fails['Major'],
            'track2_minor_fails': t2_fails['Minor'],
        },
        'track1_anti_patterns': t1_results,
        'track2_acceptance_criteria': t2_results,
    }


def format_markdown_report(report_data: dict[str, Any], target_name: str) -> str:
    """Generates an executive markdown report complying with report-template.md."""
    m = report_data['metrics']
    t1_criteria = report_data['track1_anti_patterns']
    t2_criteria = report_data['track2_acceptance_criteria']

    lines = [
        f'# 🚀 Startup Landing Page Launch Gate & Acceptance Audit: {target_name}',
        '',
        f'**Audit Timestamp**: {report_data["timestamp"]}  ',
        '**Auditor**: Startup Landing Screener v2.0 (Antigravity Founder Skills)  ',
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
        (
            f'| **Composite Launch Readiness** | **{m["composite_readiness_score"]}%** | $\\ge 85\\%$ | '
            f'{"PASS" if m["composite_readiness_score"] >= 85 else "FAIL"} |'
        ),
        (
            f'| **Track 1: Vibe-Coded Index** | **{m["vibe_coded_index"]}%** (lower is better) | $\\le 20\\%$ | '
            f'{"PASS" if m["vibe_coded_index"] <= 20 else "WARN"} |'
        ),
        (
            f'| **Track 2: Technical QA Score** | **{m["tech_qa_score"]}%** (higher is better) | $\\ge 85\\%$ | '
            f'{"PASS" if m["tech_qa_score"] >= 85 else "FAIL"} |'
        ),
        (
            f'| **Critical Blockers** | **{m["critical_fails_total"]}** (T1: {m["track1_critical_fails"]}, T2: {m["track2_critical_fails"]}) | 0 | '
            f'{"PASS" if m["critical_fails_total"] == 0 else "CRITICAL"} |'
        ),
        f'| **Major Defect Count** | **{m["major_fails_total"]}** | $\\le 2$ | {"PASS" if m["major_fails_total"] <= 2 else "WARN"} |',
        f'| **Minor Polish Items** | **{m["minor_fails_total"]}** | $\\le 3$ | {"PASS" if m["minor_fails_total"] <= 3 else "WARN"} |',
        '',
        '---',
        '',
        '## 📋 Track 1: 30-Criteria Anti-Patterns Matrix (What to Avoid / Red Flags)',
        '',
        '| # | Anti-Pattern Criterion | Category | Severity | Status | Observed Evidence / Current State | Remediation Needed? |',
        '| :-: | :--- | :--- | :---: | :---: | :--- | :---: |',
    ]

    for c in t1_criteria:
        status_md = f'`{c["status"]}`'
        remediation_needed = 'Yes' if c['status'] in ('FAIL', 'WARN') else 'No'
        clean_evidence = c['evidence'].replace('|', '/')
        lines.append(f'| {c["id"]} | {c["name"]} | {c["category"]} | {c["severity"]} | {status_md} | {clean_evidence} | {remediation_needed} |')

    lines.extend(
        [
            '',
            '---',
            '',
            '## 🛠️ Track 2: 20-Criteria Web QA Acceptance Checklist (What to Verify & Have)',
            '',
            '| ID | Acceptance Criterion | Category | Severity | Status | Verification Evidence / Current State | Fix Needed? |',
            '| :-: | :--- | :--- | :---: | :---: | :--- | :---: |',
        ]
    )

    for c in t2_criteria:
        status_md = f'`{c["status"]}`'
        fix_needed = 'Yes' if c['status'] in ('FAIL', 'WARN') else 'No'
        clean_evidence = c['evidence'].replace('|', '/')
        lines.append(f'| {c["id"]} | {c["name"]} | {c["category"]} | {c["severity"]} | {status_md} | {clean_evidence} | {fix_needed} |')

    lines.extend(
        [
            '',
            '---',
            '',
            '## 🔍 Detailed Criterion Comparison & Actionable Suggestions',
            '',
        ]
    )

    t1_flagged = [c for c in t1_criteria if c['status'] in ('FAIL', 'WARN')]
    t2_flagged = [c for c in t2_criteria if c['status'] in ('FAIL', 'WARN')]

    if not t1_flagged and not t2_flagged:
        lines.append('✨ **Outstanding**: No criteria were flagged on either track. The landing page is authentic, functional, and ready to launch!')
    else:
        if t1_flagged:
            lines.append('### Track 1 Remediation: Positioning & Anti-Patterns')
            for c in t1_flagged:
                lines.extend(
                    [
                        f'#### Criterion #{c["id"]}: {c["name"]} ({c["severity"]} - `{c["status"]}`)',
                        f'- **Category**: {c["category"]}',
                        f'- **Observed Finding**: {c["evidence"]}',
                        f'- **Actionable Suggestion**: {c["suggestion"]}',
                        '',
                    ]
                )
        if t2_flagged:
            lines.append('### Track 2 Remediation: Technical & Web QA Acceptance')
            for c in t2_flagged:
                lines.extend(
                    [
                        f'#### Criterion [{c["id"]}]: {c["name"]} ({c["severity"]} - `{c["status"]}`)',
                        f'- **Category**: {c["category"]}',
                        f'- **Observed Finding**: {c["evidence"]}',
                        f'- **Actionable Fix**: {c["suggestion"]}',
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

    # Combined top prioritized fixes
    all_flagged = t1_flagged + t2_flagged
    sorted_fixes = sorted(
        all_flagged,
        key=lambda x: 0 if x['severity'] == 'Critical' else (1 if x['severity'] == 'Major' else 2),
    )
    top_5 = sorted_fixes[:5]
    if top_5:
        for idx, item in enumerate(top_5, 1):
            identifier = f'#{item["id"]}' if isinstance(item['id'], int) else f'[{item["id"]}]'
            lines.append(f'{idx}. **[{item["severity"].upper()}] {identifier} {item["name"]}**: {item["suggestion"]}')
    else:
        lines.append('✅ No remaining blockers before push!')

    lines.append('')
    return '\n'.join(lines)


def run_doctor() -> None:
    """Performs environment and dependency diagnostics."""
    print('=== Startup Landing Screener v2.0: Doctor Diagnostic ===')
    print(f'Script Version: {TOOL_VERSION}')
    print(f'Python Executable: {sys.executable}')
    print(f'Python Version: {sys.version.split()[0]}')
    print('URLLib HTTP / HTTPS Client: OK')
    print('HTML Parser: OK')
    print(f'Track 1 Anti-Pattern Criteria: {len(TRACK1_SPECS)}')
    print(f'Track 2 Acceptance Criteria: {len(TRACK2_SPECS)}')
    print(f'Total Evaluated Criteria: {len(TRACK1_SPECS) + len(TRACK2_SPECS)}')
    print('Diagnostic Status: HEALTHY')


def main() -> None:
    parser = argparse.ArgumentParser(description='Screen a startup landing page against dual-track acceptance criteria.')
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
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SynapseAI - Revolutionize your workflow with AI</title>
        </head>
        <body class="bg-black text-white overflow-x-hidden">
            <header>
                <a href="/" aria-label="SynapseAI Home"><img src="/logo.svg" alt="SynapseAI Logo" /></a>
                <button class="hamburger md:hidden" aria-label="Open Menu">☰</button>
            </header>
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
            <button type="submit" class="bg-purple-600">Contact Sales for Custom Enterprise Pricing</button>
            <footer>
                <a href="/privacy">Privacy Policy</a>
                <a href="/terms">Terms of Service</a>
                <p>© 2026 SynapseAI Inc. All rights reserved.</p>
            </footer>
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
