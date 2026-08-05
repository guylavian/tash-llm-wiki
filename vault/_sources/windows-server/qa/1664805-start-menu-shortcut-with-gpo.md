---
title: "Start Menu Shortcut with GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1664805/start-menu-shortcut-with-gpo
question_id: 1664805
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Start Menu Shortcut with GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1664805/start-menu-shortcut-with-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello! 

Since the start menu layout (xml file) can no longer be exported from a reference computer and transferred to other Windows 11 PCs via GPO (Start Layout Setting under Policies => Administrative Templates => Start Menu and Taskbar), is there any other way that we can set the start menu layout like from Registry or file path? Thank you in advance for your positive supports!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-05-10*

Hi Aung,

You can still export and deploy the layout, only the procedure has changed (now exported to JSON) :

Here's the full details: https://learn.microsoft.com/windows/configuration/start/layout

Hope this helps,
