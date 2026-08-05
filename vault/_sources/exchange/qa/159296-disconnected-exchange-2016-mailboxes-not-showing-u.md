---
title: "Disconnected Exchange 2016 mailboxes not showing up"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/159296/disconnected-exchange-2016-mailboxes-not-showing-u
question_id: 159296
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Disconnected Exchange 2016 mailboxes not showing up

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/159296/disconnected-exchange-2016-mailboxes-not-showing-u (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to migrate several linked mailboxes INTO our main domain. My current process is to:  

Identify the MailDB and GUID of the mailbox to be moved  

Disable the linked mailbox user  

Run Update-StoreMailboxState -Database <MailDB> -Identity <MailGUID> with the database and GUID of the mailbox  

Re-connect the mailbox to the new AD User object.  

However, the disconnected mailbox does not show up for quite some time (several hrs in some tests I've run) which I cannot explain.   

Does anyone have any ideas please?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-12*

Run the following command to ensure if the mailbox exists in the database:    

```
Get-MailboxDatabase | foreach {Get-MailboxStatistics -Database $_.name} | where {$_.DisplayName -eq ""} | Format-List DisplayName,Database,DisconnectReason
```

During which step did you find the mailbox not showing up?     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
