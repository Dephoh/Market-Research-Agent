---
name: market-research
description: "Run comprehensive market research pipeline with specialized agents. Usage: /market-research <topic or description>"
user_invocable: true
---

# Market Research Pipeline

You are orchestrating a comprehensive market research pipeline. The user has requested research on: **$ARGUMENTS**

---

## CRITICAL: Anti-Hang Instructions

**Every subagent MUST follow these rules to prevent hanging:**

1. **NEVER ask for user input or clarification.** Make your best judgment and proceed. If truly stuck, write what you have and note the limitation.
2. **NEVER retry the same failing approach more than 3 times.** After 3 failures, document the issue and move on.
3. **If a web search returns no results, try 2 alternative queries max, then proceed with available information.**
4. **If a file cannot be read/written, report the error and continue with other tasks.**
5. **Complete your task within reasonable bounds - do not pursue perfection endlessly.**

---

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

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
- NEVER ask for user input or clarification. Make your best judgment.
- If a search returns no results, try up to 2 alternative queries, then proceed with what you have.
- If you cannot find data for a section, write "Data not available" and continue.
- Complete your research and write the file. Do not get stuck seeking perfection.
- You have a maximum of 15 web searches. Use them wisely.

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

When finished, confirm the file was written successfully.
```

### Agent 2: competitor-mapper
```
Prompt: Map the competitive landscape for {topic}.

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
- NEVER ask for user input or clarification. Make your best judgment.
- If a search returns no results, try up to 2 alternative queries, then proceed with what you have.
- If you cannot find data for a company, note "Limited data available" and continue.
- Complete your research and write the file. Do not get stuck seeking perfection.
- You have a maximum of 15 web searches. Use them wisely.

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

When finished, confirm the file was written successfully.
```

### Agent 3: customer-researcher
```
Prompt: Research customer pain points and unmet needs in {topic}.

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
- NEVER ask for user input or clarification. Make your best judgment.
- If a search returns no results, try up to 2 alternative queries, then proceed with what you have.
- If you cannot find verbatim quotes, summarize the pain points you found and note the source.
- Complete your research and write the file. Do not get stuck seeking perfection.
- You have a maximum of 15 web searches. Use them wisely.

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

When finished, confirm the file was written successfully.
```

### Agent 4: trend-scanner
```
Prompt: Research technology trends, regulatory changes, and market shifts affecting {topic}.

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
- NEVER ask for user input or clarification. Make your best judgment.
- If a search returns no results, try up to 2 alternative queries, then proceed with what you have.
- If regulatory data is sparse for a region, note "Limited regulatory data" and continue.
- Complete your research and write the file. Do not get stuck seeking perfection.
- You have a maximum of 15 web searches. Use them wisely.

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

When finished, confirm the file was written successfully.
```

### Agent 5: latent-demand-researcher
```
Prompt: Research latent and hidden demand opportunities in {topic}.

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
- NEVER ask for user input or clarification. Make your best judgment.
- If a search returns no results, try up to 2 alternative queries, then proceed with what you have.
- If you cannot find examples for a category, note "No clear examples found" and continue.
- Complete your research and write the file. Do not get stuck seeking perfection.
- You have a maximum of 15 web searches. Use them wisely.

CONTEXT: Latent demand refers to demand that exists but is not being served by current market offerings. Classic example: Uber didn't just take taxi market share—it created NEW demand by enabling short trips people wouldn't have taken with expensive taxis. The market was bigger than anyone measured because measurement only captured existing consumption.

Your task:
1. **Non-consumption analysis**: Identify who is NOT using current solutions and why
   - What barriers prevent adoption? (price, access, complexity, time, trust)
   - Who "makes do" with inferior substitutes or manual workarounds?
   - What jobs-to-be-done are people hiring inadequate solutions for?

2. **Workaround detection**: Search for behavioral signals of latent demand
   - DIY solutions, spreadsheets, manual processes people cobble together
   - "Hacks" or creative misuse of adjacent products
   - Complaints about having to use multiple tools for one job
   - Forum discussions about "I wish there was a way to..."

