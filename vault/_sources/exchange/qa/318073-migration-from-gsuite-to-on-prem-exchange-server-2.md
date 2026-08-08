---
title: "Migration from Gsuite to On-prem Exchange Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/318073/migration-from-gsuite-to-on-prem-exchange-server-2
question_id: 318073
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Migration from Gsuite to On-prem Exchange Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/318073/migration-from-gsuite-to-on-prem-exchange-server-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,  

In our organization, there are around 50 Gsuite email users which are have mailboxes over 50GB.   

I will migrate the mailboxes (email, calendar, contacts) on Gsuite (google workspace) to the Exchange server (on-prem) where I will install it.  How can I achieve this migration in the most effective way without using a 3.part application?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-18*

Hi @Yasin Turaner   ,    

Agree with michev. The easy way to migrate mailboxes is through the .pst file, you could using Outlook client to export the mailbox to .pst file, and then import the .pst file to the new mailbox.    

For more information: Import and export Outlook email, contacts, and calendar    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-17*

There are no native tools for this scenario. You can either export/import PSTs or use a third-party tool.
