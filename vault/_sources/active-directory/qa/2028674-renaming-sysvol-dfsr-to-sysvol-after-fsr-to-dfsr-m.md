---
title: "Renaming SYSVOL_DFSR to SYSVOL After FSR to DFSR Migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2028674/renaming-sysvol-dfsr-to-sysvol-after-fsr-to-dfsr-m
question_id: 2028674
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Renaming SYSVOL_DFSR to SYSVOL After FSR to DFSR Migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2028674/renaming-sysvol-dfsr-to-sysvol-after-fsr-to-dfsr-m (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After migrating from FSR to DFSR, we want to rename "SYSVOL_DFSR" to "SYSVOL". What are the steps we need to follow, what impact will it have, and what registry changes need to be made to achieve this?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-30*

Hello，

Steps to rename “sysvol_dfsr” to “sysvol”

-  Verify Migration Completion:

-  Ensure that the migration from FRS to DFSR is fully completed and that all domain controllers are replicating correctly using DFSR.

-  Update the SYSVOL Path:

-  On each domain controller, update the SYSVOL path in the registry:

-  Open the Registry Editor

-  Navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters

-  Modify the value to point to the new path (e.g., ).SysVol C:\Windows\SYSVOL

-  Rename the Folder:

-  Rename the folder to on each domain controller.

-  Update DFSR Configuration:

-  Update the DFSR configuration to reflect the new path:

-  Open the DFS Management console.

-  Navigate to the Replication section.

-  Update the folder path for the SYSVOL replication group to the new path.

-  Restart Services:

-  Restart the and services on each domain controller to apply the changes.`NetlogonDFSR`

Please always take a backup of the current configuration and data before making any changes.

Best Regards, 

Hania Lian

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
