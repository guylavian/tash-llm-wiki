---
title: "Exchange 2016 Test-ReplicationHealth - DatabaseAvailability FAILED"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/287972/exchange-2016-test-replicationhealth-databaseavail
question_id: 287972
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 Test-ReplicationHealth - DatabaseAvailability FAILED

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/287972/exchange-2016-test-replicationhealth-databaseavail (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm not sure why I'm having a failure with this command.    

    

The database is healthy and mounted on the server which shows the error above    

    

When I look at further databasecopy status output, I see the failure there too and the last check passed date is a long time ago.    

    

The HighAvailability component is running.    

    

We have two nodes in each of our two sites and we have Intrasite Activation mode enabled.  Automatic failover of the databases during patching and other maintenance works fine.     

I'm not sure what to do to fix this.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-27*

Even with Unrestricted turn on, I still see this on the servers in the one datacenter where we see the problem

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-27*

Toggling Unrestricted on resolved the issue, however when I toggle IntrasiteOnly back on, the error returns.  It's odd that the warning is only for the databases that are active at one datacenter but not the copies that are active in the other datacenter.  I toggled it back to Unrestricted for now.  I'm going to give it a little more time to see if Active Manager needs to do some other checks.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-26*

Thanks @KyleXu-MSFT   .  I will try that on one of the databases and let you know how it goes.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-26*

@Hollisorama      

The error is mainly caused by "-DatabaseCopyAutoActivationPolicy" set to "IntrasiteOnly". I think there may exist issue with the communication between mounted active database and passive database.    

I would suggest you set it to "Unrestricted", then use "Update-MailboxDatabaseCopy -Identity DB1\MBX1" to make sure all database copy is update to data, then change the "DatabaseCopyAutoActivationPolicy" back to "IntrasiteOnly".    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
