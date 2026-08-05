---
title: "2013 MonitoringDiagnosticLogs MSExchangeHMHost logs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1023704/2013-monitoringdiagnosticlogs-msexchangehmhost-log
question_id: 1023704
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# 2013 MonitoringDiagnosticLogs MSExchangeHMHost logs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1023704/2013-monitoringdiagnosticlogs-msexchangehmhost-log (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

Like many users posted and blogged about MonitoringDiagnosticLogs folder created on the D drive of the exchange server 2013 since CU1 we also have this issue.    

https://jaapwesselius.com/2014/01/30/strange-directories-in-exchange-2013-on-d-drive/    

We need to remove drive D from the exchange server, but looking at the D:\MonitoringDiagnosticLogs\MSExchangeHMHost we are seeing current logs.     

We are on CU23    

Is there a way to move the logs to another drive \ folder before we remove the D drive from the system ?    

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-27*

I think it would be easier to redeploy the server and dedicate a partition for Exchange binaries.    

There is much more logging than that, also transport database and IIS logs.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-27*

Hi  @nettech  ,    

According to my search, there is currently no official documentation pointing to any solution or workaround to this situation. It is still an issue.    

I am afraid you cannot move the folder, and when you move the folder, an error may occur and not allow this.    

This issue is also mentioned in the following threads, you could try to stop the Microsoft Exchange Health Manager service and then remove your D drive.    

msexchange-common-event-6003-msexchangehmhost    

move-monitoringdiagnosticlogs-and-transport-role-logs    

Kind Regards!    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
