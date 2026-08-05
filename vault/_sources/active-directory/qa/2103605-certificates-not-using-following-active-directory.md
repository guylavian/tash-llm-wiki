---
title: "Certificates not using following Active Directory Certificate Services settings"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2103605/certificates-not-using-following-active-directory
question_id: 2103605
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Certificates not using following Active Directory Certificate Services settings

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2103605/certificates-not-using-following-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've setup Active Directory Certificate Services and set the CRL Publication Interval to daily and the Delta publication interval to 30 minutes. Then within the Online Responder setup, this is set to 15 minutes.

However, when I then check an exported certificate with certutil -f -urlfetch -verify the none of the times match with what is set.

I'm not sure if I've missed a setting or something which may be causing this.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-16*

Hello

Thank you for posting in Q&A forum.

The first image shows when the CRL will be updated.

While this command shows which certificates are verifiable and valid, you should compare this certificate with the CRL.

Basic CRL checking with certutil - Microsoft Community Hub

Best regards

Yanhong

=====================================

If the answer is helpful, please click "Accept answer" and upvote it
