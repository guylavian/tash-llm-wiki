---
title: "Inquiry Regarding wbadmin and Domain Controller Backup Restoration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2286701/inquiry-regarding-wbadmin-and-domain-controller-ba
question_id: 2286701
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Independent Advisor"]
---
# Inquiry Regarding wbadmin and Domain Controller Backup Restoration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2286701/inquiry-regarding-wbadmin-and-domain-controller-ba (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

The issue concerns the built-in `wbadmin` utility available in Windows Server 2016/2019, which is used for creating system backups. I am performing a bare metal backup on a physical server running Windows Server 2016 that functions as the first domain controller. Problems arise when attempting to restore this backup—regardless of whether the target is a physical or virtual machine.

When booting into the recovery environment using an ISO file in an isolated network, I encounter issues related to the RID master role. There is another domain controller in the same infrastructure (running as a virtual machine), but it is not present in the same test network during the recovery process.

Additionally, I attempted an authoritative restore, although I understand that this is not recommended in environments with multiple domain controllers. Following this restore, I was unable to log into the system. The login screen behaves abnormally—after entering credentials, the screen scrolls upward and then immediately returns, preventing any successful login.

I would also appreciate clarification on whether `wbadmin` is considered a sufficient and secure backup solution for server environments, or if the use of third-party tools (e.g., Veeam) is recommended as a more reliable and flexible alternative. 

Is there an official Microsoft statement that they do not recommend performing a backup if there is more than one domain controller? I need proof at my workplace.

Thank you in advance for your assistance.

Kind regards,

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-06-26*

Hello,

```
Thank you for posting question on Microsoft Windows Forum.

Based on your issue description, the followings are the plausible explanations to your queries.
```

1.For the issues related to the RID master role.

-  When restoring a domain controller (DC) in an isolated network without other DCs present, especially if that DC was the RID Master, you're essentially bringing up a DC that believes it is the sole authority for RID pools. However, in a multi-DC environment, RIDs are managed across all DCs to prevent duplication.

-  Also, the restored DC, isolated from its replication partners, might not correctly update its RID pool or allocate new RIDs without conflicting with RIDs potentially issued by other DCs in the actual production environment. If you then introduce this DC back into the production network, it could lead to RID pool inconsistencies or even exhaustion, impacting the ability to create new users, groups, or computers.

2.For the issue of logging in system after performing an authoritative restore.

-  It is probable of that an authoritative restore telling the restored DC that its copy of Active Directory is the "source of truth" and all other DCs should synchronize from it. If the restored DC's AD database is significantly older than the current state of other DCs (even if they're not in your test network), or if there are inconsistencies introduced by the restore process, the DC might struggle to function correctly. The login loop might indicate issues with Kerberos authentication, NTLM, or Active Directory services themselves, preventing successful user authentication. It is possible the restored DC's security identifiers (SIDs) or other crucial AD components are out of sync with what the system expects, leading to the authentication failures.

3.Regarding the wbadmin and third-party tool (Veeam).

-  Generally, If the environment is small and you strictly need FC/USB bare-metal snapshots of DCs or back up and restore a DC's system state, wbadmin can suffice. 

-  For production environments with multiple domain controllers and a need for reliable, flexible, granular recovery and require a more robust and manageable solution for Active Directory protection and recovery. Third-party tool could be considered.

-  For more information https://www.gartner.com/reviews/market/enterprise-backup-and-recovery-software-solutions/compare/microsoft-vs-veeam

4.For the query of official Microsoft statement of not recommending performing a backup if there is more than one domain controller.

-  There is no official Microsoft statement that you should not perform a backup if there is more than one domain controller. In fact, the best practices explicitly state the importance of backing up at least one domain controller, and often more. 

You can refer to below useful articles for further reference pertinent to your queries.

-  https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-devise-a-plan

-  https://learn.microsoft.com/en-us/azure/backup/active-directory-backup-restore

-  https://helpdesk.kaseya.com/hc/en-gb/articles/4407521162257-Detailed-Options-for-Protecting-Domain-Controller-DC-and-and-Restoring-Active-Directory-AD?utm_source=chatgpt.com

Hope the above information is helpful!
