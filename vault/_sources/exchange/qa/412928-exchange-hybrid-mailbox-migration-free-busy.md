---
title: "Exchange Hybrid Mailbox Migration - Free / Busy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/412928/exchange-hybrid-mailbox-migration-free-busy
question_id: 412928
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Exchange Hybrid Mailbox Migration - Free / Busy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/412928/exchange-hybrid-mailbox-migration-free-busy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a bit of a strange situation. I am currently in the middle of migrating users to Office365 from an Exchange 2019 Environment.  

-  If I move a mailbox using the O365 Migration Batch Wizard, on-prem users can not see their Free / Busy information.  

-  If I move a mailbox using PowerShell (New-MoveRequest), on-prem users cannot see their Free / Busy information.  

I have proven the issue only exists when I use PowerShell as I have moved one of my accounts back to on-prem and then used the migration wizard and now the Free / Busy is working as expected when an on-prem user tries to view it.  

I have checked all the settings of an account that works and an account that doesn't and I can't see any obvious differences and I can't seem to find anyone who has had a similar experience. Has anyone else seen this or can point me in the right direction of how I can resolve this without moving all the accounts back to on-prem and then using the batch migration wizard (There are a lot of accounts already moved).

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-28*

I think I may have found the issue, but not sure how I can correct it on already moved mailboxes.  

The -TargetDeliveryDomain was set in the script to domain.onmicrosoft.com  

I changed it to domain.mail.onmicrosoft.com and tested an account and that worked. Not sure why this would make a difference as the account still moves successfully with the domain.onmicrosoft.com without error.  

Is there any way to fix accounts that have already been migrated?
