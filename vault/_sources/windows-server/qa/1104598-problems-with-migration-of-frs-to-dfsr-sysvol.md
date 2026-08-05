---
title: "Problems with migration of FRS to DFSR SYSVOL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1104598/problems-with-migration-of-frs-to-dfsr-sysvol
question_id: 1104598
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Problems with migration of FRS to DFSR SYSVOL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1104598/problems-with-migration-of-frs-to-dfsr-sysvol (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have migrated all of our Domain Controllers from Server 2003 to Server 2012 R2 now and raised the DFL to 2012 R2, I've now started to migrate SYSVOL from FRS to DFRS.    

I am using the instructions from this link - https://www.rebeladmin.com/2015/04/step-by-step-guide-for-upgrading-sysvol-replication-to-dfsr-distr...    

After over 24 hours one of the servers still on Start, is there anyway I can check the issue or get that server to start manually?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-01*

Hi @Anonymous   ,    

Sorry a bit late replying back, all sorted now, the DC that was having an issue that site firewall I need to update a couple routes in there, so all good now.    

Thanks for your assistance.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-25*

Hi @Anonymous   ,    

No I just started with Dfsrmig /setglobalstate 1, so I barely started the process.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-25*

Are the rest at Eliminated state?    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
