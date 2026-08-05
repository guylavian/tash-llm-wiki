---
title: "Exchange 2013 SSL auto renewed installation process"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/235046/exchange-2013-ssl-auto-renewed-installation-proces
question_id: 235046
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2013 SSL auto renewed installation process

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/235046/exchange-2013-ssl-auto-renewed-installation-proces (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My exchange SSL certificate is issued by CA GoDaddy. They automatically sent me the renewed certificate and I am trying to apply it per their Exchange2013 SSL install process.  

In Exchange Admin center, the expiring certificate says .. renew so I cannot "Complete" the process and install.  

I generated certificate request and that created the "Pending Request->Complete" status with the new expires date. Exchange admin center shows 2 certificates with my mail name with current and future expires on date. The old status is VALID.RENEW and the new one is Pending Request.Complete  

I then clicked complete (intermediate already installed) and pointed to the downloaded, renewed .CRT. It takes it but the exchange admin center stays at pending request and does not move to VALID   

How do I get the renewed certificate into exchange?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-19*

Re-key with CSR ... works  

Thanks  

I will turn off auto renewal and next time send CSR request

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-18*

OK< I submitted the Key request to GoDaddy. I'll post progress when I receive the Certificate
