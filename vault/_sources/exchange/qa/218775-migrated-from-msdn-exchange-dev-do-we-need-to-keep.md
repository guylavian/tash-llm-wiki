---
title: "[Migrated from MSDN Exchange Dev] Do we need to keep ECP enabled after migrating to Exchange Online?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/218775/migrated-from-msdn-exchange-dev-do-we-need-to-keep
question_id: 218775
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# [Migrated from MSDN Exchange Dev] Do we need to keep ECP enabled after migrating to Exchange Online?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/218775/migrated-from-msdn-exchange-dev-do-we-need-to-keep (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

[MSDN thread link]  Do we need to keep ECP enabled after migrating to Exchange Online?   

We recently migrated from an on-prem Exchange 2016 running on Server 2016 Standard to Exchange Online with a hybrid AAD. I recently ran Crowdstrike's assessment tool and one thing it noted was that ECP is enabled for all our Exchange accounts. From what I see online this hasn't been a 'thing' since 2013. We've since powered down the old Exchange server so I can't go in through the Exchange shell and make any changes. Is there some way to disable ECP via AD, or is this something I just don't need to care about?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-05*

Hi,    

According to your information above, you are having Exchange 2016 hybrid environment now.     

And you have powered down the Exchange 2016 server. EMS is not connecting now, if that's the case, are you still able to access the Exchange 2016 ECP?    

If you want to disable the on-premise Exchange ECP (which means disable external access to it), we can use IIS to meet this need.    

And seems not find such way to do this via AD.    

In addition, you could also refer to the official document if you want to decomission your on-premise Exchange server in hybrid.      

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
