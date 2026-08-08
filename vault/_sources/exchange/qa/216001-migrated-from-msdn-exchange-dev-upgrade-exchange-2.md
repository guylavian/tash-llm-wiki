---
title: "[Migrated from MSDN Exchange Dev]Upgrade Exchange 2013 to CU23"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/216001/migrated-from-msdn-exchange-dev-upgrade-exchange-2
question_id: 216001
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]Upgrade Exchange 2013 to CU23

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/216001/migrated-from-msdn-exchange-dev-upgrade-exchange-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.

Dear All,

I have exchange server 2013 U12 and I need to upgrade it to 2013 U23,

I have successfully upgrade the MBX, when I try to upgrade the CAS server its failed with the following error:

Error:  

The following error was generated when "$error.Clear();  

$dependentAssemblyGeneratorExePath = [System.IO.Path]::Combine($RoleInstallPath, "bin", "DependentAssemblyGenerator.exe");  

$exchangeBinPath = [System.IO.Path]::Combine($RoleInstallPath, "bin");  

$frontEndPath = [System.IO.Path]::Combine($RoleInstallPath, "FrontEnd");  

$clientAccessPath = [System.IO.Path]::Combine($RoleInstallPath, "ClientAccess");  

$sharedWebConfig = [System.IO.Path]::Combine($RoleInstallPath, "FrontEnd", "HttpProxy", "SharedWebConfig.config");

```
$a = &"$dependentAssemblyGeneratorExePath" -exchangePath "$exchangeBinPath" -exchangePath "$frontEndPath" -exchangePath "$clientAccessPath" -configFile "$sharedWebConfig";
      $a | % { if ($_.Length > 0) { Write-ExchangeSetupLog -Info "$_.ToString()" } }
      Start-SetupProcess -Name "iisreset" -Args "/timeout:120"
    " was run: "System.Management.Automation.RemoteException".
```

Error:  

The following error was generated when "$error.Clear();  

$dependentAssemblyGeneratorExePath = [System.IO.Path]::Combine($RoleInstallPath, "bin", "DependentAssemblyGenerator.exe");  

$exchangeBinPath = [System.IO.Path]::Combine($RoleInstallPath, "bin");  

$frontEndPath = [System.IO.Path]::Combine($RoleInstallPath, "FrontEnd");  

$clientAccessPath = [System.IO.Path]::Combine($RoleInstallPath, "ClientAccess");  

$sharedWebConfig = [System.IO.Path]::Combine($RoleInstallPath, "FrontEnd", "HttpProxy", "SharedWebConfig.config");

```
$a = &"$dependentAssemblyGeneratorExePath" -exchangePath "$exchangeBinPath" -exchangePath "$frontEndPath" -exchangePath "$clientAccessPath" -configFile "$sharedWebConfig";
      $a | % { if ($_.Length > 0) { Write-ExchangeSetupLog -Info "$_.ToString()" } }
      Start-SetupProcess -Name "iisreset" -Args "/timeout:120"
    " was run: "System.Management.Automation.RemoteException: Unhandled Exception:".
```

Error:  

The following error was generated when "$error.Clear();  

$dependentAssemblyGeneratorExePath = [System.IO.Path]::Combine($RoleInstallPath, "bin", "DependentAssemblyGenerator.exe");  

$exchangeBinPath = [System.IO.Path]::Combine($RoleInstallPath, "bin");  

$frontEndPath = [System.IO.Path]::Combine($RoleInstallPath, "FrontEnd");  

$clientAccessPath = [System.IO.Path]::Combine($RoleInstallPath, "ClientAccess");  

$sharedWebConfig = [System.IO.Path]::Combine($RoleInstallPath, "FrontEnd", "HttpProxy", "SharedWebConfig.config");

```
$a = &"$dependentAssemblyGeneratorExePath" -exchangePath "$exchangeBinPath" -exchangePath "$frontEndPath" -exchangePath "$clientAccessPath" -configFile "$sharedWebConfig";
      $a | % { if ($_.Length > 0) { Write-ExchangeSetupLog -Info "$_.ToString()" } }
      Start-SetupProcess -Name "iisreset" -Args "/timeout:120"
    " was run: "System.Management.Automation.RemoteException:  ".
```

Error:  

The following error was generated when "$error.Clear();  

