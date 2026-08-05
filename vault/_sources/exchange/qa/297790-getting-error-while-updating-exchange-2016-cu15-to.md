---
title: "Getting error while updating exchange 2016 CU15 to CU19"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/297790/getting-error-while-updating-exchange-2016-cu15-to
question_id: 297790
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Getting error while updating exchange 2016 CU15 to CU19

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/297790/getting-error-while-updating-exchange-2016-cu15-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have mailbox server which have exchange 2016 CU15 installed on it. When I am trying to install CU19 I am getting below errors please help- Setup will prepare the organization for Exchange Server 2016 by using 'Setup /PrepareAD'. No Exchange Server 2013 roles have been detected in this topology. After this operation, you will not be able to install any Exchange Server 2013 roles. For more information, visit: https://learn.microsoft.com/Exchange/plan-and-deploy/deployment-ref/readiness-checks?view=exchserver-2016 Setup will prepare the organization for Exchange Server 2016 by using 'Setup /PrepareAD'. No Exchange Server 2010 roles have been detected in this topology. After this operation, you will not be able to install any Exchange Server 2010 roles. For more information, visit: https://learn.microsoft.com/Exchange/plan-and-deploy/deployment-ref/readiness-checks?view=exchserver-2016 The Mailbox server role isn't installed on this computer. For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.UnifiedMessagingRoleNotInstalled.aspx The Mailbox server role isn't installed on this computer. For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.BridgeheadRoleNotInstalled.aspx The Active Directory schema isn't up-to-date, and this user account isn't a member of the 'Schema Admins' and/or 'Enterprise Admins' groups. For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.SchemaUpdateRequired.aspx Global updates need to be made to Active Directory, and this user account isn't a member of the 'Enterprise Admins' group. For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.GlobalUpdateRequired.aspx The local domain needs to be updated. You must be a member of the 'Domain Admins' group and 'Organization Management' role group, or 'Enterprise Admins' group to continue. For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.LocalDomainPrep.aspx You must be a member of the 'Organization Management' role group or a member of the 'Enterprise Admins' group to continue. For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.GlobalServerInstall.aspx You must use an account that's a member of the Organization Management role group to install or upgrade the first Mailbox server role in the topology. For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.DelegatedBridgeheadFirstInstall.aspx You must use an account that's a member of the Organization Management role group to install the first Client Access server role in the topology. For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.DelegatedCafeFirstInstall.aspx You must use an account that's a member of the Organization Management role group to install the first Client Access server role in the topology. For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.DelegatedFrontendTransportFirstInstall.aspx You must use an account that's a member of the Organization Management role group to install or upgrade the first Mailbox server role in the topology. For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.DelegatedMailboxFirstInstall.aspx You must use an account that's a member of the Organization Management role group to install or upgrade the first Client Access server role in the topology. For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.DelegatedClientAccessFirstInstall.aspx You must use an account that's a member of the Organization Management role group to install the first Mailbox server role in the topology. For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.DelegatedUnifiedMessagingFirstInstall.aspx Setup encountered a problem while validating the state of Active Directory: The user-specified domain controller cannot be used because setup has determined that it must use the schema master domain controller. See the Exchange setup log for more information on this error. For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.AdInitErrorRule.aspx The forest functional level of the current Active Directory forest is not Windows Server 2003 native or later. To install Exchange Server 2016, the forest functional level must be at least Windows Server 2003 native. For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.ForestLevelNotWin2003Native.aspx Either Active Directory doesn't exist, or it can't be contacted. For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.CannotAccessAD.aspx The Exchange Server setup operation didn't complete. More details can be found in ExchangeSetup.log located in the <SystemDrive>:\ExchangeSetupLogs folder.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-03-14*

This issue may be caused because your exchange server is not in the primary AD Site. Try the below:

1) Run prepare schema, prepare AD and prepare all domains from a member server in the primary site  

2) Force AD Replication and then try Exchange CU installation

If it still fails, then move the schema master role to a DC in the same site as the exchange server. Then run prepare schema, prepare AD, prepare all domains from the exchange server.

You should be able to successfully install Exchange CU after this.

Regards,  

Jay Thakker

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-05*

Hi,    

Have you tried /PrepareSchema and /PrepareAD after that? Does it work?    

