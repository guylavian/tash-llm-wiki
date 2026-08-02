---
title: "Exchange 2016 CU23 fails on Mailbox role:Mailbox service"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1657514/exchange-2016-cu23-fails-on-mailbox-role-mailbox-s
question_id: 1657514
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 CU23 fails on Mailbox role:Mailbox service

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1657514/exchange-2016-cu23-fails-on-mailbox-role-mailbox-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

2024-04-18_10h11_43.png

Hi

We have multiple Exchange 2010/2016 servers environment, whilst we are migrating our users to the cloud..

Currently installing a new Exchange 2016 server, but it fails at the Mailbox role:Mailbox Service. Tried using another ISO but the install still fails. Previously installed Exchange 2016 with no issues

Also followed the install process as outlined in this article: https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites?view=exchserver-2016

Below is the error, any insight would be involved; as there is not much info out there with regards to this specific error

[ERROR] Could not load file or assembly 'Microsoft.Exchange.PublicFolders, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The module was expected to contain an assembly manifest.

 [ERROR-REFERENCE] Id=SystemAttendantDependent___a5f453e312d0462d81d676dd43c79488 Component=EXCHANGE14:\Current\Release\Transport\Internet

[1] Setup is stopping now because of one or more critical errors.

[ERROR] The following error was generated when "$error.Clear(); 

```
if (!$RoleIsDatacenter -and !$RoleIsDatacenterDedicated)

      {

      $mailboxId = [Microsoft.Exchange.Management.Deployment.UpdateRmsSharedIdentity]::SharedIdentityCommonName;

      $displayName = "Microsoft Exchange Federation Mailbox";

      $existingFederatedUserMailboxes = @(Get-Mailbox -Filter {Name -eq $mailboxId} -IgnoreDefaultScope -ResultSize 1);

      $existingFederatedArbitrationMailboxes = @(Get-Mailbox -Arbitration -Filter {Name -eq $mailboxId} -IgnoreDefaultScope -ResultSize 1);

      if (($existingFederatedUserMailboxes.Length -eq 0) -and ($existingFederatedArbitrationMailboxes.Length -eq 0))

      {

      $mailboxDatabase = @(get-MailboxDatabase -Server:$RoleFqdnOrName -DomainController $RoleDomainController);

      if ($mailboxDatabase.Length -ne 0)

      {

      $mailboxUsers = @(Get-User -Filter {LastName -eq $mailboxId} -IgnoreDefaultScope -ResultSize 1);

      if ($mailboxUsers.Length -ne 0)

      {

      $federatedMailbox = Enable-Mailbox -Arbitration -Identity $mailboxUsers[0] -Database $mailboxDatabase[0].Identity;

      Set-Mailbox -Arbitration -Identity $federatedMailbox -RequireSenderAuthenticationEnabled $false -ProhibitSendReceiveQuota 1MB -ProhibitSendQuota 1MB -IssueWarningQuota 1MB -UseDatabaseQuotaDefaults $false -SCLDeleteEnabled $false -SCLJunkEnabled $false -SCLQuarantineEnabled $false -SCLRejectEnabled $false -HiddenFromAddressListsEnabled $true -DisplayName $displayName -Force;

      Set-TransportConfig -OrganizationFederatedMailbox $federatedMailbox.WindowsEmailAddress.ToString();

      }

      }

      }

      }

    " was run: "System.BadImageFormatException: Could not load file or assembly 'Microsoft.Exchange.PublicFolders, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The module was expected to contain an assembly manifest.
```File name: 'Microsoft.Exchange.PublicFolders, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35'

   at Microsoft.Exchange.Data.Directory.SystemConfiguration.TenantPublicFolderConfigurationCache.Create()

   at Microsoft.Exchange.ExchangeSystem.LazyMember`1.GetLazyMemberInternal()

   at Microsoft.Exchange.Management.RecipientTasks.GetMailbox.ConvertDataObjectToPresentationObject(IConfigurable dataObject)

   at Microsoft.Exchange.Configuration.Tasks.GetRecipientObjectTask`2.WriteResult(IConfigurable dataObject)

   at Microsoft.Exchange.Configuration.Tasks.GetTaskBase`1.WriteResult[T](IEnumerable`1 dataObjects)

   at Microsoft.Exchange.Configuration.Tasks.GetTaskBase`1.InternalProcessRecord()

   at Microsoft.Exchange.Configuration.Tasks.GetObjectWithIdentityTaskBase`2.InternalProcessRecord()

   at Microsoft.Exchange.Configuration.Tasks.GetRecipientObjectTask`2.InternalProcessRecord()

   at Microsoft.Exchange.Management.RecipientTasks.GetRecipientWithAddressListBase`2.InternalProcessRecord()

   at Microsoft.Exchange.Configuration.Tasks.Task.b__91_1()

   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)

   at Microsoft.Exchange.Configuration.Tasks.Task.ProcessTaskStage(TaskStage taskStage, Action initFunc, Action mainFunc, Action completeFunc)

   at Microsoft.Exchange.Configuration.Tasks.Task.ProcessRecord()

   at System.Management.Automation.CommandProcessor.ProcessRecord()

WRN: Assembly binding logging is turned OFF.

To enable assembly bind failure logging, set the registry value [HKLM\Software\Microsoft\Fusion!EnableLog] (DWORD) to 1.

Note: There is some performance penalty associated with assembly bind failure logging.

To turn this feature off, remove the registry value [HKLM\Software\Microsoft\Fusion!EnableLog].
```

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2024-04-19*

Hi,

According to your description of the issue, Errors are reported indicating that the installation process was unable to properly load a specific set of programs related to Microsoft Exchange, which can be due to a variety of reasons, such as corrupt installation files, missing prerequisites, or problems with the system environment on which the installation is attempted.

-  Check all prerequisites, including required roles and features, .NET Framework version, Windows Management Framework, and updates.

-  Check permissions to ensure that you are running the Exchange installer with administrator privileges

-  Verify operating system compatibility: Ensure that Exchange Server is compatible with the version of Windows Server you are running.

And,I would like to confirm with you that the public folders in your organization's environment are functioning properly.

Please be free to contact us if you have any questions.
