---
title: "jointure of active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/804374/jointure-of-active-directory
question_id: 804374
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# jointure of active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/804374/jointure-of-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

when doing a join of my client station and my active directory, I got this error message:  

The following error occurred while trying to join the domain "name.tp""  

"The network path was not found."

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-04-07*

I'd check the domain controller and problem member both have the static ip address of DC listed for DNS and no others such as router or public DNS.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
