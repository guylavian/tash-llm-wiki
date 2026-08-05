---
title: "SysVol replication fails on the DFS replication."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1690414/sysvol-replication-fails-on-the-dfs-replication
question_id: 1690414
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# SysVol replication fails on the DFS replication.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1690414/sysvol-replication-fails-on-the-dfs-replication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,

Please assist with the below issue.

I have two Domain controllers running server 2016 and the replication is not working. we are using the DFS replication

Im getting the below error when i run Dcdiag

CN=NTDS Settings,CN=AD01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=ecn,DC=local

 Base Object Description: "DSA Object"

 Value Object Attribute Name: serverReferenceBL

 Value Object Description: "SYSVOL FRS Member Object"

 Recommended Action: See Knowledge Base Article: Q312862

Netshare does show that sysvol ,netlogon is shared however they are not up to date. please assist and feel free to ask for more

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-03*

Hello Mahlatse,

Thank you for posting in Q&A forum.

1.Based on the description above, do you have one forest with single one domain and two domain controllers?  

2.If so, please check the AD replication in the entire AD forest, please run commands below on PDC in the forest root domain.  

repadmin /showrepl >C:\rep1.txt

repadmin /replsum >C:\rep2.txt

repadmin /showrepl * /csv >c:\repsum.csv

3.Please confirm the SYSVOL replication engine again.  

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.  

4.If the AD replication is OK and the SYSVOL replication engine is DFSR.  

Please back up all the domain controllers (System state or full server) using the built-in Windows server backup role, and back up SYSVOL folder on every Domain Controller.  

Then try to fix the SYSVOL replication based on the steps in the part 

"How to perform a non-authoritative synchronization of DFSR-replicated sysvol replication (like D2 for FRS)" in the link.

Force synchronization for Distributed File System Replication (DFSR) replicated sysvol replication - Windows Server | Microsoft Learn

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
