---
title: "configuration ADFS shows :Time out has expired and the operation has not been completed."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/879284/configuration-adfs-shows-time-out-has-expired-and
question_id: 879284
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# configuration ADFS shows :Time out has expired and the operation has not been completed.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/879284/configuration-adfs-shows-time-out-has-expired-and (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question



## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-07*

Hi SilverLu-4233,  

There are many potential reasons for this error, it may be a permission issue for the user who is running the service or the same port has been used for other services, SPN Issue, endpoint protection etc. Try checking the event log and if you can't figure out the reason paste the event viewer error here and hopefully we can figure out the issue.  

--If the reply is helpful, please Upvote and Accept as answer--
