---
title: "How can I enable LDAPS on secodary domain controller?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1282900/how-can-i-enable-ldaps-on-secodary-domain-controll
question_id: 1282900
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
---
# How can I enable LDAPS on secodary domain controller?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1282900/how-can-i-enable-ldaps-on-secodary-domain-controll (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

I have two on-premise domain controller in the same VLAN.

In this moment I deployed CA role on the first domain controller so I can use with LDAPS (TCP 636).  

I already checked LDAPS configuration with "ldp" tool. I didn't face any trouble.

In this moment I need to enable LDAPS on the secondary domain controller.  

How can I do it?  

How can I generate and deploy certificate for the secondary domain controller?

These two DC are running Windows Server 2019.

Thanks a lot  

Federico

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-05-11*

Hi,

For this you will need to deploy Domain Controller Certificate Template and distribute the certificate via the enrollment policy - Details over here - https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/hello-cert-trust-validate-pki

==

Please Accept the answer if the information helped you. This will help us and others in the community as well.
