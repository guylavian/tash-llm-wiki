---
title: "Lost a disk on a domain controller with FSMo roles"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/207442/lost-a-disk-on-a-domain-controller-with-fsmo-roles
question_id: 207442
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Lost a disk on a domain controller with FSMo roles

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/207442/lost-a-disk-on-a-domain-controller-with-fsmo-roles (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

A disk on one of our domain controller failed where there are sysvol folder?  

what we should do to remediate the situation ?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-22*

You can seize FSMO roles to another healthy one    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

then perform clean up    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

then rebuild the failed one after hardware repairs.    

--please don't forget to Accept as answer if the reply is helpful--
