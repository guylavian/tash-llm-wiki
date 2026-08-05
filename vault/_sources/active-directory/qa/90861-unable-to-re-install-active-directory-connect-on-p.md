---
title: "Unable to re-install Active Directory Connect on Primary DC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/90861/unable-to-re-install-active-directory-connect-on-p
question_id: 90861
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_affiliations: ["Mvp"]
---
# Unable to re-install Active Directory Connect on Primary DC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/90861/unable-to-re-install-active-directory-connect-on-p (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello MSFT,    

I have a primary DC running Windows Server 2012 R2 which contains all of our users in Active Directory which we use to sync over to Azure. We were having some issues with AD Sync so I tried to uninstall, reboot and now I am having issues with re-installing.    

I've downloaded the latest version of AD Connect, ensured that the previous install (and remaining registry files) were gone and downloaded the latest version of .Net. After installing AD Connect, I am able to enter in my credentials, however when the program tries to sync, I get this error:    

"Unable to install the Synchonization Service. Error installing msi package 'SychronizationService.msi".      

Here is the tracelog of the error that I am recieving:    

[22:10:35.149] [  1] [INFO ]     

[22:10:35.149] [  1] [INFO ] ================================================================================    

[22:10:35.149] [  1] [INFO ] Application starting    

[22:10:35.149] [  1] [INFO ] ================================================================================    

[22:10:35.149] [  1] [INFO ] Start Time (Local): Wed, 09 Sep 2020 22:10:35 GMT    

[22:10:35.149] [  1] [INFO ] Start Time (UTC): Wed, 09 Sep 2020 22:10:35 GMT    

[22:10:35.149] [  1] [INFO ] Application Version: 1.5.45.0    

[22:10:35.149] [  1] [INFO ] Application Build Date: 2020-07-25 07:23:51Z    

[22:10:36.216] [  1] [INFO ] Telemetry session identifier: {6eaac65a-8105-45b7-a845-feac0d55d9fe}    

[22:10:36.216] [  1] [INFO ] Telemetry device identifier: ITV5+Lo6iHJubxwxh6hJ2CA0NtY9huORPfBcM80XRcc=    

[22:10:36.216] [  1] [INFO ] Application Build Identifier: AD-IAM-HybridSync master (1da805f80)    

[22:10:36.270] [  1] [INFO ] machine.config path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\machine.config.    

[22:10:36.271] [  1] [INFO ] Default Proxy [ProxyAddress]: <Unspecified>    

[22:10:36.271] [  1] [INFO ] Default Proxy [UseSystemDefault]: Unspecified    

[22:10:36.271] [  1] [INFO ] Default Proxy [BypassOnLocal]: Unspecified    

[22:10:36.271] [  1] [INFO ] Default Proxy [Enabled]: True    

[22:10:36.271] [  1] [INFO ] Default Proxy [AutoDetect]: Unspecified    

[22:10:36.271] [  1] [INFO ] Default Proxy [UseDefaultCredentials]: False    

[22:10:36.300] [  1] [VERB ] Scheduler wizard mutex wait timeout: 00:00:05    

[22:10:36.300] [  1] [INFO ] AADConnect changes ALLOWED: Successfully acquired the configuration change mutex.    

[22:10:36.352] [  1] [INFO ] RootPageViewModel.GetInitialPages: Beginning detection for creating initial pages.    

[22:10:36.352] [  1] [INFO ] Checking if machine version is 6.1.7601 or higher    

[22:10:36.387] [  1] [INFO ] The current operating system version is 6.3.9600, the requirement is 6.1.7601.    

[22:10:36.387] [  1] [INFO ] Password Hash Sync supported: 'True'    

[22:10:36.408] [  1] [INFO ] DetectInstalledComponents stage: The installed OS SKU is 7    

[22:10:36.414] [  1] [INFO ] DetectInstalledComponents stage: Checking install context.    

[22:10:36.418] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Visual C++ 2013 Redistributable Package    

[22:10:36.421] [  1] [VERB ] Getting list of installed packages by upgrade code    

[22:10:36.428] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {20400cf0-de7c-327e-9ae4-f0f38d9085f8}: verified product code {53cf6934-a98d-3d84-9146-fc4edf3d5641}.    

[22:10:36.428] [  1] [VERB ] Package=Microsoft Visual C++ 2013 x64 Minimum Runtime - 12.0.40664, Version=12.0.40664, ProductCode=53cf6934-a98d-3d84-9146-fc4edf3d5641, UpgradeCode=20400cf0-de7c-327e-9ae4-f0f38d9085f8    

