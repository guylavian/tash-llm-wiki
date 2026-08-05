---
title: "Domain Controller Access"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/646884/domain-controller-access
question_id: 646884
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller Access

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/646884/domain-controller-access (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All  

I am not a domain Admin, I have a terminal server and from the terminal server i want to connect to domain controller to check the services and event viewer logs. without domain admin access is it possible to connect to domain controller. is there any custom access which can fetch this information.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-12-01*

Is it possible to check the services remotely without domain admin rights.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-01*

You could add the user to the Event Log Readers group.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
