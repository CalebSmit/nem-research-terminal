#!/usr/bin/env python3
"""Update STORY tab and CMD CENTER references to match new credibility findings."""

app_path = "/home/user/workspace/nem_terminal/app.py"

with open(app_path, "r") as f:
    content = f.read()

replacements = [
    # 1. THE CREDIBILITY QUESTION section — full rewrite of the content block
    (
        """        Before I put any weight on forward guidance, I tested whether NEM management deserves the
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
        of the estimate, not the direction.""",
        """        Before I put any weight on forward guidance, I tested whether NEM management deserves the
        benefit of the doubt. I pulled 10 years of initial guidance vs. actual results (2015&ndash;2025,
        excluding 2019's Goldcorp structural break) for production and AISC.
        <br><br>
        <b>The honest answer: they beat production guidance in only 2 of 10 comparable years</b> (2016 and 2017,
        both pre-Goldcorp). Average miss: &minus;3.5%. But two distinct eras emerge. Pre-Goldcorp (2015-2018),
        NEM was a disciplined B+ operator with a &minus;0.8% average miss. Post-Goldcorp (2020-2025), the Goldcorp
        integration destroyed that track record: &minus;5.4% average miss, 0 beats. The trajectory tells the real story:
        &minus;11.8% in 2020 &rarr; &minus;0.2% in 2025. The integration tax is being paid down.
        <br><br>
        For context: Barrick (GOLD) averaged &minus;3.8% vs. midpoint with 2 outright misses in 6 years.
        Agnico Eagle (AEM) is the gold standard &mdash; +0.1% average deviation post-merger, never missed
        (excl. 2020 COVID force majeure). NEM's recent trajectory is converging toward Barrick-level, not yet AEM-level.
        <br><br>
        I haircut our production estimate to 5.11 Moz (&minus;2.9% vs. guided 5.26 Moz). At $4,576 gold
        and $1,680 AISC, each 100 Koz of production variance equals ~$290M in FCF. The &minus;2.9% haircut
        puts $443M of FCF at risk vs. guidance &mdash; that's the credibility gap, quantified."""
    ),

    # 2. WHERE TO GO FROM HERE — "6-year" → "10-year"
    (
        """<b style="color:#58a6ff;">13&middot;CREDIBILITY</b> &mdash; The 6-year guidance study. The charts that almost killed the thesis.""",
        """<b style="color:#58a6ff;">13&middot;CREDIBILITY</b> &mdash; The 10-year guidance study. The charts that almost killed the thesis."""
    ),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"OK: Replaced '{old[:60]}...'")
    else:
        print(f"WARN: Could not find '{old[:60]}...'")

with open(app_path, 'w') as f:
    f.write(content)

print("\nDone. Story tab references updated.")
