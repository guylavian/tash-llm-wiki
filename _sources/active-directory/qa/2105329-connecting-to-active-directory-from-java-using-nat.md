---
title: "Connecting to Active Directory from Java Using Native JGSS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2105329/connecting-to-active-directory-from-java-using-nat
question_id: 2105329
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Connecting to Active Directory from Java Using Native JGSS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2105329/connecting-to-active-directory-from-java-using-nat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How can a connection to an Active Directory server be established from Java code using the native JGSS implementation (i.e., without JAAS)?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-18*

Hello McLachlan, Alexander •,

Thank you for posting in Q&A forum.

Here are some steps for your reference:

-  Set Up Kerberos Configuration

-  Acquire a Kerberos Ticket:

-  Use GSS-API for Authentication

-  For more detailed information, you can refer to the GSS-API/Kerberos v5 Authentication - Oracle

 and A Guide to Java GSS API - Baeldung

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
