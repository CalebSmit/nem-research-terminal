# NEM Equity Research Terminal — Full Context for Continuation

> **Purpose**: This document contains everything needed to continue work on the NEM Research Terminal dashboard in a new conversation. Read this entirely before doing anything.

---

## What This Project Is

A **Streamlit-based equity research terminal** for **Newmont Corporation (NYSE: NEM)** built for the **Perplexity Stock Pitch Competition 2026**. It has a Bloomberg Terminal dark aesthetic with 19 tabs of analysis. The goal is to win first place.

### Key Files
| File | Description |
|------|-------------|
| `/home/user/workspace/nem_terminal/app.py` | **MAIN DELIVERABLE** — ~3,869 lines, Streamlit app. **CURRENTLY HAS A SYNTAX ERROR** (see below) |
| `/home/user/workspace/nem_terminal/requirements.txt` | `streamlit>=1.32.0, plotly>=5.18.0, pandas>=2.1.0, numpy>=1.26.0, scipy>=1.11.0` |
| `/home/user/workspace/nem_data.json` | All data (keys: `as_of, market_data, nem_annual_financials, nem_operational, peer_quotes, peer_ratios_latest, gold_macro, esg, analyst_consensus, estimates, earnings_history`) |
| `/home/user/workspace/tab_overhaul_plan.md` | Detailed plan: ONE insight per tab + all changes needed |
| `/home/user/workspace/research/annotation_data.md` | Verified research data for chart annotations (central bank gold, ESG AUM, discovery drought, Cadia AISC, AI copper demand, NEM breakeven) |

### How to Run
```bash
cd /home/user/workspace/nem_terminal
streamlit run app.py --server.port 5000
```

---

## CRITICAL: Current Broken State

### Syntax Error at Line 1453-1455
The master overhaul script inserted two lines (`fig_cb.add_hline` and `fig_cb.add_annotation`) at **wrong indentation** — they're at 4-space indent but need to be at 8-space indent (inside a `with c2:` block). The specific broken section:

```python
# Line 1449: end of fig_cb.add_trace (inside `with c2:` block, 8-space indent)
        fig_cb.add_hline(y=cb_data['pre_2022_avg'], line_dash='dash', ...)  # line 1450 — correct, 8 spaces
        apply_layout(fig_cb, "CB PURCHASES: STRUCTURAL DEMAND SHIFT", 280)   # line 1452 — correct, 8 spaces
    fig_cb.add_hline(y=473, ...)     # line 1453 — WRONG: 4 spaces (should be 8)
    fig_cb.add_annotation(x='2022', y=1136, ...)  # line 1454 — WRONG: 4 spaces (should be 8)
        st.plotly_chart(fig_cb, use_container_width=True)  # line 1455 — this triggers IndentationError
```

**Fix**: Lines 1453-1454 need 4 more spaces of indentation (change from 4 to 8 spaces) to be inside the `with c2:` block. Also note line 1450 already adds a similar hline — the line 1453 hline is a duplicate that should either replace line 1450-1451 or be removed. The annotation on line 1454 is new and should be kept (with correct indentation).

---

## What's Already Done (DO NOT REDO)

### ✅ WMIM Callouts — Applied to ALL 19 tabs
"What the Market is Missing" highlighted callout boxes at the top of every tab. These use a `<div>` with `border: 2px solid #58a6ff` styling. All 19 are present and correct.

### ✅ Chart Annotations on 5 Charts
Annotations were successfully added to these figures:
- `fig_cb` (Central Bank chart, GOLD tab) — but with wrong indentation (the syntax error)
- `fig_fcf` (FCF chart, PROFILE tab)
- `fig_hist` (MC Simulation histogram)
- `fig_debt` (Debt trajectory, RETURNS tab)
- `fig_cred` (Credibility bar chart)

### ✅ Data Corrections Already Applied
- Cadia AISC: Changed from "$400/oz" to note about cave transition (~$1,950/oz current)
- Breakeven: Changed from "$1,558/oz" to "$1,700/oz" (more defensible)

