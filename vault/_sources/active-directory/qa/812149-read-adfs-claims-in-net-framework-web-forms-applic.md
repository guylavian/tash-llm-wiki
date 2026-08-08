---
title: "Read ADFS Claims in .net framework web forms application"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/812149/read-adfs-claims-in-net-framework-web-forms-applic
question_id: 812149
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-csharp", "microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Read ADFS Claims in .net framework web forms application

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/812149/read-adfs-claims-in-net-framework-web-forms-applic (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have successfully setup ad fs to redirect to .net framework web forms site upon successful login.  I have defined claims for this relying part trust.  How do I retrieve those claims in redirect page code behind?  

Thanks in advance

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-04-21*

Thanks for your help.  

Actually, I am looking for a more detailed exampled.  

To elaborate what I am looking for...  

I am attempting to conver an exisiting web forms application to use ad fs.  

I have successfully setup ad fs to redirect to .net framework web forms site upon successful login. I have defined claims for this relying part trust. How do I retrieve those claims in redirect page code behind?  

I was able to retrieve the claims only when changing the authentication mode from anonymous to windows. However, this, also, produces authentication windows authentication popups. I don't want the popups. I suppose what I am looking for, let me know if it wrong, 1) upon successful ad fs login, I am redirected to web forms application signin page which doesn't prompt user with login since it receives user identity and other claims from ad fs. 2) Retrieve claims and lookup permissions on backend db based on user identity and claims. 3) Create and maintain session. Step 2 and 3 are done by the web forms application currently. So, I am looking to retrieve claims in 2).  

Thanks again

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-04-14*

It depends what you use on your application. There are examples in the public documentation: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/development/ad-fs-openid-connect-oauth-concepts
