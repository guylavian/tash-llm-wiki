---
title: "GPO Option missing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2179746/gpo-option-missing
question_id: 2179746
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO Option missing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2179746/gpo-option-missing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I cannot find the GPO option Computer Configuration > Administrative Templates > Windows Components > Smart Card Policy: Allow cached logon for smart card users

Looking to apply this so users can log onto their system when domain is unavailable

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-20*

Hello,

The Group Policy Object (GPO) setting "Allow cached logon for smart card users" is not available in the default Group Policy Editor (GPE) because it is specific to smart card logon behavior. However, you can achieve similar functionality by configuring related settings or using alternative methods.

The setting you're looking for might not exist in newer versions of Windows or might have been moved. To confirm:

Open the Group Policy Management Editor. Navigate to: Computer Configuration > Administrative Templates > Windows Components > Smart Card. Look for any related settings, such as "Interactive logon: Number of previous logons to cache".

If the specific setting is unavailable, you can configure cached logons for all users, including smart card users, by adjusting the following GPO setting:

Navigate to: Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options.

Locate the policy: Interactive logon: Number of previous logons to cache (in case domain controller is not available)

Set this to a value greater than 0 (e.g., 10). This allows users to log in with cached credentials when the domain is unavailable.

Note:

Ensure that the domain controllers are reachable during normal operations so that credentials can be cached.

Caching credentials, including smart card logons, can pose a security risk. Evaluate the trade-offs before enabling this feature.

Ensure the GPO is applied to the correct Organizational Unit (OU) and that the systems have successfully updated their Group Policy (run gpupdate /force on the target systems).

I hope the information above is helpful.

Best regards

Zunhui

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
