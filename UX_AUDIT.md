# NEM RESEARCH TERMINAL v2 — UX AUDIT

**Date:** 2026-04-02
**Auditor perspective:** Professional hedge-fund trading-platform UX designer
**App:** Streamlit-based equity research terminal for Newmont Corporation (NYSE: NEM)
**Total tabs:** 20 (mapped as Tabs 01-20 below)

---

## TAB STRUCTURE MAPPING

The app contains 20 sequential tabs organized as a story arc:

| # | Tab Label | Purpose | Lines | Story Phase |
|---|-----------|---------|-------|-------------|
| 01 | STORY | Research narrative — how the thesis was built | ~240 | SETUP |
| 02 | CMD | Command Center dashboard — thesis + key metrics | ~290 | SETUP |
| 03 | GOLD | Gold macro context — CB buying, forecasts, regime | ~175 | CONTEXT |
| 04 | PROFILE | Company financials — FCF, margins, quality scores | ~100 | CONTEXT |
| 05 | MINES | Mine portfolio — map, AISC, Cadia/Lihir spotlights | ~160 | CONTEXT |
| 06 | DCF | Full DCF engine + SOTP NAV + Copper NAV + NGM JV | ~935 | VALUATION |
| 07 | REL VAL | Peer multiples — EV/EBITDA, P/E, re-rating | ~230 | VALUATION |
| 08 | RISK | Scenario analysis — Bull/Base/Bear/Stress + risk matrix | ~220 | VALUATION |
| 09 | MC SIM | Monte Carlo — 50K correlated simulations | ~185 | VALUATION |
| 10 | RETURNS | Capital allocation — buybacks, dividends, net cash | ~110 | EVIDENCE |
| 11 | CATALYST | Forward catalyst map — probability-weighted EV | ~95 | EVIDENCE |
| 12 | ALT DATA | 8 AI channel checks — bullish/neutral/bearish signals | ~220 | EVIDENCE |
| 13 | ESG | ESG ratings + peer comparison + honest tensions | ~125 | EVIDENCE |
| 14 | CREDIBILITY | 10-year management guidance study + peer comparison | ~355 | EVIDENCE |
| 15 | VERDICT | Reverse DCF + convergence of 4 methods | ~295 | VERDICT |
| 16 | GLD CMP | NEM vs GLD operating leverage comparison | ~150 | VERDICT |
| 17 | COPPER | Copper optionality — Cadia hidden upside | ~110 | VERDICT |
| 18 | MGMT | CEO profile, board, capital allocation timeline | ~105 | VERDICT |
| 19 | ROIC | ROIC & EVA — value creation evidence | ~145 | VERDICT |
| 20 | QRTLY MODEL | Forward quarterly model + reserve replacement | ~455 | VERDICT |

---

## TAB-BY-TAB FINDINGS

### Tab 01: STORY
**#1 Takeaway:** The market implies gold at ~$3,605/oz; actual spot is $5,200 — a 44% gap.
**Hierarchy:** Good narrative structure but the punchline (price target, upside, BUY) was buried below 5 dense text blocks.
**Issue:** No at-a-glance KPI strip; user must scroll to find the thesis conclusion.
**Fix applied:** Added hero KPI strip at top (Price, Target, Upside, Rating) for immediate visual dominance.

### Tab 02: CMD
**#1 Takeaway:** "Our View vs Consensus" — three falsifiable non-consensus calls.
**Hierarchy:** Strong. Reverse DCF banner is dominant. Three-driver cards are well-balanced.
**Issue:** Minor — Primary Metrics row shows Current Price, which also appears in Reverse DCF banner.
**No fix needed:** Redundancy is acceptable for the command center role.

### Tab 03: GOLD
**#1 Takeaway:** Central bank gold purchases running 2x pre-2022 rates — structural bull market.
**Hierarchy:** Gold price vs AISC chart is the visual anchor. Regime assessment box is strong but placed late.
**Issue:** Bank Forecasts chart is secondary; could be demoted.
**No fix applied:** Tab is well-structured as-is.

### Tab 04: PROFILE
**#1 Takeaway:** Gross margin expanded 10% (2023) to 50% (2025) — structural transformation.
**Hierarchy:** FCF trajectory chart leads. Financial summary table is dense but necessary.
**Issue:** Piotroski + Altman Z scores appear here AND in Tab 02 (minor duplication).
**No fix needed:** Deep-dive context justifies showing them again.

