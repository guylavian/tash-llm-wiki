---
title: "How to find out if my Exchange Hybrid configuration is classic or Modern ."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1058351/how-to-find-out-if-my-exchange-hybrid-configuratio
question_id: 1058351
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# How to find out if my Exchange Hybrid configuration is classic or Modern .

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1058351/how-to-find-out-if-my-exchange-hybrid-configuratio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How can I find out if my Exchange Hybrid configuration is classic or Modern .    

version :Exchange 2016, CU 23    

These are the results from  Get-HybridConfiguration.    

[PS] C:\Windows\system32>Get-HybridConfiguration | fl    

RunspaceId               : **************************    

ClientAccessServers     : {}    

EdgeTransportServers     : {}    

ReceivingTransportServers : {server names}    

SendingTransportServers : {server names}    

OnPremisesSmartHost     : host name    

Domains                 : {domain names}    

Features                 : {FreeBusy, MoveMailbox, Mailtips, MessageTracking, OwaRedirection, OnlineArchive,    

                            SecureMail, Photos}  

ExternalIPAddresses     : {}    

TlsCertificateName       : cert name    

ServiceInstance         : 0    

AdminDisplayName         :    

ExchangeVersion         : 0.20 (15.0.0.0)    

Name                     : Hybrid Configuration    

DistinguishedName       : CN=Hybrid Configuration,CN=Hybrid Configuration,CN=domain ,CN=Microsoft    

                            Exchange,CN=Services,CN=Configuration,DC=dc name  

Identity                 : Hybrid Configuration    

Guid                     : **************************    

ObjectCategory           : domain name/Configuration/Schema/ms-Exch-Coexistence-Relationship    

ObjectClass             : {top, msExchCoexistenceRelationship}    

WhenChanged             : 9/27/2018 4:42:53 PM    

WhenCreated             : 7/20/2017 6:14:52 PM    

WhenChangedUTC           : 9/27/2018 12:42:53 PM    

WhenCreatedUTC           : 7/20/2017 2:14:52 PM    

OrganizationId           :    

Id                       : Hybrid Configuration    

OriginatingServer       : DC name    

IsValid                 : True    

ObjectState             : Unchanged

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-24*

Hi @ESJ  ,    

Agree with the reply above from Andy, you could take a reference at the brief description and comparison about these two modes below:    

Hybrid Agent & Exchange Modern Hybrid now available as a public preview    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
