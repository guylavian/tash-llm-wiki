---
title: "Exchange Certificate Renewal Subject Alternative Name settings"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/180618/exchange-certificate-renewal-subject-alternative-n
question_id: 180618
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Certificate Renewal Subject Alternative Name settings

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/180618/exchange-certificate-renewal-subject-alternative-n (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016 services are configured with a certificate from local AD CA, but the time has come to replace it with a branded certificate, comodo, thawte, etc. There are three domains on this server that can receive mail, and the existing certificate matches them all...   

-domain1.com   

-domain2.com    

and then the local AD one  

-domain1.local   

There are SAN on each domain, including the autodiscover's and the hostname for the local server.  

What kind of certificate do i require to meet all these wildcard scenarios... just ignore the wildcards and get one that allow me to add Subject Alternative Names for each domain, or should i look for one that includes a mix of multiple domains and wildcards on each of those domains?   

Does it need to include the autodiscover fqdn's and the local hostname, or can i reduce this list?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-01*

Hi @jeff mcnabney   ,    

I agree with what Andy said. It’s recommend you using the SAN certificate. You could add a list of multiple host names in the certificate’s Subject Alternative Name. For the minimum host name contained in the certificate used in Exchange, it’s must contain the mail.domain.com and autodiscover.contoso.com. So the certificate need to include the Autodiscover FQDN.    

You could refer the "Best Practices for Exchange certificates" provide by Microsoft: Best practices for Exchange certificates    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
