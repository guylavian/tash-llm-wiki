---
title: "Exchange Database are in unknow state (Exchange server 2019)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1832338/exchange-database-are-in-unknow-state-exchange-ser
question_id: 1832338
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Exchange Database are in unknow state (Exchange server 2019)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1832338/exchange-database-are-in-unknow-state-exchange-ser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have two Exchange servers (EXG-01 and EXG-02) configured with a Database Availability Group (DAG). In this setup, DB01 and DB02 reside on EXG-02, while DB03 and DB04 are located on EXG-01. Unfortunately, EXG-01 has crashed and is currently inaccessible. Upon checking EXG-02, I found that DB01 and DB02 are healthy and operational. However, DB03 and DB04 are in an unknown state and require updating on EXG-02. Could you please provide a step-by-step guide to bring all databases online on EXG-02?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-07-22*

Hello Parsian, 

```
Get-DatabaseAvailabilityGroup -Name 
```

 Replace <DAGName> with the actual name of your DAG. If the DAG status is healthy and shows DB01 and DB02 in a synchronized state, you can bring them online using the following command: 

```
Get-MailboxDatabase -Database  | Set-MailboxDatabase -Status Online
```

Replace <DatabaseName> with the names of the databases you want to bring online (DB01 and DB02). If the previous step fails or the database copies are not synchronized, you might need a forced activation. Use this command with caution as it can cause data loss: 

```
Get-MailboxDatabase -Database  | Set-MailboxDatabase -ActivationPolicy Forced
```

 Replace <DatabaseName> with the specific database name. After attempting to bring the databases online, monitor their status using the following command: 

```
Get-MailboxDatabase -Status
```

This will show the current state of all mailbox databases in the DAG, including DB03 and DB04. If DB03 and DB04 remain offline after these steps, further troubleshooting is required to determine the cause and recovery process. You might need to perform a manual failover or restore the databases from backup depending on the specific issue.
