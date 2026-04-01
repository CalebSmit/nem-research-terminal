# NEM DASHBOARD — FINAL REVIEW & QA PLAN

## The Last Pass Before Submission: Find Everything That's Wrong and Fix It

---

# ═══════════════════════════════════════════════════════════════
# AUDIT 1: MATHEMATICAL INTEGRITY
# ═══════════════════════════════════════════════════════════════

Go through every calculation in the dashboard and verify it is correct. Do not assume anything is right just because it looks reasonable. Actually check the math.

## DCF Model:
- [ ] Revenue Year 1 = Gold Price × Production (Moz) + Other Revenue. Manually verify.
- [ ] Revenue Years 2-5: does gold price escalate at the stated rate? Does production follow the stated ramp? Does other revenue grow at the stated CAGR? Verify each year independently.
- [ ] COGS = Revenue × COGS% for each year. Verify the percentage matches what the assumption panel says.
- [ ] EBIT = Revenue − COGS − R&D − SGA − Other OpEx. Verify for each year.
- [ ] NOPAT = EBIT × (1 − tax rate). Verify the tax rate matches the stated assumption.
- [ ] FCFF = NOPAT + D&A − CapEx − ΔWC. Verify each component for each year.
- [ ] Discount factors: are they computed using mid-year convention? Is the stub period adjustment correct for the partial first year? Show your work — what is the exact discount exponent for each year?
- [ ] PV of each year's FCFF = FCFF ÷ (1 + WACC)^(period). Verify each.
- [ ] Total PV of FCFs = sum of individual PVs. Verify the addition.
- [ ] Terminal Value = Year 5 EBITDA × Exit Multiple. Verify EBITDA Year 5 is correct and the multiple matches the assumption.
- [ ] PV of Terminal Value = TV ÷ (1 + WACC)^(Year 5 period). Verify.
- [ ] Enterprise Value = Total PV of FCFs + PV of Terminal Value. Verify.
- [ ] Equity Value = EV − Minority Interest − Total Debt + Cash. Verify each component matches the balance sheet data. Check signs — debt is subtracted, cash is added.
- [ ] Implied Price = Equity Value ÷ Diluted Shares. Verify shares outstanding is current.
- [ ] Upside % = (Implied Price ÷ Current Price − 1) × 100. Verify current price is live/recent.

## Gordon Growth Cross-Check:
- [ ] TV_GGM = Year 5 FCFF × (1 + g) ÷ (WACC − g). Verify.
- [ ] Implied exit multiple from GGM = TV_GGM ÷ Year 5 EBITDA. Verify.
- [ ] Is the GGM-implied multiple HIGHER than the applied exit multiple? If yes, the terminal value is conservative — this should be explicitly stated. If no, something may be wrong with the growth rate or WACC.

## WACC:
- [ ] Ke = Rf + β × ERP. Verify each component and the arithmetic.
- [ ] Pre-tax Kd = Rf + Default Spread. Verify the ICR, the synthetic rating lookup, and the spread.
- [ ] After-tax Kd = Pre-tax Kd × (1 − tax rate). Verify.
- [ ] Weights: equity weight = market cap ÷ (market cap + debt); debt weight = 1 − equity weight. Verify market cap = price × shares.
- [ ] WACC = Ke × We + Kd(1−t) × Wd. Verify.
- [ ] Does the WACC displayed everywhere in the dashboard (sliders, assumption panels, sensitivity matrix, Monte Carlo) match the calculated WACC? No inconsistencies.

## P/NAV:
- [ ] Gold deck: is it actually the trailing 2-year average spot? Verify the calculation window and the average.
- [ ] Cash margin = gold deck − AISC. Verify AISC matches the most recent FY actual.
- [ ] Annual production = P&P reserves ÷ mine life. Verify reserves and mine life sources.
- [ ] Annual OCF = cash margin × annual production. Verify.
- [ ] Annuity factor = [1 − (1 + r)^(−n)] ÷ r. Verify with the stated discount rate and mine life.
- [ ] Gross NAV = OCF × annuity factor. Verify.
- [ ] Equity NAV = Gross NAV + net cash. Verify net cash = cash − debt from balance sheet.
- [ ] NAV/share = Equity NAV ÷ diluted shares. Verify.
- [ ] Implied price = NAV/share × target multiple. Verify the multiple and its justification.

