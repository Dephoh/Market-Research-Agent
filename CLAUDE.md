# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a market research workspace for producing academic-quality market analysis reports using a multi-agent pipeline. Research projects produce structured deliverables in a dedicated project folder.

## Primary Command

```
/market-research <topic or description>
```

This launches the full research pipeline. The topic can be a simple name ("aquaculture robotics") or a longer description—the system will derive a filesystem-friendly project name.

## Pipeline Architecture

```
/market-research {topic}
        │
        ▼
┌─── PHASE 1: RESEARCH (parallel) ───┐
│  market-sizer                      │
│  competitor-mapper                 │──▶ {project}/raw_research/
│  customer-researcher               │
│  trend-scanner                     │
└────────────────────────────────────┘
        │
        ▼
   research-validator (quality gate)
        │
        ▼
┌─── PHASE 2: ANALYSIS (parallel) ───┐
│  opportunity-analyst               │
│  competitive-analyst               │──▶ {project}/analysis/
│  data-synthesizer                  │
└────────────────────────────────────┘
        │
        ▼
   [user checkpoint]
        │
        ▼
┌─── PHASE 3: REPORT (sequential) ───┐
│  report-architect ──▶ outline.md   │
│         │                          │──▶ {project}/report/
│  latex-writer ──▶ .tex + .bib      │
└────────────────────────────────────┘
        │
        ▼
   pdflatex/bibtex compilation
        │
        ▼
┌─── PDF VALIDATION (iterative) ────┐
│  model reviews PDF for:           │
│  - table readability              │
│  - paragraph spacing              │
│  - professional formatting        │
│  ↺ fix & recompile if needed      │
└───────────────────────────────────┘
        │
        ▼
      📄 PDF (validated)
```

## Agent Inventory

| Agent | Purpose |
|-------|---------|
| market-sizer | TAM/SAM/SOM, growth projections, segment analysis |
| competitor-mapper | Player profiles, funding, positioning, M&A |
| customer-researcher | Pain points, buyer personas, willingness to pay |
| trend-scanner | Technology shifts, regulatory changes, investment patterns |
| research-validator | Quality gate checking sources and completeness |
| opportunity-analyst | Cross-references data to identify and rank opportunities |
| competitive-analyst | Strategic white space and competitive dynamics |
| data-synthesizer | Consolidates all quantitative data with reconciliation |
| report-architect | Designs report structure and content flow |
| latex-writer | Produces professional LaTeX document and BibTeX |

## Project Structure

Each research project creates:
```
{project_name}/
├── raw_research/
│   ├── market_sizing.md
│   ├── competitors.md
│   ├── customer_insights.md
│   ├── trends.md
│   └── _validation.md
├── analysis/
│   ├── opportunities.md
│   ├── competitive_dynamics.md
│   └── key_statistics.md
└── report/
    ├── outline.md
    ├── {project_name}_market_report.tex
    ├── {project_name}_references.bib
    └── {project_name}_market_report.pdf
```

## Build Commands

Compile a LaTeX report manually:
```bash
cd {project}/report
pdflatex {project}_market_report.tex
bibtex {project}_market_report
pdflatex {project}_market_report.tex
pdflatex {project}_market_report.tex
```

## Research Quality Standards

- Claims require multiple independent sources; single-source claims are hypotheses
- Market sizes must include methodology and source attribution
- Competitor analysis needs specific names, capabilities, and pricing data
- Include confidence levels (High/Medium/Low) for key claims
- Minimum 5 unique source URLs per research file
