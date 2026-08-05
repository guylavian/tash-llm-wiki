---
title: "How to obtain new certificate from ADCS server?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1002275/how-to-obtain-new-certificate-from-adcs-server
question_id: 1002275
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Volunteer Moderator"]
---
# How to obtain new certificate from ADCS server?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1002275/how-to-obtain-new-certificate-from-adcs-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Team,     

I have active directory and CA server separately.    

As I can see, AD server has three certificates issued by CA.     

1 . Directory Service Email Replication    

 2. Kerberos Authentication    

 3. domain controller authentication    

What will happen if I "renew these certificates with new key" ?     

Is there any effect for domain computers and users?     

Could you kindly suggest?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-20*

Do you know what is the usage of "RAS and IAS Server template" ?    

We need to renew the certificate since it is expired.    

Do you know what the difference when we renew the certificate with "same key " or "new key" ?    

How can we decide how it will impact to domain users or domain computers?

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-11*

Hi,    

No issues if you renew with new key, just make sure the SAN and other details in the Certificate is same including the CN.    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
