---
title: "Adding a 2019 server domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/66480/adding-a-2019-server-domain-controller
question_id: 66480
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Adding a 2019 server domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/66480/adding-a-2019-server-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, we currently have a 2008 R2 primary domain controller and a 2012 R2 secondary domain controller. We would like to add a 2019 domain controller and demote the 2008. Currently I have entered the following commend in powershell Test-ADDSDomainControllerInstallation -DomainName <domainname>

Getting the following measage......

Message

Test VerifyAdminTrustedForDelegation completed successfully  

Test VerifyADPrepPrerequisites completed successfully  

Verification of prerequisites for Domain Controller promotion failed. The forest functional level is not supported. ...  

Test VerifyOutboundReplicationEnabled completed successfully

Can someone help with the problem on the third line?  

Thank you

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2020-08-14*

Hello ValdyRossit-0408,

Thank you for posting here.

Here are the answer for your references.

Q: we currently have a 2008 R2 primary domain controller and a 2012 R2 secondary domain controller. We would like to add a 2019 domain controller and demote the 2008.  

A:  

1. Before we add 2019 DC into existing domain, we should ensure:  

The minimum requirement to add a Windows Server 2019 Domain Controller is a Windows Server 2008 functional level. The domain also has to use DFS-R as the engine to replicate SYSVOL.

So we can check the forest functional level and domain functional level on 2008 R2 primary domain controller as below:

Check functional level through GUI.  

Open Active Directory Domains and Trusts\right click Active Directory Domains and Trusts\Raise Forest Functional Level\Check forest functional level.  

Open Active Directory Domains and Trusts\right click domain name\Raise Domain Functional Level\Check domain functional level.  

Or check functional level through PowerShell command.  

(Get-ADForest).ForestMode  

(Get-ADDomain).DomainMode  

Check If SVSVOL replication is DFR replication type or FRS replication type on 2008 R2 primary domain controller through registry.  

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.

2. Before we do any change in existing AD domain environment, we had better do:  

-  Check if AD environment is healthy. Check all DCs in this domain is working fine by running Dcdiag /v.  

Check if AD replication works properly by running repadmin /showrepl and repadmin /replsum.  

-  We had better back up all domain controllers.

3. For add a 2019 domain controller, the steps below are for your reference:  

-  Add the new Window server 2019 to the existing domain.  

-  Add AD DS and DNS roles and promote this Windows server 2019 as a DC (as a GC).  

-  Check if AD environment is healthy again.  

-  If AD environment is running fine, we can transfer FSMO roles to new 2019 DC if needed.  

-  Demote old 2008 R2 DC if needed after transferring FSMO roles. Before we demote 2008 R2 DC, we should also check:

If the removed DC was a DNS server, update the DNS client configuration on all member workstations, member servers, and other DCs that might have used this DNS server for name resolution. If it is required, modify the DHCP scope to reflect the removal of the DNS server.

If the removed DC was a DNS server, update the Forwarder settings and the Delegation settings on any other DNS servers that might have pointed to the removed DC for name resolution.

4. From the error message “Verification of prerequisites for Domain Controller promotion failed. The forest functional level is not supported. ...” we provided, maybe we need to raise forest functional level.

Before raising function level, we should understand:

1)Ensure that all domain functional levels are equal to or higher than the forest functional level;  

2)Ensure that the operating system level of all domain controllers is equal to or higher than the domain functional level;  

3)The domain function level can only be upgraded on the PDC;  

4)The forest functional level can only be upgraded on the schema master.  

5)Raise methods:  

Open Active Directory Domains and Trusts\right click Active Directory Domains and Trusts\Raise Forest Functional Level.  

Open Active Directory Domains and Trusts\right click domain name\Raise Domain Functional Level.  

6) As a kind of reminder, perhaps the applications on workstations or member servers may be impacted by forest functional level and/or the operating system version of domain controllers. So before raising forest functional level, we can check if there is any impact on any application in your AD environment.

For example:  

Whether specific Exchange version can be supported, it depends on server operating system version installed with Exchange, Exchange version and Active Directory environments (including DC operating system version and AD forest functional level).

Exchange Server supportability matrix  

https://learn.microsoft.com/en-us/Exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019

If we need to migrate SVYSVOL from FRS to DFSR, for migrating FRS to DFSR, we can refer to the link below.  

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405

5. If you have already added one 2019 DC into the existing domain, and functional level or SYSVOL replication type does not meet the AD requirement:  

1)We can demote this 2019 DC, check AD health.  

2)Raise functional level or migrate SYSVOL if needed.  

3)Check AD health again.  

4)Re-promote this 2019 server as DC.

If it does not work above, in order to better troubleshoot the problem, please confirm the following information:

1.Are the forest functional level and domain functional level of the existing domain both 2008 R2 or higher?  

2.Is the SYSVOL replication mode FRS or DFSR?  

3.Follow the above method to check whether the AD environment is working properly?  

4.Have you already added the 2019 DC into the domain?  

5.Which server do you run the PowerShell command on (do you run the PS command on the new 2019 DC)?

Hope the information above is helpful. If anything is unclear, please feel free to let us know.

Best Regards,  

Daisy Zhou

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-13*

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR  

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405  

I'd use dcdiag / repadmin tools to verify health correcting all errors found before starting any operations. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-08-13*

You have to raise the forest functional level to at least 2008, better 2008 R2.    

https://social.technet.microsoft.com/Forums/en-US/6c407784-002b-47fc-bbb7-25b0ca04ac82/adding-a-windows-server-2019-domain-controller?forum=winserverDS    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels    

--please don't forget to Accept as answer if the reply is helpful--
