---
title: "LDAP signing set to 'Require Signing' on Endpoints (including Servers) & none on Domain Controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2128546/ldap-signing-set-to-require-signing-on-endpoints-i
question_id: 2128546
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# LDAP signing set to 'Require Signing' on Endpoints (including Servers) & none on Domain Controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2128546/ldap-signing-set-to-require-signing-on-endpoints-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Background Information:

We are in the process of enabling LDAP signing within our domain.

-  Phase 1: We updated the Group Policy on client machines to 'Negotiate Signing' and enabled auditing on Domain Controllers. The 2889 event ID in Directory Services identified few legacy appliances and applications that cannot support LDAP signing.

To address this, we decided to redirect such legacy systems to a specific Domain Controller (e.g., DC10). Currently, the LDAP signing policy on all Domain Controllers is set to 'None.'

Phase 2: We plan to enable LDAP signing as 'Require Signing' on all Domain Controllers except DC10.

Phase 3: We intend to enforce LDAP signing as 'Require Signing' on all client machines (including servers).

Question:

Given that we will not enable the LDAP signing group policy on DC10 (keeping it set to 'None'), will client machines configured to require LDAP signing face any authentication issues when attempting to authenticate via DC10 after Phase 3? Or will it still function correctly, even though DC10 does not mandate LDAP signing?

## Answers

_No answers on this thread._
