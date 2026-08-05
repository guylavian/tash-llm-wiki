---
title: "Exchange Hybrid Certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1457937/exchange-hybrid-certificate
question_id: 1457937
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
---
# Exchange Hybrid Certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1457937/exchange-hybrid-certificate (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have a question to be verified for the following scenario:

We've Root Domain (lan.contoso.com) and the external URL for emails is contoso.com with 4 Exchange server 2013 and child domain (lan2.contoso.com) which has one exchange server 2013 with another external URL (domain.com)

both domains contoso.com and domain.com is added to accepted domains.

since exchange 2013 is out of support we are planning to migrate all users mailbox to EXCH Online.

I'm confused a little bit about the prober configuration for the hybrid configuration wizard:

-  do we need to run the hybrid configuration wizard in both domain (root and child) ? or the root domain is enough?

-  Microsoft Entra connect will be installed at the root domain and will sync all users from root domain and child.

-  M365 Tenant will be verified for both public domains.

-  regarding the certification for the hybrid wizard do we need a new certificate so the two domains (contoso.com and domain.com) will be added since each exchange server use his own certificate?

Thanks,

## Answers

_No answers on this thread._
