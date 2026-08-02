---
title: "How to Setup AutoDiscover for TWO Exchange Server 2016(CU19) For Lab Environment as local Network"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/320835/how-to-setup-autodiscover-for-two-exchange-server
question_id: 320835
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# How to Setup AutoDiscover for TWO Exchange Server 2016(CU19) For Lab Environment as local Network

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/320835/how-to-setup-autodiscover-for-two-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,

My Current Infra

1-Primary Domain Controller  

1-Secondary Domain Controller + File Server

2-RODC

2 Child Domain

1 Exchange Server 2016 (CU19)

DB01  

DB02

I am trying to Search article for Step by Step Moving Existing Exchange Server2016(01) To New Exchange Server 2016(02) with in same Domain (TestLab) Internal Network

I want to migrate Exch2016-01(CU19)Old to Exch2016-02(CU19)New with in the same Domain

Once installed. New exchange . need to be decommission the Exch2016-01(CU19)

Steps that i need

1)How to Install New Exchange Exch2016-02(CU19) in the same organization

2) How to Move Database, Rules, How it is created in Exch2016-01(CU19) same

3) How to decommission the Exch2016-01(CU19)

Next

Now i am having two Exchange Server. as Test Lab only internal access (Not External Access)  

Exch2016-01  

Exch2016-02

Issue:-  

Getting certificate alert  

Users are not able to connect Outlook and Phones

What could be the reason?  

How to fix. i think related to Autodiscover?  

It can be use internal to connect Autodiscover with network PCs and Mobiles

Two Cases  

1)How to Merge Two Exchange Server's Autodiscover

2) Before decommission How to point secondary Exchange with AutoDiscover

Please advise

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-19*

@Sathishkumar Singh       

This issue isn't related with Autodiscover, in a coexist lab, you just need to one autodiscover record. About the connection issue, it is related with the virtual directories configuration on your Exchange server. About the certificate issue, it is related with the service URL and the subject that contained in your certificate.    

Could you provided detail information about the certificate error? It will help us to narrow down this issue.    

I also suggest you provide those information below to us:    

```
Get-OutlookAnywhere | Select Server,InternalHostName,ExternalHostName  
  
Get-MAPIVirtualDirectory | Select Server,InternalURL,ExternalURL   
  
Get-OABVirtualDirectory | Select Server,InternalURL,ExternalURL  
  
Get-WebServicesVirtualDirectory | Select Server,InternalURL,ExternalURL  
  
Get-ClientAccessServer | Select Name,AutoDiscoverServiceInternalUri  
  
Get-OWAVirtualDirectory | Select Server,InternalURL,ExternalURL  
  
Get-ECPVirtualDirectory | Select Server,InternalURL,ExternalURL  
  
Get-ActiveSyncVirtualDirectory | Select Server,InternalURL,ExternalURL  
  
Get-PowerShellVirtualDirectory | Select Server,InternalURL,ExternalURL   
  
Get-ExchangeCertificate | fl Subject,CertificateDomains,Services
```

I would also suggest you create a new mailbox on this new Exchange server, then check the look up step from Outlook "Test Email Autoconfiguration", those information will help us to know the detailed information in your organization and help you to narrow down it.    

Remember remove privacy information before posting result on this forum.     

This tool also useful to you: Exchange Deployment Assistant    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
