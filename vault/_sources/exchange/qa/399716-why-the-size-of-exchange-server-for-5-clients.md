---
title: "Why the size of Exchange server for 5 clients"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/399716/why-the-size-of-exchange-server-for-5-clients
question_id: 399716
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Why the size of Exchange server for 5 clients

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/399716/why-the-size-of-exchange-server-for-5-clients (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2012 - Current  CU  

Server2012R2 Standard  

This exchange server hosts my small business. ~5 active mailboxes accessed by Outlook 2013 & Outlook2019  

The server is a Hyper-V system. The VHDX size is 225 GB. With only 5 active clients, the used VHDX size is 200GB. I do run a daily clean log job that was posted on the forum.  

Why so large a VHDX space usage. Is there anything else I should look at to get this size down?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-06-21*

You can move or delete any IIS logs under there. Its just the IIS logs. Not needed for Exchange or Windows to keep those.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-21*

well, I found this...  

I checked size of each folder & sub folder on the server. I also ran my utility program that cleans out temp files (450 MB) and did disk clean up (100 MB).  

 One sub folder is huge  

InetPub\Logs\Logfiles\w3svc2 at 90 GB  

What can I do to this?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-05-19*

Hi @John Lenz  

Do you have a large amount of messages send/receive per mailbox per day?

Please have a check of the size of the database folders in this path:  

C:\Program Files\Microsoft\Exchange Server\V15\Mailbox\<database name>

If you can see a lot of log files, as Andy suggested, you may use Windows Server Backup to make a VSS full backup to truncate the transaction logs.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
