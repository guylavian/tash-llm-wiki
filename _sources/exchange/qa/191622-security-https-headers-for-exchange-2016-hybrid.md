---
title: "Security Https Headers For Exchange 2016 Hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/191622/security-https-headers-for-exchange-2016-hybrid
question_id: 191622
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# Security Https Headers For Exchange 2016 Hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/191622/security-https-headers-for-exchange-2016-hybrid (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an exchange 2016 Hybrid setup which has mix mailboxes some in onpremise and some are migrated to Office 365.    

Our SOC team does random checks for any security issues and they tried to run a poodle scan using following website: https://securityheaders.com/     

SOC team ran the test for autodiscover.domain.com and got an F rating. Attached is the screenshot for the same. IMG-20201130-WA0001.jpg    

Now the issue is that SOC team want to make sure that the exchange server has strict security and should not get any web attacks and want it to be secured from hackers.    

I tried to follow some articles:    

https://blog.ollischer.com/microsoft-exchange-2016-and-iis-8-5-enable-http-strict-transport-security-hsts     

https://www.ryadel.com/en/iis-web-config-secure-http-response-headers-pass-securityheaders-io-scan/    

I enabled the IIS HTTP header to strict mode and ran the security test again which gave me a D rating (See Screenshot) Screenshot from 2020-11-30 17-11-27.jpg, but I cannot go further since if I use the web.config changes mentioned in below article it breaks ECP and OWA functionality.    

https://www.ryadel.com/en/iis-web-config-secure-http-response-headers-pass-securityheaders-io-scan/    

Does anyone has some information OR do we really need to worry about the security headers if it is an exchange server. I can understand if we are using a website like Apache or Ngnix so we can use the above articles for strict HTTP response, but what if it is an exchange server in hybrid and any web attack would be possible for a hacker.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-14*

@KyleXu-MSFT      

Thank you for your response on this topic and apologise for my delay in response     

Our Organisation using security scorecard tool to get this scan and i don't have any Idea about working mechanism of this tool.    

I just mentioned only https://autodiscover.domain.com to explain the issue but our Security team mentioned all service records (Mail.domain.com,owa.domain.com,autodiscover...etc) where the security headers missing for all records. every time they mentioning DNS records (mail.domin.com...etc) as subdomains, normally we called those as DNS records or service records, and i have no idea how this security scorecard tool fetching these records by scanning domain.com.    

Anyhow i would like to know this scan applicable on a exchange environment or not? because these headers are really needed for any exchange then why Microsoft not designed these by default, as we know exchange websites generate automatically with the exchange installation.    

Does anyone have information about this tool and this kind of vulnerability scans against exchange environment? Please let me know..
