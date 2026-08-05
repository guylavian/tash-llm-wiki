---
title: "Exchange2016  CU23 on Windows Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1257596/exchange2016-cu23-on-windows-server-2019
question_id: 1257596
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange2016  CU23 on Windows Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1257596/exchange2016-cu23-on-windows-server-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
we have Exchange Hybrid server 2016  CU23 which is running windows Server 2012R2.
We want to upgrade this server 2012 to latest version so what we planned is to, Install Exchange server 2016 CU 23 on new windows server 2019 and once this is successful, then decommission old windows server 2012.
    
when Install Exchange server 2016 on Windows server 2019 server, I get this below error message,  any idea of this below error message. I need your assistance , Is that possible to install Exchange 2016 CU23 on Windows 2019?

Error:
The following error was generated when "$error.Clear(); 
          if (Get-Service MpsSvc* | ?{$_.Name -eq 'MpsSvc'})
          {
            Set-Service MpsSvc -StartupType Automatic
            Start-SetupService -ServiceName MpsSvc
          }
        " was run: "Microsoft.PowerShell.Commands.ServiceCommandException: Service 'Windows Defender Firewall (MpsSvc)' cannot be configured due to the following error: Access is denied ---> System.ComponentModel.Win32Exception: Access is denied
   --- End of inner exception stack trace ---".
```

Thanks  

Charles Binny

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2023-04-26*

Hi @charles binny  
 

`Is that possible to install Exchange 2016 CU23 on Windows 2019?`

By research, Supported operating systems for Exchange 2016 shows that it is not supported to install Exchange 2016 on WS2019 systems. As shown below:  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
