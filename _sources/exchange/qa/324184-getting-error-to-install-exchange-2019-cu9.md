---
title: "Getting error to install Exchange 2019 CU9"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/324184/getting-error-to-install-exchange-2019-cu9
question_id: 324184
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Getting error to install Exchange 2019 CU9

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/324184/getting-error-to-install-exchange-2019-cu9 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi    

I am getting below error, when I am trying to install the exchange 2019 CU9 into our current Exchange 2013 CU23 environment,    

Error:    

The following error was generated when "$error.Clear();    

if (!$RoleIsDatacenter -and !$RoleIsDatacenterDedicated)    

{    

$mailboxId = [Microsoft.Exchange.Management.Migration.MigrationService.Batch.MigrationBatchIdParameter]::MigrationMailboxName;    

$dispName = "Microsoft Exchange Migration";    

$mbxs = @(Get-Mailbox -Arbitration -DomainController $RoleDomainController -Filter {Name -eq $mailboxId});    

$migrationMailbox = $null;    

```
if ($mbxs.Length -eq 0)  
   {  
   Write-ExchangeSetupLog -Info ("Retrieving mailbox databases on Server=$RoleFqdnOrName.");  
   $dbs = @(Get-MailboxDatabase -Server:$RoleFqdnOrName -DomainController $RoleDomainController);  
   if ($dbs.Length -ne 0)  
   {  
   Write-ExchangeSetupLog -Info ("Retrieving users with Name=$mailboxId.");  
   $arbUsers = @(Get-User -Filter {Name -eq $mailboxId} -IgnoreDefaultScope -ResultSize 1);  
   if ($arbUsers.Length -ne 0)  
   {  
   Write-ExchangeSetupLog -Info ("Enabling mailbox $mailboxId.");  
   $migrationMailbox = Enable-Mailbox -Arbitration -Identity $arbUsers[0] -DisplayName $dispName -database $dbs[0].Identity;  
   }  
   }  
   }  
   else  
   {  
   $migrationMailbox = $mbxs[0];  
   }  
   # Set the Organization Capabilities and quotas needed for this mailbox  
   if ($migrationMailbox -ne $null)  
   {  
   Set-Mailbox -Arbitration -Identity $migrationMailbox -ProhibitSendReceiveQuota 300MB -ProhibitSendQuota 300MB -IssueWarningQuota 150MB -RecoverableItemsQuota 30GB -RecoverableItemsWarningQuota 20GB -UseDatabaseQuotaDefaults $false -SCLDeleteEnabled $false -SCLJunkEnabled $false -SCLQuarantineEnabled $false -SCLRejectEnabled $false -HiddenFromAddressListsEnabled $true -DisplayName $dispName -Management:$true -Force;  
   }  
   else  
   {  
   Write-ExchangeSetupLog -Info ("Cannot find migration mailbox with name=$mailboxId.");  
   }  
   }  
 " was run: "Microsoft.Exchange.Data.DataValidationException: Database is mandatory on UserMailbox.".
```

Error:    

The following error was generated when "$error.Clear();    

if (!$RoleIsDatacenter -and !$RoleIsDatacenterDedicated)    

{    

$mailboxId = [Microsoft.Exchange.Management.Migration.MigrationService.Batch.MigrationBatchIdParameter]::MigrationMailboxName;    

$dispName = "Microsoft Exchange Migration";    

$mbxs = @(Get-Mailbox -Arbitration -DomainController $RoleDomainController -Filter {Name -eq $mailboxId});    

$migrationMailbox = $null;    

```
if ($mbxs.Length -eq 0)  
   {  
   Write-ExchangeSetupLog -Info ("Retrieving mailbox databases on Server=$RoleFqdnOrName.");  
   $dbs = @(Get-MailboxDatabase -Server:$RoleFqdnOrName -DomainController $RoleDomainController);  
   if ($dbs.Length -ne 0)  
   {  
   Write-ExchangeSetupLog -Info ("Retrieving users with Name=$mailboxId.");  
   $arbUsers = @(Get-User -Filter {Name -eq $mailboxId} -IgnoreDefaultScope -ResultSize 1);  
   if ($arbUsers.Length -ne 0)  
   {  
   Write-ExchangeSetupLog -Info ("Enabling mailbox $mailboxId.");  
   $migrationMailbox = Enable-Mailbox -Arbitration -Identity $arbUsers[0] -DisplayName $dispName -database $dbs[0].Identity;  
   }  
   }  
   }  
   else  
   {  
   $migrationMailbox = $mbxs[0];  
   }  
   # Set the Organization Capabilities and quotas needed for this mailbox  
   if ($migrationMailbox -ne $null)  
   {  
   Set-Mailbox -Arbitration -Identity $migrationMailbox -ProhibitSendReceiveQuota 300MB -ProhibitSendQuota 300MB -IssueWarningQuota 150MB -RecoverableItemsQuota 30GB -RecoverableItemsWarningQuota 20GB -UseDatabaseQuotaDefaults $false -SCLDeleteEnabled $false -SCLJunkEnabled $false -SCLQuarantineEnabled $false -SCLRejectEnabled $false -HiddenFromAddressListsEnabled $true -DisplayName $dispName -Management:$true -Force;  
   }  
   else  
   {  
   Write-ExchangeSetupLog -Info ("Cannot find migration mailbox with name=$mailboxId.");  
   }  
   }  
 " was run: "Microsoft.Exchange.Data.DataValidationException: Database is mandatory on UserMailbox.
```

at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)    

at Microsoft.Exchange.Configuration.Tasks.Task.WriteError(Exception exception, ErrorCategory category, Object target, Boolean reThrow)    

at Microsoft.Exchange.Configuration.Tasks.DataAccessTask`1.Validate(TDataObject dataObject)     at Microsoft.Exchange.Configuration.Tasks.SetTaskBase`1.InternalValidate()    

at Microsoft.Exchange.Configuration.Tasks.SetRecipientObjectTask`3.InternalValidate()     at Microsoft.Exchange.Management.Common.SetMailEnabledRecipientObjectTask`3.InternalValidate()    

at Microsoft.Exchange.Management.RecipientTasks.SetUserBase`3.InternalValidate()     at Microsoft.Exchange.Management.RecipientTasks.SetMailboxBase`3.InternalValidate()    

at Microsoft.Exchange.Management.RecipientTasks.SetMailbox.InternalValidate()    

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()    

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".    

We have checked that. Arbitration and Migration Mailbox exists with database.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-03-31*

@Yuki Sun-MSFT       

Sorry for the late response.    

I had checked the homeMDB attribute of the migration mailbox is identical to the value of homeMDB for the other arbitration mailboxes. As you suggested, I had moved the arbitration mailboxes to another database but the issue persisted.    

Exchange 2019 CU9 installation issue is resolved after 4 days of tiresome troubleshooting. I have found that the issue was Public Folder Mailbox which database is not exist. After setting the database, the issue is resolved.    

Please someone accept this answer and upvote it if this answer is helpful.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-22*

Hi @Al Amran  ,    

Please ensure that all the Exchange Server prerequisites have been installed and it's also recommended to follow the best practices listed here when installing the Exchange 2019 CU9.    

Besides, as regards to the error message you shared above, I'd suggest trying to recreate the Microsoft Exchange Migration mailbox and see if there would be any improvement:    

 1.Remove the existent migration system mailbox via ADUC > CN=Users:    

    

 2.Run the Get-Mailbox -Arbitration command again to verify that it's really removed. Then run the command below (from the correct installation media by the way) to recreate the Arbitration Mailbox:     

```
Setup.exe /PrepareAD /IAcceptExchangeServerLicenseTerms
```

 3.Run the following command in Exchange Management Shell, :     

```
Enable-Mailbox -Arbitration -Identity "Migration.8f3e7716-2011-43e4-96b1-aba62d229136"  
Set-Mailbox "Migration.8f3e7716-2011-43e4-96b1-aba62d229136" -Arbitration -Management:$True -Force
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-21*

Did you run each Forest Prep Step Individually?    

If not, try that:    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2019    

```
Run each step separately:
```

   Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareSchema    

   Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAD    

   Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAllDomains
