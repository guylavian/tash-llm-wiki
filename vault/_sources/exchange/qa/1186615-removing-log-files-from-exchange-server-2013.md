---
title: "Removing log files from exchange server 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1186615/removing-log-files-from-exchange-server-2013
question_id: 1186615
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Removing log files from exchange server 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1186615/removing-log-files-from-exchange-server-2013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we have on-prem exchange 2013 (we are migrating to online soon).   Is it ok to remove the old log files from the c:\program files\microsoft\exchange server\v15\logging*CmdletInfra*

The CmdletInfra folder has logs from 2015**.** 

Thank you.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-03-05*

Yes, those are just diagnostic logs. Ok to remove.
