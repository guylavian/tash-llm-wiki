---
title: "Prepare AD error after updating Exchange 2016 to CU 18"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/173270/prepare-ad-error-after-updating-exchange-2016-to-c
question_id: 173270
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Prepare AD error after updating Exchange 2016 to CU 18

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/173270/prepare-ad-error-after-updating-exchange-2016-to-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi    

I am getting this error after updating to Exchange server 2016 CU 18 when trying to prepare AD after an accidental deleting of arbitration mailbox:    

Setup will prepare the organization for Exchange Server 2016 by using 'Setup /PrepareAD'. No Exchange Server 2013 roles have been detected in this topology. After this operation, you will not be able to install any Exchange Server 2013 roles.    

For more information, visit: https://learn.microsoft.com/Exchange/plan-and-deploy/deployment-ref/readiness-checks?view=exchserver-2016    

Setup will prepare the organization for Exchange Server 2016 by using 'Setup /PrepareAD'. No Exchange Server 2010 roles have been detected in this topology. After this operation, you will not be able to install any Exchange Server 2010 roles. For more information, visit: https://learn.microsoft.com/Exchange/plan-and-deploy/deployment-ref/readiness-checks?view=exchserver-2016    

Global updates need to be made to Active Directory, and this user account isn't a member of the 'Enterprise Admins' group. For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.GlobalUpdateRequired.aspx    

The local domain needs to be updated. You must be a member of the 'Domain Admins' group and 'Organization Management' role group, or 'Enterprise Admins' group to continue.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.LocalDomainPrep.aspx    

Setup encountered a problem while validating the state of Active Directory: The Active Directory organization configuration version (16752) is higher than Setup's version(16218). Therefore, PrepareAD can't be executed. See the Exchange setup log for more information on this error.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.AdInitErrorRule.aspx    

The forest functional level of the current Active Directory forest is not Windows Server 2003 native or later. To install Exchange Server 2016, the forest functional level must be at least Windows Server 2003 native.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.ForestLevelNotWin2003Native.aspx    

Either Active Directory doesn't exist, or it can't be contacted.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.CannotAccessAD.aspx    

The Exchange Server setup operation didn't complete. More details can be found in ExchangeSetup.log located in the <SystemDrive>:\ExchangeSetupLogs folder.    

Obviously, the account is member of both Enterprise Admin and Domain Admin. The forest has two domains (domain.local and domain.com). The FSMO role is located on 'domain.local' and so is the Exchange server.    

The DC is running WS2019 standard and the EX WS2012R2.    

Please advise - thank you in advance.    

Best regards    

Kris

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-24*

Hi  

Thank you - that was really helpful!
