---
title: "ADFS url over public internet"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/579470/adfs-url-over-public-internet
question_id: 579470
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS url over public internet

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/579470/adfs-url-over-public-internet (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,'  

Our ADFS url does not works with internal IP. however it works with server FQDN. My request is will this url work if ADFS machine is made available over internet to browse with public IP  

Thanks  

Athulya

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-10-07*

This seems to be a tangent of the other post.  

You could make it work with IP addresses by adding bindings in that case to the Web Application Poxy server (since you are talking about Internet facing, I am assuming you are using a WAP).  

You know that FQDN are actually much more practical than IP addresses. Why this eagerness to use IP addresses?