3. **Friction analysis**: What friction in current solutions suppresses demand?
   - High minimum order sizes, long lead times, complex onboarding
   - Geographic or demographic segments underserved
   - Use cases that are technically possible but practically difficult

4. **Adjacent market spillover**: Where could demand migrate FROM if barriers dropped?
   - What do people do instead when they can't access this market's solutions?
   - What cheaper/simpler alternatives cannibalize potential demand?
   - What new use cases would emerge at 10x lower cost or 10x more convenience?

5. **Analogous market patterns**: Find examples from other industries
   - Markets that exploded when friction was removed (streaming, ride-sharing, cloud computing)
   - What was the "Uber moment" in similar verticals?
   - What enabled market expansion beyond incumbent assumptions?

Write your findings in structured markdown to: {project_name}/raw_research/latent_demand.md

Required sections:
- ## Executive Summary
- ## Non-Consumption Analysis (who's not buying and why)
- ## Workarounds and DIY Signals (evidence of unmet demand)
- ## Friction Points Suppressing Demand
- ## Adjacent Market Opportunities
- ## Analogous Market Patterns
- ## Latent Demand Hypotheses (ranked by evidence strength)
- ## Market Expansion Scenarios (if friction removed)
- ## Sources (with URLs)

When finished, confirm the file was written successfully.
```

**WAIT for all five agents to complete before proceeding.**

---

## Step 3: Research Validation

Launch the research-validator agent:

```
Prompt: Validate the quality of research files in {project_name}/raw_research/

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
- NEVER ask for user input or clarification. Make your best judgment.
- Complete validation in a single pass. Do not iterate endlessly.
- If a file is missing, note it and continue validating other files.
- Your job is to ASSESS quality, not to fix issues yourself.

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
- [ ] Latent demand hypotheses are supported by evidence (workarounds, non-consumption signals)

Write validation report to: {project_name}/raw_research/_validation.md

Format:
## Validation Status: [PASSED/NEEDS_REVISION]

## File-by-File Assessment
[For each file: status, issues found, recommendations]

## Cross-File Consistency
[Note any conflicts or gaps]

## Blocking Issues (if any)
[List issues that must be fixed before proceeding]

When finished, confirm the file was written successfully.
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

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
- NEVER ask for user input or clarification. Make your best judgment.
- Work only with the data in the provided files. Do not search for more.
- If data is missing for an analysis, note the gap and proceed with available information.
- Complete your analysis and write the file. Do not get stuck seeking perfection.

Read these files:
- {project_name}/raw_research/market_sizing.md
- {project_name}/raw_research/customer_insights.md
- {project_name}/raw_research/competitors.md
- {project_name}/raw_research/latent_demand.md

Your task:
1. Cross-reference market segments with unmet customer needs
2. Identify niches where: demand exists + competition is low + barriers are surmountable
3. **Evaluate latent demand opportunities**: Assess which latent demand hypotheses represent the largest potential market expansion (like Uber creating new trips, not just taking taxi share)
4. For each opportunity estimate: addressable market size, competition density, entry barriers, time to market, **latent demand multiplier** (potential to expand the market beyond current consumption)
5. Rank opportunities by attractiveness (consider market size, competition, barriers, urgency of need, **latent demand potential**)

Write analysis to: {project_name}/analysis/opportunities.md

Required sections:
- ## Executive Summary (top 3 opportunities, noting any with significant latent demand)
- ## Opportunity Assessment Framework
- ## Detailed Opportunity Profiles (ranked)
- ## Latent Demand Opportunities (market expansion potential beyond current consumption)
- ## Opportunity Comparison Matrix (table, include latent demand multiplier column)
- ## Recommended Focus Areas
- ## Risks and Mitigations

When finished, confirm the file was written successfully.
```

### Agent 2: competitive-analyst
```
Prompt: Analyze competitive dynamics and strategic positioning for {topic}.

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
- NEVER ask for user input or clarification. Make your best judgment.
- Work only with the data in the provided files. Do not search for more.
- If data is missing for an analysis, note the gap and proceed with available information.
- Complete your analysis and write the file. Do not get stuck seeking perfection.

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

