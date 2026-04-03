# Bloomberg Terminal Design System — Full Specification

## COLOR SYSTEM (enforce exact hex values everywhere)
- Page background: #0d1117
- Panel and card backgrounds: #161b22
- Borders and dividers: #30363d
- Primary accent (gold): #f0b429
- Secondary accent (teal): #00b4d8
- Positive values: #3fb950
- Negative values: #f85149
- Body text: #e6edf3
- Muted text (labels, captions): #8b949e
- All numbers and data: font-family 'Courier New', monospace

## TYPOGRAPHY
- Tab headlines: bold, 18-20px, #e6edf3
- Section headers: bold, 14-16px, #f0b429
- Body text: 13-14px, #e6edf3
- All numerical values: monospace font, ALWAYS
- No serif fonts anywhere on the dashboard

## METRIC CARDS (all standalone key metrics)
- Background: #161b22
- Left border accent: 3px solid #f0b429 (or #00b4d8 for secondary metrics)
- Label: 4 words max, #8b949e, small
- Value: large, monospace, #e6edf3
- Delta: below the value, #3fb950 for positive, #f85149 for negative

## CHARTS
- Background: transparent or #161b22 — NEVER white
- Grid lines: #30363d
- Axis labels: #8b949e
- Chart titles: #e6edf3
- Use the defined color palette for all series colors

## TABLES
- Background: #161b22
- Alternating row shading: #0d1117 and #161b22
- Header row: #f0b429 text on #161b22 background
- Borders: #30363d
- Numbers: monospace, right-aligned
- Text: left-aligned

## SPACING
- Consistent 16px padding inside all cards and panels
- 24px gap between major sections
- No content touching the viewport edge

## REMOVE
- Any default Streamlit light-mode styling bleeding through
- Any white or light backgrounds on charts or components
- Any styling that looks like a consumer app rather than a terminal

## RULE CHECK BEFORE COMMITTING
- No first-person language introduced during styling changes
- All data is still present — visual changes only
- The dashboard looks identical in design quality from the first tab to the last
