---
title: "EXCHANGE SERVER 2010 Database issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1181319/exchange-server-2010-database-issue
question_id: 1181319
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
---
# EXCHANGE SERVER 2010 Database issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1181319/exchange-server-2010-database-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We had an exchange server 2010 installed on our domain.  Due to some issues WHILE TRYING TO UPGRADE IT TO 2016 the mailbox role got removed and all of its entries from active directory aswell.  Although we have a backup of whole mailbox server but since AD schema has been changed on all domain controllers,  we can't restore it.     Now the issue is that i have created a new mailbox server role and i want to attach my mailbox database from the previous server to the new server. But since the old mailbox server is not available i am failing to attach it to the new server.  I tried creating a new database on the new server with the same name as of the old one  so that i can copy the database file to that location but it says the name is already in use.  Is there any way that i can connect my old database as it has all the user mailboxes and emails in it.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-17*

Hi @Usama A. Rub ,

I'm sorry that Microsoft no longer supports Exchange 2010, so I could only give some advice. You could upgrade your Exchange server as soon as possible to continue to receive support from Microsoft.

What do you mean "AD schema has been changed on all domain controllers"? How did you perform the backup? If you are using the backup method supported by Microsoft, then you could create a new Exchange 2010 environment and import the database.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
