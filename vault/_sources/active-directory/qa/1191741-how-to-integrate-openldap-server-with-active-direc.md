---
title: "How to integrate OpenLDAP server with Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1191741/how-to-integrate-openldap-server-with-active-direc
question_id: 1191741
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# How to integrate OpenLDAP server with Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1191741/how-to-integrate-openldap-server-with-active-direc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear All,

We have a project where we need to integrate existing OpenLDAP server with Active Directory for user authentication and authorization purposes. Can any one please help us to achieve this?

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-22*

Hello

Thank you for your question and reaching out. I can understand you are  having query\issues related  to Integration of OpenLDAP  with AD.

To deploy OpenLDAP server we followed following procedure

-  Create a pod with 389, 443 and 636 ports exposed

-  Create a OpenLDAP server container in above create pod

-  Create a OpenLDAP GUI container in same pod as server

4 )Update the dns entries to add OpenLDAP server entry

Reference :

https://learn.microsoft.com/en-us/answers/questions/880255/integration-of-open-ldap-server-with-active-direct

--If the reply is helpful, please Upvote and Accept as answer--
