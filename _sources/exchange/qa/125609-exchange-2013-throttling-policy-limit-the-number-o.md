---
title: "Exchange 2013 - Throttling Policy Limit the number of Internet messages a user can send a day"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/125609/exchange-2013-throttling-policy-limit-the-number-o
question_id: 125609
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 - Throttling Policy Limit the number of Internet messages a user can send a day

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/125609/exchange-2013-throttling-policy-limit-the-number-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

My environment : Exchange 2013 CU23 , 3 servers (mailbox + CAS roles) , 1000 users , 7 mailbox databases .  

I want to create a Throttling Policy limit the number of Internet messages a user can send a day : 500 and apply it to all users , including the newly created in future. Is below policy ok ?  

```
New-ThrottlingPolicy -Name LimitMessagesSent -RecipientRateLimit 500 -ThrottlingPolicyScope Organization
```

If I want to exclude some special user cases , I should create another Throttling Policy with scope regular and assign it to them ? Can I do as below ?  

```
New-ThrottlingPolicy -Name NoLimitMessagesSent -RecipientRateLimit Unlimited/1000 -ThrottlingPolicyScope Regular

Set-Mailbox -Identity user_alias -ThrottlingPolicy NoLimitMessagesSent
```

The order would be Regular > Organization > Global ? How about between regular policies ?  

Can I assign many regular throttling policies for a user ?  

There is a default global scope Throttling Policy exists , can I remove it ?  

