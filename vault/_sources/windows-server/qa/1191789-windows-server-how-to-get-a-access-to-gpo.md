---
title: "Windows Server - How to get a access to GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1191789/windows-server-how-to-get-a-access-to-gpo
question_id: 1191789
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Windows Server - How to get a access to GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1191789/windows-server-how-to-get-a-access-to-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have rename my Domain name , after that  I have problem to join computers, 

Got the message: the network path was not found

The Policy in GPO: 

Default Domain Controllers Policy and Default Domain Policy is missing permission to edit 

Got Group Policy Error 

Failed top open the Group Policy Object. You might not have the appropriate rights

Details --> The system cannot find the path specified

Please Help me to fix that :-)

Sokoban

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-22*

I have solve that , find a website there is the default settings for Policies. So I typing that and now its working :-) 

Happy me :-)

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-03-21*

Renaming the domain name is a very risky move. Hopefully there's a backup in case it turns out fatal. I'd check the domain controller event logs for clues, also dcdiag, repamin tools may be helpful.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