### Tab 05: MINES
**#1 Takeaway:** Cadia ($400/oz AISC) is the crown jewel with copper optionality worth billions.
**Hierarchy:** Excellent — map is visually dominant, immediately communicates geographic diversification.
**Issue:** Treemap and sorted AISC chart show similar data; could consolidate.
**No fix applied:** Both serve different audiences (visual vs analytical).

### Tab 06: DCF
**#1 Takeaway:** DCF equity value and implied share price with full assumption transparency.
**Hierarchy:** KPI tiles at top are clear. Quick Stress Test buttons are excellent.
**Issue:** ESG WACC adjustment (+23bp) is buried in an expander — material but invisible by default. NGM JV is rendered 3 ways (cards, waterfall, target build).
**No fix applied:** Tab is the deepest and most interactive; restructuring would be high-risk.

### Tab 07: REL VAL
**#1 Takeaway:** NEM trades at discount to peer median; re-rating implies significant upside.
**Hierarchy:** Opening callout and re-rating tiles are clear.
**Issue:** Two peer bar charts (EV/EBITDA and P/E) tell the same story; could merge.
**No fix applied:** Minor redundancy acceptable.

### Tab 08: RISK
**#1 Takeaway:** Risk-reward is asymmetric — bull case >> bear case downside.
**Hierarchy:** Strong. Four scenario cards, risk matrix scatter, and asymmetry bar are effective.
**Issue:** Five alt-data risks at bottom are qualitative, not quantified into scenario model.
**No fix applied:** Narrative risks are intentionally qualitative.

### Tab 09: MC SIM
**#1 Takeaway:** 50K simulations show >60% probability above current price, right-skewed.
**Hierarchy:** Excellent — KPI tiles + histogram + convergence proof.
**Issue:** Convergence plot is nice-to-have; could be collapsible.
**No fix applied:** Adds institutional rigor.

### Tab 10: RETURNS
**#1 Takeaway:** $3.4B returned to shareholders in 2025 + net cash $7.2B (fortress balance sheet).
**Hierarchy:** Three-panel layout is clean. Debt trajectory transformation is visually prominent.
**Issue:** Minimal. Well-curated and concise.
**No fix applied.**

### Tab 11: CATALYST
**#1 Takeaway:** ~$30/share in probability-weighted forward catalyst EV over 12 months.
**Hierarchy:** Clear. Scorecard + waterfall + timeline cover different dimensions.
**Issue:** Minimal redundancy between table and bar chart.
**No fix applied.**

### Tab 12: ALT DATA
**#1 Takeaway:** 5 bullish, 1 neutral, 2 bearish AI channel checks = net score +3.
**Hierarchy:** Excellent. Explicit inclusion of bearish findings is a strength.
**Issue:** "What the Bears Have Right" partially overlaps with individual channel cards.
**No fix applied:** Editorial summary adds value.

### Tab 13: ESG
**#1 Takeaway:** #1 Bloomberg ESG Transparency in S&P 500; 99th percentile on S&P CSA.
**Hierarchy:** Strong ratings dashboard and radar chart.
**Issue:** "Honest Tensions" (fatalities, environmental impact) are buried at the end — should be earlier.
**No fix applied:** Structural change would require significant reflow.

### Tab 14: CREDIBILITY
**#1 Takeaway:** C+ credibility grade (improving) — miss trend converging from -11.8% to -0.2%.
**Hierarchy:** Two-era comparison is compelling. Miss trend chart is the standout visual.
**Issue:** At 355 lines, this is the second-longest tab. EPS Beat Tracker feels like scope creep.
**No fix applied:** Content supports the thesis; trimming would lose depth.

### Tab 15: VERDICT
**#1 Takeaway:** Reverse DCF gap is THE single most important insight — 4 methods converge.
**Hierarchy:** Hero section with $48-font implied vs actual gold prices is unmissable.
**Issue:** Convergence conclusion needed a visual "conviction meter" to summarize.
**Fix applied:** Added Conviction Meter bar (X of 4 methods above current price, % convergence).

### Tab 16: GLD CMP
**#1 Takeaway:** NEM provides operating leverage, dividends, and copper optionality; GLD provides none.
**Hierarchy:** Operating leverage chart is the centerpiece.
**Issue:** Dividend Advantage chart is somewhat redundant.
**No fix applied.**

