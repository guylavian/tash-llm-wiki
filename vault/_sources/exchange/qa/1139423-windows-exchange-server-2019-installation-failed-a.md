---
title: "Windows exchange server 2019 installation failed at last step"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1139423/windows-exchange-server-2019-installation-failed-a
question_id: 1139423
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Windows exchange server 2019 installation failed at last step

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1139423/windows-exchange-server-2019-installation-failed-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Community,     

I get below error when installing Exchange server 2019. Any tips or help would be great.     

Error:    

The following error was generated when "$error.Clear();     

          $dependentAssemblyGeneratorExePath = [System.IO.Path]::Combine($RoleInstallPath, "bin", "DependentAssemblyGenerator.exe");  

          $exchangeBinPath  = [System.IO.Path]::Combine($RoleInstallPath, "bin");  

          $clientAccessPath = [System.IO.Path]::Combine($RoleInstallPath, "ClientAccess");  

          $sharedWebConfig  = [System.IO.Path]::Combine($RoleInstallPath, "ClientAccess", "SharedWebConfig.config");  

```
$a = &"$dependentAssemblyGeneratorExePath" -exchangePath "$exchangeBinPath" -exchangePath "$clientAccessPath" -configFile "$sharedWebConfig";  
      $allOutput = @();  
      $a | % { $allOutput += $_ };  
      Write-ExchangeSetupLog -Info ($allOutput -join "`r`n");  
      Stop-SetupService -ServiceName WAS;  
      Start-SetupService -ServiceName W3SVC;  
    " was run: "System.Management.Automation.RemoteException".
```

Error:    

The following error was generated when "$error.Clear();     

          $dependentAssemblyGeneratorExePath = [System.IO.Path]::Combine($RoleInstallPath, "bin", "DependentAssemblyGenerator.exe");  

          $exchangeBinPath  = [System.IO.Path]::Combine($RoleInstallPath, "bin");  

          $clientAccessPath = [System.IO.Path]::Combine($RoleInstallPath, "ClientAccess");  

          $sharedWebConfig  = [System.IO.Path]::Combine($RoleInstallPath, "ClientAccess", "SharedWebConfig.config");  

```
$a = &"$dependentAssemblyGeneratorExePath" -exchangePath "$exchangeBinPath" -exchangePath "$clientAccessPath" -configFile "$sharedWebConfig";  
      $allOutput = @();  
      $a | % { $allOutput += $_ };  
      Write-ExchangeSetupLog -Info ($allOutput -join "`r`n");  
      Stop-SetupService -ServiceName WAS;  
      Start-SetupService -ServiceName W3SVC;  
    " was run: "System.Management.Automation.RemoteException: Process is terminated due to StackOverflowException.".
```

Regards,    

Muralidharan

## Answers

_No answers on this thread._
