---
title: "ADFS problems"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/66239/adfs-problems
question_id: 66239
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS problems

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/66239/adfs-problems (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Support,     

I am did some test with ADFS integrated with O365 now,  the scenario is as low    

-  A tenant has ADFS deployed and everything working fine from intranet, no proxy deployed as just we are in a test.    

-  B tenant only has AD environment sync with B,  no ADFS deployed, then I referred to the link  https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-fed-single-adfs-multitenant-federation   to federate two Azure AD tenants with one ADFS server,   the issue is when the tenant B users tried to sign in office.com, they are redirect to A tenant ADFS login page, and when tried to login, it failed with error An error occured. Contact your Administrator for more informatuon. Reyling party: Microsoft Office 365 Indetity Platform."  17513-adfs-event-log.txt    

Does anyone know about this issue, and how to resolve it?    

Thanks

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-01-22*

Why do you need ADFS? We have workshops to help move off ADFS https://techcommunity.microsoft.com/t5/community-events-list/microsoft-workshops-how-to-successfully-migrate-away-from-ad-fs/m-p/3668480 & https://www.microsoft.com/en-us/security/business/identity-access/upgrade-adfs
