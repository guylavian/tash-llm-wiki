---
title: "Creating a second Exchange 2016  DAG in the same AD site for Archive Mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/214247/creating-a-second-exchange-2016-dag-in-the-same-ad
question_id: 214247
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Creating a second Exchange 2016  DAG in the same AD site for Archive Mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/214247/creating-a-second-exchange-2016-dag-in-the-same-ad (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

I have an Existing Exchange 2016 DAG with user mailboxes.  

I would like to deploy on premise Archive mailboxes on different mailbox servers.  

Since the backup process is configured per DAG and we do have backup issues from time to time  

I was considering creating the new mailbox servers in a second DAG in the same AD site so the backups could run in parallel and not impact the other backup process.  

I have a few questions hopefully someone can provide answers:  

-  Is there a problem hosting TWO Exchange 2016 DAGs in the same AD site ?  

-  Can I host the primary mailbox on a mailbox server in one DAG and the archive mailbox on a mailbox server in the second DAG ?  

-  Can two DAGs use the same DAG network address ranges ?  

-  Will the existing mailbox servers be able to proxy client access to the archive mailboxes on the second DAG without the client contacting the archive mailbox servers directly ?  

Thanks  

Liran Zamir

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-21*

I think that s not problem if you have at least CU12 for 2016 Servers .  

You can check this by the following url.  

https://support.microsoft.com/en-us/topic/exchange-server-2016-allows-adding-exchange-server-2019-mailbox-server-into-a-same-dag-and-vice-versa-9a7738d8-c16c-1625-34d0-5dde62ed5f16

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-17*

Hi    

I have an Existing Exchange 2016 DAG    

in the process of upgrading to Exchange 2019, for having a safety environment I tried to run a new DAG on new exchange server 2019 (In the same organization) but it was not successful.    

first I thought it's a misconfiguration after many troubleshooting progress and run a LAB scenario I found that is because of Exchange 2016 DAG.    

Now my question is, is it possible to add a new DAG for Exchange 2019 in the same organization that already had a Exchange 2016 DAG
