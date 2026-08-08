---
title: "ADFS Red X sign showing for relying trust due to Relying trust party monitoring out of due to monitoring errors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/384222/adfs-red-x-sign-showing-for-relying-trust-due-to-r
question_id: 384222
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Red X sign showing for relying trust due to Relying trust party monitoring out of due to monitoring errors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/384222/adfs-red-x-sign-showing-for-relying-trust-due-to-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

ADFS Red X sign showing for relying trust due to Relying trust party monitoring out of due to monitoring errors

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-05-05*

This means that the Metadata URL available in the Relying Party Trust properties is not reachable from the ADFS server.    

It could be because of many reasons:    

-  The URL is incorrect    

-  The ADFS server doesn't have access to the URL (if the URL is a public site, the ADFS might not have access to the Internet)    

-  The URL is blocked (it is an XML document maybe the HTTP proxy has weird rules blocking that)    

-  The URL uses a TLS version not supported by ADFS by default (for example, if that uses only TLS1.2 and you have not enable .Net strong crypto) see here: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/manage-ssl-protocols-in-ad-fs    

In any cases, the monitorig feature is a "nice to have" configuration. It doesn't mean the app doesn't work, it doesn't mean users can't access the workload. So at the end of the day, if the ADFS server can't reach the URL for legit reason (like you don't want to give access to the Internet in the case the URL is a public one), then you can just disable the monitoring and ask the owner of the app to notify you by email when things change on their side.
