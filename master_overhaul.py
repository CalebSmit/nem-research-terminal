#!/usr/bin/env python3
"""
Master overhaul script: Add WMIM callouts, chart annotations, and expand thin tabs.
Uses line-based replacement for precision.
"""

import re

APP = "/home/user/workspace/nem_terminal/app.py"

with open(APP, "r") as f:
    lines = f.readlines()

# ============================================================
# HELPER: Find line number containing exact text
# ============================================================
def find_line(text, start=0, end=None):
    """Find first line containing text. Returns 0-indexed line number or -1."""
    end = end or len(lines)
    for i in range(start, end):
        if text in lines[i]:
            return i
    return -1

def find_line_exact(text, start=0, end=None):
    """Find first line where stripped content equals text."""
    end = end or len(lines)
    for i in range(start, end):
        if lines[i].strip() == text:
            return i
    return -1

def insert_after(line_idx, new_content):
    """Insert new_content after the given line index."""
    global lines
    new_lines = new_content.split('\n')
    for j, nl in enumerate(new_lines):
        lines.insert(line_idx + 1 + j, nl + '\n')
    return len(new_lines)

def insert_before(line_idx, new_content):
    """Insert new_content before the given line index."""
    global lines
    new_lines = new_content.split('\n')
    for j, nl in enumerate(new_lines):
        lines.insert(line_idx + j, nl + '\n')
    return len(new_lines)

# ============================================================
# WMIM CALLOUT HTML GENERATOR
# ============================================================
def wmim_code(text):
    """Generate Python code for a WMIM callout in Streamlit."""
    # Escape quotes for Python string
    text_escaped = text.replace("'", "\\'").replace('"', '\\"')
    return f'''    st.markdown("""
    <div style="background:#0d1117;border:2px solid #58a6ff;padding:14px 20px;margin-bottom:16px;">
      <div style="color:#58a6ff;font-size:9px;letter-spacing:2.5px;text-transform:uppercase;margin-bottom:6px;font-weight:700;">WHAT THE MARKET IS MISSING</div>
      <div style="color:#e6edf3;font-size:12px;line-height:1.6;font-weight:500;">{text_escaped}</div>
    </div>""", unsafe_allow_html=True)'''

# ============================================================
# PHASE 1: Add WMIM callouts to all tabs that need them
# ============================================================
print("PHASE 1: Adding WMIM callouts...")

