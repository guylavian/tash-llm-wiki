---
title: "RPC Operations/sec Outstanding Exchange Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/265588/rpc-operations-sec-outstanding-exchange-server-201
question_id: 265588
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# RPC Operations/sec Outstanding Exchange Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/265588/rpc-operations-sec-outstanding-exchange-server-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have added one new server into the existing production, OS 2019 Core, Exchange Server 2019. We have moved one of the databases DAG copy on this server and started to face performance issues and we check it via setting performance counter found that there is always a backlog RPC Operations/sec where on other servers its always on 0.  

We moved back the DB to other servers and try to check the same with one DB which's having a single mailbox but again there is always RPC Operations/sec backlogs and which is increasing IS RPC latency so whoever client is connected to this CAS server started to face the slowness in accessing MAPI mailboxes.  

We have checked all the Application and System Event logs but did not find anything related.  

Server Hardware Configurations are below  

HP ProLiant DL360p Gen8  

Intel Xeon E5-2650L v2 @ 1.70GHz, 1701 Mhz, 10 Core(s), 20 Logical Processor(s)  

Intel Xeon E5-2650L v2 @ 1.70GHz, 1696 Mhz, 10 Core(s), 20 Logical Processor(s)  

Memory 128 GB  

DISK Enterprise SSD (RAID 0)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-07*

Unfortunately, It's still same and even after getting Exchange server Installed on new server where MS support did nothing but waste a lot of time. Anyone is having any clue why this RPC Operations/sec backlogs from the RPC CLIENT ACCESS COUNTERS is not stable on just one server we are adding in existing Exchange 2019 Production. This is creating huge issues :(

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-10*

Hi @Bhupender Kumar  ,    

From what I read, we usually check the status of both "RPC Operations/sec" and "RPC Requests" when troubleshooting slow RPC request processing issues. So you could check the RPC Requests performance counter as well and see how it goes.     

-  If RPC Requests is steadily increasing while RPC Operations/sec remains fairly stable, this indicates that the server cannot handle the existing workload and it's suggested to verify hardware components or decrease the number of users on the server. (This doesn't seem to be applicable to your situation as your hardware configuration seems good enough and you have tried to leave a single mailbox on the server.)    

-  If RPC Requests is steadily increasing but RPC Operations/sec steadily decreases, this indicates that the Exchange server is the source of the bottleneck. This kind of situation is generally caused by either a serious physical resource shortage (memory or disk) or a processing issue within the Information Store or an integrated component (antivirus, journaling, and so on).    

Reference: Troubleshooting Slow RPC Request Processing Issues.    

Furthermore, for current situation, if the users who report the performance issues are running Outlook in Online mode, it's recommended to switching to Cached mode instead which could potentially help improve the performance.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
