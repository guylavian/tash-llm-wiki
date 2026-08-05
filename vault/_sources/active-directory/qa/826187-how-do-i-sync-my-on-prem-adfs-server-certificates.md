---
title: "How do I sync my on-prem ADFS server certificates with Azure ADFS? or vice versa."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/826187/how-do-i-sync-my-on-prem-adfs-server-certificates
question_id: 826187
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# How do I sync my on-prem ADFS server certificates with Azure ADFS? or vice versa.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/826187/how-do-i-sync-my-on-prem-adfs-server-certificates (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an on-prem ADFS server and Azure ADFS servers, currently the AZURE ones have priority on the LB but I checked our on-prem on and the Token-Signing and Token-Decrypting certificates are different on each server, seems like AutoCertificateRollover ran independently of each other and now I have mismatching certs, the secondary certs are the same on both sets of servers, however the primary (new auto created certs) have different thumbprints on them.   

I guess I have 2 questions,   

-  Does it matter that the certificates are not the same?   

-  How do I sync them? I've tried running Update-AdfsCertificate -CertificateType Token-Decrypting -Urgent and Update-AdfsCertificate -CertificateType Token-Signing -Urgent then running Update-MsolFederatedDomain -DomainName <domain> -SupportMultipleDomain on the on-prem ADFS server but that didn't update the certs in AZURE and now they are completely different...   

Any help would be much appreciated,  

Thanks,  

Tim

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-01-22*

If you are looking to migrate those apps to Azure AD [https://www.microsoft.com/en-us/security/business/identity-access/upgrade-adfs & [https://techcommunity.microsoft.com/t5/community-events-list/microsoft-workshops-how-to-successfully-migrate-away-from-ad-fs/m-p/3668480
