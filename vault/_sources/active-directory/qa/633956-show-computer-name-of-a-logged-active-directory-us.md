---
title: "Show computer name of a logged Active Directory user?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/633956/show-computer-name-of-a-logged-active-directory-us
question_id: 633956
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Show computer name of a logged Active Directory user?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/633956/show-computer-name-of-a-logged-active-directory-us (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.  

I want to know the name of the computer a user is currently using.  

Ex: My user is test_user and i am currently logged in computer_005  

How would i do if i wanted to discover the computer name test_user is using?  

Please, can someone help?  

Thanks in advance.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-22*

You can also look for the events 4768 on your domain controllers for that user. It will tell you all the machines (IP addresses) from which the user has entered its credentials. It will tell me more than just interactive logon though as a runas or a script for example could also generated those. But that could still be useful to spot where accounts are used in general.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-11-19*

This tool will do that.    

https://learn.microsoft.com/en-us/sysinternals/downloads/psloggedon    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
