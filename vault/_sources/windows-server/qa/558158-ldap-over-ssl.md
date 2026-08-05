---
title: "LDAP over SSL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/558158/ldap-over-ssl
question_id: 558158
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# LDAP over SSL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/558158/ldap-over-ssl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have configured LDAP over SSL in my AD Server. Using ldp I am able to connect successfully using port 636.  

Shall I need to configure in GPO for Client Computers to access LDAP which is configured over SSL or will connect to that server without any configuration  

Please advise

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-25*

Hi,  

LDAPS is primarily intended to support simple bind requests, so plain text passwords are encrypted when transmitted over the network. To use this functionality the application or service must be specifically written to support LDAPS, as it needs to request a SSL based connection.  Typically security and network devices use simple binds when LDAP\S is used.   

I don't believe there is any GPO settings that would force normal clients to use LDAPS as the default connections method.  

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-20*

Hello,    

Thank for reaching out.    

Yes, you may Enable GPO for LDAP sign-in to improve security.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/enable-ldap-signing-in-windows-server    

Thank you.
