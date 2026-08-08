---
title: "How to configure a certificate with ADCS with notbefore=2023 and notafter later than 2050?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1434241/how-to-configure-a-certificate-with-adcs-with-notb
question_id: 1434241
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# How to configure a certificate with ADCS with notbefore=2023 and notafter later than 2050?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1434241/how-to-configure-a-certificate-with-adcs-with-notb (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to configure a certificate to authenticate VCENTER over LDAPS, but it must have "notafter" later than 2050.

 According to the RFC5280, certificates with validity dates in 2050 or later must be encoded as GeneralizedTime; dates through 2049 should be encoded as UTCTime. 

Since I need the "notbefore" to be 2023 and the "notafter" to be 2060, how can I properly configure my certificate?

## Answers

_No answers on this thread._
