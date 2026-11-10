# AI Prompts for Customer Success

Copy-paste prompts to use with an AI assistant (Claude, ChatGPT, or similar). Each one lists when to use it and what to paste in. **Check every number and claim before it goes to a customer — AI drafts, you decide.**

---

## 1. QBR Prep

**When:** The week before a quarterly business review.
**Paste in:** Your account notes from the quarter + usage numbers (spend, adoption, campaigns live) + any support tickets.

```
Act as a customer success manager preparing a quarterly business review.

Account: [name]
Quarter: [Q1/Q2/Q3/Q4 + year]
Account notes: [paste]
Usage numbers: [paste — spend, adoption, active campaigns/users]

Give me a QBR outline with:
1. Top 3 wins this quarter, each with the number that proves it
2. Adoption — what's being used, what isn't, and why it matters
3. Top 3 risks, each with one concrete next step
4. Expansion talking points — where the customer could get more value
5. Three questions to ask the customer in the room

Keep it to one page. Flag anything you can't verify from what I pasted.
```

---

## 2. Customer Health Review

**When:** Monthly, or when an account feels off and you want a structured read.
**Paste in:** Adoption figures, ticket count and themes, meeting/engagement notes, any stakeholder changes.

```
Score this account's health and tell me what to do about it.

Account: [name]
Adoption: [e.g. 62% of licensed seats active, 3 of 5 products in use]
Support tickets (last 90 days): [count + top themes]
Engagement: [last meeting date, who attended, response time]
Stakeholder changes: [anyone left, joined, or changed role]

Give me:
1. A health score: Green / Amber / Red, with one sentence of reasoning
2. The top 3 risks, ranked
3. One action per risk — owner and date
4. One thing to stop worrying about, if there is one

Use the scoring in health-score-template.md if I paste it in.
```

---

## 3. Churn-Risk Triage

**When:** Usage has dropped, a key contact has gone quiet, or a renewal is at risk.
**Paste in:** Usage trend (before/after), ticket themes, last contact date, contract end date.

```
Help me triage a churn risk and draft a save plan.

Account: [name]
Usage trend: [e.g. active users down 40% in 6 weeks]
Ticket themes: [paste]
Last meaningful contact: [date + who]
Contract ends: [date]

Give me:
1. The most likely reason they're disengaging, in one paragraph
2. A save plan as a table: action | owner | date | what "done" looks like
3. What to say in the first outreach message — 3 sentences, human tone, no jargon
4. One thing I should NOT do yet

Be direct. Don't soften bad news.
```

---

## 4. Onboarding Plan

**When:** A new customer signs and you need a 30/60/90-day plan.
**Paste in:** The customer's goals in their own words, their team size, their timeline, and any blockers.

```
Turn this customer's goals into a 30/60/90-day onboarding plan.

Customer: [name]
Their goals (their words): [paste]
Team: [size + roles]
Timeline / deadline: [date if any]
Known blockers: [paste]

Give me:
1. Days 1–30: get live — milestones and success criteria
2. Days 31–60: build the habit — milestones and success criteria
3. Days 61–90: prove the value — milestones and success criteria
4. One risk per phase and how to spot it early
5. The single metric that tells us onboarding worked

Use the checklist in onboarding-checklist.md as the structure.
```

---

## 5. Expansion Opportunity Finder

**When:** Quarterly account planning, or before a QBR.
**Paste in:** Usage patterns, which products/features are adopted, stakeholder notes, and any budget signals.

```
Find expansion opportunities in this account.

Account: [name]
Usage: [which products/features, how much, trend]
Stakeholder notes: [who cares about what]
Budget signals: [anything they've said about budget or plans]

Give me a short list of expansion candidates, each with:
- What it is
- Who it helps and how
- The business case in one sentence
- What would need to be true for them to say yes
- How confident you are (High / Medium / Low) and why

Rank by confidence. Leave out anything that's just a guess.
```

---

## 6. Escalation Summary

**When:** A ticket thread has gone long and leadership needs the picture in 30 seconds.
**Paste in:** The ticket thread (or the key messages), impact, and current status.

```
Turn this messy ticket thread into a one-paragraph executive summary.

Ticket thread: [paste]
Impact: [who is affected, how badly]
Current status: [where things stand]

Give me:
1. One paragraph: what happened, impact, status, next step — plain language, no blame
2. A timeline: date + one line per key event
3. The one thing leadership should know that isn't obvious from the thread
```

---

## 7. Meeting Follow-Up

**When:** Right after a customer call, from rough notes.
**Paste in:** Your rough notes — don't tidy them first, that's the point.

```
Turn my rough call notes into a structured follow-up email.

Call notes: [paste — rough is fine]
Attendees: [names + roles]
Date: [date]

Give me:
1. A follow-up email I can send as-is: thank you, decisions made, owners, dates
2. A separate internal list: anything I promised that I haven't tracked yet
3. Any open question I should chase before the next meeting

Keep the email short. No filler phrases like "just circling back".
```
