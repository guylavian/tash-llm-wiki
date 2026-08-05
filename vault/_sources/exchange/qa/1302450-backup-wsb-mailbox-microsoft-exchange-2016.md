---
title: "Backup (WSB) mailbox Microsoft Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1302450/backup-wsb-mailbox-microsoft-exchange-2016
question_id: 1302450
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Backup (WSB) mailbox Microsoft Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1302450/backup-wsb-mailbox-microsoft-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!

Need advice for backing up mailboxes. 

There are 2 Exchange 2016 (Standart) servers configured in DAG. There is a mailbox with a volume of 900 GB., stored on the disk D with capacity of 3 TB. This disc is almost full, and increase the size of the impossible. Most of this disc is the transaction logs. I read about the "Circular Logging", but as I understand it, this option should be used if there are no other options. But all is recommended to use a backup. I added another disk of 1.5 TB. for backup, the task for backup folder mailbox database and transport roles (if you select the whole disk, then there will be error that the disk to backup a little volume). The task of Backup folder is executed and fails with the error "Backup location is running low on space". 

1.JPG

There will be errors in the log: 

Event ID:16389 "Writer Microsoft Exchange Writer experienced retryable error during shadow copy creation. Retrying... "

Event ID: 2034 "The Microsoft Exchange Replication service VSS Writer (Instance f622dbda-d7d4-40eb-bcf0-50b9d962e20a) failed with error FFFFFFFC when processing the backup completion event."

2.JPG

When creating the task of backing up the mail database, I expected that the transaction logs would be truncated and the 900 GB database would fit on a 1.5 Tb disk. Am I wrong? Logs are truncated only after a full backup?

I added the parameter:

HKLM\Software\Microsoft\ExchangeServer\v15\Replay\Parameters\EnableVSSWriter

0 or 1 - No effect**.**

Thanks!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-06-14*

Hi Radek,

Thanks for the share so that others experiencing the same thing can easily reference this! Since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others", I'll repost your solution in case you'd like to "Accept" the answer : )

[ Backup (WSB) mailbox Microsoft Exchange 2016-Need advice for backing up mailboxes.]

Issue Symptom:

The task of Backup folder is executed and fails with the error "Backup location is running low on space". 

There will be errors in the log:

Event ID:16389 "Writer Microsoft Exchange Writer experienced retryable error during shadow copy creation. Retrying... "

Event ID: 2034 "The Microsoft Exchange Replication service VSS Writer (Instance f622dbda-d7d4-40eb-bcf0-50b9d962e20a) failed with error FFFFFFFC when processing the backup completion event."

Resolution:

The server was backed up with veeam and circular logging was turned on.

Regards

Shaofan

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-14*

I performed a backup of the server using veeam and turned it on circular logging. I don't see any problems yet. Thank you Amit Singh!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-06-12*

For Event ID: 2034 - Restart "Microsoft Exchange Replication Service" on the passive node and see if that resolves the issue. If the problem persists, try switching protection to the current active node.

Also wanted to know if you are running a Full Backup. Based on the output, it seems incremental.
