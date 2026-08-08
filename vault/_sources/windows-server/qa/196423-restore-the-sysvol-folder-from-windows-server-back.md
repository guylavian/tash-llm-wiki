---
title: "Restore the SysVol Folder from Windows Server Backup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/196423/restore-the-sysvol-folder-from-windows-server-back
question_id: 196423
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["Mvp"]
---
# Restore the SysVol Folder from Windows Server Backup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/196423/restore-the-sysvol-folder-from-windows-server-back (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear All,  

We have DC with Win2012 Std, ADC with Win2012Std & ADC1 with 2008R2 Std, unfortunately our environment have Ransomware Attached recently due to this our SysVol Folder &Files has been encrypted. We want to recover our SysVol Folders with minimum efforts, please can any one suggest us best soloutions.  

Thanks in Advance.  

Regards,  

M Akhtar

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-13*

Restore the system state somewhere, then you can follow along here.  

https://support.microsoft.com/en-us/help/315457/how-to-rebuild-the-sysvol-tree-and-its-content-in-a-domain  

--please don't forget to Accept as answer if the reply is helpful--
