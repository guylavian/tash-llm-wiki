---
title: "Exchange 2016 transport service starts and stops"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1239984/exchange-2016-transport-service-starts-and-stops
question_id: 1239984
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 transport service starts and stops

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1239984/exchange-2016-transport-service-starts-and-stops (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016 transport service starts and stops with Event ID 7036
How to resolve this error

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-17*

Check whether the permissions were removed for the Network Service account on the HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExchangeServer\v15\Transport\ hives keys and all subkeys or not.
If yes, then Grant permissions to all keys and subkeys. The services will start running, and mail is flowing again.
