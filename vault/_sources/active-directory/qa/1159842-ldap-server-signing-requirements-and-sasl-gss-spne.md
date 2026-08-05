---
title: "LDAP server signing requirements and SASL GSS-SPNEGO on port 389"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1159842/ldap-server-signing-requirements-and-sasl-gss-spne
question_id: 1159842
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# LDAP server signing requirements and SASL GSS-SPNEGO on port 389

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1159842/ldap-server-signing-requirements-and-sasl-gss-spne (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Folks

I plan to change LDAP server signing requirements to Require signing but in the network I Can see a lot of LDAP connections base on SASL GSS-SPNEGO on port 389.

Please let me know if connections base on SASL  will be blocked after policy change or not ?

I enabled LDAP logging and remediated all applications generating  Event logs ID like: 2887,2888,2889

Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-12*

Hi,

Please let me know if connections base on SASL will be blocked after policy change or not ?

The answer is yes. After enabling LDAP signing on domain controller , all LDAP request/connection will be rejected by domain controller.  

I invite you to read the following article talking about LDAP signing:

 Microsoft article about LDAP Signing

Please don't forget to mark helpful reply as answer
