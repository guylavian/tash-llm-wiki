---
title: "Azure AD connect error on Microsoft key distribution service failed to start."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/684879/azure-ad-connect-error-on-microsoft-key-distributi
question_id: 684879
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Azure AD connect error on Microsoft key distribution service failed to start.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/684879/azure-ad-connect-error-on-microsoft-key-distributi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,  

I am trying to configure single sign-on using the ADConnect. However, I keep on receiving the error "Unable to install the Synchronisation Service. Microsoft Key Distribution Service failed to start. Please see the Application and System event logs for additional details."  

I have checked the log file and this is what I am seeing inside my log file inside C:\ProgramData\AADConnect. Any help would be much appreciated.  

[15:57:29.988] [  1] [INFO ] Setting default logger for MSAL provider..  

[15:57:30.004] [  1] [INFO ] Default logger set successfully.  

[15:57:30.129] [  1] [INFO ]   

[15:57:30.129] [  1] [INFO ] ================================================================================  

[15:57:30.129] [  1] [INFO ] Application starting  

[15:57:30.129] [  1] [INFO ] ================================================================================  

[15:57:30.129] [  1] [INFO ] Start Time (Local): Wed, 05 Jan 2022 15:57:30 GMT  

[15:57:30.129] [  1] [INFO ] Start Time (UTC): Wed, 05 Jan 2022 23:57:30 GMT  

[15:57:30.129] [  1] [INFO ] Application Version: 2.0.89.0  

[15:57:30.129] [  1] [INFO ] Application Build Date: 1968-04-12 01:59:50Z  

[15:57:32.129] [  1] [INFO ] Telemetry session identifier: {4683ae86-6a7c-43df-8615-ddbe246c5122}  

[15:57:32.129] [  1] [INFO ] Telemetry device identifier: kgLIlca/i5Floy+qFHZwhvRlMPv2U2nxqn7h9JcNRh4=  

[15:57:32.129] [  1] [INFO ] Application Build Identifier: AD-IAM-HybridSync master (7c62acb9afcb810e9b9d233239f773e25116b859)  

[15:57:32.519] [  1] [INFO ] machine.config path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\machine.config.  

[15:57:32.519] [  1] [INFO ] Default Proxy [ProxyAddress]: <Unspecified>  

[15:57:32.519] [  1] [INFO ] Default Proxy [UseSystemDefault]: Unspecified  

[15:57:32.519] [  1] [INFO ] Default Proxy [BypassOnLocal]: Unspecified  

[15:57:32.519] [  1] [INFO ] Default Proxy [Enabled]: True  

[15:57:32.519] [  1] [INFO ] Default Proxy [AutoDetect]: Unspecified  

[15:57:32.519] [  1] [INFO ] Default Proxy [UseDefaultCredentials]: False  

[15:57:32.597] [  1] [VERB ] Scheduler wizard mutex wait timeout: 00:00:05  

[15:57:32.597] [  1] [INFO ] AADConnect changes ALLOWED: Successfully acquired the configuration change mutex.  

[15:57:32.707] [  1] [INFO ] RootPageViewModel.GetInitialPages: Beginning detection for creating initial pages.  

[15:57:32.754] [  1] [INFO ] Loading the persisted settings .  

[15:57:32.800] [  1] [INFO ] Checking if machine version is 6.1.7601 or higher  

[15:57:32.972] [  1] [INFO ] The current operating system version is 10.0.17763, the requirement is 6.1.7601.  

[15:57:32.972] [  1] [INFO ] Password Hash Sync supported: 'True'  

[15:57:33.003] [  1] [INFO ] DetectInstalledComponents stage: The installed OS SKU is 80  

[15:57:33.003] [  1] [INFO ] Detected .NET release 461814  

[15:57:33.003] [  1] [INFO ] TLS 1.2 is properly configured.  

[15:57:33.019] [  1] [INFO ] DetectInstalledComponents stage: Checking install context.  

[15:57:33.035] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Visual C++ 2019 Redistributable Package  

[15:57:33.035] [  1] [VERB ] Getting list of installed packages by upgrade code  

[15:57:33.050] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {36f68a90-239c-34df-b58c-64b30153ce35}: verified product code {e642504a-44a4-4cea-ab54-76d0f34f33ba}.  

[15:57:33.050] [  1] [VERB ] Package=Microsoft Visual C++ 2019 X64 Minimum Runtime - 14.29.30036, Version=14.29.30036, ProductCode=e642504a-44a4-4cea-ab54-76d0f34f33ba, UpgradeCode=36f68a90-239c-34df-b58c-64b30153ce35  

