---
title: "Exchange 2016 CU18 HealthManagerHeartbeatProbe \"failed by design\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/265556/exchange-2016-cu18-healthmanagerheartbeatprobe-fai
question_id: 265556
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 CU18 HealthManagerHeartbeatProbe "failed by design"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/265556/exchange-2016-cu18-healthmanagerheartbeatprobe-fai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a new 2016 CU18 environment (6 servers on Windows 2012 R2) as we finally look to migrate off of 2010 SP3. When running a Get-HealthReport against the 6 servers, we've got one server reporting Monitoring is unhealthy.  

```
CurrentHealthSetState   : NotApplicable
Name                    : HealthManagerWorkItemQuarantineMonitor
TargetResource          :
HealthSetName           : Monitoring
HealthGroupName         : ServiceComponents
AlertValue              : Unhealthy
FirstAlertObservedTime  : 2/8/2021 11:15:57 AM
Description             :
IsHaImpacting           : False
RecurranceInterval      : 0
DefinitionCreatedTime   : 2/9/2021 8:44:07 AM
HealthSetDescription    :
ServerComponentName     : None
LastTransitionTime      : 2/8/2021 11:15:57 AM
LastExecutionTime       : 2/9/2021 8:44:08 AM
LastExecutionResult     : Succeeded
ResultId                : 5013189
WorkItemId              : 1628252781
IsStale                 : False
Error                   :
Exception               :
IsNotified              : False
LastFailedProbeId       : -1
LastFailedProbeResultId : -1
ServicePriority         : 0
Identity                : Monitoring\HealthManagerWorkItemQuarantineMonitor\
IsValid                 : True
ObjectState             : New
```

When I run Invoke-MonitoringProbe monitoring\HealthManagerHeartbeatProbe against the server, we get a failed by design error. Is this accurate? Wondering why we don't see this on all 6 servers?  

```
MonitorIdentity    : monitoring\HealthManagerHeartbeatProbe
RequestId          : 658baf57-fbfa-40d2-b5fc-a91ff64ef092
ExecutionStartTime : 2/9/2021 2:08:09 PM
ExecutionEndTime   : 2/9/2021 2:08:09 PM
Error              : Failed by design.
Exception          : System.Exception: Failed by design.
                        at Microsoft.Office.Datacenter.ActiveMonitoring.TestActiveMonitoringProbe.DoWork(CancellationToken cancellationToken)
                        at System.Threading.Tasks.Task.Execute()
                     --- End of stack trace from previous location where exception was thrown ---
                        at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
                        at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
                        at Microsoft.Office.Datacenter.WorkerTaskFramework.WorkItem.d__b.MoveNext()
                     --- End of stack trace from previous location where exception was thrown ---
                        at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
                        at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
                        at Microsoft.Office.Datacenter.WorkerTaskFramework.WorkItem.d__7.MoveNext()
```

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-10*

I do get the same 'failed by design' when invoking the probe on a healthy server, so that answers that part of it.  I did find this early yesterday in the Monitoring event log. However after being in an unhealthy state since Thursday, it now shows healthy today (and ActiveSync is now unhealthy on this server, going through that remediation now).  

Are there steps we can do to address this error below with Event ID 4 in Microsoft-Exchange-ManagedAvailability/Monitoring?  

Workitem "E4EAppPool.Maintenance.Workitem" (ID: 688275914) has been poisoned repeatedly. As a consequence, the workitem has been quarantined and will not be scheduled to run for 24 hours. Notice that poison results are normally caused by workitem timeouts. Please investigate.  

States of all health sets:  

Note: Data may be stale. To get current data, run: Get-HealthReport -Identity 'ServerName'  

State               HealthSet                     AlertValue     LastTransitionTime       MonitorCount          

Unknown             Unknown                       Unknown        1/1/0001 12:00:00 AM     1                     

Note: Subsequent detected alerts are suppressed until the health set is healthy again.
