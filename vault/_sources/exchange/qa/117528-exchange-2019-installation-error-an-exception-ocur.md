---
title: "Exchange 2019 installation error | An exception ocurred while setting shared config DC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/117528/exchange-2019-installation-error-an-exception-ocur
question_id: 117528
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User", "Volunteer Moderator"]
---
# Exchange 2019 installation error | An exception ocurred while setting shared config DC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/117528/exchange-2019-installation-error-an-exception-ocur (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Need help

I am Getting following error while installing exchange server 2019 in DR

We have 4 node in DC (3 Mailbox and 1 for Archive) and 2 in DR , while adding another exchange node in DR getting error.

Error:  

The following error was generated when "$error.Clear();  

$maxWait = New-TimeSpan -Minutes 8  

$timeout = Get-Date;  

$timeout = $timeout.Add($maxWait);  

$currTime = Get-Date;  

$successfullySetConfigDC = $false;

```
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
```

at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)  

at Microsoft.Exchange.Management.Deployment.WriteExchangeSetupLog.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2020-10-07*

@Nur Hossain       

Hi,    

Here are some suggestions:    

-  Check if the new Exchange 2019 Server can access the domain controller in the DR site.     

-  Make sure IPv6 is enabled on the Exchange 2019 Server.    

-  Check if the Microsoft Exchange Active Directory Topology Service on the Exchange 2019 Server is stopped during installation. If so, start it manually and see if the problem persists.    

If suggestions above didn't help you with your problem,    

please check the Application Log in the Event Viewer and see if it generates some warnings or error messages during a failed installtion.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-27*

To others who may come across this, when searching for solutions.

Here the issue was the Microsoft Baseline GPO for domain controllers, where the user rights assignements "Debug programs" and "Manage auditing and security log" were overwritten.

Debug programs must contain:

-  BUILTIN\Administrators

-  Exchange Servers

-  Exchange Trusted Subsystem

Manage auditing and security log must contain:

-  BUILTIN\Administrators

Exchange Servers

The Exchange groups were missing and that caused the issue.To others who may come across this, when searching for solutions.

Here the issue was the Microsoft Baseline GPO for domain controllers, where the user rights assignements "Debug programs" and "Manage auditing and security log" were overwritten.

Debug programs must contain:

-  BUILTIN\Administrators

-  Exchange Servers

-  Exchange Trusted Subsystem

Manage auditing and security log must contain:

-  BUILTIN\Administrators

-  Exchange Servers

The Exchange groups were missing and that caused the issue.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-07-10*

Had the same problem installing Exchange 2019, none of the existing suggestions on the web helped me, so I think I will share my solution on this problem.

We have an old AD with one site (Default-First-Site-Name).

In "AD Sites and Services" under "Sites|Default-First-Site-Name|Servers" there were several decommissioned DC's registered.

After removing these old DC*s from the list, the installation succeeded.

Exchange Topology Service uses this list, to determine DC's for the relevant site.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-10-09*

Hi  

Check if the Net.tcp port sharing service is started?
