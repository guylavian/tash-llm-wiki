---
title: "[Migrated from MSDN Exchange Dev] Cannot upgrade Exchange server from CU12 to CU15"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/155943/migrated-from-msdn-exchange-dev-cannot-upgrade-exc
question_id: 155943
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Cannot upgrade Exchange server from CU12 to CU15

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/155943/migrated-from-msdn-exchange-dev-cannot-upgrade-exc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

[MSDN thread link]  Cannot upgrade Exchange server from CU12 to CU15  

I have 1 x exchange server 2016 cu12, 3 x domain controllers ( 2 x 2012R2 version and 1 x 2016 version).  

EXchange server: IP 192.168.1.251  

Domain controller  

IP: 192.168.1.10 (2012R2)  

IP: 192.168.1.16 (2016)  

IP: 192.168.2.21(2012R2)  

192.168.2.21 server can ping our exchange server.  

I would like to upgrade CU12 to CU15, but fail. I found the the error message is  

Setup encountered a problem while validating the state of Active Directory: A native error 0x5B4 occurred while looking for domain controllers in domain "domain name": This operation returned because the timeout period expired  See the Exchange setup log for more information on this error.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-12*

I changed the FSMO Scheme and other role to IP: 192.168.1.16 (2016)  

Then type Setup.exe /preparedomain /IAcceptExchangeServerLicenseTerms,   

After finish it, run the latest CU.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-09*

Hi,    

Please make sure you have met all requests to Upgrade Exchange to the latest Cumulative Update listed in the official document.    

And according to my search, the error 0x5B4 usually occurs when you enable the Failover Cluster feature. If you have enabled that, please remove it temporarily.    

In addition, please use the command below to check the AD settings in your environment:    

```
Get-ADServerSettings | fl
```

As the error says above, check the Exchange setup log to get more detailed information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
