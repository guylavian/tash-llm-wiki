---
title: "does logs of domain controllers replicate between them?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/291129/does-logs-of-domain-controllers-replicate-between
question_id: 291129
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
---
# does logs of domain controllers replicate between them?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/291129/does-logs-of-domain-controllers-replicate-between (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I'm trying to centralize the logs of our two ADs, with nxlog, in a Graylog server.  

I noticed that some logs were duplicate, identical (same date, same message, same users, etc.) apart from the source. (for example, i got twice a security log about a failed logon from a user, from AD1 and AD2, with the same Timestamp)  

do all logs replicate, or only some, like "security" one?  

What should i send to graylog to monitoring our domain?  

PS: sry for bad english, it is not my natural language...

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-21*

Is there any option to enable Log replication ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-03*

Hi,  

after a few test, i conclude that logs were not replicated, it seems that client tried to logon on both DC at the same time, i think..  

Thank you all for your help ^^

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-26*

there shouldn't be a time lag between the two attempts?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-26*

Hi,  

Logs are not replicated (by default).  

Maybe you client on failed authentication tried to authenticate to another DC. That is why you see it "duplicated" altough it is actually not.  

Send logs from all DCs to your Graylog.
