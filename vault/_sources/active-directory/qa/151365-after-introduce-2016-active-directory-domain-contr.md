---
title: "After introduce 2016 active directory domain controller on 2008 r2 Active directory environment, can we upgrade the Sysvol folder FRS to DFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/151365/after-introduce-2016-active-directory-domain-contr
question_id: 151365
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# After introduce 2016 active directory domain controller on 2008 r2 Active directory environment, can we upgrade the Sysvol folder FRS to DFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/151365/after-introduce-2016-active-directory-domain-contr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,  

I have installed and configured the Active directory 2016 domain controller on Active directory 2008 r2 environment. Sysvol folder replication is not working. So Can i upgrade the Sysvol folder FRS to DFS or need to uninstall the Active directory 2016 and Upgrade Sysvol folder.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-04*

Hi,    

To migrate replication system for sysvol from FRS to DFSR , you have to start by fixing the replication issue. You can launch a non-authoritative restore as mentioned by this link :    

use-burflags-to-reinitialize-frs    

Once the sysvol replication is restored , you can proceed the migration to DFS-R if the domain functional level is Windows 2008 or higher.    

Please don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-04*

No, you cannot. I'd check the event logs for related errors / details which will define a course of action.   

https://support.microsoft.com/en-us/help/290762/using-the-burflags-registry-key-to-reinitialize-file-replication-servi  

https://support.microsoft.com/en-us/help/257338/troubleshooting-missing-sysvol-and-netlogon-shares-on-windows-domain-c  

Post the source and event IDs if help needed.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-04*

Dear Patrick,  

Repadmin /syncall , repadmin /replsum, repadmin/showrepl commands working fine no error.  

Only sysvol is not replicated. So can i proceed Sysvol folder upgrade or not

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-04*

No, you'll need to fix what's broken as first step, which may involve removing the new domain controller. I'd check the event logs for related errors and a course of action.  

https://support.microsoft.com/en-us/help/290762/using-the-burflags-registry-key-to-reinitialize-file-replication-servi  

https://support.microsoft.com/en-us/help/257338/troubleshooting-missing-sysvol-and-netlogon-shares-on-windows-domain-c  

--please don't forget to Accept as answer if the reply is helpful--
