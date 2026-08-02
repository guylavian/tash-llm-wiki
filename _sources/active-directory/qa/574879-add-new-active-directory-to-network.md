---
title: "Add new Active directory to network"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/574879/add-new-active-directory-to-network
question_id: 574879
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Add new Active directory to network

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/574879/add-new-active-directory-to-network (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a 2008 R2 SQL server with an Active Directory server providing DNS and Domain controller roles. The AD server both RAID drives failed and couldn't recover them or the AD. If I create a new AD on a new server 2008 or higher, will the SQL and the other machine on the network recognize the AD and function normally? If not, any suggestions?  

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-04*

Hello,  

Thank you for your question and reaching out.  

If your AD server have failed then you will be required at least one member server for example additional domain controller exists in your environment , so that you can do Authorities restore.   

If you create new AD then it will be with new name and new GUID and you will required to reconfigure your SQL server,  in this case please get first SA account credentials.  

--If the reply is helpful, please Upvote and Accept as answer--
