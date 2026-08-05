---
title: "Bypass ADFS SSO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/369665/bypass-adfs-sso
question_id: 369665
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Bypass ADFS SSO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/369665/bypass-adfs-sso (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello. Thank you for any help you can give.   

We have our on PremAD and our AzureAD synchronising via Azure AD Connect. We also use onPrem ADFS for SSO.   

We synchronise our OnPrem AD accounts and lets say they have the UPN of ******@domain1.com. We have a need for some accounts that have the @domain1 UPN to not be sent to our onPrem ADFS server and for them to just login in the same way you would if you used @domain1.onmicrosoft.com  

Is this possible.   

Thanks in advance

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-04-25*

By default, domains are either managed or federated. You configure this with the MSOL PowerShell module. When a domain is federated, the authentication will take place somewhere else than Azure AD, on a federation service of your choice (ie. ADFS). When a domain is managed, Azure AD will perform the authentication. On that case, either your enable PHS to authenticate users directly in the cloud or PTA to have users send their credentials to Azure AD but then an on-premises agent picks up the request and authenticate the users on-premises. In those last two cases, you can also enable Seamless Single Sign-On to maintain an SSO experience for domain joined machines.

That said, you can also configure the Staged Roll Out feature. This allow you to use a group to select users within a Federated domain to use PHS or PTA instead of ADFS. There is a documentation that explains how to use that transition feature: 

-  Migrate from federation to password hash synchronization for Azure Active Directory

-  Migrate from federation to pass-through authentication for Azure Active Directory

Looking at your scenario, that Staged Roll Out feature might be the way to go for you.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-04-23*

Hi,   

if you create (not sync) those accounts as "cloud only" accounts in Azure AD directly those will not be sent to ADFS.   

Regards  

Julian