[22:10:36.429] [  1] [INFO ] Determining installation action for Microsoft Visual C++ 2013 Redistributable Package (20400cf0-de7c-327e-9ae4-f0f38d9085f8)    

[22:10:36.430] [  1] [INFO ] Product Microsoft Visual C++ 2013 Redistributable Package (version 12.0.40664) is installed.    

[22:10:36.430] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Directory Sync Tool    

[22:10:36.431] [  1] [VERB ] Getting list of installed packages by upgrade code    

[22:10:36.431] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {bef7e7d9-2ac2-44b9-abfc-3335222b92a7}: no registered products found.    

[22:10:36.431] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {dc9e604e-37b0-4efc-b429-21721cf49d0d}: no registered products found.    

[22:10:36.431] [  1] [INFO ] GetProductInfoProperty({525aa4eb-dbe5-4ce9-8a57-cb488eeb1bc9}, VersionString): unknown product    

[22:10:36.431] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {545334d7-13cd-4bab-8da1-2775fa8cf7c2}: stale product code {525aa4eb-dbe5-4ce9-8a57-cb488eeb1bc9}.    

[22:10:36.431] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {545334d7-13cd-4bab-8da1-2775fa8cf7c2}: no registered products found.    

[22:10:36.431] [  1] [WARN ] CheckInstallationState: Stale product code: {525aa4eb-dbe5-4ce9-8a57-cb488eeb1bc9} found for Microsoft Directory Sync Tool. The installation of this component could fail.    

[22:10:36.431] [  1] [WARN ] CheckInstallationState: By uninstalling AADConnect Wizard, an attempt to remove the stale product codes will be performed    

[22:10:36.437] [  1] [INFO ] Determining installation action for Microsoft Directory Sync Tool UpgradeCodes {bef7e7d9-2ac2-44b9-abfc-3335222b92a7}, {dc9e604e-37b0-4efc-b429-21721cf49d0d}    

[22:10:36.437] [  1] [INFO ] DirectorySyncComponent: Product Microsoft Directory Sync Tool is not installed.    

[22:10:36.437] [  1] [INFO ] Performing direct lookup of upgrade codes for: Azure AD Sync Engine    

[22:10:36.437] [  1] [VERB ] Getting list of installed packages by upgrade code    

[22:10:36.437] [  1] [INFO ] GetProductInfoProperty({525aa4eb-dbe5-4ce9-8a57-cb488eeb1bc9}, VersionString): unknown product    

[22:10:36.437] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {545334d7-13cd-4bab-8da1-2775fa8cf7c2}: stale product code {525aa4eb-dbe5-4ce9-8a57-cb488eeb1bc9}.    

[22:10:36.437] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {545334d7-13cd-4bab-8da1-2775fa8cf7c2}: no registered products found.    

[22:10:36.437] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {dc9e604e-37b0-4efc-b429-21721cf49d0d}: no registered products found.    

[22:10:36.437] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {bef7e7d9-2ac2-44b9-abfc-3335222b92a7}: no registered products found.    

[22:10:36.437] [  1] [WARN ] CheckInstallationState: Stale product code: {525aa4eb-dbe5-4ce9-8a57-cb488eeb1bc9} found for Azure AD Sync Engine. The installation of this component could fail.    

[22:10:36.437] [  1] [WARN ] CheckInstallationState: By uninstalling AADConnect Wizard, an attempt to remove the stale product codes will be performed    

[22:10:36.440] [  1] [INFO ] Determining installation action for Azure AD Sync Engine (545334d7-13cd-4bab-8da1-2775fa8cf7c2)    

[22:10:36.622] [  1] [INFO ] Product Azure AD Sync Engine is not installed.    

[22:10:36.622] [  1] [INFO ] Performing direct lookup of upgrade codes for: Azure AD Connect Synchronization Agent    

[22:10:36.622] [  1] [VERB ] Getting list of installed packages by upgrade code    

[22:10:36.622] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {3cd653e3-5195-4ff2-9d6c-db3dacc82c25}: no registered products found.    

[22:10:36.622] [  1] [INFO ] Determining installation action for Azure AD Connect Synchronization Agent (3cd653e3-5195-4ff2-9d6c-db3dacc82c25)    

[22:10:36.622] [  1] [INFO ] Product Azure AD Connect Synchronization Agent is not installed.    

