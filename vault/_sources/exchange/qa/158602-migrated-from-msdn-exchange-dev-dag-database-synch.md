---
title: "[Migrated from MSDN Exchange Dev] DAG database synchronization"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/158602/migrated-from-msdn-exchange-dev-dag-database-synch
question_id: 158602
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev] DAG database synchronization

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/158602/migrated-from-msdn-exchange-dev-dag-database-synch (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on Exchange developer questions and the TechNet Exchange forums for Non-developer Exchange have been locked down and transitioned to Microsoft Q&A for support, we manually migrated this one to Microsoft Q&A platform to continue the discussion.  

[MSDN thread link] DAG database synchronization  

[Original post]  

Hi;  

Today, I found a huge number in "Copy queue length" number, after I hit "resume", the number goes down to "0" and I checked the all mailbox database, its "Content index state: Healthy" is healthy.  

TestReplicationHealth -Identity Mailboxserver-1  

TestReplicationHealth -Identity Mailboxserver-2  

No error found, all pass.  

However; when I look at the file folder where usually keep the copy queue, there are still a lot of files... some of them are .jrs files, a lot of them are the "E01008xxxx.log - E01009xxxx.log" files.  

I know that this folder should be clean at all times, how can I clean up these files or resync this file?  

C:\OS partition  

D:\ to keep the mailbox.edb files  

E:\ to keep the log files.  A lot of log files since Oct 21st.  

What can I do?  

thx!~

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-11*

Hi,  

What's the version of your Exchange server?  

Do you see any error events which could be related to this issue in the Application logs?  

Please have a check to see if you are having high disk or high CPU usage problems.  

It's also suggested to try restarting the Microsoft Exchange Replication Service and see if there would be any improvement.  

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
