# COMPETITIVE ANALYSIS — NEM RESEARCH TERMINAL

**Reviewer perspective:** Finance & CS double major, MIT. Finalist-round scouting report.
**Date:** 2026-04-02

---

## WHAT IMPRESSES ME / WHAT I WOULD STEAL

**The Reverse DCF framing is the single best idea in the submission.** Tab 01 (STORY) opens with "The Market Is Pricing Newmont as If Gold Falls to $3,605. I Spent a Week Figuring Out Whether That's Right. It Isn't." That sentence does more work than most teams' entire pitch decks. It reframes the thesis from "NEM is cheap" (consensus, boring) to "the market is making an implicit bet on gold reversion — is that bet correct?" (falsifiable, contrarian). I would steal this framing wholesale and apply it to my own ticker.

**The 8 AI channel checks (Tab 12: ALT DATA) are genuine differentiation.** Specifically: the insider selling deep-dive (81 Form 4 filings, David Fry's unconfirmed 10b5-1 sale, NEM fell 7.1% the next day — Tab 01, line ~1214) and the Ghana royalty quantification (+$50/oz on total NEM AISC, excluded from guidance, enacted Mar 9 — Tab 02: CMD, "Our View vs. Consensus" grid) are the kind of granular, falsifiable, non-consensus claims that win competitions. The inclusion of bearish findings (insider selling, Ghana royalty, Cadia class action, Tanami fatality) in the STORY tab is intellectually honest in a way most pitches are not.

**The assumption transparency engine (sidebar + 38 DEFAULTS with why/source metadata) is technically the most impressive feature.** Every slider has a documented rationale, source, and color-coded deviation badge. This is a Bloomberg Terminal feature that no other Streamlit submission will have. The `why_expander()` pattern at `app.py:620-629` is clean and reusable.

**Management credibility study (Tab 14: CREDIBILITY)** — 10-year guidance vs. actual with two-era decomposition (pre-Goldcorp vs. post-Goldcorp) and the convergence from -11.8% to -0.2%. The -2.9% haircut on production is the kind of quantified skepticism judges remember.

---

## WEAKNESSES / WHAT I WOULD ATTACK

**No explicit variant-perception framework.** The "Our View vs. Consensus" grid (Tab 02: CMD) lists three non-consensus calls but never says: "Here is what we believe, here is what the market believes, here is the evidence weighting, and here is the catalyst that closes the gap with a date." A strong attacker presents after this team and says: "Their thesis is correct but has no timeline. When does the gap close? What triggers repricing?"

**No disconfirming-evidence section with kill criteria.** Tab 01 has "WHAT ALMOST KILLED THE THESIS" but never states: "If X happens, the thesis is wrong and we exit." Specifically: what gold price kills the thesis? What AISC print at Q1 earnings (Apr 23) invalidates the model? What insider buying threshold would flip the signal? Without explicit kill criteria, the pitch reads as conviction without discipline.

**The closing is buried.** Tab 15 (VERDICT) has a strong convergence framework and conviction meter, but there is no 30-second "judge summary" panel that a reviewer can screenshot. The competition footer (lines 5857-5870) lists features but not the thesis conclusion. A judge skimming tabs sees "NEM EQUITY RESEARCH TERMINAL v2" and stats — not "BUY NEM, $145 target, +34% upside, 4 methods converge."

**Source confidence signaling is absent.** Every `source_footer()` says "Source: X | As of Mar 31, 2026" but never grades the confidence: is that source a 10-K filing (audited), an analyst estimate (consensus), a LinkedIn scrape (anecdotal), or a Perplexity search (unverified)? Mixing audited financials with job-posting scrapes at the same credibility level is a weakness a sharp judge will notice.

**Evidence hierarchy is flat.** All 20 tabs have equal visual weight. The five most important panels (reverse DCF gap, channel check scorecard, credibility miss trend, convergence bar chart, scenario asymmetry) should be visually distinguished from the supporting evidence. Currently, Tab 17 (COPPER) and Tab 18 (MGMT) get the same treatment as Tab 15 (VERDICT).

---

## WHAT I WOULD DO TO MAKE MY SUBMISSION BETTER

Add an "Executive Summary for Judges" as the first thing visible — above the story arc nav. Five lines: ticker, recommendation, target, upside, the single-sentence thesis, and the key variant perception with catalyst date. Make it impossible to miss in a 10-second scan.

Add explicit kill criteria: "We exit if gold falls below $X for 3 consecutive months, if Q1 AISC prints above $Y, or if insider buying remains zero through Q2."

Add a source confidence tier system: Tier 1 (audited filings), Tier 2 (consensus estimates), Tier 3 (alternative data / AI-gathered). Apply to every source footer.

---

## WHAT THIS SUBMISSION DOES NOT DO THAT A WINNING ENTRY SHOULD

1. **No position sizing or portfolio context.** A winning pitch says: "Size this at 3-5% of AUM because the Kelly criterion on our probability distribution implies X." This submission models NEM in isolation.
2. **No catalyst timeline with probability-weighted dates.** Tab 11 (CATALYST) has probability-weighted EV but no calendar visualization showing when each catalyst resolves and what to watch for at each date.
3. **No explicit comparison to alternative investments.** "Why NEM and not GLD, GOLD, AEM, or copper futures?" Tab 16 (GLD CMP) partially addresses GLD but doesn't explain why NEM beats Barrick or Agnico on a risk-adjusted basis.

---

## HOW WORRIED AM I?

**7/10.** This is a top-3 submission. The reverse DCF framing, channel checks, credibility study, and assumption transparency engine are genuine edges. The weaknesses are fixable in hours (kill criteria, judge summary, source tiers). If I'm presenting after this team, I need to either (a) match their analytical depth with my own ticker or (b) attack the timeline/catalyst gap hard. The most dangerous thing about this submission is that it's honest about its weaknesses — which makes it hard to attack on intellectual honesty grounds. My main angle of attack: "They found the mispricing but can't tell you when it corrects."
