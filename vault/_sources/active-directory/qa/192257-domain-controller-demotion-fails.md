---
title: "Domain Controller demotion fails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/192257/domain-controller-demotion-fails
question_id: 192257
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller demotion fails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/192257/domain-controller-demotion-fails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

we tried to demote Domain Controller through removing ADDS role from the server but faced an issue   

The operation failed because:  

DFS Replication: Access is denied.   

"Access is denied."  

DFs & DFSR services are disabled and not used for a long time.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-09*

What operating system is used?    

DFs & DFSR services are disabled and not used for a long time.    

not sure what is meant? Are domain controllers using FRS? Another simpler method is to remove from network then perform metadata cleanup to remove from active directory.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to Accept as answer if the reply is helpful--
