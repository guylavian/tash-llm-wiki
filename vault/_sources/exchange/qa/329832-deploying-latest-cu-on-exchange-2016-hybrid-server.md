---
title: "Deploying latest CU on Exchange 2016 Hybrid server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/329832/deploying-latest-cu-on-exchange-2016-hybrid-server
question_id: 329832
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Deploying latest CU on Exchange 2016 Hybrid server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/329832/deploying-latest-cu-on-exchange-2016-hybrid-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an AD forest with a "empty" root domain, let's refer to it as root.local, and a subdomain, child.root.local.  Our Exchange 2016 CU15 server is located in the child domain, and is the hybrid server for our Exchange Online mailboxes.  The Exchange Server (in child.root.local) and Schema Master role holder (in root.local) are in the same Site.  This Exchange server was setup by a third party, who left no documentation on setup.  

My account is in the root.local Schema and Enterprise Admin groups, as well as the Organization Management group.  

When running setup.exe for CU20, we receive messages indicating account permission issues, mailbox roles not found, etc.  I assume this is due to the multi-domain and requires PrepareSchema and/or PrepareAD to be run first.  

Question is:  Do I need to run /PrepareDomain switch for the root and child domain after running /PrepareAD in each?  And when and where (root or child) do I run the /TenantOrganizationConfig switch (and is it necessary for a CU install?)?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-24*

Error:    

A reboot from a previous installation is pending. Please restart the system and then rerun Setup.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.RebootPending.aspx    

Error:    

The Mailbox server role isn't installed on this computer.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.UnifiedMessagingRoleNotInstalled.aspx    

Error:    

The Mailbox server role isn't installed on this computer.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.BridgeheadRoleNotInstalled.aspx    

Error:    

The Active Directory schema isn't up-to-date, and this user account isn't a member of the 'Schema Admins' and/or 'Enterprise Admins' groups.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.SchemaUpdateRequired.aspx    

Error:    

Global updates need to be made to Active Directory, and this user account isn't a member of the 'Enterprise Admins' group.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.GlobalUpdateRequired.aspx    

Error:    

The local domain needs to be updated. You must be a member of the 'Domain Admins' group and 'Organization Management' role group, or 'Enterprise Admins' group to continue.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.LocalDomainPrep.aspx    

Error:    

You must be a member of the 'Organization Management' role group or a member of the 'Enterprise Admins' group to continue.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.GlobalServerInstall.aspx    

Error:    

You must use an account that's a member of the Organization Management role group to install or upgrade the first Mailbox server role in the topology.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.DelegatedBridgeheadFirstInstall.aspx    

Error:    

You must use an account that's a member of the Organization Management role group to install the first Client Access server role in the topology.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.DelegatedCafeFirstInstall.aspx    

Error:    

You must use an account that's a member of the Organization Management role group to install the first Client Access server role in the topology.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.DelegatedFrontendTransportFirstInstall.aspx    

Error:    

You must use an account that's a member of the Organization Management role group to install or upgrade the first Mailbox server role in the topology.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.DelegatedMailboxFirstInstall.aspx    

Error:    

You must use an account that's a member of the Organization Management role group to install or upgrade the first Client Access server role in the topology.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.DelegatedClientAccessFirstInstall.aspx    

Error:    

You must use an account that's a member of the Organization Management role group to install the first Mailbox server role in the topology.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.DelegatedUnifiedMessagingFirstInstall.aspx    

Error:    

Setup encountered a problem while validating the state of Active Directory: Exchange organization-level objects have not been created, and setup cannot create them because the local computer is not in the same domain and site as the schema master.  Run setup with the /prepareAD parameter on a computer in the domain firm and site EXP1, and wait for replication to complete.  See the Exchange setup log for more information on this error.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.AdInitErrorRule.aspx    

Error:    

The forest functional level of the current Active Directory forest is not Windows Server 2003 native or later. To install Exchange Server 2016, the forest functional level must be at least Windows Server 2003 native.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.ForestLevelNotWin2003Native.aspx    

Error:    

Either Active Directory doesn't exist, or it can't be contacted.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.CannotAccessAD.aspx    

Warning:    

Setup will prepare the organization for Exchange Server 2016 by using 'Setup /PrepareAD'. No Exchange Server 2013 roles have been detected in this topology. After this operation, you will not be able to install any Exchange Server 2013 roles.    

For more information, visit: https://learn.microsoft.com/Exchange/plan-and-deploy/deployment-ref/readiness-checks?view=exchserver-2016    

Warning:    

Setup will prepare the organization for Exchange Server 2016 by using 'Setup /PrepareAD'. No Exchange Server 2010 roles have been detected in this topology. After this operation, you will not be able to install any Exchange Server 2010 roles.    

For more information, visit: https://learn.microsoft.com/Exchange/plan-and-deploy/deployment-ref/readiness-checks?view=exchserver-2016    

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=    

[PS] xxxxxx>.\SetupAssist.ps1 -Verbose    

User Name          SID    

  ================== =============================================    

 child\adminxxxx ----------------------------------------    

User is an administrator.    

User is a member of CHILD\Domain Admins   S-1-5-21-    

User is a member of ROOT\Schema Admins   S-1-5-21-    

User is a member of ROOT\Enterprise Admins   S-1-5-    

User is a member of ROOT\Organization Management   S-1-5-21-    

ExecutionPolicy is Unrestricted    

No installer packages missing.    

No other PowerShell instances were detected.    

VERBOSE: Key set at: HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager - PendingFileRenameOperations. Remove it if    

 reboot doesn't work    

WARNING: Reboot pending.    

Exchange 2016 CU17 Ready.    

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=    

[PS] xxxxxx>.\SetupLogReviewer.ps1    

cmdlet SetupLogReviewer.ps1 at command pipeline position 1    

Supply values for the following parameters:    

SetupLog: C:\ExchangeSetupLogs\ExchangeSetup.log    

Setup.exe Run Date: 03/22/2021 17:34:31    

Current Exchange Build: 15.1.1913.5    

WARNING: Setup failed to validate AD environment level. This is the internal exception that occurred:    

Exchange organization-level objects have not been created, and setup cannot create them because the local computer is not in the same domain and site as the schema master.  Run setup with the /prepareAD parameter on a computer in the domain firm and site EXP1, and wait for replication to complete.    

Additional Context:    

User Logged On: CHILD\adminxxxxxx    

Setup Running on: EOLMGMT01.child.root.local    

Setup Running in Domain: CHILD    

Setup Running in AD Site Name: EXP1    

----------------------------------    

Schema Master: ROOT-DC01.root.local    

Schema Master in Domain: ROOT    

Unable to run setup in current domain.
