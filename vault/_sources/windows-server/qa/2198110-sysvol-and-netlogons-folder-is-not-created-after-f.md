---
title: "Sysvol and Netlogons folder is not created after FSMO role transfer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198110/sysvol-and-netlogons-folder-is-not-created-after-f
question_id: 2198110
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Sysvol and Netlogons folder is not created after FSMO role transfer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198110/sysvol-and-netlogons-folder-is-not-created-after-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Sysvol and Netlogons folder is not created after FSMO role transfer

Windows Server 2022 Std edtion ,

we had transfer FSMO role from DC01 to DC  and all roles are successfully transfused but  strange issue we are facing on

newly promoted domain controller (Name : DC) two folder is not found when checked.

\DC

no shared folder showing 

Any help is highly appreciate

either move back all roles to DC01 from Newly promoted DC server or troubleshoot on DC

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-09*

Hi arvind_snp,

Thank you for posting in the Microsoft Community Forums.

First, you need to make sure that the Sysvol and Netlogons folders are actually not created. In Windows Server, the Sysvol folder is usually located under the %systemroot%\SYSVOL path, and the Netlogons folder is actually a subfolder within the Sysvol folder (e.g. %systemroot%\SYSVOL\sysvol&lt;domain name>\scripts). It is shared as NETLOGON.

Starting with Windows Server 2008, Sysvol replication uses the DFS-R (Distributed File System Replication) service by default instead of the older FRS (File Replication Service). Therefore, you need to ensure that the DFS-R service is running and configured correctly.

Check if the DFS-R service is started.

Check the DFS-R replication status and event logs to verify that there are no errors or warning messages.

Force synchronization for Distributed File System Replication (DFSR) replicated sysvol replication - Windows Server | Microsoft Learn

Best regards

Neuvi
