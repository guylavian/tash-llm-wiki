---
title: "Cannot Move user Mail box to another Exchange database which is DAG member"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1191870/cannot-move-user-mail-box-to-another-exchange-data
question_id: 1191870
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Cannot Move user Mail box to another Exchange database which is DAG member

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1191870/cannot-move-user-mail-box-to-another-exchange-data (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Running 

`New-MoveRequest -identity <mailbox> -skipmoving:folderviews,folderrestrictions -TargetDatabase <database>`  

gives error skipmoving deprecated and use moveoptions

How to use moveoptions in this command?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-03-22*

Hi @ azhar Nasim ，

It is not recommended that you skip content during migration. If a mailbox is missing folderviews, folderrestrictions, it can be corrupted and unusable.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-03-21*

Hi, why the need to do this?

It specifically says do not use unless working with support:

https://learn.microsoft.com/en-us/powershell/module/exchange/new-moverequest?view=exchange-ps
