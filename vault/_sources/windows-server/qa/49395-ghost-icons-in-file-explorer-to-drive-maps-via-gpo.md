---
title: "Ghost icons in File explorer to drive maps via GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/49395/ghost-icons-in-file-explorer-to-drive-maps-via-gpo
question_id: 49395
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Ghost icons in File explorer to drive maps via GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/49395/ghost-icons-in-file-explorer-to-drive-maps-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

While testing the effect of different users in an Server 2019 RDS, drive map icons remain after a user is demoted.    

Scenario    

A test user was promoted to an equivalent of an exec team member, by being made a member of the equivalent domain groups.  That user then receives extra drives mapped at login due to the GP targeting with the followng criteria "if a user is a member of the Exec team, map Fin Exec, Exec and GM shares etc"    

I removed the user from the Executive groups, logged off, but ghost "icons" remain in File Explorer.  How do I address this or have I done something wrong?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-24*

Hi  

Which action was set on the GPP drive map configuration?  

Was the "reconnect" option active in the GPP drive map configuration?
