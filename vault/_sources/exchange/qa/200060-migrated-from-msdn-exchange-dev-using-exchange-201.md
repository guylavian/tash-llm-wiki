---
title: "[Migrated from MSDN Exchange Dev] using exchange 2010 how to connect 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/200060/migrated-from-msdn-exchange-dev-using-exchange-201
question_id: 200060
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] using exchange 2010 how to connect 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/200060/migrated-from-msdn-exchange-dev-using-exchange-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

I am using exchange 2010 how can i connect another server which is 2013 is it possible?  please guide and suggest

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-16*

Hi,    

You could upgrade Exchange server from Exchange 2010 to Exchange 2013.    

Since Exchange 2010 does not support in-place upgrade, you need to install Exchange 2013 on another computer that joins the same domain to form a coexistence environment, and then migrate user mailboxes, public folders and other data in Exchange 2010 to Exchange 2013, and then Configure the virtual directory URL , DNS record, Autodiscover service and other settings.    

For more detail you could refer to:  Upgrade from Exchange 2010 to Exchange 2013 and Checklist: Upgrade from Exchange 2010        

In addition, considering the complexity of the whole process, it’s recommended for you to use the Exchange Deployment Assistant. It will provide you with specific steps and guidance.    

Exchange 2010 has ended support, so please upgrade to a higher version of Exchange server as soon as possible.    

For more information: Exchange 2010 end of support roadmap    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
