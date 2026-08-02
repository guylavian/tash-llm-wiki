---
title: "Update certificate for ADFS 3.0"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/100123/update-certificate-for-adfs-3-0
question_id: 100123
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Update certificate for ADFS 3.0

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/100123/update-certificate-for-adfs-3-0 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

The current wildcard certificate used with ADFS (Windows 2016, FBL 3.0) is about to expire in 2 weeks. We are not using any WAP, using F5 as reverse proxy. Shell we follow below steps to update the certificate  

-  Import the new wildcard certificate to ADFS server and provide read permission to ADFS service account  

-  From ADFS console, with the new certificate select "Set Service Communications Certificate"  

-  Set the new certificate :- Set-AdfsSslCertificate -Thumbprint “thumbprintofthenewsslcert" and restart the ADFS service  

-  Update the certificate with F5  

Here we have once concern. The existing certificate subject contains the published domain name as *.domain.com, while the new certificate subject contains another domain name as *.seconddomain.com with SAN contains published domain name as *.domain.com. Will this cause any issue with ADFS publishing?  

Thanks in advance

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-27*

It is fine.  

Note that if you want to be supported with F5 as a WAP replacement, make sure you use the version 13.1.0 or higher (see: https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/releasenotes/product/relnote-bigip-ve-13-1-0.html)
