---
title: "Multiple Signature certificates in ADFS Relying Party"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/36426/multiple-signature-certificates-in-adfs-relying-pa
question_id: 36426
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Multiple Signature certificates in ADFS Relying Party

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/36426/multiple-signature-certificates-in-adfs-relying-pa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My application (SP) is in process of rolling over the signing certificates and including both the old and the new certificates in the SP Metadata. ADFS is set up to auto-update the relying party metadata. ADFS has now auto-updated pulling in both certificates in. Now the SP-initiated SAML is failing as it seems that ADFS is only using the most recent cert, which is not the cert with which the SAML Request is signed. We were under the impression that multiple signature certs can be loaded into a relying party trust and ADFS would try both, however, we're observing that it is only trying the first cert.  Is there a configuration on ADFS that we're missing?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-16*

What do you mean by "Now the SP-initiated SAML is failing as it seems that ADFS is only using the most recent cert"? ADFS is not signing things with the certificates presents on the RP config. It is only verify signature with those (ADFS doesn't even have the assocaited private key). So can you please described where you get the error and what errror it is?
