---
title: "Clone Active Directory users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1185565/clone-active-directory-users
question_id: 1185565
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Clone Active Directory users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1185565/clone-active-directory-users (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have an AD for the developers, that is identical to the production AD.  

Is it possible to export a container with users from production to dev, but export the users password also?  

I need the same users on both AD, but they can´t connect between them.  

Thanks  

Carlos

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-03-01*

but export the users password also?  

Sorry, but this is not possible to do.  You can use PowerShell to export the users.  

https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps  

-  

 --please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
