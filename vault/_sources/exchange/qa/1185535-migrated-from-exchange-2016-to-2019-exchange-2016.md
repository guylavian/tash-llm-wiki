---
title: "Migrated from Exchange 2016 to 2019.  Exchange 2016 is failing to uninstall all roles"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1185535/migrated-from-exchange-2016-to-2019-exchange-2016
question_id: 1185535
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
---
# Migrated from Exchange 2016 to 2019.  Exchange 2016 is failing to uninstall all roles

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1185535/migrated-from-exchange-2016-to-2019-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We recently migrated from Exchange 2016 to Exchange 2019.  We are in the process of removing the 2016 servers, however when we go to uninstall whether it's via GUI or command line, it fails right when it gets to the Mailbox role: Unified Messaging Service.

When looking at the exchange setup log, I noticed that it was complaining about not being able to find the server in AD.  I also read some places to go into the registry and delete the watermark and actions keys.  Doing so did proceed onto the next step but then we ran into the same failure.  It seems that it just skipped the UM service when we deleted those keys.  I restored them back and started looking into why it was saying it couldn't find the server.

When looking in ADSIEdit, the servers we attempted the uninstall on seems to have been removed from the servers list.  Some people on some forms say as long as it's not listed there it's fine but I'm not convinced.  Usually those people can make it to step 8 and it gets past removing all of the mailbox roles before failing.  In our case, on any server we try, it seems to be removing the server from ADSI Edit as soon as it completes the removal of the Mailbox role: Mailbox Service.  

Really hoping for some assistance on this one.  I don't want to have "remove it from ADSI Edit" as a solution in case there are lingering problems down the line.  I'll post what the Exchange log displayed.

