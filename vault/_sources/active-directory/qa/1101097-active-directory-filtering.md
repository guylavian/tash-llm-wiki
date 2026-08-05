---
title: "Active directory filtering"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1101097/active-directory-filtering
question_id: 1101097
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
---
# Active directory filtering

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1101097/active-directory-filtering (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello ,     

How to select the users who have two different emails in the active directory?

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-11-23*

Hi,    

So are you looking for exporting users with email address attribute? Try this code `Get-ADUser -Filter * -Properties EmailAddress,DisplayName, samaccountname| select EmailAddress, DisplayName`    

Hope this helps.    

JS    

==    

Please Accept the answer if the information helped you. This will help us and others in the community as well.
