---
title: "Error enabling federation trust in HCW on Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1844683/error-enabling-federation-trust-in-hcw-on-exchange
question_id: 1844683
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Error enabling federation trust in HCW on Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1844683/error-enabling-federation-trust-in-hcw-on-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Microsoft ,

We are in the process of configuration of the HCW on Exchange 2016 servers which are in DAG.

Overall, the environment contains 3 Exchange 2010 and 2 Exchange 2016 servers.

We followed the prerequisites and enabled MRS proxy on 2016 servers and started the HCW

The HCW is giving errors while Enabling the Federation Trust

'New-FederationTrust': Unable to access the Federation Metadata document from the federation partner. Detailed information: "The underlying connection was closed: An unexpected error occurred on a send.". {CategoryInfo={Activity=[System.String] New-FederationTrust,Category=[System.Management.Automation.ErrorCategory] MetadataError,Reason=[System.String] FederationMetadataException,TargetName=[System.String] ,TargetType=[System.String] },ErrorDetails=,Exception=[System.Management.Automation.RemoteException] Unable to access the Federation Metadata document from the federation partner. Detailed information: "The underlying connection was closed: An unexpected error occurred on a send.".,FullyQualifiedErrorId=[System.String] [Server=XXXVEXCH02,RequestId=7684efde-a476-4d97-8db6-63728c919af7,TimeStamp=7/26/2024 12:54:14 PM] [FailureCategory=Cmdlet-FederationMetadataException] A280C284,Microsoft                                       .Exchange.Management.SystemConfigurationTasks.NewFederationTrust}

We tried rebooting the server didnt help

We tried HCW on another 2016 in DAG but that also gave the same error.

We tried manually enabling the trust through PowerShell gave an error.

Need Help how to resolve this and proceed ahead with HCW.

Regards,

Irfan Mapkar

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2024-07-28*

Ensure you have TLS 1.2 enabled on the Exchange Servers

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-tls-configuration?view=exchserver-2019
