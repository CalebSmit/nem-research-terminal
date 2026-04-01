# NEM DASHBOARD — REVIEW & IMPROVEMENT PLAN v2

## Second Pass: Go Deeper, Think Outside the Box, Win

---

# ═══════════════════════════════════════════════════════════════
# SECTION 0: THE ASSUMPTION TRANSPARENCY FRAMEWORK
# ═══════════════════════════════════════════════════════════════

## THIS SECTION OVERRIDES EVERYTHING ELSE IN THIS DOCUMENT AND IN THE ORIGINAL MASTER PLAN.

Every single input and assumption in the entire dashboard — from the gold price forecast to the WACC to the P/NAV mine life to the Monte Carlo correlation coefficient — must follow these three rules:

### RULE 1: EVERY INPUT MUST BE DEFENSIBLE AND EXPLAINED

No input should be a magic number. Every assumption must have a visible, expandable justification panel or tooltip that explains:
- **What it is** (plain English definition)
- **What value the model is using** (the number)
- **Why that value was chosen** (the sourced, logical defense)
- **Where the data came from** (specific source and as-of date)

For example, a gold price assumption shouldn't just say "$4,800." It should say:
> **Gold Price — Year 1: $4,800/oz**
> Average of 2026 consensus forecasts from J.P. Morgan ($5,055), Goldman Sachs ($4,628), RBC ($4,600), and Bank of America ($4,538). We use the average rather than the highest estimate to ensure the thesis does not depend on aggressive gold assumptions. Source: Bank research reports, fetched [date].

This applies to EVERY input: WACC components, tax rate, terminal multiple, production assumptions, cost structure, mine life, P/NAV discount rate, scenario gold decks, Monte Carlo distribution parameters — everything.

### RULE 2: EVERY INPUT MUST BE OVERRIDABLE BY THE USER

Every assumption that feeds into a calculation should be adjustable. The user should be able to change any input and watch the model recalculate with their value. Implementation options (use the best fit for each input):
- **Slider** — for continuous numerical inputs (gold price, WACC, multiples, growth rates)
- **Number input field** — for precise values the user wants to type
- **Dropdown** — for categorical choices (scenario selection, valuation method)
- **Toggle** — for on/off choices (include copper optionality yes/no, use Gordon Growth vs Exit Multiple)

Group these controls logically. The most important ones (gold price, WACC, terminal multiple) should be prominent and always accessible. Less frequently adjusted inputs (tax rate, mine life, D&A as % of revenue) can live in expandable "Advanced Assumptions" panels.

### RULE 3: A "RESET TO AI-SUGGESTED" BUTTON ON EVERY INPUT GROUP

Every section that has overridable inputs must include a clearly labeled button:

**⟲ Reset to AI-Suggested Defaults**

When clicked:
- ALL inputs in that section snap back to the values that the model calculated from its own research
- The justification panels update to show WHY those are the suggested values
- The model recalculates with the original AI-derived assumptions

This should exist at multiple levels:
- **Per-section reset** — e.g., "Reset WACC Assumptions" resets just Rf, ERP, β, Kd, weights
- **Per-tab reset** — e.g., "Reset DCF Assumptions" resets everything on the DCF tab
- **Global reset** — a master "Reset All to AI-Suggested" button (in the sidebar or header) that restores the entire dashboard to its research-backed defaults

The UX should make it CLEAR which inputs the user has modified vs which are still at AI defaults. Use a visual indicator — for example:
- **AI-suggested values:** displayed normally
- **User-overridden values:** highlighted with an accent color border or a small "✎ Modified" badge

This way, a judge can immediately see: "They changed the gold price and the terminal multiple, but everything else is the model's original research."

---

## COMPLETE LIST OF INPUTS THAT MUST FOLLOW THESE RULES

Every one of the following must be (a) explained with a sourced justification, (b) overridable, and (c) resettable.

