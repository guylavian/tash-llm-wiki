---
title: "how to check security patches exchange (KB5000871)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/297967/how-to-check-security-patches-exchange-kb5000871
question_id: 297967
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# how to check security patches exchange (KB5000871)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/297967/how-to-check-security-patches-exchange-kb5000871 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

What command check security patch on exchnage server 2016 ? I patched KB5000871 on exchnage server need to double check.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-05*

wmic qfe list and get-hotfix cannot file KB5000871 becuase this patch apply on exchange not windows server.
