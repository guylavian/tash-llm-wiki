---
title: "Apply CU 23 to Exchange server 2016 CU7"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1190706/apply-cu-23-to-exchange-server-2016-cu7
question_id: 1190706
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Apply CU 23 to Exchange server 2016 CU7

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1190706/apply-cu-23-to-exchange-server-2016-cu7 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is it possible to install CU 23 to Exchange server 2016.

The current build is 1261.35 

The latest CU installed is 7.

What is the correct way to approach this?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-20*

Hi @Jose Durand ,

Agree with Andy, you could install the latest CU first: https://www.microsoft.com/en-us/download/details.aspx?id=104132

And then the latest SU: https://support.microsoft.com/en-us/topic/description-of-the-security-update-for-microsoft-exchange-server-2019-2016-and-2013-march-14-2023-kb5024296-e13b0369-2102-4c95-bee2-456514630727

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-03-17*

Yes, you can go straight to CU23, then install the latest security updates following:

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/install-cumulative-updates?view=exchserver-2019
