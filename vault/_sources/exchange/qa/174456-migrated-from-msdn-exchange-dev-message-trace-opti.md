---
title: "[Migrated from MSDN Exchange Dev]message trace option is missing in ECP\" Not running office65\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/174456/migrated-from-msdn-exchange-dev-message-trace-opti
question_id: 174456
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev]message trace option is missing in ECP" Not running office65"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/174456/migrated-from-msdn-exchange-dev-message-trace-opti (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]  

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.  

As the former Outlook forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.  

[MSDN Link]  

message trace option is missing in ECP" Not running office65"  

[Original post]  

Hi Team   

I am not on office 365 and I need help on how to track a message. message trace option is missing in ECP.  

Do i need to enable it or configure it in order to appear under Mail flow?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-25*

Hi,    

Message trace option in Exchange Admin Center is only available in Exchange Online(Office 365).    

On an Exchange on-premises server, you need to use delivery reports under the mail flow tag or you can use the Exchange Management Shell to run the Get-MessageTrackingLog command to do a message tracking.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in [our documentation][4] to enable e-mail notifications if you want to receive the related email notification for this thread.
