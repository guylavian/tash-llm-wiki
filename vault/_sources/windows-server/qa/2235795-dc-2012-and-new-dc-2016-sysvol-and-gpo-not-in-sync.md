---
title: "DC 2012 and new DC 2016 sysvol and gpo not in sync issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2235795/dc-2012-and-new-dc-2016-sysvol-and-gpo-not-in-sync
question_id: 2235795
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# DC 2012 and new DC 2016 sysvol and gpo not in sync issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2235795/dc-2012-and-new-dc-2016-sysvol-and-gpo-not-in-sync (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

We have 1 DC 2012 and when we promoted new DC 2016 into environment we got strange issues with gpo not in sync with baseline DC. All troubleshooting tools showing no errors. 

We run full dcdiag on both DC's, repadmin /showrepl and repadmin /replsummary all without issues.  

Every new GPO that is created got this issue and it complaining that the new DC has the issue. I also notice that the sysvol folder is not in sync which means that the new created gpos has different date modified.   

Steps that we did:

-  Authoritative sysvol restore

-  robocopy permissions copy

-  dcdiag pollad --> / repadmin / syncall  --> repadmin /syncall /adep

-  Servers up to date

-  Removed duplicate permissions via GPO on all GPO's

-  When we create new GPO, we can see it on both DC's but it is complaining on ACL  

What can we do? Please help.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-18*

Hello Kak Tak,

Thank you for posting in Q&A forum. 

Based on the description, as I understand you have only 1 DC 2012 before you add the new DC 2016, am I right? If so, please make sure everything is OK on 2012 DC before you add 2016 DC.

Then please check information below:

1.Please check the forest functional level and domain functional level.

Check the forest functional level by running PS command: (Get-ADForest).ForestMode 

Check the forest functional level by running PS command: (Get-ADDomain).DomainMode

2.Please check the SYSVOL replication type, it should be DFSR.

Check the registry value on Domain Controller.

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.

3.Check the FSMO roles by running netdom query fsmo.

4.Check group policy setting applied successfully on all machines.

5.After you add new 2016 DC, check AD replication again by running commands below on PDC.

repadmin /showrepl >C:\rep1.txt 

repadmin /replsum >C:\rep2.txt 

repadmin /showrepl * /csv >c:\repsum.csv

6.If AD replication is OK between 2012 DC and new 2016 DC, please back up every Domain Controller using Windows built-in back up role, and back up the SYSVOL folder on both DCs.

Then take actions based on the part 

"How to perform a non-authoritative synchronization of DFSR-replicated sysvol replication (like D2 for FRS)" on problematic DC (non-authoritative synchronization).

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization

7.If it does not work step 6, please take actions based on the part 

"How to perform an authoritative synchronization of DFSR-replicated sysvol replication (like D4 for FRS)" on working DC (an authoritative synchronization) (step 1- step 11)and then on problematic DC (non-authoritative synchronization) (step 12- step 14).

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization

Other reference

Active Directory Domain Services functional levels

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels

I hope the information above is helpful. 

If you have any questions or concerns, please feel free to let us know. 

Best Regards, 

Daisy Zhou 

============================================ 

If the Answer is helpful, please click "Accept Answer" and upvote it.
