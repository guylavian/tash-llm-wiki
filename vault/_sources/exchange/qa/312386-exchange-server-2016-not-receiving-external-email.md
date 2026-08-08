---
title: "Exchange server 2016 not receiving external email"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/312386/exchange-server-2016-not-receiving-external-email
question_id: 312386
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange server 2016 not receiving external email

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/312386/exchange-server-2016-not-receiving-external-email (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I just started having this issue yesterday. I restarted the MSExchange Transport service and the external mail started to come in.  HOwever after an hour or so, the same issue. This time restarting the service had no effect.  I had to reboot the server and mail flow resumed.  

However, today, it is happening again and restarting the service nor rebooting the server is working.  What am I missing?  Can someone assist?  

Thanks,  

Roger

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-12*

It looks like my issue was due to low disk space. One I increased the size of the hard drive the external emails started to flow in.
