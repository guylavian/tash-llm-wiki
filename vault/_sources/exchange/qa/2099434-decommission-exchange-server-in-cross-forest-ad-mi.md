---
title: "Decommission Exchange Server in Cross-Forest AD migration (mailboxes in Exchange Online)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2099434/decommission-exchange-server-in-cross-forest-ad-mi
question_id: 2099434
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
---
# Decommission Exchange Server in Cross-Forest AD migration (mailboxes in Exchange Online)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2099434/decommission-exchange-server-in-cross-forest-ad-mi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am currently working in an environment where we are migrating from Forest A to Forest B. The purpose of this migration is to transition to a new domain, and using the rendom tool is not an option.

Current Environment:

-  Mailboxes: Previously hosted on on-premises Exchange, but they have now been migrated to Exchange Online. We still have the on-premises Exchange server in place for mail flow.

-  Hybrid Configuration: The Hybrid Configuration Wizard (HCW) has been enabled, and we have Hybrid Azure AD Connect configured with hybrid enabled settings in the source environment.

-  Email Applications: Some applications are currently using the on-premises Exchange server to send emails.

Migration Plan:

-  AD Migration: We have finalized the timelines for the Active Directory migration and plan to use Active Directory Migration Tool (ADMT).

-  Azure AD Connect: After migrating all objects to the destination forest, we plan to disable AD synchronization in the source environment. Instead of importing the Azure AD Connect settings from the source, we are considering re-creating the configuration for the Azure AD Connect tool in the new forest, using mS-DS-ConsistencyGuid as the source anchor.

-  Mail Flow: Once we have established mail flow with the Exchange mailboxes authenticating against the new forest's Active Directory, we intend to decommission the source environment's Exchange server.

Request for Advice:

I would like to receive suggestions on how to effectively plan this migration to avoid any disruption in mail flow during the transition. Specifically, I am concerned about:

-  Ensuring continuous mail flow while migrating objects to the new forest.

-  Configuring Azure AD Connect in the new environment without causing synchronization issues.

-  Any additional considerations or best practices to follow during this migration process.

Thank you for your assistance!

## Answers

_No answers on this thread._
