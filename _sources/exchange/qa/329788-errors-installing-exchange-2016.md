---
title: "Errors installing Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/329788/errors-installing-exchange-2016
question_id: 329788
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Errors installing Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/329788/errors-installing-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an environment with an 2013 Exchange server and I am attempting to migrate this to a 2016 Exchange server. All of the perquisites are met and the install starts but on step 6 (mailbox role:Transport service) it fails because it is trying to install Exchange 2007 Standard Anti-spam Filter Updates.![81176-exchange-2007-anti-spam.jpg][1] [1]: /api/attachments/81176-exchange-2007-anti-spam.jpg?platform=QnA Here are the details of the error: Microsoft Exchange Server 2016 Cumulative Update 19 Unattended Setup Copying Files... File copy complete. Setup will now collect additional information needed for installation. Languages Mailbox role: Transport service Mailbox role: Client Access service Mailbox role: Unified Messaging service Mailbox role: Mailbox service Mailbox role: Front End Transport service Mailbox role: Client Access Front End service Performing Microsoft Exchange Server Prerequisite Check Configuring Prerequisites COMPLETED Prerequisite Analysis 100% MAPI over HTTP, the preferred Outlook desktop client connectivity with Exchange server, is currently not enabled. Consider enabling it using: Set-OrganizationConfig -MapiHttpEnabled $true For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.WarnMapiHttpNotEnabled.aspx Configuring Microsoft Exchange Server Preparing Setup COMPLETED Stopping Services COMPLETED Copying Exchange Files COMPLETED Language Files COMPLETED Restoring Services COMPLETED Language Configuration COMPLETED Mailbox role: Transport service 100% The following error was generated when "$error.Clear(); $feVdirName = "PowerShell (Default Web Site)"; $beVdirName = "PowerShell (Exchange Back End)"; $vdirName = "PowerShell"; $InternalPowerShellUrl="http://" + $RoleFqdnOrName + "/powershell"; $vdir = get-PowerShellVirtualDirectory -ShowMailboxVirtualDirectories -server $RoleFqdnOrName -DomainController $RoleDomainController | where { $.Name -eq $beVdirName }; if ($vdir -eq $null) { new-PowerShellVirtualDirectory $vdirName -Role Mailbox -DomainController $RoleDomainController -BasicAuthentication:$false -WindowsAuthentication:$true -RequireSSL:$true -WebSiteName "Exchange Back End" -Path ($RoleInstallPath + "ClientAccess\PowerShell-Proxy"); } else { update-PowerShellVirtualDirectoryVersion -DomainController $RoleDomainController; } $vdir2 = get-PowerShellVirtualDirectory -ShowMailboxVirtualDirectories -server $RoleFqdnOrName -DomainController $RoleDomainController | where { $.Name -eq $feVdirName }; if ($vdir2 -eq $null) { new-PowerShellVirtualDirectory $vdirName -Role Mailbox -InternalUrl $InternalPowerShellUrl -DomainController $RoleDomainController -BasicAuthentication:$false -WindowsAuthentication:$false -RequireSSL:$false -WebSiteName "Default Web Site" -AppPoolId "MSExchangePowerShellFrontEndAppPool"; } else { update-PowerShellVirtualDirectoryVersion -DomainController $RoleDomainController; } " was run: "System.ArgumentException: The virtual directory 'PowerShell' already exists under '<servername>/Exchange Back End'. Parameter name: VirtualDirectoryName at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl) at Microsoft.Exchange.Management.SystemConfigurationTasks.NewExchangeVirtualDirectory`1.InternalValidate() at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1() at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)". The following error was generated when "$error.Clear(); $feVdirName = "PowerShell (Default Web Site)"; $beVdirName = "PowerShell (Exchange Back End)"; $vdirName = "PowerShell"; $InternalPowerShellUrl="http://" + $RoleFqdnOrName + "/powershell"; $vdir = get-PowerShellVirtualDirectory -ShowMailboxVirtualDirectories -server $RoleFqdnOrName -DomainController $RoleDomainController | where { $_.Name -eq $beVdirName }; if ($vdir -eq $null) { new-PowerShellVirtualDirectory $vdirName -Role Mailbox -DomainController $RoleDomainController -BasicAuthentication:$false -WindowsAuthentication:$true -RequireSSL:$true -WebSiteName "Exchange Back End" -Path ($RoleInstallPath + "ClientAccess\PowerShell-Proxy"); } else { update-PowerShellVirtualDirectoryVersion -DomainController $RoleDomainController; } $vdir2 = get-PowerShellVirtualDirectory -ShowMailboxVirtualDirectories -server $RoleFqdnOrName -DomainController $RoleDomainController | where { $_.Name -eq $feVdirName }; if ($vdir2 -eq $null) { new-PowerShellVirtualDirectory $vdirName -Role Mailbox -InternalUrl $InternalPowerShellUrl -DomainController $RoleDomainController -BasicAuthentication:$false -WindowsAuthentication:$false -RequireSSL:$false -WebSiteName "Default Web Site" -AppPoolId "MSExchangePowerShellFrontEndAppPool"; } else { update-PowerShellVirtualDirectoryVersion -DomainController $RoleDomainController; } " was run: "System.ArgumentException: The virtual directory 'PowerShell' already exists under '<servername>/Default Web Site'. Parameter name: VirtualDirectoryName at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl) at Microsoft.Exchange.Management.SystemConfigurationTasks.NewExchangeVirtualDirectory`1.InternalValidate() at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1() at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)". The Exchange Server setup operation didn't complete. More details can be found in ExchangeSetup.log located in the <SystemDrive>:\ExchangeSetupLogs folder.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-25*

Hi, @Orin Eisenhauer       

Since this forum is public, I have modified the question to cover the FQDN of your Exchange server.    

For security reasons, please don't forget to hide your personal information in the post.    

Thanks for your understanding!    

According to the log, the error messages are:    

The virtual directory 'PowerShell' already exists under '<servername>/Exchange Back End'.     

The virtual directory 'PowerShell' already exists under '<servername>/Default Web Site'.    

Please open ADSIEdit and connect to Configuration.    

Locate CN=Configuration,DC="your domain",DC=com>CN=Services>CN=Microsoft Exchange>CN="Organization name">CN=Administrative Groups>CN=Exchange Administrative Groups>CN=Servers>CN="This Exchange 2016 server name">CN=Protocols>CN=HTTP    

Delete the "CN=Powershell (Default Web Site)" and "CN=Powershell (Exchange Back End)" in it.    

And rerun the setup.    

Please note that: Using ADSIEdit is dangerous and can cause serious problems to your environment if not performed correctly.    

Please make sure to have a full backup of your AD and Exchange servers in case something goes wrong.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