```
[02/28/2023 22:08:40.0864] [2] Active Directory session settings for 'Uninstall-MsiPackage' are: View Entire Forest: 'True', Configuration Domain Controller: 'domaincontroller.contoso.com', Preferred Global Catalog: 'domaincontroller.contoso.com', Preferred Domain Controllers: '{ domaincontroller.contoso.com }'

[02/28/2023 22:08:40.0864] [2] User specified parameters:  -ProductCode:'cef60964-21ae-47e0-93c6-611aa8941b7f' -LogFile:'C:\ExchangeSetupLogs\remove-UMLanguagePack.en-us.msilog' -PropertyValues:'ESE=1'

[02/28/2023 22:08:40.0864] [2] Beginning processing uninstall-MsiPackage

[02/28/2023 22:08:40.0865] [2] Removing MSI package with code 'cef60964-21ae-47e0-93c6-611aa8941b7f'.

[02/28/2023 22:08:52.0424] [2] Ending processing uninstall-MsiPackage

[02/28/2023 22:08:52.0449] [2] Active Directory session settings for 'Get-ExchangeServer' are: View Entire Forest: 'True', Configuration Domain Controller: 'domaincontroller.contoso.com', Preferred Global Catalog: 'domaincontroller.contoso.com', Preferred Domain Controllers: '{ domaincontroller.contoso.com }'

[02/28/2023 22:08:52.0449] [2] User specified parameters:  -Identity:'MBXSERVER' -DomainController:'domaincontroller.contoso.com'

[02/28/2023 22:08:52.0450] [2] Beginning processing Get-ExchangeServer

[02/28/2023 22:08:52.0452] [2] Searching objects "MBXSERVER" of type "Server" under the root "$null".

[02/28/2023 22:08:52.0458] [2] Previous operation run on domain controller 'domaincontroller.contoso.com'.

[02/28/2023 22:08:52.0458] [2] Previous operation run on domain controller 'domaincontroller.contoso.com'.

[02/28/2023 22:08:52.0458] [2] Preparing to output objects. The maximum size of the result set is "Unlimited".

[02/28/2023 22:08:52.0461] [2] [ERROR] The operation couldn't be performed because object 'MBXSERVER' couldn't be found on 'domaincontroller.contoso.com'.

[02/28/2023 22:08:52.0462] [2] [ERROR] The operation couldn't be performed because object 'MBXSERVER' couldn't be found on 'domaincontroller.contoso.com'.

[02/28/2023 22:08:52.0463] [2] Ending processing Get-ExchangeServer

[02/28/2023 22:08:52.0464] [2] Active Directory session settings for 'Uninstall-MsiPackage' are: View Entire Forest: 'True', Configuration Domain Controller: 'domaincontroller.contoso.com', Preferred Global Catalog: 'domaincontroller.contoso.com', Preferred Domain Controllers: '{ domaincontroller.contoso.com }'

[02/28/2023 22:08:52.0464] [2] User specified parameters:  -ProductCode:'66d57636-bd4b-402f-9e7d-5e89c28c8136' -LogFile:'C:\ExchangeSetupLogs\remove-UMLanguagePack.en-us.msilog'

[02/28/2023 22:08:52.0465] [2] Beginning processing uninstall-MsiPackage

[02/28/2023 22:08:52.0465] [2] Removing MSI package with code '66d57636-bd4b-402f-9e7d-5e89c28c8136'.

[02/28/2023 22:08:53.0366] [2] Ending processing uninstall-MsiPackage

[02/28/2023 22:08:53.0374] [2] Active Directory session settings for 'Uninstall-MsiPackage' are: View Entire Forest: 'True', Configuration Domain Controller: 'domaincontroller.contoso.com', Preferred Global Catalog: 'domaincontroller.contoso.com', Preferred Domain Controllers: '{ domaincontroller.contoso.com }'

[02/28/2023 22:08:53.0374] [2] User specified parameters:  -ProductCode:'b07da010-66cf-40a7-908f-f6482219c57f' -LogFile:'C:\ExchangeSetupLogs\remove-UMLanguagePack.en-us.msilog'

[02/28/2023 22:08:53.0374] [2] Beginning processing uninstall-MsiPackage

[02/28/2023 22:08:53.0375] [2] Removing MSI package with code 'b07da010-66cf-40a7-908f-f6482219c57f'.

[02/28/2023 22:08:54.0021] [2] Ending processing uninstall-MsiPackage

[02/28/2023 22:08:54.0022] [2] Active Directory session settings for 'Uninstall-MsiPackage' are: View Entire Forest: 'True', Configuration Domain Controller: 'domaincontroller.contoso.com', Preferred Global Catalog: 'domaincontroller.contoso.com', Preferred Domain Controllers: '{ domaincontroller.contoso }'

[02/28/2023 22:08:54.0022] [2] User specified parameters:  -ProductCode:'8466eaed-7024-4aee-9d13-f3a55b98d114' -LogFile:'C:\ExchangeSetupLogs\remove-UMLanguagePack.en-us.msilog'

[02/28/2023 22:08:54.0022] [2] Beginning processing uninstall-MsiPackage

[02/28/2023 22:08:54.0022] [2] Removing MSI package with code '8466eaed-7024-4aee-9d13-f3a55b98d114'.

[02/28/2023 22:08:54.0815] [2] Ending processing uninstall-MsiPackage

[02/28/2023 22:08:54.0817] [1] The following 1 error(s) occurred during task execution:

[02/28/2023 22:08:54.0817] [1] 0.  ErrorRecord: The operation couldn't be performed because object 'MBXSERVER' couldn't be found on 'domaincontroller.contoso.com'.

[02/28/2023 22:08:54.0817] [1] 0.  ErrorRecord: Microsoft.Exchange.Configuration.Tasks.ManagementObjectNotFoundException: The operation couldn't be performed because object 'MBXSERVER' couldn't be found on 'domaincontroller.contoso.com'.

   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)

   at Microsoft.Exchange.Configuration.Tasks.GetObjectWithIdentityTaskBase`2.InternalProcessRecord()

   at Microsoft.Exchange.Configuration.Tasks.Task.b__91_1()

   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)

