---
title: "Recovering Active Directory domain to isolated network for test purpose"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/325379/recovering-active-directory-domain-to-isolated-net
question_id: 325379
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Recovering Active Directory domain to isolated network for test purpose

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/325379/recovering-active-directory-domain-to-isolated-net (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are planning to do a restore drill to an isolated network. This will consist of AD restoration, DNS, and other critical apps restoring to this environment from the respective backup. AD restoration plan is to restore from snapshot veeam backup of existing 2 VM DCs out of the total 8 DCs. So, we aren't restoring all DCs but only these 2, to provide AD services to this isolated network. Please advise a best-suited plan for this kind of restore and verification points to make sure everything restored as required.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-23*

Hi,    

Based on my understanding , you want to create a domain environment  for just for test ,right?    

First of all, please note that : Do not use the Snapshot feature as a backup to restore a virtual machine that was configured as a domain controller.    

Then， If you need to restore Active Directory to different hardware, create full server backups and plan to perform a full server recovery.    

-  Perform a full server restore in order to restore the operating system and all files and applications.    

-     Perform a system state restore using wbadmin.exe in order to mark SYSVOL as authoritative.    

For how to choose the restore DC, you can refer to:    

    

More information about the :Recover the forest in isolation, you can refer to:    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/ad-forest-recovery-determine-how-to-recover    

Best Regards,
