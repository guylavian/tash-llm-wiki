---
title: "Cross Forest Domain Migration with Exchange Hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1865191/cross-forest-domain-migration-with-exchange-hybrid
question_id: 1865191
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Cross Forest Domain Migration with Exchange Hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1865191/cross-forest-domain-migration-with-exchange-hybrid (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Currently I've a single forest (Forest A) and need to perform cross-forest migration to Forest B due to acquisition and merger. Forest A currently have Exchange on-prem with Exchange hybrid setup. As researched, I do not have any issue in migrating the on-prem mailboxes to Forest B with ADMT & move request in mailboxes migration. But how about the Exchange Hybrid? The new exchange in Forest B will have hybrid back to the existing M365 tenant with different custom domain name. Below would be my questions:

-  How about the migrated users objects and their mailbox which sitting on the M365 tenant currently? If I have already use the ms-consistencyGUID as the source anchor, anything else I need to do?

-  To reconfigure the Hybrid connection from forest B, I will have to remove Exchange hybrid from Forest A first then establish for forest B?

-  Appreciate if anyone could advise the proper steps in doing this cross-forest migration with exchange hybrid in-place.

Thank you.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-15*

Cross-forest migrations, especially when it involves Exchange hybrid environments, can be complex. Here’s a general outline to guide you through the process considering your specific scenario:

Phase 1: Preparation

-  Assess and Plan:

-  Conduct a thorough assessment of your current environment.

-  Ensure that your new Exchange environment in Forest B is set up correctly and is ready to host mailboxes.

-  ADMT (Active Directory Migration Tool):

-  Use ADMT to migrate user accounts and related objects from Forest A to Forest B.

-  Ensure that the ms-DS-ConsistencyGUID attribute is being used as the source anchor. This should smooth the integration with Azure AD.

Phase 2: Transition to Forest B

-  Prepare Forest B for Hybrid Deployment:

-  Configure Exchange in Forest B with a hybrid setup.

-  You'll need to add the necessary domains in your M365 tenant for Forest B.

-  Remove Hybrid from Forest A:

-  Properly decommission the hybrid setup in Forest A to free up the tenant for reconfiguration.

-  Ensure all mailboxes are either moved or properly handled to avoid data loss.

-  Establish Hybrid in Forest B:

-  Run the Hybrid Configuration Wizard (HCW) to establish a new hybrid setup between Exchange in Forest B and the existing M365 tenant.

-  Ensure that all necessary DNS records are updated appropriately.

Phase 3: Migrating Mailboxes

-  Sync Mailboxes:

-  Use the Move Mailbox wizard or PowerShell scripts to move mailboxes from on-premises in Forest B to M365.

-  Make sure email flow and calendar sharing are working correctly.

-  Test and Validate:

-  Thoroughly test mail flow, calendar sharing, and access permissions after each stage of migration.

-  Communicate with end users to ensure there are no issues with their mailboxes post-migration.

Specific Concerns:

-  Migrated User Objects and Mailboxes:  If you have used the ms-DS-ConsistencyGUID as the source anchor, ensure that these attributes are correctly synchronized with Azure AD. Validate user objects to ensure they are recognized correctly in Azure AD post-migration.

-  Reconfiguring Hybrid:  Yes, typically, you would need to decommission the hybrid connection from Forest A before establishing it in Forest B. This helps prevent any conflicts or misconfigurations.

Steps Overview:

-  Prepare Exchange in Forest B.

-  Decommission hybrid in Forest A.

-  Configure hybrid for Forest B.

-  Migrate mailboxes and validate.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-14*

Hi,

Thanks for posting your question in Microsoft Q&A forum!

Based on your description, I found a case that have similar question to yours. You can refer to:

https://answers.microsoft.com/en-us/msoffice/forum/all/cross-forest-exchange-migration-with-hybrid/2e6d59b9-1278-456e-ac95-51f5bdbb9615Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer!
