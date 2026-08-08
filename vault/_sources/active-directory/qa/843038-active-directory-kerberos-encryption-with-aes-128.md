---
title: "Active Directory: Kerberos encryption with AES 128"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/843038/active-directory-kerberos-encryption-with-aes-128
question_id: 843038
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory: Kerberos encryption with AES 128

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/843038/active-directory-kerberos-encryption-with-aes-128 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have added a new support to AES-128 encryption only so our client supports AES 128 only , we cannot add support to AES-256 for some internal reasons, and we are receiving error and incorrect negations due to which domain join and user authentications fails, Please help us with the below first two cases.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-11*

Hi there,     

You can have a look at the below article which Describes the best practices, location, values, and security considerations for the Network security: Configure encryption types allowed for Kerberos security policy setting.    

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-configure-encryption-types-allowed-for-kerberos    

For the first error a computer in a child domain of an Active Directory Domain Services (AD DS) forest cannot access a service that resides in a different domain within the same forest.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/unsupported-etype-error-accessing-trusted-domain    

-----------------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--
