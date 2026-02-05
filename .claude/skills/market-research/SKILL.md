---
name: market-research
description: "Run comprehensive market research pipeline with specialized agents. Usage: /market-research <topic or description>"
user_invocable: true
---

# Market Research Pipeline

You are orchestrating a comprehensive market research pipeline. The user has requested research on: **$ARGUMENTS**

## Step 1: Determine Project Name

First, determine a short, filesystem-friendly project name (lowercase, underscores, no spaces, max 30 chars).

- If the input is a simple topic like "aquaculture robotics" → use `aquaculture_robotics`
- If the input is a longer explanation → extract the core topic and shorten it

State the project name you'll use, then create the directory structure:

```
{project_name}/
  raw_research/
  analysis/
  report/
```

Use Bash to create these directories.

---

## Step 2: Primary Research Phase (PARALLEL)

Launch ALL FOUR of these agents simultaneously using multiple Task tool calls in a SINGLE message. This is critical for efficiency.

### Agent 1: market-sizer
```
Prompt: Research market size and growth projections for {topic}.

Your task:
1. Search for TAM (Total Addressable Market), SAM, and SOM estimates
2. Find projections from multiple research firms (note methodology differences)
3. Document: current market size, projected size, CAGR, segment breakdowns, geographic splits
4. Include source URLs for every data point
5. Rate confidence (High/Medium/Low) for each estimate based on source quality and corroboration

Write your findings in structured markdown to: {project_name}/raw_research/market_sizing.md

Required sections:
- ## Executive Summary
- ## Market Size Estimates (table format with Source, Value, Year, Methodology)
- ## Growth Projections
- ## Segment Breakdown
- ## Geographic Analysis
- ## Data Conflicts and Reconciliation
- ## Sources (with URLs)
```

### Agent 2: competitor-mapper
```
Prompt: Map the competitive landscape for {topic}.

Your task:
1. Identify players by tier: Tier 1 (established leaders), Tier 2 (growth-stage), Tier 3 (emerging/startups)
2. For each significant player document: company name, HQ location, founding year, funding raised, estimated revenue, key products/services, pricing if available, target customers, strengths, weaknesses
3. Identify recent M&A activity and partnerships
4. Note competitive dynamics: who is consolidating, who is disrupting

Write your findings in structured markdown to: {project_name}/raw_research/competitors.md

Required sections:
- ## Executive Summary
- ## Tier 1 Players (detailed profiles)
- ## Tier 2 Players (detailed profiles)
- ## Tier 3 / Emerging Players (brief profiles)
- ## Recent M&A and Partnerships
- ## Competitive Dynamics
- ## Sources (with URLs)
```

### Agent 3: customer-researcher
```
Prompt: Research customer pain points and unmet needs in {topic}.

Your task:
1. Search forums, Reddit, industry publications, reviews for customer complaints
2. Identify buyer personas (enterprise, SMB, consumer, geographic segments)
3. Document specific pain points with evidence (quotes, links)
4. Find "hair on fire" problems - urgent needs with inadequate solutions
5. Note willingness to pay signals and budget constraints mentioned

Write your findings in structured markdown to: {project_name}/raw_research/customer_insights.md

Required sections:
- ## Executive Summary
- ## Buyer Personas
- ## Primary Pain Points (ranked by frequency/severity)
- ## Unmet Needs by Segment
- ## Willingness to Pay Signals
- ## Verbatim Customer Quotes (with sources)
- ## Sources (with URLs)
```

### Agent 4: trend-scanner
```
Prompt: Research technology trends, regulatory changes, and market shifts affecting {topic}.

Your task:
1. Identify emerging technologies that could disrupt or enable the market
2. Find recent and upcoming regulatory changes
3. Track investment trends (VC funding patterns, corporate investment)
4. Note macroeconomic factors affecting the market
5. Identify potential black swan risks and tailwinds

Write your findings in structured markdown to: {project_name}/raw_research/trends.md

Required sections:
- ## Executive Summary
- ## Technology Trends (with timeline estimates)
- ## Regulatory Landscape (by geography)
- ## Investment Trends
- ## Macroeconomic Factors
- ## Risks and Tailwinds
- ## Sources (with URLs)
```

**WAIT for all four agents to complete before proceeding.**

---

## Step 3: Research Validation

Launch the research-validator agent:

```
Prompt: Validate the quality of research files in {project_name}/raw_research/

Read all .md files in the raw_research folder. For each file, check:
- [ ] Has required sections per the research type
- [ ] Claims are backed by sources (flag unsourced claims)
- [ ] Quantitative data includes methodology notes
- [ ] At least 5 unique source URLs
- [ ] Confidence levels are stated
- [ ] No obvious contradictions within the file

Cross-file validation:
- [ ] Market size estimates are consistent or conflicts are noted
- [ ] Competitor lists align with market segments discussed
- [ ] Customer pain points map to solutions competitors offer

Write validation report to: {project_name}/raw_research/_validation.md

Format:
## Validation Status: [PASSED/NEEDS_REVISION]

## File-by-File Assessment
[For each file: status, issues found, recommendations]

## Cross-File Consistency
[Note any conflicts or gaps]

## Blocking Issues (if any)
[List issues that must be fixed before proceeding]
```

