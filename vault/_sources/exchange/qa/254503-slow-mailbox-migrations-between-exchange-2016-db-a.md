---
title: "Slow Mailbox Migrations between Exchange 2016 DB and Exchange 2019 DB"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/254503/slow-mailbox-migrations-between-exchange-2016-db-a
question_id: 254503
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Slow Mailbox Migrations between Exchange 2016 DB and Exchange 2019 DB

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/254503/slow-mailbox-migrations-between-exchange-2016-db-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am in the process of migrating Journal mailboxes from a Exchange 2016 database to a Exchange 2019 database. We are using 10GB network adapters on both Exchange servers and both Exchange servers are on the same switch\network.  

Yet I am experiencing very slow mailbox migrations. (We were using 1GB network adapter for previous migrations and expecting an increase in performance by at least 50%.)  

Is there a known performance issue when migrating mailboxes from Exchange 2016 to Exchange 2019?  

Is there anything I can do to increase performance?  

Please advise.  

Thank you,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-08*

Hi Lou,  

Unfortunately changing the MRS config file had no effect on the performance of the journal Mailbox Migrations.   

I use EAC to launch migrations so using the "priority emergency" as a parameter to new-move in powershell won't work for me. I do occasionally use powershelll do moves but in this case...Its not an emergency and I would hate to bog down our Exchange environment for a non-emergency event.  

Last, the journals are between 400 and 500 gig. I would not want to put that large of mailbox in a PST.   

I have resolved to suffer through the slow migrations. I have 2 journal mailboxes left to process.  

thank you for your advise and recommendations.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-02*

Hi @Catherine Jaszewski   ,    

If the mailboxes you need to migrate are large or the number is so big you may experience the low speed migration. But it is only one reason.    

You can improve the migration speed with these methods:     

- 	Modify the MSExchangeMailboxReplication.exe.config file to increase the values that control the performance.    

It’s in C:\Program Files\Microsoft\Exchange Server\V15\Bin     

Find the MRSConfiguration part, and modify these:    

     

Change them to 50.    

Then scroll down and find:    

 Change it to 10240    

Explanation about these values: Throttling the Mailbox Replication Service    

- 	Use the parameter -priority emergency of the New-MoveRequest:    

New-MoveRequest -Identity user@keyman  .com -TargetDatabase “DB1” -Priority Emergency    

- 	Manually move these mailboxes: export the mailboxes to .pst files and then import them to the new Exchange 2019 server.(As planB)    

Kindly hope these would help you.    

Bests,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
