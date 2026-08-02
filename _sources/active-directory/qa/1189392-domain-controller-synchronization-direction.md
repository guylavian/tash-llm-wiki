---
title: "Domain controller synchronization direction"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1189392/domain-controller-synchronization-direction
question_id: 1189392
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# Domain controller synchronization direction

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1189392/domain-controller-synchronization-direction (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have such question I have two domain controllers, main DC1 that hold all FSMO roles, and the second DC2, now I have to turn off for couple of days DC1 server, as this is a server with FSMO roles, after restoring it, won't the old data from DC1 to DC2 be synchronized ? Thanks for explanation.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-03-14*

Hi @Tutek  

sorry I thought that you talk about DC1 restoration from a backup.

if you will just restart DC1 , AD objects already modified from DC 2 before the restart of DC 1 will be replicated automatically to DC1 at the first AD replication. So old data will be updated by DC2 .

Please don’t forget to mark helpful answer as accepted*

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-03-14*

Hi @Tutek  

When you restore DC1 ,and choose a Non-AUTHORITATIVE RESTORE , all  restored DATA will be replaced after the first AD replication between DC1 and DC2.

In other hand If you choose authoritative restore , the old DATA restored from DC1 backup will be replicated and replace the new Data in DC2 :   

For more details you can read this link : HOW TO RESTORE DOMAIN CONTROLLER FROM BACKUP?

Please don't forget to mark helpful answer as accepted