[22:10:36.622] [  1] [INFO ] Performing direct lookup of upgrade codes for: Azure AD Connect Health agent for sync    

[22:10:36.622] [  1] [VERB ] Getting list of installed packages by upgrade code    

[22:10:36.622] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {114fb294-8aa6-43db-9e5c-4ede5e32886f}: no registered products found.    

[22:10:36.622] [  1] [INFO ] Determining installation action for Azure AD Connect Health agent for sync (114fb294-8aa6-43db-9e5c-4ede5e32886f)    

[22:10:36.622] [  1] [INFO ] Product Azure AD Connect Health agent for sync is not installed.    

[22:10:36.622] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Azure AD Connect Authentication Agent    

[22:10:36.622] [  1] [VERB ] Getting list of installed packages by upgrade code    

[22:10:36.622] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {0c06f9df-c56b-42c4-a41b-f5f64d01a35c}: no registered products found.    

[22:10:36.622] [  1] [INFO ] Determining installation action for Microsoft Azure AD Connect Authentication Agent (0c06f9df-c56b-42c4-a41b-f5f64d01a35c)    

[22:10:36.622] [  1] [INFO ] Product Microsoft Azure AD Connect Authentication Agent is not installed.    

[22:10:36.622] [  1] [INFO ] Performing direct lookup of upgrade codes for: Azure AD Connect Administration Agent    

[22:10:36.622] [  1] [VERB ] Getting list of installed packages by upgrade code    

[22:10:36.622] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {886051ec-1165-4df8-a492-19d1e0ff57ee}: no registered products found.    

[22:10:36.622] [  1] [INFO ] Determining installation action for Azure AD Connect Administration Agent (886051ec-1165-4df8-a492-19d1e0ff57ee)    

[22:10:36.623] [  1] [INFO ] Product Azure AD Connect Administration Agent is not installed.    

[22:10:36.623] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft SQL Server 2012 Command Line Utilities    

[22:10:36.623] [  1] [VERB ] Getting list of installed packages by upgrade code    

[22:10:36.623] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {52446750-c08e-49ef-8c2e-1e0662791e7b}: verified product code {89ca7913-f891-4546-8f55-355338677fe6}.    

[22:10:36.623] [  1] [VERB ] Package=Microsoft SQL Server 2012 Command Line Utilities , Version=11.4.7001.0, ProductCode=89ca7913-f891-4546-8f55-355338677fe6, UpgradeCode=52446750-c08e-49ef-8c2e-1e0662791e7b    

[22:10:36.623] [  1] [INFO ] Determining installation action for Microsoft SQL Server 2012 Command Line Utilities (52446750-c08e-49ef-8c2e-1e0662791e7b)    

[22:10:36.623] [  1] [INFO ] Product Microsoft SQL Server 2012 Command Line Utilities (version 11.4.7001.0) is installed.    

[22:10:36.623] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft SQL Server 2012 Express LocalDB    

[22:10:36.623] [  1] [VERB ] Getting list of installed packages by upgrade code    

[22:10:36.623] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {c3593f78-0f11-4d8d-8d82-55460308e261}: verified product code {72b030ed-b1e3-45e5-ba33-a1f5625f2b93}.    

[22:10:36.623] [  1] [VERB ] Package=Microsoft SQL Server 2012 Express LocalDB , Version=11.4.7469.6, ProductCode=72b030ed-b1e3-45e5-ba33-a1f5625f2b93, UpgradeCode=c3593f78-0f11-4d8d-8d82-55460308e261    

[22:10:36.623] [  1] [INFO ] Determining installation action for Microsoft SQL Server 2012 Express LocalDB (c3593f78-0f11-4d8d-8d82-55460308e261)    

[22:10:36.623] [  1] [INFO ] Product Microsoft SQL Server 2012 Express LocalDB (version 11.4.7469.6) is installed.    

[22:10:36.623] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft SQL Server 2012 Native Client    

[22:10:36.623] [  1] [VERB ] Getting list of installed packages by upgrade code    

[22:10:36.623] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {1d2d1fa0-e158-4798-98c6-a296f55414f9}: verified product code {b9274744-8bae-4874-8e59-2610919cd419}.    

[22:10:36.623] [  1] [VERB ] Package=Microsoft SQL Server 2012 Native Client , Version=11.4.7001.0, ProductCode=b9274744-8bae-4874-8e59-2610919cd419, UpgradeCode=1d2d1fa0-e158-4798-98c6-a296f55414f9    