$dependentAssemblyGeneratorExePath = [System.IO.Path]::Combine($RoleInstallPath, "bin", "DependentAssemblyGenerator.exe");  

$exchangeBinPath = [System.IO.Path]::Combine($RoleInstallPath, "bin");  

$frontEndPath = [System.IO.Path]::Combine($RoleInstallPath, "FrontEnd");  

$clientAccessPath = [System.IO.Path]::Combine($RoleInstallPath, "ClientAccess");  

$sharedWebConfig = [System.IO.Path]::Combine($RoleInstallPath, "FrontEnd", "HttpProxy", "SharedWebConfig.config");

```
$a = &"$dependentAssemblyGeneratorExePath" -exchangePath "$exchangeBinPath" -exchangePath "$frontEndPath" -exchangePath "$clientAccessPath" -configFile "$sharedWebConfig";
      $a | % { if ($_.Length > 0) { Write-ExchangeSetupLog -Info "$_.ToString()" } }
      Start-SetupProcess -Name "iisreset" -Args "/timeout:120"
    " was run: "System.Management.Automation.RemoteException: System.Globalization.CultureNotFoundException: Culture is not supported.
```

Parameter name: name  

UA is an invalid culture identifier.  

at System.Globalization.CultureInfo..ctor(String name, Boolean useUserOverride)  

at System.Reflection.RuntimeAssembly.GetLocale()  

at System.Reflection.RuntimeAssembly.GetName(Boolean copiedName)  

at Microsoft.Exchange.Management.DependentAssemblyGenerator.GetExchangeAssemblies(String exchangeInstallPath, IList`1 assembliesToAddToWebConfig)  

at Microsoft.Exchange.Management.DependentAssemblyGenerator.Main(String[] args)".

Error:  

The following error was generated when "$error.Clear();  

$dependentAssemblyGeneratorExePath = [System.IO.Path]::Combine($RoleInstallPath, "bin", "DependentAssemblyGenerator.exe");  

$exchangeBinPath = [System.IO.Path]::Combine($RoleInstallPath, "bin");  

$frontEndPath = [System.IO.Path]::Combine($RoleInstallPath, "FrontEnd");  

$clientAccessPath = [System.IO.Path]::Combine($RoleInstallPath, "ClientAccess");  

$sharedWebConfig = [System.IO.Path]::Combine($RoleInstallPath, "FrontEnd", "HttpProxy", "SharedWebConfig.config");

```
$a = &"$dependentAssemblyGeneratorExePath" -exchangePath "$exchangeBinPath" -exchangePath "$frontEndPath" -exchangePath "$clientAccessPath" -configFile "$sharedWebConfig";
      $a | % { if ($_.Length > 0) { Write-ExchangeSetupLog -Info "$_.ToString()" } }
      Start-SetupProcess -Name "iisreset" -Args "/timeout:120"
    " was run: "System.Management.Automation.RemoteException:
```

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-01*

Hi,  

Please check if the "SharedWebConfig.config" exists.  

The default path:  

1)%ExchangeInstallPath%\V15\ClientAccess.  

2)%ExchangeInstallPath%\V15\FrontEnd\HttpProxy

If the “SharedWebConfig.config” file is missing:  

1.You can copy this file ( SharedWebConfig.config ) from another CAS server and re-run upgrading process to check again. The default path: %ExchangeInstallPath%\V15\ClientAccess.  

2.If only one CAS server, you can refer to the following steps to generate the file and re-run again:  

Run cd %ExchangeInstallPath%\bin to change the current directory to the bin folder that's under the Exchange installation path.  

Use the DependentAssemblyGenerator.exe tool to generate the file  

1)If the file is missing from C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess, run the following command:

```
DependentAssemblyGenerator.exe -exchangePath "%ExchangeInstallPath%\bin" -exchangePath "%ExchangeInstallPath%\ClientAccess" -configFile "%ExchangeInstallPath%\ClientAccess\SharedWebConfig.config"
```

2)If the file is missing from C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy, run the following command:

```
DependentAssemblyGenerator.exe -exchangePath "%ExchangeInstallPath%\bin" -exchangePath "%ExchangeInstallPath%\FrontEnd\HttpProxy" -configFile "%ExchangeInstallPath%\FrontEnd\HttpProxy\SharedWebConfig.config"
```

3)Run IISRESET, or restart the server.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
