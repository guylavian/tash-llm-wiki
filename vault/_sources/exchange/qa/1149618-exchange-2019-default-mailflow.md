---
title: "Exchange 2019 - Default Mailflow"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1149618/exchange-2019-default-mailflow
question_id: 1149618
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Exchange 2019 - Default Mailflow

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1149618/exchange-2019-default-mailflow (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We using Exchange 2019 (Hybrid),     

There some question that bugging us.     

-  Why on the receive connector Exchange allowed anonymous users by default ? Since it's allowed spoofing the domain account or any other domain and send to any validate internal user domain.     

-  Is it possible / recommended to remove the anonymous user on Default Frontend transport and put some specific additional receive connector ( with whitelisted IP ) which have anonymous permission ?    

-  If it's not possible, how to tackle / prevent if the source not defined on anonymous receive connector list ? ( this is not possible if the suggestion required to block outbound port 25 on whole network infrastructure )

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-04*

Hi Andy,    

Thanks for your answer,     

So we just need to add another anonymous receive connector from my 3rd party Mail Gateway and O365 Connection IP List, and then disable permission anonymous users on Default Frontend of Exchange ?
