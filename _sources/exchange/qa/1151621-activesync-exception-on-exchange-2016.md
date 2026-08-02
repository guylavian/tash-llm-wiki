---
title: "ActiveSync exception on  Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1151621/activesync-exception-on-exchange-2016
question_id: 1151621
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# ActiveSync exception on  Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1151621/activesync-exception-on-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I get this error on my event after restart IIS.     

I run this two command  for resolve error but error is exist.    

`Get-Mailbox | Set-CasMailbox -ActiveSyncEnabled $False`    

`Get-Mailbox | Set-CasMailbox -ActiveSyncEnabled $True'    

Error:    

Level Date and Time Source Event ID Task Category    

Warning 1/3/2023 11:37:52 AM ASP.NET 4.0.30319.0 1309 Web Event "Event code: 3005     

Event message: An unhandled exception has occurred.     

Event time: 1/3/2023 11:37:52 AM     

Event time (UTC): 1/3/2023 8:07:52 AM     

Event ID: 7c89094cd79849efb70201ca892246f8     

Event sequence: 3     

Event occurrence: 1     

Event detail code: 0     

Application information:     

    Application domain: /LM/W3SVC/2/ROOT/Microsoft-Server-ActiveSync-1-133171417813586892     

    Trust level: Full     

    Application Virtual Path: /Microsoft-Server-ActiveSync     

    Application Path: C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess\sync\     

    Machine name: EX-MB-03     

Process information:     

    Process ID: 17228     

    Process name: w3wp.exe     

    Account name: NT AUTHORITY\SYSTEM     

Exception information:     

    Exception type: ThreadStateException     

    Exception message: Thread has not been started.    

   at System.Threading.Thread.JoinInternal(Int32 millisecondsTimeout)    

   at System.Threading.Thread.Join(TimeSpan timeout)    

   at Microsoft.Exchange.AirSync.Common.NotificationManager.ShutdownNotificationManagerTimerThread()    

   at Microsoft.Exchange.AirSyncHandler.Global.ExecuteApplicationEnd(Object sender, EventArgs e)    

Request information:     

    Request URL:      

    Request path:      

    User host address:      

    User:      

    Is authenticated: False     

    Authentication Type:      

    Thread account name: NT AUTHORITY\SYSTEM     

Thread information:     

    Thread ID: 114     

    Thread account name: NT AUTHORITY\SYSTEM     

    Is impersonating: False     

    Stack trace:    at System.Threading.Thread.JoinInternal(Int32 millisecondsTimeout)    

   at System.Threading.Thread.Join(TimeSpan timeout)    

   at Microsoft.Exchange.AirSync.Common.NotificationManager.ShutdownNotificationManagerTimerThread()    

   at Microsoft.Exchange.AirSyncHandler.Global.ExecuteApplicationEnd(Object sender, EventArgs e)

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2023-01-05*

Hi @Ehsan Rabiee  ,    

Is it causing any activesync issues in your organization?    

Aside from restarting IIS, did you make other changes in your environment?    

Please try recycling the MSExchangeSyncAppPool via IIS manager and see if it can help.    

    

In case the warning persists, I'd suggest restarting the Exchange server out-of-hours to check the result.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
