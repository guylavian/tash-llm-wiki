---
title: "Unable to add 2nd PC to the Domain controller(PC1)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4291711/unable-to-add-2nd-pc-to-the-domain-controller-pc1
question_id: 4291711
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Unable to add 2nd PC to the Domain controller(PC1)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4291711/unable-to-add-2nd-pc-to-the-domain-controller-pc1 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Community, 

I have created two Azure VM's, VM1 installed with windows 2019 datacenter and successfully promoted as DC. 

VM2 installed with same server and when i try to add the VM2 to VM1, received below error. 

Note: This information is intended for a network administrator.   

If you are not your network's administrator, notify the administrator that you received this information, which has been recorded in the file C:\Windows\debug\dcdiag.txt. 

The following error occurred when DNS was queried for the service location (SRV) resource record used to locate an Active Directory Domain Controller (AD DC) for domain "domain name": 

The error was: "DNS name does not exist." 

(error code 0x0000232B RCODE_NAME_ERROR) 

The query was for the SRV record for _ldap._tcp.dc._msdcs.domain name

Common causes of this error include the following: 

-  The DNS SRV records required to locate a AD DC for the domain are not registered in DNS.  

These records are registered with a DNS server automatically when a AD DC is added to a domain.  

They are updated by the AD DC at set intervals. This computer is configured to use DNS servers with the following IP addresses: 

168.63.129.16 

-  One or more of the following zones do not include delegation to its child zone: 

domain name

com 

. (the root  

I can ping VM1 from VM2, 

By default, VM2 assigned with following DNS address "168.63.129.16 ", when i add google dns(8.8.8.8 and 8.8.4.4). Unable to ping VM1 from VM2. 

tried with different version, still same. 

Kindly advise, 

Regards, 

Muralidharan

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-22*

Hello Bill,

This is not for a business purpose. 

I'm learning AD and Exchange, so as part of this trying to create an environment.

Any tips regarding this issue would be great.

Regards, 

Muralidharan

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-22*

Your question is beyond the scope of these Forums

This Community is mainly for home users and their computer problems, not business systems.

The following forum(s) have migrated to Microsoft Q&A: All English Windows Server forums!   

Visit Microsoft Q&A to post new questions.

https://docs.microsoft.com/en-us/answers/products/windows

Windows Server General

-  General

-  Windows Server 2016

-  Windows Server 2019

-  Windows Server 2012

-  Windows Home Server 2011

-  Server Core

-  Nano Server

-  Windows Small Business Server

-  Windows Server Essentials

-  Windows Server Update Services

The Azure forums were at MSDN and TechNet, but:

Those forums have migrated to Microsoft Q&A. Visit Microsoft Q&A to post new questions.

https://docs.microsoft.com/en-us/answers/products/azure?product=all
