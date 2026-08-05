---
title: "[Migrated from MSDN Exchange Dev] Semi Migration Exchange 2016 to O365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/150622/migrated-from-msdn-exchange-dev-semi-migration-exc
question_id: 150622
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# [Migrated from MSDN Exchange Dev] Semi Migration Exchange 2016 to O365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/150622/migrated-from-msdn-exchange-dev-semi-migration-exc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

[MSDN thread link] Semi Migration Exchange 2016 to O365  

Is it possible to migrate a part of my users from Exchange 2016 to O365, meanwhile the others one still using Exhange.  

I Explain, I have a domain named contoso.local, and customer ask me to migrate the headquarters to Office 365 but not the others ones.  

Is it possible ?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-04*

Hi,    

Yes, it is possible.    

You could deploy a hybrid environment, which will include the features introduced in the official document below    

Exchange Server hybrid deployments    

Then you can choose the users you want to move to cloud, and other users still locate on-premise    

Detailed information here: Move mailboxes between on-premises and Exchange Online organizations in hybrid deployments    

For the guide to help you deploy your hybrid environment, using this: Microsoft 365 and Office 365 mail migration advisor (login your Microsoft 365 or Office 365 account with Global administrator permissions)    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
