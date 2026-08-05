---
title: "Exchange 2016.  Set-MailboxAutoReplyConfiguration. Access to the registry key is denied."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/202408/exchange-2016-set-mailboxautoreplyconfiguration-ac
question_id: 202408
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016.  Set-MailboxAutoReplyConfiguration. Access to the registry key is denied.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/202408/exchange-2016-set-mailboxautoreplyconfiguration-ac (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

Please assist with setting proper permissions for a Service Account.

I have got a task from business to make scheduled task on Exchange Server 2016. Action - setting Automatic Reply to a mailbox.  

Have prepared script for that, but, when I run script under service account in PowerShell (to test it, if there are any errors or not, since Task Scheduler does not shows errors), I am getting such error:

PS C:\Users\aaa> C:_Scripts\AutoReplyState.ps1  

WARNING: An unexpected error has occurred and a Watson dump is being generated: Access to the registry key 'HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\AssistantsQuarantine\1c33ea3f-ed68-4671-95d5-f29d599e2e51\powershell_ise\PoisonControl\PoisonControlComposite' is denied.

WARNING: Task module "ReportExceptionModule.ReportException" fails with exception "Access to the path 'C:\ExchangeSetupLogs\ExchangeSetupWatson.log' is denied.". This module is skipped. Task execution result should not be affected.

Set-MailboxAutoReplyConfiguration : Access to the registry key 'HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\AssistantsQuarantine\1c33ea3f-ed68-4671-95d5-f29d599e2e51\powershell_ise\PoisonControl\PoisonControlComposite' is denied.

At C:_Scripts\AutoReplyState.ps1:18 char:1  

-  Set-MailboxAutoReplyConfiguration -identity XXX -AutoReplyState ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : NotSpecified: (:) [Set-MailboxAutoReplyConfiguration], UnauthorizedAccessException  

-  FullyQualifiedErrorId : System.UnauthorizedAccessException,Microsoft.Exchange.Management.StoreTasks.SetMailboxAutoReplyConfiguration

My script does:  

Set-MailboxAutoReplyConfiguration -identity XXX -AutoReplyState Scheduled -StartTime "$month/20/$year 12:00 AM" -EndTime "$month/$LastDayOfMonth/$year 12:00 PM" -InternalMessage $text -ExternalMessage $text;

This is something with missing permissions.

When I run same script under Exchange Admin account, it works fine. Please assist, which permissions should I set to a service account to be able to run successfully PowerShell command:  

Set-MailboxAutoReplyConfiguration

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-21*

Hi,    

I have got this result:    

```
[PS] C:\WINDOWS\system32>$Perms = Get-ManagementRole -Cmdlet Set-MailboxAutoReplyConfiguration  
[PS] C:\WINDOWS\system32>$perms  
  
Name            RoleType  
----            --------  
User Options    UserOptions  
MyBaseOptions   MyBaseOptions  
Mail Recipients MailRecipients  
  
  
[PS] C:\WINDOWS\system32>$Perms | foreach {Get-ManagementRoleAssignment -Role $_.Name -Delegating $false | Format-Table  
-Auto Role,RoleAssigneeType,RoleAssigneeName}  
  
Role         RoleAssigneeType RoleAssigneeName  
----         ---------------- ----------------  
User Options        RoleGroup Help Desk  
User Options        RoleGroup Organization Management  
  
  
Role              RoleAssigneeType RoleAssigneeName  
----              ---------------- ----------------  
MyBaseOptions RoleAssignmentPolicy Default Role Assignment Policy  
  
  
Role            RoleAssigneeType RoleAssigneeName  
----            ---------------- ----------------  
Mail Recipients        RoleGroup Organization Management  
Mail Recipients        RoleGroup Recipient Management  
Mail Recipients        RoleGroup BackupExecRoles
```

What I did next - opened ECP and added my SVC account into 2 RoleGroups:    

-  Help Desk;    

-  Recipient Management.    

From Exchange management shell run command:    

```
[PS] C:\WINDOWS\system32>Get-ManagementRoleAssignment -RoleAssignee "svc" -Delegating $false | Format-Table -Auto Role,RoleAssigneeName,RoleAssigneeType  
  
Role                        RoleAssigneeName     RoleAssigneeType  
----                        ----------------     ----------------  
Mail Enabled Public Folders Recipient Management        RoleGroup  
Move Mailboxes              Recipient Management        RoleGroup  
Mail Recipient Creation     Recipient Management        RoleGroup  
Recipient Policies          Recipient Management        RoleGroup  
Migration                   Recipient Management        RoleGroup  
Message Tracking            Recipient Management        RoleGroup  
Mail Recipients             Recipient Management        RoleGroup  
Distribution Groups         Recipient Management        RoleGroup  
Team Mailboxes              Recipient Management        RoleGroup  
View-Only Recipients        Help Desk                   RoleGroup  
User Options                Help Desk                   RoleGroup
```

And still I am unable to execute script with that SVC account and getting same:    

```
PS C:\_Scripts> .\AutoReplyState.ps1  
Set-MailboxAutoReplyConfiguration : Cannot open mailbox /o=COMPANYNAME/ou=Exchange Administrative Group  
(FYDIBOHF23SPDLT)/cn=Configuration/cn=Servers/cn=YYY/cn=Microsoft System Attendant.  
At C:\_Scripts\AutoReplyState.ps1:26 char:1  
+ Set-MailboxAutoReplyConfiguration -identity XXX -AutoReplyState  ...  
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
    + CategoryInfo          : NotSpecified: (:) [Set-MailboxAutoReplyConfiguration], ConnectionFailedTransientExceptio  
   n  
    + FullyQualifiedErrorId : [Server=YYY,RequestId=b2c7102f-e7e9-41b5-8094-764aeab6d446,TimeStamp=12/21/2020 1:36:  
   48 PM] [FailureCategory=Cmdlet-ConnectionFailedTransientException] 3FCFF55A,Microsoft.Exchange.Management.StoreTas  
  ks.SetMailboxAutoReplyConfiguration
```

    

Please kindly assist, what I did wrong?    

Should I assign a mailbox to SVC account to accomplish the task?