## Blended Target:
- [ ] Blended = (DCF weight × DCF price) + (P/NAV weight × P/NAV price). Verify weights sum to 100%.
- [ ] Does the blended target on the Command Center match this calculation exactly?

## Sensitivity Matrix:
- [ ] Pick 3-5 random cells in the sensitivity heatmap. For each, manually compute: at that WACC and that exit multiple, what is the implied price? Does it match the cell value?
- [ ] Is the base case cell (your calculated WACC and peer median multiple) highlighted/bolded?
- [ ] Is the count "X of Y cells exceed current price" correct? Count manually for at least one row.

## Scenario Analysis:
- [ ] For each of the 4 scenarios: does the gold price assumption, production, and AISC match what's stated?
- [ ] Is the DCF re-run correctly for each scenario? Spot-check the Bear case: is the implied price reasonable given the gold assumption?
- [ ] Do the blended targets correctly apply the 70/30 DCF/P/NAV weights?
- [ ] Are the ratings (BUY/HOLD/SELL) assigned correctly based on upside/downside thresholds?

## Monte Carlo:
- [ ] Is the gold price distribution correctly parameterized? Does the ~5th percentile roughly correspond to the bear gold scenario and the ~95th to the bull?
- [ ] Is the gold-multiple correlation actually implemented? Test: in the simulation output, are high gold prices associated with high multiples? If gold and multiples appear uncorrelated in the output, the correlation is broken.
- [ ] Is WACC independently sampled? Test: is WACC distribution symmetric and unrelated to gold in the output?
- [ ] Is P/NAV held constant in every iteration?
- [ ] Does the median of the simulation approximately match the base case DCF blended target? They should be in the same neighborhood. If the median is dramatically different, something is wrong.
- [ ] Is the probability calculation correct? P(exceeds current price) = count of iterations above current price ÷ total iterations.
- [ ] Are the reported percentiles (P10, P25, P50, P75, P90) consistent with the histogram shape?

## Reverse DCF:
- [ ] The implied gold price should produce a DCF equity value ≈ current market cap. Verify: plug the implied gold back into the revenue model → FCFF → DCF. Does it return approximately the current price?
- [ ] Is the implied gold price below current spot? It MUST be for the thesis to work. If it's not, something is wrong with the model.

## Other Calculations:
- [ ] Piotroski F-Score: verify each of the 9 criteria against the financial data. Are comparisons (YoY changes) computed correctly?
- [ ] Altman Z-Score: verify the formula: 1.2×(WC/TA) + 1.4×(RE/TA) + 3.3×(EBIT/TA) + 0.6×(MktCap/TL) + 1.0×(Rev/TA). Are all components from the correct period?
- [ ] Gold Beta: is the regression run on the correct data (NEM returns vs gold returns)? Is the reported β the slope coefficient? Is R² reported correctly?
- [ ] ROIC = NOPAT ÷ Invested Capital. Verify invested capital = total equity + net debt.
- [ ] EVA = (ROIC − WACC) × Invested Capital. Verify.

---

# ═══════════════════════════════════════════════════════════════
# AUDIT 2: ASSUMPTION TRANSPARENCY & OVERRIDES
# ═══════════════════════════════════════════════════════════════

## For EVERY input in the dashboard, verify:

- [ ] **Justification exists:** click on or expand every assumption. Is there a clear explanation of what the value is, why it was chosen, where the data came from, and the as-of date? If any input is an orphan number with no explanation, fix it.

- [ ] **Override works:** change the value. Does the model recalculate? Does the output change in the expected direction? (e.g., raising WACC should lower the implied price; raising gold should raise it.) If any input is frozen or doesn't propagate, fix it.

