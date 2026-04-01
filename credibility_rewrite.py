#!/usr/bin/env python3
"""Replace the CREDIBILITY tab (tabs[13]) in app.py with the deep rewrite."""

import re

app_path = "/home/user/workspace/nem_terminal/app.py"

with open(app_path, "r") as f:
    lines = f.readlines()

# Find start and end of tabs[13] block
start_line = None
end_line = None

for i, line in enumerate(lines):
    if line.strip().startswith("with tabs[13]:"):
        start_line = i
    if start_line is not None and i > start_line and line.strip().startswith("with tabs[14]:"):
        end_line = i
        break

if start_line is None or end_line is None:
    print(f"ERROR: Could not find tabs[13] block. start={start_line}, end={end_line}")
    exit(1)

# Also find the comment block before tabs[14] — go back from end_line to find the separator
# The separator is "# TAB 12 — THESIS VERDICT" etc.
separator_start = end_line
for i in range(end_line - 1, start_line, -1):
    stripped = lines[i].strip()
    if stripped.startswith("# ═") or stripped.startswith("# TAB 12") or stripped.startswith("# TAB 14"):
        separator_start = i
    elif stripped == "":
        continue
    else:
        break

print(f"Replacing lines {start_line+1} to {separator_start} (0-indexed: {start_line} to {separator_start-1})")
print(f"That's {separator_start - start_line} lines being replaced")

