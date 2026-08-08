---
title: "Exchange 2013 Mailbox Audit Stopped"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/115312/exchange-2013-mailbox-audit-stopped
question_id: 115312
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 Mailbox Audit Stopped

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/115312/exchange-2013-mailbox-audit-stopped (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Following a server crash on wednesday, i've found that a number of mailboxes that i have auditing enabled on have stopped recording any audit entries.  

I can use the search-mailboxauditlog cmd to pull up the data from prior to the crash but nothing since it was rebooted.  

After the reboot there've been no other issues with the server and no errors showing in logs that i can see either.  

I've tried disabling the auditing and enabling it again but thats not helped.  

Is there a way of purging the log so that it starts again?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-05*

Have you tried the command that Andy posts? Is the mailbox audit working now?  

Does mailbox audit work for new created mailbox? If yes, try to move the old mailboxes to a new database or run a mailbox repair: New-MailboxRepairRequest

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-02*

You can set the audit age log to 0, the run the Folder Assistant    

```
set-mailbox  -AuditLogAgeLimit 00:00:00  

Start-ManagedFolderAssistant 
```

You may need to run that second command (Start-ManagedFolderAssistant <user>)  a few times or let it sit over night    

https://learn.microsoft.com/en-us/powershell/module/exchange/set-mailbox?view=exchange-ps    

For example, to specify 60 days for this parameter, use 60.00:00:00. Setting this parameter to the value 00:00:00 removes all audit log entries for the mailbox. The entries are removed the next time the Managed Folder Assistant processes the mailbox (automatically or manually by running the Start-ManagedFolderAssistant cmdlet).
