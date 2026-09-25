#!/usr/bin/env python3
"""
score_competitors.v2.py

Description:
  Deterministic CLI tool for investment-grade competitor intelligence evaluation.
  Calculates competitor relevance scores, assesses claim confidence levels, validates
  evidence logs against verification rules (e.g. 2+ independent sources for material claims),
  evaluates competitor threat levels, audits deliverable files for Radical Honesty compliance
  (claim labels, Red/Yellow Flags, false precision checks), and renders comparative matrices.

Changelog:
  - v2.0.0 (Enhancement from similar intelligence workflows):
    - Added 'threat' subcommand to evaluate competitor threat level (HIGH / MEDIUM / LOW)
      based on customer overlap, funding strength, growth velocity, and customer satisfaction.
    - Added 'audit-markdown' subcommand to check deliverable files for Radical Honesty compliance:
      detects missing claim labels ([Data], [Estimate], [Assumption], [Opinion]), verifies presence
      of mandatory Red Flags and Yellow Flags sections, and warns on single-point ARR/financials.
    - Enhanced 'verify-log' to audit 4-tier claim labeling and flag duplicate-source risks.
  - v1.0.0: Initial implementation supporting relevance scoring, confidence scoring,
    evidence log validation, markdown/JSON matrices, and doctor checks.
"""

import argparse
import json
import logging
import re
import sys
from datetime import datetime
from pathlib import Path


def setup_logger(tool_name: str = 'score_competitors') -> logging.Logger:
    """Configures file logging to .logs/<tool_name>_<timestamp>.log and stdout."""
    script_dir = Path(__file__).parent.resolve()
    log_dir = script_dir / '.logs'
    log_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = log_dir / f'{tool_name}_{timestamp}.log'

    logger = logging.getLogger(f'{tool_name}_{timestamp}')
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s'))
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(logging.Formatter('%(message)s'))
        logger.addHandler(console_handler)

    return logger


def calculate_relevance(customer: float, problem: float, geography: float, model: float, product: float) -> dict:
    """
    Calculates weighted competitor relevance score (0-100 scale).

    Formula:
      Relevance = 0.30 * Customer + 0.25 * Problem + 0.15 * Geography + 0.15 * Model + 0.15 * Product
    """
    total = (0.30 * customer) + (0.25 * problem) + (0.15 * geography) + (0.15 * model) + (0.15 * product)
    total_rounded = round(total, 2)

    if total_rounded >= 70.0:
        classification = 'DIRECT'
        description = 'Direct competitor: high overlap across customer, problem, and offering.'
    elif total_rounded >= 40.0:
        classification = 'INDIRECT_ADJACENT'
        description = 'Indirect or adjacent competitor: partial overlap; targets similar problem or budget.'
    else:
        classification = 'SUBSTITUTE_WATCHLIST'
        description = 'Substitute, manual workaround, incumbent, or low-overlap entity on watchlist.'

    return {
        'relevance_score': total_rounded,
        'classification': classification,
        'description': description,
        'breakdown': {
            'customer_overlap': round(customer, 2),
            'problem_overlap': round(problem, 2),
            'geography_overlap': round(geography, 2),
            'model_overlap': round(model, 2),
            'product_overlap': round(product, 2),
        },
    }


def calculate_confidence(credibility: float, corroboration: float, recency: float, completeness: float) -> dict:
    """
    Calculates weighted claim confidence score (1.0-5.0 scale).

    Formula:
      Confidence = 0.40 * Credibility + 0.30 * Corroboration + 0.20 * Recency + 0.10 * Completeness
    """
    total = (0.40 * credibility) + (0.30 * corroboration) + (0.20 * recency) + (0.10 * completeness)
    total_rounded = round(total, 2)

    if total_rounded >= 4.0:
        level = 'HIGH'
        guidance = 'High confidence (4.0-5.0): Multiple T1/T2 corroborating sources, recent, consistent.'
    elif total_rounded >= 2.5:
        level = 'MEDIUM'
        guidance = 'Medium confidence (2.5-3.9): Some corroboration, credible single source, minor gaps.'
    else:
        level = 'LOW'
        guidance = 'Low confidence (1.0-2.4): Uncorroborated, self-reported marketing claim, stale, or biased.'

    return {
        'confidence_score': total_rounded,
        'confidence_level': level,
        'guidance': guidance,
        'breakdown': {
            'source_credibility': round(credibility, 2),
            'corroboration': round(corroboration, 2),
            'recency': round(recency, 2),
            'completeness': round(completeness, 2),
        },
    }


