---
title: "Migrating from local server to exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/135087/migrating-from-local-server-to-exchange-online
question_id: 135087
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Migrating from local server to exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/135087/migrating-from-local-server-to-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

We recently migrated users from local server to exchange online.    

And after that one user can't connect to Outlook and Team after migrating.    

    

This only one error that i founded in MS teams logs.    

I tried to switch network adapter offline and than online, it's fixed the problem but after some time user can't connect to the outlook again.    

user in outlook are showing "Need Password" and they can't connect, after some time they can connect.    

Event viewer no showing anything..    

When i can't connect to outlook on computer i can connect using OWA.    

Thinking of adding  -  [HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Common\Identity] and "DisableADALatopWAMOverride"=dword:00000001

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-09*

Set remote routing address to <tenant>.mail.onmicrosoft.com from email address section of ECP
