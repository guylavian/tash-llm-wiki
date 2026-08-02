---
title: "Exchange Online Resource Schema Limits"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/286632/exchange-online-resource-schema-limits
question_id: 286632
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Exchange Online Resource Schema Limits

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/286632/exchange-online-resource-schema-limits (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good Morning All,  

Wondering if anyone knows of any limits to the ResourcePropertySchema parameter of the Set-ResourceConfig CmdLet within Exchange Online?  

Therefor adding on from that is there a known limit for the number of ResourceCustom parameter of the Set-Mailbox CmdLet?  

Many Thanks !

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-25*

@jabran-corp     

Here are all information about those two parameters:    

    

    

It doesn't say there exist a limitation on the length of value. If there exists a limitation, you will get an error about the limitation on length when you use a long value for this parameters.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
