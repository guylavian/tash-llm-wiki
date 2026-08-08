---
title: "Exchange server 2013 CU23 with security patch KB5003435"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/405840/exchange-server-2013-cu23-with-security-patch-kb50
question_id: 405840
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange server 2013 CU23 with security patch KB5003435

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/405840/exchange-server-2013-cu23-with-security-patch-kb50 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Folks,   

I have an issue after exchange server upgrade to CU 23 and security patch.   

Environment:- 2 servers configured in DAG, Exchange server 2013 CU23.   

We installed CU23 and security patch on the passive node and after that ECP is started showing wrong information.   

I can able to login to ECP without any issue but when i am looking for mailbox database copy status on passive node it is showing error. (Both servers are showing same error)  

Whereas mailbox database copy status is showing healthy in EMS from both node.   

Error :-  server-side administrative operation has failed. The Microsoft Exchange Replication service may not be running on server. Specific RPC error message: Error 0x71a (The remote procedure call was cancelled) from RpccGetCopyStatusEx4  

Please suggest if any one experienced same issue.   

Thanks  

Chinmay Joshi

## Answer (community) — community member

*upvotes: 1 · updated: 2021-05-24*

Hi KaelYao-MSFT  

Thanks for your reply. That's correct.  

I have figured out the issue. I was getting error due to windows firewall.  Once firewall status is changed to off since then everything is normal.    

Thanks  

Chinmay Joshi

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-05-24*

Hi @Chinmay Joshi       

Sorry I was a little confused with your question.    

Did you mean:    

When checking the mailbox database copy status via EAC, it returned the error message (server-side administrative operation has failed)?    

While when you run the Get-MailboxDatabaseCopyStatus command via EMS, the database copy status was healthy and there was no error message.    

If I misunderstood anything, please feel free to correct me.    

-------------------------------------------------------    

Have you checked if the "Microsoft Exchange Replication" service is running on both nodes?    

Please also run the Test-ReplicationHealth command via EMS to see if there are issues with the replication process.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