[22:10:36.623] [  1] [INFO ] Determining installation action for Microsoft SQL Server 2012 Native Client (1d2d1fa0-e158-4798-98c6-a296f55414f9)    

[22:10:36.623] [  1] [INFO ] Product Microsoft SQL Server 2012 Native Client (version 11.4.7001.0) is installed.    

[22:10:36.623] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Azure AD Connect Authentication Agent    

[22:10:36.623] [  1] [VERB ] Getting list of installed packages by upgrade code    

[22:10:36.624] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {fb3feca7-5190-43e7-8d4b-5eec88ed9455}: no registered products found.    

[22:10:36.624] [  1] [INFO ] Determining installation action for Microsoft Azure AD Connect Authentication Agent (fb3feca7-5190-43e7-8d4b-5eec88ed9455)    

[22:10:36.624] [  1] [INFO ] Product Microsoft Azure AD Connect Authentication Agent is not installed.    

[22:10:36.624] [  1] [INFO ] Determining installation action for Microsoft Azure AD Connection Tool.    

[22:10:36.645] [  1] [WARN ] Failed to read DisplayName registry key: An error occurred while executing the 'Get-ItemProperty' command. Cannot find path 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\MicrosoftAzureADConnectionTool' because it does not exist.    

[22:10:36.646] [  1] [INFO ] Product Microsoft Azure AD Connection Tool is not installed.    

[22:10:36.646] [  1] [INFO ] Performing direct lookup of upgrade codes for: Azure Active Directory Connect    

[22:10:36.646] [  1] [VERB ] Getting list of installed packages by upgrade code    

[22:10:36.646] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {d61eb959-f2d1-4170-be64-4dc367f451ea}: verified product code {1454be23-6c31-46de-abcb-a3fd413f98c9}.    

[22:10:36.646] [  1] [VERB ] Package=Microsoft Azure AD Connect, Version=1.5.45.0, ProductCode=1454be23-6c31-46de-abcb-a3fd413f98c9, UpgradeCode=d61eb959-f2d1-4170-be64-4dc367f451ea    

[22:10:36.646] [  1] [INFO ] Determining installation action for Azure Active Directory Connect (d61eb959-f2d1-4170-be64-4dc367f451ea)    

[22:10:36.646] [  1] [INFO ] Product Azure Active Directory Connect (version 1.5.45.0) is installed.    

[22:10:36.646] [  1] [INFO ] DetectInstalledComponents stage: Verifying required DCOM registry keys are present.    

[22:10:36.652] [  1] [INFO ] DetectInstalledComponents::CheckBinaryRegistryValueContainsData : Registry value 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\MachineAccessRestriction' is present.    

[22:10:36.652] [  1] [INFO ] DetectInstalledComponents::CheckBinaryRegistryValueContainsData : Registry value 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\MachineLaunchRestriction' is present.    

[22:10:36.652] [  1] [INFO ] DetectInstalledComponents::CheckBinaryRegistryValueContainsData : Registry value 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\DefaultLaunchPermission' is present.    

[22:10:36.794] [  1] [INFO ] ServiceControllerProvider: GetServiceStartMode(seclogon) is 'Manual'.    

[22:10:36.795] [  1] [INFO ] ServiceControllerProvider: verifying EventLog is in state (Running)    

[22:10:36.796] [  1] [INFO ] ServiceControllerProvider: current service status: Running    

[22:10:36.796] [  1] [INFO ] Checking for DirSync conditions.    

[22:10:36.796] [  1] [INFO ] DirSync not detected. Checking for AADSync/AADConnect upgrade conditions.    

[22:10:36.796] [  1] [INFO ] Sync engine is not present. Performing clean install.    

[22:10:42.383] [  1] [INFO ] Page transition from "Welcome" [LicensePageViewModel] to "Express Settings" [ExpressSettingsPageViewModel]    

[22:10:42.430] [  1] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Start background task Microsoft.Online.Deployment.OneADWizard.UI.WizardPages.ExpressSettingsPageViewModel.GatherEnvironmentData in Page:"Express Settings"    

[22:10:42.445] [  1] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Started Background Task Id:281    

[22:10:42.445] [ 20] [INFO ] Checking if machine version is 6.1.7601 or higher    

[22:10:42.445] [ 20] [INFO ] The current operating system version is 6.3.9600, the requirement is 6.1.7601.    

[22:10:42.445] [ 20] [INFO ] Password Hash Sync supported: 'True'    