wmim_data = {
    # tab_index: (search_text_after_which_to_insert, wmim_text)
    2: ("Central bank gold purchases are running at 2",
        "Central banks added 1,045t of gold in 2024 — the third consecutive year above 1,000t, vs. a pre-2022 average of ~473t/yr. This 2× structural demand shift puts a floor under gold that most equity models haven't incorporated."),
    3: ("NEM's gross margin expanded from 10%",
        "NEM's gross margin tripled from 10% (2023) to 50% (2025). This isn't just gold prices — it's the structural effect of divesting 6 high-cost mines and retaining only Tier 1 assets. The margin expansion is durable."),
    4: ("Cadia at $400/oz AISC",
        "After the Newcrest acquisition, NEM divested 6 non-core mines to focus on Tier 1 assets only. The remaining portfolio averages $1,358/oz by-product AISC (FY2025) vs. the global industry average of ~$1,456/oz — a structural cost advantage."),
    5: ("Even at a conservative",
        "Our DCF uses $5,200/oz gold — deliberately 10% below spot — and still produces $149/share (+38% upside). The margin of safety is in the assumptions, not the gold price."),
    6: ("NEM trades at 7.9",
        "NEM trades at 7.9× EV/EBITDA vs. peer median of 10.0×. A simple re-rating to the group — without any gold price appreciation — implies ~$130/share."),
    7: ("Risk-reward is asymmetric",
        "NEM generates positive FCF at any gold price above ~$1,700/oz (by-product AISC $1,358 + capex/overhead). With gold at $4,576, that's a $2,876/oz margin of safety — a 63% buffer before the thesis breaks."),
    8: ("50,000 correlated simulations",
        "76.4% of 50,000 Monte Carlo simulations produce a price above $107.80. The median outcome ($135.28) exceeds current price by 25% — the market is priced below the mathematical center of the distribution."),
    9: ("NEM returned $3.4B",
        "NEM returned $3.4B to shareholders in 2025 ($2.3B buybacks + $1.1B dividends) while simultaneously reaching $7.2B net cash. This dual mandate — returns AND balance sheet strength — signals peak financial health."),
    10: ("Forward catalysts add",
         "Eight forward catalysts add ~$30/share in probability-weighted expected value. The four operational catalysts alone (Cadia expansion, production inflection, Lihir, Ahafo North) contribute ~$19/share — none require gold price appreciation."),
    11: ("8 independent alternative data",
         "5 of 8 alternative data channels confirm the bull thesis. The 2 bearish signals (insider selling pattern, Ghana royalty risk) are included with full transparency — intellectual honesty, not cheerleading."),
    12: ("NEM ranks #1 in Bloomberg",
         '#1 Bloomberg ESG Transparency in the S&amp;P 500. 99th percentile S&amp;P CSA. $30T+ in ESG-mandated capital globally (Bloomberg Intelligence) increasingly flows to best-in-class operators — NEM is the beneficiary in gold mining.'),
    14: ("Two independent valuation methods",
         "Four independent methods (DCF $149, P/NAV $112, MC Sim $135, Rel Val ~$130) converge on the same zone. The reverse DCF reveals the market embeds $3,605/oz gold — 21% below spot. When four layers agree, the probability of mispricing is high."),
    15: ("NEM is not a gold bet",
         "GLD captures ~$0.40/oz in fees. NEM captures ~$2,896/oz in FCF margin. That's ~7,000× the economic capture per ounce of gold exposure — with a dividend and copper optionality that GLD can never provide."),
    16: ("Copper from Cadia adds",
         "AI data centers are projected to add 330,000–1,000,000+ tonnes of new copper demand by 2030 (IEA, Trafigura). Cadia's expansion to 150 kt Cu/yr makes NEM a backdoor AI infrastructure play — value invisible to gold-focused models."),
    17: ("Management has beaten consensus EPS",
         "Viljoen inherits the strongest balance sheet in NEM history: $7.2B net cash, Piotroski 9/9, completed Tier 1 portfolio. The restructuring is done — 2026 is the execution test."),
    18: ("NEM earns returns well above",
         "ROIC 19.6% vs. WACC 7.04% = 12.6 percentage point value creation spread. NEM generates $0.13 of economic profit per dollar of invested capital — rare in mining, where most peers destroy value."),
}

# Process in reverse order so line numbers don't shift
offset_total = 0
for tab_idx in sorted(wmim_data.keys(), reverse=True):
    search_text, wmim_text = wmim_data[tab_idx]
    # Find the insight_callout line for this tab
    line_idx = find_line(search_text)
    if line_idx == -1:
        print(f"  WARNING: Tab {tab_idx} — could not find '{search_text[:50]}...'")
        continue
    
    # Insert WMIM after the insight_callout line (and its closing paren)
    # The insight_callout is usually a single line ending with )
    # Insert after the next blank line
    insert_at = line_idx + 1
    # Skip blank lines
    while insert_at < len(lines) and lines[insert_at].strip() == '':
        insert_at += 1
    
    wmim_block = wmim_code(wmim_text)
    added = insert_after(insert_at - 1, '\n' + wmim_block + '\n')
    print(f"  Tab {tab_idx}: Inserted WMIM after line {insert_at+1} (+{added} lines)")

print(f"  Total lines after WMIM: {len(lines)}")

# ============================================================
# PHASE 2: Add chart annotations to existing figures
# ============================================================
print("\nPHASE 2: Adding chart annotations to charts...")

# Strategy: Find each st.plotly_chart call and insert annotation code before it
# We'll use the figure variable names and add annotations

# TAB 2 (GOLD) — fig_gold_price: mark the 2022 structural break
# Find "fig_gold_price" and add annotation before plotly_chart
idx = find_line("st.plotly_chart(fig_gold_price")
if idx != -1:
    insert_before(idx, """    fig_gold_price.add_annotation(x='2022', y=1800, text='<b>2022: Structural Break</b><br>Central banks 2× pre-2022 buying', showarrow=True, arrowhead=2, font=dict(size=9, color='#58a6ff'), arrowcolor='#58a6ff', bgcolor='#0d1117', bordercolor='#58a6ff', borderwidth=1, ax=0, ay=-40)""")
    print("  Tab 2 GOLD: Added structural break annotation to gold price chart")

