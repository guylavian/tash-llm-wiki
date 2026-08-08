---
title: "Exchange 2013 find disabled/ deleted mailbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/397768/exchange-2013-find-disabled-deleted-mailbox
question_id: 397768
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2013 find disabled/ deleted mailbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/397768/exchange-2013-find-disabled-deleted-mailbox (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need help in finding whether a user mailbox was disabled or deleted as I can’t find it in the admin console.  

Also how to I find whether our exchange is configured to auto deletion after 30 day

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-05-18*

Hi @Anonymous  ,    

I need help in finding whether a user mailbox was disabled or deleted as I can’t find it in the admin console.    

You can open EAC, go to Recipients > Mailboxes, click the More(...) button, choose Connect Mailbox, check if the missing user mailbox is listed there:    

    

    

An alternative is to running the command below to identify the disabled mailboxes in your organization, then you can see if the mailbox is included in the output:    

```
Get-MailboxDatabase | foreach {Get-MailboxStatistics -Database $_.DistinguishedName} | where {$_.DisconnectReason -eq "Disabled"} | Format-Table DisplayName,Database,DisconnectDate
```

    

Note: By default a disconnected mailbox is permanently deleted (purged) in 30 days(based on the MailboxRetention property value for the mailbox database), so we would not be able to find the user mailbox if it was disabled/deleted more than 30 days ago.     

For more information about disconnected mailbox, you may refer to: Disconnected mailboxes.    

As regards to your concern about whether your exchange is configured to auto deletion after 30 day, are you referring to the the deleted mailbox retention period mentioned earlier? If this is the case, you may check the Keep deleted mailboxes for (days) setting of the database:    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-17*

-  You can check or adjust settings for mailbox retention by reviewing this article https://learn.microsoft.com/en-us/exchange/policy-and-compliance/mrm/apply-retention-policies-to-mailboxes?view=exchserver-2019    

-  Another article telling you how to recover https://learn.microsoft.com/en-us/exchange/recipients/disconnected-mailboxes/restore-deleted-mailboxes?view=exchserver-2019    

-  If the above dont help and you have an offline copy/backup of the database you can use our DigiScope product to open the offline EDB to see if its still available within the EDB    

Search, Recover, & Extract Mailboxes, Folders, & Email Items from Offline Exchange Mailbox and Public Folder EDB's and Live Exchange Servers or Import/Migrate direct from Offline EDB to Any Production Exchange Server, even cross version i.e. 2003 --> 2007 --> 2010 --> 2013 --> 2016 --> 2019 --> Exchange Online with Lucid8's DigiScope
