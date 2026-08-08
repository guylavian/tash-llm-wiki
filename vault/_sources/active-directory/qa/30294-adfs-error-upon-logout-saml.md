---
title: "ADFS Error upon logout (SAML)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/30294/adfs-error-upon-logout-saml
question_id: 30294
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Error upon logout (SAML)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/30294/adfs-error-upon-logout-saml (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there any difference between what ADFS and Azure support with respect to logout requests (is there a configuration on the ADFS side that needs to be set, does the SAML request need to include/exclude/get signed/etc. when sending to ADFS vs. Azure)?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-05-29*

I believe that the logout endpoints are configured correctly but I don't think this is it because I am not seeing those endpoints (the logout ones) being called even.  

And from the ADFS logs, we can observe the following error:  

The verification of the SAML message signature failed.  

Message issuer: XXXXX  

Exception details:  

MSIS7084: SAML logout request and logout response messages must be signed when using SAML HTTP Redirect or HTTP POST binding.  

This request failed.  

Does this help?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-05-29*

There is generally a configuration to set on the Relying Party Trust in ADFS. A log-out endpoint has to be provided.
