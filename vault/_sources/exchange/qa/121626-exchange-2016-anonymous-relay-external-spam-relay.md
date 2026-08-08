---
title: "Exchange 2016 anonymous relay ? External spam relay ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/121626/exchange-2016-anonymous-relay-external-spam-relay
question_id: 121626
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
---
# Exchange 2016 anonymous relay ? External spam relay ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/121626/exchange-2016-anonymous-relay-external-spam-relay (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,    

On our exchange server we had spam problem.  Today I opened message queue and I see 25000 mails in queue. They were all intended for @Karima ben   @harsh.com   domains.     

And we sent them a lot now we are rate limited by Microsoft domains.   I am aware we have to have  "anonymous users" on "Default Frontend receive connector to accept mail from internet.  We never had problem with content filtering and spam intended for our internal domain.      

But how to stop relaying, and why is it even relaying ?  How to stop example from picture, AgentLog.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-16*

So I removed "AnnonymousUsers" from:  

Client Frontend SrvName  

Default SrvName  

Outbound Proxy Frontend SrvName  

And so far everything looks normal.      

Maybe this could save us from next spam attack.  I hope.    

Thank You

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-10-09*

Hi  

Is your server locked down to send to a smarthost only? On your firewall, do you allow port 25 from anywhere or just the exchange server to your ISP?  

Also make sure you have SPF and DMARC setup for your domain.
