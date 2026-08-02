---
title: "SYSVOL and NETLOGON Not replicating."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/409179/sysvol-and-netlogon-not-replicating
question_id: 409179
fetched: 2026-07-25
answer_count: 18
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# SYSVOL and NETLOGON Not replicating.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/409179/sysvol-and-netlogon-not-replicating (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I need to migrate to DFRS but have an issue. My PDC is 2008 r2. I noticed this issue promoting when I promoted a new DC. If I use the 2008 r2 server as a replication partner, SYSVOL and NETLOGON are not created and shared. If I use a different DC as replication partner I have no issues. Also, the contents of the SYSVOL and NETLOGON folders are no longer replicating to other DCs in the domain from this DC. I need to correct this so I can migrate to DFRS and replace the 2008 R2 DCs in the domain.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-25*

I ran the nonauthorative restore about 18 minutes ago. I received event 13520 and a few others. The last event about 14 minutes ago was 13508, "the file replication service is having trouble enabling replication fron DC2 to DC1. The netlogon and sysvol shares have not been recreated yet. The files are still in "NtFrs_PreExisting___See_EventLog"

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-25*

Just checking if there's any progress or updates?  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-25*

Yes, on the problematic one.  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-25*

Thanks. I am assuming i do this on the Dc with the issue, not on all DCs?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-25*

I'd start by trying a nonauthoritative restore  

https://support.microsoft.com/en-us/help/290762/using-the-burflags-registry-key-to-reinitialize-file-replication-servi  

--please don't forget to Accept as answer if the reply is helpful--
