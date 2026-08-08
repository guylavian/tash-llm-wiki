---
title: "Exchange Server 2013 CU9 to CU23 update error Management.RecipientTasks."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1161625/exchange-server-2013-cu9-to-cu23-update-error-mana
question_id: 1161625
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Exchange Server 2013 CU9 to CU23 update error Management.RecipientTasks.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1161625/exchange-server-2013-cu9-to-cu23-update-error-mana (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
Error:
The following error was generated when "$error.Clear(); 
          $name = [Microsoft.Exchange.Management.RecipientTasks.EnableMailbox]::DiscoveryMailboxUniqueName;
          $dispname = [Microsoft.Exchange.Management.RecipientTasks.EnableMailbox]::DiscoveryMailboxDisplayName;
          $dismbx = get-mailbox -Filter {name -eq $name} -IgnoreDefaultScope -resultSize 1;
          if( $dismbx -ne $null)
          {
          $srvname = $dismbx.ServerName;
          if( $dismbx.Database -ne $null -and $RoleFqdnOrName -like "$srvname.*" )
          {
          Write-ExchangeSetupLog -info "Setup DiscoverySearchMailbox Permission.";
          $mountedMdb = get-mailboxdatabase $dismbx.Database -status | where { $_.Mounted -eq $true };
          if( $mountedMdb -eq $null )
          {
          Write-ExchangeSetupLog -info "Mounting database before stamp DiscoverySearchMailbox Permission...";
          mount-database $dismbx.Database;
          }

          $mountedMdb = get-mailboxdatabase $dismbx.Database -status | where { $_.Mounted -eq $true };
          if( $mountedMdb -ne $null )
          {
          $dmRoleGroupGuid = [Microsoft.Exchange.Data.Directory.Management.RoleGroup]::DiscoveryManagement_InitInfo.WellKnownGuid;
          $dmRoleGroup = Get-RoleGroup -Identity $dmRoleGroupGuid -DomainController $RoleDomainController -ErrorAction:SilentlyContinue;
          if( $dmRoleGroup -ne $null )
          {
            trap [Exception]
            {
              Add-MailboxPermission $dismbx -User $dmRoleGroup.Name -AccessRights FullAccess -DomainController $RoleDomainController -ErrorAction SilentlyContinue;
              continue;
            }
            
            Add-MailboxPermission $dismbx -User $dmRoleGroup.Identity -AccessRights FullAccess -DomainController $RoleDomainController -WarningAction SilentlyContinue;
          }
          }
          }
          }
        " was run: "Microsoft.Exchange.Data.Common.LocalizedException: Couldn't resolve the user or group "xxxxxx.local/Microsoft Exchange Security Groups/Discovery Management." If the user or group is a foreign forest principal, you must have either a two-way trust or an outgoing trust. ---> System.SystemException: The trust relationship between the primary domain and the trusted domain failed.

   at System.Security.Principal.NTAccount.TranslateToSids(IdentityReferenceCollection sourceAccounts, Boolean& someFailed)
   at System.Security.Principal.NTAccount.Translate(IdentityReferenceCollection sourceAccounts, Type targetType, Boolean forceSuccess)
   at System.Security.Principal.NTAccount.Translate(Type targetType)
   at Microsoft.Exchange.Configuration.Tasks.SecurityPrincipalIdParameter.GetUserSidAsSAMAccount(SecurityPrincipalIdParameter user, TaskErrorLoggingDelegate logError, TaskVerboseLoggingDelegate logVerbose)
   --- End of inner exception stack trace ---
   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)
   at Microsoft.Exchange.Configuration.Tasks.Task.WriteError(Exception exception, ErrorCategory category, Object target)
   at Microsoft.Exchange.Configuration.Tasks.SecurityPrincipalIdParameter.GetUserSidAsSAMAccount(SecurityPrincipalIdParameter user, TaskErrorLoggingDelegate logError, TaskVerboseLoggingDelegate logVerbose)
   at Microsoft.Exchange.Configuration.Tasks.SecurityPrincipalIdParameter.GetSecurityPrincipal(IRecipientSession session, SecurityPrincipalIdParameter user, TaskErrorLoggingDelegate logError, TaskVerboseLoggingDelegate logVerbose)
   at Microsoft.Exchange.Management.RecipientTasks.SetMailboxPermissionTaskBase.InternalValidate()
   at Microsoft.Exchange.Management.RecipientTasks.AddMailboxPermission.InternalValidate()
   at Microsoft.Exchange.Configuration.Tasks.Task.b__b()
   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

