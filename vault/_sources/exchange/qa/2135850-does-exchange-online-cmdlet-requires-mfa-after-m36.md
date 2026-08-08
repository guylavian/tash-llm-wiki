---
title: "Does Exchange online cmdlet requires MFA after m365 phase 2 MFA enforcement"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2135850/does-exchange-online-cmdlet-requires-mfa-after-m36
question_id: 2135850
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-microsoft-authenticator", "office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Does Exchange online cmdlet requires MFA after m365 phase 2 MFA enforcement

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2135850/does-exchange-online-cmdlet-requires-mfa-after-m36 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange online is not mentioned in the MFA enforcement page. when MFA will be enforced for exchange online.

reference link : https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2024-12-23*

At some point Microsoft may enforce MFA on any Exchange workload, but for now, they are focusing on "management" workloads first.

You can of course, require MFA now for Microsoft 365 workloads with Conditional Access or in general if using security Defaults or per user MFA

You can also enforce MFA on admin portals:

https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-cloud-apps#microsoft-admin-portals

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-24*

Hi, @soorya raj  

There is currently no official documentation of a specific time for the implementation of MFA for Exchange Online. 

Starting 3 February 2025, Microsoft will begin requiring MFA for all users accessing the M365 admin centre. This requirement will be rolled out in phases at the tenant level. 

There is no impact to Exchange Online end users at this time. 

You can also follow Andy's advice to enforce MFA on the admin portal.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
