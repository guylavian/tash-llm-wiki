---
title: "Uninstall Exchange 2013 after migration failing at step 8, language packs."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/192767/uninstall-exchange-2013-after-migration-failing-at
question_id: 192767
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Uninstall Exchange 2013 after migration failing at step 8, language packs.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/192767/uninstall-exchange-2013-after-migration-failing-at (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Moved to 2019, uninstalling 2013, GUI stopped at phase 8, am getting this when I try to remove manually.

Performing Microsoft Exchange Server Prerequisite Check

Configuring Prerequisites COMPLETED

Configuring Microsoft Exchange Server

```
Preparing Setup                                                                                   COMPLETED
Language Files                                                                                    FAILED
 The following error was generated when "$error.Clear();
                $regPath='HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall';

                $PackageGUIDRegEx = "{DEDFFB[0-9a-fA-F]{2}-42EC-4E26-[0-9a-fA-F]{4}-430E86DF378C}";

                $InstallPath = (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\ExchangeServer\v15\setup').MsiInstallPath
```

;

```
if(test-path ($regPath))
                {
                    Write-ExchangeSetupLog -info ("Removing " +  $RoleLanguagePackType + " Language Packs.");
                    Get-ChildItem ($regPath) | foreach{
                        if($_ -match "(?$PackageGUIDRegEx)") {
                            $langPackPackageCode = $matches['ProductCode'];
                            if($langPackPackageCode -ne $null -and $langPackPackageCode.Length -ne 0) {
                                Write-ExchangeSetupLog -info ("Removing package $langPackPackageCode");
                                $language = $langPackPackageCode.Substring(20,4);
                                $logFilePath = [IO.Path]::Combine($RoleLogFilePath,"Uninstall") + '.' + $language +
```

'.' + "Client" + "." + $RoleLogDateTime + ".msilog";  

uninstall-MsiPackage -ProductCode ($langPackPackageCode) -LogFile ($logFilePath);  

};  

};  

};  

Get-Childitem -Path $InstallPath -include ".Localized.js",".Localized.min.js" -recurse | forea  

ch ($) {remove-item $.fullname};  

Write-ExchangeSetupLog -info "Remove Language Packs completed.";  

};

```
" was run: "**System.UnauthorizedAccessException: Access is denied** ---> System.ComponentModel.Win32Exception: Acce
```

ss is denied  

--- End of inner exception stack trace ---  

at System.Management.Automation.Utils.NativeDirectoryExists(String path)  

at System.Management.Automation.SessionStateInternal.IsItemContainer(CmdletProvider providerInstance, String path, Cm  

dletProviderContext context)".

In the log file:

[12/10/2020 01:00:09.0727] [1] The following 1 error(s) occurred during task execution:  

[12/10/2020 01:00:09.0727] [1] 0. ErrorRecord: Access is denied  

[12/10/2020 01:00:09.0727] [1] 0. ErrorRecord: System.UnauthorizedAccessException: Access is denied ---> System.ComponentModel.Win32Exception: Access is denied  

--- End of inner exception stack trace ---  

at System.Management.Automation.Utils.NativeDirectoryExists(String path)  

at System.Management.Automation.SessionStateInternal.IsItemContainer(CmdletProvider providerInstance, String path, CmdletProviderContext context)  

[12/10/2020 01:00:09.0743] [1] [ERROR] The following error was generated when "$error.Clear();  

$regPath='HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall';  

$PackageGUIDRegEx = "{DEDFFB[0-9a-fA-F]{2}-42EC-4E26-[0-9a-fA-F]{4}-430E86DF378C}";  

$InstallPath = (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\ExchangeServer\v15\setup').MsiInstallPath;  

if(test-path ($regPath))  

{  

Write-ExchangeSetupLog -info ("Removing " + $RoleLanguagePackType + " Language Packs.");  

Get-ChildItem ($regPath) | foreach{  

if($_ -match "(?<ProductCode>$PackageGUIDRegEx)") {  

$langPackPackageCode = $matches['ProductCode'];  

if($langPackPackageCode -ne $null -and $langPackPackageCode.Length -ne 0) {  

Write-ExchangeSetupLog -info ("Removing package $langPackPackageCode");  

$language = $langPackPackageCode.Substring(20,4);  

$logFilePath = [IO.Path]::Combine($RoleLogFilePath,"Uninstall") + '.' + $language + '.' + "Client" + "." + $RoleLogDateTime + ".msilog";  

uninstall-MsiPackage -ProductCode ($langPackPackageCode) -LogFile ($logFilePath);  

};  

};  

};  

Get-Childitem -Path $InstallPath -include ".Localized.js",".Localized.min.js" -recurse | foreach ($) {remove-item $.fullname};  

Write-ExchangeSetupLog -info "Remove Language Packs completed.";  

};

```
" was run: "System.UnauthorizedAccessException: Access is denied ---> System.ComponentModel.Win32Exception: Access is denied
```

--- End of inner exception stack trace ---  

at System.Management.Automation.Utils.NativeDirectoryExists(String path)  

at System.Management.Automation.SessionStateInternal.IsItemContainer(CmdletProvider providerInstance, String path, CmdletProviderContext context)".  

[12/10/2020 01:00:09.0743] [1] [ERROR] Access is denied  

[12/10/2020 01:00:09.0743] [1] [ERROR] Access is denied  

[12/10/2020 01:00:09.0743] [1] [ERROR-REFERENCE] Id=LanguagePackUninstallationComponent___9a89e7313d524f298d51c24709f69125 Component=EXCHANGE14:\Current\Release\Shared\Datacenter\Setup  

[12/10/2020 01:00:09.0743] [1] Setup is stopping now because of one or more critical errors.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2021-05-29*

The same approach works with Exchange Server 2016 as well. In our particular case, we restarted the server, ran setup.exe /mode:uninstall again, and it worked like a charm.
