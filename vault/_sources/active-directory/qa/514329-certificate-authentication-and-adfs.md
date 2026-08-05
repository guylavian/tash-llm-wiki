---
title: "Certificate authentication and ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/514329/certificate-authentication-and-adfs
question_id: 514329
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# Certificate authentication and ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/514329/certificate-authentication-and-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

pls I try set in ADFS Primary authetication method to certificate, but every try return No valid client certificate found in the request. No valid certificates found in the user's certificate store. Please try again after closing and reopening the browser and choose a different authentication method.  

i check: the certificate and certificate chain is correct  

crl is availably  

adfs server is 2019  

any idea ?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-09-01*

Hi the trouble is detected in trusted root certificates autority where is non self certificates. After move this certificates to intermediate certificates, the adfs and certificate authentication ok
