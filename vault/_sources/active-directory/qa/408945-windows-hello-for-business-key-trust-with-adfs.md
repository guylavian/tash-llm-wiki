---
title: "Windows Hello for Business Key Trust with ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/408945/windows-hello-for-business-key-trust-with-adfs
question_id: 408945
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Windows Hello for Business Key Trust with ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/408945/windows-hello-for-business-key-trust-with-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm looking to implement windows hello for business key trust modern managed topology with an ADFS server so mitigate the AAD connect sync back to on premise to map the public key to the AD user attribute. Do you know what configurations in ADFS are required for this configuration?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-05-25*

Assuming that the users exist in Azure AD. In that case, ADFS would be required only if your Azure AD was federated with ADFS.  

If you Azure AD domain is managed, then you don't need ADFS for Key Trust.
