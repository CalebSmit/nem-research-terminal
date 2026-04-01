# NEWMONT (NEM) — LIVE RESEARCH TERMINAL: MASTER PLAN & EXECUTION PROMPT

## Perplexity Stock Pitch Competition | BUY Recommendation
### Version 4.0 FINAL — Fully Dynamic, Zero Hardcoded Numbers

---

# ═══════════════════════════════════════════════════════════════
# PART 1: MASTER PLAN
# ═══════════════════════════════════════════════════════════════

---

## 1. PURPOSE

Build a Bloomberg Terminal-grade, live equity research platform for Newmont Corporation (NYSE: NEM). This is a standalone analytical instrument for a global stock pitch competition. No one will have a report in front of them — this IS the deliverable.

It is NOT a summary of a static report. It is a live research terminal that fetches real data, runs its own calculations, and lets users interact with the thesis in real-time. It should feel like something a buy-side desk uses internally.

**Core Philosophy:** Framework from our research. Data from reality. Depth beyond any report.

Our research provides the analytical METHODOLOGY:
- How to build the DCF, the P/NAV, the scenarios, the Monte Carlo
- How to frame the 3-driver thesis structure
- What makes NEM compelling and what the risks are

Perplexity provides the DATA and DEPTH:
- Fetch current prices, financials, multiples, macro data
- Run its own calculations — the numbers are whatever the model produces
- Go far deeper than a typical pitch: mine-level analysis, full peer universe, factor decomposition
- If something strengthens the thesis, include it. If something challenges it, include that too.

---

## 2. WHAT "GO DEEPER" MEANS

| Dimension | Typical Pitch Level | Dashboard Level |
|-----------|-------------------|----------------|
| Gold thesis | "Central banks are buying" | Live gold chart with regime detection, CB purchase tracker, ETF flows, real rate overlay, forward curve, bank forecasts |
| AISC | 3 peers, 2 years | Full peer universe (8+ companies), 3-5 year AISC trends, cost curve positioning |
| DCF | Static 5-year model | Interactive with sliders that recalculate the entire model live |
| P/NAV | Single gold deck | Multiple gold deck scenarios, mine-by-mine NAV contribution |
| Monte Carlo | Pre-computed result | Live 50,000-iteration simulation with correlated variables |
| Peers | 5 companies, 4 metrics | 6-8 companies, 10+ metrics, scatter plots, Z-score relative value |
| Risk | 3-4 scenario descriptions | Full stress test + breakeven analysis + VaR + asymmetry visualization |
| ESG | Ratings listed | Quantified scoring with peer benchmarks, honest tensions acknowledged |
| Mines | Not covered | Mine-by-mine production, AISC, reserves, NAV contribution, expansion projects |
| Catalysts | Bullet points | Interactive Gantt timeline with probability-weighted expected value |

---

## 3. ARCHITECTURE — 12 MODULES

```
┌──────────────────────────────────────────────────────────────────────────┐
│  NEM EQUITY RESEARCH TERMINAL                              [LIVE DATA]  │
├──────────┬──────────┬──────────┬──────────┬──────────┬──────────────────┤
│ COMMAND  │ GOLD     │ COMPANY  │ MINE     │ DCF      │ RELATIVE        │
│ CENTER   │ MACRO    │ PROFILE  │ PORTFOLIO│ ENGINE   │ VALUATION       │
├──────────┼──────────┼──────────┼──────────┼──────────┼──────────────────┤
│ RISK     │ MONTE    │ CAPITAL  │ CATALYST │ ESG &    │ THESIS          │
│ ENGINE   │ CARLO    │ RETURNS  │ MAP      │ STEWARD  │ VERDICT         │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────────────┘
```

---

## 4. COMPETITION EDGE — WHY THIS WINS

| Feature | Why It Wins |
|---------|------------|
| Live data throughout | Feels like a real trading desk tool, not homework |
| Interactive DCF sliders | Users challenge assumptions and see results instantly |
| Correlated Monte Carlo | Most students (if they do MC at all) use independent variables. Correlating gold + multiples is how institutions model. |
| Mine-level analysis | Shows you understand the BUSINESS, not just the ticker |
| Reverse DCF | Reframes the pitch: "What is the market pricing?" |
| Breakeven vs. peers | Visual proof NEM survives drawdowns better than anyone |
| ESG with honest tensions | Acknowledging risks = credibility |
| No hardcoded answers | The model speaks for itself — whatever the data says, it says |

---

# ═══════════════════════════════════════════════════════════════
# PART 2: EXECUTION PROMPT — FOR PERPLEXITY COMPUTER
# ═══════════════════════════════════════════════════════════════

---

