---
title: "In window server Active Directory, when you delete a user, where does his data get saved?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1187637/in-window-server-active-directory-when-you-delete
question_id: 1187637
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# In window server Active Directory, when you delete a user, where does his data get saved?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1187637/in-window-server-active-directory-when-you-delete (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Assume I have 400 users, and their all computer is domain joined and some of them are Remote users with VPN, now lets say, they are working on a big group project, and User1@example.com worked on so many files in his computer, but unfortunately he had to leave the position and I had to delete his account, so what will happen to all the files that he saved under his name and the domain added computer? How will I received his data and all the files that he created in computer? Where does his recorded get saved? in case he come back, what should I do?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-03-08*

@Dave Patrick where does the user file get saved? How do I keep their file and where? How to check their files from the active directory?  

By default, probably in the user's local machine my documents folder, but files could potentially be anywhere the user has write access. Not really an active directory related issue.    

-  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-03-08*

Hi @TechQ  

You can use another account member of local administrator group of this machine where the user data saved. Using a local administrators account let you access on all user profiles under C:\users\ even the user account is deleted from active directory.

Please don't forget to mark helpful answer as accepted

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-03-08*

Deleting an active directory user account wouldn't impact the user files. They'll still exist wherever they were saved.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
