---
title: "How to Migrate Exchange 2016 To Exchange 2016 in Same Orgainzation (Due to HAFNIUM Compromised )"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/315098/how-to-migrate-exchange-2016-to-exchange-2016-in-s
question_id: 315098
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# How to Migrate Exchange 2016 To Exchange 2016 in Same Orgainzation (Due to HAFNIUM Compromised )

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/315098/how-to-migrate-exchange-2016-to-exchange-2016-in-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Support  

My Current Infra  

1-Primary Domain Controller  

1-Secondary Domain Controller + File Server  

2-RODC  

2 Child Domain  

1 Exchange Server 2016 (CU19)  

DB01  

DB02  

I am trying to Search article for Step by Step Moving Existing Exchange Server2016 To New Exchange Server 2016 with same Domain  

Not getting any links article or Videos  

Can you please advise how to migrate without Impact ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-16*

Hi，    

What do you want to preserve/migrate?     

Since the new server is in same organization, the mailbox migration should be easy: Manage on-premises mailbox moves in Exchange Server    

Do you mean article like this: Copy receive connector to another Exchange Server    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Some settings are saved in AD while some not, it should be a big work if you want to copy everything to the new server manually.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
