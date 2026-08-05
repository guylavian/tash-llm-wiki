---
title: "getting error on exchange object could not be found (AD hostname)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1126627/getting-error-on-exchange-object-could-not-be-foun
question_id: 1126627
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# getting error on exchange object could not be found (AD hostname)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1126627/getting-error-on-exchange-object-could-not-be-foun (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

if i open anything in exchange admin center e.g. any mailbox or view mobile details. i am getting below errors    

seems like there is connectivity issue between AD and Exchange.    

can anyone assist me to fix this issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-13*

seems fine. i am not getting this on Microsoft edge.    

thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2022-12-13*

Hi,    

To identify the domain controllers used by the Exchange server by running this command:    

```
Get-ExchangeServer -status | fortmat-list static*,current*
```

you can check if the network flows is ok between Exchange servers and domain controllers.    

Please don't forget to mark helpful reply as answer
