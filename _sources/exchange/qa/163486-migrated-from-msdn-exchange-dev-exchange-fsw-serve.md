---
title: "[Migrated from MSDN Exchange Dev]Exchange FSW server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/163486/migrated-from-msdn-exchange-dev-exchange-fsw-serve
question_id: 163486
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev]Exchange FSW server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/163486/migrated-from-msdn-exchange-dev-exchange-fsw-serve (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]  

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.  

As the former Outlook forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.  

[MSDN Link]  

Exchange FSW server  

[Original post]  

We recently had an Exchange consulting company setup your Exchange infrastructure.  For the most part, the configuration looks fine, 2 Exchange 2019 servers, hosted on different Hosts, same DC though. so EX1 and Ex2 with two databases.  I had a look at the setup and it looks like they made EX2 also the FSW server.  does this make sense? if that one EX2 server goes down, so does the Witness severs, so what would happen? would our entire email delivery system stop functioning?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-16*

Hi,    

I had a look at the setup and it looks like they made EX2 also the FSW server. does this make sense?    

The Witness server is used to achieve and maintain quorum when the DAG has an even number of members.    

It doesn't make sense to configure a DAG member as the Witness server.    

For more information,please refer to this link or the following picture.    

    

if that one EX2 server goes down, so does the Witness severs, so what would happen? would our entire email delivery system stop functioning?    

When a node goes down in a two-node DAG,it needs both the other node and the Witness server to be online and accessible to continue functioning.    

If one node and the witness server both go down,the entire system would stop working.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
