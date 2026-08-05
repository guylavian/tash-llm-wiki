---
title: "ADFS application sync issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1840947/adfs-application-sync-issue
question_id: 1840947
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# ADFS application sync issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1840947/adfs-application-sync-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Installed AD HealthADFS Agent in AD FS servers but the apps are not listed in usage & Insights  section

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2024-07-25*

Verify that auditing is turned on for the AD FS servers.

Verify that verbose logging is enabled

here is the complete documentation 

https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-health-adfs
