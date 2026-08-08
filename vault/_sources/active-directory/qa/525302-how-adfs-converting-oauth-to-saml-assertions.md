---
title: "How ADFS converting OAuth to SAML assertions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/525302/how-adfs-converting-oauth-to-saml-assertions
question_id: 525302
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# How ADFS converting OAuth to SAML assertions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/525302/how-adfs-converting-oauth-to-saml-assertions (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a Main Portal Application using OAUTH for Authentication, and another sub-application using SAML. We wanted the users to access the sub-application without requiring to re-login again by using ADFS. How ADFS converting OAuth to SAML assertions?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-08-30*

The authentication is handled by the IDP (here ADFS). If both applications are trusted by the same IDP, the user doesn't have to "re-authenticate" as it already has a valid session with the IDP (granted the conditions for that session to be valid are still met - authentication policy, force fresh authentication, access policies, session times... those can influence that behavior).    

I don't know how application this is for your scenario and your applications, but you could also request a OAuth token from a SAML token. This is described here: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-saml-bearer-assertion (but it might very well be out of scope for you).     

Now if that application is not known by the IDP, you can still do something custom in the app I suppose, but that's no longer a federation question.
