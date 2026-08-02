---
title: "Exchange Hybrid Configuration Wizard succeeds, but doesn't reflect in Admin Centers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2149282/exchange-hybrid-configuration-wizard-succeeds-but
question_id: 2149282
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Hybrid Configuration Wizard succeeds, but doesn't reflect in Admin Centers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2149282/exchange-hybrid-configuration-wizard-succeeds-but (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone.

Having an odd problem here. We successfully ran the Exchange Hybrid Configuration Wizard after a few errors and some troubleshooting. The wizard now completes with no errors, however when accessing the Exchange Server Admin Center and going to the Hybrid tab, it still just prompts to begin the setup again. We have run the wizard multiple times and it works perfectly every time, however no Hybrid setup reflects on-prem or in M365.

Get-HybridConfiguration outputs the below results (edited for confidentiality) 

[PS] C:\Windows\system32>get-hybridconfiguration

 

 

RunspaceId                : ######################### 

ClientAccessServers       : {} 

EdgeTransportServers      : {} 

ReceivingTransportServers : {EXSERVER} 

SendingTransportServers   : {EXSERVER} 

OnPremisesSmartHost       : mail.domain.com 

Domains                   : {domain.com} 

Features                  : {FreeBusy, MoveMailbox, Mailtips, MessageTracking, OwaRedirection, OnlineArchive,                             SecureMail, Photos} 

ExternalIPAddresses       : {} 

TlsCertificateName        : <I>CN=Go Daddy Secure Certificate Authority - G2, OU=[http://certs.godaddy.com/repository/],                             O="GoDaddy.com, Inc.", L=Scottsdale, S=Arizona, C=US<S>CN=mail.domain.com 

ServiceInstance           : 0 

AdminDisplayName          : 

ExchangeVersion           : 0.20 (15.0.0.0) 

Name                      : Hybrid Configuration 

DistinguishedName         : CN=Hybrid Configuration,CN=Hybrid Configuration,CN=First Organization,CN=Microsoft                             Exchange,CN=Services,CN=Configuration,DC=domain,DC=local 

Identity                  : Hybrid Configuration 

Guid                      : ############################## 

ObjectCategory            : domain.local/Configuration/Schema/ms-Exch-Coexistence-Relationship 

ObjectClass               : {top, msExchCoexistenceRelationship} 

WhenChanged               : 1/17/2025 4:37:31 PM 

WhenCreated               : 1/14/2025 12:33:31 PM 

WhenChangedUTC            : 1/17/2025 12:37:31 PM 

WhenCreatedUTC            : 1/14/2025 8:33:31 AM 

OrganizationId            : 

Id                        : Hybrid Configuration 

OriginatingServer         : DC02.domain.local 

IsValid                   : True 

ObjectState               : Unchanged

Scratching my head about this one because the wizard clears everything fine, and PowerShell seems to be telling me that the Hybrid setup is configured, however there's no Hybrid services available. Any advice appreciated, thanks.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-21*

Hello, @Jeremy S,

Welcome to the Microsoft Q&A platform!

Based on your description, you have run into an issue where the Hybrid Configuration Wizard (HCW) completes successfully, but its changes do not seem to be reflected in the Exchange Admin Center (EAC) or in your hybrid setup.

To solve this issue, please follow the regular troubleshooting below.

First, ensure that the hybrid configuration is recognized by both the on-premises environment and the Microsoft 365 portal by checking the status in the Microsoft 365 admin center. Additionally, make sure that the Hybrid Configuration object is correctly set up, and that the certificates for secure mail transport are properly installed on all Internet-facing Exchange servers. 

Besides, verify that the account used to run the HCW has appropriate permissions in both environments and ensure your firewall and network configurations allow inbound access to the Autodiscover and Exchange Web Services (EWS) endpoints on the on-premises Exchange servers. Reviewing your event logs, clearing your browser cache, or accessing the EAC from a different browser might also help.

Moreover, try using the Hybrid Configuration Diagnostic tool available through the Microsoft 365 support and recovery assistant for more insights into any configuration issues. It might also help to force a synchronization between your on-premises Active Directory and Azure AD using Azure AD Connect. Re-run the HCW with elevated permissions (Run as Administrator) to ensure there are no missed steps. 

Official document for reference: Troubleshoot a hybrid deployment | Microsoft Learn.

Should you need more help on this, you can feel free to post back. 

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.

Best Wishes,

Alex Zhang