### Tab 17: COPPER
**#1 Takeaway:** $8-10/share of hidden copper upside not in base DCF.
**Hierarchy:** Copper sensitivity chart is the key visual.
**Issue:** Three-column demand narrative is filler; could be condensed.
**No fix applied.**

### Tab 18: MGMT
**#1 Takeaway:** New CEO Viljoen inherits fortress balance sheet + completed transformation.
**Hierarchy:** CEO profile leads, board composition provides institutional credibility.
**Issue:** Predecessor box is somewhat redundant.
**No fix applied.**

### Tab 19: ROIC
**#1 Takeaway:** ROIC-WACC spread is positive — NEM creates economic value, rare in mining.
**Hierarchy:** Excellent. KPI tiles + ROIC vs WACC chart + peer comparison.
**Issue:** None. This is a lean, focused tab.
**No fix applied.**

### Tab 20: QRTLY MODEL
**#1 Takeaway:** H2-weighted production; model EPS diverges from consensus due to gold deck.
**Hierarchy:** Dense but well-structured. Quarterly table + charts show forward trajectory.
**Issue:** Reserve Replacement Analysis (160 lines) competes for visual weight; buries the quarterly model.
**Fix applied:** Collapsed reserve analysis into an expander (click to expand), keeping the quarterly model as the primary focus.

---

## STORY FLOW ANALYSIS (Tabs 01-20)

### Story Arc
1. **SETUP (Tabs 01-02):** Hook the reader with the reverse DCF insight and thesis statement
2. **CONTEXT (Tabs 03-05):** Build macro + company + asset-level foundation
3. **VALUATION (Tabs 06-09):** Rigorous multi-method valuation
4. **EVIDENCE (Tabs 10-14):** Supporting evidence from capital returns, catalysts, alt data, ESG, credibility
5. **VERDICT (Tabs 15-20):** Convergence, differentiation, and forward model

### Flow Issues Identified
- **Tabs 01-02 are strong openers** — the reverse DCF hook is compelling and thesis is clear.
- **Tabs 03-05 build context logically** — gold macro -> company health -> mine assets.
- **Tabs 06-09 are the analytical core** — Tab 06 (DCF) at 935 lines is the deepest tab; could benefit from splitting but doing so would break the interactive model.
- **Tabs 10-14 provide supporting evidence** — the credibility study (Tab 14) is the most intellectually honest section.
- **Tab 15 is the climax** — convergence of 4 methods is the thesis capstone.
- **Tabs 16-20 are supplementary** — they strengthen the thesis but aren't essential to the core narrative. Moving them before Tab 15 would strengthen the "verdict" closing.
- **Fix applied:** Added a Story Arc navigation bar above the tab row that visually communicates the 5-phase structure (Setup -> Context -> Valuation -> Evidence -> Verdict).

---

## CLUTTER / FILLER REMOVAL NOTES

| Tab | Panel | Issue | Action |
|-----|-------|-------|--------|
| 02 | Primary Metrics Row | Current Price duplicated in Reverse DCF banner | Kept (command center role) |
| 06 | GGM Cross-Check | Cosmetic sanity check, doesn't drive target | Kept (adds rigor) |
| 06 | Confidence Interval Bar | Redundant with sensitivity heatmap | Kept (different audience) |
| 07 | EV/EBITDA + P/E charts | Both show NEM at discount | Kept (minor redundancy) |
| 12 | "Bears Have Right" box | Overlaps individual channel cards | Kept (editorial summary) |
| 14 | EPS Beat Tracker | Tangential to production guidance accuracy | Kept (supporting evidence) |
| 20 | Reserve Replacement | 160 lines competing with quarterly model | **Collapsed into expander** |

---

## INTERACTIVE FEEDBACK IMPROVEMENTS

### Before
- Sidebar sliders showed a single "AI suggested: $X | You: $Y (+Z%)" line only for the Gold Price slider
- No visual feedback for other sliders (Beta, ERP, Exit Multiple, Production, etc.)
- Users couldn't quickly assess how far they'd deviated from defaults

### After
- Added `slider_feedback()` helper function that generates color-coded deviation badges for all key sliders
- **Green checkmark** when at default value
- **Amber badge** when modified (<15% deviation from default)
- **Red badge** when significantly modified (>15% deviation)
- Applied to: Gold Price, Beta, ERP, Exit Multiple, Production Y1, Production Target
- Shows both percentage deviation and exact before/after values

