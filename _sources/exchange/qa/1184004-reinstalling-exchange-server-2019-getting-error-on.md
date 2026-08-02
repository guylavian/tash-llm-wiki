---
title: "Reinstalling Exchange server 2019 getting error on Step 7"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1184004/reinstalling-exchange-server-2019-getting-error-on
question_id: 1184004
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Reinstalling Exchange server 2019 getting error on Step 7

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1184004/reinstalling-exchange-server-2019-getting-error-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Gurus!  I have been tasked with setting up a test Exchange server and running in to an issue.  A little back story.  I did have a working Exchange 2019 server running last year, but we were hit with a Ransomware attack and decided not to restore that server.  Fast forward to earlier this month.  I created a new Exchange 2019 server and was working perfectly UNTIL the last patch Tuesday updates which broke Secure Boot with the VM and Server 2022.  I did not know about the bug until after I had deleted the VM.  Now I am trying to set everything up again, and when the Setup get's to step 7 I see this error.

Error: The following error was generated when "$error.Clear(); if ( ($server -eq $null) -and ($RoleIsDatacenter -ne $true) ) { Update-RmsSharedIdentity -ServerName $RoleNetBIOSName } " was run: "Microsoft.Exchange.Data.DataValidationException: Database is mandatory on UserMailbox. at Microsoft.Exchange.Data.Directory.ADDataSession.Save(ADObject instanceToSave, IEnumerable`1 properties, Boolean bypassValidation) at Microsoft.Exchange.Data.Directory.Recipient.ADRecipientObjectSession.Save(ADRecipient instanceToSave, String callerFilePath, Int32 callerFileLine, String memberName) at Microsoft.Exchange.Management.Deployment.UpdateRmsSharedIdentity.Link() at Microsoft.Exchange.Management.Deployment.UpdateRmsSharedIdentity.InternalProcessRecord() at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1() at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)"

Can someone shed some light on how to resolve this?  Many many thanks in advance!!

EDIT:

Did an uninstall, rebooted and when through the setup process aain (prepare schema etc).  Now getting this error.

```
Error:
The following error was generated when "$error.Clear(); 
          $feVdirName = "PowerShell (Default Web Site)";
          $beVdirName = "PowerShell (Exchange Back End)";
          $vdirName = "PowerShell";
          $InternalPowerShellUrl="http://" + $RoleFqdnOrName + "/powershell";

          $vdir = get-PowerShellVirtualDirectory -ShowMailboxVirtualDirectories -server $RoleFqdnOrName -DomainController $RoleDomainController | where { $_.Name -eq $beVdirName };
          if ($vdir -eq $null)
          {
            new-PowerShellVirtualDirectory $vdirName -Role Mailbox -DomainController $RoleDomainController -BasicAuthentication:$false -WindowsAuthentication:$true -RequireSSL:$true -WebSiteName "Exchange Back End" -Path ($RoleInstallPath + "ClientAccess\PowerShell-Proxy");
          }
          else
          {
            update-PowerShellVirtualDirectoryVersion -DomainController $RoleDomainController;
          }

          $vdir2 = get-PowerShellVirtualDirectory -ShowMailboxVirtualDirectories -server $RoleFqdnOrName -DomainController $RoleDomainController | where { $_.Name -eq $feVdirName };
          if ($vdir2 -eq $null)
          {
            new-PowerShellVirtualDirectory $vdirName -Role Mailbox -InternalUrl $InternalPowerShellUrl -DomainController $RoleDomainController -BasicAuthentication:$false -WindowsAuthentication:$false -RequireSSL:$false -WebSiteName "Default Web Site" -AppPoolId "MSExchangePowerShellFrontEndAppPool";
          }
          else
          {
            update-PowerShellVirtualDirectoryVersion -DomainController $RoleDomainController;
          }
        " was run: "System.ArgumentException: The virtual directory 'PowerShell' already exists under 'xxx.xxx.com/Default Web Site'.
Parameter name: VirtualDirectoryName
   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)
   at Microsoft.Exchange.Management.SystemConfigurationTasks.NewExchangeVirtualDirectory`1.InternalValidate()
   at Microsoft.Exchange.Configuration.Tasks.Task.b__91_1()
   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".
```

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-27*

Hi @Anonymous  ,

Since this forum is public, I have modified the question to cover the FQDN of your Exchange server.  

For security reasons, please don't forget to hide your personal information in the post.

Thanks for your understanding!

According to the log, the error messages are:

`The virtual directory 'PowerShell' already exists under 'xxx.xxx.com/Default Web Site'`

 

You can try the following steps to resolve the issues:

-  Please try to remove the PowerShell Virtual Directory under Default Website and Exchange Back End Website through IIS Manager. 

-  Please open ADSIEdit and connect to Configuration. Locate CN=Configuration, DC=domain, DC=[your domain]/CN=Services/CN=Microsoft Exchange/CN=[your domain]/CN=Administrative Groups/CN=Exchange Administrative Groups/CN=Servers/CN=[your server]/CN=Protocols/CN=HTTP. Delete the PowerShell items like the below. Then have a reinstallation again.

-  

Please note that: Using ADSIEdit is dangerous and can cause serious problems to your environment if not performed correctly. Please make sure to have a full backup of your AD and Exchange servers in case something goes wrong.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
