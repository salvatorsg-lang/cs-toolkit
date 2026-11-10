# Customer Success Toolkit — How I Use AI in CS Work

Hi, I'm Jonny Chai — a customer success manager with 6+ years managing 100+ advertising agencies as an embedded Meta partner across APAC, built on 12+ years in enterprise technology.

This repo is my working toolkit: the prompts, templates, and one small script I actually use to do CS work faster and more consistently with AI. It answers the question recruiters and interviewers keep asking me: **"How do you leverage AI in your customer success work?"**

## How I use AI in CS

I use AI as a drafting and thinking partner, not a replacement for judgement:

- **Before a QBR** — I feed it my account notes and usage numbers and ask for an outline with wins, risks, and expansion talking points. I check every claim before it goes to a customer.
- **On health reviews** — I use a simple scoring method (see `health-score-template.md`) and let the script in this repo rank accounts, so I spend my time on the at-risk ones instead of spreadsheets.
- **On messy situations** — churn risk, escalations, rough call notes. AI turns the mess into a structured first draft; I add the context only a human on the account knows.
- **On new accounts** — onboarding plans and 30/60/90-day milestones, drafted from the customer's own goals.

What AI does **not** do: it never talks to a customer for me, never invents a number I can't verify, and never replaces knowing the account.

## What's in here

| File | What it is |
| --- | --- |
| `ai-prompts-for-cs.md` | Copy-paste prompts for the CS jobs above — QBR prep, health review, churn triage, onboarding, expansion, escalation summaries, meeting follow-ups |
| `qbr-template.md` | QBR agenda and structure |
| `onboarding-checklist.md` | 30/60/90-day onboarding checklist |
| `health-score-template.md` | How to score an account, with a simple scoring table |
| `renewal-review-template.md` | Renewal readiness review |
| `worked-example.md` | A full QBR prep + health review for one fictional agency customer |
| `health_score.py` + `sample-accounts.csv` | A small script that ranks accounts by health from a CSV — no dependencies, standard library only |

## Try it in 2 minutes

```bash
python3 health_score.py sample-accounts.csv
```

You'll get a ranked list of five fictional accounts, each with a health score and a one-line reason.

**Try it in your browser:** the same scoring runs as an interactive demo on the portfolio site — https://salvatorsg-lang.github.io/#health-demo (live once the site is published).

## An honest note

- **All example data is fictional.** The worked example uses "Northwind Media Pte Ltd", a made-up agency, with invented-but-plausible numbers. No real client, agency, or employer data appears anywhere in this repo.
- **These are methods, not claims.** The templates and prompts show how I work. They are not a claim that I owned renewals or carried a quota — my background is retention and portfolio work, and the renewal template is framed as a working method, not a record of owned renewals.
- Everything here is free to read and adapt. If something in it helps your CS team, that's the point.
