---
title: "[Migrated from MSDN Exchange Dev] DAG Over firewall"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/145434/migrated-from-msdn-exchange-dev-dag-over-firewall
question_id: 145434
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev] DAG Over firewall

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/145434/migrated-from-msdn-exchange-dev-dag-over-firewall (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on Exchange developer questions and the TechNet Exchange forums for Non-developer Exchange has been locked down and transitioned to Microsoft Q&A for support, we manually migrated this one to Microsoft Q&A platform to continue the discussion.  

[MSDN thread link] DAG Over firewall  

[Original post]  

Good morning to all,  

I need to set up a database availability group on several sites. In each site there are two MAILBOX Exchange Server 2016 servers. The sites are protected by firewalls.  

I would like to have the list of ports to ensure good communication between the DAG members.  

Thank you in advance.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-30*

Hi,    

To the best of my knowledge, it's NOT suggested to restrict the network traffic between any internal Exchange servers. And according to the ground rule in the following official document, if you have firewalls that may restrict the network traffic, you'll need to configure rules that allow free and unrestricted communication between these servers:    

Network ports for clients and mail flow in Exchange    

    

Moreover, the blog below also mentions that "a rule allowing 'ANY/ANY' port and protocol communication must be in place allowing free communication between Exchange servers as well as between Exchange servers and domain controllers":    

Exchange, Firewalls, and Support… Oh, my!    

    

Hope you can find the above information helpful.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