[15:57:33.050] [  1] [INFO ] Determining installation action for Microsoft Visual C++ 2019 Redistributable Package (36f68a90-239c-34df-b58c-64b30153ce35)  

[15:57:33.050] [  1] [INFO ] Product Microsoft Visual C++ 2019 Redistributable Package (version 14.29.30036) is installed.  

[15:57:33.050] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Directory Sync Tool  

[15:57:33.066] [  1] [VERB ] Getting list of installed packages by upgrade code  

[15:57:33.066] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {bef7e7d9-2ac2-44b9-abfc-3335222b92a7}: no registered products found.  

[15:57:33.066] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {dc9e604e-37b0-4efc-b429-21721cf49d0d}: no registered products found.  

[15:57:33.066] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {545334d7-13cd-4bab-8da1-2775fa8cf7c2}: no registered products found.  

[15:57:33.066] [  1] [INFO ] Determining installation action for Microsoft Directory Sync Tool UpgradeCodes {bef7e7d9-2ac2-44b9-abfc-3335222b92a7}, {dc9e604e-37b0-4efc-b429-21721cf49d0d}  

[15:57:33.066] [  1] [INFO ] DirectorySyncComponent: Product Microsoft Directory Sync Tool is not installed.  

[15:57:33.066] [  1] [INFO ] Performing direct lookup of upgrade codes for: Azure AD Sync Engine  

[15:57:33.066] [  1] [VERB ] Getting list of installed packages by upgrade code  

[15:57:33.066] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {545334d7-13cd-4bab-8da1-2775fa8cf7c2}: no registered products found.  

[15:57:33.066] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {dc9e604e-37b0-4efc-b429-21721cf49d0d}: no registered products found.  

[15:57:33.066] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {bef7e7d9-2ac2-44b9-abfc-3335222b92a7}: no registered products found.  

[15:57:33.082] [  1] [INFO ] Determining installation action for Azure AD Sync Engine (545334d7-13cd-4bab-8da1-2775fa8cf7c2)  

[15:57:33.894] [  1] [INFO ] Product Azure AD Sync Engine is not installed.  

[15:57:33.894] [  1] [INFO ] Performing direct lookup of upgrade codes for: Azure AD Connect Synchronization Agent  

[15:57:33.894] [  1] [VERB ] Getting list of installed packages by upgrade code  

[15:57:33.894] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {3cd653e3-5195-4ff2-9d6c-db3dacc82c25}: no registered products found.  

[15:57:33.894] [  1] [INFO ] Determining installation action for Azure AD Connect Synchronization Agent (3cd653e3-5195-4ff2-9d6c-db3dacc82c25)  

[15:57:33.894] [  1] [INFO ] Product Azure AD Connect Synchronization Agent is not installed.  

[15:57:33.894] [  1] [INFO ] Performing direct lookup of upgrade codes for: Azure AD Connect Health agent for sync  

[15:57:33.894] [  1] [VERB ] Getting list of installed packages by upgrade code  

[15:57:33.894] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {114fb294-8aa6-43db-9e5c-4ede5e32886f}: no registered products found.  

[15:57:33.894] [  1] [INFO ] Determining installation action for Azure AD Connect Health agent for sync (114fb294-8aa6-43db-9e5c-4ede5e32886f)  

[15:57:33.894] [  1] [INFO ] Product Azure AD Connect Health agent for sync is not installed.  

[15:57:33.894] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Azure AD Connect Authentication Agent  

[15:57:33.894] [  1] [VERB ] Getting list of installed packages by upgrade code  

[15:57:33.894] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {0c06f9df-c56b-42c4-a41b-f5f64d01a35c}: no registered products found.  

[15:57:33.894] [  1] [INFO ] Determining installation action for Microsoft Azure AD Connect Authentication Agent (0c06f9df-c56b-42c4-a41b-f5f64d01a35c)  

[15:57:33.894] [  1] [INFO ] Product Microsoft Azure AD Connect Authentication Agent is not installed.  

[15:57:33.894] [  1] [INFO ] Performing direct lookup of upgrade codes for: Azure AD Connect Administration Agent  

[15:57:33.894] [  1] [VERB ] Getting list of installed packages by upgrade code  

[15:57:33.894] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {886051ec-1165-4df8-a492-19d1e0ff57ee}: no registered products found.  

[15:57:33.894] [  1] [INFO ] Determining installation action for Azure AD Connect Administration Agent (886051ec-1165-4df8-a492-19d1e0ff57ee)  

[15:57:33.894] [  1] [INFO ] Product Azure AD Connect Administration Agent is not installed.  

[15:57:33.894] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Command Line Utilities 15 for SQL Server  

[15:57:33.894] [  1] [VERB ] Getting list of installed packages by upgrade code  

