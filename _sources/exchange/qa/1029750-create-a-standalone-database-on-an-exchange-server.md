---
title: "create a Standalone Database on an exchange server that is a DAG member"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1029750/create-a-standalone-database-on-an-exchange-server
question_id: 1029750
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# create a Standalone Database on an exchange server that is a DAG member

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1029750/create-a-standalone-database-on-an-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want to create a standalone database on an existing Exchange server that has circular logging enabled and doesn't need to be a member of a DAG. Microsoft suggests building another Exchange Server that isn't a member of the DAG. However back in the days of Exchange 2010 we could have a Standalone Database that wasn't a member of the DAG.  I am hoping that there is a nice quick and easy way to do this without being a member of the DAG or having to build another Exchange Server and pay for more licenses.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-07*

Hi @Bryan Clark  ,    

Yes, as Andy said, you could create a database on a member server of the DAG, but do not add any copies of the database.    

Besides, why would you want to enable circular logging on the database?      

We do not recommend enabling circular logging on Mailbox servers.    

If you need to back up the database, you could disable circular logging before doing this.    

For information on how to disable circular logging using EAC or PowerShell, refer to the following article:    

disable-circular-logging-exchange    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

For circular logging and backups, please refer to this: Exchange Circular Logging and VSS Backups - Microsoft Tech Community    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-30*

You can do this, just create the database, mount it and do not add any copies to any other mailbox servers in the DAG. No need to build another server.
