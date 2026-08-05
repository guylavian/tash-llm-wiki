---
title: "Exchange Online Plan 1 vs M365 E3"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1127815/exchange-online-plan-1-vs-m365-e3
question_id: 1127815
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online Plan 1 vs M365 E3

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1127815/exchange-online-plan-1-vs-m365-e3 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a couple mailboxes that have a M365 E3 license on them, that are shared that were set up before I joined the company, and the people that set them up are long gone.  We are going through working at migrating to Azure from AD which means we need to implement the policies that were in AD in Intune and such, and it is preferred if we could just free up an E3 license.      

Is there any type of scenario that would require licensing a mailbox that is just shared between people with an E3 license instead of an Exchange Online Plan 1 or 2?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-14*

Hi, Sorry, I guess what I am saying is that M365 E3 would never be required for a shared mailbox simply because its a disabled account and that SKU is really designed for an actual user accessing 365/Azure workloads, not a shared mailbox. Hope that helps.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-14*

A shared mailbox in ExO does not require any license except for a few exceptions. Unless that shared mailbox meets those scenarios, you can disable the associated account and remove the licenses all together    

https://learn.microsoft.com/en-us/microsoft-365/admin/email/about-shared-mailboxes?view=o365-worldwide
