---
title: "Export user mailbox to PST after Exchange 2013 restore to different AD domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/237530/export-user-mailbox-to-pst-after-exchange-2013-res
question_id: 237530
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Export user mailbox to PST after Exchange 2013 restore to different AD domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/237530/export-user-mailbox-to-pst-after-exchange-2013-res (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,  

One of our resources deleted mails of previous 3 months from the user web mail. Since only one user affected so we decided to restore the backup from tape, We configured a new test environment to restore the DB. The backup was available on Tape. The DB was restored successfully but there was no users found in the new Exchange EAC nor in the new Active Directory.  

After the restoration completed the user mailboxes were found in the disabled state and when i try to connect them from EAC it shows an error that no matching user found which is obvious as the source and destination Active Directory domains are different. I have created a new user in the test environment but no luck.  

Please share is it possible to connect the disabled mailbox, export the content in the PST.  

Many Thanks  

Kashif Saeed

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-21*

Have you checked if those mails can be recovered directly? Read the following articles and run the command to check:    

Recoverable Items folder in Exchange Server    

Search for and recover missing items    

Otherwise, you should try to recover it on your main server, this blog for your reference: Restoring Exchange Server 2016 Mailboxes and Items Using a Recovery Database    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
