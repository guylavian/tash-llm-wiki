---
title: "Can not send emails to anyone with an @bigpond.com address"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1037084/can-not-send-emails-to-anyone-with-an-@bigpond-com
question_id: 1037084
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Can not send emails to anyone with an @bigpond.com address

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1037084/can-not-send-emails-to-anyone-with-an-@bigpond-com (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am getting the following error:    

550 5.4.300 Message expired -> 451 4.4.397 Error communicating with target host. -> 421 4.4.2 Connection dropped due to ConnectionReset    

Any help is appreciated.    

Thanks,    

JB

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-13*

Hello JB, 

We have rectified the issue by calling Telstra Bigpond team. Please ask for the SPF/Reputation record. You have to add Bigpond in your SPF once done, try to send it will work. 

Regards, 

Sreedhar K

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-06*

So this occurs on every set up including webmail and it is only @bigpond.com that is the issue. I can receive emails from them just not send them. Every other domain is issue free.
