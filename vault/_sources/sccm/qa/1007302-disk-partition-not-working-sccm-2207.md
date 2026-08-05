---
title: "Disk Partition not working | SCCM 2207"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1007302/disk-partition-not-working-sccm-2207
question_id: 1007302
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-deployment"]
answer_author_roles: ["Q&A User"]
---
# Disk Partition not working | SCCM 2207

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1007302/disk-partition-not-working-sccm-2207 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The task sequence on new branded device is working fine but only failing when we reimage the existing devices.     

We didnt do any changes on boot media and we are using command to partition the disk and then proceeding with task sequence    

 I dont want to run the command and procced. Any idea what went wrong?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-28*

@ SimonRenMSFT-3639 could you please review the logs please

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-03*

246985-smsts-diskpart.txt    

sorry for the late reply. got the smsts log and updated. please help

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-15*

241299-diskpart-error-new.pdf241328-smstss-logpdf.pdf    

Please find the attachments and yes we are using Bitlocker
