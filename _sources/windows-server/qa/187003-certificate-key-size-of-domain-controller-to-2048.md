---
title: "Certificate key size of domain controller to 2048 bit"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/187003/certificate-key-size-of-domain-controller-to-2048
question_id: 187003
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Certificate key size of domain controller to 2048 bit

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/187003/certificate-key-size-of-domain-controller-to-2048 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I want to implement 2048 bit key size domain controller certificates for my domain controllers.  right now they have 1024 bit key size domain controller certificate.  

would like to get below steps verified (let me know if anything else i srequired).  

-  create a duplicate of domain controller certificate template with minimum key size 2048 in cryptography  

-  set read, enroll and autoenroll permissions  

-  Issue the certificate template  

Question 1: Do I have to create an explicit GPO for autoenrollment (renewal) for this new certificate template as my current 1024 domain controller certificate has no explicit GPO configured and they are renewed automatically?   

Question 2: Also, once above mentioned steps are executed, will it not renew certificate from 2 different template (original domain controller and new domain controller template with 2048 key) considering existing domain controller certificates are being renewed without having any explicit autoenrollment policy  

Thanks in advance for the help

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-07*

》》》Do I have to create an explicit GPO for autoenrollment (renewal) for this new certificate template as my current 1024 domain controller certificate has no explicit GPO configured and they are renewed automatically?  

According to my knowledge, I suggest you create an automatic registration strategy  

》》》Also, once above mentioned steps are executed, will it not renew certificate from 2 different template (original domain controller and new domain controller template with 2048 key) considering existing domain controller certificates are being renewed without having any explicit autoenrollment policy  

As MVP said Just remove unnecessary templates from CA will do  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2020-12-05*

Q1: yes, it is necessary to create an autoenrollment policy when using custom template. However, you may not need to create a custom template. You can utilize "Kerberos Authentication" certificate template which should have proper key length. It already has all proper permissions. And remove "Domain Controller" and "Domain Controller Authentication" templates from CAs.  

Q2: see above. Just remove unnecessary templates from CAs.
