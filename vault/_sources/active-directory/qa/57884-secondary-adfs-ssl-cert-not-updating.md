---
title: "Secondary ADFS  ssl cert not updating"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/57884/secondary-adfs-ssl-cert-not-updating
question_id: 57884
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Secondary ADFS  ssl cert not updating

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/57884/secondary-adfs-ssl-cert-not-updating (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have primary ADFS server on 2012r2 but secondary ADFS server on 2016. When Primary ADFS cert updated, the secondary ADFS cert is not updated automatically, yet it could not be set manually as it is 2016 secondary.  

How can I update cert in 2016 secondary ADFS server in that case?  

Regards,  

Lydia

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-08-03*

To update the Service Communication certificate, you will have to:  

-  Import the new certificate in the machine store in each node. Make sure the virtual account NT SERVICE\ADFSSRV has the read permission on the private key.  

-  Run the following cmdLet only on the primary server:      Set-AdfsCertificate -CertificateType Service-Communications -Thumbprint <Thumprint of the newly imported certificate>

-  Run the following on each ADFS server:      Set-AdfsSslCertificate -Thumbprint <Thumprint of the newly imported certificate>
