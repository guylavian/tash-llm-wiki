---
title: "Change in exchange for the certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/312043/change-in-exchange-for-the-certificate
question_id: 312043
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Change in exchange for the certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/312043/change-in-exchange-for-the-certificate (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning, I have acquired a simple certificate for Exchange but internally I have problems with the names when opening MS Outloook I have 2 security alerts:  

-  autodiscover.mydomain.com  

-  serverexch.local  

names do not match  

I have already redirected the DNS and changed the main certificate names in exchange through Set-OutlookProvide EXCH, EXPR putting the name that the certificate covers, mail.mydomain.com, but this alert still appears.  

How and where can I change these names in Exchange Server 2016 to eliminate this alert.  

Thanks  

Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-15*

Hi,    

Are you using an internal or external computer that got the certificate error?     

What's the URL you set for autodiscover？ Run Get-ClientAccessService|fl uri to check that.     

Does your current certificate only covers "mail.mydomain.com"? Normally people would have "autodiscover.domain.com" included in cert as well: https://practical365.com/exchange-server/exchange-2010-faq-autodiscover-names-ssl-certificate/    

Besides, the host name(which used by client applications to connect to Exchange), the internal/external URLs and names of OWA, ActiveSync, EAC, EWS, Outlook Anywhere etc. should be added into certificates, because only a single certificate can be associated with a website and all services are offered under a single website by default, all the names that clients  of these services use must be in the certificate.     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
