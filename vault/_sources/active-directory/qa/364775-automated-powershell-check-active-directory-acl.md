---
title: "Automated Powershell check Active Directory ACL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/364775/automated-powershell-check-active-directory-acl
question_id: 364775
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Automated Powershell check Active Directory ACL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/364775/automated-powershell-check-active-directory-acl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've got 48 System Accounts, 48 Domain Local groups and 48 Global groups.  

Every Domain Local group has Full Access rights on only one specific OU to create, modify and delete Users in that OU.  

I want to create a powershell script that checks if al groups still exist, that they still have the right permissions on the right OU, and if the right users are still member of the right group. Every time I run this script I want to have a response (in a file or mail) with the results if anything has changed in the ACL or not.  

How can I best do this?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-20*

Hi @MW   ,    

maybe this helps to start with:    

https://www.reddit.com/r/PowerShell/comments/9h8ib6/report_of_permissions_for_ad_organizational_units/    

One approach could be to query the OUs and OU ACLs and then work through the nested groups. Finally, determine the group membership of the users.    

If you post your script here it is easier to help.    

----------    

(If the reply was helpful please don't forget to upvote and/or accept as answer, thank you)    

Regards    

 Andreas Baumgarten
