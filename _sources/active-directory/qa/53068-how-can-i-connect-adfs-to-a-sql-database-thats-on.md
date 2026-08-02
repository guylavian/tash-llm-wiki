---
title: "How can I connect ADFS to a SQL database that's on a different domain?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/53068/how-can-i-connect-adfs-to-a-sql-database-thats-on
question_id: 53068
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-sql-database", "microsoft-security-security-active-directory-federation-services"]
---
# How can I connect ADFS to a SQL database that's on a different domain?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/53068/how-can-i-connect-adfs-to-a-sql-database-thats-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.  

We have 2 domains. The first one contains technical servers, database, etc., the second one contains supporting servers. They can't trust each other (company rules). When configuring ADFS in domain 2, I need to connect to a SQL 2016 database in domain 1. But the ADFS connection uses Windows Authentication and as a result I get an error.  

I create scripts:  

`Export-AdfsDeploymentSQLScript -DestinationFolder "C:\SQLScript" –ServiceAccountName Domain2\ADFS`  

CreateDB.sql works fine, but Set-Permissions.sql completed with errors

Msg 15004, Level 16, State 1, Procedure sp_validname, Line 61, Name cannot be NULL.

I think this is because he didn't find a user with the same sid. Right?  

In SQL script it is like this:

DECLARE hex_account_sid varbinary(85)  

SET hex_account_sid - 0x010500000000000515000000EDF2C8FA8D26A855458E07EB50040000

DECLARE service_account sysname  

SELECT service_account - SUSER_SNAME(hex_account_sid)

I thought it might be possible to create a user with the same sid  

`CREATE LOGIN adfs_service with password - , SID - 0x010500000000000515000000EDF2C8FA8D26A855458E07EB50040000;`  

but got an error

Msg 15419, Supplied parameter sid should be binary(16).

So my question are:  

-  How can I configure ADFS to use SQL authentication?  

or  

-  How can I create the correct permission?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-28*

-   How can I configure ADFS to use SQL authentication?

I have not found any information that AD FS supports other authentication methods - only Integrated Security. In all (in)offical articles AD FS use the credentils for the database connection, which is configured for the AD FS windows service. In my opinion an active directory trust relationship is necessary.
