---
title: "ADFS SSL renewal issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/20861/adfs-ssl-renewal-issue
question_id: 20861
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# ADFS SSL renewal issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/20861/adfs-ssl-renewal-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,  

we got new SSL certificate to udpate ADFS WAP and ADFS server  

imported the SSL certificate local store and provided the service accout full control  

select set service communication as primary -done  

ADFS management shows new service communication certificate  

when i run Set-AdfsSslCertificate >thumbprint of new certificate> shows error - not found in local store  

Get-AdfsSslCertificate - is also blank  

restarted the ADFS services as well - no luck  

ran  Netsh http add sslcert hostnameport=adfs.XXXXXX.nl:443 certhash=<thumbprint of new certificate> appid={5d89a20c-beab-4389-9447-324788eb944a} certstore=my  

error The system cannot find the file specified.  

Please advise

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2020-03-31*

Are you sure that you have added this certificate with private key? If you open certlm.msc on server do you see certificate in local store? If you open certificate properties, is certificate chain looks correct?  

Regards  

Konrad
