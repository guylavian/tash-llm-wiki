---
title: "[Migrated from MSDN Exchange Dev]  old company still can send mails on the behalf of ABC.COM domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/158795/migrated-from-msdn-exchange-dev-old-company-still
question_id: 158795
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]  old company still can send mails on the behalf of ABC.COM domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/158795/migrated-from-msdn-exchange-dev-old-company-still (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/08e192a1-6c41-4c80-bfa1-00bfa7a30f74/old-company-still-can-send-mails-on-the-behalf-of-abccom-domain?forum=exchangesvrdevelopment  

ABC.COM domain and MX  is transferred to new company , after send\receive happening via new company.  

Also observe that old company  can still send mails on behalf of ABC.COM domain  

How to restrict the same?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-11*

What is remained on the old company? An Exchange server whose default accept domain is ABC.com?     

You can set up SPF record for your domain to specify which mail servers are permitted to send email for that domain name, follow this blog to create SPF: https://practical365.com/exchange-server/a-sender-policy-framework-spf-primer-for-exchange-administrators/    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
