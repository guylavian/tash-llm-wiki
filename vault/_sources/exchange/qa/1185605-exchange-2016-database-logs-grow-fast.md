---
title: "Exchange 2016 database logs grow fast"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1185605/exchange-2016-database-logs-grow-fast
question_id: 1185605
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 database logs grow fast

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1185605/exchange-2016-database-logs-grow-fast (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All. I hope all is good. I have 4 exchange servers 2016 under one single DAG. 2 exchange servers in the Headquarter exch1 exch2 and 2 servers in the disaster recovery site exch3 and exch4. Also i have 3 databases db1,db2,jr.db1 and db2 are exsiting on all the servers and mounted on exch1, as for jr which is the journal database exist only on exch1 and exch2 and mounted on exch1. The partitions existing on the servers are C drive D drive for the databases L drive for the logs and J drive for the journal which exist only on exch1 and exch2.                                      A space issue existing on C drive for exch1 and 2, 18 GB of free space red zone,as for exch3 and 4 no space issue around 38 GB free space                            for D drive space issue on all the servers 50 GB free  space, red zone.                                                             For L partition which is the dbs transaction logs, i am seeing that recently they grow fast during the week days until a full backup occure on weekend and shrink the logs (basically before the growth was more less)                                                                      for the J partition on exch1 and 2 only the space is good.                                                                             My question is : how to solve the space issue on C drive for both exch1 and exch2 ( the space should not be the same on the servers as they are identical?), second why the databases transaction logs are growing fast than before and is there anyway or there something has triggered the logs to grow?                                                                             NB : i am running out of space on the luns so i don't have the ability to expand any volumes on any server and this is also an issue for me.                                     Many thanks.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-03-02*

Hi @Tony Mourad  ,

My question is : how to solve the space issue on C drive for both exch1 and exch2 ( the space should not be the same on the servers as they are identical?), second why the databases transaction logs are growing fast than before and is there anyway or there something has triggered the logs to grow?

 

For the space issue on C drive on exch1 and exch2, just wondering is there a significant difference on the database file size on each DAG member that holds a copy?

 

About the issue of database transaction logs growing too fast, it could be caused by various factors. First, please run the following command to check if both the active and passive databases are healthy :

```
Get-MailboxDatabaseCopyStatus -Identity "DatabaseName"
```

If the Database is normal, I noticed an article that introduce how to check why the Exchange transaction log is growing rapidly, please refer to: Exchange transaction logs growing rapidly - ALI TAJRAN  

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
