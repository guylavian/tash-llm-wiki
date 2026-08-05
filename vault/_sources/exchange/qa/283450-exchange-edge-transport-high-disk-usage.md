---
title: "Exchange edge transport high disk usage"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/283450/exchange-edge-transport-high-disk-usage
question_id: 283450
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange edge transport high disk usage

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/283450/exchange-edge-transport-high-disk-usage (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Server 2016, Exchange 2016 Cu14.  No edge server.  Single exchange server.  Hyper-V VM.  

A month ago, the exchange edge transport service has increased to the point backups will not run due to high disk usage (20,000,000+ b/s for read/write combined)  

No recent updates were installed.  

No recent software installed.  

Given 15gb RAM, using about 12GB on average.  

Plenty of free disk space.  

No notable errors in event viewer.  

Roughly 100 active user mailboxes.  

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-23*

Resource manager was showing edgetransport.exe as high disk usage.  

Looks like I found the cause.  The journaling mailbox was full.  I expanded that and after several hours of messages coming into that mailbox, it looks like the disk usage is back down.  

If there's any Microsoft employees seeing this thread, an actual error saying the journaling mailbox is full would be GREATLY appreciated.   

When I use the get-queue, I show 1 message stuck in dnsconnectordelivery and is in a retry state.  Get-queue was run after the journaling mailbox was expanded.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-23*

Hi @Susan Dodds   ,    

I'm sorry that i couldn't understand the issue completely, do you mean you have no edge server but the Edge Transport Service caused the high I/O usage?    

Will the Resource Monitor show the high Total usage of EdgeTransport.exe? Since i didn't find this in the monitor, i think you could check it:    

    

I also test it in a Mailbox + Edge server environment, and found the the EdgeTransport.exe will appear for the first several minutes then gone.    

If this program always using disk resources, i think there could be messages stuck in queue.    

You could check it with Get-Queue in EMS.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
