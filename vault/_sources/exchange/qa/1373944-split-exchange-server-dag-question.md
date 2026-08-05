---
title: "Split Exchange Server DAG question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1373944/split-exchange-server-dag-question
question_id: 1373944
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Split Exchange Server DAG question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1373944/split-exchange-server-dag-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

Have some questions about Exchange Server 2016 that need your help.

Our company has 3 sites connected by dedicated lines:

Site A:

There are 3 Exchange servers

Site B:

There are 2 Exchange servers - SJMAIL1 and SJMAIL2

IP range : 172.16.26.x

Site C:

There are 2 Exchange servers - FCSMAIL1 and FCSMAIL2

IP range : 172.16.51.x

DAG - CCGMail contains Exchange servers (4 servers) in Site B and Site C 

The CCG-FC-XXXX mailbox databases are belong to site C

The CCG-SJ-XXXX mailbox databases are belong to site B

I need to split the CCGMail DAG, Site B will be created a new DAG and move all CCG-SJ-XXX mailbox databases to new DAG. Site C may be created a new DAG or continue to use CCGMail DAG.

Question 1 : How to split the DAG and what I need to do? I cannot find move action between two DAG. If I need to remove one DAG member server and then create a new DAG?

Question 2. If I create new DAG and move the mailbox database to new DAG, do all outlook users need to create new Outlook profile? Or I do not need to do anything, Outlook will continue to new DAG automatically?

Best Regards,

Borland.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-09-22*

Hi @Thomas Lau  

Question 1 : How to split the DAG and what I need to do? I cannot find move action between two DAG. If I need to remove one DAG member server and then create a new DAG?

You may need to activate database copies (which are currently active on SJ servers) on FC servers, then remove the passive database copies from SJ servers.

Take the screenshot for example, you need to activate all active database copies hosted by SJMAIL2 (starting from CCG-SalesRep to CCG-SJ-IC) on FCSMAIL1 or FCSMAIL2.

Then you can remove SJ servers from the DAG and (additionally) add new member servers to the DAG.

For more details please refer to below links which may be helpful:

Manage database availability group membership in Exchange Server

Activate a mailbox database copy

Question 2. If I create new DAG and move the mailbox database to new DAG, do all outlook users need to create new Outlook profile? Or I do not need to do anything, Outlook will continue to new DAG automatically?

To me it is not necessary to create a new DAG, you can simply add new member servers to this existing DAG.

Outlook does not connect to DAG, but connects to the member server in DAG which is hosting the active database copy for the mailbox.

In normal cases if you have DNS, load balance, and other setting like virtual directories on Exchange servers setup correctly, there is no need to recreate the Outlook profile for Outlook to connect.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
