---
title: "[Migrated from MSDN Exchange Dev]Microsoft System Attendant on the Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/206841/migrated-from-msdn-exchange-dev-microsoft-system-a
question_id: 206841
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev]Microsoft System Attendant on the Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/206841/migrated-from-msdn-exchange-dev-microsoft-system-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]  

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.  

As the former Outlook forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.

[MSDN Link]  

Microsoft System Attendant on the Exchange 2019

[Original post]  

I'm stucked in the middle of the cross-forest migration from Exchange 2013 to Exchange 2019.

Before migration we have Exchange 2013 CU23 with DAG.  

And installed six servers Exchange 2019 CU7, create DAG, switch access points to a new servers.

Then create new database on 2019 server, and move arbitration mailboxes to it.  

Then move some mailboxes from 2013 to 2019.  

All works fine for a several days.

But now problem is: I can create new databases on 2019, and I can create new mailboxes at the new bases, but I can't access to this mailboxes, and it not receiving emails.

```
Test-ServiceHealth - OK
Get-MailboxDatabaseCopyStatus - OK
```

In the Application EventLog have warnings:

MSExchange Mailbox Replication 1006:  

The Microsoft Exchange Mailbox Replication service was unable to process jobs in a mailbox database.  

Database: DAG_DB2  

Error: MapiExceptionNoSupport: Unable to open message store. (hr=0x80040102, ec=-2147221246)  

Diagnostic context:  

Lid: 55847 EMSMDBPOOL.EcPoolSessionDoRpc called [length=149]  

Lid: 43559 EMSMDBPOOL.EcPoolSessionDoRpc returned [ec=0x0][length=494][latency=49]  

Lid: 52176 ClientVersion: 15.2.721.2  

Lid: 50032 ServerVersion: 15.2.721.6002  

Lid: 35180  

Lid: 23226 --- ROP Parse Start ---  

Lid: 27962 ROP: ropLogon [254]  

Lid: 17082 ROP Error: 0x80040102  

Lid: 26937  

Lid: 21921 StoreEc: 0x80040102  

Lid: 27962 ROP: ropExtendedError [250]  

Lid: 1494 ---- Remote Context Beg ----  

Lid: 1238 Remote Context Overflow  

Lid: 55098 StoreEc: 0x80070005  

Lid: 46872 StoreEc: 0x80070005 PropTag: 0x669B0014  

Lid: 55098 StoreEc: 0x80070005  

Lid: 59418 dwParam: 0x79  

Lid: 34842 dwParam: 0x79  

Lid: 59418 dwParam: 0x79  

Lid: 34842 dwParam: 0x79  

Lid: 59418 dwParam: 0x79  

Lid: 34842 dwParam: 0x79  

Lid: 59418 dwParam: 0x79  

Lid: 34842 dwParam: 0x79  

Lid: 59418 dwParam: 0x79  

Lid: 34842 dwParam: 0x79  

Lid: 44106 StoreEc: 0x80040102  

Lid: 56872 dwParam: 0xFE  

Lid: 42712 StoreEc: 0x80040102  

Lid: 45434 Guid: 980645aa-5d54-434b-98df-49a5cd728669  

Lid: 10786 dwParam: 0x0 Msg: 15.02.0721.002:ExchSrv2:e43c253f-8d00-4126-bed8-7c9a14db7de6  

Lid: 1750 ---- Remote Context End ----  

Lid: 27962 ROP: ropGetPropsSpecific [7]  

Lid: 26881  

Lid: 21817 ROP Failure: 0x80040102  

Lid: 46042 StoreEc: 0x80040102  

Lid: 32441  

Lid: 1706 StoreEc: 0x80040102  

Lid: 24761  

Lid: 20665 StoreEc: 0x80040102  

Lid: 25785  

Lid: 29881 StoreEc: 0x80040102

[PS] C:\>Test-MAPIConnectivity -Database DAG_DB2 -Verbose |fl Error

