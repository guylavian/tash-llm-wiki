---
title: "SYSVOL and NETLOGON not shared"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/706007/sysvol-and-netlogon-not-shared
question_id: 706007
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# SYSVOL and NETLOGON not shared

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/706007/sysvol-and-netlogon-not-shared (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

After domain controller promotion , sysvol and netlogon not shared.  

Sysvol replication seems completed but it's not shared.  

Any idea please ?

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-01-22*

Not much to go on but try working through this one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares    

or simply move roles off, demote, confirm domain health is 100%, reboot, and promo it again.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
