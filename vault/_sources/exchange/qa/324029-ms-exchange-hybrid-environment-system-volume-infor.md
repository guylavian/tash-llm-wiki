---
title: "MS Exchange Hybrid environment - System volume information"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/324029/ms-exchange-hybrid-environment-system-volume-infor
question_id: 324029
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# MS Exchange Hybrid environment - System volume information

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/324029/ms-exchange-hybrid-environment-system-volume-infor (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have a MS Exchange Hybrid environment with Office 365 and all our Mailboxes are in Office365 and hybrid is being only used for management. On that server, I have a space of 1TB out of which 675 GB is filled by System Volume Information already though shadow copies are disabled but still occupying space. I want to free up space for smooth operation of mailboxes and their logs, I googled and found that If I limit the size of shadow copies then I will get lot of space. My worry is, will I  loose anything, means any data loss or OS instability etc.     

    

    

Please assist.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-22*

Thanks Andy  

I would give it a try

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-21*

I would set a limit to the minimum - as little as possible and get all that space back.   

You won't lose anything. With Exchange, if you needed to restore, you would restore from your Exchange backup, not the shadow copy.  

If you needed to rebuild, you wouldn't use that copy either.