### DCF Model Inputs:
| Input | How to Defend It |
|-------|-----------------|
| Gold Price — Year 1 | Average of major bank consensus forecasts. Cite each bank and their number. Explain that you use the average (not the highest) to be conservative. |
| Gold Price — Annual Escalation | Historical long-run gold appreciation rate OR inflation + modest real return. Cite the data. ~2-4% is typical; explain why your choice is reasonable. |
| Production (Moz) — Year 1 | NEM's official FY guidance from their most recent earnings call or 10-K. Cite the filing. |
| Production — Ramp Schedule | NEM's stated long-term production targets from investor presentations. Cite the source. If interpolating between guidance and target, explain the interpolation. |
| COGS as % of Revenue | 2-year historical average. Show the calculation: FY[X] COGS/Rev = X%, FY[Y] COGS/Rev = Y%, average = Z%. Explain why 2-year average is used (captures both strong and weak margin years, avoids projecting peak margins forward). |
| Other OpEx (R&D, SGA, Other) as % of Revenue | Multi-year historical average. Show the calculation for each line item. |
| Effective Tax Rate | Most recent fiscal year effective rate from the income statement. Cite the filing. If it differs significantly from the statutory rate, explain why (e.g., jurisdictional mix, tax credits). |
| Depreciation as % of Revenue | Historical average. Note: for a miner, D&A is driven by asset base and depletion, so % of revenue shifts as gold prices move. Acknowledge this limitation. |
| CapEx as % of Revenue | Historical average, cross-checked against management's CapEx guidance. Cite both. |
| Working Capital Change as % of Revenue Change | Historical average. Note this is inherently noisy for miners; explain approach. |
| Risk-Free Rate | Current 10-Year US Treasury yield. Cite the source (FRED, Bloomberg, etc.) and the exact date. |
| Equity Risk Premium | Damodaran's current implied ERP. Cite the source URL and date. If unavailable, explain the alternative (e.g., historical arithmetic average, survey data) and cite it. |
| Beta | Source, methodology (5-year monthly vs S&P 500 is standard), and exact value. Note: if beta seems unusually low or high, explain why (e.g., gold miners often have low market beta because gold is a hedge against equities). |
| Cost of Debt — Synthetic Rating | Show the full chain: Interest Coverage Ratio (from financials) → Damodaran ICR lookup table → Synthetic Rating → Default Spread → Pre-tax Kd. Every step visible and auditable. |
| Capital Structure Weights | Market cap for equity (cite price × shares), book value for debt (cite balance sheet). Show the calculation. |
| Terminal EV/EBITDA Multiple | Peer median. Show the peer set, each peer's EV/EBITDA, and the median calculation. Explain why peer median is appropriate (it's what an acquirer would pay; it's where the stock "should" trade if fairly valued). |
| Gordon Growth Rate (cross-check) | Long-term GDP growth or inflation rate. Cite the source. Explain this is only a cross-check, not the primary terminal method. |
| DCF/P-NAV Blend Weights | 70/30 is a judgment call. Defend it: DCF is primary because NEM generates $7B+ FCF, making cash flow valuation structurally appropriate. P/NAV gets 30% because it captures reserve optionality that cash flow multiples miss. These weights are the user's to change. |

### P/NAV Inputs:
| Input | How to Defend It |
|-------|-----------------|
| Gold Price Deck | Trailing 2-year average spot. Calculate it live: average of daily/monthly closing prices over the last 24 months. Show the calculation. Explain: this normalizes for the recent macro spike and stress-tests reserves at cycle-midpoint pricing, which is standard institutional practice for long-life mining assets. |
| AISC | Most recent full-year actual AISC from NEM's filings. Cite the source. |
| Mine Life (years) | P&P reserves ÷ annual production = implied mine life. Show the math. Cross-check against NEM's stated mine life estimates. If they differ, explain which you chose and why. |
| P/NAV Discount Rate | Blended Tier 1/Tier 2 WACC. Explain: Tier 1 assets (low-risk, long-life, OECD jurisdictions) warrant a lower discount; Tier 2 (emerging market, shorter life) warrant higher. Research what discount rates P/NAV analysts typically use for gold miners (~5-7% is standard). Cite a source if available (e.g., broker research methodology, Damodaran country risk data). |
| P/NAV Target Multiple | Start with the peer average P/NAV multiple (fetch it). Then argue for a premium or discount and explain why. Factors: S&P 500 membership, credit rating, reserve size, jurisdiction quality, ESG ratings. Each factor should be stated and its directional impact on the multiple explained. |

