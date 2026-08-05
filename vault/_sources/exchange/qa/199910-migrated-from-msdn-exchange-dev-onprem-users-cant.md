---
title: "[Migrated from MSDN Exchange Dev]Onprem users can't view EOL Users' calendars"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/199910/migrated-from-msdn-exchange-dev-onprem-users-cant
question_id: 199910
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev]Onprem users can't view EOL Users' calendars

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/199910/migrated-from-msdn-exchange-dev-onprem-users-cant (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]  

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.  

As the former Outlook forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.  

[MSDN Link]  

Onprem users can't view EOL Users' calendars  

[Original post]  

Hi,  

We are currently migrating our onprem mailboxes to Exchange Online. The onprem mailboxes are on Exchange 2010 servers, and there are Exchange 2016 servers to enable hybrid mode.   

We have migrated several mailboxes to Exchange Online, but omprem users can't view the EOL user calendars. The users in EOL can view onprem and other EOL calendars OK. If an onprem user tries to schedule a meeting with an EOL user, when they hover over the EOL's calendar they see a 'The attendee's server couldn't be contacted. (Error Code: 5016)' message.  

The default calendar permission is free busy time, and if we change the default to reviewer, then the onprem users can then view the EOL calendars. However, we can't use this option for confidentiality reasons.   

Is there any way to allow the onprem users to view the EOL calendars without changing the permission to reviewer?  

Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-16*

Hi,    

Please refer to this part of the document on how to troubleshoot this problem:     

Exchange 2010/2013 user cannot see cloud user's free/busy (Error Code 5016)    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
