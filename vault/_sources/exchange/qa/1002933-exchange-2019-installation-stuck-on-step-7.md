---
title: "Exchange 2019 Installation stuck on Step 7"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1002933/exchange-2019-installation-stuck-on-step-7
question_id: 1002933
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2019 Installation stuck on Step 7

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1002933/exchange-2019-installation-stuck-on-step-7 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Error:    

The following error was generated when "$error.Clear();     

          if (get-service MSExchangeServiceHost* | where {$_.name -eq "MSExchangeServiceHost"})  

          {  

              if ($RoleDatacenterIsTestEnv)  

              {  

                  Stop-Process -Name "Microsoft.Exchange.ServiceHost" -Force  

                  Sleep -Seconds 15  

              }  

              else  

              {  

                  Stop-service MSExchangeServiceHost  

              }  

```
Start-service MSExchangeServiceHost  
      }  
    " was run: "Microsoft.PowerShell.Commands.ServiceCommandException: Failed to start service 'Microsoft Exchange Service Host (MSExchangeServiceHost)'.".
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-14*

Please have a check and verify all the system requirements and prerequisites to install Exchange 2019 have been met. And if the server you are trying to install Exchange on is a domain controller, it’s recommended to install on a member server instead, see Installing Exchange on a domain controller is not recommended.    

For anyone else with this sort of problem, these article seems to resolve it -     

https://exchangeshare.wordpress.com/2014/05/16/exchange-2013-sp1-install-error-database-is-mandatory-on-arbitration-mailboxes/     

https://www.stellarinfo.com/article/setup-new-exchange-server-2019.php