- [ ] **Reset works:** click "Reset to AI-Suggested." Does the input snap back to the original value? Does the model recalculate to match the original output? Test at per-section level and global level.

- [ ] **Modified indicator shows:** change an input. Is it visually flagged as modified (accent border, "✎ Modified" badge, or similar)? Reset it — does the flag disappear?

- [ ] **No contradictions:** if the user overrides gold price in the sidebar master slider, does it also update in the DCF tab's gold price slider? In the Build Your Own Thesis panel? Are all representations of the same input synchronized?

## Specific override propagation tests:

- [ ] Change the gold price master slider. Verify that ALL of the following update:
  - DCF implied price
  - P/NAV implied price (cash margin changes)
  - Blended target
  - Command Center KPI tiles
  - Breakeven buffer in Risk Engine
  - GLD comparison scenario table
  - Revenue bridge table in DCF

- [ ] Change the WACC slider. Verify:
  - DCF implied price changes
  - Sensitivity matrix base case cell shifts
  - Blended target updates
  - The WACC displayed in the WACC build-up panel matches the slider

- [ ] Change the terminal multiple. Verify:
  - Terminal value changes
  - DCF implied price changes
  - Sensitivity matrix column labels or base case cell shifts

- [ ] Change scenario probability weights. Verify:
  - Probability-weighted expected value on Thesis tab updates
  - Risk-reward ratio updates (if built)

- [ ] Set EVERY input to an extreme value (gold = minimum, WACC = maximum, multiple = minimum). Does the model still function without crashing? Does it produce a negative or very low implied price? That's correct — the model should be honest even under extreme assumptions. Is the recommendation SELL in this case?

- [ ] Hit global "Reset All to AI-Suggested." Does every single input return to default? Does the dashboard look exactly like it did before any modifications?

---

# ═══════════════════════════════════════════════════════════════
# AUDIT 3: DATA FRESHNESS & SOURCING
# ═══════════════════════════════════════════════════════════════

- [ ] **NEM stock price:** is it from today or the most recent trading day? Check the timestamp.
- [ ] **Gold spot price:** is it current? Does it match a reliable source (Kitco, CME, Bloomberg)?
- [ ] **10Y Treasury yield:** is it current? Check against FRED or similar.
- [ ] **Peer stock prices and multiples:** are they from the same date? Stale peer data with fresh NEM data creates inconsistencies.
- [ ] **NEM financials:** are they from the most recent annual or quarterly filing? Is there a newer filing available that you missed?
- [ ] **Bank gold forecasts:** are these the most recent forecasts, or are they stale? Banks update gold targets frequently. Check dates.
- [ ] **Central bank gold purchase data:** is it the most recent available from the World Gold Council or similar?
- [ ] **ESG ratings:** are these current? MSCI and Sustainalytics update periodically.
- [ ] **Mine-level data:** is it from the most recent annual report or investor presentation? Is there a more recent quarterly update?
- [ ] **Every source footer:** does every panel show "Source: [name] | As of [date]"? Is any panel missing a source?

---

# ═══════════════════════════════════════════════════════════════
# AUDIT 4: DESIGN SYSTEM COMPLIANCE
# ═══════════════════════════════════════════════════════════════

Go through every tab and every element. This must be pixel-perfect.

