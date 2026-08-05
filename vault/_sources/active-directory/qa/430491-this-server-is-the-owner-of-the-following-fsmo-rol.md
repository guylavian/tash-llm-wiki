---
title: "This server is the owner of the following FSMO role, but does not consider it valid."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/430491/this-server-is-the-owner-of-the-following-fsmo-rol
question_id: 430491
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# This server is the owner of the following FSMO role, but does not consider it valid.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/430491/this-server-is-the-owner-of-the-following-fsmo-rol (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

we have migrated servers from 2k8 to 2016 and the replication was working fine after the migration last week.  

But from yesterday there is replication issue and am getting the below error in event logs.  

I checked the schema master and naming master with below steps  

-  Type dsmgmt <enter>  

-  Type roles <enter>  

-  Type connections <enter>  

-  Type connect to server servername:portnumber of instance <enter>  

-  Type quit <enter>  

-  Type select operation target <enter>  

-  Type list roles for connected server <enter> Note: This should list who owns the FSMO roles.  

they are pointing to new servers and replication was working fine until yesterday morning.  

This server is the owner of the following FSMO role, but does not consider it valid. For the partition which contains the FSMO, this server has not replicated successfully with any of its partners since this server has been restarted. Replication errors are preventing validation of this role.   

Operations which require contacting a FSMO operation master will fail until this condition is corrected.   

FSMO Role: CN=Schema,CN=Configuration,CN={B4F5E18B-05C8-4E54-83D3-900A9BAA75EB}   

User Action:   

-  Initial synchronization is the first early replications done by a system as it is starting. A failure to initially synchronize may explain why a FSMO role cannot be validated. This process is explained in KB article 305476.   

-  This server has one or more replication partners, and replication is failing for all of these partners. Use the command repadmin /showrepl to display the replication errors.  Correct the error in question. For example there maybe problems with IP connectivity, DNS name resolution, or security authentication that are preventing successful replication.   

-  In the rare event that all replication partners are expected to be offline (for example, because of maintenance or disaster recovery), you can force the role to be validated. This can be done by using NTDSUTIL.EXE to seize the role to the same server. This may be done using the steps provided in KB articles 255504 and 324801 on http://support.microsoft.com.   

The following operations may be impacted:   

Schema: You will no longer be able to modify the schema for this forest.   

Domain Naming: You will no longer be able to add or remove domains from this forest.   

PDC: You will no longer be able to perform primary domain controller operations, such as Group Policy updates and password resets for non-Active Directory Lightweight Directory Services accounts.   

RID: You will not be able to allocation new security identifiers for new user accounts, computer accounts or security groups.   

Infrastructure: Cross-domain name references, such as universal group memberships, will not be updated properly if their target object is moved or renamed.  

could someone help to fix this? today we were facing slowness in application login functionality .could that be due to replication issue?  

Thanks

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-10*

Regardless, the configuration is incorrect so expect the unexpected results to continue as it is.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-10*

Hi ,  

Thanks for the quick analysis.  

I just wonder how the replication has worked last week and why are these are causing issues now.  

and we have the similar setup in DEV env and there it works without any issues.  

Regards,  

Rathi

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-10*

SOK-24-34-26 is multi-homed so I'd disable the second adapter.  

SOK-24-34-26 should have own static ip address (172.24.34.26) listed for DNS and no others such as router or public DNS (if the 10.208.40.x are not domain controllers then remove them) then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service  

SOK-24-34-27 is multi-homed so I'd disable the second adapter.  

SOK-24-34-27 should have own static ip address (172.24.34.27) listed for DNS and no others such as router or public DNS (if the 10.208.40.x are not domain controllers then remove them) then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service  

I did not bother to look at the other files since these ones are show stoppers. After corrections if problems persist then put up a new set of files to look at.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-10*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

then put `unzipped` text files up on OneDrive and share a link.  

Dcdiag /skip:systemlog /v /c /d /e /s:%computername% >c:\dcdiag.log

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-10*

How many domain controllers? Are the old ones still available?
