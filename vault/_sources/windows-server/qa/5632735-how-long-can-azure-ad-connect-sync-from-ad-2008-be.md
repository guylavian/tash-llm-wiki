---
title: "How Long Can Azure AD Connect Sync from AD 2008 Before Full M365 Cutover?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5632735/how-long-can-azure-ad-connect-sync-from-ad-2008-be
question_id: 5632735
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# How Long Can Azure AD Connect Sync from AD 2008 Before Full M365 Cutover?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5632735/how-long-can-azure-ad-connect-sync-from-ad-2008-be (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm currently running Exchange 2010 in a hybrid configuration with Microsoft 365. I'm using Azure AD Connect to sync users from Active Directory 2008. My question is: how long can I continue using Azure AD Connectto sync users to the cloud? I need to prepare for a complete cutoff from on-premises infrastructure and transition to using Microsoft 365 only.

I'm concerned about compatibility issues with AD 2008 and Azure AD Connect?

## Answer (community) — community member

*upvotes: 0 · updated: 2025-11-23*

Azure AD Connect V1 has been retired as of August 31, 2022, and is no longer supported. If you are using Azure AD Connect to sync users from Active Directory 2008, you need to upgrade to Microsoft Entra Connect V2 immediately to ensure continued functionality and support.

As of October 1, 2023, Microsoft Entra cloud services stopped accepting connections from Azure AD Connect V1 servers, meaning that if you are still using Azure AD Connect V1, you must take action immediately to avoid disruptions in user synchronization.

In terms of compatibility, using Active Directory 2008 with Azure AD Connect V1 is no longer viable, and you should consider migrating to a supported version to facilitate a smooth transition to Microsoft 365 only.

To prepare for a complete cutover from on-premises infrastructure, you should look into upgrading to Microsoft Entra Connect V2 or consider moving to Microsoft Entra Cloud Sync, which is designed for modern cloud environments.