```
Get-ThrottlingPolicy

Name                                    ThrottlingPolicyScope                   IsServiceAccount
----                                    ---------------------                   ----------------
GlobalThrottlingPolicy_0b04ec59-1b03... Global                                  False

RunspaceId                                  : 242150ca-4b46-4420-94e3-c6c97921ce8e
ThrottlingPolicyScope                       : Global
IsServiceAccount                            : False
AnonymousMaxConcurrency                     : 1
AnonymousMaxBurst                           : 120000
AnonymousRechargeRate                       : 420000
AnonymousCutoffBalance                      : 720000
EasMaxConcurrency                           : 10
EasMaxBurst                                 : 480000
EasRechargeRate                             : 1800000
EasCutoffBalance                            : 600000
EasMaxDevices                               : 100
EasMaxDeviceDeletesPerMonth                 : Unlimited
EasMaxInactivityForDeviceCleanup            : Unlimited
EwsMaxConcurrency                           : 27
EwsMaxBurst                                 : 300000
EwsRechargeRate                             : 900000
EwsCutoffBalance                            : 3000000
EwsMaxSubscriptions                         : 5000
ImapMaxConcurrency                          : Unlimited
ImapMaxBurst                                : 3600000
ImapRechargeRate                            : 600000
ImapCutoffBalance                           : Unlimited
OutlookServiceMaxConcurrency                : 27
OutlookServiceMaxBurst                      : 300000
OutlookServiceRechargeRate                  : 900000
OutlookServiceCutoffBalance                 : 3000000
OutlookServiceMaxSubscriptions              : 5000
OutlookServiceMaxSocketConnectionsPerDevice : 4
OutlookServiceMaxSocketConnectionsPerUser   : 12
OwaMaxConcurrency                           : 20
OwaMaxBurst                                 : 480000
OwaRechargeRate                             : 1800000
OwaCutoffBalance                            : Unlimited
OwaVoiceMaxConcurrency                      : 3
OwaVoiceMaxBurst                            : 75000
OwaVoiceRechargeRate                        : 375000
OwaVoiceCutoffBalance                       : 525000
PopMaxConcurrency                           : 20
PopMaxBurst                                 : 3600000
PopRechargeRate                             : 600000
PopCutoffBalance                            : Unlimited
PowerShellMaxConcurrency                    : 18
PowerShellMaxBurst                          : Unlimited
PowerShellRechargeRate                      : Unlimited
PowerShellCutoffBalance                     : Unlimited
PowerShellMaxTenantConcurrency              : Unlimited
PowerShellMaxOperations                     : Unlimited
PowerShellMaxCmdletsTimePeriod              : Unlimited
ExchangeMaxCmdlets                          : Unlimited
PowerShellMaxCmdletQueueDepth               : Unlimited
PowerShellMaxDestructiveCmdlets             : Unlimited
PowerShellMaxDestructiveCmdletsTimePeriod   : Unlimited
PowerShellMaxCmdlets                        : Unlimited
PowerShellMaxRunspaces                      : Unlimited
PowerShellMaxTenantRunspaces                : Unlimited
PowerShellMaxRunspacesTimePeriod            : Unlimited
PswsMaxConcurrency                          : 18
PswsMaxRequest                              : Unlimited
PswsMaxRequestTimePeriod                    : Unlimited
RcaMaxConcurrency                           : 40
RcaMaxBurst                                 : 150000
RcaRechargeRate                             : 900000
RcaCutoffBalance                            : Unlimited
CpaMaxConcurrency                           : 20
CpaMaxBurst                                 : Unlimited
CpaRechargeRate                             : Unlimited
CpaCutoffBalance                            : Unlimited
MessageRateLimit                            : Unlimited
RecipientRateLimit                          : Unlimited
ForwardeeLimit                              : Unlimited
DiscoveryMaxConcurrency                     : 2
DiscoveryMaxMailboxes                       : 5000
DiscoveryMaxKeywords                        : 500
DiscoveryMaxPreviewSearchMailboxes          : 5000
DiscoveryMaxStatsSearchMailboxes            : 100
DiscoveryPreviewSearchResultsPageSize       : 200
DiscoveryMaxKeywordsPerPage                 : 25
DiscoveryMaxRefinerResults                  : 10
DiscoveryMaxSearchQueueDepth                : 32
DiscoverySearchTimeoutPeriod                : 10
PushNotificationMaxConcurrency              : 20
PushNotificationMaxBurst                    : Unlimited
PushNotificationRechargeRate                : Unlimited
PushNotificationCutoffBalance               : Unlimited
PushNotificationMaxBurstPerDevice           : 10
PushNotificationRechargeRatePerDevice       : 6
PushNotificationSamplingPeriodPerDevice     : 600000
EncryptionSenderMaxConcurrency              : 200
EncryptionSenderMaxBurst                    : 4800000
EncryptionSenderRechargeRate                : 18000000
EncryptionSenderCutoffBalance               : Unlimited
EncryptionRecipientMaxConcurrency           : 20
EncryptionRecipientMaxBurst                 : 480000
EncryptionRecipientRechargeRate             : 1800000
EncryptionRecipientCutoffBalance            : Unlimited
ComplianceMaxExpansionDGRecipients          : 10000
ComplianceMaxExpansionNestedDGs             : 25
IsLegacyDefault                             : False
Diagnostics                                 :
AdminDisplayName                            :
ExchangeVersion                             : 0.20 (15.0.0.0)
Name                                        : GlobalThrottlingPolicy_0b04ec59-1b03-4a89-a87f-160b7b45945c
DistinguishedName                           : CN=GlobalThrottlingPolicy_0b04ec59-1b03-4a89-a87f-160b7b45945c,CN=Global
                                              Settings,CN=First Organization,CN=Microsoft
                                              Exchange,CN=Services,CN=Configuration,DC=mydomain,DC=com
Identity                                    : GlobalThrottlingPolicy_0b04ec59-1b03-4a89-a87f-160b7b45945c
Guid                                        : 936d132b-30c6-48c8-a97a-8b8bf4e6d4cb
ObjectCategory                              : mydomain.com/Configuration/Schema/ms-Exch-Throttling-Policy
ObjectClass                                 : {top, msExchGenericPolicy, msExchThrottlingPolicy}
WhenChanged                                 : 6/18/2018 8:15:17 PM
WhenCreated                                 : 3/19/2013 2:32:05 PM
WhenChangedUTC                              : 6/18/2018 1:15:17 PM
WhenCreatedUTC                              : 3/19/2013 7:32:05 AM
OrganizationId                              :
Id                                          : GlobalThrottlingPolicy_0b04ec59-1b03-4a89-a87f-160b7b45945c
OriginatingServer                           : ex.mydomain.com
IsValid                                     : True
ObjectState                                 : Changed
```

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-10-14*

The RecipientRateLimit policy applies to ALL messages, not just internet messages. It includes internal messages as well, so I would be very careful if you want to really implement this,    

-RecipientRateLimit    

The RecipientRateLimit parameter specifies the limits on the number of recipients that a user can address in a 24-hour period.    

https://learn.microsoft.com/en-us/powershell/module/exchange/set-throttlingpolicy?view=exchange-ps    

You do not need mess with the default policy or remove it.     

Create any new policies and apply one of them to a mailbox.     

You can only apply one policy per mailbox.    

Any mailbox without a specific policy applied uses the default policy so leave that be.    

https://learn.microsoft.com/en-us/Exchange/server-health/workload-management?view=exchserver-2019#scopes-in-user-workload-settings    

I would not worry about setting the scopes. Simply create a custom throttling policy if required and apply to the mailboxes you want it to.    

Then the rest will just use the default policy.
