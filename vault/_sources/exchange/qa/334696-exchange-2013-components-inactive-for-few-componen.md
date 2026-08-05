---
title: "Exchange 2013 components inactive for few components in one of the DAG member"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/334696/exchange-2013-components-inactive-for-few-componen
question_id: 334696
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 components inactive for few components in one of the DAG member

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/334696/exchange-2013-components-inactive-for-few-componen (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi;  

I am running DAG on two Exchange 2013 servers, EX1 and EX2.  I tried to apply CU23 but it failed and after roll backup to previous backup, I spotted some components is "inactive" on EX1 but EX2 is all "active", I also tried to run this command   

"Set-ServerComponentState EX1 -Component AutoDiscoverProxy -State Active -Requester Functional"  

for bring the "AutoDiscoveryProxy" up but no help.  What can I do?  I check the distribution of my mailbox database, they looks fine.  

I also run these commands.  

"$Requesters = Get-ServerComponentstate –Identity $Computer -Component ServerWideOffline"  

"$Requesters.LocalStates"  

The result is..  

Requester      State     Timestamp                       Component  

Functional     Active    3/28/2021 9:20:57 AM    ServerWideOffline  

Maintenance Active    3/28/2021 9:18:24 AM    ServerWideOffline  

I am wondering if the EX1 is still in maintenance state because when I run  

"$Requesters = Get-ServerComponentstate –Identity EX2 -Component ServerWideOffline", the result is "Functional"  

when I run "$Requesters = Get-ServerComponentstate –Identity EX1 -Component ServerWideOffline", the result is "Maintenance"  

Please help me to troubleshoot the issue.  Many thanks!  

Component                     State  

ServerWideOffline           Active  

HubTransport                  Active  

FrontendTransport          Active  

Monitoring                     Active  

RecoveryActionsEnabled       Active  

AutoDiscoverProxy          Inactive  

ActiveSyncProxy              Inactive  

EcpProxy                         Active  

EwsProxy                         Inactive  

ImapProxy                      Active  

OabProxy                       Inactive  

OwaProxy                      Active  

PopProxy                       Active  

PushNotificationsProxy       Active  

RpsProxy                      Active  

RwsProxy                     Active  

RpcProxy                     Inactive  

UMCallRouter                 Active  

XropProxy                       Active  

HttpProxyAvailabilityGroup   Active  

ForwardSyncDaemon            Active  

ProvisioningRps              Active  

MapiProxy                      Inactive  

EdgeTransport                Active  

HighAvailability             Active  

SharedCache                  Active

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-29*

Hi;  

this is the result....  

[PS] D:\PS1scripts>(Get-ServerComponentState -Identity EX1 -Component ServerWideOffline).LocalStates  

Requester                              State       Timestamp                                    Component  

Functional                              Active     3/28/2021 9:20:57 AM                  ServerWideOffline  

Maintenance                          Active     3/28/2021 9:18:24 AM                  ServerWideOffline
