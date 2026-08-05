---
title: "Exchange Server 2013 Update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4245985/exchange-server-2013-update
question_id: 4245985
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: []
---
# Exchange Server 2013 Update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4245985/exchange-server-2013-update (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We're trying to update our exchange hybrid deployment to exchange server 2019 and I've encountered somewhat of a roadblock. When I run the pre-requisite checks it throws up an error that we need to update our 2 Exchange 2013 CU 13 servers to CU 21 and I've encountered this error:

Error:

The following error was generated when "$error.Clear(); 

          if (Get-Service MpsSvc* | ?{$_.Name -eq 'MpsSvc'})

          {

            Set-Service MpsSvc -StartupType Automatic

            Start-SetupService -ServiceName MpsSvc

          }

        " was run: "Microsoft.PowerShell.Commands.ServiceCommandException: Service 'Windows Defender Firewall (MpsSvc)' cannot be configured due to the following error: Access is denied ---> System.ComponentModel.Win32Exception: Access is denied

   --- End of inner exception stack trace ---".

From googling around it seems that it's referring to some sort of incompatibility. The 2 exchange servers we currently have are running Windows Server 2012 R2 and Windows Server 2019. Is it actually the case where I can't update this version of exchange and I need to go through the process of just installing Exchange Server 2019 on a fresh environment?

Thanks in advance,

Dan

## Answers

_No answers on this thread._
