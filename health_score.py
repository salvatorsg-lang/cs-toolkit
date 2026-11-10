#!/usr/bin/env python3
"""Rank customer accounts by health from a CSV file.

Usage:
    python3 health_score.py sample-accounts.csv

CSV columns:
    account, adoption_pct, tickets_last_90d, exec_sponsor,
    last_qbr_days_ago, expansion_opportunity

    - adoption_pct: 0-100, share of licensed seats actively using the product
    - tickets_last_90d: number of support tickets in the last 90 days
    - exec_sponsor: yes / no — is an executive sponsor active?
    - last_qbr_days_ago: days since the last QBR (or first review)
    - expansion_opportunity: yes / no — is there a realistic expansion case?

Scoring (0-100, higher is healthier):
    - Adoption: up to 40 points (adoption_pct * 0.4)
    - Tickets: up to 25 points (fewer is better; 0 tickets = 25, 10+ = 0)
    - Sponsor: 20 points if yes, 0 if no
    - QBR recency: 15 points if within 90 days, sliding down to 0 at 180+ days

Bands: 75+ Green, 50-74 Amber, below 50 Red.
Standard library only — no dependencies.
"""

import csv
import sys


def score_row(row):
    """Score one account. Returns (score, reasons list)."""
    reasons = []

    adoption = float(row["adoption_pct"])
    adoption_points = adoption * 0.4
    if adoption < 50:
        reasons.append(f"low adoption ({adoption:.0f}%)")

    tickets = int(row["tickets_last_90d"])
    ticket_points = max(0, 25 - tickets * 2.5)
    if tickets >= 8:
        reasons.append(f"high ticket volume ({tickets} in 90 days)")

    sponsor = row["exec_sponsor"].strip().lower() == "yes"
    sponsor_points = 20 if sponsor else 0
    if not sponsor:
        reasons.append("no active exec sponsor")

    qbr_days = int(row["last_qbr_days_ago"])
    if qbr_days <= 90:
        qbr_points = 15
    elif qbr_days >= 180:
        qbr_points = 0
    else:
        qbr_points = 15 * (180 - qbr_days) / 90
    if qbr_days > 120:
        reasons.append(f"no QBR in {qbr_days} days")

    score = adoption_points + ticket_points + sponsor_points + qbr_points
    return round(score, 1), reasons


def band(score):
    if score >= 75:
        return "Green"
    if score >= 50:
        return "Amber"
    return "Red"


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 health_score.py <accounts.csv>")
        sys.exit(1)

    path = sys.argv[1]
    accounts = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            score, reasons = score_row(row)
            accounts.append((score, row["account"], reasons,
                             row["expansion_opportunity"].strip().lower() == "yes"))

    accounts.sort(key=lambda a: a[0], reverse=True)

    print(f"{'Account':<28} {'Score':>6}  {'Band':<6}  Notes")
    print("-" * 90)
    for score, name, reasons, expansion in accounts:
        note = "; ".join(reasons) if reasons else "healthy — look for expansion" if expansion else "healthy"
        if expansion and band(score) == "Green":
            note += " (expansion candidate)"
        print(f"{name:<28} {score:>6.1f}  {band(score):<6}  {note}")


if __name__ == "__main__":
    main()
