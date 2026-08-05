---
title: "Exchange Server and AD Authentication - Lockouts"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/299417/exchange-server-and-ad-authentication-lockouts
question_id: 299417
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange Server and AD Authentication - Lockouts

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/299417/exchange-server-and-ad-authentication-lockouts (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, So I may be asking a bonehead question: However, Does on-prem Exchange server 2013 or 2016 cache/store AD credentials when it attempts to authenticate back to AD? Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-05*

Awesome, thanks for that answer - that's what suspected but wasn't sure, if for some crazy reason they would be stored  there besides the users client apps.  

I posted because I've been dealing with crazy account lockout issues (Exchange 2013 CU-22) as in an account being locked every 3 minutes - currently pouring through posts on locating the lockout causes when all it shows is the Exchange servers in Event 4740.  

I thought maybe a corrupted mailbox or something might be causing the lockouts, but I'm not an Exchange expert by any means so that may be completely ignorant.  

Anyhow, It's easy when the Event 4740 points to the device, but almost impossible when the Event is only showing the lockouts coming from the 2 Exchange servers, to which I used ExMon on the Exchange servers to capture user connections.  

ExMon showed me a PC, but I cleared that PC of the user's Exchange account, then ExMon only showed connections coming from  "Client=MSExchangeRPC" and "none" for the Client IP address.   

So now I've found some more tools I can use to possibly see more into what is causing these lockouts.  

And I'm going run some health checks.  

If anyone has additional input, it is appreciated!
