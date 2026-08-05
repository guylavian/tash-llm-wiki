---
title: "Exchange2016 requires to share calendar to users of an external organization but reports an error when enabling federated authentication trust"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1050314/exchange2016-requires-to-share-calendar-to-users-o
question_id: 1050314
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange2016 requires to share calendar to users of an external organization but reports an error when enabling federated authentication trust

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1050314/exchange2016-requires-to-share-calendar-to-users-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Two-way trust is established between the two domains, and have been added the TXT DNS

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-18*

Hi @ITSUPPORT      

Take a reference at the methods discussed in this similar thread: Exchange Server Federation Error    

Make sure TLS1.2 is enabled for your on-prem server, detailed steps here: Enabling TLS 1.2 and Identifying Clients Not Using It    

    

And more information about sharing in on-prem Exchange server, which applied to Exchange 2016 as well: https://learn.microsoft.com/en-us/exchange/sharing-exchange-2013-help?source=recommendations    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
