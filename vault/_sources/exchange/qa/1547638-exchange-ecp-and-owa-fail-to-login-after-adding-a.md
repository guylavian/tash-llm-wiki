---
title: "Exchange ECP and OWA fail to login after adding a new certificate from Free Public CA."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1547638/exchange-ecp-and-owa-fail-to-login-after-adding-a
question_id: 1547638
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange ECP and OWA fail to login after adding a new certificate from Free Public CA.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1547638/exchange-ecp-and-owa-fail-to-login-after-adding-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am working in a lab to test upgrades and migration of Exchange.  In lab I am having the hardest time getting the certificate I created to work.  

The cert is added correctly.  I import the PFX and then set it to the Exchange services.  

```
$newCert = Get-ExchangeCertificate -Thumbprint "xyz"

$newCert | Enable-ExchangeCertificate -Services POP,IMAP,IIS,SMTP
```

If I don't run IISRESET the website works for the moment and I can login.  If I run IISRESET I can get to the website but the login fails.  

When I set the certificate back to the default self signed certificate the ECP can be logged into.  

What am I missing?  I'm not sure why it's failing.  I can pin it down to using the cert.  I know it's free stuff but there are examples of using it in Exchange.    

I'm not sure where to look.  I see no errors.  There are no events that point to an issue.  I think it's maybe TLS related but I don't know.  

I've struggled trying to discover WHAT IS WRONG!!??  

The updates and changes mimic what I've done in production for years.  I'm just afraid I'm missing something and I'm about to install new services in production and this is a sticking point for me.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-02-21*

Hello @ComputerHabit  ,

I'm not sure where to look. I see no errors.

Perhaps you could try checking Event Viewer to see if there are any error messages that provide details about the problem.

Depending on what you describe, there could be an issue with the certificate itself or an issue with how the certificate is installed or configured, you could try generating a new certificate or try deleting the certificate and then re-importing it and setting it up for Exchange again Serve.
Besides, It may be that the self-signed certificate bound to the Exchange backend website is missing. It is recommended that you check again to make sure that Exchange and the Exchange backend site are using the correct certificate in IIS (edit binding) and then restart the site or IIS.

I think it's maybe TLS related but I don't know.

As you suspected, it might have something to do with TLS. Exchange Server 2019 and later are configured to enable only TLS 1.2 and disable support for legacy algorithm 2. If your certificate does not meet these requirements, it may not work properly.For more information about Exchange Server TLS configuration best practices, you can refer to:https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-tls-configuration?view=exchserver-2019

I'm not sure WHAT fixed it.

I understand that it can be frustrating when problems seem to resolve themselves without a clear explanation. When you make changes to the URL or certificate, some potential issues may be resolved, but it's hard to know for sure without more information. But this problem intermittently suggests that it may be related to a few things:

Caching: Sometimes changes don't take effect immediately due to caching. Clearing the cache or waiting for it to update can resolve the issue.

Service restart: Some changes only take effect after a service restart. The IISRESET command you mentioned earlier is a good example. However, please note that frequent resets may interrupt service. 

Configuration status: Exchange and IIS have many interdependent settings. Incorrect or inconsistent status can cause problems. Regularly checking and maintaining these configurations can help prevent problems. 

If you continue to experience these issues, you may want to consider documenting in detail the steps you took and changes you made, as well as any error messages or symptoms you observed. This can help you identify patterns or potential causes of problems and may make it easier to diagnose and fix them in the future.

Hope the above information is helpful to you！

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
