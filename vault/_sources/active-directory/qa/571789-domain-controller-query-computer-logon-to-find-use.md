---
title: "Domain Controller Query Computer Logon to Find User"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/571789/domain-controller-query-computer-logon-to-find-use
question_id: 571789
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller Query Computer Logon to Find User

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/571789/domain-controller-query-computer-logon-to-find-use (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I'm looking for a way to query the domain controller to find out who has been logging into a specific computer. I have 2 computers that we're trying to find out who is logging into them.  

I'm looking at XML Queries but all I'm finding is the script to find a specific user's logon.  

Does someone have a script that can query a specific computer name's logon, so then I can find the user logging into it?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-30*

Hello @nicholas conger       

The topic has been lengthy discussed and provided different answers in this post:    

https://learn.microsoft.com/en-us/answers/questions/159086/getting-list-of-users-who-logged-in-within-5-days.html    

Hope this helps with your query,    

---------------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-30*

That works GREAT !!! I just have to wait until the computer is logged in on our domain and that would work.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-30*

This tool should sort it.    

https://learn.microsoft.com/en-us/sysinternals/downloads/psloggedon    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
