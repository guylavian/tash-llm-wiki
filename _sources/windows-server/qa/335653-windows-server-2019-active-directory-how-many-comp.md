---
title: "Windows server 2019 (Active directory) how many computer can join 1-AD DS?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/335653/windows-server-2019-active-directory-how-many-comp
question_id: 335653
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Windows server 2019 (Active directory) how many computer can join 1-AD DS?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/335653/windows-server-2019-active-directory-how-many-comp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, In this question I wanna know 1 Active directory server can add how many Computer(Machine) in one Server. Our server performance is : Windows server 2019 Standard 64-Bit Memory: 32GB CPU: Xeon 2.40GHz (8 CPUs) 100% performance how many machine can join? 60% performance how many machine can join? We plan to connect 3000+ computer on AD server.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-30*

Hope the information provided by DSPatric will be helpful .  

There should be a minimum of two DCs in a domain.  If you only have one domain, all your DCs should also be GCs.  

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-03-29*

There's a bit more to it than that. You can review here.    

https://learn.microsoft.com/en-us/windows-server/administration/performance-tuning/role/active-directory-server/capacity-planning-for-active-directory-domain-services    

--please don't forget to Accept as answer if the reply is helpful--
