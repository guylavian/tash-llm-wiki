---
title: "ADFS group memberships"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/934695/adfs-group-memberships
question_id: 934695
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS group memberships

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/934695/adfs-group-memberships (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,    

I am trying to lock down our environment by removing unneeded group memberships to ADFS. We use ADFS with the WID database. Can I remove the adfs service account from any of these groups?    

Administrators    

Domain Admins    

Enterprise Admins    

Enterprise Key Admins    

Schema Admins

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-07-25*

Yes. In your scenario (WID deployment) the service account only needs the following:    

-  Access to the DKM container in AD (given by default at install, so unless you have changed the service account of the farm you are good).    

-  Access to the private keys of the TLS certificate    

-  Privilege to generate security logs ("Generate security audits" in the User Right Assignment section of the security policy)    

So it can be a regular domain user (only a member of the Domain Users group) as long as the aforementioned requirement are met.
