---
title: "[Migrated from MSDN Exchange Dev]Exchange Server 2016 Adding New Node to Dag"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/155985/migrated-from-msdn-exchange-dev-exchange-server-20
question_id: 155985
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]Exchange Server 2016 Adding New Node to Dag

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/155985/migrated-from-msdn-exchange-dev-exchange-server-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

Hello Everyone  

I have a requirement to add a new Exchange Server 2016 Node in Existing DAG and I need your help to step by step to configure this node in DAG with URL and SSL Certificate properly without facing any issue in production environment, Please note the below which I already taken care of.  

-  I already installed the new Exchange Server 2016 on windows server 2016 OS   

-  After Installation received error message from few users and outlook is not getting connected and prompting with SSL Certificate and URL mismatch error   

-  I need exact powershell command to configure the exchange node same as other nodes URL (I need to get command to check the current configuration and set command to set the same URL on this node) without breaking any current configuration to avoid the chaos  

-  I exported the SSL Certificare from other exchange node and import on this new node successfully  

-  I need steps to properly configure this node as same as exisiting exchange node and have to add inside the existing dag  

-  I installed the similar windows updates same as other nodes and CU also matching with the other nodes   

-  I need support configuring this exchange node with existing URLs  

-  Need support with step by step to avoid any production issues  

Thanks for your support in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-09*

Hi,    

What is the specific error?    

Which URL do you want to modify?    

This article may be helpful to you: How to suppress the AutoDiscover mismatch warning    

You could run the following command to add the Exchange server to DAG, and please noted that a DAG is a set of up to 16 Microsoft Exchange Server Mailbox servers:    

```
Add-DatabaseAvailabilityGroupServer -Identity <> -MailboxServer <>
```

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