### ✅ STORY Tab — Fully rewritten in first-person analyst voice
### ✅ ALT DATA Tab — All 8 channel checks deepened with specific research data
### ✅ CREDIBILITY Tab — Extended to 10-year study (2015-2025) with peer comparison and quantified punchline

---

## What Still Needs to Be Done

### 1. FIX THE SYNTAX ERROR (Priority 1)
Lines 1453-1454 need correct indentation. See "Syntax Error" section above.

### 2. Add Chart Annotations to ~8 More Charts
Every chart needs at least one annotation/reference line/callout. These charts have NONE:

| Figure Variable | Tab | Line | What to Annotate |
|----------------|-----|------|------------------|
| `fig_gold` | GOLD (tab 2) | 1406 | Mark 2022 structural break, add spot price reference |
| `fig_aisc_mine` | MINES (tab 4) | 1730 | Reference line at NEM portfolio avg AISC, mark Cadia |
| `fig_heat` | DCF (tab 5) | 1934 | Circle/highlight the base case cell |
| `fig_nav_sens` | REL VAL (tab 6) | 2112 | Mark NEM vs peer median |
| `fig_asym` | RISK (tab 7) | 2249 | Highlight the asymmetry (upside vs downside) |
| `fig_olev` | GLD CMP (tab 15) | 3364 | Annotate operating leverage divergence |
| `fig_cu` | COPPER (tab 16) | 3539 | Reference line at current copper price, AI demand note |
| `fig_roic` | ROIC (tab 18) | 3787 | Label the ROIC-WACC spread |

Also check: `fig_bridge` (CMD, 1315), `fig_earn` (PROFILE, 1611), `fig_risk` (RISK, 2226), `fig_conv` (MC SIM, 2416), `fig_tornado` (MC SIM, 2432), `fig_pie` (RETURNS, 2476), `fig_shares` (RETURNS, 2522), `fig_score` (ALT DATA, 2747), `fig_radar` (ESG, 2857), `fig_eva` (ROIC, 3802), `fig_peer_roic` (ROIC, 3834).

### 3. Expand CATALYST Tab (Tab 10, lines 2551-2590) — TOO THIN
Currently: 1 data table + 1 summary box. **0 charts.** Needs:
- Horizontal waterfall/bar chart showing each catalyst's probability-weighted EV contribution
- Timeline visualization showing when catalysts trigger (Q1 2026 → Q1 2027)
- Currently has a `catalysts` list with data already defined (8 items with Impact, Prob, Cat, Q fields)

### 4. Expand ESG Tab (Tab 12, lines 2796-2878) — BORDERLINE THIN
Currently: 5 KPI tiles, E/S/G metric rows, 1 radar chart, honest tensions section. Needs:
- ESG peer comparison bar chart (NEM vs Barrick vs Agnico Eagle scores)
- Could add an ESG AUM trend line showing capital flowing to ESG mandates

### 5. Add Charts to MGMT Tab (Tab 17, lines 3602-3713) — 0 CHARTS
Currently: Guidance vs Actuals text rows, EPS beat KPIs, capital allocation timeline (text), CEO profile. Needs:
- EPS beat/miss bar chart (data exists in `d['earnings_history']` — has `actual_eps`, `est_eps`, `quarter` fields)
- Could convert the capital allocation timeline to a visual

### 6. Add Convergence Chart to VERDICT Tab (Tab 14, lines 3165-3334) — 0 CHARTS
Currently: Reverse DCF display, Final Verdict box, Convergence of Evidence (4 text cards), closing argument. Needs:
- Bar chart showing the four valuation methods converging: DCF $149.24, P/NAV $111.56, MC Sim $135.28, Rel Val ~$130
- Reference line at current price $107.80

---

## Design System (Bloomberg Terminal Dark)

```python
COLORS = {
    'bg': '#0d1117',
    'panel': '#161b22',
    'border': '#30363d',
    'text': '#e6edf3',
    'muted': '#8b949e',
    'blue': '#58a6ff',
    'green': '#3fb950',
    'red': '#f85149',
    'amber': '#d29922',
}
```
- Font: `'Consolas', 'SF Mono', 'Fira Code', monospace`
- Border-radius: 0 everywhere
- Max-width: 1100px
- All charts use `PLOT_LAYOUT` dict and `apply_layout(fig, title, height)` helper function

