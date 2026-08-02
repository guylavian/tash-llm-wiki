---
title: "Exchange (2016) Hybrid Migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/348205/exchange-2016-hybrid-migration
question_id: 348205
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Exchange (2016) Hybrid Migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/348205/exchange-2016-hybrid-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I recently deployed a new Exchange server (2016).  The end goal is to get rid of my 2010 server.  The hybrid config wizard comes back with an autodiscover error, but the remote connectivity analyzer works without issue.  

The bigger problem, is I can't migrate a new exchange mailbox to o365, the migration says it can't find my mail server.  o365 support says this is an on prem server issue so they can't help.  It's funny, because this is only here to facilitate the use of o365.  Anyway, there is an internal DNS A record for autodiscover pointing to the Exchange server.  Also the (Get-MigrationEndpoint).Identity command returns nothing, but I don't get any errors regarding the creation of the migration endpoint.  I am stuck and going in circles!  

Thanks!

## Answers

_No answers on this thread._
