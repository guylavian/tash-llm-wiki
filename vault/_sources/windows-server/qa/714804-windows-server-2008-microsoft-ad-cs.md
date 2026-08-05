---
title: "windows server 2008 Microsoft AD CS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/714804/windows-server-2008-microsoft-ad-cs
question_id: 714804
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# windows server 2008 Microsoft AD CS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/714804/windows-server-2008-microsoft-ad-cs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everybody  

Recently we are using Microsoft ADCS on windows server 2008 in our organization. we have an OSCP server beside our enterprise CA server. We have just noticed that the OCSP is CRL based in Microsoft CA and so as OCSP gets access to the CRL periodically sometimes OCSP returns "good" for revoked certificates because they are revoked between the two points of time that OCSP gets access to the CRL. It seems that there is a fix or update to solve this issue but I can not find the download link. can anyone help me. By the way, we can not change the version of our OS.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2022-01-29*

There is no update for this behavior. The behavior is a fundamental property of CRL-based OCSP server. In order to reduce the load, OCSP caches the referenced CRL for a period specified in CRL (Next Update) and revocation is not detected immediately. In revocation configuration provider settings you can specify how often OCSP should check for CRL updates:    

    

do not set too small value, because OCSP can be overloaded with CRL download and update operations.    

we can not change the version of our OS    

interesting, why?