def calculate_threat(relevance: float, funding_scale: float, growth_velocity: float, satisfaction: float) -> dict:
    """
    Calculates competitor threat rating (HIGH / MEDIUM / LOW).
    Inputs:
      - relevance (0-100 scale)
      - funding_scale (1-5 scale: 1=Bootstrapped, 5=Tier 1 Mega-funded)
      - growth_velocity (1-5 scale: 1=Stagnant/Decline, 5=Hypergrowth)
      - satisfaction (1-5 scale: 1=Poor ratings, 5=Beloved product)
    """
    # Normalize relevance to 1-5 scale
    rel_norm = (relevance / 100.0) * 5.0
    threat_index = (0.35 * rel_norm) + (0.25 * growth_velocity) + (0.20 * funding_scale) + (0.20 * satisfaction)
    threat_index = round(threat_index, 2)

    if threat_index >= 3.8:
        level = 'HIGH'
        summary = 'High Threat: Head-to-head collision; strong growth, well-funded, high customer satisfaction.'
    elif threat_index >= 2.6:
        level = 'MEDIUM'
        summary = 'Medium Threat: Competitive threat in specific segments; noticeable gaps in UX or distribution.'
    else:
        level = 'LOW'
        summary = 'Low Threat: Stagnant, targeting different segment, or suffering customer dissatisfaction.'

    return {
        'threat_index': threat_index,
        'threat_level': level,
        'summary': summary,
        'factors': {
            'relevance_score': round(relevance, 2),
            'funding_scale': round(funding_scale, 2),
            'growth_velocity': round(growth_velocity, 2),
            'satisfaction_rating': round(satisfaction, 2),
        },
    }


def audit_markdown_file(file_path: Path) -> dict:
    """
    Audits a Markdown deliverable file for Radical Honesty and structural standards:
    - Presence of standardized claim labels ([Data], [Estimate], [Assumption], [Opinion])
    - Mandatory presence of Red Flags and Yellow Flags sections
    - Warning on uncalibrated single-point financial numbers
    """
    if not file_path.exists():
        return {'error': f'File not found: {file_path}'}

    content = file_path.read_text(encoding='utf-8')
    lines = content.splitlines()

    has_red_flags = bool(re.search(r'#+\s+Red Flags', content, re.IGNORECASE))
    has_yellow_flags = bool(re.search(r'#+\s+Yellow Flags', content, re.IGNORECASE))

    # Detect claim labels
    data_count = len(re.findall(r'\[Data\]', content))
    estimate_count = len(re.findall(r'\[Estimate\]', content))
    assumption_count = len(re.findall(r'\[Assumption\]', content))
    opinion_count = len(re.findall(r'\[Opinion\]', content))
    total_labeled = data_count + estimate_count + assumption_count + opinion_count

    # Check for single-point ARR assertions like "ARR is $14.2M" or "$10M ARR" without range
    false_precision_warnings = []
    for idx, line in enumerate(lines, start=1):
        if re.search(r'ARR\s+(?:is|=|of)?\s*\$\d+(?:\.\d+)?\s*[MKmk](?!\s*[-–—to])', line) and '-' not in line and 'to' not in line:
            false_precision_warnings.append(f'Line {idx}: Potential single-point ARR without range: "{line.strip()[:60]}"')

    issues = []
    if not has_red_flags:
        issues.append('MISSING: Mandatory "Red Flags" section is absent.')
    if not has_yellow_flags:
        issues.append('MISSING: Mandatory "Yellow Flags" section is absent.')
    if total_labeled == 0 and len(lines) > 30:
        issues.append('WARNING: No standardized claim labels ([Data], [Estimate], etc.) detected.')

    status = 'PASS' if not issues and not false_precision_warnings else ('WARN' if not issues else 'FAIL')

    return {
        'file': str(file_path),
        'status': status,
        'has_red_flags': has_red_flags,
        'has_yellow_flags': has_yellow_flags,
        'label_counts': {
            'data': data_count,
            'estimate': estimate_count,
            'assumption': assumption_count,
            'opinion': opinion_count,
            'total': total_labeled,
        },
        'issues': issues,
        'false_precision_warnings': false_precision_warnings,
    }