[22:10:42.477] [  1] [INFO ] Express Settings install is supported: domain-joined + OS version allowed.    

[22:10:43.345] [  1] [INFO ] Express Settings:  Updating page flow for EXPRESS mode install.    

[22:10:43.346] [  1] [INFO ] Called SetWizardMode(ExpressInstall, True)    

[22:10:43.348] [  1] [WARN ] MicrosoftOnlinePersistedStateProvider.Save: zero state elements provided, saving an empty persisted state file    

[22:10:43.359] [  1] [INFO ] MicrosoftOnlinePersistedStateProvider.UpdateFileProtection: updating file protection from the persisted state file: C:\ProgramData\AADConnect\PersistedState.xml, isAddProtection: True    

[22:10:43.375] [  1] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Start background task Microsoft.Online.Deployment.OneADWizard.UI.WizardPages.ExpressSettingsPageViewModel.StartPrerequisiteInstallation in Page:"Express Settings"    

[22:10:43.375] [  1] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Started Background Task Id:473    

[22:10:43.392] [ 22] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Start background task Microsoft.Online.Deployment.OneADWizard.UI.WizardPages.InstallSyncEnginePageViewModel.StartNewInstallation in Page:"Install required components"    

[22:10:43.392] [ 22] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Started Background Task Id:496    

[22:10:43.411] [ 20] [INFO ] SyncEngineSetupViewModel: Validating sync engine settings.    

[22:10:43.415] [ 20] [INFO ] Enter ValidateSqlVersion.    

[22:10:43.415] [ 20] [INFO ] Exit ValidateSqlVersion (localdb).    

[22:10:43.417] [ 20] [INFO ] Enter ValidateSqlAoaAsyncInstance.    

[22:10:43.417] [ 20] [INFO ] Exit ValidateSqlAoaAsyncInstance (localdb).    

[22:10:43.419] [ 20] [INFO ] The ADSync database does not exist and will be created.  serverAdmin=True.    

[22:10:43.419] [ 20] [INFO ] Attaching to the ADSync database: SQLServerName= SQLInstanceName= ServiceAccountName=, state=DoesNotExist, Collation=, /UseExistingDatabase=False.    

[22:10:43.419] [ 20] [INFO ] Starting Sync Engine installation    

[22:10:43.420] [ 20] [INFO ] Starting Prerequisite installation    

[22:10:43.421] [ 20] [VERB ] WorkflowEngine created    

[22:10:43.422] [ 20] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Visual C++ 2013 Redistributable Package    

[22:10:43.422] [ 20] [VERB ] Getting list of installed packages by upgrade code    

[22:10:43.422] [ 20] [INFO ] GetInstalledPackagesByUpgradeCode {20400cf0-de7c-327e-9ae4-f0f38d9085f8}: verified product code {53cf6934-a98d-3d84-9146-fc4edf3d5641}.    

[22:10:43.422] [ 20] [VERB ] Package=Microsoft Visual C++ 2013 x64 Minimum Runtime - 12.0.40664, Version=12.0.40664, ProductCode=53cf6934-a98d-3d84-9146-fc4edf3d5641, UpgradeCode=20400cf0-de7c-327e-9ae4-f0f38d9085f8    

[22:10:43.422] [ 20] [INFO ] Determining installation action for Microsoft Visual C++ 2013 Redistributable Package (20400cf0-de7c-327e-9ae4-f0f38d9085f8)    

[22:10:43.422] [ 20] [INFO ] Product Microsoft Visual C++ 2013 Redistributable Package (version 12.0.40664) is installed.    

[22:10:43.424] [  1] [INFO ] Page transition from "Express Settings" [ExpressSettingsPageViewModel] to "Connect to Azure AD" [AzureTenantPageViewModel]    

[22:10:43.427] [  1] [INFO ] Property Username failed validation with error The Microsoft Azure account name cannot be empty.    

[22:10:46.434] [  1] [INFO ] Property Username failed validation with error Username must be in the format name@keyman  .com or name@keyman  .onmicrosoft.com    

[22:10:50.628] [  1] [INFO ] Property Password failed validation with error A valid domain must be selected.    

[22:10:51.874] [  1] [INFO ] Property Username failed validation with error Username must be in the format name@keyman  .com or name@keyman  .onmicrosoft.com    

[22:10:54.534] [ 22] [INFO ] AzureTenantPage: Beginning Windows Azure tenant credential validation for user - @bitglass.onmicrosoft.com    

