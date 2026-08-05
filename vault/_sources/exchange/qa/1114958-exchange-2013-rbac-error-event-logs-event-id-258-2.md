---
title: "Exchange 2013 RBAC error Event logs Event ID 258, 23, and 16"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1114958/exchange-2013-rbac-error-event-logs-event-id-258-2
question_id: 1114958
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 RBAC error Event logs Event ID 258, 23, and 16

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1114958/exchange-2013-rbac-error-event-logs-event-id-258-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After installing Exchange Server 2013 CU23 in coexistence with Exchange Server 2007 SP3  RU23 DCs Windows 2016 Domain Level = 2012r2 Forest Level = Windows 2003, we are getting the following errors constantly being logged:    

Event ID 258 MSExchange RBAC: RemotePS Public API Func GetApplicationPrivateData throws Exception Microsoft.Exchange.Configuration.Authorization.CmdletAccessDeniedException: The operation couldn't be performed because '<Exchange server object>' couldn't be found    

Event ID 23 MSExchange RBAC: Exchange AuthZPlugin Fails to finish method GetApplicationPrivateData due to application exception Microsoft.Exchange.Configuration.Authorization.CmdletAccessDeniedException: The operation couldn't be performed because '<Exchange server object>' couldn't be found.    

Event ID 16 MSExchange RBAC: RBAC authorization returns Access Denied for user <Exchange server object (SID=S-1-5-21-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx). Reason: User was not found on Domain Controller <DC FQDN>"    

I can't find any references to a solution to this issue anywhere, nor where I should start troubleshooting, so any help would be greatly appreciated.    

I apply RU23-KB4011325 a the issues is the same    

Gaetano    

Thanks,.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-10*

I was able to resolve the Incident by placing the computer object in an OU where group policies were not applied to it. OS Default Polices ware applied     

The Exchange server was in the correct groups, no third-party agents were installed, and the antivirus was uninstalled.    

The issues was originate by GPO Policies    

thanks for your help

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-04*

The problem was caused by group policies applied in several GPOs in Active directory, I have not been able to determine which policy causes the problem.
