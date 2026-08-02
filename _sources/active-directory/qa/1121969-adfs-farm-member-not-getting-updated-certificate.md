---
title: "ADFS Farm member not getting updated Certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1121969/adfs-farm-member-not-getting-updated-certificate
question_id: 1121969
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Farm member not getting updated Certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1121969/adfs-farm-member-not-getting-updated-certificate (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Updated the certificate on the primary node and farm member (Server 2019) before making the change via powershell and using Set-AdfsCertificate -CertificateType Service-Communications and Set-AdfsSslCertificate to make the change on the primary node. Farm member is still showing the old thumbprint of the old certificate after change and restart of services and server. The farm member doesn't appear to have any issues so not sure how to force this update. Primary node is working fine after cert update.

PS C:\Windows\system32> Get-AdfsFarmInformation

CurrentFarmBehavior FarmNodes FarmRoles

4 {ERDCCOADFS1.X ERDCCOADFS.X} {UserState}

## Answers

_No answers on this thread._
