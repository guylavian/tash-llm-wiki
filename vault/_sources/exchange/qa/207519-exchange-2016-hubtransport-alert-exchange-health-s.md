---
title: "Exchange 2016. HubTransport. Alert: Exchange Health Set. Messages.failed.to.be.made.redundant.Monitor -Unhealthy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/207519/exchange-2016-hubtransport-alert-exchange-health-s
question_id: 207519
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016. HubTransport. Alert: Exchange Health Set. Messages.failed.to.be.made.redundant.Monitor -Unhealthy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/207519/exchange-2016-hubtransport-alert-exchange-health-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi team,    

Got alert message from SCOM, telling:    

Alert: Exchange Health Set    

Source: MYSERVER - HubTransport    

Path: MYSERVER; MYSERVER    

Last modified by: System    

Last modified time: 12/22/2020 5:08:57 PM Alert description: The total number of messages rejected due to shadow failure over the last 60 minutes exceeds 200    

States of all monitors within the health set:    

Note: Data may be stale. To get current data, run: Get-ServerHealth -Identity 'MYSERVER' -HealthSet 'HubTransport'    

When I run this command in Exchange Management shell, I get:    

```
[PS] C:\WINDOWS\system32>Get-ServerHealth -Identity 'MYSERVER' -HealthSet 'HubTransport' | select name, alertvalue  
  
Name                                                        AlertValue  
----                                                        ----------  
**Messages.failed.to.be.made.redundant.Monitor                 Unhealthy**
```

Guys, instructions here:    

https://learn.microsoft.com/en-us/exchange/management/health/troubleshooting-hubtransport-health-set?redirectedfrom=MSDN    

says, that I have to rerun Probe. But there is no Probe for this Monitor.    

(none (notification or check) - HubTransport - Messages.failed.to.be.made.redundant.Monitor)    

Please assist, how to fix this Critical alert.

## Answers

_No answers on this thread._
