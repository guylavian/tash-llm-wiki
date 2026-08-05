---
title: "rest api for exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1664462/rest-api-for-exchange-online
question_id: 1664462
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-office-exchange-server-development", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# rest api for exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1664462/rest-api-for-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I know there is rest API support to control your outlook/mail. But I need to know if there is any API reference for Exchange Online settings. For example, in powershell we have cmdlets like Get-TransportRule, Get-MalwareFilterPolicy, Get-OrganizationConfig is there any similar API reference (Graph API or any other) for me to exploit those in Java or in any other language.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 2 · updated: 2024-05-09*

There isn't, at least not a public one. The workaround you can use is to "proxy" the cmdlets via the /InvokeCommand endpoint, which works akin to any RESTful API. Take a look at the second part of this article for detailed instructions: https://www.michev.info/blog/post/3883/exchange-online-powershell-module-gets-rid-of-the-winrm-dependence
