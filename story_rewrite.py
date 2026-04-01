#!/usr/bin/env python3
"""Replace the STORY tab content (lines 935-1092) with the new first-person narrative."""

import pathlib

app_path = pathlib.Path("/home/user/workspace/nem_terminal/app.py")
lines = app_path.read_text().splitlines(keepends=True)

# Lines 935-1092 (1-indexed) = indices 934-1091 (0-indexed)
# We keep everything before line 935 and from line 1093 onward
before = lines[:934]   # lines 1-934
after = lines[1092:]   # lines 1093+

new_story = r'''with tabs[0]:
    B = BASE
    st.markdown(f"""
    <div style="background:#161b22;border:1px solid #30363d;padding:28px 24px 20px 24px;margin-bottom:20px;">
      <div style="color:#58a6ff;font-size:11px;letter-spacing:3px;text-transform:uppercase;margin-bottom:12px;">HOW WE GOT HERE</div>
      <div style="color:#e6edf3;font-size:20px;font-weight:700;line-height:1.4;margin-bottom:8px;">
        The Market Is Pricing Newmont as If Gold Falls to $3,605. I Spent a Week Figuring Out Whether That's Right. It Isn't.</div>
      <div style="color:#8b949e;font-size:11px;line-height:1.6;">
        This is a first-person account of how I used Perplexity Computer to build a differentiated thesis
        on the world's largest gold miner. Not a polished pitch deck &mdash; an honest research narrative,
        including the parts that scared me.</div>
    </div>
    """, unsafe_allow_html=True)

    # The Starting Point
    st.markdown(f"""
    <div style="background:#0d1117;border-left:3px solid #58a6ff;padding:16px 20px;margin-bottom:16px;">
      <div style="color:#58a6ff;font-size:12px;font-weight:700;letter-spacing:1px;margin-bottom:10px;">THE STARTING POINT</div>
      <div style="color:#e6edf3;font-size:11px;line-height:1.8;">
        I started where everyone starts: a DCF model that said Newmont was cheap. $149.24 implied value
        versus $107.80 market price. Fine. Every team in this competition will have a DCF that says NEM
        is undervalued. That's the consensus view dressed up in a spreadsheet.
        <br><br>
        The interesting part came when I ran the model backward. I asked: what gold price does the
        <i>market</i> need to believe to justify the current stock price? The answer was
        <b style="color:#f85149;">${{B['implied_gold']:,.0f}}/oz</b> &mdash; a
        <b style="color:#f85149;">{B['gold_gap_pct']:.0f}% discount</b> to the current spot
        of ${B['gold_spot']:,}/oz. That's not a small disagreement. That's the market saying gold is
        going back to 2023 levels and staying there. I wanted to know if the market knew something I didn't,
        or if it was just wrong.
      </div>
    </div>
    """, unsafe_allow_html=True)

    # The 8 Channel Checks
    st.markdown("""
    <div style="background:#0d1117;border-left:3px solid #3fb950;padding:16px 20px;margin-bottom:16px;">
      <div style="color:#3fb950;font-size:12px;font-weight:700;letter-spacing:1px;margin-bottom:10px;">THE 8 CHANNEL CHECKS</div>
      <div style="color:#e6edf3;font-size:11px;line-height:1.8;">
        So I ran 8 alternative data channel checks using Perplexity Computer &mdash; the kind of research
        that usually costs a Bloomberg terminal, an expert network subscription, and a team of junior analysts.
        Here's what actually happened:
        <br><br>
        <b style="color:#3fb950;">Job postings.</b> I went to jobs.newmont.com expecting to find post-restructuring
        attrition &mdash; a company still shrinking after its portfolio cleanup. Instead I found 121 open positions.
        Graduate engineering roles at Cadia. Construction managers at Ahafo North. A structural engineer at Lihir
        posted <i>days</i> after the $550M nearshore tailings barrier got approved. These aren't maintenance hires.
        This is a company building.
        <br><br>
        <b style="color:#3fb950;">Analyst revisions.</b> 4 upgrades, 0 downgrades in 6 months. Average target up 64%
        from ~$75 to $123. Bernstein initiated at $157. The Street is rotating bullish, but consensus ($123) still
        trails our model ($137.93) by 12%.
        <br><br>
        <b style="color:#3fb950;">Earnings call tone.</b> I scored the tone of Q1&ndash;Q4 2025 transcripts.
        It went from 3.6 (cautious) in Q2 to 4.5 (confident) by Q3. The moment that caught my attention:
        analysts on both Q2 and Q3 calls explicitly asked management if guidance was "too conservative."
        When sell-side analysts start questioning whether you're sandbagging, something has shifted.
        <br><br>
        <b style="color:#3fb950;">The copper surprise.</b> This one I didn't expect. AI data centers use
        27&ndash;33 tonnes of copper per MW. With 124 GW of AI capacity to be built by 2030, that's 3.5&ndash;4.1M
        tonnes of cumulative copper demand. Newmont's Cadia mine produces 82 kt Cu/yr, expanding to 150 kt.
        That makes NEM a backdoor AI infrastructure play that no pure gold miner can match. I don't think the
        gold-focused market is pricing this at all.
      </div>
    </div>
    """, unsafe_allow_html=True)

    # What Almost Killed the Thesis
    st.markdown("""
    <div style="background:#0d1117;border-left:3px solid #d29922;padding:16px 20px;margin-bottom:16px;">
      <div style="color:#d29922;font-size:12px;font-weight:700;letter-spacing:1px;margin-bottom:10px;">WHAT ALMOST KILLED THE THESIS</div>
      <div style="color:#e6edf3;font-size:11px;line-height:1.8;">
        Around check #5, I found the stuff that made me uncomfortable.
        <br><br>
        <b style="color:#f85149;">Insider selling.</b> Zero insider purchases in 12 months. 21 sales totaling $7.6M.
        When nobody on the inside is buying, that's not a great sign. I almost stopped here. But I dug into
        the Form 4s: 100% of the sales were pre-scheduled 10b5-1 plans, not discretionary dumps. Still &mdash;
        absence of buying is absence of conviction. I flag it as neutral-bearish.
        <br><br>
        <b style="color:#f85149;">Ghana royalty.</b> On March 10, 2026, Ghana enacted a sliding-scale royalty
        that adds roughly +$50/oz to AISC at Ahafo. The important detail: NEM already excluded Ghana from
        their current-year guidance, so the financial hit is flagged but not a model-breaker at $3,218/oz margins.
        <br><br>
        <b style="color:#f85149;">Cadia class action.</b> 2,000 plaintiffs. Arsenic and PFAS contamination claims.
        Filed February 2026 in NSW Supreme Court. This is a real liability, not a nuisance suit.
        <br><br>
        <b style="color:#f85149;">Tanami fatality.</b> A worker died at Tanami in February 2026.
        Regulatory scrutiny followed. This is the kind of event that doesn't show up in a DCF but
        shapes operating risk for quarters.
        <br><br>
        I built all four of these into the Risk tab. None of them broke the thesis individually. But together
        they explain why the stock trades at a discount &mdash; and why that discount is larger than it should be.
      </div>
    </div>
    """, unsafe_allow_html=True)

    # The Credibility Question
    st.markdown("""
    <div style="background:#0d1117;border-left:3px solid #58a6ff;padding:16px 20px;margin-bottom:16px;">
      <div style="color:#58a6ff;font-size:12px;font-weight:700;letter-spacing:1px;margin-bottom:10px;">THE CREDIBILITY QUESTION</div>
      <div style="color:#e6edf3;font-size:11px;line-height:1.8;">
        Before I put any weight on forward guidance, I tested whether NEM management deserves the
        benefit of the doubt. I pulled 6 years of initial guidance vs. actual results (2020&ndash;2025)
        for production, AISC, and CapEx.
        <br><br>
        <b>The honest answer: they missed production guidance 6 out of 6 years.</b> A 0% beat rate. Average miss
        of &minus;5.4%. That's bad. But the trajectory tells a different story: the miss compressed from
        &minus;11.8% in 2020 to &minus;0.2% in 2025. They went from serial disappointment to essentially hitting the number.
        <br><br>
        For context: Barrick (GOLD) also has a 0% beat rate with a worse &minus;5.4% average miss.
        Agnico Eagle (AEM) beats 40% of the time. NEM is improving but hasn't earned Agnico-level trust.
        <br><br>
        I haircut our production estimate to 5.09 Moz to reflect this. At $4,576 gold, each 100 Koz
        of production variance equals roughly $290M in FCF. The credibility gap changes the precision
        of the estimate, not the direction.
      </div>
    </div>
    """, unsafe_allow_html=True)

    # The Punchline
    st.markdown(f"""
    <div style="background:#161b22;border:2px solid #3fb950;padding:24px;margin-bottom:16px;">
      <div style="color:#3fb950;font-size:12px;font-weight:700;letter-spacing:2px;text-align:center;margin-bottom:14px;">THE PUNCHLINE</div>
      <div style="color:#e6edf3;font-size:12px;line-height:1.8;text-align:center;">
        Target: <b style="color:#3fb950;font-size:14px;">${{B['blended_target']:.2f}}</b> &nbsp;|&nbsp;
        Upside: <b style="color:#3fb950;font-size:14px;">{B['upside']:+.1f}%</b> &nbsp;|&nbsp;
        Rating: <b style="color:#3fb950;font-size:14px;">BUY</b>
        <br><br>
        <span style="color:#e6edf3;">Three independent methods &mdash; DCF modeling, 8 alternative data channel checks,
        and a management credibility study &mdash; all converge on the same conclusion.
        NEM is materially undervalued.</span>
        <br><br>
        <span style="color:#8b949e;">The question isn't whether NEM reaches our target. The question is whether
        you believe gold permanently reverts to ${{B['implied_gold']:,.0f}}. Everything I found says it won't.</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Bear Case Preemption
    st.markdown(f"""
    <div style="background:#0d1117;border:1px solid #30363d;border-left:3px solid {COLORS['red']};padding:16px 20px;margin-bottom:16px;">
      <div style="color:{COLORS['red']};font-size:11px;font-weight:700;letter-spacing:1px;margin-bottom:8px;">THE BEAR CASE I TOOK SERIOUSLY</div>
      <div style="color:#e6edf3;font-size:11px;line-height:1.8;">
        <b>"You're just riding the gold price."</b> &mdash; If gold falls 27% to $3,605/oz (the price the market implies),
        NEM's AISC of $1,358/oz still produces $2,247/oz margin &mdash; positive FCF in every scenario above $1,558/oz.
        This is not a hope trade. It's an asymmetric margin-of-safety play.<br>
        <b>"Management is new and unproven."</b> &mdash; Correct. Viljoen started Jan 2026. But she inherits net cash of $7.2B,
        Piotroski 9/9, and a completed portfolio transformation. The hard work is done.
        Track 2026 guidance delivery as the validation trigger.<br>
        <b>"Insider selling is a red flag."</b> &mdash; I agree it's cautionary. Zero purchases and 21 sales ($7.6M)
        in 12 months. But 100% were systematic 10b5-1 plans, not discretionary liquidations.
        I still flag it as neutral-bearish because absence of buying is absence of conviction.
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Navigation guide
    st.markdown("""
    <div style="background:#161b22;border:1px solid #30363d;padding:16px 20px;">
      <div style="color:#8b949e;font-size:10px;letter-spacing:2px;text-transform:uppercase;margin-bottom:10px;">WHERE TO GO FROM HERE</div>
      <div style="color:#e6edf3;font-size:10px;line-height:1.8;">
        <b style="color:#58a6ff;">01&middot;CMD</b> &mdash; The dashboard. Key metrics, thesis statement, what the market is missing.<br>
        <b style="color:#58a6ff;">05&middot;DCF</b> &mdash; Full 5-year FCFF model. Every assumption is overridable.<br>
        <b style="color:#58a6ff;">07&middot;RISK</b> &mdash; Scenario analysis including the alt-data risks I found.<br>
        <b style="color:#58a6ff;">11&middot;ALT DATA</b> &mdash; All 8 channel checks with raw findings and signal ratings.<br>
        <b style="color:#58a6ff;">13&middot;CREDIBILITY</b> &mdash; The 6-year guidance study. The charts that almost killed the thesis.<br>
        <b style="color:#58a6ff;">14&middot;VERDICT</b> &mdash; Convergence framework. Four independent methods, one conclusion.
      </div>
    </div>
    """, unsafe_allow_html=True)
    source_footer("Primary Research: NEM 10-K/10-Q/8-K Filings, SEC Form 4, Earnings Transcripts Q1-Q4 2025, jobs.newmont.com, LinkedIn, Perplexity Finance, BHP, McKinsey, JPMorgan, IEA, ICSG, S&P Global, Ghana Minerals Commission, NSW Supreme Court | Mar 31, 2026")

'''

# Convert new_story to lines
new_lines = [line + '\n' for line in new_story.split('\n')]

# Combine
result = before + new_lines + after
app_path.write_text(''.join(result))

print(f"Done. Original lines 935-1092 ({1092-935+1} lines) replaced with {len(new_lines)} new lines.")
print(f"Total file now has {len(result)} lines.")
