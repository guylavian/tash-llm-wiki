---
title: "ADFS and 3rd Party Identity Provider: Double Username issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/305877/adfs-and-3rd-party-identity-provider-double-userna
question_id: 305877
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS and 3rd Party Identity Provider: Double Username issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/305877/adfs-and-3rd-party-identity-provider-double-userna (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I'm trying to integrate a 3rd party IdP which also acts as 2MFA with Azure AD and ADFS: Azure AD doesn't yet support it so in the meanwhile, I've configured ADFS to use it as IdP provider.  

Login auth flow sample:  

Azure AD -> ADFS -> 3rd party IdP  

Everything works except that when a user provide his creds to Azure AD and that he is redirected to ADFS, when he lands on the IdP web page, he has to provide again the username.   

Any thought ?

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-01-22*

Why do you need to federate with ADFS at all? Just go directly to the other IDP. But if we have workshops to help move off ADFS https://techcommunity.microsoft.com/t5/community-events-list/microsoft-workshops-how-to-successfully-migrate-away-from-ad-fs/m-p/3668480 & https://www.microsoft.com/en-us/security/business/identity-access/upgrade-adfs
