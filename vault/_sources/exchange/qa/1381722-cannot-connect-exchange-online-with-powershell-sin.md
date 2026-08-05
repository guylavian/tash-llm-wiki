---
title: "Cannot connect Exchange online with Powershell - Since Deprecation of Remote PowerShell in Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1381722/cannot-connect-exchange-online-with-powershell-sin
question_id: 1381722
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Cannot connect Exchange online with Powershell - Since Deprecation of Remote PowerShell in Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1381722/cannot-connect-exchange-online-with-powershell-sin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We just had the "Deprecation of Remote PowerShell in Exchange Online – Re-enabling or Extending RPS support" applied to our tenant on Monday.  Ever since this was done I have been unable to run Connect-ExchangeOnline.  I get the following error.  

```
New-ExoPSSession : Connecting to remote server outlook.office365.com failed with the following error message :  For more information, see the about_Remote_Troubleshooting Help topic.At C:\Program Files (x86)\WindowsPowerShell\Modules\ExchangeOnlineManagement\2.0.5\netFramework\ExchangeOnlineManagement.psm1:475 char:30+ ... PSSession = New-ExoPSSession -ExchangeEnvironmentName $ExchangeEnviro ...+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    + CategoryInfo          : ResourceUnavailable: (:) [New-ExoPSSession], PSRemotingTransportException    + FullyQualifiedErrorId : System.Management.Automation.Remoting.PSRemotingDataStructureException,Microsoft.Exchange.Management.ExoPowershellSnapin.NewExoPSSession
```

I have been going over different sites looking for a resolution and have not had any luck.   Any help would be greatly appreciated.    

Information I have gotten and want to provide from other things I have completed.   

PS C:\WINDOWS\system32> Get-InstalledModule ExchangeOnlineManagement

Version    Name                                Repository           Description                                                                                   3.3.0      ExchangeOnlineManagement            PSGallery              

PS C:\WINDOWS\system32> [Net.ServicePointManager]::SecurityProtocol

Tls12

```

```

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-13*

Hi @McGuiggan, Michael   

Thanks for your reply and glad everything worked fine after you reinstalled!

If you don't mind, we will write you a summary below so that other users who encounter similar problems can refer to your experience.

Since the Microsoft Q&A community has a policy that "[The question author cannot accept their own answer. They can only accept answers by others)], I'll repost your solution in case you'd like to "[Accept] the answer :)

***[Cannot connect Exchange online with Powershell - Since Deprecation of Remote PowerShell in Exchange Online] ***

** issue symptom: **

Error：

New-ExoPSSession : Connecting to remote server outlook.office365.com failed with the following error message : For more information, see the about_Remote_Troubleshooting Help topic.

**Resolution: **

By McGuiggan,Michael:

I ended up rebuilding my Computer from Scratch to Resolve this problem. I had already been thinking it was time for a refresh and this pushed me over the edge.

Once I re-installed everything, everything was working great.

Regards

Shaofan

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-10-04*

I would remove the all ExO modules and install again. 

Look like you are still referencing the old 2.x module in that error