When Exchange setup fails, it would give you lots of reasons. The real cause is just one of them.    

You may also need to check if schema master role is on your DC in same site.    

And try updating with command in elevated CMD:    

```
setup /m:upgrade /IAcceptExchangeServerLicenseTerms
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-04*

I read between the exchange setup log. If this helps more-

[03/04/2021 03:17:24.0945] [0] Setup will use the path 'F:\' for installing Exchange.  

[03/04/2021 03:17:24.0947] [0] Setup will discover the installed roles from server object '<server DN>'.  

[03/04/2021 03:17:24.0949] [0] 'BridgeheadRole' is installed on the server object.  

[03/04/2021 03:17:24.0949] [0] 'ClientAccessRole' is installed on the server object.  

[03/04/2021 03:17:24.0949] [0] 'MailboxRole' is installed on the server object.  

[03/04/2021 03:17:24.0949] [0] 'UnifiedMessagingRole' is installed on the server object.  

[03/04/2021 03:17:24.0949] [0] 'CafeRole' is installed on the server object.  

[03/04/2021 03:17:24.0949] [0] 'FrontendTransportRole' is installed on the server object.  

[03/04/2021 03:17:24.0951] [0] The installation mode is set to: 'BuildToBuildUpgrade'.  

[03/04/2021 03:17:30.0007] [0] An Exchange organization with name 'Exchange' was found in this forest.  

[03/04/2021 03:17:30.0007] [0] Active Directory Initialization status : 'False'.  

[03/04/2021 03:17:30.0008] [0] Schema Update Required Status : 'True'.  

[03/04/2021 03:17:30.0008] [0] Organization Configuration Update Required Status : 'True'.  

[03/04/2021 03:17:30.0009] [0] Domain Configuration Update Required Status : 'True'.  

[03/04/2021 03:17:30.0010] [0] The locally installed version is 15.1.1913.5.  

[03/04/2021 03:17:30.0011] [0] Exchange Installation Directory : 'E:\Microsoft\Exchange'.  

[03/04/2021 03:17:30.0070] [0] Setup is determining what organization-level operations to perform.  

[03/04/2021 03:17:30.0070] [0] Setup has detected a missing value. Setup is adding the value PrepareSchema.  

[03/04/2021 03:17:30.0070] [0] Setup has detected a missing value. Setup is adding the value PrepareOrganization.  

[03/04/2021 03:17:30.0070] [0] Setup has detected a missing value. Setup is adding the value PrepareDomain.  

[03/04/2021 03:17:30.0071] [0] Because the value was specified, setup is setting the argument OrganizationName to the value Exchange.  

[03/04/2021 03:17:30.0087] [0] RootDataHandler has 1 DataHandlers  

[03/04/2021 03:17:30.0087] [0] Languages  

[03/04/2021 03:17:30.0087] [0] Management tools  

[03/04/2021 03:17:30.0088] [0] Mailbox role: Transport service  

[03/04/2021 03:17:30.0089] [0] Mailbox role: Client Access service  

[03/04/2021 03:17:30.0090] [0] Mailbox role: Unified Messaging service  

[03/04/2021 03:17:30.0090] [0] Mailbox role: Mailbox service  

[03/04/2021 03:17:30.0091] [0] Mailbox role: Front End Transport service  

[03/04/2021 03:17:30.0092] [0] Mailbox role: Client Access Front End service  

[03/04/2021 03:17:30.0101] [0] Validating options for the 7 requested roles  

[03/04/2021 03:17:30.0101] [0] UpgradeModeDataHandler has 18 handlers and 18 work units  

[03/04/2021 03:17:30.0127] [0] Performing Microsoft Exchange Server Prerequisite Check  

[03/04/2021 03:17:30.0147] [0] Setup is determining what organization-level operations to perform.  

[03/04/2021 03:17:30.0147] [0] Setup has detected a missing value. Setup is adding the value PrepareSchema.  

[03/04/2021 03:17:30.0147] [0] Setup has detected a missing value. Setup is adding the value PrepareOrganization.  

[03/04/2021 03:17:30.0147] [0] Setup has detected a missing value. Setup is adding the value PrepareDomain.  

[03/04/2021 03:17:30.0147] [0] Because the value was specified, setup is setting the argument OrganizationName to the value Exchange.
