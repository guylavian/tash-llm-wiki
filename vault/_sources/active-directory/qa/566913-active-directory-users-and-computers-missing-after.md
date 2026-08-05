---
title: "Active Directory Users and Computers Missing after upgrade to Windows 10 Version 21H1 from version 1909"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/566913/active-directory-users-and-computers-missing-after
question_id: 566913
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory Users and Computers Missing after upgrade to Windows 10 Version 21H1 from version 1909

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/566913/active-directory-users-and-computers-missing-after (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have upgraded the Windows version from 1909 to version 21H1. After the restart, I found out that Active Directory was missing. How will I get it back?  

I am new to AD so asking how to install it.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-09-27*

Hi @Sule Oebao       

From the Start menu, select Settings > Apps.    

Click the hyperlink on the right side labeled Manage Optional Features and then click the button to Add feature.    

Select RSAT: Active Directory Domain Services and Lightweight Directory Tools.    

Click Install.    

When the installation completes, you will have a new menu item in the start menu called Windows Administrative Tools.    

-------------    

--If the reply is helpful, please Upvote and Accept as answer--
