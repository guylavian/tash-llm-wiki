---
title: "Hyper-V Domain Controller Boot Issues.  How to Backup prior to running chkdsk"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1499687/hyper-v-domain-controller-boot-issues-how-to-backu
question_id: 1499687
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-high-availability-virtualization-hyper-v", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Hyper-V Domain Controller Boot Issues.  How to Backup prior to running chkdsk

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1499687/hyper-v-domain-controller-boot-issues-how-to-backu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good Morning,
I have a 2012R2 host running a 2012r2 DC.  I am using Arcserve SPX for backups.  My backups won’t boot.  Arcserve support has discovered errors:
Arcserve has asked me to run chkdsk /f /r.  This is my PDC and file server.
I want to create a functional backup prior to the repair (Stuff happens).  What is the best way to achieve this please.  Export, Replicate or other 3<sup>rd</sup> party backup solution.  I am worried this thing might never boot again and I must be prepared.
TIA
Chris
Arcserve Case Notes follow:  

[Findings]

-  Disk\volume corruption found from the Windows system and application logs. A few entries are shown below. Source disk\volume corruption could cause the boot failure from the backup data as well.

-  The \Device\Harddisk0\DR0 disk is the C: volume disk.

   

Log Name:      System  

Source:        disk  

Date:          12/24/2023 8:01:25 PM  

Event ID:      32  

Task Category: None  

Level:         Warning  

Keywords:      Classic  

User:          N/A  

Computer:      DC-1.mydomain.com  

Description:  

The driver detected that the device \Device\Harddisk0\DR0 has its write cache enabled. Data corruption may occur.  

Log Name:      System  

Source:        volsnap  

Date:          10/10/2023 7:06:19 PM  

Event ID:      8  

Task Category: None  

Level:         Error  

Keywords:      Classic  

User:          N/A  

Computer:      DC-01.mydomain.com
Description:  

The flush and hold writes operation on volume C: timed out while waiting for a release writes command.
Arcserve has asked me to run chkdsk /f /r.  This is my PDC on and file server.  I want to create a functional backup prior to the repair (Stuff happens).  What is the best way to achieve this please.  Export, Replicate or other 3<sup>rd</sup> party backup solution.  I am worried this thing might never boot again and I must be prepared.
TIA
Chris

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-18*

Hi Chris,

Hope you're doing well.

Based on the information you've provided, it seems that your backups won't boot due to disk/volume corruption. Arcserve support has recommended running "chkdsk /f /r" to repair the logical file system errors and scan for bad sectors. Before running "chkdsk", it's advisable to create a full backup of your data to ensure that you have a functional backup in case something goes wrong.

At the same time, you can try to use Windows Server Backup to do the full backup.

It's important to note that creating a backup is not a substitute for repairing the disk/volume corruption. You should still run "chkdsk /f /r" to repair the errors and scan for bad sectors.
chkdsk | Microsoft Learn

I hope this helps.

Best Regards,

Ian Xue

If the Answer is helpful, please click "Accept Answer" and upvote it.
