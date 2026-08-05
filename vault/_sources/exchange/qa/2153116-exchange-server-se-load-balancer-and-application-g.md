---
title: "Exchange Server SE - Load Balancer and Application Gateway Considerations"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2153116/exchange-server-se-load-balancer-and-application-g
question_id: 2153116
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Server SE - Load Balancer and Application Gateway Considerations

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2153116/exchange-server-se-load-balancer-and-application-g (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,

Do we have any special requirements for Exchange Server Subscription Edition in terms of load balancer (using legacy protocols such as IMAP and POP3) and application gateway (web traffic HTTP and HTTPS)? For example, is a WAF strictly required for Exchange Server SE?. it is disabled in our current settings due to latency and performance issues.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-01-31*

I dont think anyone can answer that. It wont be released until later this year and there is no official documentation yet..

However the deployment guidance will apparently be the same as 2019:

https://techcommunity.microsoft.com/blog/exchange/upgrading-your-organization-from-current-versions-to-exchange-server-se/4241305
