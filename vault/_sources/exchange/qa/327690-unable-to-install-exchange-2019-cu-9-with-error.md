---
title: "Unable to install exchange 2019 CU 9 with Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/327690/unable-to-install-exchange-2019-cu-9-with-error
question_id: 327690
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Unable to install exchange 2019 CU 9 with Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/327690/unable-to-install-exchange-2019-cu-9-with-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In Our current environment, we have three domain controllers (Windows server 2019-2 in DC and 1 in DR) and Two Mailbox  + CAS servers (exchange 2013). Both Forest and domain functional levels are winSvr2012R2.    

While we trying to deploy the exchange server 2019 CU 9. we are getting the following errors.    

    

Any Idea?    

Thank You    

Nur

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2021-03-24*

Hi Nur,  

Looks like issue with the arbitration mailbox. please follow the below steps,  

Run Get-Mailbox -Arbitration | ft Name,ServerName,Database -Auto  

This will return warning message for one the system mailbox which is for migration. Then run the below command,  

Set-Mailbox “SystemMailbox{xxxxxx}” -Arbitration -Database “YourDatabaseNameHere”  

You have to enter the name of the system mailbox where the database value is null.  

Re-run the setup.  

https://exchangeshare.wordpress.com/2014/05/16/exchange-2013-sp1-install-error-database-is-mandatory-on-arbitration-mailboxes/  

If the above suggestion helps, please click on "Accept Answer" and upvote it. Thanks for understanding.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-03-24*

Below is error details and I also attached setup logs

[03/23/2021 12:45:49.0244] [1] [ERROR] The following error was generated when "$error.Clear();  

if (!$RoleIsDatacenter -and !$RoleIsDatacenterDedicated)  

{​​​​​​​  

$mailboxId = [Microsoft.Exchange.Management.Migration.MigrationService.Batch.MigrationBatchIdParameter]::MigrationMailboxName;  

$dispName = "Microsoft Exchange Migration";  

$mbxs = @(Get-Mailbox -Arbitration -DomainController $RoleDomainController -Filter {​​​​​​​Name -eq $mailboxId}​​​​​​​);  

$migrationMailbox = $null;

```
if ($mbxs.Length -eq 0)
      {​​​​​​​
      Write-ExchangeSetupLog -Info ("Retrieving mailbox databases on Server=$RoleFqdnOrName.");
      $dbs = @(Get-MailboxDatabase -Server:$RoleFqdnOrName -DomainController $RoleDomainController);
      if ($dbs.Length -ne 0)
      {​​​​​​​
      Write-ExchangeSetupLog -Info ("Retrieving users with Name=$mailboxId.");
      $arbUsers = @(Get-User -Filter {​​​​​​​Name -eq $mailboxId}​​​​​​​ -IgnoreDefaultScope -ResultSize 1);
      if ($arbUsers.Length -ne 0)
      {​​​​​​​
      Write-ExchangeSetupLog -Info ("Enabling mailbox $mailboxId.");
      $migrationMailbox = Enable-Mailbox -Arbitration -Identity $arbUsers[0] -DisplayName $dispName -database $dbs[0].Identity;
      }​​​​​​​
      }​​​​​​​
      }​​​​​​​
      else
      {​​​​​​​
      $migrationMailbox = $mbxs[0];
      }​​​​​​​

      # Set the Organization Capabilities and quotas needed for this mailbox
      if ($migrationMailbox -ne $null)
      {​​​​​​​
      Set-Mailbox -Arbitration -Identity $migrationMailbox -ProhibitSendReceiveQuota 300MB -ProhibitSendQuota 300MB -IssueWarningQuota 150MB -RecoverableItemsQuota 30GB -RecoverableItemsWarningQuota 20GB -UseDatabaseQuotaDefaults $false -SCLDeleteEnabled $false -SCLJunkEnabled $false -SCLQuarantineEnabled $false -SCLRejectEnabled $false -HiddenFromAddressListsEnabled $true -DisplayName $dispName -Management:$true -Force;
      }​​​​​​​
      else
      {​​​​​​​
      Write-ExchangeSetupLog -Info ("Cannot find migration mailbox with name=$mailboxId.");
      }​​​​​​​
      }​​​​​​​
    " was run: "Microsoft.Exchange.Data.DataValidationException: Database is mandatory on UserMailbox.
```

at Microsoft.Exchange.Data.Directory.SystemConfiguration.TenantConfigurationCacheableItem`1.TryRunADOperation(ADOperation operation, Boolean throwExceptions)    at Microsoft.Exchange.Data.Directory.SystemConfiguration.TenantConfigurationCacheableItem`1.Initialize(OrganizationId organizationId, CacheNotificationHandler cacheNotificationHandler, Object state)  

at Microsoft.Exchange.Data.Directory.SystemConfiguration.TenantConfigurationCache`1.InitializeAndAddPerTenantSettings(OrganizationId orgId, Boolean allowExceptions, TSettings& perTenantSettings, Object state)    at Microsoft.Exchange.Data.Directory.SystemConfiguration.TenantConfigurationCache`1.TryGetValue(OrganizationId orgId, Boolean allowExceptions, TSettings& perTenantSettings, Boolean& hasExpired, Object state)  

at Microsoft.Exchange.Data.Directory.SystemConfiguration.TenantConfigurationCache`1.GetValue(OrganizationId orgId)    at Microsoft.Exchange.Management.RecipientTasks.GetMailbox.ConvertDataObjectToPresentationObject(IConfigurable dataObject)    at Microsoft.Exchange.Configuration.Tasks.GetRecipientObjectTask`2.WriteResult(IConfigurable dataObject)  

at Microsoft.Exchange.Configuration.Tasks.GetTaskBase`1.WriteResult[T](IEnumerable`1 dataObjects)  

at Microsoft.Exchange.Configuration.Tasks.GetTaskBase`1.InternalProcessRecord()    at Microsoft.Exchange.Configuration.Tasks.GetObjectWithIdentityTaskBase`2.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.GetRecipientObjectTask`2.InternalProcessRecord()    at Microsoft.Exchange.Management.RecipientTasks.GetRecipientWithAddressListBase`2.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-03-23*

Hi @Nur Hossain   ,    

Unfortunately this error is not complete. Please share the complete error by covering your personal information.    

Have you run the below commands before the setup?    

Setup.exe /PrepareSchema /IAcceptExchangeServerLicenseTerms    

Setup.exe /PrepareAD /IAcceptExchangeServerLicenseTerms
