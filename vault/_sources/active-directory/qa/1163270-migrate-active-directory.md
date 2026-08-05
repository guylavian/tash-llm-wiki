---
title: "Migrate Active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1163270/migrate-active-directory
question_id: 1163270
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Migrate Active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1163270/migrate-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a server. This server has a 2008r2 functional level of the foresta.I Need insert new 2022 server as domani controller.Is It possible?How can I do It?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-01-23*

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR  

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019 or 2022, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-23*

Hi,

The minimum requirements to add a Windows Server 2022 Domain Controller is the same as windows 2019:  

Windows Server 2008  functional level or higher.  

Use DFS-R as the engine to replicate SYSVOL.

You current functional level Windows 2008 R2 should be sufficient , to promote a domain controller under Windows 2022, but it's recommended to raise it to Windows 2016 once all domain controllers upgraded to windows 2016 or higher.

Please don't forget to mark helpful answer as accepted
