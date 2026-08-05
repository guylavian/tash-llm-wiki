---
title: "exchange 2019 Microsoft Failover Cluster service CPU usage 100%"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2258123/exchange-2019-microsoft-failover-cluster-service-c
question_id: 2258123
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange 2019 Microsoft Failover Cluster service CPU usage 100%

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2258123/exchange-2019-microsoft-failover-cluster-service-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello:

Currently, two Exchange 2019 CU14 Apr24HU(KB5037224) form a DAG. At present, the status of EX02 becomes isolated after the monthly cumulative update installation is restarted, and the Cluster Service is not started and manual startup fails. After EX02 is restarted, the status changes from isolated to normal. However, the CPU usage of the Microsoft Failover Cluster service on EX01 is 100% and the blue Screen of death occurs. After EX02 is shut down and EX01 is restarted, services are restored. However, after EX02 is powered on, the CPU usage of EX01 is 100% and the blue screen of death occurs. Thank you!

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-18*

Hi 1,

Thank you for posting your question in the Microsoft Q&A forum.

Based on your description, here are some suggestions for you:

-  When EX02 is powered on, is cluster service running well on EX02?   We have to confirm that cluster service keeps running well on all DAG member servers.

-  You could check Applications logs and System log from Event Viewer on EX01 and EX02, to see if any obvious errors are generated when the Microsoft Failover Cluster service consumes too much CPU.  

-  Try to remove EX02 from DAG member, then check if blue screen issue still occurs on EX01 when EX02 is powered on.   You also can re-add EX02 back to DAG.

-  If you have any third-party scan tool or antivirus software is installed on EX01 and EX02, you can un-install it temporarily and restart Exchange for troubleshooting.   In the long term, please perform Exchange related folder, file and process exclusion according to the following document. This could avoid any file lock or service interference when Exchange function:   Running Windows antivirus software on Exchange servers | Microsoft Learn 

-  In general, for this kind of blue screen issue, we also could capture dump files when issue occurs and raise ticket to Microsoft windows server support team for root cause analysis.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
