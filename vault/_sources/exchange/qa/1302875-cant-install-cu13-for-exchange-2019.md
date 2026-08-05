---
title: "can't install CU13 for Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1302875/cant-install-cu13-for-exchange-2019
question_id: 1302875
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# can't install CU13 for Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1302875/cant-install-cu13-for-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

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
   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)
   at Microsoft.Exchange.Configuration.Tasks.Task.WriteError(Exception exception, ErrorCategory category, Object target, Boolean reThrow)
   at Microsoft.Exchange.Configuration.Tasks.DataAccessTask`1.Validate(TDataObject dataObject)
   at Microsoft.Exchange.Configuration.Tasks.SetTaskBase`1.InternalValidate()
   at Microsoft.Exchange.Configuration.Tasks.SetRecipientObjectTask`3.InternalValidate()
   at Microsoft.Exchange.Management.Common.SetMailEnabledRecipientObjectTask`3.InternalValidate()
   at Microsoft.Exchange.Management.RecipientTasks.SetUserBase`3.InternalValidate()
   at Microsoft.Exchange.Management.RecipientTasks.SetMailboxBase`3.InternalValidate()
   at Microsoft.Exchange.Management.RecipientTasks.SetMailbox.InternalValidate()
   at Microsoft.Exchange.Configuration.Tasks.Task.b__91_1()
   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".
```

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-06-09*

Sounds like you are missing the discovery mailbox:

See this solution first:

https://learn.microsoft.com/en-us/answers/questions/324501/error-upgrading-exchange-2013-to-cu23

https://learn.microsoft.com/en-us/exchange/architecture/mailbox-servers/recreate-arbitration-mailboxes?view=exchserver-2019#re-create-the-microsoft-exchange-discovery-system-mailbox
