---
title: "MECM 2107 Violation of PRIMARY KEY constraint 'CI_DocumentStore_PK'. Cannot insert duplicate key in object 'dbo.CI_DocumentStore"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1009283/mecm-2107-violation-of-primary-key-constraint-ci-d
question_id: 1009283
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-intune-configuration-manager-updates"]
---
# MECM 2107 Violation of PRIMARY KEY constraint 'CI_DocumentStore_PK'. Cannot insert duplicate key in object 'dbo.CI_DocumentStore

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1009283/mecm-2107-violation-of-primary-key-constraint-ci-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

There was a problem, when synchronizing SUP updates, MECM 2107 tries to create an entry with an already existing Document_ID in the database (PRIMARY KEY 'CI_DocumentStore_PK').    

***** [23000][2627][Microsoft][SQL Server Native Client 11.0][SQL Server]Violation of PRIMARY KEY constraint 'CI_DocumentStore_PK'. Cannot insert duplicate key in object 'dbo.CI_DocumentStore'. The duplicate key value is (16777216). SMS_WSUS_SYNC_MANAGER**    

Makes several attempts until the value 16777224 (all of these Document_IDs already exist in the database) after which the WSUS synchronization ends with the error "Too many consecutive failures. Aborting sync." In this case, the last Document_ID = 33561329 in the dbo.CI_DocumentStore table .    

Why is MECM trying to set the Document_ID = 16777216 to an already existing one, and not as it was before the order number 33561330 ? Who has any ideas about this?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-16*

We have made some progress on this issue.  

Wrong identity seed for Document_ID is set as a result of spCheckReseedIdentity stored procedure.

A simple test to verify this:

DBCC CHECKIDENT('CI_DocumentStore');  

Checking identity information: current identity value '16777215', current column value '33563054'.

Next, we performed RESEED:

DBCC CHECKIDENT('CI_DocumentStore', RESEED);  

Checking identity information: current identity value '33563054', current column value '33563054'.

After that, update synchronization was launched and at that moment the spCheckReseedIdentity stored procedure replaced the identity seed with what is already in use

*Microsoft SQL Server reported SQL message 50000, severity 15: [42000][50000][Microsoft][SQL Server Native Client 11.0][SQL Server]ERROR : The following table(s) had incorrect identity seed, but it has been fixed. CI_DocumentStore, : spCheckReseedIdentity

DBCC CHECKIDENT('CI_DocumentStore');  

Checking identity information: current identity value '16777215', current column value '33563054'.*

At this time, in the wsyncmgr.log:

Synchronizing update 9ddb3360-dad9-47c3-b4ba-734fd2edbcc4 - Security Intelligence Update for Microsoft Endpoint Protection - KB2461484 (Version 1.375.378.0)
insert into CI_DocumentStore (DocumentIdentifier, Body, IsVersionLatest, DocumentType) values ​​('fb7298f9-c957-43cf-b2b5-b937fd40d9ea', '', 0, 0)~;select SCOPE_IDENTITY()  

[23000][2627][Microsoft][SQL Server Native Client 11.0][SQL Server]Violation of PRIMARY KEY constraint 'CI_DocumentStore_PK'. Cannot insert duplicate key in object 'dbo.CI_DocumentStore'. The duplicate key value is (16777216).  

Failed to sync update 9ddb3360-dad9-47c3-b4ba-734fd2edbcc4. Error: Failed to save update fb7298f9-c957-43cf-b2b5-b937fd40d9ea. CCISource error: -1. Source: Microsoft.SystemsManagementServer.SoftwareUpdatesManagement.UpdatesManager.UpdatesManagerClass.DefineUpdate

You can make sure that this is really the result of executing the spCheckReseedIdentity stored procedure by running it after RESEED

DECLARE @return  _value int  

EXEC @return  _value = [dbo].[spCheckReseedIdentity]  

SELECT 'ReturnValue' = @return  _value

Interestingly, the stored procedure uses the dbo.fnGetSiteRangeEnd function:

"ALTER function [dbo].fnGetSiteRangeEnd returns int with SCHEMABINDING as begin return 16777215 end"

What to do with it? How to solve this problem? I would appreciate any help on this issue.
