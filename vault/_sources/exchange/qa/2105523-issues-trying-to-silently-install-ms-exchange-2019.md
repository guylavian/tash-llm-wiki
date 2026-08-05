---
title: "Issues trying to silently install MS Exchange 2019 on root/child AD environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2105523/issues-trying-to-silently-install-ms-exchange-2019
question_id: 2105523
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Issues trying to silently install MS Exchange 2019 on root/child AD environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2105523/issues-trying-to-silently-install-ms-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a root/child AD environment that I would like to install Exchange in.  

On one of my root servers I run PrepareSchema, PrepareAD.  On a child AD I run PrepareAllDomains.  

When I try to install the mailbox role on my exchange server, I get the error:  

Couldn't find recipient "rootdomain/Users/SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c}.  

After each step of the process I run a repadmin /syncall /AeD and repadmin replsummary trying to ensure replication has completed before running the next step.    

Suggestions on what I am doing wrong or different steps I can take?

This is on a fresh install of AD.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-10-17*

If you are missing an arbitration maibox:

https://learn.microsoft.com/en-us/exchange/architecture/mailbox-servers/recreate-arbitration-mailboxes?view=exchserver-2019#re-create-the-microsoft-exchange-organization-mailbox-for-oabs
