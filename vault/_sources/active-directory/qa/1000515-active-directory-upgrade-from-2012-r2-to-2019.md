---
title: "Active Directory upgrade from 2012 R2 to 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1000515/active-directory-upgrade-from-2012-r2-to-2019
question_id: 1000515
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
---
# Active Directory upgrade from 2012 R2 to 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1000515/active-directory-upgrade-from-2012-r2-to-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Please be informed that we are handling legacy applications developed using Visual Basic 6.0 and Visual Studio 2008 (VB.NET etc.) and will send email using MAPI.    

We need to maintain the older Operating system (Windows XP and Windows 7) in our development environment due to the technical challenges of installing the 16Bit development tools (such as VB6.0 etc.).    

The Infra windows team is planning to upgrade the active directory version to 2019 which includes domain controllers in On-prem and AWS cloud.    

We suspect the Legacy Applications and Development Server environments with Older Operating system might be impacted by the active directory upgrade to 2019 version and may affect the users in production.    

But we cannot upgrade the older Operating system (Windows XP and Windows 7) in our development environment.    

Kindly advise and clarify to resolve the issue smoothly.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-16*

Hello    

Thank you for your question and reaching out. I can understand you are  having query  related  to AD upgrade from 2012 R2 to 2019.    

Normally it should not be issue if only AD is upgraded to 2019 as it should be backward compatible.    

Is your VB Application is using any specific feature or Attribute of AD  ?    

--------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-11*

I’m checking how the things are going on about this issue?    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-09*

You are welcome Ganapathi.    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-09*

Hi,    

I will suggest you to setup a isolated network, Dev& Test or Preprod and replicate all the applications and clients for testing the upgrade process. As you are in a better position to carry out the testing the application functionality and check the results.    

Also you can review the functional levels of the DC and features of the DC - active-directory-functional-levels    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