[22:10:54.977] [ 22] [INFO ] AzureConfigurationFromPrincipalName: Successfully resolved UPN (@bitglass.onmicrosoft.com) to the Worldwide Azure instance.     

Resolution Method [AzureInstanceDiscovery]: Cloud Instance Name (microsoftonline.com), Tenant Region Scope (NA), Token Endpoint (https://login.microsoftonline.com/1cc02a8e-83af-44e8-b066-26f075845da1/oauth2/token).    

[22:10:54.992] [ 22] [INFO ] ResolveAzureInstance [Worldwide]: authority=HTTPS://LOGIN.WINDOWS.NET/BITGLASS.ONMICROSOFT.COM,     

Resolution Method [AzureInstanceDiscovery]: Cloud Instance Name (microsoftonline.com), Tenant Region Scope (NA), Token Endpoint (https://login.microsoftonline.com/1cc02a8e-83af-44e8-b066-26f075845da1/oauth2/token).    

[22:10:54.992] [ 22] [INFO ] Authenticate-ADAL [Acquiring token]: STS endpoint (HTTPS://LOGIN.WINDOWS.NET/BITGLASS.ONMICROSOFT.COM), resource (https://graph.windows.net), userName (@bitglass.onmicrosoft.com).    

[22:10:55.008] [ 22] [INFO ] ADAL: 2020-09-09T22:10:55.0082600Z: 00000000-0000-0000-0000-000000000000 - AdalLoggerBase.cs: Clearing Cache :- 0 items to be removed    

[22:10:55.008] [ 22] [INFO ] ADAL: 2020-09-09T22:10:55.0082600Z: 00000000-0000-0000-0000-000000000000 - AdalLoggerBase.cs: Successfully Cleared Cache    

[22:10:55.023] [ 22] [INFO ] ADAL: 2020-09-09T22:10:55.0238856Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: ADAL PCL.Desktop with assembly version '5.2.2.0', file version '5.2.2.0' and informational version '5.2.2' is running...    

[22:10:55.023] [ 22] [INFO ] ADAL: 2020-09-09T22:10:55.0238856Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: === Token Acquisition started:     

	CacheType: Microsoft.IdentityModel.Clients.ActiveDirectory.TokenCache (0 items)    

	Authentication Target: User    

	, Authority Host: login.windows.net    

[22:10:55.227] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2270189Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: No matching token was found in the cache    

[22:10:55.227] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2270189Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: Checking MSAL cache for user token cache    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: A match was found in the MSAL cache ? False    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: No matching token was found in the cache    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: Checking MSAL cache for user token cache    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: A match was found in the MSAL cache ? False    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: No matching token was found in the cache    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: Checking MSAL cache for user token cache    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: A match was found in the MSAL cache ? False    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: No matching token was found in the cache    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: Checking MSAL cache for user token cache    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: A match was found in the MSAL cache ? False    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: No matching token was found in the cache    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: Checking MSAL cache for user token cache    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: A match was found in the MSAL cache ? False    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: No matching token was found in the cache    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: Checking MSAL cache for user token cache    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: A match was found in the MSAL cache ? False    

[22:10:55.242] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.2426458Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: Sending request to userrealm endpoint.    

[22:10:55.602] [ 16] [INFO ] ADAL: 2020-09-09T22:10:55.6020238Z: 35bcf081-0676-46f2-bbc8-8d5250e7cc39 - AdalLoggerBase.cs: === Token Acquisition finished successfully. An access token was returned: Expiration Time: 9/9/2020 11:10:54 PM +00:00    

[22:10:55.602] [ 22] [INFO ] Authenticate-ADAL: successfully acquired an access token.  TenantId=1cc02a8e-83af-44e8-b066-26f075845da1, ExpiresUTC=9/9/2020 11:10:54 PM +00:00, UserInfo=@bitglass.onmicrosoft.com, IdentityProvider=https://sts.windows.net/1cc02a8e-83af-44e8-b066-26f075845da1/.    

[22:10:55.617] [ 22] [INFO ] DiscoverServiceEndpoint [AdminWebService]: ServiceEndpoint=https://adminwebservice.microsoftonline.com/provisioningservice.svc, AdalAuthority=HTTPS://LOGIN.WINDOWS.NET/BITGLASS.ONMICROSOFT.COM, AdalResource=https://graph.windows.net.    

[22:10:55.617] [ 22] [INFO ] AzureTenantPage: attempting to connect to Azure via AAD PowerShell.    

[22:10:55.617] [ 22] [INFO ] DiscoverServiceEndpoint [AzurePowerShell]: ServiceEndpoint=https://provisioningapi.microsoftonline.com/provisioningwebservice.svc, AdalAuthority=HTTPS://LOGIN.WINDOWS.NET/BITGLASS.ONMICROSOFT.COM, AdalResource=https://graph.windows.net.    

[22:10:55.617] [ 22] [INFO ] AcquireServiceToken [AzurePowerShell]: acquiring service token.    

[22:10:55.617] [ 22] [INFO ] Authenticate-ADAL [Acquiring token]: STS endpoint (HTTPS://LOGIN.WINDOWS.NET/BITGLASS.ONMICROSOFT.COM), resource (https://graph.windows.net), userName (@bitglass.onmicrosoft.com).    

[22:10:55.617] [ 22] [INFO ] ADAL: 2020-09-09T22:10:55.6176516Z: c8c1e2bc-124c-4939-adeb-598259a5dd63 - AdalLoggerBase.cs: ADAL PCL.Desktop with assembly version '5.2.2.0', file version '5.2.2.0' and informational version '5.2.2' is running...    

[22:10:55.617] [ 22] [INFO ] ADAL: 2020-09-09T22:10:55.6176516Z: c8c1e2bc-124c-4939-adeb-598259a5dd63 - AdalLoggerBase.cs: === Token Acquisition started:     

	CacheType: Microsoft.IdentityModel.Clients.ActiveDirectory.TokenCache (1 items)    

	Authentication Target: User    

	, Authority Host: login.windows.net    

[22:10:55.617] [ 22] [INFO ] ADAL: 2020-09-09T22:10:55.6176516Z: c8c1e2bc-124c-4939-adeb-598259a5dd63 - AdalLoggerBase.cs: An item matching the requested resource was found in the cache    

[22:10:55.617] [ 22] [INFO ] ADAL: 2020-09-09T22:10:55.6176516Z: c8c1e2bc-124c-4939-adeb-598259a5dd63 - AdalLoggerBase.cs: 59.9825519583333 minutes left until token in cache expires    

[22:10:55.617] [ 22] [INFO ] ADAL: 2020-09-09T22:10:55.6176516Z: c8c1e2bc-124c-4939-adeb-598259a5dd63 - AdalLoggerBase.cs: A matching item (access token or refresh token or both) was found in the cache    

[22:10:55.617] [ 22] [INFO ] ADAL: 2020-09-09T22:10:55.6176516Z: c8c1e2bc-124c-4939-adeb-598259a5dd63 - AdalLoggerBase.cs: === Token Acquisition finished successfully. An access token was returned: Expiration Time: 9/9/2020 11:10:54 PM +00:00    

[22:10:55.617] [ 22] [INFO ] Authenticate-ADAL: successfully acquired an access token.  TenantId=1cc02a8e-83af-44e8-b066-26f075845da1, ExpiresUTC=9/9/2020 11:10:54 PM +00:00, UserInfo=@bitglass.onmicrosoft.com, IdentityProvider=https://sts.windows.net/1cc02a8e-83af-44e8-b066-26f075845da1/.    

[22:10:55.617] [ 22] [INFO ] PowerShellHelper.ConnectMsolService: Connecting using an AccessToken. AzureEnvironment=0.    

[22:10:56.164] [ 22] [INFO ] AzureTenantPage: successfully connected to Azure via AAD PowerShell.    

[22:10:56.992] [ 22] [INFO ] AzureTenantPage: Successfully retrieved company information for tenant 1cc02a8e-83af-44e8-b066-26f075845da1.  Initial domain (bitglass.onmicrosoft.com).    

[22:10:56.992] [ 22] [INFO ] AzureTenantPage: DirectorySynchronizationEnabled=True    

[22:10:56.992] [ 22] [INFO ] AzureTenantPage: DirectorySynchronizationStatus=Enabled    

[22:10:56.992] [ 22] [INFO ] PowershellHelper: lastDirectorySyncTime=9/9/2020 9:47:52 PM    

[22:10:58.164] [ 22] [INFO ] AzureTenantPageViewModel.GetSynchronizedUserCount: number of synchronized users (max 500) - 422    

[22:10:59.258] [ 22] [INFO ] AzureTenantPageViewModel.GetSynchronizedUserCount: number of synchronized users (max 500) - 422    

[22:10:59.476] [ 22] [INFO ] AzureTenantPage: Successfully retrieved 7 domains from the tenant.    

[22:10:59.476] [ 22] [INFO ] AzureTenantPage: Calling to get the last dir sync time for the current user    

[22:10:59.664] [ 22] [INFO ] DiscoverServiceEndpoint [AdminWebService]: ServiceEndpoint=https://adminwebservice.microsoftonline.com/provisioningservice.svc, AdalAuthority=HTTPS://LOGIN.WINDOWS.NET/BITGLASS.ONMICROSOFT.COM, AdalResource=https://graph.windows.net.    

[22:10:59.664] [ 22] [INFO ] AcquireServiceToken [AdminWebService]: acquiring service token.    

[22:10:59.664] [ 22] [INFO ] Authenticate-ADAL [Acquiring token]: STS endpoint (HTTPS://LOGIN.WINDOWS.NET/BITGLASS.ONMICROSOFT.COM), resource (https://graph.windows.net), userName (@bitglass.onmicrosoft.com).    

[22:10:59.664] [ 22] [INFO ] ADAL: 2020-09-09T22:10:59.6644632Z: cb2c9a3c-6739-469a-92de-f97b2c35c98e - AdalLoggerBase.cs: ADAL PCL.Desktop with assembly version '5.2.2.0', file version '5.2.2.0' and informational version '5.2.2' is running...    

[22:10:59.664] [ 22] [INFO ] ADAL: 2020-09-09T22:10:59.6644632Z: cb2c9a3c-6739-469a-92de-f97b2c35c98e - AdalLoggerBase.cs: === Token Acquisition started:     

	CacheType: Microsoft.IdentityModel.Clients.ActiveDirectory.TokenCache (1 items)    

	Authentication Target: User    

	, Authority Host: login.windows.net    

[22:10:59.664] [ 22] [INFO ] ADAL: 2020-09-09T22:10:59.6644632Z: cb2c9a3c-6739-469a-92de-f97b2c35c98e - AdalLoggerBase.cs: An item matching the requested resource was found in the cache    

[22:10:59.664] [ 22] [INFO ] ADAL: 2020-09-09T22:10:59.6644632Z: cb2c9a3c-6739-469a-92de-f97b2c35c98e - AdalLoggerBase.cs: 59.9151050983333 minutes left until token in cache expires    

[22:10:59.664] [ 22] [INFO ] ADAL: 2020-09-09T22:10:59.6644632Z: cb2c9a3c-6739-469a-92de-f97b2c35c98e - AdalLoggerBase.cs: A matching item (access token or refresh token or both) was found in the cache    

[22:10:59.664] [ 22] [INFO ] ADAL: 2020-09-09T22:10:59.6644632Z: cb2c9a3c-6739-469a-92de-f97b2c35c98e - AdalLoggerBase.cs: === Token Acquisition finished successfully. An access token was returned: Expiration Time: 9/9/2020 11:10:54 PM +00:00    

[22:10:59.664] [ 22] [INFO ] Authenticate-ADAL: successfully acquired an access token.  TenantId=1cc02a8e-83af-44e8-b066-26f075845da1, ExpiresUTC=9/9/2020 11:10:54 PM +00:00, UserInfo=@bitglass.onmicrosoft.com, IdentityProvider=https://sts.windows.net/1cc02a8e-83af-44e8-b066-26f075845da1/.    

[22:11:00.133] [ 22] [INFO ] GetCompanyConfiguration: tenantId=(1cc02a8e-83af-44e8-b066-26f075845da1), IsDirSyncing=True, IsPasswordSyncing=True, DomainName=, DirSyncFeatures=41017, AllowedFeatures=None.    

[22:11:00.133] [ 22] [INFO ] AzureTenantPage: AdminWebService returned the company information for tenant 1cc02a8e-83af-44e8-b066-26f075845da1.    

[22:11:00.133] [ 22] [INFO ] AzureTenantPage: AzureTenantSourceAnchorAttribute is objectGUID    

[22:11:00.133] [ 22] [INFO ] MicrosoftOnlinePersistedStateProvider.Save: saving the persisted state file    

[22:11:00.133] [ 22] [INFO ] MicrosoftOnlinePersistedStateProvider.UpdateFileProtection: updating file protection from the persisted state fi

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-09-09*

Might check the service credentials format.    

https://learn.microsoft.com/en-us/troubleshoot/azure/active-directory/upgrade-fails-error-code-1603
