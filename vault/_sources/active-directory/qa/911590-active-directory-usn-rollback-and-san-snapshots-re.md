---
title: "Active Directory USN Rollback and SAN Snapshots / Replication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/911590/active-directory-usn-rollback-and-san-snapshots-re
question_id: 911590
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory USN Rollback and SAN Snapshots / Replication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/911590/active-directory-usn-rollback-and-san-snapshots-re (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I understand that Windows 2012 R2 and newer OS's can handle when a snapshot is reverted on them as long on the hypervisor is new enough to support it. My question is for DR purposes if you replicate your SAN storage to another location, and have DC's that reside on separate Lun's. Do you still have to worry about USN rollback? Or what if you use a SAN snapshot, would that cause USN rollback?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-02*

Thank you for the article, but I am more interested to learn about the impact of SAN level snapshots / replicated Lun's on AD, than taking a snapshot of AD within the guest OS.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-07-02*

You can read on here about active directory snapshots.    

https://www.rebeladmin.com/2015/02/how-to-create-active-directory-snapshots/    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
