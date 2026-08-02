---
title: "Enabling /adfs/services/trust/13/windowstransport endpoint on ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/331956/enabling-adfs-services-trust-13-windowstransport-e
question_id: 331956
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Enabling /adfs/services/trust/13/windowstransport endpoint on ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/331956/enabling-adfs-services-trust-13-windowstransport-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I will be rolling out Hybrid Azure AD Join for Federated domains and one of the requirements is to enable the  internal endpoint, /adfs/services/trust/13/windowstransport. Currently that is disabled in my production environment. I have been trying to research what the affects are if I enable this internally and disable on the Proxy. I understand this is a requirement for Hybrid Azure AD JOin, but want to make sure I don't break anything when I enable it. Thoughts?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-04-03*

You can't break things by enabling it.   

You can break things by disabling it later on... Once you actually started using it.  

It should be disabled and remain disabled on the proxies.
