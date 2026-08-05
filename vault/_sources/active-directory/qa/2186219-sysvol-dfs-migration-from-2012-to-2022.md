---
title: "SYSVOL DFS migration from 2012 to 2022"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2186219/sysvol-dfs-migration-from-2012-to-2022
question_id: 2186219
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 4
qa_tags: []
---
# SYSVOL DFS migration from 2012 to 2022

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2186219/sysvol-dfs-migration-from-2012-to-2022 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a 2012 domain using SYSVOL DFSR replication on 2012 servers. The 2012 PDC has the DFS function. I've been tasked with adding 2022 DCs and will eventually demote/decommission the PDC hosting the DFSR service, and I want to clarify what is/should happen before I start (I've searched and can't find the answers).  

When I add a new 2022 DC, will it join the SYSVOL replication group automatically or do I have to add it manually?  

How do I move the DFS function and replication group to a new 2022 DC? Should DFS move to DC or a member server?

What happens in the DFS replication group when I decommission the existing 2012 servers? I'm assuming they are removed but wanted to make sure in case I have to manually remove them.

Thank you in advance for your advice!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-19*

Hi Scott Fenstermacher1,

Thank you for posting in the Microsoft Community Forum.

When adding a new Windows Server 2022 domain controller (DC) to an existing domain with SYSVOL DFSR replication, here's what typically happens:

-  Joining SYSVOL Replication Group: When you promote the new 2022 DC to a domain controller, it should automatically join the SYSVOL replication group. SYSVOL replication is an integral part of Active Directory replication, and the new DC should seamlessly participate in this replication process.

-  Moving DFS Function and Replication Group: To move the DFS function and replication group to the new 2022 DC, you'll need to perform the following steps:    a. Install the DFS Replication feature on the new 2022 DC.    b. Add the new 2022 DC as a member of the DFS Replication group. You can do this by using the DFS Management console on one of the existing 2012 DCs.    c. Once the new 2022 DC is added as a member, you can gradually transfer the replication role to the new DC. This can be done by changing the membership in the replication group properties in DFS Management console. You should do this carefully to ensure data consistency and minimize disruptions.

-  Decommissioning Existing 2012 Servers: When you decommission the existing 2012 servers, the DFS replication group should automatically adjust. However, it's a good practice to manually remove the decommissioned servers from the DFS replication group to ensure clean removal and avoid any potential issues. This can be done through the DFS Management console by removing the decommissioned servers from the replication group membership.

It's important to thoroughly plan and test these steps in a non-production environment before implementing them in your production environment to ensure a smooth transition and minimize any potential disruptions to your Active Directory environment. Additionally, always ensure you have proper backups of your Active Directory data before making any significant changes.

DFS Replication overview | Microsoft Learn

Best regards

Neuvi Jiang
