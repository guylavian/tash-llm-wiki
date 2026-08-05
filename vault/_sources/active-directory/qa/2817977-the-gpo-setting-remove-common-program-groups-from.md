---
title: "The GPO setting \"Remove common program groups from START MENU\" is also removing icons from Public\\Desktop\\ on Windows 10 Pro 64bit build 1803"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2817977/the-gpo-setting-remove-common-program-groups-from
question_id: 2817977
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 50
qa_tags: []
---
# The GPO setting "Remove common program groups from START MENU" is also removing icons from Public\Desktop\ on Windows 10 Pro 64bit build 1803

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2817977/the-gpo-setting-remove-common-program-groups-from (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I believe that this was a bug introduced with Windows 10 Pro 64bit build 1803, but it may have been just before it and I just didn't catch it previously...

Basically, I first used this setting for our Windows 7 systems to prohibit user from jumping to the All Users Programs directory, and then navigating the file structure. However, in Windows 10, that functionality was prohibited by simply removing the All
 Programs list from non-administrative users. However, this option now ALSO removes the All Users' Desktop icons (from C:\Users\Public\Desktop) as well...which it shouldn't be doing as the setting label clearly states "START MENU".

I realize that these desktop icons are still under the classification of ALL USERS' Programs, but they are NOT directly linked to the start menu, but rather are shortcut from the working directory.

Can this be resolved?

Moved from: Windows /Windows 10 /Desktop, Start,
 & personalization /Desktop

## Answer (community) — community member

*upvotes: 0 · updated: 2018-06-27*

Hi, 

Your Windows 10 question is more complex than what is typically answered in the Microsoft Answers forums. It is better suited for the IT Pro
 audience on TechNet. Please post your question in the TechNet Windows 10 forum.

Feel free to post back should you have further concerns.