When finished, confirm the file was written successfully.
```

### Agent 3: data-synthesizer
```
Prompt: Synthesize and reconcile all quantitative data for {topic}.

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
- NEVER ask for user input or clarification. Make your best judgment.
- Work only with the data in the provided files. Do not search for more.
- If numbers conflict, document both values and note the discrepancy. Do not endlessly try to reconcile.
- Complete your synthesis and write the file. Do not get stuck seeking perfection.

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
- ## Latent Demand Indicators (quantified where possible)
- ## Data Gaps
- ## Methodology Notes

When finished, confirm the file was written successfully.
```

**WAIT for all three agents to complete before proceeding.**

---

## Step 5: User Checkpoint

Present a summary to the user:

1. **Top 3 Opportunities** from opportunities.md (one sentence each)
2. **Key Data Points** from key_statistics.md (market size, growth rate, major players)
3. **Strategic White Space** from competitive_dynamics.md (main gaps found)
4. **Latent Demand Highlights** from opportunities.md (top market expansion opportunities where reducing friction could unlock hidden demand)

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

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
- NEVER ask for user input or clarification. Make your best judgment.
- Work only with the data in the provided files. Do not search for more.
- Design a complete outline in a single pass. Do not iterate endlessly.
- Complete your outline and write the file. Do not get stuck seeking perfection.

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

When finished, confirm the file was written successfully.
```

---

## Step 7: LaTeX Report Generation

Launch the latex-writer agent:

```
Prompt: Write a professional LaTeX market research report on {topic}.

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
- NEVER ask for user input or clarification. Make your best judgment.
- Work only with the data in the provided files. Do not search for more.
- Write complete .tex and .bib files in a single pass.
- If you're unsure about formatting, use standard LaTeX conventions and proceed.
- Complete the files. Do not get stuck seeking perfection.

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

When finished, confirm both files were written successfully.
```

---

## Step 8: LaTeX Validation and Compilation

**IMPORTANT: Maximum 5 compilation attempts. If still failing after 5 attempts, report the error to the user and proceed to deliver the .tex file without PDF.**

First, run a draft compilation to check for errors:

```bash
cd {project_name}/report && timeout 60 pdflatex -draftmode -halt-on-error {project_name}_market_report.tex
```

If this fails:
1. Read the .log file to identify errors
2. Fix the LaTeX errors in the .tex file
3. Retry (track attempt count)
4. **After 3 failed attempts at draft mode**, simplify the LaTeX (remove complex tables, simplify formatting) and try again
5. **After 5 total attempts**, stop and report the issue to the user

Once draft mode passes, run the full compilation:

```bash
cd {project_name}/report && timeout 120 pdflatex {project_name}_market_report.tex && timeout 60 bibtex {project_name}_market_report && timeout 120 pdflatex {project_name}_market_report.tex && timeout 120 pdflatex {project_name}_market_report.tex
```

If bibtex fails, try compiling without bibliography (comment out \bibliography line) and note this in the final report.

---

## Step 9: PDF Readability Validation (Iterative)

**IMPORTANT: Maximum 3 fix-and-recompile cycles. After 3 cycles, accept the current PDF quality.**

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

**If issues are found (max 3 fix cycles):**

1. Identify the specific LaTeX causing the issue
2. Edit the .tex file to fix the problem:
   - For table overflow: adjust column widths, use `longtable`, or reduce font size
   - For spacing issues: adjust `\parskip`, `\baselineskip`, or use `\vspace`
   - For formatting issues: check package usage and LaTeX syntax
3. Recompile the PDF:
   ```bash
   cd {project_name}/report && timeout 120 pdflatex {project_name}_market_report.tex && timeout 120 pdflatex {project_name}_market_report.tex
   ```
4. Re-validate the PDF by reading it again
5. **After 3 fix cycles, accept the current quality and proceed**

**Validation passes when:**
- All tables render cleanly within margins (or best effort after 3 cycles)
- Text is properly spaced and readable
- Professional appearance is achieved
- No major visual defects remain

Proceed to Step 10 when validation passes OR after 3 fix cycles.

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