# TAB 2 (GOLD) — fig_cb: annotate the step-change in central bank buying
idx = find_line("st.plotly_chart(fig_cb")
if idx != -1:
    insert_before(idx, """    fig_cb.add_hline(y=473, line_color='#8b949e', line_width=1, line_dash='dot', annotation_text='Pre-2022 avg: 473t/yr', annotation_position='bottom right', annotation_font=dict(size=9, color='#8b949e'))
    fig_cb.add_annotation(x='2022', y=1136, text='<b>1,136t</b><br>Record (2× avg)', showarrow=True, arrowhead=2, font=dict(size=9, color='#3fb950'), arrowcolor='#3fb950', bgcolor='#0d1117', bordercolor='#3fb950', borderwidth=1, ax=40, ay=-30)""")
    print("  Tab 2 GOLD: Added annotations to central bank chart")

# TAB 3 (PROFILE) — fig_fcf: annotate the 2025 inflection
idx = find_line("st.plotly_chart(fig_fcf")
if idx != -1:
    insert_before(idx, """    fig_fcf.add_annotation(x='2025', y=7300, text='<b>$7.3B FCF</b><br>Record — 2.5× 2024', showarrow=True, arrowhead=2, font=dict(size=9, color='#3fb950'), arrowcolor='#3fb950', bgcolor='#0d1117', bordercolor='#3fb950', borderwidth=1, ax=-40, ay=-30)""")
    print("  Tab 3 PROFILE: Added FCF inflection annotation")

# TAB 4 (MINES) — fig_aisc_bar: add reference line at global average
idx = find_line("st.plotly_chart(fig_aisc_bar")
if idx != -1:
    insert_before(idx, """    fig_aisc_bar.add_hline(y=1456, line_color='#f85149', line_width=1, line_dash='dash', annotation_text='Global Avg AISC: $1,456/oz (WGC Q3 2024)', annotation_position='top right', annotation_font=dict(size=9, color='#f85149'))""")
    print("  Tab 4 MINES: Added global avg AISC reference line")

# TAB 5 (DCF) — fig_sens: annotate base case
idx = find_line("st.plotly_chart(fig_sens")
if idx != -1:
    insert_before(idx, """    fig_sens.add_annotation(text='<b>BASE CASE</b>', x=0.5, y=0.5, xref='paper', yref='paper', showarrow=False, font=dict(size=10, color='#58a6ff'), bgcolor='#0d1117', bordercolor='#58a6ff', borderwidth=1, borderpad=4)""")
    print("  Tab 5 DCF: Added base case annotation to sensitivity")

# TAB 6 (REL VAL) — fig_disc: highlight NEM discount
idx = find_line("st.plotly_chart(fig_disc")
if idx != -1:
    insert_before(idx, """    fig_disc.add_hline(y=0, line_color='#3fb950', line_width=2, line_dash='dash', annotation_text='Fair Value (Peer Median)', annotation_position='top right', annotation_font=dict(size=9, color='#3fb950'))""")
    print("  Tab 6 REL VAL: Added fair value reference line")

# TAB 7 (RISK) — fig_scenario: annotate asymmetry
idx = find_line("st.plotly_chart(fig_scenario")
if idx != -1:
    insert_before(idx, """    fig_scenario.add_annotation(text='<b>ASYMMETRIC</b>: Bull upside > Bear downside', x=0.5, y=1.05, xref='paper', yref='paper', showarrow=False, font=dict(size=10, color='#d29922'), bgcolor='#0d1117')""")
    print("  Tab 7 RISK: Added asymmetry annotation")

# TAB 8 (MC SIM) — fig_hist: mark current price and median
idx = find_line("st.plotly_chart(fig_hist")
if idx != -1:
    insert_before(idx, """    fig_hist.add_vline(x=107.80, line_color='#f85149', line_width=2, line_dash='dash', annotation_text='Current: $107.80', annotation_position='top left', annotation_font=dict(size=9, color='#f85149'))""")
    print("  Tab 8 MC SIM: Added current price line to histogram")

# TAB 9 (RETURNS) — fig_debt: annotate net cash inflection
idx = find_line("st.plotly_chart(fig_debt")
if idx != -1:
    insert_before(idx, """    fig_debt.add_annotation(x='2025', y=7200, text='<b>Net Cash: $7.2B</b><br>Fortress balance sheet', showarrow=True, arrowhead=2, font=dict(size=9, color='#3fb950'), arrowcolor='#3fb950', bgcolor='#0d1117', bordercolor='#3fb950', borderwidth=1, ax=-50, ay=-30)""")
    print("  Tab 9 RETURNS: Added net cash annotation")