[15:57:33.894] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {11e5cc67-2eca-41a1-8775-5ea0b51ccbaa}: verified product code {eda3fabe-e481-4e69-a7b0-e845df0fec22}.  

[15:57:33.910] [  1] [VERB ] Package=Microsoft Command Line Utilities 15 for SQL Server, Version=15.0.2000.5, ProductCode=eda3fabe-e481-4e69-a7b0-e845df0fec22, UpgradeCode=11e5cc67-2eca-41a1-8775-5ea0b51ccbaa  

[15:57:33.910] [  1] [INFO ] Determining installation action for Microsoft Command Line Utilities 15 for SQL Server (11e5cc67-2eca-41a1-8775-5ea0b51ccbaa)  

[15:57:33.910] [  1] [INFO ] Product Microsoft Command Line Utilities 15 for SQL Server (version 15.0.2000.5) is installed.  

[15:57:33.910] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft ODBC Driver 17 for SQL Server  

[15:57:33.910] [  1] [VERB ] Getting list of installed packages by upgrade code  

[15:57:33.910] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {0123a210-9b73-46e7-b5ce-7f33630300e7}: verified product code {853997da-6fcb-4fb9-918e-e0ff881faf65}.  

[15:57:33.910] [  1] [VERB ] Package=Microsoft ODBC Driver 17 for SQL Server, Version=17.7.2.1, ProductCode=853997da-6fcb-4fb9-918e-e0ff881faf65, UpgradeCode=0123a210-9b73-46e7-b5ce-7f33630300e7  

[15:57:33.910] [  1] [INFO ] Determining installation action for Microsoft ODBC Driver 17 for SQL Server (0123a210-9b73-46e7-b5ce-7f33630300e7)  

[15:57:33.910] [  1] [INFO ] Product Microsoft ODBC Driver 17 for SQL Server (version 17.7.2.1) is installed.  

[15:57:33.910] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft SQL Server 2019 LocalDB  

[15:57:33.910] [  1] [VERB ] Getting list of installed packages by upgrade code  

[15:57:33.910] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {f0176a51-908a-4240-8853-e229d0ae3f39}: verified product code {ee44ed1f-d6f5-4d2c-8d9b-3da6a00102bf}.  

[15:57:33.910] [  1] [VERB ] Package=Microsoft SQL Server 2019 LocalDB , Version=15.0.4138.2, ProductCode=ee44ed1f-d6f5-4d2c-8d9b-3da6a00102bf, UpgradeCode=f0176a51-908a-4240-8853-e229d0ae3f39  

[15:57:33.910] [  1] [INFO ] Determining installation action for Microsoft SQL Server 2019 LocalDB (f0176a51-908a-4240-8853-e229d0ae3f39)  

[15:57:33.910] [  1] [INFO ] Product Microsoft SQL Server 2019 LocalDB (version 15.0.4138.2) is installed.  

[15:57:33.910] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft OLE DB Driver for SQL Server  

[15:57:33.910] [  1] [VERB ] Getting list of installed packages by upgrade code  

[15:57:33.910] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {debb0805-202c-471d-a182-675ff32f65c2}: verified product code {9d6f8754-28e9-4940-b319-3fc8588cf18f}.  

[15:57:33.910] [  1] [VERB ] Package=Microsoft OLE DB Driver for SQL Server, Version=18.5.0.0, ProductCode=9d6f8754-28e9-4940-b319-3fc8588cf18f, UpgradeCode=debb0805-202c-471d-a182-675ff32f65c2  

[15:57:33.910] [  1] [INFO ] Determining installation action for Microsoft OLE DB Driver for SQL Server (debb0805-202c-471d-a182-675ff32f65c2)  

[15:57:33.910] [  1] [INFO ] Product Microsoft OLE DB Driver for SQL Server (version 18.5.0.0) is installed.  

[15:57:33.910] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Azure AD Connect Authentication Agent  

[15:57:33.910] [  1] [VERB ] Getting list of installed packages by upgrade code  

[15:57:33.910] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {fb3feca7-5190-43e7-8d4b-5eec88ed9455}: no registered products found.  

[15:57:33.910] [  1] [INFO ] Determining installation action for Microsoft Azure AD Connect Authentication Agent (fb3feca7-5190-43e7-8d4b-5eec88ed9455)  

[15:57:33.910] [  1] [INFO ] Product Microsoft Azure AD Connect Authentication Agent is not installed.  

[15:57:33.910] [  1] [INFO ] Determining installation action for Microsoft Azure AD Connection Tool.  

[15:57:34.019] [  1] [WARN ] Failed to read DisplayName registry key: An error occurred while executing the 'Get-ItemProperty' command. Cannot find path 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\MicrosoftAzureADConnectionTool' because it does not exist.  

