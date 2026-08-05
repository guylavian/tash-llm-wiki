---
title: "FSMO role sizing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/700179/fsmo-role-sizing
question_id: 700179
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# FSMO role sizing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/700179/fsmo-role-sizing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

What we should do when we seize a fsmo role by mistake?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-18*

Not a lot to go only but confirm the new one holds the roles. netdom query fsmo Then also confirm domain health. (dcdiag, repadmin) The failed one can be rebuilt after cleanup.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
