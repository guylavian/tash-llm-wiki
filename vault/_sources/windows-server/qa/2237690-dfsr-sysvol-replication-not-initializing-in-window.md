---
title: "DFSR SYSVOL Replication Not Initializing in Windows Server 2019 (New Domain, 2016 Functional Level)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2237690/dfsr-sysvol-replication-not-initializing-in-window
question_id: 2237690
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# DFSR SYSVOL Replication Not Initializing in Windows Server 2019 (New Domain, 2016 Functional Level)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2237690/dfsr-sysvol-replication-not-initializing-in-window (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Issue Summary:

I have set up a brand-new Windows Server 2019 domain, but SYSVOL replication is not functioning correctly with DFSR. This is occurring immediately after domain promotion, before any custom modifications were made.

Environment Details:

-  Windows Server 2019 Standard (Eval)

-  Two domain controllers: DC01 (PDC Emulator) and DC02

-  Domain functional level: Windows Server 2016

-  Fresh domain install, no schema modifications or migrations

-  `dfsrMig /GetGlobalState` returns "Eliminated" (expected)

-  SYSVOL and NETLOGON are shared

-  DFSR service is running

-  Active Directory replication (NTDS) is working correctly

-  However, DFSR replication does not occur, and no DFSR connection objects exist in ADSI Edit

What I Have Checked So Far:

-  DFSR Service is Running

-  SYSVOL and NETLOGON Shares Exist

-  DFSR Recognizes SYSVOL in WMI

-  State is reported as 4

-  DFSR Membership Exists

-  Both DCs show up as DFSR members

-  No DFSR Connection Objects

-  DFSR is not replicating and no `msDFSR-Connection` objects exist

-  Manual Creation Fails

-  Manual creation of DFSR connection objects fails with: "The object cannot be added because the parent is not on the list of possible superiors."

-  No DFSR Event Log Exists

-  DFSR log is missing from Event Viewer

Key Questions:

-  Should DFSR automatically create connection objects in a new domain?

-  Is this a known issue or bug with Server 2019 DFSR initialization?

-  Does Server 2019 require additional configuration for DFSR to function properly in a 2016-level domain?

-  Could schema or default container misconfiguration be preventing DFSR from creating connection objects?

Any guidance or confirmation of expected behavior would be appreciated—especially if this is a known Microsoft issue.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-24*

Hello Daisy,

Thanks for the answer...my ultimate problem is failing GPO application that doesnt make much sense...this is a new install I stood up to help in troubleshooting my live domain but once I had it all setup it was exhibiting the same replication behaviour. 

I'm not very knowledgeable when it comes to replication so I am going by feel a lot with a lot of Google Fu without really understanding it all. The contents of SYSVOL on both DCs are identical, the command /showrepl returns the correct inbound neighbor and the last attempts are all within 5 minutes  

command repadmin /replsum shows no fails, 5 total, and the largest Delta a bit over 5 minutes  

BUT, when I use dfsrdiag replicationstate i get no active inbound connections and no updates received. Maybe this is normal? As I said, not well-versed in this.

In Regedit, the key HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState doesnt exist, however HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\MigratingSysVols has a Global State, Local State, and Migrating State, and they are all set at 3.

What has been pointing me to a replication issue is the dfsrdiag /replicationstate, but maybe I have been chasing a non-existent issue? I still have GPO deployment problems but if after seeing what I provide here you can definitively say the replication doesn't have any bearing on that then I will drop it and go back to trying to figure out the GPO stuff.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-24*

Hello support,  

Thank you for posting in Q&A forum. 

Based on the description, you have a new forest (root domain), domain functional level is Windows Server 2016, there are two DCs (Windows server 2019) in this domain, they are DC01 (PDC) and DC 02.

Before troubleshooting the SYSVOL replication problem, please make sure AD replication is Ok.  Please check the AD replication between two DCs first, run the commands below on PDC.

repadmin /showrepl >C:\rep1.txt 

repadmin /replsum >C:\rep2.txt 

repadmin /showrepl * /csv >c:\repsum.csv

Also, please check information below: HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.

If AD replication is OK and SYSVOL is using DFSR replication engine, what do you mean "DFSR replication does not occur, and no DFSR connection objects exist in ADSI Edit"? Please provide the screenshot about it.

If you mean the contents in the path C:\Windows\SYSVOL\sysvol\b.com\Policies on both DCs are different?

 For example:   

You can back up the DC one by one and SYSVOL folder on both DCs. Then try the steps in the part of "How to perform a non-authoritative synchronization of DFSR-replicated sysvol replication (like D2 for FRS)" in the following link.

If it does not work, you can try the steps in the part of "How to perform an authoritative synchronization of DFSR-replicated sysvol replication (like D4 for FRS)"  in the following link.

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization

I hope the information above is helpful. If there is anything I misunderstood, please correct me.

If you have any questions or concerns, please feel free to let us know. 

Best Regards, 

Daisy Zhou 

============================================ 

If the Answer is helpful, please click "Accept Answer" and upvote it.
