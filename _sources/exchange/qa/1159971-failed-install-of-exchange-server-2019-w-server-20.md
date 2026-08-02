---
title: "Failed install of Exchange server 2019 W server 2022"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1159971/failed-install-of-exchange-server-2019-w-server-20
question_id: 1159971
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Failed install of Exchange server 2019 W server 2022

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1159971/failed-install-of-exchange-server-2019-w-server-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I tried running the installer again and got this error in step 6 of 12 Mailbox role: Transport Service:

```
Error:
The following error was generated when "$error.Clear(); 
          if ( ($server -eq $null) -and ($RoleIsDatacenter -ne $true) )
          {
            Update-RmsSharedIdentity -ServerName $RoleNetBIOSName
          }
        " was run: "Microsoft.Exchange.Data.DataValidationException: Database is mandatory on UserMailbox.
   at Microsoft.Exchange.Data.Directory.ADDataSession.Save(ADObject instanceToSave, IEnumerable`1 properties, Boolean bypassValidation)
   at Microsoft.Exchange.Data.Directory.Recipient.ADRecipientObjectSession.Save(ADRecipient instanceToSave, String callerFilePath, Int32 callerFileLine, String memberName)
   at Microsoft.Exchange.Management.Deployment.UpdateRmsSharedIdentity.Link()
   at Microsoft.Exchange.Management.Deployment.UpdateRmsSharedIdentity.InternalProcessRecord()
   at Microsoft.Exchange.Configuration.Tasks.Task.b__91_1()
   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".
```

When I try via powershell with the following command .\Setup.exe /IAcceptExchangeServerLicenseTermsDiagnosticDataOFF /mode:upgrade /dc:someDC  

 I get:

```
Microsoft Exchange Server 2019 Cumulative Update 12 Unattended Setup

Copying Files...
File copy complete. Setup will now collect additional information needed for installation.

Languages
Management tools

Performing Microsoft Exchange Server Prerequisite Check

    Configuring Prerequisites                                                                         COMPLETED
    Prerequisite Analysis                                                                             COMPLETED

Configuring Microsoft Exchange Server

    Language Files                                                                                    COMPLETED
    Restoring Services                                                                                COMPLETED
    Language Configuration                                                                            COMPLETED
    Exchange Management Tools                                                                         COMPLETED
    Finalizing Setup                                                                                  COMPLETED

The Exchange Server setup operation completed successfully.
PS C:\Exchange>
```

No mailbox role, which was the intention and the way it was initially installed.

Any assistance for me to get mailbox role installed?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-13*

We use Admin accounts in our environment and mine was corrupted.

I got that information from the installation logs.

After rebuilding the admin account it installed properly.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-12*

First of all thanks for the reply.

I installed from PS and used the following command to prepare:  

PS C:\Exchange>  Install-WindowsFeature Server-Media-Foundation, NET-Framework-45-Features, RPC-over-HTTP-proxy, RSAT-Clustering, RSAT-Clustering-CmdInterface, RSAT-Clustering-Mgmt, RSAT-Clustering-PowerShell, WAS-Process-Model, Web-Asp-Net45, Web-Basic-Auth, Web-Client-Auth, Web-Digest-Auth, Web-Dir-Browsing, Web-Dyn-Compression, Web-Http-Errors, Web-Http-Logging, Web-Http-Redirect, Web-Http-Tracing, Web-ISAPI-Ext, Web-ISAPI-Filter, Web-Lgcy-Mgmt-Console, Web-Metabase, Web-Mgmt-Console, Web-Mgmt-Service, Web-Net-Ext45, Web-Request-Monitor, Web-Server, Web-Stat-Compression, Web-Static-Content, Web-Windows-Auth, Web-WMI, Windows-Identity-Foundation, RSAT-ADDS

After that I ran the:

 ./Setup.exe /PrepareSchema /IAcceptExchangeServerLicenseTerms_diagnosticaDataOFF 

and 

 ./Setup.exe /PrepareAD /IAcceptExchangeServerLicenseTerms_diagnosticaDataOFF 

On our root DC as it is in our root domain and the server is in our child domain.

After waiting for propagation I ran the installer just to verify if I had missed anything and there were a couple of pre-requisites missing that I completed install.

I restarted the server and ran the install from installer again and it failed on Transport Hub.

Then I ran the upgrade option:

```
PS C:\Exchange> .\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF /mode:upgrade /dc:fmdaddc5

Microsoft Exchange Server 2019 Cumulative Update 12 Unattended Setup

Copying Files...
File copy complete. Setup will now collect additional information needed for installation.

Languages
Management tools

Performing Microsoft Exchange Server Prerequisite Check

    Configuring Prerequisites                                                                         COMPLETED
    Prerequisite Analysis                                                                             COMPLETED

Configuring Microsoft Exchange Server

    Language Files                                                                                    COMPLETED
    Restoring Services                                                                                COMPLETED
    Language Configuration                                                                            COMPLETED
    Exchange Management Tools                                                                         COMPLETED
    Finalizing Setup
```

I am missing all services under Microsoft Exchange and cannot go forward neither backwards (install/remove)

Tried as well to run the install from PS specifying the Hub Transport 

```
PS C:\Exchange> .\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF /mode:install /r:hubtransport

Microsoft Exchange Server 2019 Cumulative Update 12 Unattended Setup

Copying Files...
File copy complete. Setup will now collect additional information needed for installation.

Languages
Mailbox role: Transport service
Mailbox role: Client Access service
Mailbox role: Mailbox service
Mailbox role: Front End Transport service
Mailbox role: Client Access Front End service

Performing Microsoft Exchange Server Prerequisite Check

    Configuring Prerequisites                                                                                                   COMPLETED
    Prerequisite Analysis                                                                                                       FAILED

A Setup failure previously occurred while installing the HubTransportRole role. Either run Setup again for just this role, or remove the role
using Control Panel.
For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.InstallWatermark.aspx

A Setup failure previously occurred while installing the PreFileCopy role. Either run Setup again for just this role, or remove the role using
Control Panel.
For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.InstallWatermark.aspx

The Exchange Server setup operation didn't complete. More details can be found in ExchangeSetup.log located in the
:\ExchangeSetupLogs folder.
PS C:\Exchange>
```

and that is where I am at. 

Very tempted to reinstall the servers and try from scratch!
