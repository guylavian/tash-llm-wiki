---
title: "[Migrated from MSDN Exchange Dev] Office 365 users are restricted to a 10MB attachment Limit"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/202799/migrated-from-msdn-exchange-dev-office-365-users-a
question_id: 202799
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# [Migrated from MSDN Exchange Dev] Office 365 users are restricted to a 10MB attachment Limit

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/202799/migrated-from-msdn-exchange-dev-office-365-users-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

[MSDN thread link] Office 365 users are restricted to a 10MB attachment Limit  

We currently have a hybrid setup of Exchange 2013 and Office 365.   

Our 365 users are unable to receive attachments larger than 10MB. I have looked everywhere and assume the issue lies within the transportconfig setting our ExternalDsnMaxMessageAttachSize and InternalDsnMaxMessageAttachSize at 10MB  

In our On prem exchange I can change these values, however in 365 it appears as though they have deprecated the commands to change these values.  

Does anyone know how I can remedy this situation?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-18*

Hi,    

Please refer to the official article which introduces about setting message size limit in Exchange online: Office 365 now supports larger email messages—up to 150 MB    

    

Some related links below for your reference as well:    

Message limits    

Configuring Max Email Message Size Limits for Office 365    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
