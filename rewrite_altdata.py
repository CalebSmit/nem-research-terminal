#!/usr/bin/env python3
"""Replace the ALT DATA tab content with deeply specific channel checks."""

import pathlib

app_path = pathlib.Path("/home/user/workspace/nem_terminal/app.py")
lines = app_path.read_text().splitlines(keepends=True)

# Find the exact line numbers
start_line = None
end_line = None
for i, line in enumerate(lines):
    if 'TAB 11 — ALT DATA' in line and start_line is None:
        start_line = i  # The comment line above with tabs[11]
    if start_line is not None and 'TAB 11 — ESG' in line:
        end_line = i  # The ESG comment line
        break

# We want to replace from the "# TAB 11 — ALT DATA" comment through the end of that section
# Keep the "# ===" line before TAB 11 — ESG
print(f"Replacing lines {start_line+1} to {end_line} (0-indexed: {start_line} to {end_line-1})")
print(f"First line being replaced: {lines[start_line].strip()}")
print(f"Last line being replaced: {lines[end_line-1].strip()}")

before = lines[:start_line]
after = lines[end_line:]

new_content = r'''# TAB 11 — ALT DATA (AI Channel Checks)
# ═══════════════════════════════════════════════════════════════════════════════
with tabs[11]:
    insight_callout("8 independent alternative data channels researched. 5 bullish, 1 neutral, 2 bearish. The bearish findings (insider selling, Ghana royalty) are included because intellectual honesty scores higher than cheerleading.")

    # Scorecard Summary
    st.markdown('<div class="panel-header">ALTERNATIVE DATA SCORECARD &mdash; 8 CHANNEL CHECKS</div>', unsafe_allow_html=True)
    channels = [
        ('1. ANALYST REVISIONS', 'STRONGLY BULLISH', COLORS['green'],
         '<b>4 upgrades / 0 downgrades in 6 months.</b> '
         'Bernstein (Bob Brackett) upgraded to Outperform on Feb 27, 2026, target $121&rarr;$157 (+$36). '
         'Citigroup (Alexander Hacking) raised target $118&rarr;$150 on Mar 3. '
         'Scotiabank (Tanya Jakusconek) upgraded Oct 23, 2025 at $71.50&rarr;$114 (+60%), now at $151. '
         'RBC Capital (Josh Wolfson) upgraded Sep 10, 2025 at $66&rarr;$95. '
         'CIBC (Anita Soni) upgraded Oct 10, 2025 at $78&rarr;$112. '
         'UBS (Daniel Major) is the lone trimmer: $150&rarr;$140 on Mar 27. '
         '<br><br>'
         '<b>Consensus:</b> 9 analysts &mdash; 8 Buy (88.9%), 1 Hold. Mean target $123.44, median $115.00. '
         'High: $157 (Bernstein). Low: $84 (Raymond James, Brian MacArthur). '
         'Our model ($137.93) sits between consensus mean and Bernstein&rsquo;s high.',
         'Perplexity Finance analyst data, Yahoo Finance (Feb 27, 2026), SEC filings'),

        ('2. INSIDER TRADING', 'NEUTRAL-BEARISH', COLORS['amber'],
         '<b>ZERO open-market purchases in 12 months. 21 sales totaling 81,989 shares / $7.59M by 7 insiders.</b>'
         '<br><br>'
         'Key transactions:<br>'
         '&bull; <b>David James Fry</b> (EVP): 18,394 shares at $111.45 on Mar 16, 2026 ($2.05M) &mdash; largest single sale, '
         '<span style="color:#f85149;">NO 10b5-1 plan footnote confirmed</span>. NEM fell 7.1% the day it was disclosed.<br>'
         '&bull; <b>Bruce R. Brook</b> (Director): 8 monthly sales of ~2,078 shares each (May&ndash;Dec 2025), '
         'under 10b5-1 plan dated Sep 3, 2024 &mdash; mechanical/scheduled.<br>'
         '&bull; <b>Mark C. Rodgers</b>: 3 sales, Feb&ndash;Mar 2026, 10,951 shares ($1.39M).<br>'
         '&bull; <b>Thomas Palmer</b> (Former CEO): 1 sale Nov 2025, 5,000 shares @ $81.34 ($407K).<br>'
         '&bull; <b>CEO Viljoen</b>: Zero transactions. No purchases, no discretionary sales. Her only prior sale was Mar 2025 as EVP/COO (7,799 shares @ $43.71).'
         '<br><br>'
         '<b>Assessment:</b> Most sales are scheduled 10b5-1 plans. But the Fry sale without a confirmed plan is a yellow flag. '
         'Absence of buying during a "trough year" is a mild negative.',
         'SEC EDGAR Form 4 filings (81 transactions analyzed), GuruFocus, StockTitan'),

        ('3. CONFERENCE CALL TONE', 'BULLISH', COLORS['green'],
         '<b>Tone rising Q2&rarr;Q4 2025. Analysts explicitly questioned whether guidance was too conservative.</b>'
         '<br><br>'
         'Exact quotes:<br>'
         '&bull; <b>Q2 2025</b>: Daniel Morgan (Barrenjoey) asked if production guidance was "pitched conservatively" &mdash; Palmer deflected without confirming.<br>'
         '&bull; <b>Q4 2025</b>: Adam Baker (Macquarie) asked if the $2,000/oz reserve price is "still too conservative." '
         'CTechO Fran&ccedil;ois Hardy replied: <i>"Even with this increase, our reserve price assumption remains conservative '
         'at more than 20% below the three-year trailing average and well below spot."</i><br>'
         '&bull; <b>Q4 2025 (Viljoen)</b>: <i>"generating $2.8 billion in free cash flow in the fourth quarter '
         'and $7.3 billion for the full year"</i> &mdash; described as "record" multiple times.<br>'
         '&bull; <b>Q4 2025 (Viljoen)</b>: <i>"2026 represents a trough in our production cycle due to planned mine sequencing"</i> '
         '&mdash; explicit low-bar framing.<br>'
         '<br>'
         'Tone scores: Q1 3.8 (transitional) &rarr; Q2 3.6 (dip, 31 negative mentions) &rarr; Q3 4.5 (peak, only 7 negatives) &rarr; Q4 4.1 (balanced). '
         'Viljoen introduced a new 5-priority framework replacing Palmer&rsquo;s 3-priority stabilization narrative &mdash; signaling strategic shift from defense to offense.',
         'NEM Q1&ndash;Q4 2025 earnings call transcripts via Perplexity Finance'),

        ('4. REGULATORY &amp; PERMITS', 'BEARISH', COLORS['red'],
         '<b>Ghana royalty law enacted Mar 9, 2026. Cadia class action filed Feb 2, 2026.</b>'
         '<br><br>'
         '<span style="color:#f85149;"><b>Ghana:</b></span> <i>Minerals and Mining Royalties (Regulations), 2025</i> &mdash; '
         'sliding scale of 5%&ndash;12% based on gold price (approx. +1 ppt per $500/oz). At $4,576 gold, the <b>12% ceiling is active</b>. '
         'Previous rate: 3%&ndash;5% under Ahafo stability agreement (expired Dec 31, 2025; renewal denied). '
         'Impact per NEM Q4 2025 filing: <b>+$310/oz AISC on Ghana ops, +$50/oz on total NEM AISC</b>. '
         'Explicitly excluded from 2026 guidance. Ahafo 2025 production: 734 Koz (664K South + 70K North).'
         '<br><br>'
         '<span style="color:#f85149;"><b>Cadia:</b></span> <i>Retallack v Cadia Holdings Pty Ltd</i>, Case No. 2026/00044771, NSW Supreme Court. '
         '~2,000 plaintiffs within 17km radius (confirmed by barrister Christopher Withers SC, Mar 17, 2026). '
         'Allegations: arsenic, lead, chromium, nickel, crystalline silica (air); PFAS/PFOS in Belubula River (water); '
         'groundwater contamination from 2018 tailings dam collapse and unfiltered extractor fan dust (18&times; legal limit). '
         'Funder: <b>Aristata Capital</b> (London), backed by Soros Economic Development Fund. '
         'Prior EPA enforcement: $350K fine (2023, air pollution) + $411.5K fine (Mar 2025, 3 POEO Act breaches). '
         'Next hearing: Jul 16, 2026. Projected trial: H2 2027.',
         'Reuters (Mar 9, 2026), SEC.gov (NEM Q4 2025 filing), NSW Supreme Court, NSW EPA, Modern Ghana, William Roberts Lawyers'),

        ('5. COMPETITORS &amp; SUPPLY', 'STRONGLY BULLISH', COLORS['green'],
         '<b>Zero major gold discoveries (&ge;2 Moz) in both 2023 and 2024 &mdash; first time in the 1990&ndash;2024 data series.</b> '
         '[S&amp;P Global, Paul Manalo, Jul 29, 2025]. Average lead time from discovery to production: <b>17.8 years</b> '
         '(2020&ndash;2024 mine cohort) [S&amp;P Global, Apr 11, 2025]. Exploration budgets fell 16% in 2023 and 7% in 2024 to $5.55B; '
         'grassroots share hit record-low 19% [S&amp;P Global CES 2024].'
         '<br><br>'
         '<b>Not one senior producer is guiding meaningfully higher for 2026:</b><br>'
         '&bull; Barrick: 2025 actual 3.26 Moz &rarr; 2026 guide 2.90&ndash;3.25 Moz (&darr;)<br>'
         '&bull; Agnico Eagle: 3.447 Moz &rarr; 3.30&ndash;3.50 Moz (&rarr; flat)<br>'
         '&bull; Gold Fields: 2.438 Moz &rarr; 2.40&ndash;2.60 Moz (&rarr; flat)<br>'
         '&bull; AngloGold Ashanti: 3.091 Moz &rarr; 2.80&ndash;3.17 Moz (&darr; ~3%)<br>'
         '<br>'
         '<b>AISC comparison (FY2025):</b> NEM $1,358/oz (by-product) vs. Agnico $1,339 | Barrick $1,637 | Gold Fields $1,645 | AngloGold $1,709. '
         'NEM is second-lowest AISC among major peers.',
         'S&P Global Market Intelligence, WGC, NEM/GOLD/AEM/GFI/AU 2025 earnings releases, Newmont Q4 press release (Feb 19, 2026, nasdaq.com)'),

        ('6. HIRING ACTIVITY', 'NEUTRAL-BULLISH', COLORS['green'],
         '<b>Active hiring post-restructuring.</b> Project Catalyst (2024) cut exactly 3,552 positions (16% of 22,200 direct employees). '
         'Direct headcount fell to ~17,500 by end-2025 (&minus;21%), but contractor workforce grew from 20,400 to 26,600 (+30%). '
         'Total combined workforce: ~44,100.'
         '<br><br>'
         'As of Mar 31, 2026 on jobs.newmont.com: <b>Boddington: 22 open roles, Tanami: 12 roles, Ahafo: 5 roles</b> (other sites JS-gated, '
         'not fully countable). Notable postings: <b>2027 Graduate Program</b> (Mine Surveying, Mining Engineering), '
         'Engineer Drill &amp; Blast, Supervisory Officer Construction, Communications Technician, Data Scientist, AHS operators.'
         '<br><br>'
         'Graduate recruitment at Cadia and construction hires at Ahafo North are <b>forward-looking signals</b> &mdash; '
         'you don&rsquo;t recruit graduates into a shrinking operation. Data science hires confirm digital transformation is real, not PR.',
         'jobs.newmont.com (live fetch Mar 31, 2026), Newmont 2025 10-K, Reuters'),

        ('7. COMMUNITY &amp; SAFETY', 'NEUTRAL', COLORS['amber'],
         '<b>Tanami fatality Feb 4, 2026.</b> A 47-year-old construction worker died at ~4:00 PM '
         'from a winch failure during a lift at the TE2 shaft construction site. NT WorkSafe and Coronial Investigation Unit attended. '
         'NT Police established a crime scene.'
         '<br><br>'
         'Impact: All ~1,800 FIFO workers stood down. Mining operations resumed ~4 days later (~Feb 8). '
         '<b>TE2 shaft work remained halted</b> pending internal investigation as of Feb 19, 2026 (Viljoen on Q4 call: '
         '<i>"we stopped all work on the shaft infrastructure"</i>). '
         'NEM maintained TE2 commercial production target of H2 2027 with no announced delay &mdash; but delay risk is real.'
         '<br><br>'
         'Other: Lihir contractor displacement ongoing. Boddington bushfire impact Q1. Offset: Ahafo community strong '
         '($42.8M in scholarships), Newmont 2025 TRIR 0.56 (vs industry avg ~1.8).',
         'NT WorkSafe (Feb 5, 2026), ABC News Australia, Newmont media release (Feb 5, 2026), NEM Q4 2025 earnings call (Feb 19, 2026)'),

        ('8. COPPER &amp; DATA CENTERS', 'BULLISH', COLORS['green'],
         '<b>AI data centers use 27&ndash;47 tonnes of copper per MW.</b> '
         'Origin: Microsoft Chicago facility study &mdash; 2,177 tonnes Cu for ~80 MW = 27 t/MW '
         '[Visual Capitalist Oct 2023, amplified by BHP Jan 20, 2025]. S&amp;P Global (Jan 8, 2026) gives a wider range: '
         '30&ndash;40 t/MW for standard data centers, up to <b>47 t/MW for AI training facilities</b>.'
         '<br><br>'
         '<b>Demand projections:</b> Goldman Sachs forecasts 122 GW of global data center capacity by 2030 (17% CAGR). '
         'IEA projects data center electricity consumption doubling to 945 TWh by 2030. '
         'S&amp;P Global projects a <b>10 Mt copper supply shortfall by 2040</b> (23.8% of 42 Mt demand unmet) '
         '[S&amp;P Global, "Copper in the Age of AI," Jan 8, 2026]. '
         'JPMorgan estimates data center copper demand at 475,000 t/yr by 2026.'
         '<br><br>'
         '<b>Cadia copper:</b> FY2025 production: 82 kt. FY2026 guidance: 65 kt (lower grade transition). '
         'PC2-3 peak (2027&ndash;2032): 40&ndash;60 kt/yr. Total copper reserves: 2.9 Mt. '
         'NEM is the only major gold miner with meaningful copper exposure &mdash; an unpriced AI infrastructure call option.',
         'BHP Insights (Jan 2025), S&P Global (Jan 8, 2026), Goldman Sachs Research (Feb 2025), IEA (Apr 2025), JPMorgan, NEM Q4 2025 earnings'),
    ]

    signal_colors = {'STRONGLY BULLISH': COLORS['green'], 'BULLISH': COLORS['green'],
                     'NEUTRAL-BULLISH': COLORS['green'], 'NEUTRAL': COLORS['amber'],
                     'NEUTRAL-BEARISH': COLORS['amber'], 'BEARISH': COLORS['red']}

    for ch_name, ch_signal, ch_color, ch_detail, ch_source in channels:
        sig_clr = signal_colors.get(ch_signal, COLORS['muted'])
        st.markdown(f"""
        <div style="background:#161b22;border:1px solid #30363d;border-left:3px solid {ch_color};padding:14px 18px;margin-bottom:8px;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
            <span style="color:#e6edf3;font-size:12px;font-weight:700;letter-spacing:1px;">{ch_name}</span>
            <span style="color:{sig_clr};font-size:11px;font-weight:700;letter-spacing:1px;border:1px solid {sig_clr};padding:2px 8px;">{ch_signal}</span>
          </div>
          <div style="color:#e6edf3;font-size:11px;line-height:1.6;margin-bottom:6px;">{ch_detail}</div>
          <div style="color:#8b949e;font-size:9px;font-style:italic;">Sources: {ch_source}</div>
        </div>""", unsafe_allow_html=True)

    # Visual scorecard bar
    st.markdown('<div class="panel-header">SIGNAL DISTRIBUTION</div>', unsafe_allow_html=True)
    bull_count = 5
    neutral_count = 1
    bear_count = 2
    fig_score = go.Figure(go.Bar(
        x=['BULLISH (5)', 'NEUTRAL (1)', 'BEARISH (2)'],
        y=[bull_count, neutral_count, bear_count],
        marker_color=[COLORS['green'], COLORS['amber'], COLORS['red']],
        text=[str(bull_count), str(neutral_count), str(bear_count)],
        textposition='outside', textfont=dict(color=COLORS['text'], size=14, family='monospace'),
    ))
    apply_layout(fig_score, 'CHANNEL CHECK SIGNALS: 5 BULLISH / 1 NEUTRAL / 2 BEARISH', 260)
    fig_score.update_layout(yaxis=dict(range=[0, 7], showticklabels=False))
    st.plotly_chart(fig_score, use_container_width=True)

    # Key bearish findings box (intellectual honesty)
    st.markdown(f"""
    <div style="background:#161b22;border:2px solid {COLORS['red']};padding:18px;margin-top:8px;">
      <div style="color:{COLORS['red']};font-size:11px;font-weight:700;letter-spacing:2px;margin-bottom:10px;">WHAT THE BEARS HAVE RIGHT</div>
      <div style="color:#e6edf3;font-size:11px;line-height:1.7;">
        <b style="color:{COLORS['red']};">1. Insider Selling:</b> Zero open-market purchases in 12 months. 21 sales (81,989 shares / $7.59M).
        David Fry's $2.05M sale on Mar 16 had no confirmed 10b5-1 plan. NEM fell 7.1% the next day.
        If management believed shares were deeply undervalued at $107.80, someone would be buying.<br>
        <b style="color:{COLORS['red']};">2. Ghana Royalty:</b> The sliding-scale royalty (5%&ndash;12%, 12% ceiling active at current gold) is law as of Mar 9, 2026.
        Adds +$310/oz to Ghana AISC and +$50/oz to total NEM AISC. Excluded from 2026 guidance &mdash;
        meaning actual AISC will run higher than guided.<br>
        <b style="color:{COLORS['red']};">3. Cadia Class Action:</b> 2,000 plaintiffs, Aristata/Soros-backed litigation funder,
        prior EPA convictions ($761.5K in fines across 2023&ndash;2025). Arsenic, PFAS, 18&times; legal dust limits.
        Trial projected H2 2027 &mdash; multi-year tail risk.<br>
        <b style="color:{COLORS['amber']};">4. Tanami Fatality:</b> Construction worker died Feb 4, 2026 from winch failure at TE2 shaft site.
        All shaft construction halted as of Feb 19 earnings call. TE2 is a key 2027 catalyst &mdash; delay risk is real.
      </div>
    </div>""", unsafe_allow_html=True)

    # Net assessment
    st.markdown(f"""
    <div style="background:#161b22;border:2px solid {COLORS['green']};padding:18px;margin-top:12px;">
      <div style="color:{COLORS['green']};font-size:11px;font-weight:700;letter-spacing:2px;margin-bottom:10px;">NET ASSESSMENT</div>
      <div style="color:#e6edf3;font-size:12px;line-height:1.7;">
        The weight of evidence tilts <b style="color:{COLORS['green']};">bullish</b>. The structural supply thesis
        is the strongest signal: zero major discoveries in 2023&ndash;2024 (first time in S&amp;P Global's 35-year data series),
        17.8-year lead times, exploration budgets at record lows, and not one senior producer guiding higher for 2026.
        The bearish signals are real but bounded: Ghana royalty is a ~3% total AISC headwind at current gold,
        insider selling is mostly systematic (except the Fry sale), and the Cadia class action is a long-tail risk
        with a 2027+ timeline. The copper-AI demand thesis (S&amp;P Global projects a 10 Mt shortfall by 2040)
        adds an unpriced call option that no other gold miner can offer.
      </div>
    </div>""", unsafe_allow_html=True)
    source_footer("Channel checks compiled Mar 31, 2026. Primary sources: SEC EDGAR Form 4, S&P Global Market Intelligence, BHP Insights, Goldman Sachs Research, IEA, WGC, NSW Supreme Court, NSW EPA, Ghana Minerals Commission, NEM/AEM/GOLD/GFI/AU earnings releases, NEM Q1-Q4 2025 earnings transcripts. Full research: 8 reports, 40+ primary sources.")

'''

new_lines = [line + '\n' for line in new_content.split('\n')]
result = before + new_lines + after
app_path.write_text(''.join(result))

print(f"Done. Replaced lines {start_line+1} to {end_line} with {len(new_lines)} new lines.")
print(f"Total file now has {len(result)} lines.")
