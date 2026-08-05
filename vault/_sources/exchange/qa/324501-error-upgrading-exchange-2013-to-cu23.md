---
title: "Error upgrading exchange 2013 to cu23."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/324501/error-upgrading-exchange-2013-to-cu23
question_id: 324501
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Error upgrading exchange 2013 to cu23.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/324501/error-upgrading-exchange-2013-to-cu23 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Error:  

The following error was generated when "$error.Clear();  

if (($RoleIsDatacenter -ne $true) -and ($RoleIsDatacenterDedicated -ne $true))  

{  

if (test-ExchangeServersWriteAccess -DomainController $RoleDomainController -ErrorAction SilentlyContinue)  

{  

$sysMbx = $null;  

$name = "SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}";  

$dispname = "Microsoft Exchange";  

$mbxs = @( get-mailbox -arbitration -Filter {name -eq $name} -IgnoreDefaultScope -resultSize 1 );  

if ( $mbxs.length -eq 0)  

{  

$dbs = @(get-MailboxDatabase -Server:$RoleFqdnOrName -DomainController $RoleDomainController);  

if ($dbs.Length -ne 0)  

{  

$arbUsers = @(get-user -Filter {name -eq $name} -IgnoreDefaultScope -ResultSize 1);  

if ($arbUsers.Length -ne 0)  

{  

$sysMbx = enable-mailbox -Arbitration -identity $arbUsers[0] -DisplayName $dispname -database $dbs[0].Identity;  

}  

}  

}  

else  

{  

if ($mbxs[0].DisplayName -ne $dispname )  

{  

set-mailbox -Arbitration -identity $mbxs[0] -DisplayName $dispname -Force;  

}  

$sysMbx = $mbxs[0];  

}

```
# Set the Organization Capabilities needed for this mailbox
      if ($sysMbx -ne $null)
      {
      Write-ExchangeSetupLog -Info ("Setting mailbox properties.");
      set-mailbox -Arbitration -identity $sysMbx -UMDataStorage:$true -Force;

      # No RetentionPolicy assigned to E-Discovery arbitration mailbox currently, we need to set it here.
      # This can be remove after BUG(O15#2555914) is fixed.
      if ($sysMbx.RetentionPolicy -eq $null )
      {
      $arbitrationRetentionPolicy = @(Get-RetentionPolicy -DomainController $RoleDomainController | where {$_.Name -eq 'ArbitrationMailbox'});
      set-mailbox -Arbitration -identity $sysMbx -RetentionPolicy $arbitrationRetentionPolicy[0].Identity -Force;
      }
      }
      else
      {
      Write-ExchangeSetupLog -Info ("Cannot find E-discovery arbitration mailbox with name=$name.");
      }
      }
      else
      {
      write-exchangesetuplog -info "Skipping creating Discovery Arbitration Mailbox because of insufficient permission."
      }
      }
    " was run: "Microsoft.Exchange.Data.DataValidationException: Database is mandatory on UserMailbox.".
```

Error:  

The following error was generated when "$error.Clear();  

if (($RoleIsDatacenter -ne $true) -and ($RoleIsDatacenterDedicated -ne $true))  

{  

if (test-ExchangeServersWriteAccess -DomainController $RoleDomainController -ErrorAction SilentlyContinue)  

{  

$sysMbx = $null;  

$name = "SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}";  

$dispname = "Microsoft Exchange";  

$mbxs = @( get-mailbox -arbitration -Filter {name -eq $name} -IgnoreDefaultScope -resultSize 1 );  

if ( $mbxs.length -eq 0)  

{  

$dbs = @(get-MailboxDatabase -Server:$RoleFqdnOrName -DomainController $RoleDomainController);  

if ($dbs.Length -ne 0)  

{  

$arbUsers = @(get-user -Filter {name -eq $name} -IgnoreDefaultScope -ResultSize 1);  

if ($arbUsers.Length -ne 0)  

{  

$sysMbx = enable-mailbox -Arbitration -identity $arbUsers[0] -DisplayName $dispname -database $dbs[0].Identity;  

}  

}  

}  

else  

{  

if ($mbxs[0].DisplayName -ne $dispname )  

{  

set-mailbox -Arbitration -identity $mbxs[0] -DisplayName $dispname -Force;  

}  

$sysMbx = $mbxs[0];  

}

```
# Set the Organization Capabilities needed for this mailbox
      if ($sysMbx -ne $null)
      {
      Write-ExchangeSetupLog -Info ("Setting mailbox properties.");
      set-mailbox -Arbitration -identity $sysMbx -UMDataStorage:$true -Force;

      # No RetentionPolicy assigned to E-Discovery arbitration mailbox currently, we need to set it here.
      # This can be remove after BUG(O15#2555914) is fixed.
      if ($sysMbx.RetentionPolicy -eq $null )
      {
      $arbitrationRetentionPolicy = @(Get-RetentionPolicy -DomainController $RoleDomainController | where {$_.Name -eq 'ArbitrationMailbox'});
      set-mailbox -Arbitration -identity $sysMbx -RetentionPolicy $arbitrationRetentionPolicy[0].Identity -Force;
      }
      }
      else
      {
      Write-ExchangeSetupLog -Info ("Cannot find E-discovery arbitration mailbox with name=$name.");
      }
      }
      else
      {
      write-exchangesetuplog -info "Skipping creating Discovery Arbitration Mailbox because of insufficient permission."
      }
      }
    " was run: "Microsoft.Exchange.Data.DataValidationException: Database is mandatory on UserMailbox.
```

at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)  

at Microsoft.Exchange.Configuration.Tasks.Task.WriteError(Exception exception, ErrorCategory category, Object target, Boolean reThrow)  

at Microsoft.Exchange.Configuration.Tasks.DataAccessTask`1.Validate(TDataObject dataObject)    at Microsoft.Exchange.Configuration.Tasks.SetTaskBase`1.InternalValidate()  

at Microsoft.Exchange.Configuration.Tasks.SetRecipientObjectTask`3.InternalValidate()    at Microsoft.Exchange.Management.Common.SetMailEnabledRecipientObjectTask`3.InternalValidate()  

at Microsoft.Exchange.Management.RecipientTasks.SetUserBase`2.InternalValidate()    at Microsoft.Exchange.Management.RecipientTasks.SetMailboxBase`2.InternalValidate()  

at Microsoft.Exchange.Management.RecipientTasks.SetMailbox.InternalValidate()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__b()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-06-09*

I was getting somewhere wilh this https://learn.microsoft.com/en-us/exchange/security-and-compliance/in-place-ediscovery/delete-and-re-create-default-discovery-mailbox#Overview

```
Add-MailboxPermission "DiscoverySearchMailbox{D919BA05-46A6-415f-80AD-7E09334BB852}" -User "Discovery Management" -AccessRights FullAccess -InheritanceType all
```

and I got error 

Add-MailboxPermission: The operation couldn't be performed because 'DiscoverySearchMailbox{D919BA05-46A6-415f-80AD-7E09334BB852}' matches multiple entries.

this sounds like what stopped the installer.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-26*

Put in a call with Microsoft.  The Distinguished name was copied into the homeDB value.  After this was done, reran the update and all was good.  Thanks for your help.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-23*

Hi @PABLO   ,    

From the result we could see the following arbitration mailboxes(System mailboxes) are corrupted, so we should first repair them to install the update.    

-  SystemMailbox{1f05a927-d349-42cf-a6a6-f5aea5feab7c}    

-  FederatedEmail.4c1f4d8b-8179-4148-93bf-00a95fa1e042     

-  SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}    

Please first check it with:    

-  Open ADSI EDIT and connect to default naming context partition.    

-  Expand CN=Users so you'll find the above CN=SystemMailbox and CN=FederatedEmail units, right click the corrupted ones and click Properties.    

-  From the Attribute Editor, find homeMDB, check if it's <not set> or null, if so you could copy the right value from the other system mailbox like SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c}.    

-  If the homeMDB values of these system mailboxes are good, you could consider recreate them with Recreating arbitration mailboxes    

After fixed these errors, retry installing the update.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-22*

Hi @PABLO   ,

We could get some useful message from the errors you posted, like:

Write-ExchangeSetupLog -Info ("Cannot find E-discovery arbitration mailbox with name=$name.")

This refers to the error message that will be wrote to the ExchangeSetupLogs.  

Based on my knowledge, this is because something is wrong of the arbitration mailboxes.  

So you could first check them with:

```
Get-Mailbox –Arbitration | Select Name,Database
```

If it's right, the result will be five databases as this doc described: Recreating arbitration mailboxes  

Or it's like: https://www.petenetlive.com/KB/Article/0001221  

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

Regards,  

Lou

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
