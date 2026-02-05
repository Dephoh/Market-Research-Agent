# Market Research Pipeline

A market research workspace for producing academic-quality market analysis reports using a multi-agent pipeline powered by Claude Code.

## Purpose

This repository provides an automated research pipeline that transforms a topic or market description into a comprehensive, professionally formatted PDF report. The system coordinates specialized AI agents to gather data, validate findings, perform analysis, and generate LaTeX-based deliverables.

## What's Included

### Claude Code Project Configuration

The repository includes a `CLAUDE.md` file that configures Claude Code with:

- **Custom Skill**: `/market-research <topic>` command that launches the full pipeline
- **10 Specialized Agents**: Each with defined roles and tool access
- **Quality Gates**: Validation checkpoints ensuring research integrity
- **Structured Output**: Consistent project folder organization

### Agent Pipeline

The pipeline runs in three phases:

| Phase | Agents | Output |
|-------|--------|--------|
| **Research** (parallel) | market-sizer, competitor-mapper, customer-researcher, trend-scanner | `raw_research/` |
| **Analysis** (parallel) | opportunity-analyst, competitive-analyst, data-synthesizer | `analysis/` |
| **Report** (sequential) | report-architect, latex-writer | `report/` with PDF |

### Agent Responsibilities

| Agent | Purpose |
|-------|---------|
| market-sizer | TAM/SAM/SOM, growth projections, segment analysis |
| competitor-mapper | Player profiles, funding, positioning, M&A activity |
| customer-researcher | Pain points, buyer personas, willingness to pay |
| trend-scanner | Technology shifts, regulatory changes, investment patterns |
| research-validator | Quality gate checking sources and completeness |
| opportunity-analyst | Cross-references data to identify and rank opportunities |
| competitive-analyst | Strategic white space and competitive dynamics |
| data-synthesizer | Consolidates quantitative data with reconciliation |
| report-architect | Designs report structure and content flow |
| latex-writer | Produces professional LaTeX document and BibTeX |

## Usage

```
/market-research <topic or description>
```

Examples:
- `/market-research aquaculture robotics`
- `/market-research AI-powered diagnostic tools for veterinary medicine`

## Output Structure

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

## Research Quality Standards

- Claims require multiple independent sources
- Market sizes include methodology and source attribution
- Competitor analysis includes specific names, capabilities, and pricing
- Key claims tagged with confidence levels (High/Medium/Low)
- Minimum 5 unique source URLs per research file

## Requirements

- Claude Code CLI
- LaTeX distribution (for PDF compilation)
  - `pdflatex`
  - `bibtex`