**Check the validation output.**
- If PASSED → proceed to Step 4
- If NEEDS_REVISION → report the blocking issues to the user and ask which research agents to re-run with what additional focus

---

## Step 4: Analysis Phase (PARALLEL)

Launch ALL THREE analyst agents simultaneously in a SINGLE message:

### Agent 1: opportunity-analyst
```
Prompt: Identify and rank market opportunities for {topic}.

Read these files:
- {project_name}/raw_research/market_sizing.md
- {project_name}/raw_research/customer_insights.md
- {project_name}/raw_research/competitors.md

Your task:
1. Cross-reference market segments with unmet customer needs
2. Identify niches where: demand exists + competition is low + barriers are surmountable
3. For each opportunity estimate: addressable market size, competition density, entry barriers, time to market
4. Rank opportunities by attractiveness (consider market size, competition, barriers, urgency of need)

Write analysis to: {project_name}/analysis/opportunities.md

Required sections:
- ## Executive Summary (top 3 opportunities)
- ## Opportunity Assessment Framework
- ## Detailed Opportunity Profiles (ranked)
- ## Opportunity Comparison Matrix (table)
- ## Recommended Focus Areas
- ## Risks and Mitigations
```

### Agent 2: competitive-analyst
```
Prompt: Analyze competitive dynamics and strategic positioning for {topic}.

Read these files:
- {project_name}/raw_research/competitors.md
- {project_name}/raw_research/trends.md

Your task:
1. Map competitors against trends - who is well-positioned for emerging shifts?
2. Identify strategic white space - areas competitors are ignoring
3. Analyze competitive moats (data, network effects, switching costs, brand, scale)
4. Predict likely competitive moves (expansion, consolidation, pivots)
5. Identify vulnerable competitors (underfunded, poorly positioned for trends)

Write analysis to: {project_name}/analysis/competitive_dynamics.md

Required sections:
- ## Executive Summary
- ## Competitor Positioning Matrix
- ## Strategic White Space
- ## Competitive Moats Analysis
- ## Predicted Competitive Moves
- ## Vulnerability Assessment
- ## Strategic Implications
```

### Agent 3: data-synthesizer
```
Prompt: Synthesize and reconcile all quantitative data for {topic}.

Read ALL files in: {project_name}/raw_research/

Your task:
1. Extract every quantitative data point (market sizes, growth rates, funding, pricing, etc.)
2. Reconcile conflicting numbers - note methodology differences that explain discrepancies
3. Create consolidated reference tables
4. Calculate derived metrics where possible (e.g., market concentration, growth differentials)
5. Flag data gaps that should be noted in the final report

Write synthesis to: {project_name}/analysis/key_statistics.md

Required sections:
- ## Data Summary
- ## Market Size Data (consolidated table with source attribution)
- ## Growth Rate Data (consolidated table)
- ## Funding and Investment Data
- ## Pricing Data (where available)
- ## Data Conflicts and Reconciliation Notes
- ## Data Gaps
- ## Methodology Notes
```

**WAIT for all three agents to complete before proceeding.**

---

## Step 5: User Checkpoint

Present a summary to the user:

1. **Top 3 Opportunities** from opportunities.md (one sentence each)
2. **Key Data Points** from key_statistics.md (market size, growth rate, major players)
3. **Strategic White Space** from competitive_dynamics.md (main gaps found)

Use AskUserQuestion with these options:
- "Proceed with report generation using this analysis"
- "Re-analyze with different focus (specify)"
- "Need additional research on a specific area"
- "Review the full analysis files before proceeding"

**Wait for user response before proceeding.**

---

## Step 6: Report Architecture

Launch the report-architect agent:

```
Prompt: Design the structure for a professional market research report on {topic}.

Read all files in:
- {project_name}/analysis/
- {project_name}/raw_research/

Your task:
1. Design a logical report flow that tells a compelling story
2. Decide which data belongs in which section
3. Identify which tables and figures to include
4. Write a detailed outline with bullet points of content for each section
5. Note which sources support each major claim

Write outline to: {project_name}/report/outline.md

Required format:
## Report Title: [Suggest a professional title]

## Abstract
[2-3 bullet points of what it should cover]

## 1. Introduction
### 1.1 [Subsection]
- Point to make (source: filename)
- Point to make (source: filename)
[Continue for all subsections]

## 2. [Next major section]
[Continue pattern]

## Tables and Figures Needed
- Table 1: [description] (data from: filename)
- Figure 1: [description] (data from: filename)
[List all]

## Appendices
[What supplementary material to include]
```

---

## Step 7: LaTeX Report Generation

Launch the latex-writer agent:

