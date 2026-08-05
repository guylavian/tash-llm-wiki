---
title: "MVC Application hosted in DMZ Server throwing LDAP server is unavailable Exception for some users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1159767/mvc-application-hosted-in-dmz-server-throwing-ldap
question_id: 1159767
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# MVC Application hosted in DMZ Server throwing LDAP server is unavailable Exception for some users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1159767/mvc-application-hosted-in-dmz-server-throwing-ldap (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

MVC Application is throwing Server Un available exception for some users only while trying to authenticate in DMZ Server. It works for all users in local host under domain machine. Screenshot of error attached below.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-12*

Hi,

It seems a network flow issue. 
You should start by checking all required ports between DMZ server and domain controllers.
How to configure a firewall for Active Directory domains and trusts

Please don't forget to mark helpful reply as answer
