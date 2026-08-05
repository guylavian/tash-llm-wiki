---
title: "Export list of OU where \"Chrome\" GPO is not applied"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/768545/export-list-of-ou-where-chrome-gpo-is-not-applied
question_id: 768545
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Export list of OU where "Chrome" GPO is not applied

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/768545/export-list-of-ou-where-chrome-gpo-is-not-applied (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have to fetch a list of GPOs where "Chrome" GPO is not applied. We have many OUs so the manual task is not possible. We have two different regions APAC, and America but every region's OU will have its region code (region name+UniqueID) in its attribute, region code is the same (APAC) for a region but UID is unique for example APAC OUs will have an attribute APAC001,APAC002, APAC003 and so be America, example AMERICA001, AMERICA002. Thank you in advance for your help.  

This attribute name is "region"

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-11*

How about Get-GPInheritance?  get-gpinheritance    

Build a list of OU's to check with Get-OrganizationalUnit and then check the result of the Get-GPInheritance for each of them. When you don't find "Chrome" in the list you found an OU where the GPO isn't applied.