### Chart Layout Pattern
```python
PLOT_LAYOUT = dict(
    paper_bgcolor='#0d1117', plot_bgcolor='#161b22',
    font=dict(family='Consolas, SF Mono, Fira Code, monospace', color='#e6edf3', size=11),
    xaxis=dict(gridcolor='#30363d', zerolinecolor='#30363d'),
    yaxis=dict(gridcolor='#30363d', zerolinecolor='#30363d'),
    margin=dict(l=40, r=20, t=40, b=40), showlegend=True,
    legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(size=10, color='#8b949e')),
)

def apply_layout(fig, title, height=350):
    fig.update_layout(**PLOT_LAYOUT, title=title, height=height,
                      title_font=dict(size=12, color='#8b949e'))
```

### Annotation Style Pattern (use this for consistency)
```python
# Reference line
fig.add_hline(y=VALUE, line_color='#8b949e', line_width=1, line_dash='dot',
              annotation_text='Label text', annotation_position='bottom right',
              annotation_font=dict(size=9, color='#8b949e'))

# Callout annotation
fig.add_annotation(x=X, y=Y, text='<b>Bold</b><br>Detail', showarrow=True,
                   arrowhead=2, font=dict(size=9, color='#3fb950'),
                   arrowcolor='#3fb950', bgcolor='#0d1117',
                   bordercolor='#3fb950', borderwidth=1, ax=40, ay=-30)
```

---

## Tab Structure (19 tabs, index 0-18)

| Index | Name | Line Start | Charts | Status |
|-------|------|-----------|--------|--------|
| 0 | STORY | 935 | 0 (narrative) | ✅ Strong |
| 1 | CMD CENTER | 1127 | 4 (bridge, sparklines) | Needs annotations |
| 2 | GOLD | 1375 | 3+ (gold price, CB, banks) | **SYNTAX ERROR HERE** + needs annotations |
| 3 | PROFILE | 1554 | 2 (FCF ✅, earnings) | Needs earn annotation |
| 4 | MINES | 1657 | 3 (map, AISC bar, treemap) | Needs annotations |
| 5 | DCF | 1815 | 2 (heatmap, discount) | Needs annotations |
| 6 | REL VAL | 1987 | 2 (discount, NAV sens) | Needs annotations |
| 7 | RISK | 2124 | 2 (risk matrix, asymmetry) | Needs annotations |
| 8 | MC SIM | 2327 | 3 (histogram ✅, convergence, tornado) | Partially done |
| 9 | RETURNS | 2454 | 4 (pie, debt ✅, shares, div) | Partially done |
| 10 | CATALYST | 2551 | **0** | ❌ **TOO THIN — needs 2-3 charts** |
| 11 | ALT DATA | 2594 | 1 (score) | Needs annotation |
| 12 | ESG | 2796 | 1 (radar) | ❌ **Borderline thin — needs peer chart** |
| 13 | CREDIBILITY | 2883 | 1 (cred ✅) | ✅ Strong |
| 14 | VERDICT | 3165 | **0** | ❌ **Needs convergence bar chart** |
| 15 | GLD CMP | 3339 | 2 (olev, div adv) | Needs annotations |
| 16 | COPPER | 3483 | 1 (cu bar) | Needs annotation |
| 17 | MGMT | 3602 | **0** | ❌ **Needs EPS beat bar chart** |
| 18 | ROIC | 3718 | 3 (roic, eva, peer_roic) | Needs annotations |

---

## Verified Dashboard Values (hardcoded in BASE dict)
- WACC: 7.04%, DCF Target: $149.24, P/NAV: $111.56, Blended: $137.93
- Upside: +28.0%, Recommendation: BUY
- Implied Gold: $3,605/oz, Gold Spot: $4,576/oz, Gap: 26.9%
- MC Median: $135.28, P(>current): 76.4%
- Piotroski: 9/9, Altman Z: 4.10, ROIC: 19.6%, Price: $107.80

---

## Research Data Available for Annotations

All sourced data is in `/home/user/workspace/research/annotation_data.md`. Key figures:

