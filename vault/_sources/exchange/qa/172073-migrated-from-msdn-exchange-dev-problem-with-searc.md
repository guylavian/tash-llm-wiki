---
title: "[Migrated from MSDN Exchange Dev]problem with search index on exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/172073/migrated-from-msdn-exchange-dev-problem-with-searc
question_id: 172073
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]problem with search index on exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/172073/migrated-from-msdn-exchange-dev-problem-with-searc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted  on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.    

Hi    

I have  exchange server  Version 15.2 (Build 659.4)  which recently lunched , users can not search in web mail (OWA)    

after i check the server status , i think the database search index is not bailed , i search a lot and run some commands as bellow , please help me to solve this issue    

as i search it should be a folder inside the DB path to remove or rename the index but that folder is not exist in DB path

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-23*

Hi ,    

What is the specific problem phenomenon you encountered during the search process, would you mind describing your operation process and results to me in detail?    

-  About the first screenshot you provided. According to my research and test in my Exchange 2019 lab environment, it is by design in Exchange 2019 that the ContentIndexState is NotApplicable. Exchange 2019 uses the new search engine called "Big Funnel", using Bing technology to make the search even faster and provide better results. Search indexes are no longer stored on disk per Mailbox database, but search indexes are now stored inside the Mailbox database on a per Mailbox basis. So the context index for the database shows NotApplicable in Exchange 2019, and the unhealthy index state will become a thing of the past.    

-  About the second screenshot you provided. According to my check, there is no this script in Exchange 2019 folder by default, so you will get an error when you run the script.    

-  About the fifth screenshot you provided. According to my research, this command is the process in which a copy of a mailbox database is added to another Mailbox server. Is your environment a DAG environment?    

-  Please check and restart the Microsoft Exchange Search service and Microsoft Exchange Search Host Controller service.    

-  Please try to migrate users to another new database to see if users can search successfully.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
