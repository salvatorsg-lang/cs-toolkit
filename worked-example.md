# Worked Example — QBR Prep + Health Review

> **SAMPLE DATA — all fictional.** "Northwind Media Pte Ltd" is a made-up agency. Every number below is invented for illustration. No real client, agency, or employer data is used.

## The account

- **Customer:** Northwind Media Pte Ltd (fictional)
- **Type:** Mid-size media agency, Singapore
- **Team using the product:** 18 people across 3 client teams
- **Contract:** Annual, renews in 4 months
- **Last QBR:** 92 days ago

## Inputs (what I pasted into the prompts)

- **Adoption:** 61% of licensed seats active. 3 of 5 core features in regular use. Reporting module untouched since onboarding.
- **Usage trend:** Active users down from 16 to 11 in 6 weeks.
- **Tickets (last 90 days):** 9 tickets — 5 about reporting exports failing, 2 about permissions, 2 general questions.
- **Engagement:** Last meeting 3 weeks ago; the day-to-day contact replies within a day; the executive sponsor hasn't attended a meeting in 2 months.
- **Stakeholder change:** The original champion left the agency 5 weeks ago; her replacement is new and hasn't been onboarded yet.

## Output 1 — Health review

**Score: Amber (13/25)**

> Note: `health_score.py` uses a simpler 0–100 model and scores this same account Red (41.6) — it's a ranking tool for a whole book of accounts, not the full five-factor template above. Use the template for the real judgement.

| Factor | Score | Reason |
| --- | --- | --- |
| Adoption | 3 | Core use is there, but reporting untouched and seats falling |
| Engagement | 3 | Day-to-day contact responsive; sponsor absent |
| Support health | 2 | 5 tickets on the same reporting issue — a pattern, not noise |
| Stakeholder strength | 2 | Champion left; replacement not onboarded |
| Commercial health | 3 | Renewal in 4 months, no concern raised yet — but no expansion talk either |

**Top 3 risks:**
1. Reporting exports keep failing — this is the issue behind the usage drop, and it's fixable.
2. No champion — the replacement hasn't been brought in, so nobody inside is pushing usage.
3. Sponsor disengaged — if the renewal conversation starts with a sponsor who hasn't heard from us in 2 months, that's a bad start.

**Actions:**
| Action | Owner | Date |
| --- | --- | --- |
| Get the reporting export bug fixed or a workaround in place | Support + me | This week |
| Onboard the new champion — 30-minute intro + quick win | Me | Next week |
| Re-engage the sponsor with a one-page value summary before the QBR | Me | Before QBR |

## Output 2 — QBR outline

**Wins:**
1. Campaign reporting time cut from 2 days to 4 hours for the two teams using it (numbers from their ops lead).
2. Two new client teams onboarded in the quarter.
3. Zero downtime incidents.

**Adoption:** 61% seat usage; reporting module is the gap — worth a live demo in the QBR once the export issue is fixed.

**Risks (to raise honestly):** Reporting exports, champion transition, sponsor engagement — each with the plan above.

**Expansion talking points:** The third client team is still on manual reporting; if the reporting module lands, that's the natural next step — but only after the export issue is resolved. Don't pitch expansion on top of a broken feature.

**Questions to ask in the room:**
1. What does reporting need to do for your team that it doesn't do today?
2. Who should own this internally once the new champion is up to speed?
3. What would make the renewal an easy yes for you?

## What happened next (illustrative)

The QBR led with the reporting fix, not the expansion pitch. The new champion got a quick win in week one, the sponsor re-engaged after the value summary, and the account moved back to Green the following month. That's the point of the exercise: score honestly, fix the real problem first, and let expansion follow value.
