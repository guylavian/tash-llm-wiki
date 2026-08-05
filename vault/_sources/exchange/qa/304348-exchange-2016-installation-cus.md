---
title: "Exchange 2016 installation CUs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/304348/exchange-2016-installation-cus
question_id: 304348
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 installation CUs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/304348/exchange-2016-installation-cus (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, Recently after installing windows update on Windows server 2016, I have come to a weird issue, I have exchange servers 2016 on CU15, due to recent vulnerabilities, I decide to upgrade it to CU19, however when I run the setup, the installation windows suddenly disappears on Organization Preparation 1- 18 steps, it does not throw any error on the screen, it just magically disappear basically, later I found out that it is not only with CU19, I even tried with other older CUs LIKE 16 or 17, it was the result.    

 I have tried to install via PowerShell and CMD the setup was failing on the Organization Preparation stage without throwing any error on the screen also i have tried to run the Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareSchema it completes successfully, however when I run Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAD, it does not and it does not show any error too.      

Please help.    

, ![75504-set.jpg][1] [1]: /api/attachments/75504-set.jpg?platform=QnA     

  the installation is attached below.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-12*

Hi @Khyber Hamid   ,  

Since you have the same problem installing Exchange 2019, and according to the setup log, I found the below error:

03/07/2021 10:55:09.0595 Status code check (d:\dbs\sh\e16df\1126_100440_0\cmd\19\sources\dev\admin\src\libs\ds\x_dob.cxx:3370)  

Error code 0X8000500D (20493): This property can't be found in the cache.

So please following the steps to check if the fsmoroleowner attribute is pointing to a vaild DC. If not, change it manually.

Path: ADSI Edit -> connect to “DC=Forestdnszones,dc=Contoso,dc=com” -> expand “dc=contoso,dc=com” -> check properities of “cn=infrstructure” -> fSMORoleOwner attribute

Then repeat the same operation for “DC=Forestdnszones,dc=Contoso,dc=com”.  

  

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-09*

@Lucas Liu-MSFT       

the PrepareAD does fails, however it does not generate any error on the screen. as mentioned before the exchange installation as soon as it reach to Organization Preparation 1-18 stage, the setup windows terminates itself all the sudden, disappears.     

the replication works fine, i dont see any error between domain controllers, specially when I force replication repadmin / syncall / addep.    

i have restarted exchange servers multiple times, still same result.     

I have even tried to install a new windows server 2019 with Exchange 2019, just wanted to see if the installation goes where it terminates for Exchange 2016, unfortunately it was unexpectedly terminating for the exchange 2019 setup as well on the same stage.     

this is the exchange 2016 setup full logs.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-09*

Hi  

When you run the command to prepare AD and no errors are generated, so what if you judge that prepare failed? The window suddenly disappears or gets stuck？  

When you run the Setup wizard, is it prompted to update page?

1.According to the research on the log information provided by you, no specific error message was found. Do you provide complete log information? If not, share the complete log with us. Please note that please cover your personal information.  

2.I noted that there are two Domain controllers, please make sure that the replication between DCs is normal.  

3.Please try to restart the Exchange server and run the Exchange Setup wizard again.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