# TAB 13 (CREDIBILITY) — fig_cred: strengthen Goldcorp annotation
idx = find_line("st.plotly_chart(fig_cred")
if idx != -1:
    insert_before(idx, """    fig_cred.add_annotation(text='<b>2024-2025: Integration tax paid</b><br>Miss compressed to -0.4%', x='2025', y=-0.2, showarrow=True, arrowhead=2, font=dict(size=9, color='#3fb950'), arrowcolor='#3fb950', bgcolor='#0d1117', bordercolor='#3fb950', borderwidth=1, ax=-60, ay=-40)""")
    print("  Tab 13 CREDIBILITY: Added convergence annotation")

# TAB 15 (GLD CMP) — fig_leverage: annotate the divergence
idx = find_line("st.plotly_chart(fig_leverage")
if idx != -1:
    insert_before(idx, """    fig_leverage.add_annotation(text='<b>Operating leverage divergence</b><br>NEM margin expands; GLD is flat', x=0.8, y=0.85, xref='paper', yref='paper', showarrow=False, font=dict(size=9, color='#58a6ff'), bgcolor='#0d1117', bordercolor='#58a6ff', borderwidth=1, borderpad=4)""")
    print("  Tab 15 GLD CMP: Added operating leverage annotation")

# TAB 16 (COPPER) — fig_cu_sens: add current copper price reference
idx = find_line("st.plotly_chart(fig_cu_sens")
if idx != -1:
    insert_before(idx, """    fig_cu_sens.add_vline(x=4.50, line_color='#d29922', line_width=2, line_dash='dash', annotation_text='~Current Cu Price', annotation_position='top', annotation_font=dict(size=9, color='#d29922'))""")
    print("  Tab 16 COPPER: Added current copper price line")

# TAB 18 (ROIC) — fig_roic_wacc: label the spread
idx = find_line("st.plotly_chart(fig_roic_wacc")
if idx != -1:
    insert_before(idx, """    fig_roic_wacc.add_annotation(text='<b>12.6pp Value Creation Spread</b>', x=0.5, y=0.5, xref='paper', yref='paper', showarrow=False, font=dict(size=11, color='#3fb950'), bgcolor='#0d1117', bordercolor='#3fb950', borderwidth=1, borderpad=6)""")
    print("  Tab 18 ROIC: Added value creation spread label")

print(f"  Total lines after annotations: {len(lines)}")

# ============================================================
# PHASE 3: Fix Cadia AISC reference ($400 → accurate)
# ============================================================
print("\nPHASE 3: Fixing Cadia AISC reference...")

# Fix the MINES tab insight_callout
for i in range(len(lines)):
    if "Cadia at $400/oz AISC" in lines[i]:
        lines[i] = lines[i].replace(
            "Cadia at $400/oz AISC is one of the world's lowest-cost gold mines",
            "Cadia historically operated at deeply negative to ~$400/oz AISC (Newcrest era, by-product) — now in cave transition at higher costs but with 150 kt Cu/yr expansion ahead"
        )
        print(f"  Fixed Cadia AISC reference at line {i+1}")
        break

# Fix RISK tab $1,558 reference
for i in range(len(lines)):
    if "$1,558" in lines[i] or "1,558" in lines[i]:
        lines[i] = lines[i].replace("$1,558", "$1,700").replace("1,558", "1,700")
        print(f"  Fixed $1,558 → $1,700 at line {i+1}")
        # Don't break — there might be multiple references
for i in range(len(lines)):
    if "~$1,55" in lines[i]:
        lines[i] = lines[i].replace("~$1,55", "~$1,70")
        print(f"  Fixed ~$1,55x → ~$1,70x at line {i+1}")

# ============================================================
# PHASE 4: Expand CATALYST tab (add chart + timeline)
# ============================================================
print("\nPHASE 4: Expanding CATALYST tab...")

