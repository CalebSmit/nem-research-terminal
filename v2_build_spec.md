# V2 Build Specification

## CRITICAL CONSTRAINTS
- Keep the exact Bloomberg Terminal dark design system (#0d1117 bg, #161b22 panels, #30363d borders, #e6edf3 text, #8b949e muted, #58a6ff blue, #3fb950 green, #f85149 red, #d29922 amber)
- Monospace font everywhere (Consolas, SF Mono, Fira Code)
- border-radius: 0 everywhere
- max-width: 1100px
- DO NOT rebuild from scratch — integrate into existing architecture
- Maintain `run_base_calculations()` but make it accept overrides from session_state
- Maintain all 12 existing tabs + add new ones

## ARCHITECTURE CHANGES

### Session State Driven Assumptions
Replace hardcoded values with `st.session_state` driven controls. The key change:
- Create `DEFAULTS` dict with ALL model inputs and their metadata (value, explanation, source)
- Initialize `st.session_state` with defaults on first run
- `run_base_calculations()` should read from session_state instead of hardcoded values
- Remove `@st.cache_data` from `run_base_calculations()` since it now depends on mutable state

### Sidebar: Master Control Panel (Always Open)
Set `initial_sidebar_state="expanded"` and build in sidebar:
1. Gold Price Master Slider (prominent, top)
2. Modified assumptions counter ("3 of 28 at AI defaults")  
3. Global Reset button
4. "Build Your Own Thesis" collapsible sections

### New Tabs to Add
After existing 12 tabs, add:
- Tab 13: GLD COMPARE
- Tab 14: COPPER OPT
- Tab 15: MGMT CRED
- Tab 16: ROIC/EVA

## DATA POINTS AVAILABLE
From nem_data.json:
- NEM Price: $107.80, Mkt Cap: $117.3B, Shares: 1087.8M
- Gold spot: $4,576, 10Y: 4.31%, S&P: 6504.95
- FY2025: Rev $22,097M, EBITDA $13,123M, FCF $7,299M, Cash $7,647M, Debt $474M
- AISC 2025: $1,358/oz, Production 2025: 5.9 Moz, Reserves: 118.2 Moz
- Copper reserves: 12.5 Mt
- Bank forecasts: JPM $6,300, GS $5,400, UBS $6,200, MS $5,700, Citi $5,000
- Avg bank forecast: $5,720
- GLD price: $430.13, Copper: $5.63/lb

## COMPLETE DEFAULTS DICT (with justifications)
```python
DEFAULTS = {
    # Gold & Revenue
    'gold_y1': {'value': 5200, 'label': 'Gold Price — Year 1 ($/oz)', 
        'why': 'Conservative estimate below bank consensus average of $5,720. Uses ~90% of avg to avoid dependence on aggressive forecasts. Banks: JPM $6,300, GS $5,400, UBS $6,200, MS $5,700, Citi $5,000.',
        'source': 'Bank research reports (JPM, GS, UBS, MS, Citi), as of Mar 2026'},
    'gold_escalation': {'value': 3.0, 'label': 'Gold Annual Escalation (%)',
        'why': 'Long-run gold appreciation: ~2% inflation + ~1% real return. Historical 20-year CAGR ~8%, but we use 3% for conservatism.',
        'source': 'World Gold Council historical data'},
    'production_y1': {'value': 5.3, 'label': 'Production Year 1 (Moz)',
        'why': "NEM's FY2026 production guidance. Conservative vs. 2025 actual of 5.9 Moz to account for mine sequencing.",
        'source': 'NEM FY2025 10-K, Investor Presentation Mar 2026'},
    'production_target': {'value': 6.0, 'label': 'Long-term Production Target (Moz)',
        'why': "NEM's stated long-term target from investor day. Ramp from 5.3→6.0 over 5 years.",
        'source': 'NEM Investor Day Presentation 2025'},
    
    # Cost Structure
    'cogs_pct': {'value': None, 'label': 'COGS as % of Revenue',  # computed from data
        'why': '2-year average (FY2024-2025) to smooth cyclicality. Captures both strong and weak margin years.',
        'source': 'NEM FY2024-2025 Income Statements'},
    'sga_pct': {'value': None, 'label': 'SG&A as % of Revenue',
        'why': '2-year average (FY2024-2025).',
        'source': 'NEM FY2024-2025 Income Statements'},
    'effective_tax': {'value': None, 'label': 'Effective Tax Rate (%)',
        'why': "NEM's FY2025 effective rate, capped at 35%. Higher than US statutory due to global operations in high-tax jurisdictions.",
        'source': 'NEM FY2025 Income Statement'},
    'da_pct': {'value': None, 'label': 'D&A as % of Revenue',
        'why': '2-year average. Note: for miners, D&A is driven by asset base and depletion, so this ratio shifts as gold prices move.',
        'source': 'NEM FY2024-2025 Financial Statements'},
    'capex_pct': {'value': None, 'label': 'CapEx as % of Revenue',
        'why': '2-year average, cross-checked against NEM 2026 CapEx guidance of ~$3.2B.',
        'source': 'NEM FY2024-2025 Cash Flow Statements'},
    
    # WACC Components
    'rf': {'value': None, 'label': 'Risk-Free Rate (%)',  # from data
        'why': 'Current 10-Year US Treasury yield as of data fetch date.',
        'source': 'US Treasury / FRED, as of Mar 31, 2026'},
    'beta': {'value': 0.61, 'label': 'Equity Beta',
        'why': '5-year monthly beta vs S&P 500. Lower than market due to gold hedge effect — gold miners often have low market beta because gold price moves inversely to equity risk.',
        'source': 'Yahoo Finance / Bloomberg, 5yr monthly regression'},
    'erp': {'value': 4.5, 'label': 'Equity Risk Premium (%)',
        'why': "Damodaran's current implied ERP for the US market, updated monthly.",
        'source': 'Damodaran Online (NYU Stern), Jan 2026'},
    'wacc_override': {'value': None, 'label': 'WACC Override (%)',
        'why': 'Override calculated WACC. Leave blank to use CAPM-derived value.',
        'source': 'User override'},
    
    # Terminal Value
    'exit_multiple': {'value': 9.5, 'label': 'Exit EV/EBITDA Multiple (×)',
        'why': 'Peer median. Peers: AEM (10.2×), KGC (8.1×), GFI (6.8×), WPM (17.3×). Median excl. WPM streaming premium = ~8.4×; incl. WPM = 9.5×. NEM deserves at-median given S&P 500 inclusion and scale.',
        'source': 'Peer financial data as of Mar 2026'},
    'ggm_growth': {'value': 0.8, 'label': 'Gordon Growth Rate (%)',
        'why': 'Long-term GDP growth proxy. Used only as cross-check for exit multiple reasonableness.',
        'source': 'IMF World Economic Outlook, long-term real GDP forecast + inflation'},
    
    # P/NAV
    'gold_deck': {'value': 2775, 'label': 'P/NAV Gold Deck ($/oz)',
        'why': 'Trailing 2-year average gold spot price. 2024 avg ~$2,350, 2025 avg ~$3,200, average = ~$2,775. This normalizes for recent price spikes and tests reserves at cycle-midpoint pricing — standard institutional practice.',
        'source': 'LBMA / World Gold Council, 2024-2025 daily averages'},
    'nav_wacc': {'value': 5.75, 'label': 'P/NAV Discount Rate (%)',
        'why': 'Blended Tier 1/Tier 2 rate. Tier 1 (Cadia, Boddington — OECD) ~5%, Tier 2 (Ahafo, Yanacocha — emerging) ~7%. Weighted by NAV contribution ≈ 5.75%.',
        'source': 'Industry convention per Damodaran country risk premiums'},
    'nav_multiple': {'value': 1.20, 'label': 'P/NAV Target Multiple (×)',
        'why': 'Peer avg ~1.0-1.1×. NEM warrants 1.20× premium for: S&P 500 inclusion (liquidity), investment-grade credit, largest reserve base (118 Moz), ESG leadership.',
        'source': 'Peer P/NAV analysis, broker research'},
    'mine_life': {'value': 21, 'label': 'Mine Life (years)',
        'why': 'P&P reserves (118.2 Moz) ÷ annual production (~5.6 Moz avg) = ~21 years. Cross-checks vs. NEM stated mine life estimates.',
        'source': 'NEM FY2025 10-K Reserve Statement'},
    
    # Blend
    'dcf_weight': {'value': 70, 'label': 'DCF Weight (%)',
        'why': 'DCF primary (70%) because NEM generates $7B+ FCF, making cash flow valuation structurally appropriate. P/NAV gets 30% because it captures reserve optionality that cash flow multiples miss.',
        'source': 'Valuation methodology judgment'},
    
    # Scenario Probabilities
    'prob_bull': {'value': 20, 'label': 'Bull Probability (%)',
        'why': '20% — structural gold tailwinds (central bank buying, de-dollarization) make upside scenario plausible but not dominant.',
        'source': 'Analyst judgment based on macro backdrop'},
    'prob_base': {'value': 50, 'label': 'Base Probability (%)',
        'why': '50% — consensus view is most likely by definition.',
        'source': 'Standard base case weighting'},
    'prob_bear': {'value': 25, 'label': 'Bear Probability (%)',
        'why': '25% — rate cuts stalling, strong USD, gold mean-reversion risk.',
        'source': 'Analyst judgment'},
    'prob_stress': {'value': 5, 'label': 'Stress Probability (%)',
        'why': '5% — tail risk (2013-style gold crash, global deflation).',
        'source': 'Historical precedent analysis'},
    
    # Monte Carlo
    'mc_rho': {'value': 0.7, 'label': 'Gold-Multiple Correlation',
        'why': 'When gold rises, sentiment improves → multiples expand. Empirically observed: during 2013/2015 gold selloffs, EV/EBITDA compressed 30-40%. ρ=0.7 is a moderate-strong correlation.',
        'source': 'Regression of gold miner EV/EBITDA vs gold price, 2010-2025'},
    'mc_gold_sigma': {'value': 0.35, 'label': 'Gold Price Volatility (σ)',
        'why': 'Calibrated so P10-P90 spans approximately $2,500-$7,500. This matches gold 10-year realized vol of ~15% annualized, compounded over 5-year horizon.',
        'source': 'LBMA gold price volatility data'},
    'mc_iterations': {'value': 50000, 'label': 'MC Iterations',
        'why': '50,000 ensures convergence — running median stabilizes by ~10,000. Academic convention is 10,000+.',
        'source': 'Monte Carlo simulation best practice'},
    
    # Scenario Gold Prices
    'bull_gold': {'value': 6300, 'label': 'Bull Gold Price ($/oz)',
        'why': "Highest major bank forecast — JPMorgan's end-2026 target.",
        'source': 'JPMorgan Global Research, 2026 Gold Outlook'},
    'bear_gold': {'value': 3500, 'label': 'Bear Gold Price ($/oz)',
        'why': 'Trailing 3-year average spot price — represents reversion to pre-spike gold environment.',
        'source': 'LBMA 2023-2025 average'},
    'stress_gold': {'value': 2500, 'label': 'Stress Gold Price ($/oz)',
        'why': 'Below 5-year average — represents full unwinding of structural bull thesis. Comparable to 2020 levels.',
        'source': 'Historical floor analysis'},
    
    # Copper (for new module)
    'copper_price': {'value': 5.63, 'label': 'Copper Price ($/lb)',
        'why': 'Current spot price as of data fetch.',
        'source': 'CME HG=F, as of Mar 31, 2026'},
    'copper_production_ktpa': {'value': 120, 'label': 'Cadia Copper Production (kt/yr)',
        'why': "Cadia's annual copper production from NEM filings. Expected to increase with panel cave expansion.",
        'source': 'NEM FY2025 Annual Report'},
    'copper_discount_rate': {'value': 8.0, 'label': 'Copper Discount Rate (%)',
        'why': 'Higher than gold WACC due to commodity-specific risk and Cadia single-asset concentration.',
        'source': 'Industry convention for copper project evaluation'},
    
    # Other
    'other_rev': {'value': 2000, 'label': 'Other Revenue ($M)',
        'why': 'Byproduct revenue from copper, silver, zinc, and other metals. Conservative estimate below FY2025 actual.',
        'source': 'NEM FY2025 Annual Report segment data'},
    'gold_beta': {'value': 0.95, 'label': 'NEM Gold Beta',
        'why': "NEM's stock price sensitivity to gold. Regression: NEM monthly returns vs gold returns, 5-year period. β≈0.95 means NEM moves ~1:1 with gold.",
        'source': 'Regression analysis, NEM vs XAU/USD, 2021-2025'},
    'breakeven_fixed_cost': {'value': 200, 'label': 'Fixed Cost per Oz ($/oz)',
        'why': 'Corporate overhead, G&A, and sustaining costs not in AISC. Estimated from NEM SG&A ÷ production.',
        'source': 'NEM FY2025 Income Statement / Production Report'},
    
    # GLD comparison
    'gld_price': {'value': 430.13, 'label': 'GLD ETF Price ($)',
        'why': 'Current GLD price for comparison.',
        'source': 'NYSE Arca, as of Mar 31, 2026'},
}
```
