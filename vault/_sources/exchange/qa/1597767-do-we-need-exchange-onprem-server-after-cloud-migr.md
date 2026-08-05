---
title: "Do we need exchange onprem server after cloud migration?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1597767/do-we-need-exchange-onprem-server-after-cloud-migr
question_id: 1597767
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Do we need exchange onprem server after cloud migration?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1597767/do-we-need-exchange-onprem-server-after-cloud-migr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have migrated my mailbox from the OnPrem server to the cloud exchange server. 
Do we need to hold the OnPrem server?  

Is there any dependency?  

Is there any impact if I decommit OnPrem on the closed server?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-26*

After migrating your mailbox from the OnPrem server to the cloud exchange server, you may not need to hold the OnPrem server, but it depends on your organization's needs. If you plan to keep Microsoft Entra Connect to manage user accounts in Active Directory, you need to keep at least one Exchange server on-premises. If all Exchange servers are removed, you won't be able to make changes to Exchange recipients. This is because the source of authority is Active Directory and changes need to be made there. However, if you do not need to manage recipients using an on-premises Exchange server, you may be able to shut down your last Exchange server and manage recipients using Windows PowerShell. It is important to carefully consider the implications and properly plan the full or partial decommissioning of on-premises servers.

References:

-  Exchange Server hybrid deployments

-  How and when to decommission your on-premises Exchange servers in a hybrid deployment

-  Exchange 2013 end of support roadmap
