---
title: "Migration from OpenLdap server to Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1302615/migration-from-openldap-server-to-active-directory
question_id: 1302615
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Migration from OpenLdap server to Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1302615/migration-from-openldap-server-to-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a business need where we have to migrate around 100 users from OpenLdap server to Active Directory. Basically, we are migrating from Openldap to AD.

Can any one please suggest us so we can migrate user data smoothly/effecttively with the existing passwords so users would not have login issues.

TIA

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-06-12*

As far as I know, ADMT can be used to migrate OpenLDAP to Active Directory. Locally stored user profiles on workstations can be migrated as well, presenting almost no disruption to the user. 

A similar thread has been discussed: 

https://social.technet.microsoft.com/Forums/windowsserver/en-US/061b6deb-5eb7-4db8-a0a8-5ac618799e5b/migration-openldap-to-ad?forum=winserverDS

 Please take a look at other links/threads mentioned in it.