### Monte Carlo Inputs:
| Input | How to Defend It |
|-------|-----------------|
| Gold Price Distribution — Type | Log-normal. Defend: gold prices cannot go negative, and empirical gold returns are approximately log-normally distributed. Cite any academic or practitioner reference. |
| Gold Price Distribution — Mean & Std Dev | Center on your base case gold assumption. σ should be calibrated so that the ~5th percentile roughly equals your bear gold scenario and the ~95th roughly equals your bull scenario. Show this calibration explicitly. |
| Exit Multiple Distribution — Type & Correlation | Correlated with gold via a shared factor. Defend: when gold prices rise, market sentiment toward gold miners improves, multiples expand, and vice versa. This is empirically observable — during gold selloffs (2013, 2015), gold miner EV/EBITDA multiples compressed alongside gold. Correlation of ~0.5-0.7 is a reasonable estimate; acknowledge this is a judgment call and let the user override it. |
| WACC Distribution — Type & Range | Normal, independent of gold. Defend: WACC shifts are driven by rate changes and risk appetite, which are partially but not fully correlated with gold. For simplicity, model as independent. Range: ±75-100bps around calculated WACC, which corresponds to roughly ±1 standard deviation of the individual WACC components shifting simultaneously. |
| Number of Iterations | 50,000. Defend: show convergence — the running median stabilizes well before 50,000. This proves the sample size is sufficient. Academic convention is typically 10,000+. |

### Scenario Analysis Inputs:
| Input | How to Defend It |
|-------|-----------------|
| Bull Gold Price | Highest major bank forecast. Cite the bank and number. |
| Base Gold Price | Average of major bank forecasts. Cite each. |
| Bear Gold Price | Trailing 3-5 year average spot price, representing reversion to a "normal" gold environment. Calculate it, show it, cite it. |
| Stress Gold Price | Trailing 10-year average or below — represents a full unwinding of the structural bull thesis. Calculate it. Acknowledge this is extreme but useful for floor-value analysis. |
| Scenario Probability Weights | This is the most subjective input. Be honest about that. Defend with reasoning: "We assign 50% to Base because it aligns with consensus; 25% to Bull given structural tailwinds; 20% to Bear as the primary risk; 5% to Stress as a tail event." These are judgment calls — let the user set their own weights. |

### Other Inputs:
| Input | How to Defend It |
|-------|-----------------|
| NEM Gold Beta | Regression output. Show the regression: NEM weekly/monthly returns vs gold returns. Report β, R², p-value, and sample period. If the beta has changed over time (e.g., higher since Newcrest acquisition because of larger gold exposure), note that. |
| Breakeven Gold Price | Find the gold price at which NEM's operating cash flow = 0. This requires knowing total cash costs (not just AISC — include corporate overhead, interest, sustaining capex). Show the calculation transparently. |
| Copper Optionality Assumptions | Current copper price (fetched), Cadia production profile (from filings), assumed copper price scenarios. For anything projected, use analyst consensus or the futures curve and cite it. |
| Reserve Replacement Cost | If using depletion-adjusted FCF, explain how you estimate the cost to replace one ounce of reserve. Methods: (a) historical exploration + development spend per ounce discovered/converted, or (b) precedent acquisition cost per reserve ounce. Either way, show the math and cite the data. |

---

# ═══════════════════════════════════════════════════════════════
# SECTION 1: NEW FEATURES
# ═══════════════════════════════════════════════════════════════

---

## 1. THE "WHY NOT JUST BUY GLD?" MODULE

**Why this matters:** The #1 objection any judge will have.

