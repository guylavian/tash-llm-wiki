---
title: "Why does sysvol replication fail if the disk with Windows Server is cloned?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1471057/why-does-sysvol-replication-fail-if-the-disk-with
question_id: 1471057
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Why does sysvol replication fail if the disk with Windows Server is cloned?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1471057/why-does-sysvol-replication-fail-if-the-disk-with (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Sysvol replication stopped in an AD domain with 2 DCs.  One runs Windows Server 2016 and the other 2019.  

After years of failure, Sysvol replication was restored by:

-  Deleting the clone partition of System Reserve and C:.  

-  Temporarily increasing MaxOfflineTimeInDays.

Why was it necessary to delete the partitions created by disk cloning software like Macrium Reflect or EaseUS Disk Copy?  

The cloned drives were taken as an easy backoff and left in the server when not needed.  When deleting the partitions using Disk Manager, there was usually an extra warning on those 2 partitions indicating they were in use.

Note this impacted any DFSR configuration, not just sysvol.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-03*

Hello PaulS,  

Thank you for posting in Q&A forum.  

If you want to more Domain Controllers, you can add extra servers to domain and promote them as Domain Controllers.  

It seems the clone method you used affects the AD replication, then it will affect SYSVOL replication and DFSR replication, SYSVOL replication and DFSR replication depends on AD replication.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-12-30*

Hi @PaulS •

The domain controller cloning method you are using is not supported. The only supported cloning method is through sysprep as mentioned in the following link : STEP-BY-STEP GUIDE TO CLONE A DOMAIN CONTROLLER

When you use unsupported tools to clone or backup a domain controller , replication will not working and ut's a normal behavior  

If you want to backup a domain controller, it is recommended to avoid cloning methods via third-party tools. The simplest way is to use Windows backup on a dedicated disk or network share.

Please don't forget to accept helpful answer
