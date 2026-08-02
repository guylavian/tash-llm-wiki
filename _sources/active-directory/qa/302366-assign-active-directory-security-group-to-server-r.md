---
title: "Assign active directory security group to server role"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/302366/assign-active-directory-security-group-to-server-r
question_id: 302366
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["sql-server-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Assign active directory security group to server role

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/302366/assign-active-directory-security-group-to-server-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Guys,  

I'm trying to assign Active Directory Security Group as a member in a server role that i created.  

but when i'm open my Object types, i don't have groups option available, only Logins and Server roles.  

maybe the solution is to create login that is base on active directory security group, but i tried to find how to do it and failed.  

Anyone have a solution?  

Thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-07*

```
CREATE LOGIN [DOMAIN\GROUP] FROM WINDOWS
ALTER SERVER ROLE MyServerRole ADD MEMBER [DOMAIN\GROUP]
```
