---
title: "Cannot upgrade Hybrid Exchange 2016 CU 20 to CU 23"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1035261/cannot-upgrade-hybrid-exchange-2016-cu-20-to-cu-23
question_id: 1035261
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# Cannot upgrade Hybrid Exchange 2016 CU 20 to CU 23

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1035261/cannot-upgrade-hybrid-exchange-2016-cu-20-to-cu-23 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The only exchange server left on prem after the migration to exchange online is a management server required for hybrid management of mailboxes via on prem AD. It is NOT one of the original on prem servers. It is Exchange 2016 CU 20. Single Forest, Single Domain. Exchange Server not in same AD Sites & Services site as Schema Master. Ran Setup.exe as administrator as well as an elevated command prompt (D:\>setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF /Mode:Upgrade /DomainController:FQDNOfSchemaMaster /EnableErrorReporting), both with same result. Account used is a member of Exchange Organization Administrators, Domain Admins, and Enterprise Admins. Domain and Forest Function Levels are Windows Server 2016. Pictures are from on prem EAC. What do I need to do for the upgrade to work?

Errors  

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

Setup encountered a problem while validating the state of Active Directory: Exchange organization-level objects have not been created, and setup cannot create them because the local computer is not in the same domain and site as the schema master. Run setup with the /prepareAD parameter on a computer in the domain bvs and site CedarRapids, and wait for replication to complete. See the Exchange setup log for more information on this error.  

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.AdInitErrorRule.aspx

Error:  

The forest functional level of the current Active Directory forest is not Windows Server 2003 native or later. To install Exchange Server 2016, the forest functional level must be at least Windows Server 2003 native.  

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.ForestLevelNotWin2003Native.aspx

Error:  

Either Active Directory doesn't exist, or it can't be contacted.  

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.CannotAccessAD.aspx

Error:  

The 'IIS URL rewrite module' isn't installed on this computer and needs to be installed before Exchange Setup can begin.  

For more information, visit: https://learn.microsoft.com/Exchange/plan-and-deploy/deployment-ref/ms-exch-setupreadiness-IISURLRewriteNotInstalled?view=exchserver-2016

Warning:  

Setup will prepare the organization for Exchange Server 2016 by using 'Setup /PrepareAD'. No Exchange Server 2013 roles have been detected in this topology. After this operation, you will not be able to install any Exchange Server 2013 roles.  

For more information, visit: https://learn.microsoft.com/Exchange/plan-and-deploy/deployment-ref/readiness-checks?view=exchserver-2016

Warning:  

Setup will prepare the organization for Exchange Server 2016 by using 'Setup /PrepareAD'. No Exchange Server 2010 roles have been detected in this topology. After this operation, you will not be able to install any Exchange Server 2010 roles.  

For more information, visit: https://learn.microsoft.com/Exchange/plan-and-deploy/deployment-ref/readiness-checks?view=exchserver-2016

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-05*

I added the account to Schema admins and then ran those few commands (Thanks AndyDavid!) from and elevated command prompt on a server in the same site as the Schema master. I was then able to complete the command     

Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /Mode:Upgrade /DomainController:XXXXXX.XXXXXXXXXX.XXX    

on the server in the other site (pointing to the domain controller in that site).

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-05*

@Wayne Lauer      

Make sure the connection between DC and Exchange server is ok.     

Then I would suggest you create a new admin account with permission below:    

    

Then use this new admin command to run the command that AndyDavid provided.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
