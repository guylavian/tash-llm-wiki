---
title: "Exchange Online mail spammed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/332000/exchange-online-mail-spammed
question_id: 332000
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online mail spammed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/332000/exchange-online-mail-spammed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have an Exchange Server 2016 environment that I am migrating to Exchange Online. The hybrid configuration has already been done.  

Meanwhile, users migrated to Exchange are seeing their emails spammed when they send to other Exchange Online users belonging to other Office 365 tenants. Before the migration they did not have this problem.  

If someone can help me to find the cause of the problem.  

Regards

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-25*

Set that up then:    

https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/use-dkim-to-validate-outbound-email?view=o365-worldwide    

https://dmarcly.com/blog/how-to-set-up-dmarc-dkim-and-spf-in-office-365-o365-the-complete-implementation-guide

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-25*

You can double-check that your DMARC, DKIM, and SPF records are all set up properly.  

To validate, go to https://mxtoolbox.com.
