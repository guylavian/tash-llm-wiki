---
title: "Exchange server rebooting \"to complete or continue the configuration of 'Microsoft Exchange Server'"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1132009/exchange-server-rebooting-to-complete-or-continue
question_id: 1132009
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange server rebooting "to complete or continue the configuration of 'Microsoft Exchange Server'

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1132009/exchange-server-rebooting-to-complete-or-continue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Automatic updates are turned off. No one was manually updating the server or configuring Exchange at 0230 this morning. This is concerning both from an operational standpoint (we need to know when the server is restarting to manage user expectations) and a security standpoint (if I can't explain it then it's suspicious). There is nothing else in the Event logs to explain this. Can anyone offer a possible explanation or what else I can look at to try and figure this out? Exchange Server 2016 running on Windows Server 2016.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-16*

Check the managed availability logs     

https://techcommunity.microsoft.com/t5/exchange-team-blog/responding-to-managed-availability/ba-p/589196
