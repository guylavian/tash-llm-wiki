---
title: "Exchange Hybrid Configuration Wizard succeeds, but doesn't reflect in Admin Centers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2186906/exchange-hybrid-configuration-wizard-succeeds-but
question_id: 2186906
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Exchange Hybrid Configuration Wizard succeeds, but doesn't reflect in Admin Centers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2186906/exchange-hybrid-configuration-wizard-succeeds-but (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

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

Features                  : {FreeBusy, MoveMailbox, Mailtips, MessageTracking, OwaRedirection, OnlineArchive,  

                            SecureMail, Photos}  

ExternalIPAddresses       : {}  

TlsCertificateName        : <I>CN=Go Daddy Secure Certificate Authority - G2, OU=http://certs.godaddy.com/repository/,  

                            O="GoDaddy.com, Inc.", L=Scottsdale, S=Arizona, C=US<S>CN=mail.domain.com  

ServiceInstance           : 0  

AdminDisplayName          :  

ExchangeVersion           : 0.20 (15.0.0.0)  

Name                      : Hybrid Configuration  

DistinguishedName         : CN=Hybrid Configuration,CN=Hybrid Configuration,CN=First Organization,CN=Microsoft  

                            Exchange,CN=Services,CN=Configuration,DC=domain,DC=local  

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

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-20*

Hello,

Thank you for posting in Microsoft Community forum.  

Based on the description, I understand your question is related to Exchange Server.   

Since there are no engineers dedicated to Exchange Server in this forum. In order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.  

Questions - Microsoft Q&A  

Click the "Ask a Question" button in the upper right corner to post your question and select "Exchange Server" tag.

Thank you for your understanding and support.  If you have any question or concern, please feel free to let us know.

Have a nice day.

Best Regards,

Hania Lian
