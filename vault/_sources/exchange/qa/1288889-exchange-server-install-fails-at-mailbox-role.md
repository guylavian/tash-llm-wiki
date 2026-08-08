---
title: "Exchange server install fails at mailbox role"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1288889/exchange-server-install-fails-at-mailbox-role
question_id: 1288889
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Exchange server install fails at mailbox role

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1288889/exchange-server-install-fails-at-mailbox-role (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am getting this error after on-prem Exchange 2019 crashed and needs to be rebuilt. I have tried to uninstall and install again to no avail. Can you help?

```
Microsoft Exchange Server 2019 Cumulative Update 13 Unattended Setup

Copying Files...
File copy complete. Setup will now collect additional information needed for installation.

Languages
Management tools
Mailbox role: Transport service
Mailbox role: Client Access service
Mailbox role: Mailbox service
Mailbox role: Front End Transport service
Mailbox role: Client Access Front End service

Performing Microsoft Exchange Server Prerequisite Check

    Configuring Prerequisites                                                                         COMPLETED
    Prerequisite Analysis                                                                             COMPLETED

Configuring Microsoft Exchange Server

    Preparing Setup                                                                                   COMPLETED
    Stopping Services                                                                                 COMPLETED
    Copying Exchange Files                                                                            COMPLETED
    Language Files                                                                                    COMPLETED
    Restoring Services                                                                                COMPLETED
    Language Configuration                                                                            COMPLETED
    Exchange Management Tools                                                                         COMPLETED
    Mailbox role: Transport service                                                                   FAILED

The following error was generated when "$error.Clear();
 $feVdirName = "PowerShell (Default Web Site)";
 $beVdirName =
"PowerShell (Exchange Back End)";
 $vdirName = "PowerShell";
 $InternalPowerShellUrl="http://" + $RoleFqdnOrName +
"/powershell";

 $vdir = get-PowerShellVirtualDirectory -ShowMailboxVirtualDirectories -server $RoleFqdnOrName
-DomainController $RoleDomainController | where { $_.Name -eq $beVdirName };
 if ($vdir -eq $null)
 {

new-PowerShellVirtualDirectory $vdirName -Role Mailbox -DomainController $RoleDomainController
-BasicAuthentication:$false -WindowsAuthentication:$true -RequireSSL:$true -WebSiteName "Exchange Back End" -Path
($RoleInstallPath + "ClientAccess\PowerShell-Proxy");
 }
 else
 {
 update-PowerShellVirtualDirectoryVersion
-DomainController $RoleDomainController;
 }

 $vdir2 = get-PowerShellVirtualDirectory -ShowMailboxVirtualDirectories
-server $RoleFqdnOrName -DomainController $RoleDomainController | where { $_.Name -eq $feVdirName };
 if ($vdir2 -eq
$null)
 {
 new-PowerShellVirtualDirectory $vdirName -Role Mailbox -InternalUrl $InternalPowerShellUrl -DomainController
$RoleDomainController -BasicAuthentication:$false -WindowsAuthentication:$false -RequireSSL:$false -WebSiteName
"Default Web Site" -AppPoolId "MSExchangePowerShellFrontEndAppPool";
 }
 else
 {

update-PowerShellVirtualDirectoryVersion -DomainController $RoleDomainController;
 }
 " was run:
"System.ArgumentException: The virtual directory 'PowerShell' already exists under 'ex201901.wachtell.local/Default Web
Site'.
Parameter name: VirtualDirectoryName
 at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception
exception, ErrorCategory errorCategory, Object target, String helpUrl)
 at
Microsoft.Exchange.Management.SystemConfigurationTasks.NewExchangeVirtualDirectory`1.InternalValidate()
 at
Microsoft.Exchange.Configuration.Tasks.Task.b__91_1()
 at
Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean
terminatePipelineIfFailed)".

The Exchange Server setup operation didn't complete. More details can be found in ExchangeSetup.log located in the
:\ExchangeSetupLogs folder.
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-22*

Make sure your server meets the prerequisites of Exchange Server 2019 and Setup wizard: Windows Server 2019 prerequisites for Exchange 2019, Install Exchange Mailbox servers using the Setup wizard, and Install Exchange Cumulative Updates.

For the users who can install Exchange on servers that have already been provisioned in Active Directory by an Exchange administrator: Delegate the installation of Exchange servers

Also, check this thread for help - https://www.experts-exchange.com/dashboard/#/questions/29233485

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.