```
You are building a world-class, interactive equity research terminal for the Perplexity Stock Pitch Competition. The subject is Newmont Corporation (NYSE: NEM).

This is a GLOBAL COMPETITION. The dashboard must look, feel, and function like a Bloomberg Terminal-grade institutional research platform — the most sophisticated analytical tool any judge has ever seen from a competition team. Think hedge fund internal tool, not student project.

═══════════════════════════════════════════════════════════════
CRITICAL PHILOSOPHY
═══════════════════════════════════════════════════════════════

You are building a LIVE RESEARCH TERMINAL, not reproducing a static report.

- FETCH real, current data from the web for EVERYTHING
- RUN your own calculations using the methodologies I specify below
- The model's output IS the recommendation — do NOT start with a predetermined price target
- Whatever the data and the model produce, THAT is the answer
- GO DEEPER than any equity research report — mine-level data, factor decomposition, full peer universe, regime detection
- If you find data that strengthens the thesis, include it
- If you discover something that challenges the thesis, include it — intellectual honesty wins competitions
- ADD features and analysis I haven't listed if they would impress a CFA charterholder

═══════════════════════════════════════════════════════════════
TECH STACK
═══════════════════════════════════════════════════════════════

Python Streamlit app (preferred) OR Plotly Dash app.
- Plotly for all charts
- numpy for Monte Carlo simulation
- pandas for data handling
- Fetch data via web search, APIs, or any available source
- If a source is unavailable, use the best alternative and note the as-of date

═══════════════════════════════════════════════════════════════
DESIGN SYSTEM — BLOOMBERG TERMINAL DARK (MANDATORY)
═══════════════════════════════════════════════════════════════

NON-NEGOTIABLE. Apply to EVERY element.

Colors:
  Background:         #0d1117
  Panel Surface:      #161b22
  Borders:            #30363d (1px solid, ZERO rounded corners, ZERO shadows, ZERO gradients)
  Primary Text:       #e6edf3
  Muted/Label Text:   #8b949e
  Accent Blue (KPIs): #58a6ff
  Green (positive):   #3fb950
  Red (negative):     #f85149
  Amber (warning):    #d29922

Typography:
  Font: 'Consolas', 'SF Mono', 'Fira Code', monospace — EVERYWHERE
  KPI Values: 28px bold, accent blue
  KPI Labels: 10px uppercase, letter-spacing 1.5px, muted
  Panel Titles: 11px uppercase, letter-spacing 2px, muted
  Table Headers: 10px uppercase, muted
  Table Cells: 12px

Layout:
  Max-width: 1100px centered
  border-radius: 0 on EVERYTHING (* { border-radius: 0 !important; })
  Maximum data density — every pixel earns its place
  ZERO decorative elements

Number Formatting (ENFORCE EVERYWHERE):
  Dollars per share: $XXX.XX
  Dollars in millions: $XX,XXXM
  Dollars in billions: $XX.XB
  Percentages: XX.X%
  Multiples: X.XX×
  Production: X.XX Moz
  Negatives: ($X,XXX) in red with parentheses
  Right-align numbers, left-align text, commas for thousands

Plotly Template:
  Base: plotly_dark
  Override: paper_bgcolor='#161b22', plot_bgcolor='#161b22'
  Gridlines: #30363d
  Font: monospace, #8b949e for axes, #e6edf3 for titles
  No watermarks. Every chart MUST have title, axis labels, source note, and at least one annotation.

═══════════════════════════════════════════════════════════════
NAVIGATION — 12 TABS
═══════════════════════════════════════════════════════════════

1.  COMMAND CENTER    — Landing page, KPIs, thesis summary
2.  GOLD MACRO        — Gold price analysis, demand drivers, bank forecasts
3.  COMPANY PROFILE   — Financials, earnings quality, margins
4.  MINE PORTFOLIO    — Mine-level production, AISC, reserves, NAV contribution
5.  DCF ENGINE        — Interactive discounted cash flow model (CROWN JEWEL)
6.  RELATIVE VALUE    — Peer comparison, P/NAV, multiples
7.  RISK ENGINE       — Scenarios, stress testing, breakeven
8.  MONTE CARLO       — 50,000-iteration probabilistic simulation
9.  CAPITAL RETURNS   — FCF deployment, debt, buybacks, dividends
10. CATALYST MAP      — Forward timeline with probability weighting
11. ESG & STEWARDSHIP — Ratings, benchmarks, honest tensions
12. THESIS VERDICT    — Reverse DCF, summary, final recommendation

═══════════════════════════════════════════════════════════════
STEP 1: DATA COLLECTION — FETCH ALL OF THIS
═══════════════════════════════════════════════════════════════

Before building anything, fetch the following. Use current sources. Record every as-of date.

MARKET DATA:
  □ NEM current stock price, 52-week range, market cap, shares outstanding, dividend yield
  □ Gold spot price (XAU/USD) and 5-10 year price history
  □ Silver and copper spot prices (NEM has copper exposure via Cadia)
  □ 10-Year US Treasury yield
  □ S&P 500 level

NEM FINANCIALS (3-5 years historical + forward estimates):
  □ Income statement: Revenue, COGS, Gross Profit, EBITDA, EBIT, Net Income, EPS
  □ Cash flow: OCF, CapEx, FCF, Dividends Paid, Buybacks
  □ Balance sheet: Total Assets, Cash, Long-Term Debt, Total Equity, Current Ratio, D/E
  □ All margins: Gross, Operating, Net, FCF
  □ Quarterly EPS (last 4-8 quarters) — actual vs. consensus
  □ Forward consensus estimates (next 2 fiscal years)
  □ Analyst price targets: mean, median, high, low

NEM OPERATIONAL DATA:
  □ AISC per ounce: at least 3 years historical + current year guidance
  □ Attributable gold production (Moz): historical + guidance
  □ Mine-by-mine production and AISC for every major operation:
    Boddington, Tanami, Ahafo, Ahafo North, Cadia, Peñasquito, Merian,
    Cerro Negro, Yanacocha, Lihir, Pueblo Viejo (and any others)
  □ Reserve base (Moz P&P) and reserve life
  □ Copper production (tonnes), especially Cadia
  □ Production guidance and long-term production targets

PEER DATA (fetch for ALL):
  Barrick Gold (GOLD), Agnico Eagle (AEM), Kinross (KGC),
  Gold Fields (GFI), Wheaton Precious Metals (WPM), and optionally PAAS, HL
  For each: price, market cap, EV, EV/EBITDA, P/E, P/CF, P/Book,
  FCF yield, dividend yield, AISC, production, reserves

GOLD MARKET:
  □ Central bank gold purchases (annual, 2015-present)
  □ Gold ETF holdings/flows (GLD, IAU)
  □ Bank gold price forecasts — most current from Goldman, JPM, UBS, Citi, BofA, RBC
  □ Gold forward curve (COMEX futures)
  □ US real yields (TIPS) and USD index (DXY)

ESG:
  □ NEM MSCI ESG rating, DJSI ranking, Sustainalytics score, CDP Climate, S&P CSA
  □ GHG emissions per ounce, water recycling rates, safety metrics (TRIR, fatalities)
  □ Community investment data
  □ Active controversies, class actions, or legal proceedings

SUPPLEMENTAL (if available):
  □ Short interest as % of float
  □ Institutional ownership changes
  □ Insider buying/selling activity
  □ Earnings revision trend (are analysts raising or lowering estimates?)
  □ Options implied volatility

═══════════════════════════════════════════════════════════════
STEP 2: ANALYTICAL METHODOLOGY — HOW TO BUILD EACH MODEL
═══════════════════════════════════════════════════════════════

These are the METHODS. Plug in whatever data you fetched. The output is whatever the math produces.

─── DCF MODEL ────────────────────────────────────────────────

Build a five-year FCFF (Free Cash Flow to Firm) DCF.

REVENUE FORECAST (bottom-up build):
  Gold Revenue = Gold Price Assumption × Attributable Production (Moz)
  - Year 1 gold price: use the AVERAGE of major bank consensus forecasts for the current/next year
  - Years 2-5: step up ~3% annually from Year 1 (deliberately conservative — should be BELOW the most bullish bank forecast so the thesis doesn't depend on aggressive gold)
  - Production: use NEM's official guidance for Year 1, ramp toward their stated long-term target over Years 2-5
  Other Revenue = most recent "other metals/byproduct" revenue, grown at that segment's trailing CAGR
  Total Revenue = Gold Revenue + Other Revenue

COST STRUCTURE:
  - COGS: use the 2-YEAR historical average COGS-as-%-of-revenue (NOT the most recent year alone if it was a record margin year — this builds in trough-year conservatism)
  - R&D, SGA, Other OpEx: forecast as % of revenue using multi-year historical averages
  - This produces EBIT

FCFF BUILD:
  EBIT × (1 - effective tax rate) = NOPAT
  + Depreciation
  - CapEx
  - Change in Net Working Capital
  = Unlevered Free Cash Flow (FCFF)
  (Forecast D&A, CapEx, ΔWC as % of revenue using historical averages)

WACC — CALCULATE FROM SCRATCH:
  Cost of Equity (CAPM):
    Ke = Risk-Free Rate + β × Equity Risk Premium
    - Rf = current 10Y US Treasury yield (fetched)
    - β = from Yahoo Finance or similar (5yr monthly vs S&P 500)
    - ERP = Damodaran's current implied equity risk premium
      (try fetching from pages.stern.nyu.edu/~adamodar/ — if unavailable, ~4-5% is a reasonable range for the US)

  Cost of Debt (Damodaran synthetic rating method):
    - Calculate Interest Coverage Ratio = EBIT / Interest Expense
    - Map ICR to synthetic credit rating using Damodaran's lookup table
    - Pre-tax Kd = Risk-Free Rate + Default Spread for that rating
    - After-tax Kd = Pre-tax × (1 - effective tax rate)

  Capital Structure:
    - Equity weight = market cap / (market cap + book value of debt)
    - Debt weight = book value of debt / (market cap + book value of debt)

  WACC = Ke × We + Kd(1-t) × Wd

TERMINAL VALUE:
  Primary method: Exit Multiple
    - Use the PEER MEDIAN EV/EBITDA as exit multiple (calculate it from the peer data you fetched)
    - TV = Year 5 EBITDA × Exit Multiple
  Cross-check: Gordon Growth Model
    - TV_GGM = Year 5 FCFF × (1 + g) / (WACC - g), using g ≈ 0.5-1.0%
    - Calculate the implied exit multiple from GGM
    - If the GGM-implied multiple is HIGHER than your applied multiple, your terminal value is conservative — display this as validation

DISCOUNTING:
  - Use mid-year convention with a stub period adjustment for the partial first year
  - PV = FCFF / (1 + WACC)^(period)
  - Enterprise Value = Σ PV(FCFFs) + PV(Terminal Value)
  - Equity Value = EV - Minority Interest - Total Debt + Cash & Equivalents
  - Implied Price Per Share = Equity Value / Diluted Shares Outstanding

─── P/NAV MODEL ──────────────────────────────────────────────

CRITICAL: Use a CONSERVATIVE gold price deck — NOT current spot.
  - Gold deck = trailing 2-year average spot price
  - This normalizes for the recent macro spike and stress-tests reserve value at cycle-midpoint pricing
  - It should be SIGNIFICANTLY below current spot — that gap is intentional

Build:
  Cash Margin/Oz = Conservative Gold Deck − Most Recent FY AISC
  Annual Production = P&P Reserves ÷ Mine Life (~20-21 years for Tier 1 assets)
  Annual OCF = Cash Margin × Annual Production
  Gross NAV = Annual OCF × Annuity Factor (at ~5.5-6.0% blended WACC, over mine life)
  + Net Cash Position (from balance sheet)
  = Equity NAV
  ÷ Diluted Shares = NAV/Share

  Target P/NAV Multiple:
  - Research current peer P/NAV multiples from the data you fetched
  - NEM should trade at a modest premium to peer average, justified by: S&P 500 membership, investment-grade credit, largest reserve base
  - Implied Price = NAV/Share × Target Multiple

BLENDED TARGET:
  Final Price Target = 70% × DCF Implied Price + 30% × P/NAV Implied Price
  Upside = (Target / Current Price - 1) × 100

  Recommendation:
    > 20% upside = BUY
    -20% to +20% = HOLD
    > 20% downside = SELL

─── SCENARIO ANALYSIS ───────────────────────────────────────

Run 4 scenarios through the full DCF. Define them dynamically based on the data:

BULL: Gold at the highest major bank consensus forecast, full production ramp, AISC improvement, multiple expansion to peer premium
BASE: Gold at the average bank consensus, official production guidance, stable AISC, current peer median multiples
BEAR: Gold reversion toward the trailing 3-5 year average, AISC rises ~15-25%, flat production, multiple compression
STRESS: Gold collapses toward the trailing 10-year average or below, AISC rises sharply, production declines, severe multiple compression

For EACH scenario compute and display:
  Gold price assumptions (Year 1 and Year 5)
  Year 5 Revenue, EBITDA, EBITDA Margin, FCF
  PV of FCFs, PV of Terminal Value, Enterprise Value
  DCF Implied Price, Blended Target
  Upside/Downside vs current price
  Rating (BUY / HOLD / SELL)

KEY INSIGHT TO SURFACE: Does NEM generate positive FCF even in the Bear case? At what gold price does NEM's operating cash flow go to zero (breakeven)? How wide is the buffer between breakeven and current spot? This asymmetry — large upside vs. survivable downside — is the core of the investment case.

─── MONTE CARLO SIMULATION ──────────────────────────────────

50,000 iterations minimum.

CRITICAL: Gold price and exit multiple must be CORRELATED.
  When gold is high → sentiment bullish → multiples expand
  When gold crashes → fear → multiples compress
  Independent sampling is naive. Correlated sampling is how institutions model.

Implementation:
  1. Generate a single "market environment" factor per iteration (standard normal Z)
  2. Gold price = exp(μ_gold + σ_gold × Z) — log-normal
     Center μ on your base case gold assumption, σ calibrated so that the range spans roughly from your bear to bull gold scenarios
  3. Exit multiple = base_multiple + ρ × Z × σ_multiple — correlated with gold via the same Z
     ρ = correlation coefficient (~0.6-0.8 is reasonable)
  4. WACC = base_wacc + ε — INDEPENDENT normal, small σ (~50-100bps)
  5. P/NAV anchor = your calculated P/NAV price, held constant
  6. For each iteration: compute simplified DCF → blend 70% DCF + 30% P/NAV

Display:
  - Histogram (50+ bins) with vertical annotations for: median, mean, current stock price, bear case price
  - Shade region above current price green, label with probability %
  - Key stats: Median, Mean, P10, P25, P50, P75, P90
  - Tornado chart ranking input variables by influence on output variance
  - CDF curve with interactive hover
  - Assumption summary table showing each variable's distribution and parameters

─── REVERSE DCF (MOST IMPORTANT SINGLE FEATURE) ─────────────

This is the killer insight. Build it on the Thesis Verdict tab.

Concept: Given the CURRENT stock price, what gold price is the market implicitly assuming?

Method:
  - Take your DCF model
  - Instead of solving for price, SOLVE FOR the long-term gold price that produces an implied equity value equal to the current market cap
  - The result: "The market is pricing NEM as if gold is ~$X/oz"
  - Compare that implied gold to current spot
  - The GAP is the mispricing

Display prominently:
  "At [current price], the market is implicitly pricing gold at ~$[implied]/oz —
   [X]% below current spot of $[spot]. The gap is the opportunity."

Also run the P/NAV version: at what gold deck does NAV/share ≈ current price? That implied deck vs. actual spot tells the same story.

This reframes the entire thesis. The question becomes: "Do you believe gold stays at $[implied]?" If the answer is no (which is obvious when spot is far above), then NEM is undervalued.

═══════════════════════════════════════════════════════════════
STEP 3: MODULE-BY-MODULE BUILD INSTRUCTIONS
═══════════════════════════════════════════════════════════════

--- TAB 1: COMMAND CENTER ---

Header: "NEWMONT CORPORATION | NYSE: NEM" left, "PERPLEXITY STOCK PITCH COMPETITION 2026" right.
Show "LIVE DATA" badge with last-fetched timestamp.

Primary KPI Strip (4 tiles):
  - Current Price (live)
  - Your Calculated Target Price (from model)
  - Upside/Downside % (calculated)
  - Recommendation: BUY / HOLD / SELL (determined by model output)

Secondary KPI Strip (4 tiles):
  - Monte Carlo: P(exceeds current price) %
  - Piotroski F-Score: X/9 (calculate from financial data)
  - Altman Z-Score: X.XX (calculate from financial data)
  - NEM Gold Beta: X.XX× (calculate from returns regression)

Three thesis driver cards:
  1. Gold Macro Tailwinds — key stat: your gold assumption vs bank consensus
  2. Portfolio Transformation — key stat: AISC YoY change, only decliner in peer group (verify)
  3. Capital Discipline — key stat: FCF level, net debt/cash position

Valuation bridge waterfall: 70% DCF + 30% P/NAV = Blended Target

Mini sparklines: NEM multi-year price, gold multi-year price, FCF trend

--- TAB 2: GOLD MACRO ---

1. Gold price chart (5-10 year) with NEM AISC line overlay to show expanding margin. Annotate key events (central bank acceleration, ETF surges, price milestones).
2. Gold price averages table: 10-year, 5-year, 3-year, 1-year, 6-month, current spot — with return from each average to current. Shows the acceleration.
3. Central bank demand bar chart with prior-decade-average reference line. Annotate the "2× prior average" dynamic if it holds.
4. Bank gold forecast horizontal bars. Highlight where your model assumption sits vs consensus.
5. Gold-vs-real-rate scatter showing the broken inverse correlation (pre-2022 cluster vs post-2022 cluster).
6. Gold ETF holdings/flows chart.
7. NEM gold beta regression: NEM returns vs gold returns, compute and display β and R². Annotate: "Every $100/oz gold increase → ~$[X]M incremental FCF" (calculate from AISC + production).
8. Operating leverage callout: current AISC + current spot = margin/oz.
9. BONUS: Gold regime detector — use 50-day/200-day MA crossover, RSI, momentum to classify current phase (Accumulation / Breakout / Euphoria / Correction).

--- TAB 3: COMPANY PROFILE ---

1. Full financial summary table (3-5 years historical + estimates). Green/red color coding.
2. FCF bar chart showing the recent inflection trajectory.
3. Earnings beat tracker: grouped bars (actual vs consensus) for recent quarters. Highlight beat magnitudes.
4. AISC comparison vs FULL peer universe (all companies you fetched). Identify who is declining vs rising. If NEM is the only decliner, highlight that.
5. Balance sheet trajectory: net debt vs net cash over time.
6. Piotroski F-Score: CALCULATE all 9 criteria from the financial data you fetched. Show pass/fail for each. Highlight any that recently flipped.
7. Altman Z-Score: CALCULATE from financial data. Show components, map to safety zones.
8. Operating margin vs industry average.
9. Revenue composition: gold vs other metals/byproducts — show any growing diversification.

--- TAB 4: MINE PORTFOLIO (DEEP — GOES FAR BEYOND A TYPICAL PITCH) ---

Build this from NEM's most recent public filings, 10-K, and investor presentations.

1. World map showing all NEM operations (Plotly geo scatter or choropleth).
2. Sortable table for each mine:
   - Location, country, mine type (open pit / underground)
   - Annual production (Koz Au-eq)
   - Mine-level AISC ($/oz)
   - Remaining reserves (Moz), estimated mine life
   - Key expansion projects / status
   - Estimated NAV contribution (% of total, if calculable)
3. Mine-by-mine AISC bar chart sorted low→high with portfolio average reference line.
4. Production treemap: size = production, color = AISC (green = low cost, red = high).
5. Tier 1 mine definition callout: 10+ year life, low-cost, expansion potential. Note NEM operates exclusively Tier 1 post-divestiture (verify this claim).
6. Cadia spotlight: gold-copper production, panel cave timeline, copper's structural deficit thesis (EV, renewables, data centers).
7. Lihir spotlight: Nearshore Barrier, ore body optionality, mine life extension.
8. If you can calculate mine-by-mine NAV (production × margin × annuity factor), show a stacked bar decomposing total NAV by mine.

--- TAB 5: DCF ENGINE (CROWN JEWEL — MOST IMPORTANT TAB) ---

Build the full model using the methodology above and the data you fetched.

1. Revenue forecast table: show the bottom-up build (gold price × production + other metals).
2. Full P&L waterfall: Revenue → COGS → Gross Profit → OpEx → EBIT.
3. FCFF build: EBIT → NOPAT → +D&A → -CapEx → -ΔWC → FCFF.
4. DCF output: discount factors, PV of each year's FCFF, terminal value, PV of terminal, EV.
5. Bridge: EV → minus debt/MI → plus cash → Equity Value → ÷ shares → Implied Price.

6. INTERACTIVE SLIDERS (NON-NEGOTIABLE):
   - WACC: ±200bps around your calculated WACC, steps of 25bps
   - Terminal EV/EBITDA Multiple: reasonable range around peer median, steps of 0.5×
   - Gold Price (Year 1): wide range (roughly half to double current spot), steps of $100
     → When changed: recalculate gold revenue for ALL years (Year 1 = slider, Years 2-5 step up ~3%/yr)
     → Other revenue constant
     → Recompute entire model end-to-end
   - Tax Rate: 10% to 30%, steps of 1%

   AS SLIDERS MOVE: Implied Price and Upside % update LIVE.
   Color: GREEN (>20% upside), AMBER (0-20%), RED (downside).

7. Sensitivity heatmap:
   - WACC (rows) vs Terminal Multiple (columns) = implied price per cell
   - Color gradient: green → yellow → red
   - Bold the base case cell
   - Count: "X of Y cells exceed current price of $[live price]"

8. WACC build-up detail (expandable):
   Every component: Rf, ERP, β, Ke, ICR, synthetic rating, spread, Kd, tax shield, weights, WACC.

9. Gordon Growth cross-check:
   Show implied exit multiple from GGM. If higher than your applied multiple → terminal value is conservative. Display this.

--- TAB 6: RELATIVE VALUATION ---

1. Full peer comparison table: NEM + all peers, 8+ metrics (EV/Sales, EV/EBITDA, P/E, P/CF, P/Book, FCF Yield, Div Yield, AISC).
2. Discount/premium bars: NEM vs peer median for each metric.
3. Peer scatter: EV/EBITDA vs FCF Yield (or another revealing pair), bubble size = market cap. NEM should ideally appear in the "cheap + high quality" quadrant.
4. Full P/NAV build showing every step.
5. P/NAV sensitivity table: implied price at multiple conservative gold decks (e.g., trailing 2yr avg, trailing 3yr avg, trailing 5yr avg, and current spot). Shows how much upside exists even at very conservative assumptions.
6. Peer P/NAV comparison: where does NEM's multiple sit vs peers?
7. Historical NEM EV/EBITDA range (if available): current vs 3-5 year range.

--- TAB 7: RISK ENGINE ---

1. Four-scenario panel (Bull/Base/Bear/Stress) with toggle buttons. Each displays full detail: gold assumptions, financials, valuation, rating. ALL computed by your models.
2. Risk matrix: 2D scatter (probability vs impact) with labeled bubbles:
   - Gold Price Reversion
   - Jurisdictional Cost Increases (NEM operates in ~10 countries)
   - Rising AISC / Operational Disruption (especially in trough production years)
   - Integration / Execution Risk
   Research current risks from recent filings and news.
3. Breakeven analysis: at what gold price does NEM's OCF = 0? Display as bar vs current spot. Compare to peers if possible. The wider the buffer, the stronger the case.
4. Asymmetry chart: base case upside % vs bear case downside %. Two bars, dramatically different heights. Caption: "The asymmetry defines this investment."
5. Bear case compounding narrative: explain how risks stack (operational disruption + jurisdictional costs + gold reversion). Quantify combined impact. But show: even then, does the dividend hold? Does the business survive?
6. VaR from Monte Carlo: 5th percentile outcome = "95% confidence worst case."

--- TAB 8: MONTE CARLO ---

Run 50,000 iterations as described in methodology.

1. Histogram with annotated vertical lines: median, mean, current price, bear/bull case.
   Shade above current price green, label probability.
2. Key stats box: Median, Mean, Std Dev, P5, P10, P25, P50, P75, P90, P95.
3. CDF curve with interactive hover.
4. Tornado chart: rank inputs by influence on output variance.
5. Assumption table: distribution type and parameters for each variable.
6. BONUS: show how distribution shape changes with different gold-multiple correlation levels. Higher correlation = fatter tails = more extreme outcomes. This demonstrates modeling sophistication.

--- TAB 9: CAPITAL RETURNS ---

1. FCF allocation visualization: how most recent FY's FCF was deployed (debt repayment, buybacks, dividends, retained). Pie, donut, or treemap.
2. Debt trajectory: multi-year view of long-term debt, showing deleveraging.
3. Net debt → net cash bridge (if applicable).
4. Share count trend: diluted shares over time (declining = good via buybacks).
5. Per-share compounding: same dividend pool ÷ fewer shares = higher DPS without higher capital commitment. Visualize.
6. Dividend sustainability: FCF coverage ratio of dividends. How many times over is the dividend covered?
7. Management's stated capital allocation priorities (from most recent earnings call).

--- TAB 10: CATALYST MAP ---

Build an interactive horizontal Gantt/timeline.

Research NEM's current corporate calendar, guidance, and project timelines. Include:
  - Most recent earnings results and any beats/misses
  - Key mine ramp-ups and commissioning milestones (Ahafo North, Cadia panel caves, Lihir Nearshore Barrier, etc.)
  - Production inflection points (trough → recovery)
  - Multiple convergence potential (if NEM trades at a discount to peer median EV/EBITDA)
  - Balance sheet milestones (net cash achievement, potential rating upgrades)
  - Any other upcoming catalysts from filings or investor presentations

For each catalyst:
  - Date/quarter
  - Description
  - Status: Completed ✓ / In Progress ◐ / Upcoming ◯
  - Estimated impact ($/share or $M FCF — your best estimate)
  - Probability of on-schedule occurrence
  - Expected Value = Impact × Probability

Summary: "Total expected value of catalysts not yet in consensus: ~$X/share"
Key insight: "These catalysts add volume and margin WITHOUT requiring gold price appreciation."

--- TAB 11: ESG & STEWARDSHIP ---

This matters for competition scoring. Build with INTELLECTUAL HONESTY.

RATINGS DASHBOARD:
  All available ESG ratings for NEM, with sector/peer context.

ENVIRONMENTAL:
  GHG per ounce, water recycling rates/targets, land reclamation, net-zero pathway and interim targets.

SOCIAL:
  Safety metrics (TRIR, fatalities — use REAL numbers), community investment by country, foundation/scholarship programs.

GOVERNANCE:
  Board composition, exec comp alignment with ESG.

HONEST TENSIONS (CRITICAL — builds credibility):
  - Worker fatalities (whatever the actual number is — don't hide it)
  - Any active class actions or lawsuits (e.g., Cadia dust/water issues)
  - Inherent environmental impact of gold mining (open-pit, cyanide extraction)
  - Jurisdictional tensions in developing countries

STEWARDSHIP FRAMING:
  "Capital will flow to gold mining regardless. Investing in the producer with the strongest safety record, highest environmental commitment, and deepest community investment per ounce is better than letting capital flow to less responsible miners. This is not a rationalization — it's a principled choice."

--- TAB 12: THESIS VERDICT ---

Everything converges here. This is the closing argument.

1. Three-driver thesis summary with key metrics for each (pulled from your analysis).

2. Valuation bridge waterfall: Current Price → Your Calculated Target. Building blocks:
   - Earnings growth recognition
   - Multiple re-rating toward peer median
   - Gold price running above conservative model assumptions
   - Catalyst recognition

3. REVERSE DCF (CENTERPIECE — MOST IMPORTANT FEATURE):
   Display prominently:
   "At $[current_price], the market is implicitly pricing gold at ~$[implied]/oz —
    [X]% below current spot of $[spot]. The gap is the opportunity."

   Also show the P/NAV version: at what gold deck does NAV/share ≈ current price?
   Both should tell the same story: the market is pricing gold far below reality.

4. Probability-weighted expected value:
   Assign rough probabilities to each scenario (e.g., Bull 20%, Base 50%, Bear 25%, Stress 5%).
   Σ(probability × scenario target) = probability-weighted fair value.
   Compare to current price.

5. ESG summary strip: compact row of key ratings.

6. FINAL VERDICT BOX (large, terminal-styled, impossible to miss):
   ╔══════════════════════════════════════════════════════════════╗
   ║  RECOMMENDATION:  [computed]                                ║
   ║  PRICE TARGET:    $[computed]                               ║
   ║  UPSIDE:          [computed]%                               ║
   ║  MONTE CARLO:     [computed]% probability > current price   ║
   ║  PIOTROSKI: [X]/9 | ALTMAN Z: [X.XX] | AISC: $[X,XXX]/oz  ║
   ╚══════════════════════════════════════════════════════════════╝

═══════════════════════════════════════════════════════════════
STEP 4: ADDITIONAL FEATURES — GO BEYOND
═══════════════════════════════════════════════════════════════

Add anything you believe would impress a CFA charterholder. Ideas:

- Gold AISC cost curve: position NEM on the global industry cost curve
- Factor decomposition: how much of NEM's return is gold beta vs alpha vs market beta
- Correlation matrix: NEM vs gold vs S&P 500 vs 10Y yield vs DXY
- Historical P/NAV band chart: where NEM has traded relative to NAV over time
- FCF duration: years of FCF at current levels to recover entire market cap
- Earnings revision momentum: are analysts raising or lowering estimates?
- Insider activity tracker
- Short interest as % of float
- Implied vs realized volatility
- Global mine map with production bubbles
- Copper optionality value (separate from gold NAV)

If a feature makes a finance professional say "this is impressive" — include it.
If it's filler — skip it. Data density > decoration.

═══════════════════════════════════════════════════════════════
STEP 5: SELF-IMPROVEMENT LOOP
═══════════════════════════════════════════════════════════════

After building, run these audits:

1. MATH AUDIT:
   - EV = PV(FCFs) + PV(Terminal Value)?
   - Equity = EV - MI - Debt + Cash?
   - Price/Share = Equity / Shares?
   - Blended Target = 70% DCF + 30% P/NAV?
   - Sensitivity heatmap base case = DCF output?
   - Monte Carlo median ≈ base case DCF? (should be close)
   - Reverse DCF implied gold < current spot? (must be — otherwise the thesis doesn't work)
   - Sliders propagate correctly through ALL calculations?

2. DATA AUDIT:
   - Every data point sourced and dated?
   - Peer multiples current?
   - Financial data from most recent filings?
   - Gold price current?

3. DESIGN AUDIT:
   - EVERY element uses the dark palette? No white backgrounds?
   - No rounded corners? All fonts monospace?
   - Feels like Bloomberg, not a student project?

4. INSIGHT AUDIT:
   - Every panel tells a STORY, not just shows data?
   - Annotations, reference lines, callouts present?
   - Reverse DCF prominently displayed?
   - Asymmetry visually undeniable?
   - Would a judge understand the thesis in under 30 seconds from the Command Center?

5. COMPETITIVE AUDIT:
   - Is this the most impressive analytical tool you've ever built?
   - Would a hedge fund PM be impressed?
   - Is there a module that feels thin? Beef it up.
   - Is the Mine Portfolio genuinely insightful or just a data dump?
   - What would you add with one more hour? Add it now.

ITERATE until a finance professional would say: "How did a student build this?"

═══════════════════════════════════════════════════════════════
FINAL REMINDERS
═══════════════════════════════════════════════════════════════

1. NO PREDETERMINED ANSWERS. The model output IS the recommendation. Whatever the data says, it says.

2. INTELLECTUAL HONESTY > SALESMANSHIP. Honest risks build more credibility than hiding them.

3. THE REVERSE DCF IS THE KILLER INSIGHT. Make it impossible to miss.

4. INTERACTIVITY IS THE DIFFERENTIATOR. Sliders that recalculate live make this a TOOL, not a document.

5. CORRELATED MONTE CARLO IS YOUR FLEX. Gold ↔ multiples correlation shows real modeling sophistication.

6. GO DEEP ON MINES. No competitor will have mine-level analysis.

7. DATA > DECORATION. If choosing between one more data point and one more animation, fetch the data.

8. SPEED MATTERS. Load fast. No fluff.

Deploy to Streamlit Cloud for a shareable URL, or run locally.

Think deeply. Be rigorous. Build something extraordinary.
```

---

# ═══════════════════════════════════════════════════════════════
# APPENDIX: CALIBRATION REFERENCE (FOR PERPLEXITY'S EYES ONLY)
# ═══════════════════════════════════════════════════════════════

The following are outputs from our independent research (as of March 2026). These are provided ONLY so Perplexity can calibrate its models — if your independent analysis produces similar numbers, that's validation. If they diverge, investigate why and use your best judgment. DO NOT hardcode these into the dashboard.

**Our research produced (March 16, 2026 analysis date):**
- DCF implied: $186/share (5-year FCFF, exit multiple method, WACC ~5.6%)
- P/NAV implied: $132/share (conservative ~$3,100/oz gold deck, 1.20× multiple)
- Blended target: ~$170 (70/30 blend)
- Monte Carlo: median ~$168, ~79% probability exceeding the then-current price
- Four scenarios ranged from ~$307 (bull) to ~$29 (stress)
- Key assumptions: gold ~$4,800/oz Year 1, ~9.5% revenue CAGR, ~15% effective tax, peer median exit multiple

If your fresh analysis produces a materially different result, that's FINE — it means the data has moved. Use whatever the current data says.
