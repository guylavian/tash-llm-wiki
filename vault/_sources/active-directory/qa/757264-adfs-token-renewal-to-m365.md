---
title: "ADFS token renewal to M365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/757264/adfs-token-renewal-to-m365
question_id: 757264
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS token renewal to M365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/757264/adfs-token-renewal-to-m365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My ADFS is set with defaults  

the new token cert was promoted to primary  

my relaying trust partners have updated meta data  

just my office 365 still shows the old certificate.  the certificate in M365 expires on March 8.  how long before M365 will sync that up or is this something i need to do manually by running  

Update-MSOLFederatedDomain –DomainName <your domainname> -SupportMultipleDomains  

?  

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-03*

Ok, Thank you i was wondering since i have never ran this command in the last 5 years when this auto renewed.  

I will scheduled this for tonight
