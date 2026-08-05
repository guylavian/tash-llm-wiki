---
title: "Active Directory development environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/846245/active-directory-development-environment
question_id: 846245
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-vs-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory development environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/846245/active-directory-development-environment (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have AD based on Windows 2012 Server and I need to development graphical user interface to clone user avoiding to use AD built-in feature.  I'll creare the new user according my customized criteria.   

I need to create 2nd tool to permit ONLY to reset passwords for domain users; this task has to be permitted to special delegated users whose can make this job but with no further privileges.  

What development environment I can use ? Suggestions ?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-17*

Hello MidnightSender,  

There are already many Open Source Active Directory User Management tools that you could modify based on your preferences. One of the most well known is Active Directory Accounts Manager in Github, that can be easily added into your IIS, and developed in PHP and JS  

Hope this helps with your query,  

--If the reply is helpful, please Upvote and Accept as answer--
