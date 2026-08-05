---
title: "Active Directory PDC Crashed."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1200353/active-directory-pdc-crashed
question_id: 1200353
fetched: 2026-07-25
answer_count: 15
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory PDC Crashed.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1200353/active-directory-pdc-crashed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear All,
Our Primary Domain Controller crashed and we restored it from backup. After Restoring from the backup we are not able to create a new user and add a new machine to the domain because of an error in the RID pool. We fixed the rid pool and created 2 ADC.
To one of the ADC, we moved all the FSMO roles.
Now we are facing the following issues.

-  Unable to access SysVol from any machine in the domain. Authentication Failure. 

-  If we disable the network card, we are getting an error message domain controller is not available for authentication even though we have 2 ADC.

-  In Group Policy, it is showing that unable to replicate.

Kindly Help us to fix this issue. we want one of our ADC to be promoted to PDC and another to ADC. We also need all the group policies set up and running in the new PDC.
Thanks and Regards 
Faiz

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-09*

Dear Dave,
Thanks for your kind support.
We did the following.

-  To enable the DFS Replication service to automatically recover databases, modify the following registry key:
   HKLM\System\CurrentControlSet\Services\DFSR\Parameters\StopReplicationOnAutoRecovery

-  The hotfix is not installed. Kindly advise if the same need to do in Server 2012.

-  The ADCs are not removed yet. those servers are acting as DNS servers for users. Kindly advise if it is mandatory to remove it.

We are actually in a confused state. what are the steps to be done and in which order? Kindly advise us on what steps to be followed in which sequence.
DFSR errors and warnings are saved in this share.
https://1drv.ms/f/s!AhiPGonwBafPkFeNcKeJJmhhnjVI?e=3Cw20j

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-04-07*

-  Check the domain controller times are in sync.  

DFS Replication service stopped replication. This occurs when a DFSR JET database is not shut down cleanly and Auto Recovery is disabled  

-  Try the manual step mentioned here.  

https://support.microsoft.com/en-us/topic/changes-that-are-not-replicated-to-a-downstream-server-are-lost-on-the-upstream-server-after-an-automatic-recovery-process-occurs-in-a-dfs-replication-environment-in-windows-server-2008-r2-beb3536b-41db-8ae2-d360-b23194de32bc  

-  SERVER IS NOT RESPONDING or IS NOT CONSIDERED SUITABLE
   This likely is because of the sysvol problems (jet database offline)

Looks like there are many system event log errors that will need to be corrected. I'm also wondering what other roles are installed on this domain controller. IIS and SQL Server should never be installed on a domain controller.  I'd remove the two new addition domain controllers until all errors are cleared up with this one.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-04-06*

Not a lot to go on but try working through this one.  

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-04-06*

Ok, first step after you do the restore, I'd confirm domain health is 100% (dcdiag, repadmin tools) also check the system and dfs replication event logs are free of all errors. Do not add more domain controllers until error free.

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-04-06*

Our Primary Domain Controller crashed and we restored it from backup

It isn't clear but if there are multiple domain controllers then restoring one from backup is not recommended. Cleaner / safer option is to seize roles to another healthy one. Then do cleanup to remove remnants of failed one.
Clean up Active Directory Domain Controller server metadata
Step-By-Step: Manually Removing A Domain Controller Server  

Then stand up a new one for replacement. I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new one, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one. 

-  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
