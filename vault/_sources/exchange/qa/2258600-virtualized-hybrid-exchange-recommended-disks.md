---
title: "Virtualized hybrid Exchange - recommended disks"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2258600/virtualized-hybrid-exchange-recommended-disks
question_id: 2258600
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Virtualized hybrid Exchange - recommended disks

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2258600/virtualized-hybrid-exchange-recommended-disks (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all!

We have an hybrid Exchange. Now, all the mailboxes are in O365. On premise, we have a dag with 2 servers and another server with exchange that allows hybrid config and communicate with O365.

We are planning to remove the dag and to have a reduced number of mailboxes on premise.

The server on premise ir virtual with VMWare.

The installation has a system disk, a dedicated disk for pagefile and another disk for exchange installation.

As we want to have some mailboxes onprem, we need two additional disks, one for BD and another for logs.

The question is:

Should the additional disks be configured as dependent or independent?

According to that decission, what are the best practices regarding server maintenance and patching? Stop exchange, do the snapshot, patch the server, check everything is ok and then, start exchange?

Thanks in advance.

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-17*

Hi Aránzazu Sampablo Fos,

Thank you for posting your question in the Microsoft Q&A forum.

Do you mean you will not use DAG and high availability architecture for your on-prem organization? If you're deploying a standalone Mailbox server role architecture, RAID technology is required for the mailbox database and log volumes.

You can check this article for on-prem Exchange storage suggestions: Separated Mailbox Database and Log Volumes

Here are some additional suggestions for you, before you install any CU or SU for standalone Exchange server:

-  Perform VSS full backup for your databases.

For Exchange server, the only supported way to recover a lost Exchange server is using /Mode:RecoverServer, and we have to recover mailbox or database data from db backup files.

For your reference:

Use Windows Server Backup to back up Exchange | Microsoft Learn 

Use Windows Server Backup to restore a backup of Exchange | Microsoft Learn 

-  If you have installed any third-party scan tool or software on Exchange, please disable or turn off them temporarily.

-  Make sure all needed Exchange services are running well before installing any Exchange CU or SU.

-  Then you can perform the upgrade or install update during non-working hours and restart the Exchange server after it’s installed successfully.

 If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