new_tab = '''with tabs[13]:
    insight_callout("10-year study (2015-2025, excl. 2019 structural break): NEM beat production guidance in only 2 of 10 years. Average miss: -3.5%. But two distinct eras emerge — pre-Goldcorp accuracy was ±1%, post-Goldcorp was -5.4%. The 2024-2025 convergence to -0.4% suggests the integration tax is finally paid.")

    # ── ERA COMPARISON HEADER ──
    st.markdown(\'\'\'<div class="panel-header">PRODUCTION GUIDANCE vs ACTUALS — 10-YEAR STUDY (2015-2025)</div>\'\'\', unsafe_allow_html=True)

    st.markdown(f\'\'\'
    <div style="display:flex;gap:12px;margin-bottom:16px;">
      <div style="flex:1;background:#161b22;border:1px solid #30363d;padding:12px 16px;">
        <div style="color:#8b949e;font-size:9px;letter-spacing:1.5px;margin-bottom:6px;">ERA 1: STANDALONE NEM (2015-2018)</div>
        <div style="color:{COLORS['green']};font-size:18px;font-weight:700;">-0.8% avg miss</div>
        <div style="color:#8b949e;font-size:10px;">2 beats, 1 near miss, 1 miss | Disciplined mid-size producer</div>
      </div>
      <div style="flex:0 0 40px;display:flex;align-items:center;justify-content:center;">
        <div style="color:#8b949e;font-size:10px;writing-mode:vertical-lr;letter-spacing:2px;">2019<br>GOLDCORP</div>
      </div>
      <div style="flex:1;background:#161b22;border:1px solid #30363d;padding:12px 16px;">
        <div style="color:#8b949e;font-size:9px;letter-spacing:1.5px;margin-bottom:6px;">ERA 2: POST-GOLDCORP (2020-2025)</div>
        <div style="color:{COLORS['red']};font-size:18px;font-weight:700;">-5.4% avg miss</div>
        <div style="color:#8b949e;font-size:10px;">0 beats, 2 near misses, 4 misses | Integration-era drag</div>
      </div>
    </div>\'\'\', unsafe_allow_html=True)

    # ── FULL DATA TABLE ──
    cred_years =     ['2015','2016','2017','2018','2019*','2020','2021','2022','2023','2024','2025']
    cred_guidance =  [4.75,  4.90,  5.20,  5.15,  None,   6.70,  6.50,  6.20,  6.00,  6.90,  5.90]
    cred_actual =    [4.58,  4.90,  5.27,  5.10,  6.29,   5.91,  5.97,  5.96,  5.55,  6.85,  5.89]
    cred_miss_pct =  [-3.6,  0.0,  +1.3,  -1.0,  None, -11.8,  -8.2,  -3.9,  -7.5,  -0.7,  -0.2]
    cred_notes =     [
        'Below range floor (4.6 Moz); divestitures + lower grades',
        'Exactly at midpoint; CC&V + Merian ramp',
        'Beat — Merian + Long Canyon delivered ahead of schedule',
        'Low end of range; AISC beat massively ($909 vs $995 guided)',
        'EXCLUDED — Goldcorp added ~1.0 Moz mid-year',
        'COVID mine suspensions + Goldcorp integration chaos',
        'Persistent integration drag across portfolio',
        'Cerro Negro, Musselwhite underperformance',
        'Worst miss — Peñasquito blockade, Ahafo delays',
        'Near miss — divestiture program refocused portfolio',
        'Near miss — essentially at guidance; cleanest year since 2017',
    ]

    st.markdown('<div style="background:#161b22;border:1px solid #30363d;overflow-x:auto;">', unsafe_allow_html=True)
    # Header
    st.markdown(f"""
    <div style="display:flex;padding:10px 16px;border-bottom:2px solid #30363d;background:#0d1117;min-width:700px;">
      <span style="color:#8b949e;font-size:9px;letter-spacing:1px;width:50px;font-weight:700;">YEAR</span>
      <span style="color:#8b949e;font-size:9px;letter-spacing:1px;width:80px;font-weight:700;">GUIDED</span>
      <span style="color:#8b949e;font-size:9px;letter-spacing:1px;width:80px;font-weight:700;">ACTUAL</span>
      <span style="color:#8b949e;font-size:9px;letter-spacing:1px;width:65px;font-weight:700;">MISS %</span>
      <span style="color:#8b949e;font-size:9px;letter-spacing:1px;width:65px;font-weight:700;">VERDICT</span>
      <span style="color:#8b949e;font-size:9px;letter-spacing:1px;flex:1;font-weight:700;">CONTEXT</span>
    </div>""", unsafe_allow_html=True)

    for i in range(len(cred_years)):
        yr = cred_years[i]
        is_excluded = '2019' in yr

        if is_excluded:
            # 2019 structural break row
            st.markdown(f"""
            <div style="display:flex;padding:8px 16px;border-bottom:1px solid #30363d;background:#1a1a2e;align-items:center;min-width:700px;">
              <span style="color:#8b949e;font-size:10px;width:50px;font-weight:600;font-style:italic;">2019*</span>
              <span style="color:#8b949e;font-size:10px;width:80px;font-style:italic;">5.20</span>
              <span style="color:#8b949e;font-size:10px;width:80px;font-style:italic;">6.29</span>
              <span style="color:#8b949e;font-size:10px;width:65px;font-style:italic;">N/A</span>
              <span style="color:#8b949e;font-size:9px;width:65px;font-style:italic;">EXCLUDED</span>
              <span style="color:#8b949e;font-size:9px;flex:1;font-style:italic;">{cred_notes[i]}</span>
            </div>""", unsafe_allow_html=True)
            continue

        g = cred_guidance[i]
        a = cred_actual[i]
        m = cred_miss_pct[i]

        if m >= 0:
            miss_clr = COLORS['green']
            verdict = 'BEAT'
        elif m > -2:
            miss_clr = COLORS['amber']
            verdict = 'NEAR MISS'
        else:
            miss_clr = COLORS['red']
            verdict = 'MISS'

        bg = '#161b22' if i % 2 == 0 else '#0d1117'
        # Highlight the era boundary
        if yr == '2020':
            bg = '#1a1520'

        st.markdown(f"""
        <div style="display:flex;padding:8px 16px;border-bottom:1px solid #30363d;background:{bg};align-items:center;min-width:700px;">
          <span style="color:#e6edf3;font-size:10px;width:50px;font-weight:600;">{yr}</span>
          <span style="color:#8b949e;font-size:10px;width:80px;">{g:.2f} Moz</span>
          <span style="color:#e6edf3;font-size:10px;width:80px;">{a:.2f} Moz</span>
          <span style="color:{miss_clr};font-size:10px;font-weight:700;width:65px;">{m:+.1f}%</span>
          <span style="color:{miss_clr};font-size:9px;font-weight:600;width:65px;">{verdict}</span>
          <span style="color:#8b949e;font-size:9px;flex:1;">{cred_notes[i]}</span>
        </div>""", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Source attribution for table
    st.markdown(f\'\'\'
    <div style="color:#8b949e;font-size:9px;margin-top:6px;padding:0 4px;">
      Sources: NEM Investor Day press releases (Dec 2014-2018), Q4 earnings releases (2015-2025), SEC EDGAR 8-K filings, BMO Conference presentations.
      2019 excluded: Goldcorp acquisition closed Apr 18, 2019, adding ~1.0 Moz — guidance was pre-deal.
    </div>\'\'\', unsafe_allow_html=True)

    # ── KPI TILES ──
    st.markdown('<br>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""<div class="kpi-tile"><div class="kpi-label">BEAT RATE (10 YRS)</div>
          <div class="kpi-value" style="color:{COLORS['red']};font-size:22px;">2 / 10</div>
          <div class="kpi-sub">20% — only 2016 & 2017</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="kpi-tile"><div class="kpi-label">AVG MISS (ALL)</div>
          <div class="kpi-value" style="color:{COLORS['amber']};font-size:22px;">-3.5%</div>
          <div class="kpi-sub">10-yr avg, excl. 2019</div></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="kpi-tile"><div class="kpi-label">MISS TREND (2020→2025)</div>
          <div class="kpi-value" style="color:{COLORS['green']};font-size:22px;">-11.8% → -0.2%</div>
          <div class="kpi-sub">Integration tax fading</div></div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""<div class="kpi-tile"><div class="kpi-label">CREDIBILITY GRADE</div>
          <div class="kpi-value" style="color:{COLORS['amber']};font-size:22px;">C+</div>
          <div class="kpi-sub">Two eras, one trajectory</div></div>""", unsafe_allow_html=True)

    # ── MISS TREND BAR CHART — now spanning full 10-year history ──
    st.markdown(\'\'\'<div class="panel-header">PRODUCTION MISS TREND — TWO ERAS, ONE TRAJECTORY</div>\'\'\', unsafe_allow_html=True)
    fig_cred = go.Figure()

    # Comparable years only (exclude 2019)
    chart_years = ['2015','2016','2017','2018','2020','2021','2022','2023','2024','2025']
    chart_miss = [-3.6, 0.0, +1.3, -1.0, -11.8, -8.2, -3.9, -7.5, -0.7, -0.2]
    bar_colors_cred = [COLORS['red'] if m < -3 else (COLORS['amber'] if m < 0 else COLORS['green']) for m in chart_miss]

    fig_cred.add_trace(go.Bar(
        x=chart_years, y=chart_miss, marker_color=bar_colors_cred,
        text=[f"{m:+.1f}%" for m in chart_miss], textposition='outside',
        textfont=dict(color=COLORS['text'], size=9)
    ))

    fig_cred.add_hline(y=0, line_color=COLORS['green'], line_width=2, line_dash='dash',
        annotation_text='GUIDANCE MET', annotation_position='bottom right',
        annotation_font=dict(size=9, color=COLORS['green']))

    # Add vertical separator for Goldcorp break
    fig_cred.add_vline(x=3.5, line_color='#8b949e', line_width=1, line_dash='dot',
        annotation_text='GOLDCORP<br>2019', annotation_position='top',
        annotation_font=dict(size=8, color='#8b949e'))

    # Add trendline for post-Goldcorp
    fig_cred.add_trace(go.Scatter(
        x=['2020','2021','2022','2023','2024','2025'],
        y=[-11.8, -8.2, -3.9, -7.5, -0.7, -0.2],
        mode='lines', line=dict(color=COLORS['blue'], width=2, dash='dot'),
        name='Post-Goldcorp Trend', showlegend=False
    ))

    apply_layout(fig_cred, "PRODUCTION GUIDANCE MISS % BY YEAR (10-YEAR STUDY)", 370)
    fig_cred.update_layout(
        yaxis=dict(title='Miss %', range=[-15, 4]),
        xaxis=dict(title='Year'),
        showlegend=False
    )
    st.plotly_chart(fig_cred, use_container_width=True)

    # ── PEER CREDIBILITY COMPARISON — with year-by-year data ──
    st.markdown(\'\'\'<div class="panel-header">PEER CREDIBILITY COMPARISON (2020-2025)</div>\'\'\', unsafe_allow_html=True)

    # AEM row
    st.markdown(f\'\'\'
    <div style="background:#161b22;border:1px solid #30363d;border-left:3px solid {COLORS['green']};padding:12px 16px;margin-bottom:8px;">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
        <span style="color:#e6edf3;font-size:12px;font-weight:600;">Agnico Eagle (AEM)</span>
        <div>
          <span style="color:#8b949e;font-size:10px;margin-right:12px;">Avg Miss: <span style="color:{COLORS['green']};font-weight:700;">+0.1%</span> (post-merger)</span>
          <span style="color:{COLORS['green']};font-size:14px;font-weight:700;">A</span>
        </div>
      </div>
      <div style="color:#8b949e;font-size:9px;line-height:1.5;">
        Industry gold standard. 5/6 years within or above guidance (only miss: 2020 COVID force majeure).<br>
        Post-Kirkland merger (2022-2025): avg deviation +0.1% — virtually perfect. Beat in 2023 (top of range), above midpoint in 2024-2025.<br>
        <span style="color:#58a6ff;">Year-by-year vs midpoint:</span> 2020: -7.4% (COVID) | 2021: -0.9% | 2022: -5.0% | 2023: +3.0% | 2024: +1.0% | 2025: +1.4%
      </div>
    </div>\'\'\', unsafe_allow_html=True)

    # NEM row
    st.markdown(f\'\'\'
    <div style="background:#161b22;border:1px solid #30363d;border-left:3px solid #58a6ff;padding:12px 16px;margin-bottom:8px;">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
        <span style="color:#e6edf3;font-size:12px;font-weight:600;">Newmont (NEM)</span>
        <div>
          <span style="color:#8b949e;font-size:10px;margin-right:12px;">Avg Miss: <span style="color:{COLORS['amber']};font-weight:700;">-5.4%</span> (post-Goldcorp)</span>
          <span style="color:{COLORS['amber']};font-size:14px;font-weight:700;">C+</span>
        </div>
      </div>
      <div style="color:#8b949e;font-size:9px;line-height:1.5;">
        Two distinct eras. Pre-Goldcorp (2015-2018): avg miss -0.8%, beat in 2 of 4 years — comparable to AEM quality.<br>
        Post-Goldcorp (2020-2025): avg miss -5.4%, 0 beats. But trajectory matters: -11.8% → -0.2% across 6 years.<br>
        <span style="color:#58a6ff;">Year-by-year vs midpoint:</span> 2015: -3.6% | 2016: 0.0% | 2017: +1.3% | 2018: -1.0% | 2020: -11.8% | 2021: -8.2% | 2022: -3.9% | 2023: -7.5% | 2024: -0.7% | 2025: -0.2%
      </div>
    </div>\'\'\', unsafe_allow_html=True)

    # Barrick row
    st.markdown(f\'\'\'
    <div style="background:#161b22;border:1px solid #30363d;border-left:3px solid {COLORS['red']};padding:12px 16px;margin-bottom:8px;">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
        <span style="color:#e6edf3;font-size:12px;font-weight:600;">Barrick Gold (GOLD)</span>
        <div>
          <span style="color:#8b949e;font-size:10px;margin-right:12px;">Avg Miss: <span style="color:{COLORS['red']};font-weight:700;">-3.8%</span></span>
          <span style="color:{COLORS['red']};font-size:14px;font-weight:700;">C</span>
        </div>
      </div>
      <div style="color:#8b949e;font-size:9px;line-height:1.5;">
        Consistently lands low end of ranges. 2 outright misses (2022: -5.9%, 2023: -8.0%) from infrastructure disruptions.<br>
        Loulo-Gounkoto suspended Jan 2025 (govt action) — 2025 guidance excluded ~200-250 Koz. Flattering the 2025 in-range result.<br>
        <span style="color:#58a6ff;">Year-by-year vs midpoint:</span> 2020: 0.0% | 2021: -2.4% | 2022: -5.9% | 2023: -8.0% | 2024: -4.6% | 2025: -1.9%
      </div>
    </div>\'\'\', unsafe_allow_html=True)

    # Source for peers
    st.markdown(f\'\'\'
    <div style="color:#8b949e;font-size:9px;margin-top:4px;padding:0 4px;">
      Sources: AEM Q4 earnings releases 2020-2025 (agnicoeagle.com), Barrick Q4 results 2020-2025 (barrick.com), Mining Weekly, GlobeNewswire.
      All figures: attributable production vs initial annual guidance midpoint. AEM 2020 miss = COVID mine suspensions (force majeure). Barrick 2025 guidance excludes Loulo-Gounkoto.
    </div>\'\'\', unsafe_allow_html=True)

    # ── THE QUANTIFIED PUNCHLINE ──
    st.markdown(f\'\'\'
    <div style="background:#0d1117;border:2px solid {COLORS['amber']};padding:20px;margin-top:20px;">
      <div style="color:{COLORS['amber']};font-size:11px;letter-spacing:3px;text-transform:uppercase;margin-bottom:14px;text-align:center;">THE QUANTIFIED PUNCHLINE</div>
      <div style="color:#e6edf3;font-size:13px;line-height:1.7;max-width:900px;margin:0 auto;">
        NEM has beaten annual production guidance in <span style="color:{COLORS['red']};font-weight:700;">2 of 10</span> comparable years (2015-2025, excl. 2019 structural break),
        with an average miss of <span style="color:{COLORS['amber']};font-weight:700;">-3.5%</span>.
        <br><br>
        Applied to FY2026 guided production of <span style="font-weight:700;">5.26 Moz</span>:
      </div>

      <div style="display:flex;gap:12px;margin:16px 0;">
        <div style="flex:1;background:#161b22;border:1px solid #30363d;padding:12px;">
          <div style="color:{COLORS['red']};font-size:9px;letter-spacing:1px;margin-bottom:4px;">SCENARIO A: FULL-PERIOD AVG (-3.5%)</div>
          <div style="color:#e6edf3;font-size:16px;font-weight:700;">5.07 Moz</div>
          <div style="color:#8b949e;font-size:10px;">-186 Koz vs guidance</div>
          <div style="color:{COLORS['red']};font-size:10px;font-weight:600;">$539M FCF at risk</div>
        </div>
        <div style="flex:1;background:#161b22;border:1px solid {COLORS['amber']};padding:12px;">
          <div style="color:{COLORS['amber']};font-size:9px;letter-spacing:1px;margin-bottom:4px;">SCENARIO B: BASE CASE (-2.9%)</div>
          <div style="color:#e6edf3;font-size:16px;font-weight:700;">5.11 Moz</div>
          <div style="color:#8b949e;font-size:10px;">-153 Koz vs guidance</div>
          <div style="color:{COLORS['amber']};font-size:10px;font-weight:600;">$443M FCF at risk</div>
        </div>
        <div style="flex:1;background:#161b22;border:1px solid {COLORS['green']};padding:12px;">
          <div style="color:{COLORS['green']};font-size:9px;letter-spacing:1px;margin-bottom:4px;">SCENARIO C: RECENT TREND (-0.4%)</div>
          <div style="color:#e6edf3;font-size:16px;font-weight:700;">5.24 Moz</div>
          <div style="color:#8b949e;font-size:10px;">-24 Koz vs guidance</div>
          <div style="color:{COLORS['green']};font-size:10px;font-weight:600;">$68M FCF at risk</div>
        </div>
      </div>

      <div style="color:#e6edf3;font-size:12px;line-height:1.6;max-width:900px;margin:0 auto;">
        At $4,576/oz gold and $1,680/oz AISC, each 100 Koz of production variance = <span style="font-weight:700;">~$290M in FCF</span>.
        <br>Our base case applies a <span style="color:{COLORS['amber']};font-weight:700;">-2.9% haircut</span> (blending post-Goldcorp avg with recent trajectory),
        implying actual production of <span style="font-weight:700;">~5.11 Moz</span> — with <span style="color:{COLORS['amber']};font-weight:700;">$443M in FCF</span> at risk vs. guidance.
        <br><br>
        <span style="color:{COLORS['amber']};font-size:11px;">
          Grade: C+ (Improving) — Pre-Goldcorp NEM was a B+ operator (avg miss -0.8%). The Goldcorp integration destroyed
          that track record. But the -11.8% → -0.2% convergence over 2020-2025 suggests the integration tax is being paid down.
          We use 5.11 Moz in our DCF, not the guided 5.26 Moz. If 2026 delivery matches the 2024-2025 trajectory, upgrade to B.
        </span>
      </div>
    </div>\'\'\', unsafe_allow_html=True)

    source_footer("NEM Annual Reports & Investor Day Presentations 2015-2025, AEM Q4 Reports 2020-2025, Barrick Q4 Reports 2020-2025, SEC EDGAR, Newmont.com, Barrick.com, AgnicoEagle.com")

'''

# Replace lines
new_lines = lines[:start_line] + [new_tab + '\n'] + lines[separator_start:]

with open(app_path, 'w') as f:
    f.writelines(new_lines)

print(f"SUCCESS: Replaced {separator_start - start_line} lines with new CREDIBILITY tab")
print(f"New file has {len(new_lines)} lines (was {len(lines)})")
