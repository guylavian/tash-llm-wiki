---
title: "Hybrid Exchange and Azure Backup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1093584/hybrid-exchange-and-azure-backup
question_id: 1093584
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Hybrid Exchange and Azure Backup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1093584/hybrid-exchange-and-azure-backup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a hybrid Exchange environment. Part is in Exchange365 and part is on-prem Exchange. We want to migrate the on-prem Exchange servers to Azure.    

At this moment we use a backup tool to backup/restore at mail brick level.    

Is it possible to use Azure backup for this purpose when the Exchange server is migrated to Azure?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-17*

Correct, so that was our second option. If that works for a server which we are planning to migrate to Azure, that would be nice, because we are phasing out our on-prem DC, with the present backup tooling.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-11-17*

Yes, but you are now using it for "backup/restore at mail brick level."    

That article refers to backing up the entire database. You wont be able to do a brick level backup with that.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-17*

But can we use "https://learn.microsoft.com/en-us/azure/backup/backup-azure-exchange-mabs?WT.mc_id=Portal-Microsoft_Azure_Support" to backup/restore a VM running in Azure?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-11-17*

No, you will need to continue to use your backup solution. Azure backup is not Exchange Application aware