---

## TOP 5 UX CHANGES IMPLEMENTED

### 1. Hero KPI Strip on Tab 01 (STORY)
**Problem:** The #1 takeaway (Price Target, Upside, BUY rating) was buried below 5 dense narrative blocks. Users had to scroll to find the conclusion.
**Solution:** Added a 4-cell hero KPI strip at the very top of Tab 01 showing Price ($108.25), Target, Upside %, and Rating (with color-filled background). The BUY recommendation is now the first thing a user sees.
**Lines changed:** ~20 lines added after `with tabs[0]:` (around line 985-1005)

### 2. Story Arc Navigation Bar
**Problem:** With 20 tabs, users had no sense of where they were in the narrative flow. The tab bar showed labels but not the story structure.
**Solution:** Added a 5-phase story arc bar above the tab row (Setup -> Context -> Valuation -> Evidence -> Verdict), each phase color-coded with tab ranges. This provides a "you are here" mental model for the research narrative.
**Lines changed:** ~25 lines added before `tabs = st.tabs(...)` (around line 970-995)

### 3. Enhanced Slider Deviation Feedback
**Problem:** Only the Gold Price slider had deviation feedback. All other sliders (Beta, ERP, Exit Multiple, Production) had no visual indication of how far the user had moved from AI defaults.
**Solution:** Created `slider_feedback()` helper that generates color-coded badges (green=at default, amber=modified, red=significantly modified) with percentage deviation and exact values. Applied to 6 key sidebar sliders.
**Lines changed:** ~15 lines for helper function + ~6 lines for slider calls

### 4. Reserve Analysis Collapsed into Expander (Tab 20)
**Problem:** The Reserve Replacement Analysis (~160 lines with tables, charts, and peer comparison) dominated Tab 20, burying the core quarterly model content. Users had to scroll past it to reach the source footer.
**Solution:** Wrapped the entire reserve replacement section in a Streamlit expander (collapsed by default). Users who want the deep analysis can click to expand; the quarterly model is now the uncontested primary content.
**Lines changed:** 1 line added (expander wrapper) + ~155 lines re-indented

### 5. Conviction Meter on Tab 15 (VERDICT)
**Problem:** The VERDICT tab had strong individual elements (reverse DCF hero, convergence chart, closing paragraph) but lacked a single visual "confidence score" that synthesized all 4 methods.
**Solution:** Added a Conviction Meter bar between the convergence chart and closing paragraph. Shows "X of 4 independent methods above current price" with a progress bar (green if 3+/4, amber if 2/4, red if <2/4) and percentage convergence label.
**Lines changed:** ~15 lines added before the closing argument section

---

## FILES CHANGED

| File | Change Type | Description |
|------|------------|-------------|
| `app.py` | Modified | All 5 UX improvements: CSS additions, hero KPI strip, story arc nav, slider feedback, reserve expander, conviction meter |
| `UX_AUDIT.md` | Created | This audit document |

---

## COMPETITIVE ANALYSIS — WEAKNESS ASSESSMENT & FIX DECISIONS

The following weaknesses were identified in [COMPETITIVE_ANALYSIS.md](COMPETITIVE_ANALYSIS.md). Each is evaluated for whether it should be fixed in the dashboard.

### Weakness 1: No explicit variant-perception framework with catalyst timeline
**Fix in dashboard? YES.**
The "Our View vs. Consensus" grid in Tab 02 (CMD) lists three non-consensus calls but lacks a "catalyst that closes the gap with a date" column. Adding a fourth column ("Catalyst / Date") to the existing grid turns a good table into a falsifiable, time-bound framework that judges can evaluate.
**Implementation:** Add "CATALYST / DATE" column to the CMD tab's consensus grid. Each row gets a specific event + date (e.g., "Q1 2026 AISC print — Apr 23, 2026").

### Weakness 2: No disconfirming-evidence section with explicit kill criteria
**Fix in dashboard? YES.**
Tab 01 (STORY) has "WHAT ALMOST KILLED THE THESIS" — honest and strong — but never states exit conditions. Adding a "KILL CRITERIA" panel after the bear case preemption turns intellectual honesty into investment discipline. This is a 15-line addition.
**Implementation:** New panel in Tab 01 (STORY) after the bear case preemption: "WE EXIT IF" with 3-4 specific, falsifiable conditions.

