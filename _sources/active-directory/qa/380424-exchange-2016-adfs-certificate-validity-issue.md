---
title: "exchange 2016 adfs Certificate validity issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/380424/exchange-2016-adfs-certificate-validity-issue
question_id: 380424
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# exchange 2016 adfs Certificate validity issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/380424/exchange-2016-adfs-certificate-validity-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

https://learn.microsoft.com/zh-cn/exchange/clients/outlook-on-the-web/ad-fs-claims-based-auth?view=exchserver-2016#step-1-review-the-certificate-requirements-for-ad-fs    

Refer to the above link and see that exchange needs to import adfs self-signed certificate, the default validity period is 30 days.    

Set the validity period time command as  Set-AdfsProperties -CertificateDuration <Days>    

-  What is the maximum value that can be set?    

-  If I have multiple adfs, do I need to import a certificate that trusts each adfs on the exchange?    

-  If I import the trusted adfs certificate first, and then use the above command to update the validity time of the certificate, do I need to re-import and trust it on the exchange?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-05-03*

The default validity time for the self-signed Token Signing Certificate is 365 days (not 30).  

-  I am not sure of the maximum value. I have seen customers with 3 years (that's the longest I have seen being used, but it is not the longest accepted value)  

-  The Token Signing Certificate (the cert required to create the trust) is a farm certificate. It is the same pair of keys on every nodes.  

-  The command is taking effect only for the next certificate generation cycle.
