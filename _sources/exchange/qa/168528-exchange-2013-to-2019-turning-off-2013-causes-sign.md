---
title: "Exchange 2013 to 2019 - Turning off 2013 causes significant delays in receiving external email ONLY"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/168528/exchange-2013-to-2019-turning-off-2013-causes-sign
question_id: 168528
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 to 2019 - Turning off 2013 causes significant delays in receiving external email ONLY

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/168528/exchange-2013-to-2019-turning-off-2013-causes-sign (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey everyone, hopefully I am overlooking a simple solution here, but I suppose we shall see! So for starters, I used this guide as my foundation for performing this migration.   

https://www.kerneldatarecovery.com/blog/step-by-step-guide-for-migrating-exchange-server-2013-to-2016-part-1/  

Everything went well, clients haven't had any issues connecting, OWA works, mail flow, certs, etc.  

In prep to decommission to the old server, like I've done in the past, I like to shut it down and let the new one operate by itself. However, this time around, I am running into email deliverability issues for external incoming only. Internal sending and receiving is fine. And even internal to external is fine. No delays, no issues. Soon as I bring back up the 2013 server, everything is fine again.  

I've checked our Sonicwall ESA, its pushing the mail out of its queue so seemingly no issue there. When I run get-queue, there is nothing stuck but I did still notice that the 2013 server is the next hop in the ShadowRedundancy. Perhaps? I also didn't transfer the Discovery Mailbox over from 2013 to 2019 because as far as I am aware, it is not a necessity and it doesn't seem to be in use. Do you think that could be it?   

DNS is all properly set up as well as all firewall entries, send/receive connectors. I've checked and rechecked countless times.  

Event viewer actually looks better when the 2013 server is offline, and only shows a heartbeat error trying to connect to the shutdown server, which is normal. That and the killbit error which apparently MSFT is still trying to resolve but seems to be cosmetic. There are a couple of other messages, but they are not in reference to mail flow and from what I have read, can be ignored.   

Just to reconfirm, mail flow is not entirely killed when the 2013 is offline. Those external incoming will show up eventually, just with potentially massive delays.  

Anyways, anyone have any ideas? If you need me to clarify anything further, I'd be happy to!

## Answers

_No answers on this thread._
