---
title: "adfs autocertificaterollover generated certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2275888/adfs-autocertificaterollover-generated-certificate
question_id: 2275888
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# adfs autocertificaterollover generated certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2275888/adfs-autocertificaterollover-generated-certificate (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Adfs server had autocertificaterollover enabled and it generated new token-signing and token-decrypting certificate 15 days before the expiry date, This caused authentication issue and we had to roll back to the previous certificate setting it to primary. Now this new certificate is set to secondary, can this be distributed to all app owners so we can later set it to primary when the existing certificate expires?

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-05-30*

Hello,

Thank you for posting the question on Microsoft Windows forum!

Yes, you can distribute the new ADFS token-signing and token-decrypting certificate (currently set as secondary) to all application owners in advance. This is actually a recommended best practice to ensure a smooth transition when the current primary certificate expires.

Hope the above steps are helpful!
