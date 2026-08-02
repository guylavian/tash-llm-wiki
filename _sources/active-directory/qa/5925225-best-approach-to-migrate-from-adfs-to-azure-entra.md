---
title: "Best Approach to Migrate from ADFS to Azure Entra ID with External MFA [DUO] Without User Disruption"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5925225/best-approach-to-migrate-from-adfs-to-azure-entra
question_id: 5925225
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Best Approach to Migrate from ADFS to Azure Entra ID with External MFA [DUO] Without User Disruption

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5925225/best-approach-to-migrate-from-adfs-to-azure-entra (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
Hi,

I am looking for guidance and best practices for migrating our authentication flow from ADFS to Microsoft Entra ID while continuing to use Duo MFA.

Current Authentication Flow
User → Entra ID → ADFS Server → Duo MFA → Approved

Original Target Architecture
User → Entra ID → Conditional Access Policy → Custom Control → Duo MFA → Approved

However, after implementing and testing this approach, we learned that Microsoft will stop allowing creation/editing of Custom Controls after September 30, 2026, and plans to retire the service completely in early 2027.

Additionally, Duo has communicated a similar timeline for its Azure Active Directory (Custom Control JSON Format) application and recommends moving to the newer External MFA integration.

What Has Already Been Configured
	1. Created the Azure Active Directory application in Duo (Custom Control-JSON based integration).
	2. Configured Duo application in Custom Control in Entra ID.
	3. Created and assigned a Conditional Access policy using the Custom Control in Entra ID.
	4. Added production users to the Conditional Access policy.
	5. Unexpectedly, all production users were forced to re-authenticate / got signed out when the CA policy was applied.
	6. Configured External MFA in Entra ID Authentication Methods using the same Duo application credentials that are currently used for Custom Control.
	7. We are hesitant to remove users from the existing CA policy because we are concerned it may trigger another token re-evaluation and cause another forced sign-out event.

Redesigned Target Architecture
Instead of continuing with Custom Controls, we are planning to move directly to External MFA:

User → Entra ID → Conditional Access Policy → External MFA → Duo MFA → Approved

Proposed Migration Plan
	1. Delete and recreate the External MFA configuration using Duo's newer External MFA application.
	2. Create a New Pilot group for testing.
	3. Create a new Conditional Access policy that requires External MFA instead of Custom Control.
	4. Add pilot users to the new CA policy and enable Staged Rollout to bypass ADFS.
	5. Validate authentication experience and MFA flow.
	6. Migrate users in batches until all users are moved from ADFS to Entra ID + External MFA.

Questions I've:
	1. When we previously added users to the Custom Control Conditional Access policy, all users were unexpectedly forced to re-authenticate. Is similar behavior expected when moving users to an External MFA-based CA policy?
	2. What is the recommended approach for transitioning users from the existing Custom Control CA policy to the new External MFA CA policy while minimizing user impact and avoiding mass sign-outs?
	3. Are there any known behaviors, token refresh requirements, session impacts, or Conditional Access considerations that we should be aware of during this migration?
	4. Is there a better migration strategy for moving from:
ADFS + Duo MFA
to
Entra ID + External MFA (Duo)
while minimizing downtime and user disruption?
	5. Has anyone performed a similar migration from Duo Custom Controls to Duo External MFA, and if so, what lessons learned or pitfalls should we be aware of?

Any guidance, recommendations, or Microsoft documentation references would be greatly appreciated.
```

## Answers

_No answers on this thread._
