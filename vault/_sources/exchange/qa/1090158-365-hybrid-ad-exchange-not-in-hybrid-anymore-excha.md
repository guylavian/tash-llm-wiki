---
title: "365 Hybrid AD - Exchange not in Hybrid anymore - Exchange management"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1090158/365-hybrid-ad-exchange-not-in-hybrid-anymore-excha
question_id: 1090158
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# 365 Hybrid AD - Exchange not in Hybrid anymore - Exchange management

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1090158/365-hybrid-ad-exchange-not-in-hybrid-anymore-excha (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

While I've found tons of articles close to my scenario, i'm not getting the exact answer I'm looking for.    

We are in Hybrid AD with 365 using ADConnect tool for sync.    

We were in Hybrid Exchange with on-prem Exch 2013 servers.    

We fully migrated Exchange to 365 and removed Exchange from Hybrid mode.    

The easiest way to manage exchange settings is by using on-premise exchange server for the purpose of making modifications to local AD which is synchronized to azure AD/365    

I want to get rid of my two on premise old Exchange server.  One is a hardware mailbox server which isn't servicing any mailboxes, just running exchange services.    

The other is a CAS virtual server.  We're using the CAS server for the EAC, which is much easier than using powershell to make Exchange modifications.    

I was told by someone that I should build a new Exchange virtual server 2019, and add it to the existing Exchange server, giving it all roles, so that it can manage Exchange with it's own updated EAC, then I can remove the two old servers so i'm left with just the one.    

So far this sound ok?    

Last, I really don't want to buy a new copy of Exchange STD 2019 for this purpose, but it's looking like MS doesn't give you a free Exchange license for management unless you go back in to Exchange hybrid mode?  I really don't want to do that, and i'm not sure what the implications are, like say that on premise exchange management server goes down.    

Any advice?

## Answers

_No answers on this thread._
