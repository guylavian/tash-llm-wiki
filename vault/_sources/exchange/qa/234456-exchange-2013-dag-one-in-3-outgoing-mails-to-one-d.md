---
title: "Exchange 2013 DAG: One in 3 outgoing mails to one domain  bounced and stuck in queue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/234456/exchange-2013-dag-one-in-3-outgoing-mails-to-one-d
question_id: 234456
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 DAG: One in 3 outgoing mails to one domain  bounced and stuck in queue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/234456/exchange-2013-dag-one-in-3-outgoing-mails-to-one-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Environment: Hosted DAG Exchange 2013 environment   

One in about 3 outgoing mails to one specific domain get stuck in the queue.   

I don't know why this is.  

The domain uses ipv4  / ipv6 mx records and i thought it would be because of ipv6 but when i hardcode their mx records on the dc of the environment, it still manages to resolve the ipv6 mx-record? We do use external dns forwarders but isn't there a method to force ipv4 usage ? disabling ipv6 in registry + disable ip helper service didn't help, it still resolves the ipv6 address for the mx record of the domain having the issue  

```
Logs:

RunspaceId : 779ae3c8-728b-4078-aa88-1e8b7f3d0b43

DeliveryType : DnsConnectorDelivery

NextHopDomain : destination.com

TlsDomain :

NextHopConnector : 137c0a63-cbc7-4261-b49b-b4850e63593b

Status : Retry

MessageCount : 1

LastError : [{LRT=15-01-21 23:50:05};{LED=450 4.7.0 Proxy session setup failed on Frontend with '451 4.4.0 Primary target IP address responded with: "451 4.4.0 Security

status InvalidToken." Attempted failover to alternate host, but that did not succeed. Either there are no alternate hosts, or delivery failed to all alternate

hosts. The last endpoint attempted was 2a0X:3cXX:XX2:XXX::XX00:25'};{FQDN=MAILSERVER.DOMAIN.LOCAL};{IP=192.168.12.4}]

RetryCount : 17

LastRetryTime : 15-01-21 23:50:05

NextRetryTime : 16-01-21 00:00:05

FirstRetryTime : 15-01-21 22:06:02

DeferredMessageCount : 0

LockedMessageCount : 0

MessageCountsPerPriority : {0, 0, 0, 0}

DeferredMessageCountsPerPriority : {0, 1, 0, 0}

RiskLevel : Normal

OutboundIPPool : 0

NextHopCategory : External

IncomingRate : 0

OutgoingRate : 0

Velocity : 0

OverrideSource :

QueueIdentity : DAGSERVER5\322120

PriorityDescriptions : {High, Normal, Low, None}

Identity : DAGSERVER5\322120

IsValid : True

ObjectState : New

MESSAGE TRACKING LOGS

RunspaceId : 779ae3c8-728b-4078-aa88-1e8b7f3d0b43

Timestamp : 15-01-21 22:06:01

ServerHostname : DAGSERVER5

SourceContext : DAGSERVER50.domain.local=250 2.6.0 d6b4ad351482463aa4ec2fcc9211e93e@DAGSERVERIL08.domain.local [InternalId=DAGSERVER50.domain.local, Hostname=190735202648087] Queued mail for

redundancy

Source : SMTP

EventId : HAREDIRECT

InternalMessageId : 293969036574747

MessageId : d6b4ad351482463aa4ec2fcc9211e93e@DAGSERVER50.domain.local

Recipients : {******@destination.com}

RecipientStatus : {}

TotalBytes : 19535

RecipientCount : 1

RelatedRecipientAddress :

Reference :

MessageSubject : FW: forward mail test

Sender : sender@domain.local

ReturnPath : sender@domain.local

Directionality : Originating

MessageLatencyType : None

EventData : {[DeliveryPriority, Normal], [AccountForest, domain.local]}

RunspaceId : 779ae3c-4078-aa88-1e8b7f3d0b43

Timestamp : 15-01-21 22:06:01

ClientIp : 192.168.12.8

ClientHostname : DAGSERVER50.domain.local

ServerIp : 192.168.12.5

ServerHostname : DAGSERVER5

SourceContext : 08D8B9F10FA;2021-01-15T21:06:01.371Z;0

ConnectorId : DAGSERVER5\Default DAGSERVER5

Source : SMTP

EventId : RECEIVE

InternalMessageId : 293969036574747

MessageId : d6b4ad351482@DAGSERVER08.domain.local

Recipients : {******@destination.com}

RecipientStatus : {}

TotalBytes : 19535

RecipientCount : 1

MessageSubject : FW: forward mail test

Sender : sender@domain.local

ReturnPath : sender@domain.local

Directionality : Originating

OriginalClientIp : x.x.x.x

MessageInfo : 0cI:

MessageLatencyType : None

EventData : {[FirstForestHop, DAGSERVER5.domain.local], [DeliveryPriority, Normal], [AccountForest, domain.local]}

RunspaceId : 779ae3c8-728b-4078-aa88-1e8b7f3d0b43

Timestamp : 15-01-21 22:06:01

ClientHostname : DAGSERVER5

Source : AGENT

EventId : AGENTINFO

InternalMessageId : 293969036574747

MessageId : d6b4ad351482463aa4ec2fcc9211e93e@DAG08.domain.local

Recipients : {******@destination.com}

RecipientStatus : {}

TotalBytes : 23425

RecipientCount : 1

RelatedRecipientAddress :

MessageSubject : FW: forward mail test

Sender : sender@domain.local

ReturnPath : sender@domain.local

Directionality : Originating

OriginalClientIp : x.x.x.x

MessageLatencyType : None

EventData : {[CompCost, |ETR=0], [DeliveryPriority, Normal], [AccountForest, domain.local]}

RunspaceId : 779ae3c8-728b-4078-aa88-1e8b7f3d0b43

Timestamp : 15-01-21 22:06:02

ServerHostname : DAGSERVER5

SourceContext : ContentConversion

Source : ROUTING

EventId : TRANSFER

InternalMessageId : 293969036574748

MessageId : d6b4ad351482463aa4ec2fcc9211e93e@DAG08.domain.local

Recipients : {******@destination.com}

TotalBytes : 19697

RecipientCount : 1

RelatedRecipientAddress :

Reference : {293969036574747}

MessageSubject : FW: forward mail test

Sender : sender@domain.local

ReturnPath : sender@domain.local

EventData : {[DeliveryPriority, Normal], [AccountForest, domain.local]}
```

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-19*

Hi,    

Is any third-party anti-spam/virus tool installed on that server? Try disabling the tool temporarily and sending again.    

Run Get-SendConnector| fl on all servers and check if any settings on problematic is different?    

Try creating a send connector via powershell like "New-SendConnector -Name 1 -AddressSpaces domain.com" with:    

-   -ForceHELO $true    

-  -UseExternalDNSServersEnabled $true    

Restart the Transport service and test if it works.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
