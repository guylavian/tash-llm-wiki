---
title: "Exchange 2019 CPU on MSExchangeServicesAppPool"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1151459/exchange-2019-cpu-on-msexchangeservicesapppool
question_id: 1151459
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management", "windows-development-iis"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2019 CPU on MSExchangeServicesAppPool

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1151459/exchange-2019-cpu-on-msexchangeservicesapppool (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We have been on Exchange 2019 for over a year now.  In the last month, we have noticed some high CPU usage increase happening.  We are running it in VMWare ESXi 7 on Windows Server 2019.  We were initially running it with 4 cores.  We've now bumped it up to 8.  NUMA is active on ESXi hosts.  Memory is good and it rarely goes above 60%.      

What i've discovered is that one of the culprits is the w3wp.exe process (iis).  In Task Manager, when I add the Command Line column, I can see where w3wp.exe has this:      

C:\windows\system32\inetsrv\w3wp.exe -ap "MSExchangeServicesAppPool" -v "v4.0" -c "C:\Program Files\Microsoft\Exchange Server\V15\bin\GenericAppPoolConfigWithGCServerEnabledFalse.config" -a \.\pipe\iisipmb(some guid) -h ""C:\inetpub\temp\apppools\MSExchangeServicesAppPool\MSExchangeServicesAppPool.config"" -w """" -m 0    

I can't read the inetpub\temp\apppool\ config file.  I can look at the GenericAppPoolConfigWithGCServerEnabledFalse.config as well as the MSExchangeServicesAppPool_CLRConfig.config.      

I noticed there are other w3wp app pools that also look to the GenericAppPoolConfigWithGCServerEnabledFalse.config file.  All this file has is GCServerEnabled = false which it appears to have something to do with Garbage Collection.  The MSExchangeServicesAppPool_CLRConfig.config DOES have GCServerEnabled set to TRUE.      

So i'm not sure exactly what's going on here and if there is actual Garbage Collecting happening or not.  1 config file says it does, the other does not.  I know this may not answer the performance question, but I wanted to find out if anyone else has had to investigate this and seen anything similar in their Exchange environment?  And are there any recommended tweaks to any of these files that should be done?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-09*

Hi @Jonathan Berg   ,    

You could still use the Debug Diagnostics Tool to troubleshoot high CPU usage by a process in IIS    

-  Download and then install the Debug Diagnostics Tool v1.2    

-  Configure Performance Monitor logging    

-  Disable Debug Exception Catching    

-  Create a dump file    

-  Disable Performance Monitor logging    

-  Analyze the dump file    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-05*

I believe it's IIS 10.x.  The one that's available on Windows Server 2019.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-05*

Hi @Jonathan Berg   ,    

What version of IIS are you using? If it's IIS 7.x, you could troubleshoot for high CPU by following the instructions in this document: Troubleshooting High CPU in an IIS 7.x Application Pool    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