[02/28/2023 22:08:54.0820] [1] [ERROR] The following error was generated when "$error.Clear(); 

          uninstall-MsiPackage -ProductCode $RoleProductCode -LogFile $RoleLogFilePath -PropertyValues ("ESE=1");

          $lochost=hostname;

          $exchsrv=Get-ExchangeServer -Identity $lochost -DomainController $RoleDomainController;

          if (-not $exchsrv.IsMailboxServer)

          {

            uninstall-MsiPackage -ProductCode $RoleTeleProductCode -LogFile $RoleLogFilePath;

          }

          if ( $RoleTransProductCode -ne [system.guid]::empty )

          {

            uninstall-MsiPackage -ProductCode $RoleTransProductCode -LogFile $RoleLogFilePath;

          }

          uninstall-MsiPackage -ProductCode $RoleTtsProductCode -LogFile $RoleLogFilePath;

        " was run: "Microsoft.Exchange.Configuration.Tasks.ManagementObjectNotFoundException: The operation couldn't be performed because object 'MBXSERVER' couldn't be found on 'domaincontroller.contoso.com'.

   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)

   at Microsoft.Exchange.Configuration.Tasks.GetObjectWithIdentityTaskBase`2.InternalProcessRecord()

   at Microsoft.Exchange.Configuration.Tasks.Task.b__91_1()

   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

[02/28/2023 22:08:54.0820] [1] [ERROR] The operation couldn't be performed because object 'MBXSERVER' couldn't be found on 'domaincontroller.contoso.com'.

[02/28/2023 22:08:54.0820] [1] [ERROR-REFERENCE] Id=UmLanguagePackComponent___98c7f337c1334ef59c2ac59e52813c16 Component=EXCHANGE14:\Current\Release\Client Access\Unified Messaging

[02/28/2023 22:08:54.0820] [1] Setup is stopping now because of one or more critical errors.

[02/28/2023 22:08:54.0820] [1] Finished executing component tasks.

[02/28/2023 22:08:54.0838] [1] Ending processing Uninstall-UnifiedMessagingRole

[02/28/2023 22:08:54.0843] [0] CurrentResult console.ProcessRunInternal:198: 1

[02/28/2023 22:08:54.0848] [0] CurrentResult launcherbase.maincore:90: 1

[02/28/2023 22:08:54.0848] [0] CurrentResult console.startmain:52: 1

[02/28/2023 22:08:54.0848] [0] CurrentResult SetupLauncherHelper.loadassembly:452: 1

[02/28/2023 22:08:54.0852] [0] The Exchange Server setup operation didn't complete.  More details can be found in ExchangeSetup.log located in the :\ExchangeSetupLogs folder.

[02/28/2023 22:08:54.0857] [0] CurrentResult main.run:235: 1

[02/28/2023 22:08:54.0857] [0] CurrentResult setupbase.maincore:396: 1

[02/28/2023 22:08:54.0858] [0] End of Setup

[02/28/2023 22:08:54.0858] [0] **********************************************

 
[02/28/2023 22:08:40.08ing now because of one or more critical errors.
[02/28/2023 22:08:54.0820] [1] Finished executing component tasks.
[02/28/2023 22:08:54.0838] [1] Ending processing Uninstall-UnifiedMessagingRole
[02/28/2023 22:08:54.0843] [0] CurrentResult console.ProcessRunInternal:198: 1
[02/28/2023 22:08:54.0848] [0] CurrentResult launcherbase.maincore:90: 1
[02/28/2023 22:08:54.0848] [0] CurrentResult console.startmain:52: 1
[02/28/2023 22:08:54.0848] [0] CurrentResult SetupLauncherHelper.loadassembly:452: 1
[02/28/2023 22:08:54.0852] [0] The Exchange Server setup operation didn't complete.  More details can be found in ExchangeSetup.log located in the :\ExchangeSetupLogs folder.
[02/28/2023 22:08:54.0857] [0] CurrentResult main.run:235: 1
[02/28/2023 22:08:54.0857] [0] CurrentResult setupbase.maincore:396: 1
[02/28/2023 22:08:54.0858] [0] End of Setup
[02/28/2023 22:08:54.0858] [0] **********************************************
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-19*

This issue is reported in the following links:
https://learn.microsoft.com/en-us/answers/questions/1186926/unable-to-uninstall-exchange-2016-cu23
https://support.microsoft.com/en-au/topic/-object-servername-couldn-t-be-found-on-domaincontrollername-error-when-trying-to-uninstall-exchange-server-2dcfb94a-7f58-4a5e-8b59-d0ae12c63e1a
Unfortunately, there is not a good solution for it... If the server is already deleted in the ADSI Edit, you should assume that the Exchange Server was completely removed from the envinroment and discard the server that was hosting it.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-03*

Hi @ExchangeGod ,

How many servers do you have in your environment? According to your description, the servers have been removed and you cannot uninstall Exchange 2016 using the normal method, you can only see if there is anything left and then use ADSIedit to remove it.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-02*

Hi @ExchangeGod ,

You could recover Exchange Server on a new device first and then uninstall it. If you still cannot uninstall it, you may need to contact technical support.

Refer to: https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/recover-exchange-servers?view=exchserver-2016

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
