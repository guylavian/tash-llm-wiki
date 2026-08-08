---
title: "HCW ERROR: Timeout 504 when try to migrate Exchange Server 2019 to Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1507968/hcw-error-timeout-504-when-try-to-migrate-exchange
question_id: 1507968
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# HCW ERROR: Timeout 504 when try to migrate Exchange Server 2019 to Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1507968/hcw-error-timeout-504-when-try-to-migrate-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our company is trying to migrate from OnPrime to OnLine our email services. We are using Hybrid migration wizard, when i clicked over Finish button i got the error, see image bellow.

Reviewing the log I found the following:

```
{ErrorDetail=Microsoft.Exchange.Migration.MigrationServerConnectionFailedException: The connection to the server 'ceb7d730-8fec-40b6-ac37-f7840d8349e5.resource.mailboxmigration.his.msappproxy.net' could not be completed. ---> Microsoft.Exchange.MailboxReplicationService.MRSRemoteTransientException: The call to 'https://ceb7d730-8fec-40b6-ac37-f7840d8349e5.resource.mailboxmigration.his.msappproxy.net/EWS/mrsproxy.svc' timed out. Error details: The request channel timed out while waiting for a reply after 00:00:09.9994290. Increase the timeout value passed to the call to Request or increase the SendTimeout value on the Binding. The time allotted to this operation may have been a portion of a longer timeout. --> The remote server returned an error: (504) Gateway Timeout. --> The remote server returned an error: (504) Gateway Timeout. ---> Microsoft.Exchange.MailboxReplicationService.MRSRemotePer
                                      manentException: The request channel timed out while waiting for a reply after 00:00:09.9994290. Increase the timeout value passed to the call to Request or increase the SendTimeout value on the Binding. The time allotted to this operation may have been a portion of a longer timeout. ---> Microsoft.Exchange.MailboxReplicationService.MRSRemotePermanentException: The remote server returned an error: (504) Gateway Timeout. ---> Microsoft.Exchange.MailboxReplicationService.MRSRemotePermanentException: The remote server returned an error: (504) Gateway Timeout.    --- End of inner exception stack trace ---    --- End of inner exception stack trace ---    --- End of inner exception stack trace ---    at Microsoft.Exchange.MailboxReplicationService.MailboxReplicationServiceFault.ReconstructAndThrow(String serverName, VersionInformation serverVersion)    at Microsoft.Exchange.Connections.Common.WcfCli
                                      entWithFaultHandling`2.<>c__DisplayClass4_0.b__0()    at Microsoft.Exchange.Net.WcfClientBase`1.CallService(Action serviceCall, String context)    at Microsoft.Exchange.Connections.Common.WcfClientWithFaultHandling`2.CallService(Action serviceCall, String context)    at Microsoft.Exchange.MailboxReplicationService.WcfClientWithVersion`2.CallService(Action serviceCall, String context)    at Microsoft.Exchange.Migration.MigrationExchangeProxyRpcClient.CanConnectToMrsProxy(Fqdn serverName, Guid mbxGuid, NetworkCredential credentials, LocalizedException& error)    --- End of inner exception stack trace ---    at Microsoft.Exchange.Migration.MigrationEndpointVerifier.VerifyConnectivity(MigrationEndpointBase endpoint)    at Microsoft.Exchange.Management.Migration.MigrationService.Endpoint.TestMigrationServerAvailability.InternalProcessEndpoint(Boolean fromAutoDiscover) IsValid=True Mess
                                      age=The connection to the server 'ceb7d730-8fec-40b6-ac37-f7840d8349e5.resource.mailboxmigration.his.msappproxy.net' could not be completed. Result=Failed SupportsCutover=False}
```

Mrsproxy is enable in our local exchange server, i can reach our mrsproxy remotely and i can auntheticated too, i disabled and renable the mrsproxy and try again and all the time i got the same error. someone has been the same error and maybe could share the solution please.
Regards
Indalecio Trujillo

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-01-23*

To resolve this issue, consider adjusting the timeout values in the relevant migration configuration settings by increasing the timeout value in the Request call or changing the Binding's SendTimeout. Additionally, checking network conditions and server responsiveness may aid in resolving the timeout issue.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-01-23*

Hi @Indalecio Trujillo  ，

From the error logs, it looks like an issue which might be related to network configuration.   

Just wondering is there any firewall running on your on-prem Exchange servers? If so, it's suggested to temporarily disabling them and rerun HCW to check how it goes.  

You can also follow the instructions in the link below to verify the connectivity between Exchange 2019 and Exchange Online by downloading the sample script and running `Test-HybridConnectivity -TestO365Endpoints`.  

Verify connectivity

Moreover, noted in the thread below that a "(504) Gateway Timeout" error in HCW was finally resolved by disabling IPV6, so I assume you can have a go on your end as well and see if it can help.  

HCW Error 8078   

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