**Build a direct NEM vs GLD comparison panel:**
- Total return comparison chart: NEM vs GLD over 1yr, 3yr, 5yr. Fetch real price data for both.
- Return decomposition showing what NEM provides beyond gold exposure:
  - Operating leverage (NEM earns the spread between gold and AISC — as gold rises, margin expands nonlinearly). Build a CHART showing this: at gold $3,000, $4,000, $5,000, $6,000, what is NEM's margin per ounce? What is GLD's "margin"? (Zero — GLD is pass-through.)
  - Dividends (GLD pays nothing; calculate NEM's cumulative dividend contribution over the holding period)
  - Buyback yield (quantify the share count reduction and its per-share impact)
  - Production growth (more ounces produced over time = growing revenue even at flat gold)
  - Copper optionality (GLD has zero exposure to copper)
- Side-by-side scenario table: at gold +20%, +10%, flat, -10%, -20%, -30%:
  - GLD return = gold return (1:1)
  - NEM estimated return = calculate using gold beta, operating leverage ratio, and dividend yield. USE REAL DATA to compute these.
  - Show the asymmetry: NEM amplifies upside more than downside because of the cost floor
- Breakeven comparison: GLD tracks gold linearly to zero. NEM has positive OCF at any gold above breakeven (calculate it). Below breakeven, NEM still has $XXB in assets, reserves, and a business — GLD has bars in a vault.
- Conclusion: "NEM is not a gold bet — it's a gold OPERATING LEVERAGE bet with a dividend, a cost floor, and copper optionality."

**Overridable inputs:** Gold price scenarios for the comparison table, assumed holding period for return decomposition.

---

## 2. COPPER OPTIONALITY — VALUED SEPARATELY

**Why this matters:** Hidden value not in the standard gold DCF or P/NAV.

**Build a copper optionality panel:**
- Fetch: current copper price, copper futures curve, Cadia copper production data from NEM filings
- Show Cadia's copper production profile (current and projected with panel cave expansion)
- Calculate copper revenue at current prices and at multiple copper price scenarios
- Frame as incremental value: "Our gold-focused DCF and P/NAV do not include copper upside. At current copper prices, Cadia's copper production contributes ~$X/share of additional value beyond our target."
- Show the copper supply-demand fundamentals (deficit thesis: EVs, renewables, data centers)
- Build a simple copper sensitivity table: at copper $3.50/lb, $4.00, $4.50, $5.00, $5.50 — what is the incremental per-share value? Let the user pick a copper price assumption.

**Overridable inputs:** Copper price assumption, copper production ramp schedule, discount rate for copper cash flows.

**What I removed from the prior version:** The Black-Scholes option pricing idea. It doesn't make sense here — copper optionality is real asset value from a producing mine, not a financial option. A simple scenario NPV is more appropriate and more transparent.

---

## 3. MANAGEMENT CREDIBILITY TRACKER

**Why this matters:** DCF models depend on management execution. This answers "Can they deliver?" with data.

**Build:**
- Guidance vs actuals table: for the last 3-5 years, show management's original guidance for production (Moz), AISC ($/oz), and CapEx ($M) vs actual results. Calculate the miss/beat for each. Were they consistently conservative (actual > guide), accurate, or promotional (actual < guide)?
- Quarterly earnings accuracy: actual EPS vs consensus for last 8+ quarters. Show beat rate and average beat magnitude.
- CEO profile: Natascha Viljoen — research her background, prior role, and any measurable achievements. Present factually.
- Capital allocation track record: for each major decision in the last 3-5 years (Newcrest acquisition, non-core divestiture, buyback initiation, debt repayment), show what happened to financial metrics afterward. Was value created?

**What I removed from the prior version:** The "Management Credibility Score" composite metric. A made-up single score with arbitrary component weights would be challenged immediately by any judge who asks "How did you weight those factors?" Instead, present the raw data and let the user form their own conclusion. Data is more credible than a synthesized score.

---

## 4. UNIFIED GOLD PRICE MASTER SLIDER

**Why this matters:** Gold is the single most important variable. It should flow through the entire dashboard as one unified input, not be siloed in individual tabs.

**Build:**
- A persistent gold price control in the sidebar or header, always visible on every tab
- When the user changes it, the following ALL recalculate:
  - DCF: Year 1 gold revenue → entire FCFF → implied price
  - P/NAV: cash margin per ounce → NAV/share → implied P/NAV price
  - Blended target: updates from new DCF + P/NAV
  - Command Center KPIs: target price, upside %, recommendation
  - Risk Engine: breakeven buffer width recalculates
  - GLD comparison: NEM vs GLD scenario table updates
  - Copper optionality: relative value of gold vs copper shifts
- Also display: "AI-Suggested Gold Price: $X,XXX/oz (based on bank consensus average)" next to the slider. If the user has moved it, show the deviation: "Your assumption: $X,XXX (Y% above/below AI-suggested)"
- Include the **⟲ Reset** button right next to the slider

---

## 5. "BUILD YOUR OWN THESIS" INTERACTIVE MODE

**Why this matters:** Let judges construct their own thesis. If the model still produces a BUY under their assumptions, that's more convincing than any slide.

**Build as a sidebar or dedicated panel:**
- Expose EVERY major input with the user's current value and the AI-suggested default:

  **Gold & Revenue:**
  - Gold Price — Year 1: [slider] (AI suggests: $X,XXX — bank consensus avg)
  - Gold Escalation Rate: [slider] (AI suggests: X.X% — long-run inflation + X%)
  - Production — Year 1 (Moz): [input] (AI suggests: X.XX — NEM guidance)
  - Production — Long-term target: [input] (AI suggests: X.XX — NEM stated target)

  **Cost Structure:**
  - COGS % of Revenue: [slider] (AI suggests: XX.X% — 2yr historical avg)
  - Effective Tax Rate: [slider] (AI suggests: XX.X% — most recent FY effective rate)

  **Discount Rate:**
  - WACC: [slider] (AI suggests: X.XX% — CAPM + synthetic Kd)
  - OR override individual components: Rf, ERP, β, Kd

  **Terminal Value:**
  - Exit Multiple (EV/EBITDA): [slider] (AI suggests: X.XX× — peer median)
  - OR switch to Gordon Growth and set the growth rate

  **P/NAV:**
  - Gold Deck: [slider] (AI suggests: $X,XXX — 2yr trailing avg)
  - P/NAV Multiple: [slider] (AI suggests: X.XX× — peer avg + justified premium)
  - Mine Life: [slider] (AI suggests: XX yrs — reserves ÷ production)

  **Blend & Probabilities:**
  - DCF Weight: [slider 0-100%] / P/NAV Weight: [auto 100 minus DCF]
  - Scenario Probabilities: Bull [__]% / Base [__]% / Bear [__]% / Stress [__]% (must sum to 100%)

- As ANY input changes, all outputs recalculate live:
  - DCF Implied Price, P/NAV Implied Price, Blended Target, Upside %, Recommendation
  - Probability-weighted expected value
  - Monte Carlo shifts its base case (if technically feasible)

- **⟲ Reset All to AI-Suggested** button — one click, everything returns to research defaults
- Visual indicators on every modified input showing "✎ Modified — AI suggested: $X,XXX"

---

## 6. ACQUISITION PREMIUM / SUM-OF-THE-PARTS

**Why this matters:** A third valuation methodology. Three independent methods converging = powerful.

**Build:**
- Sum-of-the-parts: for each major mine (from the Mine Portfolio tab data), calculate: production × cash margin × annuity factor over remaining mine life. Sum all mines + corporate-level net cash − corporate overhead capitalized = SOTP equity value.
  - Each mine's inputs (production, margin, mine life, discount rate) should be visible and overridable.
  - Compare SOTP to whole-company DCF. If SOTP > DCF, there's a conglomerate discount = additional upside.
- Precedent transaction analysis: research the last 5-10 major gold mining M&A deals. What EV/EBITDA and EV/reserve-ounce multiples were paid? Cite each deal (acquirer, target, date, multiple). Apply median transaction multiple to NEM = implied acquisition value.
  - Overridable: let the user pick which transactions to include/exclude, or override the applied multiple.
- Display: "Three independent methods — DCF ($X), P/NAV ($X), SOTP ($X) — all indicate [upside/downside] vs current price. Convergence reduces model risk."

---

## 7. CAPITAL EFFICIENCY — ROIC & EVA

**Why this matters:** Almost no student pitch covers return on invested capital.

**Build:**
- ROIC: NOPAT ÷ Invested Capital (equity + net debt). Fetch and calculate for 3-5 years. Chart the trend.
- ROIC vs WACC: if ROIC > WACC, the company creates economic value. Chart the spread over time. Is it widening?
- EVA: (ROIC − WACC) × Invested Capital = dollars of economic profit. Chart over time.
- Peer comparison: ROIC for NEM vs each peer. Is NEM the most capital-efficient?
- Frame: "NEM earns X.X% on invested capital vs a X.X% cost of capital — creating $X.XB in economic value annually. This is rare in mining."

**Overridable inputs:** Invested capital definition (some analysts include operating leases, some don't), WACC for the spread calculation (should match your DCF WACC by default but can be overridden).

---

## 8. RESERVE REPLACEMENT & DEPLETION METRICS

**Why this matters:** A miner is a depleting asset. If reserves aren't being replaced, the business is shrinking.

**Build:**
- Reserve replacement ratio: (reserves at end of year + production during year − reserves at start of year) ÷ production. Ratio > 1.0 = growing resource base. Trend over 3-5 years.
- Reserve life: P&P reserves ÷ annual production. Is it stable?
- Depletion-adjusted FCF: standard FCF minus an estimate of reserve replacement cost.
  - For replacement cost, research: NEM's historical exploration + development spend per reserve ounce added. OR: use precedent acquisition cost per reserve ounce from recent deals. Show which method you used and why.
  - Compare depletion-adjusted FCF yield to standard FCF yield. If the gap is small, replacement is cheap. If large, there's hidden maintenance cost the standard FCF yield is masking.
- Key catalysts that change the depletion math: Lihir Nearshore Barrier (5M+ oz), Cadia panel caves, Ahafo North. These add reserves without acquisition-level spend.

**Overridable inputs:** Reserve replacement cost per ounce (the most subjective input — explain your estimate clearly and let users override it).

---

## 9. GOLD SUPPLY-DEMAND MODEL

**Why this matters:** Shows WHY gold goes up — fundamentals, not just a price chart.

**Build:**
- Annual gold supply: mine production (has been flat ~3,500 tonnes/yr — show this) + recycling + net central bank sales.
- Annual gold demand: jewelry + technology + investment (ETFs + bar/coin) + central bank purchases.
- Supply-demand balance chart: surplus or deficit by year? Is it tightening?
- Supply constraints: declining ore grades (fetch data if available), longer permitting timelines (qualitative), limited new major discoveries. The pipeline of future supply is thinning.
- Demand acceleration: central bank buying at 2× historical rates, ETF inflows accelerating, retail bar/coin demand.
- Key insight: "Mine supply is structurally constrained while demand is accelerating. This imbalance supports higher prices independent of monetary policy or inflation."

**Overridable inputs:** Demand growth assumptions by category, supply growth assumptions. Let the user test: "What if central bank buying drops back to the 10-year average?" How does the balance change?

---

## 10. UX & PRESENTATION POLISH

**Build any/all:**
- **"What the Market is Missing" callout** on every tab — one sentence, highlighted, explaining the key insight of that module.
- **Data source footer** on every panel: "Source: [name] | As of [date]"
- **Key Insights Sidebar** — persistent sidebar showing the 5 most important takeaways. Always visible.
- **Quick Stress buttons** on the DCF tab: "Gold -30%", "AISC +25%", "Bear WACC" — one-click presets that snap sliders to stress values. Include a **⟲ Reset** next to them.
- **Terminal-style loading states**: "FETCHING NEM FINANCIALS..." with blinking cursor.
- **Modified assumptions indicator** in the header: "3 of 24 assumptions modified by user" — so judges always know what's been changed vs what's the model's own output.

---

# ═══════════════════════════════════════════════════════════════
# SECTION 2: IMPROVEMENTS TO EXISTING MODULES
# ═══════════════════════════════════════════════════════════════

---

## Command Center:
- Add "Market Sentiment" indicator: analyst buy/hold/sell counts, short interest, insider activity.
- Add "What the Market is Missing" one-liner thesis statement.
- Show "X of Y assumptions at AI-suggested defaults" indicator.

## Gold Macro:
- Add gold forward curve overlay (contango/backwardation signals market expectations).
- Add USD reserve share decline chart as separate visual.

## DCF Engine:
- Add confidence interval on implied price derived from the sensitivity matrix (e.g., "Base case: $X — 80% confidence range: $Y to $Z based on ±50bps WACC and ±1× exit multiple").
- Every assumption in the DCF must have an expandable "Why this value?" justification panel.

## Monte Carlo:
- Add "Run Again" button to demonstrate result stability across random seeds.
- Add convergence plot: running median from 1,000 to 50,000 iterations.

## Risk Engine:
- Add "Black Swan" scenario: gold -50% in 6 months (historical precedent: 2013). Show NEM survives.
- Add risk-reward ratio: (base case upside × base probability) ÷ (bear case downside × bear probability). Display as a single number. >1.0 = favorable risk-reward. Let the user adjust scenario probabilities and watch it change.

## ESG:
- Add peer benchmarking for every ESG metric, not just NEM absolute values.
- Add trend lines: show ESG metrics improving over time.

---

# ═══════════════════════════════════════════════════════════════
# SECTION 3: QUALITY TESTS
# ═══════════════════════════════════════════════════════════════

---

## The "Why?" Test:
Click on ANY number in the dashboard. Can you immediately see why that number is what it is? If not, add a justification panel or tooltip. No orphan numbers.

## The "Override" Test:
Try to change every input. Does the model recalculate? Does the reset button work? Are modified inputs visually flagged?

## The "30-Second" Test:
Land on the Command Center. In 30 seconds, can you understand: what the recommendation is, what the target is, what the upside is, how many assumptions are at AI defaults vs user-modified, and what the single biggest insight is? If not, simplify.

## The "Challenge Me" Test:
Can a skeptical judge set every assumption to their most pessimistic value and still see a clearly functioning model that gives them an honest answer — even if that answer is SELL? The dashboard should be credible in ALL scenarios, not just the bull case.

## The "Would They Hire You?" Test:
Would a PM at a mid-market fund want to hire the person who built this? If not, keep going.

---

# ═══════════════════════════════════════════════════════════════
# PRIORITY RANKING
# ═══════════════════════════════════════════════════════════════

1. **Assumption Transparency Framework** — apply Section 0 to the ENTIRE existing dashboard first. Every input gets a justification, an override, and a reset button. This is the single highest-impact improvement.
2. **Unified Gold Price Master Slider** — ties the whole dashboard together.
3. **Build Your Own Thesis mode** — makes every assumption overridable from one place.
4. **"Why Not Just Buy GLD?" module** — addresses the #1 objection.
5. **Copper Optionality panel** — hidden value = free upside narrative.
6. **Management Credibility Tracker** — answers execution risk with data.
7. **ROIC / EVA** — signals CFA-level thinking.
8. **Quick Stress buttons + Confidence Intervals on DCF** — high UX impact, low build effort.
9. **Reserve Replacement metrics** — deep industry knowledge signal.
10. **Acquisition Premium / SOTP** — third valuation for convergence.
11. **Gold Supply-Demand model** — institutional macro depth.
12. **UX Polish** (callouts, source footers, loading states, modified indicator).
