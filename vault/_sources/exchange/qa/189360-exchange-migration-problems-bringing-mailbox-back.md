---
title: "Exchange migration: Problems bringing mailbox back on-premises(normally works)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/189360/exchange-migration-problems-bringing-mailbox-back
question_id: 189360
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange migration: Problems bringing mailbox back on-premises(normally works)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/189360/exchange-migration-problems-bringing-mailbox-back (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We just started using Exchange Online and it has been working great.  Our current plan is to use Exchange Online, but when someone quits our company we will migrate the mailbox back on-premises for a few months, to free up licenses, and then delete the mailbox 4 months later once we confirm that their boss, etc has not requested access to their email, etc.  

Normally, I can migrate mailboxes back on-premises with no issues, but now I have 1 that is stuck ay syncing for days.  Does not matter if I use Exchange Admin Center, powershell, etc the mailbox never migrates 100%.  This is not normally an issue, but have increased the error count for this mailbox, etc and it just stalls.  Anyone have any ideas or know of some good logs I can look through, etc.?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-07*

Great suggestion on the converting to shared mailbox, and releasing the license

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-07*

Service Health and Azure AD Health are completely clear, but not sure why the mailbox will no longer offload.    

Thanks for the suggestion about converting them to Shared mailbox.  I knew that was possible, but never thought it might be a smooth way to stop paying for a mailbox while it is being decommissioned
