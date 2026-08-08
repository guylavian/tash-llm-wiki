---
title: "adfs Token decryption certificate expiration time issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/382895/adfs-token-decryption-certificate-expiration-time
question_id: 382895
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# adfs Token decryption certificate expiration time issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/382895/adfs-token-decryption-certificate-expiration-time (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I used this command to successfully update the signature token    

 Update-AdfsCertificate -CertificateType "Token-Signing" -Urgent    

But I found that the decryption token time is missing and not updated    

Does the decryption token do not need to be updated manually, only adfs is automatically updated, and no additional trust operation is required?

## Answers

_No answers on this thread._