```
Prompt: Write a professional LaTeX market research report on {topic}.

Read:
- {project_name}/report/outline.md (follow this structure)
- All files in {project_name}/analysis/
- All files in {project_name}/raw_research/

Create two files:
1. {project_name}/report/{project_name}_market_report.tex
2. {project_name}/report/{project_name}_references.bib

LaTeX Requirements:
- \documentclass[12pt,a4paper]{article}
- Packages: inputenc, fontenc, geometry (1in margins), graphicx, booktabs, hyperref, natbib, float, longtable, fancyhdr, xcolor, caption, enumitem, array
- Professional title page with: title, subtitle "Market Research Report", date
- Abstract (200-250 words) that surfaces the FULL BREADTH of market trends and ALL significant niches - do NOT limit to "top 3" findings. The abstract should give readers a complete picture of the market landscape including: market size/growth, all major trends (technology, regulatory, investment, macro), all identified segments and niches, competitive dynamics, and strategic landscape.
- Table of contents (\tableofcontents)
- Proper sectioning (\section, \subsection, \subsubsection)
- Tables using booktabs (\toprule, \midrule, \bottomrule)
- All data claims cite sources using \cite{key}
- Headers: page number on left, report title on right (use fancyhdr)
- Hyperlinks for cross-references and citations
- Appendices for detailed data tables

BibTeX Requirements:
- Entry for every source cited
- Use consistent key format: authorYear or domainYear (e.g., marketsandmarkets2025, seafoodsource2024)
- Include URL field for web sources
- Include accessed date for web sources

Style Guidelines:
- Professional, objective tone
- Data-driven claims (not speculation)
- Executive-friendly (key points in first paragraph of each section)
- Tables for comparative data
- Clear section transitions
```

---

## Step 8: LaTeX Validation and Compilation

First, run a draft compilation to check for errors:

```bash
cd {project_name}/report && pdflatex -draftmode -halt-on-error {project_name}_market_report.tex
```

If this fails:
1. Read the .log file to identify errors
2. Fix the LaTeX errors in the .tex file
3. Retry until draft mode passes

Once draft mode passes, run the full compilation:

```bash
cd {project_name}/report && pdflatex {project_name}_market_report.tex && bibtex {project_name}_market_report && pdflatex {project_name}_market_report.tex && pdflatex {project_name}_market_report.tex
```

---

## Step 9: PDF Readability Validation (Iterative)

After PDF compilation succeeds, perform visual validation of the generated PDF:

**Use the Read tool to view the PDF file:**
```
Read: {project_name}/report/{project_name}_market_report.pdf
```

**Evaluate the PDF for these readability criteria:**

1. **Table Quality**
   - Tables are properly aligned and not overflowing margins
   - Column widths are appropriate for content
   - Headers are clearly distinguished from data
   - No text is cut off or wrapped awkwardly

2. **Text Formatting**
   - Paragraphs have proper spacing (not cramped, not excessive)
   - Section headings are visually distinct
   - Font sizes are consistent and readable
   - No orphan/widow lines at page breaks

3. **Professional Appearance**
   - Title page is clean and well-balanced
   - Page numbers and headers render correctly
   - Table of contents entries align properly
   - Citations appear correctly in text and bibliography

4. **Overall Layout**
   - Content flows logically across pages
   - Figures/tables appear near their references
   - No excessive white space or cramped sections
   - Margins are consistent throughout

**If any issues are found:**

1. Identify the specific LaTeX causing the issue
2. Edit the .tex file to fix the problem:
   - For table overflow: adjust column widths, use `longtable`, or reduce font size
   - For spacing issues: adjust `\parskip`, `\baselineskip`, or use `\vspace`
   - For formatting issues: check package usage and LaTeX syntax
3. Recompile the PDF:
   ```bash
   cd {project_name}/report && pdflatex {project_name}_market_report.tex && pdflatex {project_name}_market_report.tex
   ```
4. Re-validate the PDF by reading it again
5. Repeat until all readability issues are resolved

**Validation passes when:**
- All tables render cleanly within margins
- Text is properly spaced and readable
- Professional appearance is achieved
- No visual defects remain

Only proceed to Step 10 when PDF validation passes.

---

## Step 10: Final Deliverables

Confirm these files exist and report to user:

1. **{project_name}/report/{project_name}_market_report.pdf** - Final report (validated for readability)
2. **{project_name}/analysis/opportunities.md** - Ranked opportunities
3. **{project_name}/analysis/competitive_dynamics.md** - Strategic analysis
4. **{project_name}/analysis/key_statistics.md** - Consolidated data
5. **{project_name}/raw_research/*.md** - Source research

Tell the user:
> "Market research complete. Your report is at {project_name}/report/{project_name}_market_report.pdf
>
> Key deliverables:
> - Full PDF report with citations (validated for readability and professional formatting)
> - Ranked opportunities analysis
> - Competitive dynamics assessment
> - Consolidated market statistics
>
> All source research is preserved in {project_name}/raw_research/ for reference."
