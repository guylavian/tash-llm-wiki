---
title: "dsa.msc - can it use LDAPS port 636?  How?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1180330/dsa-msc-can-it-use-ldaps-port-636-how
question_id: 1180330
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# dsa.msc - can it use LDAPS port 636?  How?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1180330/dsa-msc-can-it-use-ldaps-port-636-how (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm launching dsa.msc with the /domain switch to connect to a trusted domain (one way trust).  This works fine.

DSA is using port 389 for LDAP.  LDAPS is configured and verified on the target domain. 

Is there any way to get DSA to use port 636?  Or am I wasting time?

dsa.msc /domain=mydomain.com:636 does not work.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-13*

Hi @N4

Unfortunately, it's not possible. 

You can test it when you try to change domain controller from dsa.msc and you add the port 636 for LDAPS in the end of domain controller FQDN. You will get unavailable status .

Please don't forget to mark helpful answer as accepted
