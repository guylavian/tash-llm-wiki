---
title: "Exchange 2016 (disabling Default Frontend SERVER connectors)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/153256/exchange-2016-disabling-default-frontend-server-co
question_id: 153256
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Exchange 2016 (disabling Default Frontend SERVER connectors)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/153256/exchange-2016-disabling-default-frontend-server-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

Simple question that I have not seen asked.  Have a previous post where a great resource assisted by helping to clarify some things regarding Receive Connectors.  I feel real good with that conversation, but today when I was setting up a few commands to restart the Microsoft Exchange Frontend Transport service (required to restart after making Frontend connector changes), I noticed the following description which I did not expect.    

Original Post:    

https://learn.microsoft.com/en-us/answers/questions/71815/receive-connector-odd-question.html    

Scenario:    

I plan to disable the Default Frontend SERVER Receive connectors on all of our Exchange servers.  I then plan to re-create a new Frontend Receive connector that is identical in every way except it will be scoped for our inbound SMTP traffic IPs only.  I understand that this would prevent internal mail relay that the Default Frontend connector would by default allow for, but we will have internal relay covered via a second and third connector, so we should be all set there.    

Question is, the Microsoft Exchange Frontend Transport service has a description that reads as follows:    

This service proxies SMTP connections inbound to Hub servers and outbound from Hub servers    

This implies that Exchange to Exchange native communication uses this connector for more than JUST inbound SMTP over port 25.  Can I disable this connector as I referenced above and have a second one locked to our inbound SMTP IPs without breaking something else regarding Exchange to Exchange mail flow?  Could I just add all Exchange server IPs to the new connector we have scoped to get around this if if does break things?    

Thanks,    

CWT

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-06*

Thanks for the reply and additional information Eric (much appreciated).  I think your correct in that that service description was just never updated to reflect Exchange 2013+ which is what really threw me for a loop in the first place.  Made me rethink things when I saw the outbound from Hub servers referenced :o)  

Knowing that I can disable the Default Frontend connectors without issue (provided we create another one scoped as needed), substantiates what I previously understood.  Not forgetting about other Frontends to account for mail relay requirements of course.   

Thanks much,  

CWT
