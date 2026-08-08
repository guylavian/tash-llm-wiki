---
title: "Extend Active Directory Schema - Windows Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1091243/extend-active-directory-schema-windows-server-2019
question_id: 1091243
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Extend Active Directory Schema - Windows Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1091243/extend-active-directory-schema-windows-server-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I need to extend my AD Schema on Windows Server 2019.    

I need to add a new attribute for users.    

How do it correctly?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-19*

Hi @drClays       

The screenshots look ok, so not sure why it's not working.  Have a look at this article on how to check if the new aux is shown in structure view and new attribute listed -   https://nettools.net/schema-class-browser/     

    

Just one point, as there is only one attribute in your aux class, is the aux class required and maybe just add the attribute to the user class.    

Gary.
