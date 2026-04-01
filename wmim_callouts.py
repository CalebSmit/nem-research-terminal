"""
Define the "WHAT THE MARKET IS MISSING" callout HTML for each tab.
This is a reusable function that generates the styled callout.
"""

def wmim_html(text):
    """Generate a WHAT THE MARKET IS MISSING callout box."""
    return f'''
    <div style="background:#0d1117;border:2px solid #58a6ff;padding:14px 20px;margin-bottom:16px;">
      <div style="color:#58a6ff;font-size:9px;letter-spacing:2.5px;text-transform:uppercase;margin-bottom:6px;font-weight:700;">WHAT THE MARKET IS MISSING</div>
      <div style="color:#e6edf3;font-size:12px;line-height:1.6;font-weight:500;">{text}</div>
    </div>'''

# Tab-specific WMIM callouts
WMIM = {
    0: None,  # STORY — narrative tab, gets it differently
    1: None,  # CMD — already has one
    2: wmim_html("Central banks added 1,045t of gold in 2024 — the third consecutive year above 1,000t, vs. a pre-2022 average of ~473t/yr. This 2× structural demand shift puts a floor under gold that most equity models haven't incorporated."),
    3: wmim_html("NEM's gross margin tripled from 10% (2023) to 50% (2025). This isn't just gold prices — it's the structural effect of divesting 6 high-cost mines and retaining only Tier 1 assets. The margin expansion is durable."),
    4: wmim_html("After the Newcrest acquisition, NEM divested 6 non-core mines to focus on Tier 1 assets only. The remaining portfolio averages $1,358/oz AISC vs. the global industry average of ~$1,456/oz — a structural cost advantage."),
    5: wmim_html("Our DCF uses $5,200/oz gold — deliberately 10% below spot — and still produces $149/share. The margin of safety is in the assumptions, not the gold price."),
    6: wmim_html("NEM trades at 7.9× EV/EBITDA vs. peer median of 10.0×. A simple re-rating to the group — without any gold thesis — implies ~$130/share."),
    7: wmim_html("NEM generates positive FCF at any gold price above ~$1,700/oz (AISC $1,358 + capex/overhead). With gold at $4,576, the margin of safety is $2,876/oz — a 63% buffer before the thesis breaks."),
    8: wmim_html("76.4% of 50,000 Monte Carlo simulations produce a price above $107.80. The median outcome ($135.28) exceeds current price by 25% — the market is priced below the mathematical center of the distribution."),
    9: wmim_html("NEM returned $3.4B to shareholders in 2025 ($2.3B buybacks + $1.1B dividends) while simultaneously reaching $7.2B net cash. This dual mandate — returns AND balance sheet strength — signals peak financial health."),
    10: wmim_html("Eight forward catalysts add ~$30/share in probability-weighted expected value. The four operational catalysts alone (Cadia expansion, production inflection, Lihir, Ahafo North) contribute ~$19/share — none require gold price appreciation."),
    11: wmim_html("5 of 8 alternative data channels confirm the bull thesis. The 2 bearish signals (insider selling pattern, Ghana royalty risk) are included with full transparency — intellectual honesty, not cheerleading."),
    12: wmim_html("#1 Bloomberg ESG Transparency in the S&amp;P 500. 99th percentile S&amp;P CSA. $30T+ in ESG-mandated capital globally increasingly flows to best-in-class operators — NEM is the beneficiary in gold mining."),
    13: None,  # CREDIBILITY — just rewritten, already strong
    14: wmim_html("Four independent methods (DCF $149, P/NAV $112, MC Sim $135, Rel Val ~$130) converge on the same zone. The reverse DCF reveals the market embeds $3,605/oz gold — 21% below spot. Convergence reduces model risk."),
    15: wmim_html("GLD captures $0.40/oz in fees. NEM captures $2,896/oz in FCF margin. That's 7,240× the economic capture per ounce of gold exposure — with a dividend and copper optionality that GLD can never provide."),
    16: wmim_html("AI data centers projected to add 330,000–1,000,000+ tonnes of new copper demand by 2030 (IEA, Trafigura). Cadia's expansion to 150 kt Cu/yr makes NEM a backdoor AI infrastructure play invisible to gold-focused models."),
    17: wmim_html("Viljoen inherits the strongest balance sheet in NEM history: $7.2B net cash, Piotroski 9/9, completed Tier 1 portfolio. The restructuring is done — 2026 is the execution test."),
    18: wmim_html("ROIC 19.6% vs. WACC 7.04% = 12.6pp value creation spread. NEM generates $0.13 of economic profit per dollar of invested capital — rare in mining, where most peers destroy value."),
}
