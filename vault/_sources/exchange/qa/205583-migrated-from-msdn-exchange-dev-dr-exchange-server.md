---
title: "[Migrated from MSDN Exchange Dev]DR exchange server in Maintenance mode"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/205583/migrated-from-msdn-exchange-dev-dr-exchange-server
question_id: 205583
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]DR exchange server in Maintenance mode

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/205583/migrated-from-msdn-exchange-dev-dr-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

Hi  

I have one DR exchange server, when I run the cmdlet "get-databaseavailabilitygroup -status |fl"  

serverinmaintenance:DREXG01  

Additional info: I have been executed the below cmdlet  

Set-MailboxServer DREXG01 -DatabaseCopyAutoActivationPolicy Blocked  

is this the reason the server is in maintenance?  

Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-22*

Thank you for the confirmation

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-21*

Hi,    

According to my test, you are right.    

The following is my test result. When I set the parameter of the server E19A'DatabaseCopyAutoActivationPolicy' to "Blocked", I can see that E19A appears in the "ServersInMaintenance" result. After changing "DatabaseCopyAutoActivationPolicy" to the default "Unrestricted", E19A no longer appears in the "ServersInMaintenance" result    

    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