# Find the catalyst summary box end and source_footer
idx = find_line("source_footer", find_line("tabs[10]:"))
if idx != -1:
    catalyst_expansion = '''
    # Catalyst Expected Value Waterfall
    st.markdown('<div class="panel-header">CATALYST EXPECTED VALUE — WATERFALL</div>', unsafe_allow_html=True)
    cat_names_c = [c['Catalyst'] for c in catalysts if c['Status'] != 'COMPLETED']
    cat_evs_c = [c['Impact'] * c['Prob'] for c in catalysts if c['Status'] != 'COMPLETED']
    cat_colors_c = [COLORS['green'] if c['Cat'] == 'Operations' else (COLORS['blue'] if c['Cat'] == 'Valuation' else COLORS['amber']) for c in catalysts if c['Status'] != 'COMPLETED']
    fig_cat = go.Figure()
    fig_cat.add_trace(go.Bar(y=cat_names_c, x=cat_evs_c, orientation='h', marker_color=cat_colors_c,
        text=[f"${ev:.2f}/sh" for ev in cat_evs_c], textposition='outside',
        textfont=dict(color=COLORS['text'], size=10)))
    fig_cat.add_vline(x=0, line_color=COLORS['border'], line_width=1)
    fig_cat.add_annotation(text=f'<b>Total: ${sum(cat_evs_c):.2f}/sh</b>', x=max(cat_evs_c), y=len(cat_names_c)-1, showarrow=False, font=dict(size=11, color=COLORS['green']), xanchor='left', xshift=10)
    apply_layout(fig_cat, "PROBABILITY-WEIGHTED EXPECTED VALUE PER CATALYST", 350)
    fig_cat.update_layout(yaxis=dict(autorange='reversed'), xaxis=dict(title='Expected Value ($/share)'))
    st.plotly_chart(fig_cat, use_container_width=True)

    # Catalyst Timeline
    st.markdown(\\'\\'\\'<div class="panel-header">CATALYST TIMELINE — WHEN DOES EACH TRIGGER?</div>\\'\\'\\', unsafe_allow_html=True)
    timeline_qs = ['Q2 2026', 'Q3 2026', 'Q4 2026', 'Q1 2027']
    for tq in timeline_qs:
        tq_cats = [c for c in catalysts if c['Q'] == tq and c['Status'] != 'COMPLETED']
        if not tq_cats:
            continue
        cat_list = ' | '.join([f"<span style=\\"color:{COLORS['green'] if c['Cat']=='Operations' else COLORS['blue']};font-weight:600;\\">{c['Catalyst']}</span> (+${c['Impact']*c['Prob']:.2f}/sh)" for c in tq_cats])
        st.markdown(f\\'\\'\\'
        <div style="background:#161b22;border:1px solid #30363d;border-left:3px solid {COLORS['blue']};padding:10px 16px;margin-bottom:6px;">
          <div style="display:flex;justify-content:space-between;align-items:center;">
            <span style="color:#58a6ff;font-size:11px;font-weight:700;">{tq}</span>
            <span style="color:#e6edf3;font-size:10px;">{cat_list}</span>
          </div>
        </div>\\'\\'\\', unsafe_allow_html=True)

'''
    # This is complex — let me use a simpler approach
    pass

# Actually, the catalyst expansion is tricky with escaping. Let me write it to a separate file and inject.
print("  Catalyst expansion will be handled via direct file edit")

# ============================================================
# PHASE 5: Add STORY tab WMIM
# ============================================================
print("\nPHASE 5: Adding STORY tab opening callout...")
idx = find_line("with tabs[0]:")
if idx != -1:
    # Find the first st.markdown after tabs[0]
    first_content = find_line("st.markdown", idx + 1)
    if first_content != -1:
        story_wmim = '''    st.markdown("""
    <div style="background:#0d1117;border:2px solid #58a6ff;padding:14px 20px;margin-bottom:16px;">
      <div style="color:#58a6ff;font-size:9px;letter-spacing:2.5px;text-transform:uppercase;margin-bottom:6px;font-weight:700;">WHAT THE MARKET IS MISSING</div>
      <div style="color:#e6edf3;font-size:12px;line-height:1.6;font-weight:500;">The market prices NEM as if gold is $3,605/oz — 21% below spot. Three structural catalysts go unmodeled: (1) zero gold discoveries in 2023-2024 with 17.8-year lead times, (2) copper optionality from Cadia worth ~$8-10/share, (3) management execution converging from -11.8% to -0.2% guidance miss.</div>
    </div>""", unsafe_allow_html=True)
'''
        insert_before(first_content, story_wmim)
        print(f"  Added STORY WMIM before line {first_content+1}")

# ============================================================
# SAVE
# ============================================================
print(f"\nWriting {len(lines)} lines to {APP}...")
with open(APP, 'w') as f:
    f.writelines(lines)
print("DONE!")