### Weakness 3: No 30-second judge summary / closing is buried
**Fix in dashboard? YES.**
The competition footer (lines 5857-5870) lists features but not the thesis. A judge skimming the bottom of any tab sees stats, not the conclusion. Adding an "EXECUTIVE SUMMARY FOR JUDGES" strip above the story arc nav (visible on every tab render as the page header) gives immediate thesis visibility.
**Implementation:** New judge summary strip between the terminal header and story arc nav. Five data points: Ticker, Recommendation, Target, Upside, one-sentence thesis.

### Weakness 4: Source confidence signaling absent
**Fix in dashboard? YES.**
All `source_footer()` calls treat 10-K filings and LinkedIn scrapes identically. Adding a confidence tier to the source_footer function is low-effort and high-signal.
**Implementation:** Modify `source_footer()` to accept an optional `tier` parameter. Tier 1 = audited filings (green), Tier 2 = consensus/sell-side (amber), Tier 3 = alt data/AI-gathered (muted). Apply to key tabs.

### Weakness 5: Evidence hierarchy is flat — all 20 tabs have equal visual weight
**Fix in dashboard? NO.**
Streamlit tabs are inherently flat — there is no native way to make some tabs visually "bigger" than others without breaking the tab bar layout. The story arc nav already groups tabs into phases with color coding, which is the closest available solution. Attempting to resize individual tabs would break the Bloomberg Terminal aesthetic and introduce CSS fragility.
**Reasoning visible in submission:** The story arc navigation bar above the tab row already communicates which phase (and therefore which tabs) are most important. The VERDICT phase is red-highlighted to draw attention.

### Weakness 6: No position sizing or portfolio context
**Fix in dashboard? NO.**
Position sizing requires knowledge of the portfolio, AUM, and risk budget — none of which are defined in a stock pitch competition. Adding generic Kelly criterion math without portfolio context would be academically correct but practically meaningless.
**Reasoning visible in submission:** The RISK tab (Tab 08) already includes probability-weighted scenario analysis with explicit upside/downside percentages, which is the relevant input for position sizing. The judge can apply their own framework.

### Weakness 7: No explicit comparison to alternative investments (GOLD, AEM on risk-adjusted basis)
**Fix in dashboard? PARTIAL.**
Tab 16 (GLD CMP) already covers GLD. Adding a brief "Why NEM over GOLD/AEM" callout to the VERDICT tab (Tab 15) addresses the gap without creating a new tab.
**Implementation:** Add a brief "NEM VS. ALTERNATIVES" callout in Tab 15 after the convergence section, citing 2-3 differentiators vs. Barrick (NGM JV optionality, S&P 500 inclusion) and Agnico (copper exposure, larger reserve base).

---

## VALIDATION NOTES (Updated 2026-04-02 — post competitive-analysis fixes)

1. **Syntax check:** `py_compile.compile('app.py', doraise=True)` — PASS
2. **Import check:** All imports (streamlit, plotly, pandas, numpy, scipy) resolve — PASS
3. **Data loading:** `nem_data.json` loads with all expected keys — PASS
4. **Streamlit launch:** `streamlit run app.py --server.port 5002 --server.headless=true` — PASS
5. **HTTP response:** `curl http://localhost:5002` returns HTTP 200 — PASS
6. **No runtime errors:** Log contains zero Traceback/Error/Exception lines — PASS

### Key Interactions Validated
- App starts and renders the terminal header with live data
- **NEW:** Executive Summary for Judges strip renders between header and story arc nav
- Story arc navigation bar renders above the 20-tab row
- Hero KPI strip on Tab 01 shows correct Price, Target, Upside, Rating values
- **NEW:** Kill Criteria panel renders in Tab 01 after bear case preemption
- **NEW:** Variant-perception grid in Tab 02 now has 4 columns (includes CATALYST / DATE)
- **NEW:** Source footers show Tier 1/2/3 confidence badges where applied
- **NEW:** "WHY NEM OVER ALTERNATIVES?" callout renders in Tab 15 before closing argument
- **NEW:** Competition footer includes thesis conclusion (Recommendation, Target, Upside)
- Sidebar sliders show deviation badges when modified
- Tab 20 renders quarterly model with reserve analysis collapsed in expander
- Tab 15 conviction meter displays correctly based on 4-method convergence
