---
title: "Exchange Split Brain - How to restore items?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1627805/exchange-split-brain-how-to-restore-items
question_id: 1627805
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Split Brain - How to restore items?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1627805/exchange-split-brain-how-to-restore-items (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!

Tell me please what the correct actions should be in case of a split-brain situation in Exchange?

I have never encountered this, however after performing some actions in the test environment, I was able to get this situation. As a result, the database took a long time to initialize and then switched to the “Healthy” state, after which the letters never appeared.

I suppose there is some way to restore it? For example, using transaction logs or shutting down a server with older data, creating a clone of it and restoring data from it?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-25*

Hi @Step to IT,

Please follow this link to enable DAC mode:

```
Set-DatabaseAvailabilityGroup -Identity DAG2 -DatacenterActivationMode DagOnly
```

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
