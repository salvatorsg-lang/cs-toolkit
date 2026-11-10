# Customer Health Score — Template

Score each factor 0–5. Add them up for a score out of 25, then read the band below. Score monthly, or whenever something changes.

## Scoring table

| Factor | 5 | 3 | 1 |
| --- | --- | --- | --- |
| **Adoption** | Core features in daily use by the whole team | Partial use, some features untouched | Barely used, or usage falling |
| **Engagement** | Regular meetings, quick replies, customer initiates | Meets when asked, replies are slow | Gone quiet, meetings cancelled |
| **Support health** | Few tickets, resolved fast | Steady tickets, some slow ones | Repeated issues, long open tickets |
| **Stakeholder strength** | Executive sponsor + a champion, both active | One contact, no sponsor | Sponsor left or disengaged |
| **Commercial health** | Contract secure, expansion talked about | Renewal coming up, no concerns yet | Renewal at risk, budget pressure |

## Bands

| Total (out of 25) | Band | What it means |
| --- | --- | --- |
| 20–25 | Green | Healthy. Keep the rhythm, look for expansion. |
| 13–19 | Amber | Watch it. One or two factors need a plan this month. |
| 0–12 | Red | Act now. Use the churn-risk triage prompt and build a save plan. |

## Rules

- Score what you can **see** (usage, tickets, replies), not what you hope.
- If any single factor is a 1, the account is at most Amber — a single bad factor can sink an account even if the rest looks fine.
- Write one sentence of reasoning with the score. A number with no reason is useless next quarter.
- Re-score after every QBR and after any stakeholder change.

## The script version

`health_score.py` in this repo does a simplified version of this from a CSV — adoption, tickets, sponsor, and days since the last QBR. Use it to rank a book of accounts quickly, then apply this full template to the ones that need attention.