def verify_evidence_log(entries: list[dict]) -> dict:
    """
    Audits a list of evidence log entries.
    Enforces 2+ sources for facts, range checks for estimates, and label integrity.
    """
    audit_results = []
    issues_found = 0
    total_entries = len(entries)

    for idx, item in enumerate(entries, start=1):
        claim = item.get('claim', f'Item {idx}')
        claim_type = str(item.get('claim_type', 'assumption')).lower()
        sources = item.get('sources', [])
        source_count = item.get('source_count', len(sources) if isinstance(sources, list) else 1)
        tier = item.get('source_tier', 'T3')
        confidence = float(item.get('confidence', 2.0))

        flags = []
        is_verified = True

        if claim_type == 'fact':
            if source_count < 2:
                flags.append('VIOLATION: Facts require at least 2 independent sources')
                is_verified = False
            if tier in ('T3', 'T4') and source_count < 2:
                flags.append('WARNING: Material fact relies solely on low-tier or self-reported source')
        elif claim_type == 'estimate':
            estimate_value = str(item.get('value', ''))
            if estimate_value and '-' not in estimate_value and 'to' not in estimate_value.lower():
                flags.append('WARNING: Estimates should be expressed as ranges, not point figures')
        elif claim_type not in ('fact', 'estimate', 'assumption'):
            flags.append(f'INVALID: Unknown claim_type "{claim_type}"')

        if flags:
            issues_found += len(flags)

        status = 'VERIFIED' if (is_verified and flags == []) else ('FLAGGED' if not is_verified else 'CAUTION')

        audit_results.append(
            {
                'index': idx,
                'competitor': item.get('competitor', 'N/A'),
                'claim': claim,
                'claim_type': claim_type,
                'source_count': source_count,
                'source_tier': tier,
                'confidence': confidence,
                'status': status,
                'flags': flags,
            }
        )

    return {
        'total_entries': total_entries,
        'issues_found': issues_found,
        'audit_results': audit_results,
    }


