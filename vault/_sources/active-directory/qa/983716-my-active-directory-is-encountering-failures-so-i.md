---
title: "My Active Directory is encountering failures so I cannot move computers and users to OUs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/983716/my-active-directory-is-encountering-failures-so-i
question_id: 983716
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# My Active Directory is encountering failures so I cannot move computers and users to OUs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/983716/my-active-directory-is-encountering-failures-so-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When moving computers and users to an OU in AD I cannot do this and keep getting the error 'Windows cannot move object "objectname" because: The directory service encountered an unknown failure.' We can create new folders, users, add new computers, but we cannot move users and computers into OUs. AD is running on Windows Server 2019 Standard. How do I resolve this issue?

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-08-31*

Hi,    

Can you check if the Object properties if they are not protected from accidental deletion?    

    

Microsoft treats a move as a delete in AD so even though you’re not technically deleting the OU, the operation of moving it implies a delete of the object in the process and that is why you can’t move it even though your user account may have full control over that particular OU/Object in AD    

=    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-26*

I would also suggest running a semantic file check on the AD as well     

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/complete-semantic-database-analysis-ad-db    

Gary.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-08-26*

Sounds like something is broken. I'd check the system, DFS Replication event logs, and dcdiag for clues.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
