---
title: "eventhib exchange on premise"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1376579/eventhib-exchange-on-premise
question_id: 1376579
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-event-hubs", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# eventhib exchange on premise

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1376579/eventhib-exchange-on-premise (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

does eventhub ingest exchange on premise logs?

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-09-26*

Hello @adminbnm  ,

thanks for visiting our moderated community forum.

Do you mean logs/logfiles living with the local network? 

The Azure EventHub lives in the Azure cloud. any service capable of reaching the endpoint can send data to it.

This can even be logic running on the local network, having a Shared access policy for authentication.

Here is an example.

If the response helped, do "Accept Answer". If it doesn't work, please let us know the progress. All community members with similar issues will benefit by doing so. Your contribution is highly appreciated.
