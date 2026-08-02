---
title: "How can we Block the StickyNotes through GPO ? So that user won't be able to access this."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2145728/how-can-we-block-the-stickynotes-through-gpo-so-th
question_id: 2145728
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-identity-manager", "windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# How can we Block the StickyNotes through GPO ? So that user won't be able to access this.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2145728/how-can-we-block-the-stickynotes-through-gpo-so-th (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Need to Block the StickyNotes App on windows 10 Pro Client Machine from GPO from Window Server 2019.

I Tried the below mentioned steps, but didn't work.

Can any one help me out?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-13*

This link might be helpful.

There seems to be a configuration under Computer Configuration\ Administrative Templates\ Windows Components\ Tablet PC\ Accessories\

Prevents start of Sticky Notes.

https://gpsearch.azurewebsites.net/default.aspx?policyid=4892&ref=1