Error:
The following error was generated when "$error.Clear(); 
          $name = [Microsoft.Exchange.Management.RecipientTasks.EnableMailbox]::DiscoveryMailboxUniqueName;
          $dispname = [Microsoft.Exchange.Management.RecipientTasks.EnableMailbox]::DiscoveryMailboxDisplayName;
          $dismbx = get-mailbox -Filter {name -eq $name} -IgnoreDefaultScope -resultSize 1;
          if( $dismbx -ne $null)
          {
          $srvname = $dismbx.ServerName;
          if( $dismbx.Database -ne $null -and $RoleFqdnOrName -like "$srvname.*" )
          {
          Write-ExchangeSetupLog -info "Setup DiscoverySearchMailbox Permission.";
          $mountedMdb = get-mailboxdatabase $dismbx.Database -status | where { $_.Mounted -eq $true };
          if( $mountedMdb -eq $null )
          {
          Write-ExchangeSetupLog -info "Mounting database before stamp DiscoverySearchMailbox Permission...";
          mount-database $dismbx.Database;
          }

          $mountedMdb = get-mailboxdatabase $dismbx.Database -status | where { $_.Mounted -eq $true };
          if( $mountedMdb -ne $null )
          {
          $dmRoleGroupGuid = [Microsoft.Exchange.Data.Directory.Management.RoleGroup]::DiscoveryManagement_InitInfo.WellKnownGuid;
          $dmRoleGroup = Get-RoleGroup -Identity $dmRoleGroupGuid -DomainController $RoleDomainController -ErrorAction:SilentlyContinue;
          if( $dmRoleGroup -ne $null )
          {
            trap [Exception]
            {
              Add-MailboxPermission $dismbx -User $dmRoleGroup.Name -AccessRights FullAccess -DomainController $RoleDomainController -ErrorAction SilentlyContinue;
              continue;
            }
            
            Add-MailboxPermission $dismbx -User $dmRoleGroup.Identity -AccessRights FullAccess -DomainController $RoleDomainController -WarningAction SilentlyContinue;
          }
          }
          }
          }
        " was run: "Microsoft.Exchange.Data.Common.LocalizedException: Couldn't resolve the user or group "xxxxxxxxx.local/Microsoft Exchange Security Groups/Discovery Management." If the user or group is a foreign forest principal, you must have either a two-way trust or an outgoing trust. ---> System.SystemException: The trust relationship between the primary domain and the trusted domain failed.

   at System.Security.Principal.NTAccount.TranslateToSids(IdentityReferenceCollection sourceAccounts, Boolean& someFailed)
   at System.Security.Principal.NTAccount.Translate(IdentityReferenceCollection sourceAccounts, Type targetType, Boolean forceSuccess)
   at System.Security.Principal.NTAccount.Translate(Type targetType)
   at Microsoft.Exchange.Configuration.Tasks.SecurityPrincipalIdParameter.GetUserSidAsSAMAccount(SecurityPrincipalIdParameter user, TaskErrorLoggingDelegate logError, TaskVerboseLoggingDelegate logVerbose)
   --- End of inner exception stack trace ---
   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)
   at Microsoft.Exchange.Configuration.Tasks.Task.WriteError(Exception exception, ErrorCategory category, Object target)
   at Microsoft.Exchange.Configuration.Tasks.SecurityPrincipalIdParameter.GetUserSidAsSAMAccount(SecurityPrincipalIdParameter user, TaskErrorLoggingDelegate logError, TaskVerboseLoggingDelegate logVerbose)
   at Microsoft.Exchange.Configuration.Tasks.SecurityPrincipalIdParameter.GetSecurityPrincipal(IRecipientSession session, SecurityPrincipalIdParameter user, TaskErrorLoggingDelegate logError, TaskVerboseLoggingDelegate logVerbose)
   at Microsoft.Exchange.Management.RecipientTasks.SetMailboxPermissionTaskBase.InternalValidate()
   at Microsoft.Exchange.Management.RecipientTasks.AddMailboxPermission.InternalValidate()
   at Microsoft.Exchange.Configuration.Tasks.Task.b__b()
   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-17*

Have you tried to establish a trust relationship between the primary domain and the trusted domain?

This can typically be done by creating a two-way trust between the domains, or by creating an outgoing trust from the primary domain to the trusted domain.

You may also want to check that the group name, and the domain name is correct, and verify that the group exists on the domain.

If you are unable to establish a trust relationship, you can try to run the script on a domain controller of the trusted domain and see if that resolves the issue.
