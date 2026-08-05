---
title: "2016 Windows Domain Controller no longer booting"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2186576/2016-windows-domain-controller-no-longer-booting
question_id: 2186576
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# 2016 Windows Domain Controller no longer booting

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2186576/2016-windows-domain-controller-no-longer-booting (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a domain controller 2016 standard environment and my data seems to be intact, but the efi partition is missing and the disk will not boot. What can I do to create a new partition for this disk so that I can boot into the Domain controller?

I had a c drive backup that was created from windows server backup the night before the server went down. I have not been able to get a bare metal recovery backup so that was the next best thing. I attempted to install windows server 2016 to a new disk and recover from the backup that I had created, but Windows server backup spit back an error stating the drive was compressed or had a system limitation that did not allow it to be recovered from it.

I just wanted to basically attempt to copy the files from the backup into the place of the c drive on the server instance so that I would have the EFI partition there to point to the bootable sector.

I have tried a multitude of other things, but nothing seems to work.

Please help!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-16*

Hello

Thank you for posting in Microsoft Community forum.

I understand your situation. Here are the steps you can follow to create a new EFI partition and restore your backup: 

Creating a new EFI partition: 

-  Open Command Prompt as an administrator.

-  Type diskpart and press Enter.

-  Type list disk and press Enter. Note the number of the disk where you want to create the EFI partition.

-  Type select disk X (replace X with the number of your disk) and press Enter.

-  Type create partition efi size=100 (100 is the size in MB, adjust as needed) and press Enter.

Restoring from backup: 

-  Mount the backup volume and assign a drive letter.

-  Copy all the files you need from the backup to the new EFI partition.

Regarding the error you encountered with Windows Server Backup, it could be due to a few reasons: 

-  The backup target is specified as a network share but is located on the same physical server.

-  The backup is one giant file and the file size limit on NTFS is 16.7TB.

-  The backup or the target disk might be compressed.

You might want to check these potential issues and adjust your backup strategy accordingly. If the problem persists, consider using a different backup tool or strategy. 

Best Regards,

Wesley Li
