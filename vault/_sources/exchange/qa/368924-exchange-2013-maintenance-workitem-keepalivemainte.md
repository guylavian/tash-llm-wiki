---
title: "Exchange 2013: Maintenance workitem \"KeepAliveMaintenance\" (ID: 120) has failed."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/368924/exchange-2013-maintenance-workitem-keepalivemainte
question_id: 368924
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013: Maintenance workitem "KeepAliveMaintenance" (ID: 120) has failed.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/368924/exchange-2013-maintenance-workitem-keepalivemainte (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, after installation KB5001779 on Exchange 2013 CU23 error occurred  

Alert description: Maintenance workitem "KeepAliveMaintenance" (ID: 120) has failed. Health Manager has detected it is either set to run once and failed, or has been failing consistently. Maintenance workitem failure could cause monitoring gap and should be investigated.  

The error message from the last result is:  

Microsoft.Exchange.Monitoring.ActiveMonitoring.Local.EndpointManagerEndpointUninitializedException: Endpoint type 'Microsoft.Exchange.Monitoring.ActiveMonitoring.Common.MonitoringEndpoint' has not been initialized. Make sure the endpoint is enabled in its definition, and that it has executed successfully.  

at Microsoft.Exchange.Monitoring.ActiveMonitoring.Common.LocalEndpointManager.GetEndpoint(Type type, Boolean throwIfEndpointContainsException)  

at Microsoft.Exchange.Monitoring.ActiveMonitoring.Common.LocalEndpointManager.get_MonitoringEndpoint()  

at Microsoft.Exchange.Monitoring.ActiveMonitoring.ActiveMonitoring.KeepAliveMaintenance.DoWork(CancellationToken cancellationToken)  

at Microsoft.Office.Datacenter.WorkerTaskFramework.WorkItem.Execute(CancellationToken joinedToken)  

at Microsoft.Office.Datacenter.WorkerTaskFramework.WorkItem.<>c__DisplayClass2.<StartExecuting>b__0()  

at System.Threading.Tasks.Task.Execute()  

What could be the problem ?  

When I run the script HealthChecker everything is fine except  

TCP/IP Settings: Not Set  

Error: Without this value the KeepAliveTime defaults to two hours, which can cause connectivity and perf ormance issues between network devices such as firewalls and load balancers depending on their configuration.  

More details: https://techcommunity.microsoft.com/t5/Exchange-Team-Blog/Checklist-for-troubleshooting-Outlook-connectivity-in-Exchange/ba-p/604792

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-26*

Hi @Klimko Vasiliy      

Did you encounter any connectivity issue after installing the security update? Or you are facing any other issue?    

For the connectivity issue, we could use the ExRCA tool to get detailed information: https://testconnectivity.microsoft.com/tests/exchange    

What's the configuration of your TCP/IP settings for your Exchange server, like DNS...    

A related article introduces about TCP/IP KeepAlive, Session Timeout, RPC Timeout, Exchange, Outlook and you for your reference as well.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
