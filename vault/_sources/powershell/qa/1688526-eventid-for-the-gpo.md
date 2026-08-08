---
title: "EventID for the GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1688526/eventid-for-the-gpo
question_id: 1688526
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# EventID for the GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1688526/eventid-for-the-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have enabled the GPO (Turn on PowerShell Transcription):

Computer Configuration-Administrative Templates-Windows Components-Windows PowerShell.

Turn on PowerShell Transcription: Enabled. Should I see any other Event ID besides 4103 in Event Viewer with this GPO?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-05-29*

As per this article, Event ID 4103 – Module logging, should i consider 800 or 4103

https://www.iblue.team/incident-response-1/logging-powershell-activities

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-05-29*

with this gpo enabled what event ids will we see?
