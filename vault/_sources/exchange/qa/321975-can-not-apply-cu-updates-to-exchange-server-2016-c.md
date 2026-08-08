---
title: "Can not apply CU updates to Exchange Server 2016 Coexistence Edition"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/321975/can-not-apply-cu-updates-to-exchange-server-2016-c
question_id: 321975
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Can not apply CU updates to Exchange Server 2016 Coexistence Edition

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/321975/can-not-apply-cu-updates-to-exchange-server-2016-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I wanted to update my Exchange Server using the latest CU19 which had the ZeroDay patch in it. Unfortunately I failed saying that Exchange was not installed and there were no mailboxes. Fortunately MS provided a special KB5000871 patch for Exchange 2016 CU13 several days later. This installed without any problems.  

Is there a special way of patching Exchange Server 2016 Edition "Coexistence"? I would really like to get this up to the latest CU level.  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-07*

My apologies for taking so long to get back.  

I validated that I had all the required roles. I didn't have all the roles. Later I tested with a user that did with exactly the some results unfortunately.  

The exchange server I am currently attempting to update is at a remote site with a DC which replicates with my DCs at the primary site. The remote site is not Schema Master.  

I have a question about my DNS and AD Sites and Services.  

-  DNS shows under "_sites" the following. "Default-First-Site-Name", "VDC1" and "VDC2"  

-  AD Sites and Services has , "VDC1" and "VDC2" only. "Default-First-Site-Name" was renamed to VDC1 several years ago.  

Could this be what is causing the problem?  

I will create a test lab later although this might take a while due to other work.  

Thanks  

List item

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-25*

Hi @Kai Yao       

I have tested using the same userid as the person who originally install the Exchange Hybrid system assuming that it should work. Unfortunately that was not the case.    

As another test I tried installing a CU which didn't require a AD prep or schema change. Even that didn't work.  I wondering if there is a issue with not having "Default-First-Site-Name" in Sites and Services anymore; It only appears in DNS.    

I will review this further in the next couple of weeks.    

The errors that I an getting are as follows which I need to review.     

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

Setup encountered a problem while validating the state of Active Directory: Exchange organization-level objects have not been created, and setup cannot create them because the local computer is not in the same domain and site as the schema master.  Run setup with the /prepareAD parameter on a computer in the domain vifm and site VDC1, and wait for replication to complete.  See the Exchange setup log for more information on this error.    

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

Thanks for any assistance.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-22*

Hi, @SeekingTruth       

The hybrid environment should not affect the CU update of the on-premise server.    

Is the error message like "The Mailbox server role isn't installed on this computer."?    

And do you see other error messages?    

For example, "You must use an account that's a member of the Organization Management role group ...".    

Please post a screenshot of the detailed error messages if possible.    

(Don't forget to hide your personal information for security.)    

Please make sure the Exchange server is in the same site and domain as the Schema master (primary domain controller).    

And you are using an account which has the required permissions (a member of Enterprise Admins,Domain Admins and Organization Management role group)    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
