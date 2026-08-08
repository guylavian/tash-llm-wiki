---
title: "[Migrated from MSDN Exchange Dev] Secure Exchange 2013 ECP with Azure Cloud based MFA/Office 365 MFA"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/218518/migrated-from-msdn-exchange-dev-secure-exchange-20
question_id: 218518
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Secure Exchange 2013 ECP with Azure Cloud based MFA/Office 365 MFA

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/218518/migrated-from-msdn-exchange-dev-secure-exchange-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have exchange 2010 / 2013 and 2016 deployed within forest i would like to secure one of its site with MFA the similar way i have secured remote session through remote desktop gateway with Azure extension on RDS Gateway and its great. Now i would like to secure my exchange ecp similar way but unable to find out the way to do so  

If someone could suggest something that will be great.  

Source link: https://social.msdn.microsoft.com/Forums/office/en-US/d1926e60-915d-46e1-86b5-e31c0b67aa4b/secure-exchange-2013-ecp-with-azure-cloud-based-mfaoffice-365-mfa?forum=exchangesvrdevelopment

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-05*

For Exchange on-premises ECP, you could use ADFS to protect it. After deploying ADFS, you will take two steps in login ECP, step1 to login ADFS , then you could see the real ECP webpage and login it.    

For more detail information about ADFS, you can have a look about this article: Use AD FS claims-based authentication with Outlook on the web
