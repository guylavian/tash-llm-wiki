---
title: "exchange database have automatic switch over"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/263202/exchange-database-have-automatic-switch-over
question_id: 263202
fetched: 2026-07-25
answer_count: 13
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange database have automatic switch over

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/263202/exchange-database-have-automatic-switch-over (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

the event log as below     

A request to mount Active or Passive database was processed in 0.0214939 seconds.          

Flags: 0x00000008           

Error code: NoError (0x00000000)         

Information Store - (47140,R,0,15.01.1779.002)  The database engine has begun replaying logfile E:\Program Files\Microsoft\Exchange Server\V15\Mailbox\database\E04.log.     

Previous Log Processing Stats:     

1 395.168726 -2.929166 (1584) CM +J(CM:1584, PgRf:329433, Rd:3696/31, Dy:3782/520119, Lg:139787869/556120) +M(C:1341976K, Fs:237443, WS:363016K # 348824K, PF:1381028K # 1367372K, P:1381028K).    

Then run a log to copy to E drive     

“Information Store - MBX - Senior01 (47140,R,0,15.01.1779.002) MBX - Senior01: The database engine has begun replaying logfile E:\Program Files\Microsoft\Exchange Server\V15. “    

how to avoid this status , because when failover to other database , around 1 hr the database will auto switch to original database and mounted back     

is it the right not good or other possible reason     

it is too trouble because the status happen the user outlook will no response and hang

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-10*

Get-MailboxDatabaseCopyStatus *      

    

have no failed    

but always show other Exchange B mounted default on Exchange A database     

after 1 hr , Database willauto change back Exchange A mounted , it's too confused     

during switch database , user outlook will hang and email will show disconnect with exchange

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-10*

the copy of database 'XX' on this server appears to be experiencing performance issues, possibly as a result of storage failure. Consult the event log on the server for other storage and "ExchangeStoreDb" events for more specific information about the failure. Recovery was not attempted.  

also happen database auto switch

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-10*

default is 1:00:00

i check have event log

-   Event code: 3005  

    Event message: An unhandled exception has occurred.  

    Event time:  

    Event time  

    Event ID: 42711299724e498d904aae658dfd1ff6

-   Re-delivery of messages from the transport dumpster will be attempted for database . Messages originally delivered between 2/10/2021 and 2/10/2021 3:45:25 AM (UTC) will be re-delivered.

-   Cannot access file, the file is locked or in use [HResult: 0x80131500]. The copier will automatically retry after a short delay.

then auto switch database to server B

how to avoid this status happen

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-10*

how to disable PreferenceMoveFrequency feature   

 and i check C:\ExchangeSetupLogs\DagTasks no location here.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-09*

Hi @Louis Ruth   ,    

Good day!    

What’s the version of your Exchange server?    

If it’s Exchange 2016 CU2 and later version(include Exchange 2019), that could make sense.    

Since after Exchange 2016 CU2, the new property PreferenceMoveFrequency was added:    

     

You could disable this feature with this cmdlet:    

Set-DatabaseAvailabilityGroup -Identity DAG01 -PreferenceMoveFrequency ([System.Threading.Timeout]::InfiniteTimeSpan)    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