## Colors:
- [ ] Background is #0d1117 everywhere. No white backgrounds. No light grey backgrounds. Check chart areas, table backgrounds, dropdown menus, slider tracks, tooltip backgrounds.
- [ ] Panel surfaces are #161b22. Check every card, every panel, every chart container.
- [ ] Borders are #30363d, 1px solid. No thick borders, no colored borders (except accent for modified inputs).
- [ ] Text is #e6edf3 (primary) and #8b949e (muted/labels). No black text anywhere.
- [ ] Green (#3fb950) is used ONLY for positive values. Red (#f85149) ONLY for negative. Amber (#d29922) ONLY for warnings/neutral. Blue (#58a6ff) ONLY for KPI values and data accents. No color misuse.

## Typography:
- [ ] Every piece of text is monospace. Check: chart annotations, axis labels, tooltips, button labels, slider labels, dropdown options. No sans-serif or serif fonts anywhere.
- [ ] KPI values are large (28px), bold, accent blue.
- [ ] Panel titles are 11px, uppercase, letter-spaced, muted.
- [ ] Table headers are 10px, uppercase, muted.

## Layout:
- [ ] border-radius is 0 on EVERYTHING. Check: buttons, input fields, sliders, cards, charts, tooltips, dropdowns. Absolutely nothing is rounded.
- [ ] No shadows anywhere. No gradients anywhere. No decorative elements.
- [ ] Charts use the dark Plotly template with #161b22 backgrounds and #30363d gridlines. No default Plotly light theme leaking through.

## Formatting:
- [ ] Dollar amounts per share: $XXX.XX with 2 decimal places. Not $XXX or $XXX.XXXX.
- [ ] Dollar amounts in millions: $XX,XXXM with commas. Not "23400M" — must be "$23,400M."
- [ ] Percentages: XX.X% with 1 decimal. Not "5.623%" or "6%".
- [ ] Multiples: X.XX× with the × symbol. Not "9.68x" — must be "9.68×."
- [ ] Negative numbers: ($X,XXX) in red with parentheses. Not "-$X,XXX."
- [ ] Numbers in tables are right-aligned. Text is left-aligned.
- [ ] Commas in thousands. "$7,300M" not "$7300M."
- [ ] Production: X.XX Moz. Not "5.9" or "5,900 koz" — must be "5.90 Moz."

---

# ═══════════════════════════════════════════════════════════════
# AUDIT 5: CONTENT COMPLETENESS
# ═══════════════════════════════════════════════════════════════

## Verify every tab exists and has content:
- [ ] Tab 1: Command Center — KPIs, thesis drivers, valuation bridge, sparklines
- [ ] Tab 2: Gold Macro — price chart, demand drivers, bank forecasts, beta, regime detection
- [ ] Tab 3: Company Profile — financials, FCF, earnings beats, AISC comparison, Piotroski, Altman Z
- [ ] Tab 4: Mine Portfolio — world map, mine table, AISC bar chart, Cadia/Lihir spotlights
- [ ] Tab 5: DCF Engine — full model, sliders, sensitivity heatmap, WACC build-up, GGM cross-check
- [ ] Tab 6: Relative Value — peer table, discount/premium bars, scatter plot, P/NAV build, P/NAV sensitivity
- [ ] Tab 7: Risk Engine — scenario toggle, risk matrix, breakeven, asymmetry, bear compounding narrative
- [ ] Tab 8: Monte Carlo — histogram, CDF, tornado, assumption table, convergence plot
- [ ] Tab 9: Capital Returns — FCF allocation, debt paydown, share count, dividend coverage
- [ ] Tab 10: Catalyst Map — Gantt timeline, impact quantification, expected value summary
- [ ] Tab 11: ESG & Stewardship — ratings, environment, social, governance, honest tensions, stewardship framing
- [ ] Tab 12: Thesis Verdict — three drivers, valuation bridge, REVERSE DCF, probability-weighted EV, final verdict box

## Verify new features from the improvement plan:
- [ ] "Why Not Just Buy GLD?" panel exists with NEM vs GLD comparison, operating leverage chart, scenario table
- [ ] Copper Optionality panel exists with production data, sensitivity table, deficit thesis
- [ ] Management Credibility section exists with guidance vs actuals, earnings accuracy
- [ ] ROIC / EVA section exists with multi-year trend and peer comparison
- [ ] Reserve Replacement metrics exist (replacement ratio, reserve life, depletion-adjusted FCF)
- [ ] SOTP / Acquisition Premium exists with mine-level valuation and precedent transactions
- [ ] Gold Supply-Demand exists with supply/demand balance chart
- [ ] Quick Stress buttons exist on the DCF tab
- [ ] "What the Market is Missing" callout exists on every tab

---

# ═══════════════════════════════════════════════════════════════
# AUDIT 6: THE REVERSE DCF — SPECIAL ATTENTION
# ═══════════════════════════════════════════════════════════════

The Reverse DCF is the single most important insight on the dashboard. It deserves its own audit.

- [ ] Is it on the Thesis Verdict tab (Tab 12)?
- [ ] Is it visually prominent — not buried at the bottom, not in small text?
- [ ] Does the calculation make sense? The implied gold price should be the price at which DCF equity value = current market cap.
- [ ] Is the implied gold price SIGNIFICANTLY below current spot? (If not, the thesis collapses. Investigate.)
- [ ] Is the gap between implied and actual gold clearly stated as a percentage?
- [ ] Is the framing clear? Something like: "At $[price], the market is pricing gold at $[implied] — [X]% below spot of $[spot]. The gap is the opportunity."
- [ ] Is there ALSO a P/NAV version? ("At what gold deck does NAV/share = current price?")
- [ ] Do both methods (DCF-implied and P/NAV-implied gold) tell a consistent story?
- [ ] If the user changes the gold price master slider to match the implied gold price, does the blended target approximately equal the current stock price? (This is the ultimate consistency check.)

---

# ═══════════════════════════════════════════════════════════════
# AUDIT 7: INTERACTIVITY & PERFORMANCE
# ═══════════════════════════════════════════════════════════════

- [ ] **Slider responsiveness:** move each slider rapidly. Does the output update without significant lag? If there's a >2 second delay, optimize.
- [ ] **Monte Carlo runtime:** does the 50,000-iteration simulation complete in a reasonable time? (<10 seconds is good, <5 is great, >30 is a problem.)
- [ ] **Tab switching:** can you move between all 12 tabs without delays or crashes?
- [ ] **Chart rendering:** do all Plotly charts render correctly? Any blank charts, error messages, or missing data?
- [ ] **Hover tooltips:** do they appear on all charts? Do they show useful information, not just raw data?
- [ ] **Mobile/small screen:** is the dashboard readable on a laptop screen (1366×768)? Do charts resize? Do tables scroll horizontally?
- [ ] **Error states:** what happens if a data fetch fails? Is there a graceful fallback message, or does the dashboard crash?
- [ ] **Global reset:** hit the master "Reset All" button. Does EVERYTHING return to defaults within 2 seconds?

---

# ═══════════════════════════════════════════════════════════════
# AUDIT 8: NARRATIVE & STORY
# ═══════════════════════════════════════════════════════════════

A dashboard full of correct numbers is useless if it doesn't tell a story. Check:

- [ ] **Command Center 30-second test:** land on Tab 1 with fresh eyes. In 30 seconds, can you answer: What is the recommendation? What is the target? What is the upside? What are the 3 drivers? If not, simplify the Command Center.

- [ ] **Every tab has a "so what?":** each tab should have a "What the Market is Missing" callout that gives the key insight in one sentence. If any tab is just data without a takeaway, add the callout.

- [ ] **The thesis flows logically:** if you read through tabs 1-12 in order, does the story build? Gold is structurally higher (Tab 2) → NEM is the best way to play it (Tabs 3-4) → the model says it's undervalued (Tabs 5-6) → the risks are manageable (Tab 7) → probability confirms it (Tab 8) → capital is being deployed well (Tab 9) → catalysts are coming (Tab 10) → stewardship is strong (Tab 11) → here's the verdict (Tab 12).

- [ ] **The Reverse DCF anchors the closing argument.** The last thing a judge sees should be: "The market is pricing gold at $X. Spot is $Y. That gap is the opportunity." Does the Thesis Verdict tab deliver this clearly?

- [ ] **Honest tensions are present.** ESG tab includes worker fatalities, Cadia class action, environmental impact of mining. Risk Engine includes compounding bear case. The dashboard doesn't hide bad news — it contextualizes it. Verify this.

- [ ] **Recommendation is earned, not assumed.** The final verdict should feel like the conclusion of 12 tabs of rigorous analysis, not a predetermined answer. If you change assumptions to pessimistic values, does the recommendation change to HOLD or SELL? It should. A model that always says BUY regardless of inputs is not credible.

---

# ═══════════════════════════════════════════════════════════════
# AUDIT 9: COMPETITIVE DIFFERENTIATION
# ═══════════════════════════════════════════════════════════════

- [ ] **Would a finance professional be impressed?** Show the dashboard to an imaginary CFA charterholder. What would they critique? Fix that.
- [ ] **Does anything look "default" or "template"?** Any Streamlit default styling leaking through (grey backgrounds, rounded buttons, light mode elements)? Any Plotly default annotations or watermarks? Eliminate every trace of default styling.
- [ ] **Is there anything no other competitor would have?** The mine-level analysis, the correlated Monte Carlo, the Reverse DCF, the Build Your Own Thesis mode — are these all present and polished? These are the features that create distance from other entries.
- [ ] **Is the interactivity real and deep?** Can a user genuinely explore the model and reach their own conclusions? Or is the interactivity superficial (sliders that barely change anything)?
- [ ] **Is the GLD objection preemptively killed?** If a judge thinks "Why not just buy GLD?" before seeing the answer, the dashboard has failed. Is the NEM vs GLD comparison prominent enough? Consider linking it from the Command Center.

---

# ═══════════════════════════════════════════════════════════════
# AUDIT 10: FINAL POLISH
# ═══════════════════════════════════════════════════════════════

- [ ] **Spelling and grammar:** read every label, every title, every tooltip, every callout. Fix typos.
- [ ] **Consistent terminology:** is it "FY2025" everywhere, or "FY25" in some places and "2025" in others? Pick one format and enforce it.
- [ ] **Source attribution:** does every panel have a source? Is any panel missing a "Source: [X] | As of [date]" footer?
- [ ] **Tab naming:** are tab labels clear and consistent? All caps, same style?
- [ ] **Chart titles:** does every chart have a descriptive title? Not "Chart 1" — something like "NEM AISC vs Peer Group ($/oz, FY2023–FY2025)."
- [ ] **Axis labels:** does every chart axis have a label with units? Not just "price" — "$, per share" or "$/oz."
- [ ] **Legend clarity:** are chart legends positioned so they don't overlap data? Are colors in legends consistent with the design system?
- [ ] **Empty states:** are there any panels that show "No data" or blank space? If data wasn't fetched, is there at least a message explaining why?
- [ ] **Footer:** is there a dashboard-level footer with: "Built for the Perplexity Stock Pitch Competition 2026 | Data as of [date] | NEM Equity Research Terminal"?

---

# ═══════════════════════════════════════════════════════════════
# FIX PRIORITY
# ═══════════════════════════════════════════════════════════════

If you find issues, fix them in this order:

1. **Math errors** — a wrong number destroys credibility instantly. Fix first.
2. **Broken interactivity** — a slider that doesn't work makes the whole dashboard feel broken. Fix second.
3. **Missing assumption justifications** — an unexplained number invites judge skepticism. Fix third.
4. **Design violations** — white backgrounds, rounded corners, wrong fonts undermine the professional feel. Fix fourth.
5. **Missing content** — incomplete tabs or missing features. Fix fifth.
6. **Data staleness** — old data when fresher is available. Fix sixth.
7. **Narrative gaps** — missing callouts, unclear story flow. Fix seventh.
8. **Polish** — typos, inconsistent formatting, missing sources. Fix last.

After fixing everything, do one final pass through the entire dashboard, tab by tab, and ask yourself:

**"Is this the most impressive analytical tool I've ever built?"**

If the answer is yes, ship it. If no, identify the weakest tab and improve it until the answer is yes.
