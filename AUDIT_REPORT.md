# NEM Research Terminal — Full Tab Audit Report

**Repository:** https://github.com/CalebSmit/nem-research-terminal  
**File audited:** `app.py` — 8,224 lines, 557 KB  
**Audit date:** April 2, 2026  
**Scope:** Read-only analysis. No code changes made.

---

## Table of Contents

1. [Tab-by-Tab Audit (20 tabs)](#tab-by-tab-audit)
2. [Recommended Final Tab List](#recommended-final-tab-list)
3. [Collapsible Expander Candidates](#collapsible-expander-candidates)
4. [The 5 Biggest UX Problems](#the-5-biggest-ux-problems)
5. [Full First-Person Phrase Inventory](#full-first-person-phrase-inventory)

---

## Tab-by-Tab Audit

---

### Tab 01 · STORY

**Lines:** 1164–1652 (488 lines)

**Primary Content**  
The research narrative — written as a first-person walkthrough of how the thesis was constructed using Perplexity Computer. Leads with a hero KPI strip (NEM Price, Our Target, Upside, Rating). The central insight: a reverse-DCF calculation reveals the market is implicitly pricing gold at ~$3,700/oz while spot trades ~$5,200/oz. Eight channel-check summaries are presented in prose form. A dedicated section — "What Almost Killed the Thesis" — surfaces three bearish findings (insider selling, Lihir shaft pause, Ghana royalty hike) alongside the analyst's rebuttals.

**Secondary Content**  
"The Credibility Question" sidebar. "The Punchline" summary box. Bear Case Preemption panel. Kill Criteria box (four falsifiable conditions that would flip the rating). Navigation guide — "Where to Go From Here" — pointing users to tabs 2–15. An 8-thread Perplexity Research Log mapping each research query to its finding, assumption change, and downstream tab.

**UX Problems**
- At 488 lines, this is the longest tab and requires the most scrolling. A user landing here expecting a summary gets a full novella before they see the KPIs.
- The Kill Criteria box is buried near the bottom. It is one of the most important pieces of information in the entire dashboard and a first-time user will miss it entirely.
- The navigation guide partially replicates the tab bar itself and adds scroll burden without adding clarity.
- The 8-thread Perplexity Research Log is methodologically valuable but is enormous. It occupies the bottom third of an already-long tab and is invisible to anyone who doesn't scroll past the kill criteria.
- The hero KPI strip appears at the very top but is followed by a wall of HTML prose. There is no visual break or "skip to analysis" mechanism.

**Naming Accuracy**  
Partially accurate. "STORY" fits the narrative prose sections, but Kill Criteria and the Research Log are methodology artifacts that belong in different contexts. A more precise name would be "THESIS" or "HOW WE GOT HERE."

**Consolidation Candidate**  
- Perplexity Research Log → collapsible expander at bottom of this tab  
- Kill Criteria → move exclusively to VERDICT tab (15), remove here  
- Navigation guide → remove; the tab bar does this job

---

### Tab 02 · CMD

**Lines:** 1652–2030 (378 lines)

**Primary Content**  
Dashboard command center. A 5-column grid presents the three falsifiable non-consensus calls side-by-side with the consensus view and NEM's actual 2025 performance data. KPI tiles display live price, our target, upside, and recommendation. A second row of analytical KPI tiles shows Monte Carlo P(>current price), Piotroski F-Score, Altman Z-Score, and gold beta.

**Secondary Content**  
A "Reverse DCF Anchor" callout card linking to the VERDICT tab. Three thesis-driver cards (Operating Leverage, Credibility Flip, Copper Option). A valuation bridge waterfall chart. Historical sparklines for FCF, revenue, and AISC. A "What Has to Be True" falsifiable scorecard with traffic-light status indicators.

**UX Problems**
- The 5-column non-consensus grid is very wide. On laptop-width screens it will compress and the column headers risk truncation or text-wrapping that breaks readability.
- The analytical KPI row runs a mini Monte Carlo simulation inline on every page load, which adds non-trivial compute time before the tab renders.
- "What Has to Be True" partially duplicates the Kill Criteria in tab 01·STORY and the Kill Criteria section in tab 15·VERDICT. Three locations for the same content creates maintenance risk and user confusion about which is canonical.

**Naming Accuracy**  
Accurate. "CMD" (Command Center) is the correct label — this is the hub that surfaces the thesis, the valuation anchor, and the key metrics.

**Consolidation Candidate**  
No — this tab is the intended entry point and hub. It should remain standalone.

---

### Tab 03 · GOLD

**Lines:** 2030–2575 (545 lines)

**Primary Content**  
Gold macro analysis. The flagship chart overlays the NEM-relevant gold price against the company's AISC with annotated geopolitical events. A horizontal bar chart compares major bank gold price forecasts (Goldman, JPMorgan, Citi, BofA, Barclays) against the model's $5,200 deck. A "Gold Fundamental Regime Assessment" panel summarizes why the structural bull case remains intact.

**Secondary Content**  
Gold price averages table (2022–2025 + forward). Central bank purchase bar chart (World Gold Council data). ETF flow data. Supply-demand balance stacked bar chart. Ore grade decline trend chart. Permitting timeline chart (average discovery-to-production at 16+ years). NEM AISC benchmarked against industry average. Multiple "Perplexity Premium Data" source callout boxes.

**UX Problems**
- The tab is very long. The ore grade decline and permitting timeline charts are important thesis supports but appear so far below the fold that most users will not reach them.
- Multiple "Perplexity Premium Data" callout boxes interrupt the visual flow and add significant height without adding analytical content.
- No internal anchoring or section dividers to help orient the user as they scroll.

**Naming Accuracy**  
Accurate. All content is gold macro analysis.

**Consolidation Candidate**  
- Ore grade decline + permitting timeline charts → collapsible expander ("Why Supply Cannot Respond")
- Central bank + ETF flow charts → collapsible expander ("Demand Drivers Detail")

---

### Tab 04 · PROFILE

**Lines:** 2575–2674 (99 lines)

**Primary Content**  
Five-year financial summary table spanning 2021–2025 actuals plus FY2026E and FY2027E estimates. An FCF trajectory bar chart. An earnings beat/miss tracker (quarterly).

**Secondary Content**  
Piotroski F-Score breakdown (all 9 sub-criteria with pass/fail). Altman Z-Score display with zone interpretation.

**UX Problems**
- Piotroski F-Score and Altman Z-Score are already shown as KPI tiles in the CMD tab. Showing them again here as expanded tables without acknowledging the duplication creates the impression of two authoritative sources that could diverge if data changes.
- Tab 19·ROIC is thematically identical to this tab (financial quality metrics) but is placed 15 tabs away, breaking the logical grouping.
- The tab name "PROFILE" is vague for what is actually a financial health and historical financials display.

**Naming Accuracy**  
Weak. "FINANCIALS" or "FINANCIAL PROFILE" would be clearer and set more accurate user expectations.

**Consolidation Candidate**  
- Tab 19·ROIC → merge here as a section (strong candidate)
- Piotroski/Altman expanded tables → could be collapsed if CMD shows the headline numbers

---

### Tab 05 · MINES

**Lines:** 2674–2846 (172 lines)

**Primary Content**  
Global mine portfolio map using a geographic scatter plot with AISC color-coding. A mine portfolio table listing all active assets with their NAV percentage contribution, jurisdiction, mine type, and 2025 production.

**Secondary Content**  
Mine-level AISC horizontal bar chart (lowest to highest cost). Production treemap (area proportional to Koz). Tier 1 asset spotlights: Cadia (AISC ~$400/oz) and Lihir (~700 Koz/year production).

**UX Problems**
- A production footnote explaining a ~360 Koz discrepancy between mine-by-mine totals and the portfolio-level guidance number is buried below the mine table. A user who notices the number mismatch has no obvious path to the explanation.

**Naming Accuracy**  
Accurate.

**Consolidation Candidate**  
No — a standalone mine map and portfolio table is the correct presentation for this content type. The geographic context adds genuine analytical value.

---

### Tab 06 · DCF

**Lines:** 2846–3935 (1,089 lines)

**Primary Content**  
Interactive FCFF model. User-adjustable inputs (gold price, AISC, WACC, exit multiple, production growth) drive a 5-year revenue forecast table built on a per-ounce margin model. A sensitivity heatmap shows implied target price as a function of WACC × exit multiple.

**Secondary Content**  
Quick stress test buttons (GOLD -30%, AISC +25%, BEAR WACC, RESET) that trigger `st.rerun()` to repopulate the model. A confidence interval banner. An assumption transparency scorecard listing all 38 model assumptions with source citation and rationale.

**UX Problems**
- At 1,089 lines, this is the longest tab by line count. The assumption transparency scorecard alone accounts for a substantial portion — it is thorough and valuable, but entirely collapsed by default it would retain the same value with a fraction of the scroll burden.
- The stress test buttons are the most interactive and useful element on the tab, but they appear below the sensitivity heatmap, not above it — users must scroll past results to find the controls.

**Naming Accuracy**  
Accurate.

**Consolidation Candidate**  
- Assumption transparency scorecard (38 items) → collapsible expander  
- DCF methodology note → collapsible expander

---

### Tab 07 · REL VAL

**Lines:** 3935–4703 (768 lines)

**Primary Content**  
Peer comparison table: NEM, Agnico Eagle (AEM), Barrick (GOLD), Kinross (KGC), Gold Fields (GFI), and Wheaton Precious Metals (WPM) separated into a streaming bucket. EV/EBITDA and P/E bar charts vs. peers.

**Secondary Content**  
Full equity research comp sheet (8 metrics × 6 peers). AISC vs. EV/EBITDA scatter plot. AISC trajectory line chart (2021–2025 for all peers). Peer strategy comparison narrative panels. A re-rating scenario section with three KPI tiles (current multiple, peer average, implied target on re-rating). An "Alpha Insight — Non-Consensus" panel at the bottom.

**UX Problems**
- A "Non-Obvious Competitive Insight Navigator" panel at the top explicitly tells the user to scroll down to find specific charts. This is a UX anti-pattern — it acknowledges that the content is buried and instructs the user to hunt for it instead of surfacing it.
- The peer strategy comparison section at the bottom of the tab is substantial enough to be a standalone mini-tab. It reads like a separate analysis dropped into a valuation tab.
- The AISC trajectory line chart belongs as visually and thematically in tab 03·GOLD or tab 04·PROFILE as it does here.
- At 768 lines, horizontal scrolling and chart density will create rendering pressure on lower-end devices.

**Naming Accuracy**  
Partially accurate. "REL VAL" describes the peer multiples and comp sheets, but the peer strategy comparison section (below the fold) is not relative valuation — it is competitive positioning analysis.

**Consolidation Candidate**  
- Peer strategy comparison → standalone collapsible section or move to a dedicated tab ("07·PEERS")
- AISC trajectory chart → promote to tab 03·GOLD or tab 04·PROFILE

---

### Tab 08 · RISK

**Lines:** 4703–4902 (199 lines)

**Primary Content**  
Four-scenario analysis: BULL, BASE, BEAR, and STRESS. Each scenario shows a DCF-derived price, upside/downside from current, and qualitative description. A risk-reward ratio and probability-weighted expected value are computed.

**Secondary Content**  
Risk matrix bubble chart (probability on x-axis, FCF impact on y-axis, bubble size = magnitude). Breakeven and asymmetry bar chart. A risk quantification table listing five specific risks with FCF impact estimate, target price impact, and resolution date.

**UX Problems**
- The risk quantification table contains inline text that cross-references other tabs: "Tab 01 told the story. Tab 12 has the raw findings." This is a self-referential UX pattern that breaks the tab's self-containment — a user in the RISK tab is told to go somewhere else to understand the content they are currently reading.
- The four-scenario tiles use very similar visual weight for BULL and STRESS, making it easy to confuse the range without careful reading.

**Naming Accuracy**  
Accurate.

**Consolidation Candidate**  
- Risk quantification table → could partially merge with tab 12·ALT DATA channel check summaries to eliminate the cross-reference dependency

---

### Tab 09 · MC SIM

**Lines:** 4902–5139 (237 lines)

**Primary Content**  
A 50,000-iteration correlated Monte Carlo simulation. Five KPI tiles show Median price, Mean price, P(>current price), P10, and P90. A histogram of the distribution is the central visual.

**Secondary Content**  
Convergence plot (running median stabilizes around 10,000 iterations). Tornado chart showing the proportion of output variance explained by each input variable. Simulation parameters table. Statistical robustness notes. Two `why_expander` methodology popup boxes.

**UX Problems**
- The simulation is computation-heavy. Running 50,000 iterations on every tab render is a meaningful performance cost in a Streamlit app with no caching layer shown here.
- The tab is the most quantitatively demanding in the dashboard and has no plain-English summary at the top to anchor non-quant readers before diving into the histogram and tornado chart.
- The convergence plot's title is auto-generated from the exact iteration count, which will render as a long machine-generated label rather than a human-readable chart title.

**Naming Accuracy**  
Accurate.

**Consolidation Candidate**  
- Simulation parameters table + statistical robustness notes → collapsible expander  
- Methodology popups are already using `st.expander()` — appropriate

---

### Tab 10 · RETURNS

**Lines:** 5139–5250 (111 lines)

**Primary Content**  
Capital returns analysis: 2025 dividends paid, buybacks executed, total shareholder return. FCF yield, dividend yield, buyback yield, and total shareholder yield. Net cash position context ($7.2B).

**Secondary Content**  
Share count trend (shrinking via buybacks). Dividend yield vs. gold price sensitivity. An insight callout: "NEM returned $3.4B to shareholders in 2025 while sitting on net cash of $7.2B. If the stock is mispriced, you're getting paid to wait — [X]% dividend yield + [X]% buyback yield = [X]% total shareholder yield."

**UX Problems**
- At 111 lines, this is one of the shortest tabs and feels thin compared to the analytical depth of neighboring tabs. The content would fit comfortably as a section inside tab 04·PROFILE.
- The phrase "you're getting paid to wait" appears in the insight callout in first-person address mode directed at the reader — the only instance in the dashboard where the reader is addressed as "you" in an insight callout.

**Naming Accuracy**  
"RETURNS" is somewhat ambiguous — it could mean total return (price + dividends), capital returns to shareholders, or investment return modeling. In context it means capital returns, which "CAPITAL RETURNS" or "SHAREHOLDER YIELD" would clarify.

**Consolidation Candidate**  
Strong candidate — merge with tab 04·PROFILE as a "Capital Returns" section.

---

### Tab 11 · CATALYST

**Lines:** 5250–5346 (96 lines)

**Primary Content**  
A 10-item catalyst table with probability estimate (%), expected share price impact ($/share), probability-weighted expected value, target quarter, and status. A probability-weighted EV waterfall bar chart showing cumulative catalyst impact on price.

**Secondary Content**  
Catalyst timeline scatter chart (Q1 2026 through Q1 2027) with "WE ARE HERE" annotation at the current date.

**UX Problems**
- The tab is clean and focused — the weakest criticism is that "WE ARE HERE" annotation on the timeline is a first-person collective voice element in an otherwise analytical context.
- At 96 lines, this is one of the shorter tabs. A quarterly notes section in tab 20·QRTLY MODEL partially duplicates catalysts, creating two slightly different catalyst lists in different places.

**Naming Accuracy**  
Accurate.

**Consolidation Candidate**  
Moderate candidate — could merge with tab 15·VERDICT as a forward-looking section. The catalyst map is complementary to the verdict and adds forward visibility without requiring its own tab.

---

### Tab 12 · ALT DATA

**Lines:** 5346–5728 (382 lines)

**Primary Content**  
Eight proprietary channel checks with full-text findings and a signal rating (STRONGLY BULLISH, BULLISH, NEUTRAL, or BEARISH) for each:
1. Job postings (STRONGLY BULLISH)
2. Insider transactions — Form 4 analysis (BEARISH)
3. SEC filing language delta (BULLISH)
4. Earnings call NLP sentiment (BULLISH)
5. Lihir shaft infrastructure pause (BEARISH)
6. Ghana royalty regulation change (BEARISH)
7. Competitor AISC benchmarking (STRONGLY BULLISH)
8. AI/data center copper demand (BULLISH)

A signal distribution scorecard summarizes the 8 findings.

**Secondary Content**  
Three "Non-Consensus Hero Cards" at the top: AISC Credibility Flip, Cadia Copper AI Play, Reverse DCF Gap. Bear case resolution calendar (expected resolution dates for the three bearish signals). Net assessment panel.

**UX Problems**
- The three Non-Consensus Hero Cards at the top of this tab are identical in content and visual design to the three thesis-driver cards in tab 02·CMD. This is direct content duplication across tabs with no differentiation.
- Each of the 8 channel checks is rendered as a long HTML block of prose with no `st.expander()` wrapping. A user must scroll through ~40 lines of dense text per check to find the finding summary. At 8 checks, that is 300+ lines of narrative before reaching the signal scorecard.
- The tab header uses the phrase "FINDINGS A SELL-SIDE ANALYST AT GOLDMAN DOESN'T HAVE" as a section title. This is a strong claim embedded in the UI itself.

**Naming Accuracy**  
"ALT DATA" undersells the content. These are not simply alternative data feeds — they are eight primary research investigations. "PRIMARY RESEARCH" or "CHANNEL CHECKS" would be more precise.

**Consolidation Candidate**  
No consolidation into another tab — this warrants standalone presentation. But each of the 8 channel checks should be wrapped in `st.expander()` (show signal rating + one-line summary, expand for full text).

---

### Tab 13 · ESG

**Lines:** 5728–5854 (126 lines)

**Primary Content**  
ESG ratings dashboard: five KPI tiles (MSCI ESG: AA, Sustainalytics: 27.6 Medium Risk, CDP Climate: A-, S&P CSA Percentile: 99th, ISS Governance: QS1).

**Secondary Content**  
E/S/G breakdown panels with specific metrics (GHG intensity, TRIR, board independence, etc.). Radar chart: NEM vs. sector average across 6 ESG pillars. ESG peer comparison bar chart (NEM vs. Barrick vs. Agnico). ESG capital flows context panel (with an inline caveat flagging the $30T AUM figure as a contested 2022 Bloomberg estimate). "Honest Tensions" section disclosing three negative ESG factors (fatalities, environmental impact, jurisdictional risk).

**UX Problems**
- The most important editorial judgment in this tab — the inline caveat calling out the contested $30T ESG AUM figure — is buried inside a right-column card at the bottom half of the tab. A claim of this magnitude (cited in the insight callout at the top) should be caveated before or immediately after first use, not hundreds of pixels below it.
- No UX problems with structural layout; this is one of the better-structured shorter tabs.

**Naming Accuracy**  
Accurate.

**Consolidation Candidate**  
Weak candidate — ESG content is sufficiently distinct to warrant its own tab given the audience (institutional investors screening on ESG mandates). The "Honest Tensions" section is a strong differentiator that benefits from dedicated space.

---

### Tab 14 · CREDIBILITY

**Lines:** 5854–6333 (479 lines)

**Primary Content**  
A 10-year production guidance vs. actuals study (2015–2025). The central finding: NEM beat production guidance in only 2 of 10 years, with an average miss of -3.5%. The analysis identifies two distinct eras: pre-Goldcorp (±1% accuracy) and post-Goldcorp integration (average -5.4% miss). The 2024–2025 convergence to -0.4% is presented as evidence the integration penalty is resolved — this is called "Driver 3: The Credibility Flip."

**Secondary Content**  
AISC credibility non-consensus callout panel: FY2025 AISC guided at $1,620/oz, actual $1,358/oz — a $262/oz beat described as non-consensus because "Goldman knows the production miss record; Goldman doesn't know the AISC beat." Era comparison bar chart. Peer credibility comparison. Quantified punchline: the production haircut applied to the model (-2.9%, from 5.26 to 5.11 Moz) with the resulting DCF impact.

**UX Problems**
- The insight callout at the top references tab 15·VERDICT ("the final verdict is in 15·VERDICT") — cross-tab navigation via text is functional but not linked, requiring the user to navigate manually.
- The tab numbering creates a subtle confusion: the tab is labeled "14·CREDIBILITY" but is at Python index 13 (zero-indexed), which means any code references to `tabs[13]` and any "Tab 14" references in other tabs need to stay in sync.

**Naming Accuracy**  
"CREDIBILITY" is accurate but could be more specific: "MGMT TRACK RECORD" or "GUIDANCE STUDY" would clarify that this is specifically a management guidance credibility analysis, not a broader credibility review.

**Consolidation Candidate**  
No — this is a primary analytical driver (Driver 3) and deserves standalone treatment.

---

### Tab 15 · VERDICT

**Lines:** 6333–7039 (706 lines)

**Primary Content**  
The reverse DCF gap visualized as the "single most important insight" — two large bars showing the market's implied gold price vs. spot gold, with the gap expressed as a percentage. Final Verdict panel: BUY recommendation, price target, upside %.

**Secondary Content**  
Four convergence layers summarizing how DCF, Relative Valuation, Monte Carlo, and Reverse DCF all point to the same conclusion. An 8-method convergence bar chart. A full valuation summary table with all methods, their targets, weights, and the blended result. Gold price sensitivity table (target price as a function of gold at $4,000–$6,000/oz and AISC at $1,300–$1,800/oz). Kill criteria (four conditions that would flip the rating to SELL/HOLD).

**UX Problems**
- Kill Criteria appear here AND in tab 01·STORY AND referenced in tab 02·CMD ("What Has to Be True" scorecard). The canonical home for kill criteria should be one location (here), with the other locations pointing to it.
- At 706 lines, this is the second longest tab. The 8-method convergence bar chart, full valuation table, and gold price sensitivity table are all valuable but extend the tab well past the verdict itself. The recommendation and target appear around line 6,400 — a first-time user who reads VERDICT first will not reach the supporting charts.
- The gold price sensitivity table is essentially a second sensitivity heatmap in addition to the one in tab 06·DCF. Minor duplication but adds meaningful length.

**Naming Accuracy**  
Accurate.

**Consolidation Candidate**  
- Kill Criteria → consolidate here (remove from tab 01·STORY)  
- Gold price sensitivity table → collapsible expander (methodology detail)
- 8-method convergence methodology notes → collapsible expander

---

### Tab 16 · GLD CMP

**Lines:** 7039–7190 (151 lines)

**Primary Content**  
Operating leverage comparison: NEM vs. the GLD ETF. Demonstrates that NEM provides leveraged exposure to gold price movements — a $1 move in gold produces more than $1 of equity value change in NEM due to fixed-cost structure. Scenario returns table (bear/base/bull gold assumptions).

**Secondary Content**  
Dividend advantage comparison (NEM dividend yield vs. GLD which pays none). Breakeven comparison. Conclusion panel: "If you believe gold is going higher, NEM is a better vehicle than GLD."

**UX Problems**
- The tab name "GLD CMP" is cryptic. Without context, the abbreviation "GLD CMP" does not immediately communicate "NEM vs. Gold ETF Comparison" to a new user.
- This tab does not appear in the navigation guide in tab 01·STORY ("Where to Go From Here") — it is effectively orphaned from the guided flow.
- The content is analytically relevant to the thesis but its placement at tab 16 (post-VERDICT) means most users following the linear narrative will have already formed their view before reaching it. As a pre-verdict argument for operating leverage, it might be better positioned earlier.

**Naming Accuracy**  
Poor. "NEM vs GLD" or "OPERATING LEVERAGE" would be far clearer.

**Consolidation Candidate**  
Moderate candidate — could merge with tab 07·REL VAL as an additional comparison dimension, or be repositioned before tab 15·VERDICT.

---

### Tab 17 · COPPER

**Lines:** 7190–7458 (268 lines)

**Primary Content**  
Cadia copper profile: 2.9Mt copper reserve, 2025 production of ~385 Klb, AISC of ~$400/oz net of by-product credits. Per-share copper NAV calculation ($12–15/share at $4.50/lb long-run copper). Sensitivity table: copper NAV as a function of copper price ($3.00–$6.00/lb) and discount rate (8%–12%).

**Secondary Content**  
Copper supply-demand narrative (deficit outlook). AI/data center copper demand analysis (IEA: 512 kt by 2030, Goldman Sachs: 122 GW data center capacity by 2030, Trafigura CEO: up to 1Mt). Major bank copper price forecasts bar chart. Non-consensus view panel: "No sell-side analyst assigns standalone Cu NAV to NEM."

**UX Problems**
- Substantial duplication with tab 12·ALT DATA channel check #8, which covers the same AI data center copper demand findings, the same Microsoft Chicago data point, the same IEA/Goldman/Trafigura numbers. The tab contains new content (the NAV model and sensitivity table) but the contextual narrative is largely repeated.
- The tab references "our gold-focused DCF" and "our target" — implicit acknowledgment that the copper NAV is additive optionality not embedded in the base case DCF, which could confuse users who see a different number in tab 06·DCF.

**Naming Accuracy**  
Accurate.

**Consolidation Candidate**  
Weak candidate for consolidation — the copper NAV model is substantive and earns standalone treatment. The fix is to remove the duplicated AI demand narrative and replace it with a brief cross-reference to ALT DATA channel check #8.

---

### Tab 18 · MGMT

**Lines:** 7458–7595 (137 lines)

**Primary Content**  
CEO profile: Natascha Viljoen, appointed 2024. Career background, tenure, strategic priorities. Predecessor: Tom Palmer (2019–2023), associated with the Goldcorp acquisition and the post-integration production misses analyzed in tab 14·CREDIBILITY. Thesis connection: Viljoen's arrival marks the structural break in the credibility study.

**Secondary Content**  
Board composition and governance scorecard. Director independence breakdown. ESG-linked compensation structure (20% of incentive).

**UX Problems**
- An insight callout references "the 14-CREDIBILITY tab" for guidance/EPS historical data. This cross-reference is confusing in two ways: (1) the tab is labeled "14·CREDIBILITY" with a middle dot, not a dash, inconsistent with the reference; and (2) zero-indexed it is `tabs[13]`, so any programmer reading the code finds "Tab 14" pointing to `tabs[13]`.
- The governance data (board independence, ESG-linked pay) partially duplicates what is already in tab 13·ESG (board independence: 11/12, female directors: 42%, ESG-linked pay: 20%). Both tabs show the same numbers without cross-referencing each other.

**Naming Accuracy**  
"MGMT" is accurate but minimal. "MANAGEMENT" or "LEADERSHIP" would be clearer, especially for non-analyst audiences.

**Consolidation Candidate**  
Moderate — board governance data could move entirely to tab 13·ESG (where it fits naturally under the Governance sub-panel). This tab could then focus exclusively on the CEO/leadership thesis, which is thematically linked to tab 14·CREDIBILITY.

---

### Tab 19 · ROIC

**Lines:** 7595–7743 (148 lines)

**Primary Content**  
Return on Invested Capital calculation for NEM: ROIC formula, WACC comparison, and ROIC-minus-WACC spread (economic value creation). ROIC vs. WACC spread trend chart (2021–2025).

**Secondary Content**  
EVA (Economic Value Added) trend chart. ROIC calculation detail table (NOPAT, invested capital, components). Peer ROIC comparison (NEM vs. AEM vs. GOLD).

**UX Problems**
- ROIC is a financial quality metric that belongs logically with tab 04·PROFILE (financial health, Piotroski, Altman Z). Placing it at tab 19 — after VERDICT, after COPPER, after MGMT — severs it from the financial profile context and almost guarantees it will be missed.
- The WACC used in this tab should be identical to the WACC in tab 06·DCF, but there is no explicit cross-reference linking them. A user changing WACC in the DCF tab would not know to revisit this tab.

**Naming Accuracy**  
Accurate.

**Consolidation Candidate**  
Strong candidate — merge with tab 04·PROFILE. ROIC is a direct extension of the financial profile analysis.

---

### Tab 20 · QRTLY MODEL

**Lines:** 7743–8224 (481 lines)

**Primary Content**  
Forward quarterly model: Q1–Q4 2026 and H1 2027 revenue, EBITDA, EPS, and production estimates. EPS model vs. consensus comparison (model EPS materially above thin consensus due to gold price deck divergence). A quarterly production chart and quarterly EBITDA/EPS chart.

**Secondary Content**  
AISC trajectory by quarter. Bridge: model vs. consensus for FY2026E (tabular breakdown of the drivers of divergence). Quarterly notes and catalysts section. Mine-level production phasing. Reserve replacement analysis (in an expander).

**UX Problems**
- "QUARTERLY NOTES & CATALYSTS" section at the bottom of this tab duplicates content from tab 11·CATALYST. Catalysts appear in both a standalone tab and embedded here, with no obvious mechanism to keep them synchronized.
- The model vs. consensus bridge shows the primary divergence driver is the gold price deck assumption, which is the same explanation given in tab 06·DCF. The two tabs discuss the same source of model differentiation in isolation.
- At 481 lines, this tab is long relative to its purpose. A quarterly model with bridge analysis does not need 481 lines unless the catalyst and notes section is inflating it.
- Chart title "OUR EPS MATERIALLY ABOVE THIN CONSENSUS — GOLD PRICE DECK DIVERGENCE" uses possessive first-person voice embedded directly in a chart title (not just a label or callout).

**Naming Accuracy**  
"QRTLY MODEL" is accurate, though "QUARTERLY MODEL" spelled out would be more professional.

**Consolidation Candidate**  
- Quarterly notes and catalysts section → remove; cross-reference to tab 11·CATALYST  
- Reserve replacement analysis expander is appropriate — keep

---

## Recommended Final Tab List

The following proposes a rationalized 16-tab structure that eliminates redundancy, improves logical flow, and consolidates thin tabs without losing any analytical content.

| # | New Name | What Lives Inside |
|---|---|---|
| 01 | THESIS | Current STORY content minus Kill Criteria and Research Log. Research Log moves to collapsible expander. Kill Criteria moves to VERDICT. |
| 02 | CMD | Unchanged. Remove "What Has to Be True" scorecard — it is canonical in VERDICT. |
| 03 | GOLD | Unchanged structure. Ore grade + permitting section → collapsible. Central bank + ETF section → collapsible. |
| 04 | FINANCIALS | Current PROFILE content + ROIC tab content (merged). Piotroski/Altman stay as expanded detail here; CMD shows headline numbers only. |
| 05 | MINES | Unchanged. Add footnote anchor link at the top of the discrepancy note. |
| 06 | DCF | Unchanged structure. Assumption scorecard → collapsible expander. Stress buttons moved above heatmap. |
| 07 | PEERS | Current REL VAL comp sheet + peer strategy comparison section (pulled from bottom of REL VAL). AISC trajectory chart moved to GOLD tab. |
| 08 | RISK | Unchanged. Remove inline cross-references to STORY and ALT DATA. |
| 09 | MC SIM | Unchanged. Parameters + robustness notes → collapsible. Add plain-English one-paragraph summary at top. |
| 10 | CATALYST | Unchanged. Remove duplicate from QRTLY MODEL tab. |
| 11 | ALT DATA | All 8 channel checks wrapped in `st.expander()`. Non-consensus hero cards removed (they exist in CMD). |
| 12 | ESG | Unchanged. Move the $30T caveat to immediately follow first mention in the insight callout. |
| 13 | CREDIBILITY | Rename to TRACK RECORD for clarity. Unchanged content. |
| 14 | VERDICT | Unchanged content. Kill Criteria consolidated here (removed from THESIS). Gold sensitivity → collapsible. Convergence method notes → collapsible. |
| 15 | COPPER | Remove duplicated AI demand narrative; replace with cross-reference link to ALT DATA check #8. Keep NAV model and sensitivity table. |
| 16 | MGMT | Remove board governance data (it belongs in ESG). Keep CEO/predecessor narrative. |

**Tabs eliminated by consolidation:**  
- 16·GLD CMP → merge operating leverage section into PEERS tab as a comparison dimension  
- 10·RETURNS → merge into FINANCIALS tab  
- 19·ROIC → merged into FINANCIALS tab  

**Tabs renamed:**  
- 01·STORY → THESIS  
- 04·PROFILE → FINANCIALS  
- 07·REL VAL → PEERS  
- 14·CREDIBILITY → TRACK RECORD  
- 16·GLD CMP → merged  
- 18·MGMT → MGMT (keep, but drop board governance section to ESG)  
- 20·QRTLY MODEL → QUARTERLY (spell out)

---

## Collapsible Expander Candidates

The following sections should be wrapped in `st.expander()` or moved behind a disclosure control. The summary line (visible by default) is noted where applicable.

| Tab | Section | Suggested Expander Label |
|---|---|---|
| 01·STORY | Perplexity Research Log (8 threads) | "Research Methodology — 8 Perplexity Queries" |
| 03·GOLD | Ore grade decline + permitting timeline | "Why Gold Supply Cannot Respond" |
| 03·GOLD | Central bank purchases + ETF flow charts | "Demand Driver Detail" |
| 06·DCF | Assumption transparency scorecard (38 items) | "Full Assumption Transparency — 38 Inputs" |
| 06·DCF | DCF methodology note | "Methodology & Model Assumptions" |
| 07·REL VAL | Peer strategy comparison section | "Competitive Positioning — Peer Strategy" |
| 09·MC SIM | Simulation parameters table | "Simulation Parameters" |
| 09·MC SIM | Statistical robustness notes | "Statistical Robustness Notes" |
| 15·VERDICT | Gold price sensitivity table | "Gold × AISC Sensitivity Detail" |
| 15·VERDICT | 8-method convergence breakdown | "Valuation Method Convergence Detail" |
| 20·QRTLY MODEL | Reserve replacement analysis | Already in expander — keep |

---

## The 5 Biggest UX Problems

### 1. Kill Criteria Appear in Three Different Tabs

Kill Criteria — the four conditions that flip the rating to SELL — appear in full in tab 01·STORY, are referenced via the "What Has to Be True" scorecard in tab 02·CMD, and appear again in full in tab 15·VERDICT. There is no canonical source of truth. If a kill criterion is updated in the data layer, the analyst must remember to update prose in at least two locations. For users, seeing the same content in multiple locations raises the question of which version is current. Fix: one authoritative location (VERDICT), one brief reference in CMD with a link.

### 2. Non-Consensus Hero Cards Duplicated Across Two Tabs

The three non-consensus thesis cards (AISC Credibility Flip, Cadia Copper AI Play, Reverse DCF Gap) appear in identical visual treatment in both tab 02·CMD and at the top of tab 12·ALT DATA. These are not similar — they are the same content rendered twice. Because tab 12 is the research evidence tab, the cards at its top create the impression that the "findings" section begins with marketing copy rather than data. Fix: remove the hero cards from ALT DATA entirely. CMD is the correct home.

### 3. ALT DATA Channel Checks Have No Collapsibility

Eight channel checks — each 30–60 lines of HTML prose — are rendered as a continuous scroll with no expand/collapse mechanism. To reach the signal scorecard at the bottom, a user must scroll through 250+ lines of dense text. The signal ratings (STRONGLY BULLISH through BEARISH) are the analytical output; the full text is the supporting evidence. Reversing this hierarchy — showing the signal and a one-sentence summary, with full text behind an expander — would transform this tab from scroll-fatiguing to highly usable.

### 4. Tabs 16–20 Are Orphaned from the Guided Narrative

The navigation guide in tab 01·STORY ("Where to Go From Here") maps the user flow through tabs 2–15. Tabs 16 (GLD CMP), 17 (COPPER), 18 (MGMT), 19 (ROIC), and 20 (QRTLY MODEL) are not mentioned. They appear after the VERDICT, which signals to users that the analysis is complete. These five tabs contain material analytical content (copper NAV, management track record connection, ROIC, quarterly model) but are structurally positioned as afterthoughts. Fix: either integrate them into the pre-verdict flow (tabs 16 and 17 belong before VERDICT), or acknowledge them explicitly in the navigation guide.

### 5. Content Duplication Across Copper Tabs Erodes Source-of-Truth Trust

The AI/data center copper demand narrative — IEA 512kt, Goldman Sachs 122 GW, Trafigura 1Mt, Microsoft Chicago 20kt Cu — appears in substantively identical form in both tab 12·ALT DATA (channel check #8) and tab 17·COPPER. If the data changes, both locations must be updated. If they diverge, users reading both tabs will see two conflicting numbers for the same underlying fact. The same issue applies to the AISC beat analysis (in both CREDIBILITY and ALT DATA) and to the WACC/discount rate (in both DCF and ROIC) with no explicit synchronization mechanism. Fix: establish one canonical location per data point; use cross-references or a shared data layer for all others.

---

## Full First-Person Phrase Inventory

The following is every identifiable first-person phrase found in the dashboard — in labels, headlines, insight callouts, chart titles, body HTML text, and captions. Phrases are listed by tab and line number where identified.

### Tab 01 · STORY

| Line | Location | Phrase |
|---|---|---|
| 1177 | KPI tile label | `Our Target` |
| 1200 | Insight callout | `This is a first-person account of how I used Perplexity Computer to build a differentiated thesis` |
| 1200 | Insight callout | `Not a polished pitch deck — an honest research narrative, including the parts that scared me.` |
| 1211 | HTML prose | `I started where everyone starts: a DCF model that said Newmont was cheap.` |
| 1215 | HTML prose | `The interesting part came when I ran the model backward.` |
| 1215 | HTML prose | `I asked: what gold price does the market need to believe...` |
| 1220 | HTML prose | `I wanted to know if the market knew something I didn't, or if it was just wrong.` |
| 1255 | HTML prose | `So I ran 8 alternative data channel checks using Perplexity Computer` |
| 1259 | HTML prose | `I went to jobs.newmont.com expecting to find post-restructuring attrition` |
| 1260 | HTML prose | `Instead I found active hiring` |
| 1267 | HTML prose | `Consensus mean still trails our model` |
| 1275 | HTML prose | `This one I didn't expect.` |
| 1289 | HTML prose | `Around check #5, I found the stuff that made me uncomfortable.` |
| 1291 | HTML prose | `I pulled all 81 Form 4 filings.` |
| 1312 | HTML prose | `I built all four of these into the Risk tab.` |
| 1323–1324 | HTML prose | `Before I put any weight on forward guidance, I tested whether NEM management deserves the benefit of the doubt.` |
| 1324 | HTML prose | `I pulled 10 years of initial guidance vs. actual results` |
| 1337 | HTML prose | `I haircut our production estimate to 5.11 Moz` |
| 1357–1358 | HTML prose | `Everything I found says it won't.` |
| 1366 | Section header | `THE BEAR CASE I TOOK SERIOUSLY` |
| 1374 | HTML prose | `I agree it's cautionary.` |
| 1404 | Navigation text | `Scenario analysis including the alt-data risks I found.` |
| ~1540 | Section header | `I Spent a Week Figuring Out Whether That's Right. It Isn't.` |

### Tab 02 · CMD

| Line | Location | Phrase |
|---|---|---|
| 1662 | Code comment | `# THESIS STATEMENT — OUR VIEW VS. CONSENSUS` |
| 1665 | Section header | `OUR VIEW VS. CONSENSUS — THREE FALSIFIABLE NON-CONSENSUS CALLS` |
| 1669 | Column header | `OUR VIEW (DIFFERENTIATED)` |
| ~1700 | Chart/label | `our model` (in consensus comparison text) |
| ~1750 | Callout | `our target` (in Reverse DCF anchor callout) |

### Tab 03 · GOLD

| Line | Location | Phrase |
|---|---|---|
| 2135 | Chart title | `OUR $5,200 GOLD DECK IS CONSERVATIVE vs BANK FORECASTS ($5,720 AVG)` |

### Tab 04 · PROFILE

| Line | Location | Phrase |
|---|---|---|
| ~2610 | Insight callout | `Two years ago this was a bloated, post-acquisition mess` (implied editorial voice) |

### Tab 06 · DCF

| Line | Location | Phrase |
|---|---|---|
| 3144 | Assumption text | `from FY2026 AISC guidance ($50/oz incremental per our model)` |

### Tab 07 · REL VAL

| Line | Location | Phrase |
|---|---|---|
| 4614 | Chart annotation | `vs our model; MarketScreener` |

### Tab 10 · RETURNS

| Line | Location | Phrase |
|---|---|---|
| 5142 | Insight callout | `If the stock is mispriced, you're getting paid to wait` |
| 5142 | Insight callout | `[X]% dividend yield + [X]% buyback yield = [X]% total shareholder yield` (implied "you") |

### Tab 11 · CATALYST

| Line | Location | Phrase |
|---|---|---|
| ~5310 | Timeline annotation | `WE ARE HERE` |

### Tab 12 · ALT DATA

| Line | Location | Phrase |
|---|---|---|
| 5350 | Panel header | `THE THREE NON-OBVIOUS INSIGHTS — WHAT GOLDMAN DOESN'T HAVE IN THEIR MODEL` |
| 5355 | Section banner | `NON-CONSENSUS — FINDINGS A SELL-SIDE ANALYST AT GOLDMAN DOESN'T HAVE` |
| 5384 | HTML prose | `No sell-side model has published this implied gold calculation.` |
| 5412 | HTML prose | `Our model sits between consensus mean and Bernstein's high.` |
| ~5500 | HTML prose | `we stopped all work on the shaft infrastructure` (quoted from NEM; used as evidence) |
| ~5520 | HTML prose | `we monitor` (monitoring cadence language) |
| ~5525 | HTML prose | `WHEN WE'LL KNOW` (column header in resolution calendar) |

### Tab 14 · CREDIBILITY

| Line | Location | Phrase |
|---|---|---|
| 5862 | Section banner | `NON-CONSENSUS VIEW — THE AISC CREDIBILITY FLIP CONSENSUS HASN'T PRICED` |
| 5886 | Sub-header | `WHY THIS IS NON-CONSENSUS` |

### Tab 15 · VERDICT

| Line | Location | Phrase |
|---|---|---|
| ~6395 | Prose callout | `If you believe gold stays above $[X], NEM is undervalued.` |

### Tab 17 · COPPER

| Line | Location | Phrase |
|---|---|---|
| 7290 | HTML prose | `value beyond our target — this is free optionality not in the price.` |

### Tab 20 · QRTLY MODEL

| Line | Location | Phrase |
|---|---|---|
| 7841 | Panel header | `QUARTERLY EBITDA ($M) — OUR MODEL vs CONSENSUS TREND` |
| 7861 | Chart title | `OUR EPS MATERIALLY ABOVE THIN CONSENSUS — GOLD PRICE DECK DIVERGENCE` |
| 7901 | Panel header | `BRIDGE — OUR MODEL vs. CONSENSUS (FY2026E)` |
| 7908 | Column header | `OUR MODEL` |

---

*End of audit report. Total tabs reviewed: 20. Total lines reviewed: 8,224. No code changes were made.*
