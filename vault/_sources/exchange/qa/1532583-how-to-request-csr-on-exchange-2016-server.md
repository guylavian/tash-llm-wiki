---
title: "How to Request CSR on Exchange 2016 Server?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1532583/how-to-request-csr-on-exchange-2016-server
question_id: 1532583
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# How to Request CSR on Exchange 2016 Server?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1532583/how-to-request-csr-on-exchange-2016-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an exchange server in 2016. I noticed that the functionality to export, import, renew, and complete certificate requests has been removed from the Exchange admin center.
Could someone please provide the Exchange command line to request the CSR for the Exchange 2016 server and complete the certificate request?
Thanks,
Jay

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-15*

Hi @JSPilaps  

For create a certificate request in Exchange Management Shell, please refer to this link:

Use the Exchange Management Shell to create a new certificate request

It contains examples for different scenarios like:

Wildcard certificate request

SAN certificate request

Single subject certificate request

For complete the certificate request, please refer to this link:

Use the Exchange Management Shell to complete a pending certificate request

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