| Topic | Value | Source |
|-------|-------|--------|
| Central bank gold 2022 | 1,136t (record) | [World Gold Council](https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-full-year-2022/central-banks) |
| Central bank gold 2023 | 1,037t | [World Gold Council](https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-full-year-2023/central-banks) |
| Central bank gold 2024 | 1,045t | [World Gold Council](https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-full-year-2024/central-banks) |
| Pre-2022 avg | ~473t/yr (2010-2021) | World Gold Council |
| ESG AUM | $30T+ (GSIA/Bloomberg 2022) | [Bloomberg Intelligence](https://www.bloomberg.com/company/press/global-esg-assets-predicted-to-hit-40-trillion-by-2030-despite-challenging-environment-forecasts-bloomberg-intelligence/) |
| Gold discovery drought | Zero major finds 2023-2024 (first time ever) | [S&P Global](https://www.spglobal.com/market-intelligence/en/news-insights/research/new-finds-remain-scarce-despite-gold-from-major-discoveries-at-3-boz) |
| Mine lead time | 17.8 years avg | [S&P Global](https://www.spglobal.com/market-intelligence/en/news-insights/research/from-6years-to-18years-the-increasing-trend-of-mine-lead-times) |
| AI copper demand by 2030 | 512kt (IEA) to 1M tonnes (Trafigura) | Multiple sources |
| Global avg gold AISC | ~$1,456/oz (Q3 2024 record) | [World Gold Council](https://www.gold.org/goldhub/gold-focus/2025/03/ever-upwards-aisc-distinct-regional-variations-are-emerging) |
| NEM FY2025 AISC | $1,358/oz (by-product) | [Newmont Q4 2024](https://www.newmont.com/investors/news-release/news-details/2025/Newmont-Reports-Fourth-Quarter-and-Full-Year-2024-Results-Provides-Full-Year-2025-Guidance/default.aspx) |
| NEM FY2025 FCF | $7.3B (record) | [Leverage Shares](https://leverageshares.com/us/insights/newmont-stock-surging-gold-prices-drive-record-cash-flows/) |

---

## User Instructions (CRITICAL — follow these exactly)

1. **"Do NOT rebuild the existing dashboard. Layer these additions into what's already there."**
2. **"Research FIRST, then build. The findings shape what you write."** — Research is DONE. Build now.
3. **"Be HONEST. If a channel check contradicts the thesis, include it."**
4. **"Maintain the exact same Bloomberg Terminal dark design system on all new tabs."**
5. **WMIM callout format**: One sentence, highlighted, at the top of each tab stating the insight.
6. **Chart annotations**: Every chart needs at least one annotation, reference line, or callout. "A chart without commentary is just a picture of numbers."
7. **Thin tab rule**: If fewer than 3 substantive panels/charts, expand or merge.
8. **Style for STORY tab**: "Write like a smart 22-year-old who's genuinely excited about what they found." (Already done.)
9. **Credibility punchline**: Must be quantified with exact numbers. (Already done: "-2.9% haircut, 5.11 Moz, $443M FCF at risk.")
10. **Channel check specificity**: "Exact numbers, exact comparisons, exact trend data, exact source URLs." (Already done.)

---

## Shared Asset Names (use these exact names when calling share_file to update versions)
- `nem_terminal_app` — for the app.py file
- `nem_data` — for nem_data.json
- `nem_terminal_requirements` — for requirements.txt

---

## Execution Plan (in order)

1. **Fix syntax error** at lines 1453-1454 (indent 4 more spaces, remove duplicate hline if needed)
2. **Add chart annotations** to all ~8+ unannotated charts (use research data from annotation_data.md)
3. **Expand CATALYST tab** — add waterfall bar chart + timeline visualization
4. **Expand ESG tab** — add peer comparison bar chart
5. **Add EPS beat bar chart** to MGMT tab
6. **Add convergence bar chart** to VERDICT tab
7. **Verify syntax** — `python3 -c "import py_compile; py_compile.compile('app.py', doraise=True)"`
8. **Start server** — `streamlit run app.py --server.port 5000`
9. **QA with Playwright** — screenshot each tab, verify no visual issues
10. **Share updated file** using `share_file` with name `nem_terminal_app`