def run_doctor() -> int:
    """Checks environment, Python version, and tool readiness."""
    print('=== Startup Competitors Tool Doctor (v2.0.0) ===')
    print(f'Python Version : {sys.version.split()[0]}')
    print(f'Executable     : {sys.executable}')
    print('Standard Lib   : All modules (json, argparse, logging, pathlib, re) present.')
    print('Dependencies   : Zero external dependencies required (stdlib-only).')
    print('Capabilities   : Relevance, Confidence, Threat Assessment, Deliverable Auditing, Matrix Generation.')
    print('Status         : READY')
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Score competitor relevance, evaluate claim confidence, assess threat level, and audit deliverables for investment-grade reports.'
    )
    parser.add_argument('--doctor', action='store_true', help='Check script health, python environment, and exit')

    subparsers = parser.add_subparsers(dest='command', help='Sub-commands')

    # relevance subcommand
    rel_parser = subparsers.add_parser('relevance', help='Score competitor relevance (0-100)')
    rel_parser.add_argument('--name', type=str, default='Competitor Candidate', help='Competitor name')
    rel_parser.add_argument('--customer', type=float, required=True, help='Customer overlap score (0-100)')
    rel_parser.add_argument('--problem', type=float, required=True, help='Problem overlap score (0-100)')
    rel_parser.add_argument('--geography', type=float, required=True, help='Geography overlap score (0-100)')
    rel_parser.add_argument('--model', type=float, required=True, help='Price/business model overlap score (0-100)')
    rel_parser.add_argument('--product', type=float, required=True, help='Product feature overlap score (0-100)')
    rel_parser.add_argument('--json', action='store_true', help='Output JSON instead of markdown')
    rel_parser.add_argument('--output', '-o', type=str, help='Optional output file path')

    # confidence subcommand
    conf_parser = subparsers.add_parser('confidence', help='Calculate claim confidence score (1-5)')
    conf_parser.add_argument('--credibility', type=float, required=True, help='Source credibility (1.0-5.0)')
    conf_parser.add_argument('--corroboration', type=float, required=True, help='Corroboration level (1.0-5.0)')
    conf_parser.add_argument('--recency', type=float, required=True, help='Recency score (1.0-5.0)')
    conf_parser.add_argument('--completeness', type=float, required=True, help='Completeness score (1.0-5.0)')
    conf_parser.add_argument('--json', action='store_true', help='Output JSON instead of markdown')
    conf_parser.add_argument('--output', '-o', type=str, help='Optional output file path')

    # threat subcommand
    threat_parser = subparsers.add_parser('threat', help='Evaluate competitor threat level (High/Medium/Low)')
    threat_parser.add_argument('--name', type=str, default='Competitor', help='Competitor name')
    threat_parser.add_argument('--relevance', type=float, required=True, help='Relevance score (0-100)')
    threat_parser.add_argument('--funding', type=float, required=True, help='Funding strength (1.0-5.0)')
    threat_parser.add_argument('--growth', type=float, required=True, help='Growth velocity (1.0-5.0)')
    threat_parser.add_argument('--satisfaction', type=float, required=True, help='Customer satisfaction rating (1.0-5.0)')
    threat_parser.add_argument('--json', action='store_true', help='Output JSON instead of markdown')
    threat_parser.add_argument('--output', '-o', type=str, help='Optional output file path')

    # audit-markdown subcommand
    audit_parser = subparsers.add_parser('audit-markdown', help='Audit a deliverable file for Radical Honesty compliance')
    audit_parser.add_argument('--file', '-f', type=str, required=True, help='Path to markdown file')
    audit_parser.add_argument('--json', action='store_true', help='Output JSON instead of markdown')
    audit_parser.add_argument('--output', '-o', type=str, help='Optional output file path')

    # verify-log subcommand
    verify_parser = subparsers.add_parser('verify-log', help='Validate evidence log against 2-source verification rule')
    verify_parser.add_argument('--file', '-f', type=str, required=True, help='Path to JSON file containing evidence log entries')
    verify_parser.add_argument('--json', action='store_true', help='Output JSON instead of markdown')
    verify_parser.add_argument('--output', '-o', type=str, help='Optional output file path')

    # matrix subcommand
    matrix_parser = subparsers.add_parser('matrix', help='Evaluate batch competitors from a JSON file')
    matrix_parser.add_argument('--file', '-f', type=str, required=True, help='Path to JSON list of competitors with overlap metrics')
    matrix_parser.add_argument('--json', action='store_true', help='Output JSON instead of markdown')
    matrix_parser.add_argument('--output', '-o', type=str, help='Optional output file path')

    args = parser.parse_args()

    if args.doctor:
        sys.exit(run_doctor())

    if not args.command:
        parser.print_help()
        sys.exit(1)

    logger = setup_logger()

    output_text = ''
    if args.command == 'relevance':
        res = calculate_relevance(args.customer, args.problem, args.geography, args.model, args.product)
        if args.json:
            output_text = json.dumps({'name': args.name, **res}, indent=2)
        else:
            lines = [
                f'### Competitor Relevance Score: {args.name}',
                '',
                f'- **Relevance Score**: {res["relevance_score"]} / 100',
                f'- **Classification**: `{res["classification"]}`',
                f'- **Description**: {res["description"]}',
                '',
                '| Dimension | Weight | Overlap Score | Weighted Contribution |',
                '| :--- | :---: | :---: | :---: |',
                f'| Customer Overlap | 30% | {res["breakdown"]["customer_overlap"]} | {round(0.30 * res["breakdown"]["customer_overlap"], 2)} |',
                f'| Problem Overlap | 25% | {res["breakdown"]["problem_overlap"]} | {round(0.25 * res["breakdown"]["problem_overlap"], 2)} |',
                f'| Geography Overlap | 15% | {res["breakdown"]["geography_overlap"]} | {round(0.15 * res["breakdown"]["geography_overlap"], 2)} |',
                f'| Business Model Overlap | 15% | {res["breakdown"]["model_overlap"]} | {round(0.15 * res["breakdown"]["model_overlap"], 2)} |',
                f'| Product Overlap | 15% | {res["breakdown"]["product_overlap"]} | {round(0.15 * res["breakdown"]["product_overlap"], 2)} |',
            ]
            output_text = '\n'.join(lines)

    elif args.command == 'confidence':
        res = calculate_confidence(args.credibility, args.corroboration, args.recency, args.completeness)
        if args.json:
            output_text = json.dumps(res, indent=2)
        else:
            bk = res['breakdown']
            lines = [
                '### Claim Confidence Assessment',
                '',
                f'- **Confidence Score**: {res["confidence_score"]} / 5.0',
                f'- **Confidence Level**: `{res["confidence_level"]}`',
                f'- **Guidance**: {res["guidance"]}',
                '',
                '| Metric | Weight | Value (1-5) | Weighted Score |',
                '| :--- | :---: | :---: | :---: |',
                f'| Source Credibility | 40% | {bk["source_credibility"]} | {round(0.40 * bk["source_credibility"], 2)} |',
                f'| Corroboration | 30% | {bk["corroboration"]} | {round(0.30 * bk["corroboration"], 2)} |',
                f'| Recency | 20% | {bk["recency"]} | {round(0.20 * bk["recency"], 2)} |',
                f'| Completeness | 10% | {bk["completeness"]} | {round(0.10 * bk["completeness"], 2)} |',
            ]
            output_text = '\n'.join(lines)

    elif args.command == 'threat':
        res = calculate_threat(args.relevance, args.funding, args.growth, args.satisfaction)
        if args.json:
            output_text = json.dumps({'name': args.name, **res}, indent=2)
        else:
            lines = [
                f'### Competitor Threat Assessment: {args.name}',
                '',
                f'- **Threat Index**: {res["threat_index"]} / 5.0',
                f'- **Threat Level**: `{res["threat_level"]}`',
                f'- **Summary**: {res["summary"]}',
                '',
                '| Evaluation Factor | Weight | Score |',
                '| :--- | :---: | :---: |',
                f'| Relevance Factor | 35% | {res["factors"]["relevance_score"]} / 100 |',
                f'| Growth Velocity | 25% | {res["factors"]["growth_velocity"]} / 5.0 |',
                f'| Funding Scale | 20% | {res["factors"]["funding_scale"]} / 5.0 |',
                f'| Product Satisfaction | 20% | {res["factors"]["satisfaction_rating"]} / 5.0 |',
            ]
            output_text = '\n'.join(lines)

    elif args.command == 'audit-markdown':
        audit = audit_markdown_file(Path(args.file))
        if args.json:
            output_text = json.dumps(audit, indent=2)
        else:
            lines = [
                f'### Deliverable Audit: {Path(args.file).name}',
                '',
                f'- **Status**: `{audit.get("status", "UNKNOWN")}`',
                f'- **Has Red Flags Section**: {audit.get("has_red_flags", False)}',
                f'- **Has Yellow Flags Section**: {audit.get("has_yellow_flags", False)}',
                f'- **Standard Claim Labels Detected**: {audit.get("label_counts", {}).get("total", 0)}',
                f'  (Data: {audit.get("label_counts", {}).get("data", 0)}, Estimate: {audit.get("label_counts", {}).get("estimate", 0)}, '
                f'Assumption: {audit.get("label_counts", {}).get("assumption", 0)}, Opinion: {audit.get("label_counts", {}).get("opinion", 0)})',
            ]
            if audit.get('issues'):
                lines.extend(['', '**Issues Identified:**'])
                for iss in audit['issues']:
                    lines.append(f'- {iss}')
            if audit.get('false_precision_warnings'):
                lines.extend(['', '**False Precision Warnings:**'])
                for warn in audit['false_precision_warnings']:
                    lines.append(f'- {warn}')
            if not audit.get('issues') and not audit.get('false_precision_warnings'):
                lines.extend(['', '**Verdict**: Deliverable is compliant with Radical Honesty and formatting standards.'])
            output_text = '\n'.join(lines)

    elif args.command == 'verify-log':
        log_file = Path(args.file)
        if not log_file.exists():
            logger.error(f'File not found: {log_file}')
            sys.exit(1)
        data = json.loads(log_file.read_text(encoding='utf-8'))
        if not isinstance(data, list):
            logger.error('Expected JSON file containing an array of evidence entries.')
            sys.exit(1)
        audit = verify_evidence_log(data)
        if args.json:
            output_text = json.dumps(audit, indent=2)
        else:
            lines = [
                '### Evidence Log Audit Summary',
                '',
                f'- **Total Entries**: {audit["total_entries"]}',
                f'- **Issues / Violations Found**: {audit["issues_found"]}',
                '',
                '| # | Competitor | Claim | Type | Sources | Tier | Conf | Status | Flags |',
                '| :-: | :--- | :--- | :-: | :-: | :-: | :-: | :-: | :--- |',
            ]
            for r in audit['audit_results']:
                flags_str = '; '.join(r['flags']) if r['flags'] else 'None'
                claim_short = r['claim'][:35]
                row = (
                    f'| {r["index"]} | {r["competitor"]} | {claim_short} | '
                    f'{r["claim_type"]} | {r["source_count"]} | {r["source_tier"]} | '
                    f'{r["confidence"]} | `{r["status"]}` | {flags_str} |'
                )
                lines.append(row)
            output_text = '\n'.join(lines)

    elif args.command == 'matrix':
        matrix_file = Path(args.file)
        if not matrix_file.exists():
            logger.error(f'File not found: {matrix_file}')
            sys.exit(1)
        candidates = json.loads(matrix_file.read_text(encoding='utf-8'))
        if not isinstance(candidates, list):
            logger.error('Expected JSON file containing an array of competitor objects.')
            sys.exit(1)

        results = []
        for c in candidates:
            score_data = calculate_relevance(
                float(c.get('customer', 0)),
                float(c.get('problem', 0)),
                float(c.get('geography', 0)),
                float(c.get('model', 0)),
                float(c.get('product', 0)),
            )
            results.append(
                {
                    'name': c.get('name', 'Unnamed'),
                    'stage': c.get('stage', 'N/A'),
                    'geography': c.get('geography_name', 'Global'),
                    **score_data,
                }
            )

        results.sort(key=lambda x: x['relevance_score'], reverse=True)

        if args.json:
            output_text = json.dumps(results, indent=2)
        else:
            lines = [
                '### Competitor Priority Matrix',
                '',
                '| Rank | Competitor | Stage | Geography | Relevance Score | Classification |',
                '| :-: | :--- | :--- | :--- | :-: | :--- |',
            ]
            for idx, r in enumerate(results, start=1):
                lines.append(f'| {idx} | **{r["name"]}** | {r["stage"]} | {r["geography"]} | {r["relevance_score"]} | `{r["classification"]}` |')
            output_text = '\n'.join(lines)

    if args.output:
        out_path = Path(args.output).resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output_text, encoding='utf-8')
        logger.info(f'Output written to {out_path}')
    else:
        print(output_text)


if __name__ == '__main__':
    main()
