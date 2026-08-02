---
title: "[Migrated from MSDN Exchange Dev] How to detemine the message is sent on behalf of or sent as other mailbox via exchange tracking logs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/197121/migrated-from-msdn-exchange-dev-how-to-detemine-th
question_id: 197121
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] How to detemine the message is sent on behalf of or sent as other mailbox via exchange tracking logs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/197121/migrated-from-msdn-exchange-dev-how-to-detemine-th (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

[MSDN thread link] How to detemine the message is sent on behalf of or sent as other mailbox via exchange tracking logs  

Has any properties within exchange tracking logs can be used to determined the message is sent on behalf of and sent as other mailbox and determined the exactly delegated mailbox？

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-14*

Hi,    

Mailbox Audit Logging feature can track mailbox owner, delegate, and administrator logons to a mailbox, as well as what actions are taken while the user is logged on.    

Mailbox audit logging in Exchange Server    

    

You could also refer to this thread which dicussed the similar issue:    

Tracking sent items in shared mailbox    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
