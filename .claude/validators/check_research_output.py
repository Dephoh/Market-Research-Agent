#!/usr/bin/env python3
"""
Research output validator for market research pipeline.
Checks that research files meet minimum quality standards.
"""

import sys
import re
from pathlib import Path


def count_urls(content: str) -> int:
    """Count unique URLs in content."""
    urls = re.findall(r'https?://[^\s\)\]\>]+', content)
    return len(set(urls))


def check_required_sections(content: str, file_type: str) -> list[str]:
    """Check for required sections based on file type."""
    issues = []

    section_requirements = {
        'market_sizing': [
            'Executive Summary',
            'Market Size',
            'Growth',
            'Sources'
        ],
        'competitors': [
            'Executive Summary',
            'Tier 1',
            'Sources'
        ],
        'customer_insights': [
            'Executive Summary',
            'Pain Point',
            'Sources'
        ],
        'trends': [
            'Executive Summary',
            'Technology',
            'Sources'
        ],
        'opportunities': [
            'Executive Summary',
            'Opportunity',
            'Scoring'
        ],
        'competitive_dynamics': [
            'Executive Summary',
            'White Space',
            'Strategic'
        ],
        'key_statistics': [
            'Market Size Data',
            'Data Conflicts',
            'Quick Reference'
        ]
    }

    required = section_requirements.get(file_type, ['Executive Summary', 'Sources'])

    for section in required:
        if section.lower() not in content.lower():
            issues.append(f"Missing required section: {section}")

    return issues


def check_confidence_levels(content: str) -> bool:
    """Check if confidence levels are mentioned."""
    confidence_patterns = [
        r'confidence[:\s]*(high|medium|low)',
        r'(high|medium|low)\s*confidence',
        r'\*\*confidence\*\*'
    ]

    for pattern in confidence_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True
    return False


def check_data_attribution(content: str) -> list[str]:
    """Check that data points have sources."""
    issues = []

    # Find numbers that look like market data
    market_numbers = re.findall(r'\$[\d,]+\.?\d*\s*(billion|million|B|M)', content, re.IGNORECASE)

    # Check if there are sources nearby (rough heuristic)
    if len(market_numbers) > 3:
        source_count = len(re.findall(r'\[source|\(source|source:|according to', content, re.IGNORECASE))
        if source_count < len(market_numbers) // 2:
            issues.append("Many market figures found but few explicit source attributions")

    return issues


def validate_file(filepath: str) -> dict:
    """Validate a single research file."""
    path = Path(filepath)

    if not path.exists():
        return {
            'status': 'ERROR',
            'issues': [f'File not found: {filepath}']
        }

    content = path.read_text()

    # Determine file type from name
    file_type = path.stem.replace('_', ' ').lower()
    for known_type in ['market_sizing', 'competitors', 'customer_insights', 'trends',
                       'opportunities', 'competitive_dynamics', 'key_statistics']:
        if known_type.replace('_', '') in file_type.replace(' ', ''):
            file_type = known_type
            break

    issues = []
    warnings = []

    # Check minimum length
    word_count = len(content.split())
    if word_count < 200:
        issues.append(f"File too short ({word_count} words, minimum 200)")
    elif word_count < 500:
        warnings.append(f"File is brief ({word_count} words)")

    # Check URL count
    url_count = count_urls(content)
    if url_count < 3:
        issues.append(f"Only {url_count} sources found, need at least 3")
    elif url_count < 5:
        warnings.append(f"Only {url_count} sources, 5+ recommended")

    # Check required sections
    section_issues = check_required_sections(content, file_type)
    issues.extend(section_issues)

    # Check confidence levels (warning only)
    if not check_confidence_levels(content):
        warnings.append("No confidence level annotations found")

    # Check data attribution
    attribution_issues = check_data_attribution(content)
    warnings.extend(attribution_issues)

    # Check for placeholder content
    placeholders = re.findall(r'\[TODO\]|\[TBD\]|\[INSERT\]|\[PLACEHOLDER\]', content, re.IGNORECASE)
    if placeholders:
        issues.append(f"Found {len(placeholders)} placeholder(s)")

    # Determine status
    if issues:
        status = 'FAIL'
    elif warnings:
        status = 'WARN'
    else:
        status = 'PASS'

    return {
        'status': status,
        'issues': issues,
        'warnings': warnings,
        'stats': {
            'word_count': word_count,
            'url_count': url_count
        }
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: check_research_output.py <file_path> [file_path...]")
        sys.exit(1)

    all_passed = True

    for filepath in sys.argv[1:]:
        result = validate_file(filepath)

        print(f"\n{'='*60}")
        print(f"FILE: {filepath}")
        print(f"STATUS: {result['status']}")
        print(f"Stats: {result.get('stats', {})}")

        if result['issues']:
            print("\nBLOCKING ISSUES:")
            for issue in result['issues']:
                print(f"  - {issue}")
            all_passed = False

        if result.get('warnings'):
            print("\nWARNINGS:")
            for warning in result['warnings']:
                print(f"  - {warning}")

        if result['status'] == 'PASS':
            print("\n✓ Validation passed")

    print(f"\n{'='*60}")
    if all_passed:
        print("OVERALL: All files passed validation")
        sys.exit(0)
    else:
        print("OVERALL: Some files failed validation")
        sys.exit(1)


if __name__ == "__main__":
    main()
