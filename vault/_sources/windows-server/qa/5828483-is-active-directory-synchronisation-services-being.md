---
title: "Is Active Directory Synchronisation Services being retired in 2026?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5828483/is-active-directory-synchronisation-services-being
question_id: 5828483
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# Is Active Directory Synchronisation Services being retired in 2026?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5828483/is-active-directory-synchronisation-services-being (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is Active Directory Synchronisation Services being retired in 2026?

What are the alternatives?

## Answer (community) — community member

*upvotes: 1 · updated: 2026-03-19*

Active Directory Synchronization Services (the legacy DirSync tool) is already deprecated, and older versions are blocked from syncing to Microsoft Entra ID. The key 2026-related change is a hardening update for Microsoft Entra Connect Sync, not a retirement of directory synchronization itself.

From the provided information:

-  Deprecated DirSync / legacy sync tool

-  If synchronization is still running on the old Microsoft Online Services Directory Synchronization tool (DirSync), that tool is deprecated and no longer accepted by Microsoft Entra ID.

-  When this deprecated tool is used, synchronization stops and events like ID 0 or 109 are logged with the message that the version is no longer supported and must be upgraded.

-  2026 hardening requirement for Microsoft Entra Connect Sync

-  Microsoft has introduced a dedicated first‑party application called “Microsoft Entra AD Synchronization Service” (service principal ID `6bf85cfa-ac8a-4be5-b5de-425a0d0dc016`) used by Microsoft Entra Connect Sync.

-  All customers must upgrade Microsoft Entra Connect to version 2.5.79.0 or later by September 30, 2026.

-  If not upgraded by that date, all synchronization services in Microsoft Entra Connect Sync will fail until upgraded to at least the required version.

-  This is a security hardening and support requirement, not a retirement of synchronization as a capability.

-  Alternatives / required path forward

-  For environments still using the old DirSync tool: the supported alternative is Microsoft Entra Connect. The solution is to upgrade from DirSync to Microsoft Entra Connect on a supported 64‑bit Windows Server.

-  For environments already using Microsoft Entra Connect: the path forward is to upgrade to version 2.5.79.0 or later before September 30, 2026 so synchronization continues to work after the hardening change.

In summary, directory synchronization itself is not being retired in 2026, but:

-  Legacy DirSync is already deprecated and blocked.

-  Microsoft Entra Connect Sync must be upgraded to at least 2.5.79.0 by September 30, 2026, or synchronization will fail until upgraded.

References:

-  Hardening update to Microsoft Entra Connect Sync

-  Microsoft Online Services Directory Synchronization tool stops syncing objects and triggers a Directory Synchronization error

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-03-19*

Hi Adrian,

No - Active Directory synchronization is not being fully retired in 2026, but older Microsoft Entra Connect Sync versions will stop working after September 30, 2026 unless they are upgraded to version 2.5.79.0 or later due to a Microsoft backend security change. So this is an upgrade deadline, not a complete retirement of directory sync. For the long term, Microsoft’s preferred alternative is Microsoft Entra Cloud Sync, and Microsoft states that Entra Connect Sync will eventually be retired once Cloud Sync reaches full feature parity, but no final retirement date has been announced yet.

If you are still using legacy Azure AD Connect 1.x, that version was already retired earlier and should already be replaced. 

Best practice today is: upgrade Entra Connect Sync to 2.5.79.0+ now, and start evaluating Entra Cloud Sync for future migration.

Harry.
