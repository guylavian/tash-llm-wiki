---
title: "Exchange 2016, DAG, passiv Copy dirty shutdown"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1059029/exchange-2016-dag-passiv-copy-dirty-shutdown
question_id: 1059029
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016, DAG, passiv Copy dirty shutdown

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1059029/exchange-2016-dag-passiv-copy-dirty-shutdown (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi all,    

We test any desaster szenarios and see that passiv copies have dirty shutdown when we restore it from backup.     

We test also dismount aktive DB, suspend and remove passiv copy - passiv copy are dirty shutdown and can't use without eseutil and softrepair. It this per design?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-23*

Yes, that is expected. When you dismount a database gracefully and any uncommitted logs are replayed into the database, that is a clean shutdown.    

When you restore from a backup or attempt to mount a passive database that has either lagged copies or does not have all the required logs committed to the database, it is in a "dirty" state and the required logs need to be replayed into it either by the backup program or with eseutil
