---
title: "Exchange 2019 Standart Edition Search problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/337593/exchange-2019-standart-edition-search-problem
question_id: 337593
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange 2019 Standart Edition Search problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/337593/exchange-2019-standart-edition-search-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone, I have an Exchange 2019 Server Standart edition on my environment. Two weeks ago i installed CU9 to exchange server. After this Cumulative Update i could not search any item on my or users mailboxes. I tried on owa or outlook client but there is no change. Also in exchange administrative events there is some events about this issue like event id 1010 source MSExchangeFastSearch. I googled it for some time but unfortunately could'nt find any solution. ![82826-event-id-1010.jpg][1] ![82776-search1.jpg][2] [1]: /api/attachments/82826-event-id-1010.jpg?platform=QnA [2]: /api/attachments/82776-search1.jpg?platform=QnA Please advice Thanks,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-05*

Hi @Yuki Sun-MSFT      

first of all thanks for your assistance. Last weekend when i had more time to study on exchange server checked your suggestions. Unfortunately both of them didn't work.     

Below you can find the error about migrating mailbox.    

Error 1 :     

3/29/2021 3:32:27 PM [EXCH] Connected to source mailbox '0710c9d9-503a-43ca-8784-98e662ff254b (Primary)', database 'Merkez', Mailbox server 'EXCH.contoso.com' Version 15.2 (Build 858.0).    

3/29/2021 3:32:27 PM [EXCH] Request processing continued, stage LoadingMessages.    

3/29/2021 3:32:27 PM [EXCH] Stage: LoadingMessages. Percent complete: 20.    

3/29/2021 3:32:27 PM [EXCH] Stage: LoadingMessages. Percent complete: 20.    

3/29/2021 3:32:27 PM [EXCH] Transient error BigFunnelTransientException has occurred. The system will retry (2/720).    

Error 2:    

 MigrationMRSPermanentException: Informational: The request has been temporarily postponed because Search is not up to date. The Microsoft Exchange Mailbox Replication service will attempt to continue processing the request after

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-31*

Hi @msbayazit  ,    

I tried on owa or outlook client but there is no change.    

Have you tried switching between Exchange cached mode and Online mode in Outlook client and see if there would be any difference?    

Is this issue now affecting all users in your environment?    

Please try restarting the Microsoft Exchange Search service(MSExchangeFastSearch) on the sever and see how it goes.     

Besides, it's suggested to try moving one of the affected user's mailboxes to a different mailbox database or a new created mailbox database to check the result.     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
