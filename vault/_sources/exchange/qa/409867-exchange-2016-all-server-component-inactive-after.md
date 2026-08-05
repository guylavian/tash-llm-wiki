---
title: "exchange 2016 all server component inactive after install cu20"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/409867/exchange-2016-all-server-component-inactive-after
question_id: 409867
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# exchange 2016 all server component inactive after install cu20

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/409867/exchange-2016-all-server-component-inactive-after (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear     

I had read many similar question and Google.    

I install cu20 on exchange 2016 cu7. But fail at Step 14 of 18: Mailbox role: Mailbox service. main error message as below.    

```
" was run: "System.InvalidOperationException: Failed to mount database "FFFFF Database". Error: An Active Manager operation failed. Error: The database action failed. Error: Database 'FFFFF Database' on server 'FFFF-EX01' cannot be mounted due to a previous error: At '11/29/2020 12:46:25 AM' the Exchange store database 'FFFFF Database' copy on this server appears to be inconsistent with the active database copy or is corrupted. For more details about the failure, consult the Event log on the server for other storage and "ExchangeStoreDb" events. A successful failover restored service.
```

I restore snapshot that before install, but problem had not gone. When I login ECP, after first login page, server return "HTTP error 500" with link https://domain/owa/auth.owa    

I found all service component inactive. I reference below link to reactive but nothing change.    

Would you please help if you have idea?    

Thanks for your valuable time.    

https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/requestor-changed-server-component    

Best Regards.    

Scott Gao

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-27*

Hi,    

Please let me know, do you want to solve the ECP issue or migration issue in this thread? So that we could focus on one of it.    

Can you open OWA now?  We could try recreating ECP/OWA virtual directory: https://theitbros.com/recreate-owa-ecp-virtual-directories-exchange-server-2016/    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Do you have a DAG? Test-Replicationhealth is normally used to check replication or Active Manager health in a DAG.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-26*

Hi @Scott Gao   ,    

Please note that upgrading Exchange 2016 CU7 to CU20 is a big step. Could you provide more information to identify the cause.    

Have you installed and verified the pre-requisites for CU20 as the .NET framework version requirements are different for both CU's.     

Did you put the servers in maintenance mode before upgrading?    

Are you able to login using https://localhost/ecp on the server?     

Are you getting the login page? HTTP 500 occurs before or after entering the credentials?    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019#microsoft-net-framework
