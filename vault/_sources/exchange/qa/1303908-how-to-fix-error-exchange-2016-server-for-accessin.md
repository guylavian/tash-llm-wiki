---
title: "How to fix error  Exchange 2016 server for accessing owa: [ExAssertException: ASSERT: HMACProvider.GetCertificates:protectionCertificates.Length<1]"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1303908/how-to-fix-error-exchange-2016-server-for-accessin
question_id: 1303908
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How to fix error  Exchange 2016 server for accessing owa: [ExAssertException: ASSERT: HMACProvider.GetCertificates:protectionCertificates.Length<1]

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1303908/how-to-fix-error-exchange-2016-server-for-accessin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question



## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-06-12*

Hi, your Exchange Oauth cert is expired. Please recreate it:

https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/cannot-access-owa-or-ecp-if-oauth-expired
