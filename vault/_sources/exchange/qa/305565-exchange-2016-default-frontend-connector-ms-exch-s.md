---
title: "Exchange 2016: Default Frontend Connector - \"Ms-Exch-SMTP-Accept-Any-Recipient\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/305565/exchange-2016-default-frontend-connector-ms-exch-s
question_id: 305565
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016: Default Frontend Connector - "Ms-Exch-SMTP-Accept-Any-Recipient"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/305565/exchange-2016-default-frontend-connector-ms-exch-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We've recently patched our Exchange servers, after the patch we received complaints that some of our applications were unable to send to external recipients. (the patch might not be the cause but it is the only recent change that was done on Exchange)  

I've used telnet to check the sending to external recipients and received the following error:  

550 5.7.54 SMTP; Unable to relay recipient in non-accepted domain                                                       451 4.7.0 Timeout waiting for client input  

The application mail flow is: APP/User -> Exchange Load Balancer IP -> Exchange Auto Mapped IP -> Exchange IP -> Mail Gateway  

I've escalated the issue to our Support and he modified the default frontend connector by the command below.  

Get-ReceiveConnector "Default Frontend" | Add-ADPermission -User "NT AUTHORITY\ANONYMOUS LOGON" -ExtendedRights "Ms-Exch-SMTP-Accept-Any-Recipient"  

After that emails were sent with no issue. but this seems to me like a security concern as the default frontend connector is acting as open relay. ( I know I shouldn't have modified the default receive connector but there so many calls accompanied by verbal abuse to solve the issue as soon as possible )  

After some googling I read that you shouldn't remove the Ms-Exch-SMTP-Accept-Any-Recipient as it will not accept any emails coming from internet.  

Here are the connector settings:  

AuthMechanism                             : Tls, Integrated, BasicAuth, BasicAuthRequireTLS, ExchangeServer  

Banner                                    :  

BinaryMimeEnabled                         : True  

Bindings                                  : {[::]:25, 0.0.0.0:25}  

ChunkingEnabled                           : True  

DefaultDomain                             :  

DeliveryStatusNotificationEnabled         : True  

EightBitMimeEnabled                       : True  

SmtpUtf8Enabled                           : True  

BareLinefeedRejectionEnabled              : False  

DomainSecureEnabled                       : False  

EnhancedStatusCodesEnabled                : True  

LongAddressesEnabled                      : False  

OrarEnabled                               : False  

SuppressXAnonymousTls                     : False  

ProxyEnabled                              : False  

AdvertiseClientSettings                   : False  

Fqdn                                      : LON-EX01.Constoso.local  

ServiceDiscoveryFqdn                      :  

Enabled                                   : True  

ConnectionTimeout                         : 00:10:00  

ConnectionInactivityTimeout               : 00:05:00  

MessageRateLimit                          : Unlimited  

MessageRateSource                         : IPAddress  

MaxInboundConnection                      : 5000  

MaxInboundConnectionPerSource             : 20  

MaxInboundConnectionPercentagePerSource   : 2  

MaxHeaderSize                             : 256 KB (262,144 bytes)  

MaxHopCount                               : 60  

MaxLocalHopCount                          : 5  

MaxLogonFailures                          : 3  

MaxMessageSize                            : 36 MB (37,748,736 bytes)  

MaxProtocolErrors                         : 5  

MaxRecipientsPerMessage                   : 200  

PermissionGroups                          : AnonymousUsers, ExchangeServers, ExchangeLegacyServers, Custom  

PipeliningEnabled                         : True  

ProtocolLoggingLevel                      : None  

RemoteIPRanges                            : {::-ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff, 0.0.0.0-255.255.255.255}  

RequireEHLODomain                         : False  

RequireTLS                                : False  

EnableAuthGSSAPI                          : False  

ExtendedProtectionPolicy                  : None  

LiveCredentialEnabled                     : False  

Server                                    : LON-EX01  

TransportRole                             : FrontendTransport  

RejectReservedTopLevelRecipientDomains    : False  

RejectReservedSecondLevelRecipientDomains : False  

RejectSingleLabelRecipientDomains         : False  

AcceptConsumerMail                        : False  

SizeEnabled                               : Enabled  

TarpitInterval                            : 00:00:05  

AuthTarpitInterval                        : 00:00:05  

MaxAcknowledgementDelay                   : 00:00:30  

ExchangeVersion                           : 0.1 (8.0.535.0)  

Name                                      : Default Frontend LON-EX01  

OriginatingServer                         : LON-DC01  

IsValid                                   : True  

ObjectState                               : Unchanged  

Need your guidance as I don't know where to go from here..  

Thank you and I apologize for the lengthy question. ^_^'

## Answers

_No answers on this thread._
