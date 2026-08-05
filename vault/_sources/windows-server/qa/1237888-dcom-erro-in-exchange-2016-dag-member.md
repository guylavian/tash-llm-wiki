---
title: "DCOM erro in Exchange 2016 DAG member"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1237888/dcom-erro-in-exchange-2016-dag-member
question_id: 1237888
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# DCOM erro in Exchange 2016 DAG member

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1237888/dcom-erro-in-exchange-2016-dag-member (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

All servers are Exchange server 2016
We have A DAG with 4 members and witness server this is appearing on DAG member
DCOM was unable to communicate with the computer DAG-01.domain name using any of the configured protocols; requested by PID      f0c (C:\Windows\system32\ServerManager.exe), while activating CLSID
Why this is occurring and how to resolve

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-17*

Check DNS for old entries and delete them. Check the Server Manager for this server and delete it.
If both those fail, then I would check ADSIEdit and see if they are listed - 
https://community.spiceworks.com/topic/503277-dcom-was-unable-to-communicate-to-removed-server-event-id-10028 
Report back findings - https://community.spiceworks.com/how_to/122968-how-to-remove-an-orphaned-exchange-2010-server-or-database-from-ad-active-directory
Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.