[15:57:34.019] [  1] [INFO ] Product Microsoft Azure AD Connection Tool is not installed.  

[15:57:34.019] [  1] [INFO ] Performing direct lookup of upgrade codes for: Azure Active Directory Connect  

[15:57:34.019] [  1] [VERB ] Getting list of installed packages by upgrade code  

[15:57:34.019] [  1] [INFO ] GetProductInfoProperty({b6af168b-9c68-47ed-b75d-3335c5152d2a}, VersionString): unknown product  

[15:57:34.019] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {d61eb959-f2d1-4170-be64-4dc367f451ea}: stale product code {b6af168b-9c68-47ed-b75d-3335c5152d2a}.  

[15:57:34.019] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {d61eb959-f2d1-4170-be64-4dc367f451ea}: verified product code {53b43126-d7ec-4957-b367-b6a43196ee74}.  

[15:57:34.019] [  1] [VERB ] Package=Microsoft Azure AD Connect, Version=2.0.89.0, ProductCode=53b43126-d7ec-4957-b367-b6a43196ee74, UpgradeCode=d61eb959-f2d1-4170-be64-4dc367f451ea  

[15:57:34.019] [  1] [WARN ] CheckInstallationState: Stale product code: {b6af168b-9c68-47ed-b75d-3335c5152d2a} found for Azure Active Directory Connect. The installation of this component could fail.  

[15:57:34.019] [  1] [WARN ] CheckInstallationState: By uninstalling AADConnect Wizard, an attempt to remove the stale product codes will be performed  

[15:57:34.019] [  1] [INFO ] Determining installation action for Azure Active Directory Connect (d61eb959-f2d1-4170-be64-4dc367f451ea)  

[15:57:34.019] [  1] [INFO ] Product Azure Active Directory Connect (version 2.0.89.0) is installed.  

[15:57:34.019] [  1] [INFO ] DetectInstalledComponents stage: Verifying required DCOM registry keys are present.  

[15:57:34.035] [  1] [INFO ] DetectInstalledComponents::CheckBinaryRegistryValueContainsData : Registry value 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\MachineAccessRestriction' is present.  

[15:57:34.035] [  1] [INFO ] DetectInstalledComponents::CheckBinaryRegistryValueContainsData : Registry value 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\MachineLaunchRestriction' is present.  

[15:57:34.035] [  1] [INFO ] DetectInstalledComponents::CheckBinaryRegistryValueContainsData : Registry value 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\DefaultLaunchPermission' is present.  

[15:57:35.566] [  1] [INFO ] ServiceControllerProvider: GetServiceStartMode(seclogon) is 'Manual'.  

[15:57:35.566] [  1] [INFO ] ServiceControllerProvider: verifying EventLog is in state (Running)  

[15:57:35.566] [  1] [INFO ] ServiceControllerProvider: current service status: Running  

[15:57:35.566] [  1] [INFO ] DetectInstalledComponents stage: PowerShell version verified.  

[15:57:35.566] [  1] [INFO ] Checking for DirSync conditions.  

[15:57:35.566] [  1] [INFO ] DirSync not detected. Checking for AADSync/AADConnect upgrade conditions.  

[15:57:35.582] [  1] [INFO ] Initial configuration is incomplete.  

[15:57:35.582] [  1] [INFO ] Resume Wizard from previous Azure service connectivity failure.  

[15:57:35.847] [  1] [INFO ] SyncDataProvider:LoadSettings - loading context with global settings.  

[15:57:35.925] [  1] [INFO ] SyncDataProvider:LoadSettings - retrieving global settings from the sync engine.  

