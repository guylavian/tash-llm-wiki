---
title: "Domain controller 1&2 offline over 2 months"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/557532/domain-controller-1-2-offline-over-2-months
question_id: 557532
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Domain controller 1&2 offline over 2 months

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/557532/domain-controller-1-2-offline-over-2-months (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Domain controller was setup, then taken offline for longer than the tombstone limit. Now I can't get it to replicate again with DC2. please, any solution to replicate back

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-09-18*

If a domain controller has tombstoned then the solution is to seize roles (if necessary) to a healthy one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

then perform cleanup to remove remnants    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

then rebuild the failed one. I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new one, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-20*

Hello,  

Thank you for your question.  

If the tombstone limit already passed then it may not Sync with AD properly and its better to decommission and promote new one with new name and ip or you have to use meta cleanup for AD objects.  

Please also consider to download Active Directory Replication Status Tool and see how How is the health of AD now.  

https://www.microsoft.com/en-in/download/details.aspx?id=30005  

If the reply was helpful, please don’t forget to upvote or accept as answer.
