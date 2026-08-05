---
title: "Transport rule and group membership update delays"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1301865/transport-rule-and-group-membership-update-delays
question_id: 1301865
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Transport rule and group membership update delays

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1301865/transport-rule-and-group-membership-update-delays (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!.

We are exchange 2013 CU 23 and the transport rule applies based on group membership. We are to wait for nearly hours for the group membership. Please update the maximum time for the group membership and by when transport rule starts to apply after a change in the group membership. 

Only if we restart the MS exchange transport service group membership changes take immediate effect.

Thanks

Priya

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-06-08*

You can adjust the cache time by following this.

Backup the config file before making any changes.

https://learn.microsoft.com/en-us/previous-versions/office/exchange-server-operations-management-pack-2010/ff360556(v=exchg.140)?redirectedfrom=MSDN
