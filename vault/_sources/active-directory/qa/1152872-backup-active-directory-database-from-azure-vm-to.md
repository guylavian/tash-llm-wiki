---
title: "Backup Active Directory database from Azure VM to Azure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1152872/backup-active-directory-database-from-azure-vm-to
question_id: 1152872
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Backup Active Directory database from Azure VM to Azure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1152872/backup-active-directory-database-from-azure-vm-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

Is there a tool that allows us to save Active Directory databases from an Azure VM in the Azure Environment in a dedicated azure container ?     

Currently we're doing dumps via the backup tools locally on the azure VM.    

To be more precise, is there an azure service that would allow us to save directly the Active Directory without using the local tools.    

thanks a lot in advance    

Regards    

Louis

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-01-05*

There is no built-in tools for backing up Active Directory, technically, Azure Backup will backup Active Directory, if its running on a Domain Controller.    

You could use Azure Automation, to trigger a hybrid task to backup DHCP, DNS, AD database etc to a folder share running on an Azure VM, which then gets backed up on the Azure VM - but there is no built-in tools to target the database directly, only VM backup via Azure Recovery Services.
