---
title: "Non-active directory users need authentication/SSO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1600547/non-active-directory-users-need-authentication-sso
question_id: 1600547
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-rbac", "microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Non-active directory users need authentication/SSO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1600547/non-active-directory-users-need-authentication-sso (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi - Im looking for a license type or service provided that satisfies the ability to have non-active directory employees (ie: seasonal or temp employees) logging into an application via SSO. is there a way to do this so that you do not have a full O365 license per user (they don't have an email), and you can provision the account based off role type. 
Thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-02-28*

There is no license requirement for users ( Members or guests) to create or logon to a SSO application. The application itself may have license requirements, but the access itself is not licensed:
https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal-setup-sso#prerequisites
When you say "non-active directory" , I assume you mean guests in Azure? 
As far as the lack of an email, an email is not required for SSO. Your app can use UserPrincipalName or any ohter unique value to auth and if it requires an email address , you could add the SAML claim in the Azure app to set UPN to EMail as a workaround for example.
