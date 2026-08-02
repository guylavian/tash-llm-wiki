---
title: "[Migrated from MSDN Exchange Dev] Exchange 2013 version 15 build 847.32 mail flow"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/147692/migrated-from-msdn-exchange-dev-exchange-2013-vers
question_id: 147692
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Exchange 2013 version 15 build 847.32 mail flow

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/147692/migrated-from-msdn-exchange-dev-exchange-2013-vers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/0b1d78db-2c32-4d1f-ac86-5b7763b2d3bd/exchange-2013-version-15-build-84732-mail-flow-incoming-mail-not-delivered-to-mailboxes?forum=exchangesvrdevelopment  

outgoing mails are going  no incoming mails, senders getting delay notification from their postmaster .it is already a day gone.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-02*

First, Exchange 2013 SP1 is an old version,  we recommend you to update your server to latest CU ASAP.    

What kind of NDR (retuned message) does the sender receive? Can you post the specific information?    

If you run message tracking on your server, could you see those messages logged or they didn't enter your server at all?    

Make sure your DNS records are configured well, turn off the third-party tools temporarily, run this test of Exrca: https://testconnectivity.microsoft.com/tests/InboundSMTP/input    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
