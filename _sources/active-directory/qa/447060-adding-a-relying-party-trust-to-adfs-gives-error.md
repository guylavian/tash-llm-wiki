---
title: "Adding a Relying Party Trust to ADFS gives error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/447060/adding-a-relying-party-trust-to-adfs-gives-error
question_id: 447060
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Adding a Relying Party Trust to ADFS gives error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/447060/adding-a-relying-party-trust-to-adfs-gives-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are getting attached error while adding a relying party trust to ADFS. This needed to be done as our CRM Test server had to be repaired since it was not taking in new patches. We reinstalled CRM and were trying to reconfigure IFD when we are running into this issue

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-06-23*

-  Try to open the URL with Internet Explorer on the same machine. Does it work?    

-  Try to open the URL with PowerShell on the same machine (Invoke-WebRequest -Uri <URL>). Does it work?    

If 1 is YES and 2 is NO, we just have a .Net TLS incompatibility issue. And you'll find the fix here: https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/security/enable-tls-1-2-client#bkmk_net (the SchUseStrongCrypto registry value).