Error : [Microsoft.Exchange.Data.Storage.NoSupportException]: Cannot open mailbox /o=MyOrg/ou=Exchange Administrative Group (FYDIBOHF23SPDLT)/cn=Configuration/c  

n=Servers/cn=ExchSrv2/cn=Microsoft System Attendant. There is no support for this operation. Inner error [Microsoft.Mapi.MapiExceptionNoSupport]: M  

apiExceptionNoSupport: Unable to open message store. (hr=0x80040102, ec=-2147221246)  

Diagnostic context:  

Lid: 55847 EMSMDBPOOL.EcPoolSessionDoRpc called [length=180]  

Lid: 43559 EMSMDBPOOL.EcPoolSessionDoRpc returned [ec=0x0][length=494][latency=40]  

Lid: 52176 ClientVersion: 15.2.721.2  

Lid: 50032 ServerVersion: 15.2.721.6002  

Lid: 35180  

Lid: 23226 --- ROP Parse Start ---  

Lid: 27962 ROP: ropLogon [254]  

Lid: 17082 ROP Error: 0x80040102  

Lid: 26937  

Lid: 21921 StoreEc: 0x80040102  

Lid: 27962 ROP: ropExtendedError [250]  

Lid: 1494 ---- Remote Context Beg ----  

Lid: 1238 Remote Context Overflow  

Lid: 55098 StoreEc: 0x80070005  

Lid: 46872 StoreEc: 0x80070005 PropTag: 0x669B0014  

Lid: 55098 StoreEc: 0x80070005  

Lid: 59418 dwParam: 0x79  

Lid: 34842 dwParam: 0x79  

Lid: 59418 dwParam: 0x79  

Lid: 34842 dwParam: 0x79  

Lid: 59418 dwParam: 0x79  

Lid: 34842 dwParam: 0x79  

Lid: 59418 dwParam: 0x79  

Lid: 34842 dwParam: 0x79  

Lid: 59418 dwParam: 0x79  

Lid: 34842 dwParam: 0x79  

Lid: 44106 StoreEc: 0x80040102  

Lid: 56872 dwParam: 0xFE  

Lid: 42712 StoreEc: 0x80040102  

Lid: 45434 Guid: 668ee38d-5b39-4664-9948-f2384aaffbd0  

Lid: 10786 dwParam: 0x0 Msg: 15.02.0721.002:ExchSrv2:ae9f69e6-f095-46ef-b05b-803a52d08c57  

Lid: 1750 ---- Remote Context End ----  

Lid: 27962 ROP: ropGetPropsSpecific [7]  

Lid: 26881  

Lid: 21817 ROP Failure: 0x80040102  

Lid: 46042 StoreEc: 0x80040102  

Lid: 32441  

Lid: 1706 StoreEc: 0x80040102  

Lid: 24761  

Lid: 20665 StoreEc: 0x80040102  

Lid: 25785  

Lid: 29881 StoreEc: 0x80040102

OWA access for a new user on the new database failed:

```
A problem occurred while you were trying to use your mailbox. 
X-ClientId: 37C37BB90BD443DFAF1D2A66CBB4D379
request-id d9e98815-85bc-4f8a-b390-afffb579e9c5
X-OWA-Error Microsoft.Exchange.Data.Storage.NoSupportException
X-OWA-Version 15.2.721.2
X-FEServer EXCHSRV1
X-BEServer EXCHSRV2
Date:4/29/2019 7:42:53 AM
InnerException: Microsoft.Mapi.MapiExceptionNoSupport
```

This errors affecting ONLY new databases, old databases on the 2013/2019 versions are working fine.

By googling Internet, I found than th Exchange 2019 is not using SYstem Attendant Service, and no need to check homeDB attribute.

Why it's happened and how to fix it?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-22*

Hi,    

Here is a thread in a similar situation.    

Errors working with Databases. Microsoft.Mapi.MapiExceptionNoSupport: MapiExceptionNoSupport: Unable to open message store    

According to MicahHow's reply,please try enabling MAPI over HTTP at the Organization level and recreate the databases.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
