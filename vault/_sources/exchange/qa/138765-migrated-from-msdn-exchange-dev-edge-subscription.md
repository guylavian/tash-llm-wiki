---
title: "[Migrated from MSDN Exchange Dev]Edge Subscription after Exchange 2013 MBX\\CAS server rebuild"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/138765/migrated-from-msdn-exchange-dev-edge-subscription
question_id: 138765
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev]Edge Subscription after Exchange 2013 MBX\CAS server rebuild

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/138765/migrated-from-msdn-exchange-dev-edge-subscription (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]  

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.  

As the former Non-developer Exchange forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.  

[MSDN Link]  

Edge Subscription after Exchange 2013 MBX\CAS server rebuild  

[Original post]  

Hi, following a server failure of a MBX\CAS server and successfully recovering the server we need to re subscribe it to the Edge Sync service in its AD site where we have one Edge server. Do you have to complete a new Edge Subscription or is there anyway we can resubscribe using the original Edgesubscribtion.xml that was created at the time of the Edge server was implemented.  

If not and we have to create a new subscription can it use the existing send\receive connectors associated with the previous subscription?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-26*

Hi,    

According to this official document,    

    

it is suggested to export a new Edge Subscription file.    

And when you create a new Edge Subscription,    

    

So I suppose it can't use the existing connectors.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
