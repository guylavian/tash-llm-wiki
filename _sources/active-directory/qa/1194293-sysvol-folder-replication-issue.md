---
title: "SYSVOl folder replication issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1194293/sysvol-folder-replication-issue
question_id: 1194293
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# SYSVOl folder replication issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1194293/sysvol-folder-replication-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I'm seeing lot of issue with SYSVol folder replication

ConflictAndDeleted keep filling up after i do an clean up using https://learn.microsoft.com/en-gb/archive/blogs/askds/manually-clearing-the-conflictanddeleted-folder-in-dfsr

What do i need to do to check and fix the issue with SYSVol folder replication

What firewall ports are required for replication because issue is happening between different data centre and all of our DC are firewalled in

Also

Do we need to install DFS Namespace or/And DFS Replication on all our domain controllers

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-03-29*

The ports listed here need to be open between sites.  

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts#windows-server-2008-and-later-versions  

as to broken replication, assuming not yet tomebstoned you could try a non-authoritative sync  

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization#how-to-perform-a-non-authoritative-synchronization-of-dfsr-replicated-sysvol-replication-like-d2-for-frs  

-  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
