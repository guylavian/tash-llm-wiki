---
title: "Active Directory problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/549634/active-directory-problem
question_id: 549634
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/549634/active-directory-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I have the following problem with the active directory, if an employee does not log on to the computer for about 2 weeks, then he cannot log on to the computer. The administrator must log in first, and then the user. As if after some time the computer becomes inactive. I suppose it needs to be changed somewhere in politics, but where?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-09-13*

Hi @Filip Gronostaj  ,    

Are you looking for GPO Policy solution, which helps to log out the computer if you are not logged in for 2 weeks.    

Please go through Link and help me understand, what kind of solution are you looking for    

https://www.isdecisions.com/blog/it-security/active-directory-user-logon-logoff-security/    

Thanks & Regards,    

Sarat chandra

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-09-13*

What happens when you try?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-14*

Hello FilipGronostaj,    

In order to troubleshoot Active Directory Replication errors. It is intended to provide Active Directory administrators with a method to diagnose replication failures and to determine where those failures are occurring.    

Do follow the below link to troubleshoot errors from the Active Directory Problem    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/common-active-directory-replication-errors    

 Hope this answers all your queries, if not please do repost back.     

If an Answer is helpful, please click "Accept Answer" and upvote it : )

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-14*

No no, the problem is when a regular user does not log in to this computer for 2 weeks, after returning he is not able to log in, because the domain is not available. Once the domain administrator logs on, all of this becomes active and the normal user can log back on to that computer.
