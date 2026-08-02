---
title: "Active Directory DNS _ldap SRV record owner is an Unknown account"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1614182/active-directory-dns-ldap-srv-record-owner-is-an-u
question_id: 1614182
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory DNS _ldap SRV record owner is an Unknown account

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1614182/active-directory-dns-ldap-srv-record-owner-is-an-u (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

While performing an audit of our AD DNS environment, we found numerous SRV records having an "Account Unknown" owner. For example, the _ldap SRV records shown below for our 4 domain controllers all show the same "Account Unknown" SID (5623) as the owner of the records. Does anybody know what the default owner should be for these records?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2024-03-11*

This should be set to SYSTEM. It's anyone's guess how this happened, but fortunately that's easy to fix 

hth

Marcin

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-03-12*

Thanks everyone, is it the case for all SRV records under _msdcs.domain.local zone that the owner should be SYSTEM? For example, there are additional _ldap records under _tcp.gc._msdcs.domain.local that also have the same "Unknown" account as owner:
