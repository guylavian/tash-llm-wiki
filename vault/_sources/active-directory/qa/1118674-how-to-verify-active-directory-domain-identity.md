---
title: "How to verify Active Directory domain \"identity\"?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1118674/how-to-verify-active-directory-domain-identity
question_id: 1118674
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-csharp", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# How to verify Active Directory domain "identity"?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1118674/how-to-verify-active-directory-domain-identity (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am writing a .NET application and am wondering if there is a way to concretely identify that the Active Directory domain the application is running in is mine and not another domain attempting to impersonate mine.    

In this case the internal domain names would be the identical, but they are actually separate domains running on different networks.    

I was thinking of something like a certificate on the domain that I can validate, but would accept anything else.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-08*

domain controllers do use a certificate. But assuming your app is hosted by a "fake" domain, which installed an internal certificate as trusted, you would need to supply your own certificate validation routine.
