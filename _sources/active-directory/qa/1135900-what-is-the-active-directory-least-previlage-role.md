---
title: "What is the Active Directory least previlage role to list users in third party application from Active Directory?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1135900/what-is-the-active-directory-least-previlage-role
question_id: 1135900
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other", "windows-development-iis"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# What is the Active Directory least previlage role to list users in third party application from Active Directory?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1135900/what-is-the-active-directory-least-previlage-role (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We have one third party application which retrieves users information from AD. But every time we need to assign AD Domain Admin or Enterprise Admin role to retrieve users from AD to the application. But Domain Admin and Enterprise Admin account have very high privilege access to AD resources. So, we don't want to use these account for fetching users from AD.     

The user used in IIS pool need to assign Domain Admin or Enterprise Admin role to retrieve users from AD to our application. Due to security concern we don't want to use these roles for retrieving users from AD.    

Can anyone suggest us what is the least privilege AD users with read only access to just retrieve users from AD. That's all except we don't want that users to have.    

We have tried with Help Desk and Enterprise Read Only Domain Controller and Read Only Domain Controller. But with these account we could not fetch the users from AD

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-21*

As DSPatrick has said you will need to go back to the application vendor for a fix. This is typical of older applications, whereby the principal of least privileges was not followed, in favour of quick and easy development, give it DA rights that will fix it.    

Typically any normal AD user account can be used to read attributes from the AD. The issue will be that it uses the IIS pool and the account will need to be given additional permissions on the server to run.  Which hopefully the vendor can provide.    

Gary.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-12-20*

The third-party provider will be your best resource as to what's required for the application.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
