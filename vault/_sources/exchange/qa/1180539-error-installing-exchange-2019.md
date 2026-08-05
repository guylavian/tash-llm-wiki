---
title: "Error installing Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1180539/error-installing-exchange-2019
question_id: 1180539
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Error installing Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1180539/error-installing-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

we get below error when try to install exchange 2019 

please give me hand to fix my issue .

```
Error:
The following error was generated when "$error.Clear(); 
          $maxWait = New-TimeSpan -Minutes 8
          $timeout = Get-Date;
          $timeout = $timeout.Add($maxWait);
          $currTime = Get-Date;
          $successfullySetConfigDC = $false;

          while($currTime -le $timeout)
          {
            $setSharedCDCErrors = @();
            try
            {
              Set-SharedConfigDC -DomainController $RoleDomainController -ErrorVariable setSharedCDCErrors -ErrorAction SilentlyContinue;
              $successfullySetConfigDC = ($setSharedCDCErrors.Count -eq 0);

              if($successfullySetConfigDC)
              {
                break;
              }
              Write-ExchangeSetupLog -Info ("An error ocurred while setting shared config DC. Error: " + $setSharedCDCErrors[0]);
            }
            catch
            {
              Write-ExchangeSetupLog -Info ("An exception ocurred while setting shared config DC. Exception: " + $_.Exception.Message);
            }

            Write-ExchangeSetupLog -Info ("Waiting 30 seconds before attempting again.");
            Start-Sleep -Seconds 30;
            $currTime = Get-Date;
          }

          if( -not $successfullySetConfigDC)
          {
            Write-ExchangeSetupLog -Error "Unable to set shared config DC.";
          }
        " was run: "System.Exception: Unable to set shared config DC.
   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)
   at Microsoft.Exchange.Management.Deployment.WriteExchangeSetupLog.InternalProcessRecord()
   at Microsoft.Exchange.Configuration.Tasks.Task.b__91_1()
   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".
```

## Answer (community) — community member

*upvotes: 1 · updated: 2024-09-27*

To others who may come across this, when searching for solutions.

Here the issue was the Microsoft Baseline GPO for domain controllers, where the user rights assignements "Debug programs" and "Manage auditing and security log" were overwritten. 

Debug programs must contain:

-  BUILTIN\Administrators

-  Exchange Servers

-  Exchange Trusted Subsystem

Manage auditing and security log must contain:

-  BUILTIN\Administrators

Exchange Servers

The Exchange groups were missing and that caused the issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-15*

Hi @ramin sa ,

Please make sure you have installed all prerequisites correctly, and then try to follow the below steps:

-  Locate Microsoft.Exchange.Directory.TopologyService.exe.config File , By Default It Should Be Under "C:\Program Files\Microsoft\Exchange Server\V15\Bin"  

-  Open NotePad As Administrator & Then Open Microsoft.Exchange.Directory.TopologyService.exe.config File  

-  Locate "Topology MinimumPrefixMatch"  

-  Add MinSuitableServer = "1"  

-  Save The File & Restart Microsoft Exchange Active Directory Topology Services.  

For details, you could refer to: Exchange 2013 Setup Fails With Error "An exception ocurred while setting shared config DC"

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
