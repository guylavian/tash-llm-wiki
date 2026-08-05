---
title: "Exchange 2016 CU 19 update failed at Mailbox role: Mailbox service"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/301866/exchange-2016-cu-19-update-failed-at-mailbox-role
question_id: 301866
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 CU 19 update failed at Mailbox role: Mailbox service

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/301866/exchange-2016-cu-19-update-failed-at-mailbox-role (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

R:unning CU 19 update on exchange 2016 on server 2012r2 Failed on step 13 of 17 The following error was generated when "$error.Clear(); if (!$RoleIsDatacenter -and !$RoleIsDatacenterDedicated) { $arbUsers = @(get-user -Filter {lastname -eq "MSExchApproval 1f05a927-3be2-4fb9-aa03-b59fe3b56f4c"} -IgnoreDefaultScope -ResultSize 1); if ($arbUsers.Length -ne 0) { $mbxname = $arbUsers[0].name; $mbxs = @( get-mailbox -arbitration -Filter {name -eq $mbxname} -IgnoreDefaultScope -resultSize 1 ); if ( $mbxs.length -eq 0) { $dbs = @(get-MailboxDatabase -Server:$RoleFqdnOrName -DomainController $RoleDomainController); if ($dbs.Length -ne 0) { enable-mailbox -Arbitration -identity $arbUsers[0] -database $dbs[0].Identity; } } } } " was run: "Microsoft.Exchange.Data.DataValidationException: ExternalEmailAddress is mandatory on MailUser. at Microsoft.Exchange.Data.Directory.ADDataSession.Save(ADObject instanceToSave, IEnumerable`1 properties, Boolean bypassValidation) at Microsoft.Exchange.Data.Directory.Recipient.ADRecipientObjectSession.Save(ADRecipient instanceToSave, String callerFilePath, Int32 callerFileLine, String memberName) at Microsoft.Exchange.Data.Directory.Recipient.ADRecipientObjectSession.Microsoft.Exchange.Data.IConfigDataProvider.Save(IConfigurable instance, String callerFilePath, Int32 callerFileLine, String memberName) at Microsoft.Exchange.Management.RecipientTasks.EnableMailbox.PrepareRecipientObject(ADUser& user) at Microsoft.Exchange.Management.RecipientTasks.EnableRecipientObjectTask`2.PrepareDataObject() at Microsoft.Exchange.Configuration.Tasks.SetTaskBase`1.InternalValidate() at Microsoft.Exchange.Configuration.Tasks.RecipientObjectActionTask`2.InternalValidate() at Microsoft.Exchange.Management.RecipientTasks.EnableMailbox.InternalValidate() at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1() at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-08*

I was in the process of running it again before I went to bed, I stopped backup services, antivirus was already stopped. Here are the errors: I can't put in reply it won't fit: Mailbox role: Mailbox service 100% FAILED  

Mailbox role: Mailbox service                             100%  

 FAILED  

The following error was generated when "$error.Clear();  

 If (!$RoleIsDatacenter -and !$RoleIsDatacenterDedicated) {  

 $arbUsers = @(get-user -Filter {lastname -eq "MSExchApproval  

1f05a927-3be2-4fb9-aa03-b59fe3b56f4c"} -IgnoreDefaultScope -ResultSize 1);  

 If ($arbUsers.Length -ne 0)  {  $mbxname = $arbUsers[0].name;  

 $mbxs = @( get-mailbox -arbitration -Filter {name -eq $mbxname} -IgnoreDefaultScope  

-resultSize 1 );  if ( $mbxs.length -eq 0)  {  $dbs = @(get-MailboxDatabase  

-Server:$RoleFqdnOrName -DomainController $RoleDomainController);  

 If ($dbs.Length -ne 0)  {  enable-mailbox -Arbitration -identity $arbUsers[0]  

-database $dbs[0].Identity;  }  }  }  }  " was run: "Microsoft.Exchange.Data.DataValidationException: ExternalEmailAddress is mandatory on MailUser.  At Microsoft.Exchange.Data.Directory.ADDataSession.Save(ADObject instanceToSave,  

IEnumerable`1 properties, Boolean bypassValidation)  at  icrosoft.Exchange.Data.Directory.Recipient.ADRecipientObjectSession.Save(ADReci   Pient instanceToSave, String callerFilePath, Int32 callerFileLine, String memberName)     At Microsoft.Exchange.Data.Directory.Recipient.ADRecipientObjectSession.Microsoft.E   xchange.Data.IConfigDataProvider.Save(IConfigurable   instance, String callerFilePath, Int32 callerFileLine, String memberName)    at Microsoft.Exchange.Management.RecipientTasks.EnableMailbox.PrepareRecipientObjec   t(ADUser& user)  at Microsoft.Exchange.Management.RecipientTasks.EnableRecipientObjectTask`2.Prepare  

DataObject()   at Microsoft.Excha ge.Configuration.Tasks.SetTaskBase`1.InternalValidate()    At Microsoft.Exchange.Configuration.Tasks.RecipientObjectActionTask`2.InternalValid  

ate()  at Microsoft.Exchange.Management.RecipientTasks.EnableMailbox.InternalValidate()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

 at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String  

funcName, Action func, Boolean terminatePipelineIfFailed)".

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-07*

```
Mailbox role: Mailbox service                             FAILED
```

The following error was generated when "$error.Clear();  

If ($RoleProductPlatform -eq "amd64") {  

try { # Need to configure the ETL  

traces before the fast service is installed. This will ensure that when the  

service comes up # it will have the necessary trace session setting available  

to read from the registry $fastPerfEtlTraceFolderPath = Join-Path -Path  

$RoleBinPath -ChildPath "\Search\Ceres\Diagnostics\ETLTraces"  

$fastDiagnosticTracingRegKeyPath = 'HKLM:\SOFTWARE\Microsoft\Office  

Server\16.0\Search\Diagnostics\Tracing' if(-not(Test-Path -Path  

$fastPerfEtlTraceFolderPath)) { $null = New-Item $fastPerfEtlTraceFolderPath  

-Type 'Directory' -Force }  

if (-not(Test-Path -Path $fastDiagnosticTracingRegKeyPath)) {  

$null = New-Item -Path $fastDiagnosticTracingRegKeyPath -Force }  

$null = New-ItemProperty -Path $fastDiagnosticTracingRegKeyPath -Name 'TracingPath' -PropertyType 'string' -Value $fastPerfEtlTraceFolderPath -Force $null = New-ItemProperty -Path  

$fastDiagnosticTracingRegKeyPath -Name 'TracingFileName' -PropertyType 'string'  

-Value 'DocumentProcessingTrace' -Force $null = New-ItemProperty -Path  

$fastDiagnosticTracingRegKeyPath -Name 'DocumentParserSuccessLogMessage'  

-PropertyType 'Dword' -Value 1 -Force $null = New-ItemProperty -Path  

$fastDiagnosticTracingRegKeyPath -Name 'DocumentParserLoggingNoInitialisation'  

-PropertyType 'Dword' -Value 1 -Force # Max trace folder size 50 * 100 =  

5GB $null = New-ItemProperty -Path $fastDiagnosticTracingRegKeyPath -Name  

'MaxTraceFileSize' -PropertyType 'Dword' -Value 50 -Force $null =  

New-ItemProperty -Path $fastDiagnosticTracingRegKeyPath -Name  

'MaxTraceFileCount' -PropertyType 'Dword' -Value 100 -Force  

$null = New-ItemProperty -Path $fastDiagnosticTracingRegKeyPath -Name  

'UseGeneralSwitch' -PropertyType 'Dword' -Value 1 -Force  

$null = New-ItemProperty -Path $fastDiagnosticTracingRegKeyPath -Name 'GeneralSwitch'  

-PropertyType 'Dword' -Value 0 -Force } catch { # ETl tracing is not  

critical. Info only log Write-ExchangeSetupLog -Info ("An exception ocurred  

while trying to Configure the FAST ETL traces. Exception: " +  

$_.Exception.Message); } try { $fastFusionRegKeyPath =  

'HKLM:\SOFTWARE\Microsoft\Office Server\16.0\Search\FlightControl' if  

(Test-Path -Path $fastFusionRegKeyPath) { Remove-ItemProperty -Path  

$fastFusionRegKeyPath -Name 'fusion_new_enabled' -Force -ErrorAction  

SilentlyContinue Remove-ItemProperty -Path $fastFusionRegKeyPath -Name  

'fusion_old_enabled' -Force -ErrorAction SilentlyContinue  

Remove-ItemProperty -Path $fastFusionRegKeyPath -Name 'fusion_compare_outputs' -Force -ErrorAction SilentlyContinue } } catch { # Removing new fusion keys is not critical.  

Info only log Write-ExchangeSetupLog -Info ("An exception ocurred while trying  

to remove the fast new fusion reg keys. Exception: " + $.Exception.Message);  

} $fastInstallConfigPath = Join-Path -Path $RoleBinPath -ChildPath  

"Search\Ceres\Installer"; $command = Join-Path -Path $fastInstallConfigPath  

-ChildPath "InstallConfig.ps1"; $dataFolderPath = Join-Path -Path $RoleBinPath  

-ChildPath "Search\Ceres\HostController\Data"; # Remove previous  

SearchFoundation configuration &$command -action u -silent; try { if  

([System.IO.Directory]::Exists($dataFolderPath)) {  

[System.IO.Directory]::Delete($dataFolderPath, $true); } } catch {  

$deleteErrorMsg = "Failure cleaning up SearchFoundation Data folder. - " +  

$dataFolderPath + " - " + $.Exception.Message;  

Write-ExchangeSetupLog -Error $deleteErrorMsg; }

Re-add the SearchFoundation configuration

Try { # the BasePort value MUST be kept in sync with  

dev\Search\src\OperatorSchema\SearchConfig.cs  

&$command -action i -baseport  

3800 -dataFolder $dataFolderPath -silent; } catch {  

$errorMsg = "Failure configuring SearchFoundation through installconfig.ps1 - " +  

$_.Exception.Message; Write-ExchangeSetupLog -Error $errorMsg;

Clean up the failed configuration attempt.

&$command -action u -silent; try { if ([System.IO.Directory]::Exists($dataFolderPath)) {  

[System.IO.Directory]::Delete($dataFolderPath, $true); } } catch {  

$deleteErrorMsg = "Failure cleaning up SearchFoundation Data folder. - " +  

$dataFolderPath + " - " + $_.Exception.Message;  

Write-ExchangeSetupLog -Error  

$deleteErrorMsg; } }

Set the PowerShell Snap-in's public key tokens try { $PowerShellSnapinsPath =

"HKLM:\SOFTWARE\Microsoft\PowerShell\1\PowerShellSnapIns\";  

$FastSnapinNames =  

@("EnginePSSnapin", "HostControllerPSSnapIn", "InteractionEnginePSSnapIn",  

"JunoPSSnapin", "SearchCorePSSnapIn");  

$officePublicKey = "71E9BCE111E9429C";  

$exchangePublicKey = "31bf3856ad364e35";  

foreach ($fastSnapinName in  

$FastSnapinNames) {  

$fastSnapinPath = $PowerShellSnapinsPath +  

$fastSnapinName; $assemblyNameProperty = Get-ItemProperty -Path  

$fastSnapinPath -Name "AssemblyName" -ErrorAction SilentlyContinue;  

If ($assemblyNameProperty -ne $null -and (-not  

[string]::IsNullOrEmpty($assemblyNameProperty.AssemblyName))) {  

$newAssemblyName = $assemblyNameProperty.AssemblyName -ireplace  

($officePublicKey, $exchangePublicKey);  

Set-ItemProperty -Path $fastSnapinPath  

-Name "AssemblyName" -Value $newAssemblyName; } } } catch { # Info only  

Log Write-ExchangeSetupLog -Info ("An exception ocurred while configuring  

Search Foundation PowerShell Snapin. Exception: " + $_.Exception.Message);  

} } " was run: "System.Exception: Failure cleaning up SearchFoundation Data  

folder. - C:\Program Files\Microsoft\Exchange  

Server\V15\Bin\Search\Ceres\HostController\Data - Exception calling "Delete"  

with "2" argument(s): "Access to the path  

'Microsoft.ClientResourceView.FlowService.dll' is denied."  

At Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception,  

ErrorCategory errorCategory, Object target, String helpUrl)  

atMicrosoft.Exchange.Management.Deployment.WriteExchangeSetupLog.InternalProcessR  

cord() at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String  

funcName, Action func, Boolean terminatePipelineIfFailed)".

The Exchange Server setup operation didn't complete. More details can be found  

in ExchangeSetup.log located in the <SystemDrive>:\ExchangeSetupLogs folder.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-07*

Hi @jennylee   ,    

Did you run setup /prepareAD before running the setup? Looks like issue with the arbitration mailbox.    

Run the command in Exchange management shell,    

Get-Mailbox –Arbitration | Select Name,Database    

there would be a warning for one of the system mailboxes, if yes, run the below command to set the database to that system mailbox    

Set-Mailbox "System Mailbox xxxxx" –Database "DB Name" –Arbitration    

If the above suggestion helps, please click on "Accept Answer" and upvote it.
