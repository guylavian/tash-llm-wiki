---
title: "ADFS WIA for Intranet users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/366055/adfs-wia-for-intranet-users
question_id: 366055
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS WIA for Intranet users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/366055/adfs-wia-for-intranet-users (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have ADFS 2016 configured in our company. It is used as a Idp provider for many apps like CRM, SPAs, ASP.NET MVC, etc.  

ADFS auth method configuration enables the following:  

Extranet:  

-  Froms Auth  

-  Microsoft Password Auth  

Intranet:  

-  Froms Auth  

-  Windows Auth  

-  Microsoft Password Auth  

We encountered an issue when configuring OIDC authentication for some SPA apps. The intranet user are forced to use WIA auth and because of this we have 2 problems.  

-  Login. We have two domain directories - one for internal user and one for external users. Staff members login to their machines with internal account, they are also on the Intranet - and they are not able to login with external account even in incognito window. It keeps prompting for credentials and logs are recorded on the ADFS event viewer.   

-  Logout. Intranet users are unable to logout because they are immediately logged in again. Infinite loop even in incognito window.  

The above two problems are fixed if we disable windows auth but we cannot do this because there is CRM 1612 on premises configured with WSFederation.  

I will be glad if you have some answer how we can solve our problems with login and logout, suggestions are also appreciated.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-04-25*

I don't have a repro environment so my contrib will be somewhat limited. That said, signing out from an application that allows WIA to get in the first place, I am not sure what we are expecting in term of security...    

You could force the application to request Form Based Authentication in your request. You can use the amr_values query string.
