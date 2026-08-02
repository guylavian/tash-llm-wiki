---
title: "procedure (step-wise) of making  a Non-windows LDAP client successfully interwork with Microsoft AD over LDAP protocol"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1508834/procedure-step-wise-of-making-a-non-windows-ldap-c
question_id: 1508834
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# procedure (step-wise) of making  a Non-windows LDAP client successfully interwork with Microsoft AD over LDAP protocol

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1508834/procedure-step-wise-of-making-a-non-windows-ldap-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

What is the procedure (stepwise) of making a non-windows LDAP client successfully interwork with Microsoft AD over LDAP protocol.  The client is capable of interworking with an LDAP Server.
In other words, can this client be adapted, or can Microsoft AD Server be adapted to make them interwork successfully for SSO and IAM?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-01-23*

Microsoft Active Directory works well with non-Windows LDAP clients. There are a few gotchas and oddities but little that is insurmountable. For a good single/seamless-sign-on experience you would be best off with something SAML or OIDC capable (Microsoft EntraID or ADFS), but for authentication/search LDAP is fine. If you haven't worked with non-MS LDAP much try the ldapsearch tool to get a feel for the client-side configuration (search bases, bind DNs, SSL/LDAPS, scopes etc.)