[15:57:36.269] [  1] [ERROR] Configuration policy could not be retrieved (GetGlobalConfigurationParameters).  Details: System.Management.Automation.CommandNotFoundException: The term 'Get-ADSyncGlobalSettingsParameter' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.  

   at System.Management.Automation.Runspaces.PipelineBase.Invoke(IEnumerable input)  

   at System.Management.Automation.PowerShell.Worker.ConstructPipelineAndDoWork(Runspace rs, Boolean performSyncInvoke)  

   at System.Management.Automation.PowerShell.Worker.CreateRunspaceIfNeededAndDoWork(Runspace rsToUse, Boolean isSync)  

   at System.Management.Automation.PowerShell.CoreInvokeHelperTInput,TOutput  

   at System.Management.Automation.PowerShell.CoreInvokeTInput,TOutput  

   at System.Management.Automation.PowerShell.Invoke(IEnumerable input, PSInvocationSettings settings)  

   at Microsoft.Online.Deployment.PowerShell.LocalPowerShell.Invoke()  

   at Microsoft.Online.Deployment.PowerShell.PowerShellAdapter.TypeDependencies.InvokePowerShell(IPowerShell powerShell)  

   at Microsoft.Online.Deployment.PowerShell.PowerShellAdapter.InvokePowerShellCommand(String commandName, InitialSessionState initialSessionState, IDictionary`2 commandParameters, Boolean isScript)  

   at Microsoft.Azure.ActiveDirectory.Synchronization.PowerShellConfigAdapter.GlobalSettingsConfigAdapter.GetGlobalConfigurationParameters()  

   at Microsoft.Online.Deployment.Types.Providers.SyncDataProvider.GetGlobalParametersFromSyncEngine()  

   at Microsoft.Online.Deployment.Types.Providers.SyncDataProvider.LoadSettings(IAadSyncContext aadSyncContext, GetGlobalParametersDelegate getGlobalParameters, GetConnectorsDelegate getConnectors, Boolean migratingSettings)  

[15:57:36.378] [  1] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Start background task Microsoft.Online.Deployment.OneADWizard.UI.WizardPages.ExpressSettingsPageViewModel.GatherEnvironmentData in Page:"Express Settings"  

[15:57:36.378] [  1] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Started Background Task Id:9  

[15:57:36.394] [ 17] [INFO ] Checking if machine version is 6.1.7601 or higher  

[15:57:36.394] [ 17] [INFO ] The current operating system version is 10.0.17763, the requirement is 6.1.7601.  

[15:57:36.394] [ 17] [INFO ] Password Hash Sync supported: 'True'  

[15:57:36.425] [  1] [INFO ] Express Settings install is supported: domain-joined + OS version allowed.  

[15:57:41.979] [  1] [INFO ] Express Settings:  Updating page flow for EXPRESS mode install.  

[15:57:41.980] [  1] [INFO ] Called SetWizardMode(ExpressInstall, True)  

[15:57:41.984] [  1] [WARN ] MicrosoftOnlinePersistedStateProvider.Save: zero state elements provided, saving an empty persisted state file  

[15:57:41.987] [  1] [INFO ] MicrosoftOnlinePersistedStateProvider.UpdateFileProtection: updating file protection from the persisted state file: C:\ProgramData\AADConnect\PersistedState.xml, isAddProtection: False  

[15:57:41.993] [  1] [INFO ] MicrosoftOnlinePersistedStateProvider.UpdateFileProtection: updating file protection from the persisted state file: C:\ProgramData\AADConnect\PersistedState.xml, isAddProtection: True  

[15:57:42.125] [  1] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Start background task Microsoft.Online.Deployment.OneADWizard.UI.WizardPages.ExpressSettingsPageViewModel.StartPrerequisiteInstallation in Page:"Express Settings"  

[15:57:42.127] [  1] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Started Background Task Id:685  

[15:57:42.183] [ 18] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Start background task Microsoft.Online.Deployment.OneADWizard.UI.WizardPages.InstallSyncEnginePageViewModel.StartNewInstallation in Page:"Install required components"  

[15:57:42.183] [ 18] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Started Background Task Id:708  

[15:57:42.230] [ 18] [INFO ] SyncEngineSetupViewModel: Validating sync engine settings.  

[15:57:42.245] [ 18] [INFO ] Enter ValidateSqlVersion.  

[15:57:42.245] [ 18] [INFO ] Exit ValidateSqlVersion (localdb).  

[15:57:42.245] [ 18] [INFO ] Enter ValidateSqlAoaAsyncInstance.  

[15:57:42.245] [ 18] [INFO ] Exit ValidateSqlAoaAsyncInstance (localdb).  

[15:57:42.245] [ 18] [INFO ] The ADSync database does not exist and will be created.  serverAdmin=True.  

[15:57:42.245] [ 18] [INFO ] Attaching to the ADSync database: SQLServerName= SQLInstanceName= ServiceAccountName=, state=DoesNotExist, Collation=, /UseExistingDatabase=False.  

[15:57:42.261] [ 18] [INFO ] Starting Sync Engine installation  

[15:57:42.261] [ 18] [INFO ] Starting Prerequisite installation  

[15:57:42.261] [ 18] [VERB ] WorkflowEngine created  

[15:57:42.261] [ 18] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Visual C++ 2013 Redistributable Package  

[15:57:42.261] [ 18] [VERB ] Getting list of installed packages by upgrade code  

[15:57:42.261] [ 18] [INFO ] GetInstalledPackagesByUpgradeCode {20400cf0-de7c-327e-9ae4-f0f38d9085f8}: verified product code {cb0836ec-b072-368d-82b2-d3470bf95707}.  

[15:57:42.261] [ 18] [VERB ] Package=Microsoft Visual C++ 2013 x64 Minimum Runtime - 12.0.40660, Version=12.0.40660, ProductCode=cb0836ec-b072-368d-82b2-d3470bf95707, UpgradeCode=20400cf0-de7c-327e-9ae4-f0f38d9085f8  

[15:57:42.261] [ 18] [INFO ] Determining installation action for Microsoft Visual C++ 2013 Redistributable Package (20400cf0-de7c-327e-9ae4-f0f38d9085f8)  

[15:57:42.261] [ 18] [INFO ] Product Microsoft Visual C++ 2013 Redistributable Package (version 12.0.40660) is installed.  

[15:57:42.261] [ 18] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Visual C++ 2019 Redistributable Package  

[15:57:42.261] [ 18] [VERB ] Getting list of installed packages by upgrade code  

[15:57:42.261] [ 18] [INFO ] GetInstalledPackagesByUpgradeCode {36f68a90-239c-34df-b58c-64b30153ce35}: verified product code {e642504a-44a4-4cea-ab54-76d0f34f33ba}.  

[15:57:42.261] [ 18] [VERB ] Package=Microsoft Visual C++ 2019 X64 Minimum Runtime - 14.29.30036, Version=14.29.30036, ProductCode=e642504a-44a4-4cea-ab54-76d0f34f33ba, UpgradeCode=36f68a90-239c-34df-b58c-64b30153ce35  

[15:57:42.261] [ 18] [INFO ] Determining installation action for Microsoft Visual C++ 2019 Redistributable Package (36f68a90-239c-34df-b58c-64b30153ce35)  

[15:57:42.261] [ 18] [INFO ] Product Microsoft Visual C++ 2019 Redistributable Package (version 14.29.30036) is installed.  

[15:57:42.276] [  1] [INFO ] Page transition from "Express Settings" [ExpressSettingsPageViewModel] to "Connect to Azure AD" [AzureTenantPageViewModel]  

[15:57:42.308] [  1] [INFO ] Property Password failed validation with error A valid domain must be selected.  

[15:57:47.936] [ 17] [INFO ] AzureTenantPage: Beginning Windows Azure tenant credential validation for user - @thechowk.com.au  

[15:57:48.000] [ 17] [INFO ] AzureConfigurationFromPrincipalName: Successfully resolved UPN (@thechowk.com.au) to the Worldwide Azure instance.   

Resolution Method [Registry Configuration]: Worldwide.  

[15:57:48.015] [ 17] [INFO ] ResolveAzureInstance [Worldwide]: authority=HTTPS://LOGIN.MICROSOFTONLINE.COM/THECHOWK.COM.AU,   

Resolution Method [Registry Configuration]: Worldwide.  

[15:57:48.140] [ 17] [INFO ] Authenticate-MSAL [Acquiring token]: STS endpoint (HTTPS://LOGIN.MICROSOFTONLINE.COM/THECHOWK.COM.AU), scope (https://graph.windows.net/user_impersonation), userName (******@thechowk.com.au).  

[15:57:48.140] [ 17] [INFO ] MSAL.ClearTokenCache [Clearing Token Cache]  

[15:57:48.281] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:48 - 78fb10cf-be46-48c3-bb23-c54a25ac04b5] (UnknownClient: 0.0.0.0) MSAL MSAL.Desktop with assembly version '4.5.1.0'. CorrelationId(78fb10cf-be46-48c3-bb23-c54a25ac04b5)  

[15:57:48.297] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:48 - 78fb10cf-be46-48c3-bb23-c54a25ac04b5] (UnknownClient: 0.0.0.0)   

=== Request Data ===  

Authority Provided? - True  

Scopes - https://graph.windows.net/user_impersonation  

Extra Query Params Keys (space separated) -   

[15:57:48.312] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:48 - 78fb10cf-be46-48c3-bb23-c54a25ac04b5] (UnknownClient: 0.0.0.0) === Token Acquisition (UsernamePasswordRequest) started:  

```
Authority Host: login.microsoftonline.com
```

[15:57:48.343] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:48 - 78fb10cf-be46-48c3-bb23-c54a25ac04b5] (UnknownClient: 0.0.0.0) Fetching instance discovery from the network from host login.microsoftonline.com  

[15:57:48.609] [ 12] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:48 - 78fb10cf-be46-48c3-bb23-c54a25ac04b5] (UnknownClient: 0.0.0.0) Resolving authority endpoints... Already resolved? - FALSE  

[15:57:48.703] [ 12] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:48 - 78fb10cf-be46-48c3-bb23-c54a25ac04b5] (UnknownClient: 0.0.0.0) Sending request to userrealm endpoint.  

[15:57:48.803] [ 12] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:48 - 78fb10cf-be46-48c3-bb23-c54a25ac04b5] (UnknownClient: 0.0.0.0)   

[15:57:49.037] [ 12] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49 - 78fb10cf-be46-48c3-bb23-c54a25ac04b5] (UnknownClient: 0.0.0.0) Checking client info returned from the server..  

[15:57:49.053] [ 12] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49 - 78fb10cf-be46-48c3-bb23-c54a25ac04b5] (UnknownClient: 0.0.0.0) Saving Token Response to cache..  

[15:57:49.100] [ 12] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49 - 78fb10cf-be46-48c3-bb23-c54a25ac04b5] (UnknownClient: 0.0.0.0) Looking for scopes for the authority in the cache which intersect with https://graph.windows.net/user_impersonation  

[15:57:49.100] [ 12] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49 - 78fb10cf-be46-48c3-bb23-c54a25ac04b5] (UnknownClient: 0.0.0.0) Intersecting scope entries count - 0  

[15:57:49.100] [ 12] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49 - 78fb10cf-be46-48c3-bb23-c54a25ac04b5] (UnknownClient: 0.0.0.0) Matching entries after filtering by user - 0  

[15:57:49.115] [ 12] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49 - 78fb10cf-be46-48c3-bb23-c54a25ac04b5] (UnknownClient: 0.0.0.0) Saving RT in cache...  

[15:57:49.115] [ 12] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49] (UnknownClient: 0.0.0.0) Serializing token cache with 1 items.  

[15:57:49.475] [ 12] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49 - 78fb10cf-be46-48c3-bb23-c54a25ac04b5] (UnknownClient: 0.0.0.0) === Token Acquisition finished successfully. An access token was returned with Expiration Time: 01/06/2022 01:00:53 +00:00 ===  

[15:57:49.522] [ 17] [INFO ] Authenticate-MSAL: successfully acquired an access token. TenantId=a663168d-6ff4-4d3c-99f6-a68fa20329ca, ExpiresUTC=1/6/2022 1:00:53 AM +00:00, UserInfo=@thechowk.com.au, IdentityProvider=login.windows.net.  

[15:57:49.803] [ 17] [INFO ] DiscoverServiceEndpoint [AdminWebService]: ServiceEndpoint=https://adminwebservice.microsoftonline.com/provisioningservice.svc, Authority=HTTPS://LOGIN.MICROSOFTONLINE.COM/THECHOWK.COM.AU, Resource=https://graph.windows.net.  

[15:57:49.803] [ 17] [INFO ] AzureTenantPage: attempting to connect to Azure via AAD PowerShell.  

[15:57:49.803] [ 17] [INFO ] Authenticate-MSAL [Acquiring token]: STS endpoint (HTTPS://LOGIN.MICROSOFTONLINE.COM/THECHOWK.COM.AU), scope (https://graph.windows.net/user_impersonation), userName (@thechowk.com.au).  

[15:57:49.928] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49] (UnknownClient: 0.0.0.0) Deserialized 1 items to token cache.  

[15:57:49.944] [ 17] [INFO ] Authenticate-MSAL: acquiring token via cache for account ******@thechowk.com.au  

[15:57:49.959] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49 - eb51dd05-796c-4d21-b1cb-b0dd0456aa03] (UnknownClient: 0.0.0.0) MSAL MSAL.Desktop with assembly version '4.5.1.0'. CorrelationId(eb51dd05-796c-4d21-b1cb-b0dd0456aa03)  

[15:57:49.959] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49 - eb51dd05-796c-4d21-b1cb-b0dd0456aa03] (UnknownClient: 0.0.0.0) === OnBehalfOfParameters ===  

LoginHint provided: False  

User provided: True  

ForceRefresh: False  

[15:57:49.959] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49 - eb51dd05-796c-4d21-b1cb-b0dd0456aa03] (UnknownClient: 0.0.0.0)   

=== Request Data ===  

Authority Provided? - True  

Scopes - https://graph.windows.net/user_impersonation  

Extra Query Params Keys (space separated) -   

[15:57:49.959] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49 - eb51dd05-796c-4d21-b1cb-b0dd0456aa03] (UnknownClient: 0.0.0.0) === Token Acquisition (SilentRequest) started:  

```
Authority Host: login.microsoftonline.com
```

[15:57:49.990] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49 - eb51dd05-796c-4d21-b1cb-b0dd0456aa03] (UnknownClient: 0.0.0.0) Looking up access token in the cache.  

[15:57:49.990] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49 - eb51dd05-796c-4d21-b1cb-b0dd0456aa03] (UnknownClient: 0.0.0.0) Filtering by tenant id item count before 1 after 1  

[15:57:49.990] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49 - eb51dd05-796c-4d21-b1cb-b0dd0456aa03] (UnknownClient: 0.0.0.0) Filtering by home account id item count before 1 after 1  

[15:57:49.990] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49 - eb51dd05-796c-4d21-b1cb-b0dd0456aa03] (UnknownClient: 0.0.0.0) Matching entry count -1  

[15:57:49.990] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:49 - eb51dd05-796c-4d21-b1cb-b0dd0456aa03] (UnknownClient: 0.0.0.0) Matching entry count after filtering by scopes - 1  

[15:57:50.006] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:50 - eb51dd05-796c-4d21-b1cb-b0dd0456aa03] (UnknownClient: 0.0.0.0) Access token is not expired. Returning the found cache entry. [Current time (01/05/2022 23:57:50) - Expiration Time (01/06/2022 01:00:53 +00:00) - Extended Expiration Time (01/06/2022 01:00:53 +00:00)]  

[15:57:50.006] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:50 - eb51dd05-796c-4d21-b1cb-b0dd0456aa03] (UnknownClient: 0.0.0.0) Returning access token found in cache. RefreshOn exists ? False  

[15:57:50.006] [ 17] [INFO ] MSAL: (False) MSAL 4.5.1.0 MSAL.Desktop Microsoft Windows NT 10.0.17763.0 [01/05/2022 23:57:50 - eb51dd05-796c-4d21-b1cb-b0dd0456aa03] (UnknownClient: 0.0.0.0) === Token Acquisition finished successfully. An access token was returned with Expiration Time: 01/06/2022 01:00:53 +00:00 ===  

[15:57:50.006] [ 17] [INFO ] Authenticate-MSAL: successfully acquired an access token. TenantId=a663168d-6ff4-4d3c-99f6-a68fa20329ca, ExpiresUTC=1/6/2022 1:00:53 AM +00:00, UserInfo=******@thechowk.com.au, IdentityProvider=login.windows.net.  

[15:57:50.006] [ 17] [INFO ] PowerShellHelper.ConnectMsolService: Connecting using an AccessToken. AzureEnvironment=0.  

[15:57:51.084] [ 17] [INFO ] AzureTenantPage: successfully connected to Azure via AAD PowerShell.  

[15:57:52.417] [ 17] [INFO ] AzureTenantPage: Successfully retrieved company information for tenant a663168d-6ff4-4d3c-99f6-a68fa20329ca.  Initial domain (chowkhobart.onmicrosoft.com).  

[15:57:52.417] [ 17] [INFO ] AzureTenantPage: DirectorySynchronizationEnabled=True  

[15:57:52.417] [ 17] [INFO ] AzureTenantPage: DirectorySynchronizationStatus=Enabled  

[15:57:52.417] [ 17] [INFO ] PowershellHelper: lastDirectorySyncTime=11/1/2021 10:51:01 AM  

[15:57:52.832] [ 17] [INFO ] AzureTenantPageViewModel.GetSynchronizedUserCount: number of synchronized users (max 500) - 43  

[15:57:53.160] [ 17] [INFO ] AzureTenantPageViewModel.GetSynchronizedUserCount: number of synchronized users (max 500) - 43  

[15:57:53.426] [ 17] [INFO ] AzureTen

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-01-06*

@Krishna Shakya      

Thank you for your post!    

Based off your log file, it looks like the issue is with the `Warning - Service ADSync was not found on computer`, since this caused the following error of `StartService unable to start service (ADSync)`.     

    

Potential Root Cause: - Based off of Azure Active Directory Connect: Service ADSync was not found on computer    

This is an MSI engine issue. The problem is that AAD connect installation wizard is still detecting the ADsync service product code when in fact the service is not present anymore.    

Based off the potential root cause, I did find some Warnings within your log file relating to "stale product codes".    

    

From the initial ADSync error message, I found some related threads that go over the potential solution - this requires modifying your Registry Keys. However, when it comes to modifying your Registry, this `isn't a recommended action by Microsoft`, and `should be avoided`, since this can make things worse and can cause irreversible damage the OS.     

If you aren't comfortable modifying your registry and would like to work with our support team on this, please let me know.    

Related Issues:    

Service ADSync was not found on computer    

Service ADSync was not found on computer    

Azure Active Directory Connect: Service ADSync was not found on computer    

If you have any other questions, please let me know.    

Thank you for your time and patience throughout this issue.    

----------    

Please remember to "Accept Answer" if any answer/reply helped, so that others in the community facing similar issues can easily find the solution.
