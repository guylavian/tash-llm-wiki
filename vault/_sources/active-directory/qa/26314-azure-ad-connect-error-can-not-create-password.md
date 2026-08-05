---
title: "Azure AD Connect  Error - can not create password"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/26314/azure-ad-connect-error-can-not-create-password
question_id: 26314
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Azure AD Connect  Error - can not create password

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/26314/azure-ad-connect-error-can-not-create-password (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Fresh install of Windows Server 2016 Standard. Updated. Not activated, waiting on PK. I'm running AAD Connect to sync existing users from MS365 to Windows Server domain.

Getting error:

Unable to install the Synchronization Service. Azure AD Connect is not able to create a password which satisfies the current password ploicy. We reccomend you peform a custom installation and specify your own ADSYnc service account.

I don't want to create my own service account. The password policy on the Windows 2016 Server has been disabled. I can not find any referenence to this error message.

LOG FILE:

[22:30:12.376] [ 1] [INFO ]  

[22:30:12.376] [ 1] [INFO ] ================================================================================  

[22:30:12.376] [ 1] [INFO ] Application starting  

[22:30:12.376] [ 1] [INFO ] ================================================================================  

[22:30:12.376] [ 1] [INFO ] Start Time (Local): Fri, 08 May 2020 22:30:12 GMT  

[22:30:12.376] [ 1] [INFO ] Start Time (UTC): Sat, 09 May 2020 03:30:12 GMT  

[22:30:12.376] [ 1] [INFO ] Application Version: 1.5.30.0  

[22:30:12.376] [ 1] [INFO ] Application Build Date: 2020-05-04 17:57:50Z  

[22:30:14.611] [ 1] [INFO ] Telemetry session identifier: {ee7a89cd-ff83-4574-b27a-7197feeab47c}  

[22:30:14.611] [ 1] [INFO ] Telemetry device identifier: AP0VjTNnPE7z7pq2+sR92yep3yTia7opv/1Pl0y59UA=  

[22:30:14.611] [ 1] [INFO ] Application Build Identifier: AD-IAM-HybridSync master (5e597c78f)  

[22:30:14.736] [ 1] [INFO ] machine.config path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\machine.config.  

[22:30:14.752] [ 1] [INFO ] Default Proxy [ProxyAddress]: <Unspecified>  

[22:30:14.752] [ 1] [INFO ] Default Proxy [UseSystemDefault]: Unspecified  

[22:30:14.752] [ 1] [INFO ] Default Proxy [BypassOnLocal]: Unspecified  

[22:30:14.752] [ 1] [INFO ] Default Proxy [Enabled]: True  

[22:30:14.752] [ 1] [INFO ] Default Proxy [AutoDetect]: Unspecified  

[22:30:14.752] [ 1] [INFO ] Default Proxy [UseDefaultCredentials]: False  

[22:30:14.814] [ 1] [VERB ] Scheduler wizard mutex wait timeout: 00:00:05  

[22:30:14.814] [ 1] [INFO ] AADConnect changes ALLOWED: Successfully acquired the configuration change mutex.  

[22:30:14.923] [ 1] [INFO ] RootPageViewModel.GetInitialPages: Beginning detection for creating initial pages.  

[22:30:14.955] [ 1] [INFO ] Loading the persisted settings .  

[22:30:15.017] [ 1] [INFO ] Checking if machine version is 6.1.7601 or higher  

[22:30:15.064] [ 1] [INFO ] The current operating system version is 10.0.14393, the requirement is 6.1.7601.  

[22:30:15.064] [ 1] [INFO ] Password Hash Sync supported: 'True'  

[22:30:15.127] [ 1] [INFO ] DetectInstalledComponents stage: The installed OS SKU is 7  

[22:30:15.142] [ 1] [INFO ] DetectInstalledComponents stage: Checking install context.  

[22:30:15.142] [ 1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Visual C++ 2013 Redistributable Package  

[22:30:15.158] [ 1] [VERB ] Getting list of installed packages by upgrade code  

[22:30:15.173] [ 1] [INFO ] GetInstalledPackagesByUpgradeCode {20400cf0-de7c-327e-9ae4-f0f38d9085f8}: verified product code {a749d8e6-b613-3be3-8f5f-045c84eba29b}.  

[22:30:15.173] [ 1] [VERB ] Package=Microsoft Visual C++ 2013 x64 Minimum Runtime - 12.0.21005, Version=12.0.21005, ProductCode=a749d8e6-b613-3be3-8f5f-045c84eba29b, UpgradeCode=20400cf0-de7c-327e-9ae4-f0f38d9085f8  

[22:30:15.173] [ 1] [INFO ] Determining installation action for Microsoft Visual C++ 2013 Redistributable Package (20400cf0-de7c-327e-9ae4-f0f38d9085f8)  

[22:30:15.173] [ 1] [INFO ] Product Microsoft Visual C++ 2013 Redistributable Package (version 12.0.21005) is installed.  

[22:30:15.173] [ 1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Directory Sync Tool  

[22:30:15.173] [ 1] [VERB ] Getting list of installed packages by upgrade code  

[22:30:15.173] [ 1] [INFO ] GetInstalledPackagesByUpgradeCode {bef7e7d9-2ac2-44b9-abfc-3335222b92a7}: no registered products found.  

[22:30:15.173] [ 1] [INFO ] GetInstalledPackagesByUpgradeCode {dc9e604e-37b0-4efc-b429-21721cf49d0d}: no registered products found.  

[22:30:15.173] [ 1] [INFO ] GetInstalledPackagesByUpgradeCode {545334d7-13cd-4bab-8da1-2775fa8cf7c2}: no registered products found.  

[22:30:15.189] [ 1] [INFO ] Determining installation action for Microsoft Directory Sync Tool UpgradeCodes {bef7e7d9-2ac2-44b9-abfc-3335222b92a7}, {dc9e604e-37b0-4efc-b429-21721cf49d0d}  

[22:30:15.189] [ 1] [INFO ] DirectorySyncComponent: Product Microsoft Directory Sync Tool is not installed.  

[22:30:15.189] [ 1] [INFO ] Performing direct lookup of upgrade codes for: Azure AD Sync Engine  

[22:30:15.189] [ 1] [VERB ] Getting list of installed packages by upgrade code  

[22:30:15.189] [ 1] [INFO ] GetInstalledPackagesByUpgradeCode {545334d7-13cd-4bab-8da1-2775fa8cf7c2}: no registered products found.  

[22:30:15.189] [ 1] [INFO ] GetInstalledPackagesByUpgradeCode {dc9e604e-37b0-4efc-b429-21721cf49d0d}: no registered products found.  

[22:30:15.189] [ 1] [INFO ] GetInstalledPackagesByUpgradeCode {bef7e7d9-2ac2-44b9-abfc-3335222b92a7}: no registered products found.  

[22:30:15.205] [ 1] [INFO ] Determining installation action for Azure AD Sync Engine (545334d7-13cd-4bab-8da1-2775fa8cf7c2)  

[22:30:15.673] [ 1] [INFO ] Product Azure AD Sync Engine is not installed.  

[22:30:15.673] [ 1] [INFO ] Performing direct lookup of upgrade codes for: Azure AD Connect Synchronization Agent  

[22:30:15.673] [ 1] [VERB ] Getting list of installed packages by upgrade code  

[22:30:15.673] [ 1] [INFO ] GetInstalledPackagesByUpgradeCode {3cd653e3-5195-4ff2-9d6c-db3dacc82c25}: no registered products found.  

[22:30:15.673] [ 1] [INFO ] Determining installation action for Azure AD Connect Synchronization Agent (3cd653e3-5195-4ff2-9d6c-db3dacc82c25)  

[22:30:15.673] [ 1] [INFO ] Product Azure AD Connect Synchronization Agent is not installed.  

[22:30:15.673] [ 1] [INFO ] Performing direct lookup of upgrade codes for: Azure AD Connect Health agent for sync  

[22:30:15.673] [ 1] [VERB ] Getting list of installed packages by upgrade code  

[22:30:15.673] [ 1] [INFO ] GetInstalledPackagesByUpgradeCode {114fb294-8aa6-43db-9e5c-4ede5e32886f}: no registered products found.  

[22:30:15.673] [ 1] [INFO ] Determining installation action for Azure AD Connect Health agent for sync (114fb294-8aa6-43db-9e5c-4ede5e32886f)  

[22:30:15.673] [ 1] [INFO ] Product Azure AD Connect Health agent for sync is not installed.  

[22:30:15.673] [ 1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Azure AD Connect Authentication Agent  

[22:30:15.673] [ 1] [VERB ] Getting list of installed packages by upgrade code  

[22:30:15.673] [ 1] [INFO ] GetInstalledPackagesByUpgradeCode {0c06f9df-c56b-42c4-a41b-f5f64d01a35c}: no registered products found.  

[22:30:15.673] [ 1] [INFO ] Determining installation action for Microsoft Azure AD Connect Authentication Agent (0c06f9df-c56b-42c4-a41b-f5f64d01a35c)  

[22:30:15.673] [ 1] [INFO ] Product Microsoft Azure AD Connect Authentication Agent is not installed.  

[22:30:15.673] [ 1] [INFO ] Performing direct lookup of upgrade codes for: Azure AD Connect Administration Agent  

[22:30:15.673] [ 1] [VERB ] Getting list of installed packages by upgrade code  

[22:30:15.673] [ 1] [INFO ] GetInstalledPackagesByUpgradeCode {886051ec-1165-4df8-a492-19d1e0ff57ee}: no registered products found.  

[22:30:15.673] [ 1] [INFO ] Determining installation action for Azure AD Connect Administration Agent (886051ec-1165-4df8-a492-19d1e0ff57ee)  

[22:30:15.673] [ 1] [INFO ] Product Azure AD Connect Administration Agent is not installed.  

[22:30:15.673] [ 1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft SQL Server 2012 Command Line Utilities  

[22:30:15.673] [ 1] [VERB ] Getting list of installed packages by upgrade code  

[22:30:15.673] [ 1] [INFO ] GetInstalledPackagesByUpgradeCode {52446750-c08e-49ef-8c2e-1e0662791e7b}: verified product code {89ca7913-f891-4546-8f55-355338677fe6}.  

[22:30:15.673] [ 1] [VERB ] Package=Microsoft SQL Server 2012 Command Line Utilities , Version=11.4.7001.0, ProductCode=89ca7913-f891-4546-8f55-355338677fe6, UpgradeCode=52446750-c08e-49ef-8c2e-1e0662791e7b  

[22:30:15.673] [ 1] [INFO ] Determining installation action for Microsoft SQL Server 2012 Command Line Utilities (52446750-c08e-49ef-8c2e-1e0662791e7b)  

[22:30:15.673] [ 1] [INFO ] Product Microsoft SQL Server 2012 Command Line Utilities (version 11.4.7001.0) is installed.  

[22:30:15.673] [ 1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft SQL Server 2012 Express LocalDB  

[22:30:15.673] [ 1] [VERB ] Getting list of installed packages by upgrade code  

[22:30:15.673] [ 1] [INFO ] GetInstalledPackagesByUpgradeCode {c3593f78-0f11-4d8d-8d82-55460308e261}: verified product code {72b030ed-b1e3-45e5-ba33-a1f5625f2b93}.  

[22:30:15.689] [ 1] [VERB ] Package=Microsoft SQL Server 2012 Express LocalDB , Version=11.4.7469.6, ProductCode=72b030ed-b1e3-45e5-ba33-a1f5625f2b93, UpgradeCode=c3593f78-0f11-4d8d-8d82-55460308e261  

[22:30:15.689] [ 1] [INFO ] Determining installation action for Microsoft SQL Server 2012 Express LocalDB (c3593f78-0f11-4d8d-8d82-55460308e261)  

[22:30:15.689] [ 1] [INFO ] Product Microsoft SQL Server 2012 Express LocalDB (version 11.4.7469.6) is installed.  

[22:30:15.689] [ 1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft SQL Server 2012 Native Client  

[22:30:15.689] [ 1] [VERB ] Getting list of installed packages by upgrade code  

[22:30:15.689] [ 1] [INFO ] GetInstalledPackagesByUpgradeCode {1d2d1fa0-e158-4798-98c6-a296f55414f9}: verified product code {b9274744-8bae-4874-8e59-2610919cd419}.  

[22:30:15.689] [ 1] [VERB ] Package=Microsoft SQL Server 2012 Native Client , Version=11.4.7001.0, ProductCode=b9274744-8bae-4874-8e59-2610919cd419, UpgradeCode=1d2d1fa0-e158-4798-98c6-a296f55414f9  

[22:30:15.689] [ 1] [INFO ] Determining installation action for Microsoft SQL Server 2012 Native Client (1d2d1fa0-e158-4798-98c6-a296f55414f9)  

[22:30:15.689] [ 1] [INFO ] Product Microsoft SQL Server 2012 Native Client (version 11.4.7001.0) is installed.  

[22:30:15.689] [ 1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Azure AD Connect Authentication Agent  

[22:30:15.689] [ 1] [VERB ] Getting list of installed packages by upgrade code  

[22:30:15.689] [ 1] [INFO ] GetInstalledPackagesByUpgradeCode {fb3feca7-5190-43e7-8d4b-5eec88ed9455}: no registered products found.  

[22:30:15.689] [ 1] [INFO ] Determining installation action for Microsoft Azure AD Connect Authentication Agent (fb3feca7-5190-43e7-8d4b-5eec88ed9455)  

[22:30:15.689] [ 1] [INFO ] Product Microsoft Azure AD Connect Authentication Agent is not installed.  

[22:30:15.689] [ 1] [INFO ] Determining installation action for Microsoft Azure AD Connection Tool.  

[22:30:15.767] [ 1] [WARN ] Failed to read DisplayName registry key: An error occurred while executing the 'Get-ItemProperty' command. Cannot find path 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\MicrosoftAzureADConnectionTool' because it does not exist.  

[22:30:15.767] [ 1] [INFO ] Product Microsoft Azure AD Connection Tool is not installed.  

[22:30:15.767] [ 1] [INFO ] Performing direct lookup of upgrade codes for: Azure Active Directory Connect  

[22:30:15.767] [ 1] [VERB ] Getting list of installed packages by upgrade code  

[22:30:15.767] [ 1] [INFO ] GetInstalledPackagesByUpgradeCode {d61eb959-f2d1-4170-be64-4dc367f451ea}: verified product code {553423be-b5bf-4e1e-8afc-f97777c1a7d7}.  

[22:30:15.767] [ 1] [VERB ] Package=Microsoft Azure AD Connect, Version=1.5.30.0, ProductCode=553423be-b5bf-4e1e-8afc-f97777c1a7d7, UpgradeCode=d61eb959-f2d1-4170-be64-4dc367f451ea  

[22:30:15.767] [ 1] [INFO ] Determining installation action for Azure Active Directory Connect (d61eb959-f2d1-4170-be64-4dc367f451ea)  

[22:30:15.767] [ 1] [INFO ] Product Azure Active Directory Connect (version 1.5.30.0) is installed.  

[22:30:15.767] [ 1] [INFO ] DetectInstalledComponents stage: Verifying required DCOM registry keys are present.  

[22:30:15.783] [ 1] [INFO ] DetectInstalledComponents::CheckBinaryRegistryValueContainsData : Registry value 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\MachineAccessRestriction' is present.  

[22:30:15.783] [ 1] [INFO ] DetectInstalledComponents::CheckBinaryRegistryValueContainsData : Registry value 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\MachineLaunchRestriction' is present.  

[22:30:15.783] [ 1] [INFO ] DetectInstalledComponents::CheckBinaryRegistryValueContainsData : Registry value 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\DefaultLaunchPermission' is present.  

[22:30:16.111] [ 1] [INFO ] ServiceControllerProvider: GetServiceStartMode(seclogon) is 'Manual'.  

[22:30:16.111] [ 1] [INFO ] ServiceControllerProvider: verifying EventLog is in state (Running)  

[22:30:16.111] [ 1] [INFO ] ServiceControllerProvider: current service status: Running  

[22:30:16.111] [ 1] [INFO ] Checking for DirSync conditions.  

[22:30:16.111] [ 1] [INFO ] DirSync not detected. Checking for AADSync/AADConnect upgrade conditions.  

[22:30:16.127] [ 1] [INFO ] Initial configuration is incomplete.  

[22:30:16.127] [ 1] [INFO ] Resume Wizard from previous Azure service connectivity failure.  

[22:30:16.158] [ 1] [INFO ] SyncDataProvider:LoadSettings - loading context with persisted global settings.  

[22:30:16.283] [ 1] [ERROR] Configuration policy could not be retrieved (GetGlobalConfigurationParameters). Details: System.Management.Automation.CommandNotFoundException: The term 'Get-ADSyncGlobalSettingsParameter' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.  

at System.Management.Automation.Runspaces.PipelineBase.Invoke(IEnumerable input)  

at System.Management.Automation.PowerShell.Worker.ConstructPipelineAndDoWork(Runspace rs, Boolean performSyncInvoke)  

at System.Management.Automation.PowerShell.Worker.CreateRunspaceIfNeededAndDoWork(Runspace rsToUse, Boolean isSync)  

at System.Management.Automation.PowerShell.CoreInvokeHelper[TInput,TOutput](PSDataCollection`1 input, PSDataCollection`1 output, PSInvocationSettings settings)  

at System.Management.Automation.PowerShell.CoreInvoke[TInput,TOutput](PSDataCollection`1 input, PSDataCollection`1 output, PSInvocationSettings settings)  

at System.Management.Automation.PowerShell.Invoke(IEnumerable input, PSInvocationSettings settings)  

at Microsoft.Online.Deployment.PowerShell.LocalPowerShell.Invoke()  

at Microsoft.Online.Deployment.PowerShell.PowerShellAdapter.TypeDependencies.InvokePowerShell(IPowerShell powerShell)  

at Microsoft.Online.Deployment.PowerShell.PowerShellAdapter.InvokePowerShellCommand(String commandName, InitialSessionState initialSessionState, IDictionary`2 commandParameters, Boolean isScript)  

at Microsoft.Azure.ActiveDirectory.Synchronization.PowerShellConfigAdapter.GlobalSettingsConfigAdapter.GetGlobalConfigurationParameters()  

at Microsoft.Online.Deployment.Types.Providers.SyncDataProvider.LoadSettings(IAadSyncContext aadSyncContext)  

[22:30:16.361] [ 1] [INFO ] PreviewFeatureState [PolicyPreview]: feature state is (False).  

[22:30:16.424] [ 1] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Start background task Microsoft.Online.Deployment.OneADWizard.UI.WizardPages.ExpressSettingsPageViewModel.GatherEnvironmentData in Page:"Express Settings"  

[22:30:16.424] [ 1] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Started Background Task Id:13  

[22:30:16.439] [ 16] [INFO ] Checking if machine version is 6.1.7601 or higher  

[22:30:16.439] [ 16] [INFO ] The current operating system version is 10.0.14393, the requirement is 6.1.7601.  

[22:30:16.439] [ 16] [INFO ] Password Hash Sync supported: 'True'  

[22:30:16.908] [ 1] [INFO ] Express Settings install is supported: domain-joined + OS version allowed.  

[22:30:52.196] [ 1] [INFO ] Express Settings: Updating page flow for EXPRESS mode install.  

[22:30:52.198] [ 1] [INFO ] Called SetWizardMode(ExpressInstall, True)  

[22:30:52.202] [ 1] [WARN ] MicrosoftOnlinePersistedStateProvider.Save: zero state elements provided, saving an empty persisted state file  

[22:30:52.205] [ 1] [INFO ] MicrosoftOnlinePersistedStateProvider.UpdateFileProtection: updating file protection from the persisted state file: C:\ProgramData\AADConnect\PersistedState.xml, isAddProtection: False  

[22:30:52.235] [ 1] [INFO ] MicrosoftOnlinePersistedStateProvider.UpdateFileProtection: updating file protection from the persisted state file: C:\ProgramData\AADConnect\PersistedState.xml, isAddProtection: True  

[22:30:52.271] [ 1] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Start background task Microsoft.Online.Deployment.OneADWizard.UI.WizardPages.ExpressSettingsPageViewModel.StartPrerequisiteInstallation in Page:"Express Settings"  

[22:30:52.272] [ 1] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Started Background Task Id:7301  

[22:30:52.308] [ 11] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Start background task Microsoft.Online.Deployment.OneADWizard.UI.WizardPages.InstallSyncEnginePageViewModel.StartNewInstallation in Page:"Install required components"  

[22:30:52.308] [ 11] [INFO ] ProgressWizardPageViewModel:StartProgressOperation Started Background Task Id:7324  

[22:30:52.355] [ 12] [INFO ] SyncEngineSetupViewModel: Validating sync engine settings.  

[22:30:52.355] [ 12] [INFO ] Enter ValidateSqlVersion.  

[22:30:52.355] [ 12] [INFO ] Exit ValidateSqlVersion (localdb).  

[22:30:52.371] [ 12] [INFO ] Enter ValidateSqlAoaAsyncInstance.  

[22:30:52.371] [ 12] [INFO ] Exit ValidateSqlAoaAsyncInstance (localdb).  

[22:30:52.371] [ 12] [INFO ] The ADSync database does not exist and will be created. serverAdmin=True.  

[22:30:52.371] [ 12] [INFO ] Attaching to the ADSync database: SQLServerName= SQLInstanceName= ServiceAccountName=, state=DoesNotExist, Collation=, /UseExistingDatabase=False.  

[22:30:52.371] [ 12] [INFO ] Starting Sync Engine installation  

[22:30:52.371] [ 12] [INFO ] Starting Prerequisite installation  

[22:30:52.371] [ 12] [VERB ] WorkflowEngine created  

[22:30:52.371] [ 12] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Visual C++ 2013 Redistributable Package  

[22:30:52.371] [ 12] [VERB ] Getting list of installed packages by upgrade code  

[22:30:52.386] [ 12] [INFO ] GetInstalledPackagesByUpgradeCode {20400cf0-de7c-327e-9ae4-f0f38d9085f8}: verified product code {a749d8e6-b613-3be3-8f5f-045c84eba29b}.  

[22:30:52.386] [ 12] [VERB ] Package=Microsoft Visual C++ 2013 x64 Minimum Runtime - 12.0.21005, Version=12.0.21005, ProductCode=a749d8e6-b613-3be3-8f5f-045c84eba29b, UpgradeCode=20400cf0-de7c-327e-9ae4-f0f38d9085f8  

[22:30:52.386] [ 12] [INFO ] Determining installation action for Microsoft Visual C++ 2013 Redistributable Package (20400cf0-de7c-327e-9ae4-f0f38d9085f8)  

[22:30:52.386] [ 12] [INFO ] Product Microsoft Visual C++ 2013 Redistributable Package (version 12.0.21005) is installed.  

[22:30:52.386] [ 1] [INFO ] Page transition from "Express Settings" [ExpressSettingsPageViewModel] to "Connect to Azure AD" [AzureTenantPageViewModel]  

[22:30:52.433] [ 1] [INFO ] Property Password failed validation with error A valid domain must be selected.  

[22:31:48.793] [ 13] [INFO ] AzureTenantPage: Beginning Windows Azure tenant credential validation for user - @watkinsmuseum.org  

[22:31:48.857] [ 13] [INFO ] AzureConfigurationFromPrincipalName: Successfully resolved UPN (@watkinsmuseum.org) to the Worldwide Azure instance.  

Resolution Method [Registry Configuration]: Worldwide.  

[22:31:48.873] [ 13] [INFO ] ResolveAzureInstance [Worldwide]: authority=HTTPS://LOGIN.WINDOWS.NET/WATKINSMUSEUM.ORG,  

Resolution Method [Registry Configuration]: Worldwide.  

[22:31:48.904] [ 13] [INFO ] Authenticate-ADAL [Acquiring token]: STS endpoint (HTTPS://LOGIN.WINDOWS.NET/WATKINSMUSEUM.ORG), resource (https://graph.windows.net), userName (@watkinsmuseum.org).  

[22:31:48.951] [ 13] [INFO ] ADAL: 2020-05-09T03:31:48.9516422Z: 00000000-0000-0000-0000-000000000000 - AdalLoggerBase.cs: Clearing Cache :- 0 items to be removed  

[22:31:48.967] [ 13] [INFO ] ADAL: 2020-05-09T03:31:48.9516422Z: 00000000-0000-0000-0000-000000000000 - AdalLoggerBase.cs: Successfully Cleared Cache  

[22:31:48.982] [ 13] [INFO ] ADAL: 2020-05-09T03:31:48.9829042Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: ADAL PCL.Desktop with assembly version '5.2.2.0', file version '5.2.2.0' and informational version '5.2.2' is running...  

[22:31:48.982] [ 13] [INFO ] ADAL: 2020-05-09T03:31:48.9829042Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: === Token Acquisition started:  

CacheType: Microsoft.IdentityModel.Clients.ActiveDirectory.TokenCache (0 items)  

Authentication Target: User  

, Authority Host: login.windows.net  

[22:31:49.482] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4829306Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: No matching token was found in the cache  

[22:31:49.482] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4829306Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: Checking MSAL cache for user token cache  

[22:31:49.498] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4985432Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: A match was found in the MSAL cache ? False  

[22:31:49.498] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4985432Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: No matching token was found in the cache  

[22:31:49.498] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4985432Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: Checking MSAL cache for user token cache  

[22:31:49.498] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4985432Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: A match was found in the MSAL cache ? False  

[22:31:49.498] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4985432Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: No matching token was found in the cache  

[22:31:49.498] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4985432Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: Checking MSAL cache for user token cache  

[22:31:49.498] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4985432Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: A match was found in the MSAL cache ? False  

[22:31:49.498] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4985432Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: No matching token was found in the cache  

[22:31:49.498] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4985432Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: Checking MSAL cache for user token cache  

[22:31:49.498] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4985432Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: A match was found in the MSAL cache ? False  

[22:31:49.498] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4985432Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: No matching token was found in the cache  

[22:31:49.498] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4985432Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: Checking MSAL cache for user token cache  

[22:31:49.498] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4985432Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: A match was found in the MSAL cache ? False  

[22:31:49.498] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4985432Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: No matching token was found in the cache  

[22:31:49.498] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4985432Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: Checking MSAL cache for user token cache  

[22:31:49.498] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.4985432Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: A match was found in the MSAL cache ? False  

[22:31:49.514] [ 21] [INFO ] ADAL: 2020-05-09T03:31:49.5141681Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: Sending request to userrealm endpoint.  

[22:31:50.154] [ 21] [INFO ] ADAL: 2020-05-09T03:31:50.1548260Z: f6b81f8e-dbcf-48b9-86e9-c260f875b047 - AdalLoggerBase.cs: === Token Acquisition finished successfully. An access token was returned: Expiration Time: 5/9/2020 4:31:49 AM +00:00  

[22:31:50.170] [ 13] [INFO ] Authenticate-ADAL: successfully acquired an access token. TenantId=dd8faa70-8371-4e3f-9c58-e18c5dd70b82, ExpiresUTC=5/9/2020 4:31:49 AM +00:00, UserInfo=@watkinsmuseum.org, IdentityProvider=https://sts.windows.net/dd8faa70-8371-4e3f-9c58-e18c5dd70b82/.  

[22:31:50.201] [ 13] [INFO ] DiscoverServiceEndpoint [AdminWebService]: ServiceEndpoint=https://adminwebservice.microsoftonline.com/provisioningservice.svc, AdalAuthority=HTTPS://LOGIN.WINDOWS.NET/WATKINSMUSEUM.ORG, AdalResource=https://graph.windows.net.  

[22:31:50.217] [ 13] [INFO ] AzureTenantPage: attempting to connect to Azure via AAD PowerShell.  

[22:31:50.217] [ 13] [INFO ] DiscoverServiceEndpoint [AzurePowerShell]: ServiceEndpoint=https://provisioningapi.microsoftonline.com/provisioningwebservice.svc, AdalAuthority=HTTPS://LOGIN.WINDOWS.NET/WATKINSMUSEUM.ORG, AdalResource=https://graph.windows.net.  

[22:31:50.217] [ 13] [INFO ] AcquireServiceToken [AzurePowerShell]: acquiring service token.  

[22:31:50.217] [ 13] [INFO ] Authenticate-ADAL [Acquiring token]: STS endpoint (HTTPS://LOGIN.WINDOWS.NET/WATKINSMUSEUM.ORG), resource (https://graph.windows.net), userName (@watkinsmuseum.org).  

[22:31:50.217] [ 13] [INFO ] ADAL: 2020-05-09T03:31:50.2173398Z: e3ad7801-ba8f-423b-8931-6efd683b33c9 - AdalLoggerBase.cs: ADAL PCL.Desktop with assembly version '5.2.2.0', file version '5.2.2.0' and informational version '5.2.2' is running...  

[22:31:50.217] [ 13] [INFO ] ADAL: 2020-05-09T03:31:50.2173398Z: e3ad7801-ba8f-423b-8931-6efd683b33c9 - AdalLoggerBase.cs: === Token Acquisition started:  

CacheType: Microsoft.IdentityModel.Clients.ActiveDirectory.TokenCache (1 items)  

Authentication Target: User  

, Authority Host: login.windows.net  

[22:31:50.217] [ 13] [INFO ] ADAL: 2020-05-09T03:31:50.2173398Z: e3ad7801-ba8f-423b-8931-6efd683b33c9 - AdalLoggerBase.cs: An item matching the requested resource was found in the cache  

[22:31:50.217] [ 13] [INFO ] ADAL: 2020-05-09T03:31:50.2173398Z: e3ad7801-ba8f-423b-8931-6efd683b33c9 - AdalLoggerBase.cs: 59.9809894883333 minutes left until token in cache expires  

[22:31:50.217] [ 13] [INFO ] ADAL: 2020-05-09T03:31:50.2173398Z: e3ad7801-ba8f-423b-8931-6efd683b33c9 - AdalLoggerBase.cs: A matching item (access token or refresh token or both) was found in the cache  

[22:31:50.217] [ 13] [INFO ] ADAL: 2020-05-09T03:31:50.2173398Z: e3ad7801-ba8f-423b-8931-6efd683b33c9 - AdalLoggerBase.cs: === Token Acquisition finished successfully. An access token was returned: Expiration Time: 5/9/2020 4:31:49 AM +00:00  

[22:31:50.217] [ 13] [INFO ] Authenticate-ADAL: successfully acquired an access token. TenantId=dd8faa70-8371-4e3f-9c58-e18c5dd70b82, ExpiresUTC=5/9/2020 4:31:49 AM +00:00, UserInfo=@watkinsmuseum.org, IdentityProvider=https://sts.windows.net/dd8faa70-8371-4e3f-9c58-e18c5dd70b82/.  

[22:31:50.217] [ 13] [INFO ] PowerShellHelper.ConnectMsolService: Connecting using an AccessToken. AzureEnvironment=0.  

[22:31:51.451] [ 13] [INFO ] AzureTenantPage: successfully connected to Azure via AAD PowerShell.  

[22:31:52.889] [ 13] [INFO ] AzureTenantPage: Successfully retrieved company information for tenant dd8faa70-8371-4e3f-9c58-e18c5dd70b82. Initial domain (watkinsmuseum.onmicrosoft.com).  

[22:31:52.889] [ 13] [INFO ] AzureTenantPage: DirectorySynchronizationEnabled=False  

[22:31:52.889] [ 13] [INFO ] AzureTenantPage: DirectorySynchronizationStatus=Disabled  

[22:31:52.904] [ 13] [INFO ] PowershellHelper: lastDirectorySyncTime=null  

[22:31:53.436] [ 13] [INFO ] AzureTenantPageViewModel.GetSynchronizedUserCount: number of synchronized users (max 500) - 13  

[22:31:53.826] [ 13] [INFO ] AzureTenantPageViewModel.GetSynchronizedUserCount: number of synchronized users (max 500) - 13  

[22:31:54.201] [ 13] [INFO ] AzureTenantPage: Successfully retrieved 2 domains from the tenant.  

[22:31:54.201] [ 13] [INFO ] AzureTenantPage: Calling to get the last dir sync time for the current user  

[22:31:54.530] [ 13] [INFO ] DiscoverServiceEndpoint [AdminWebService]: ServiceEndpoint=https://adminwebservice.microsoftonline.com/provisioningservice.svc, AdalAuthority=HTTPS://LOGIN.WINDOWS.NET/WATKINSMUSEUM.ORG, AdalResource=https://graph.windows.net.  

[22:31:54.530] [ 13] [INFO ] AcquireServiceToken [AdminWebService]: acquiring service token.  

[22:31:54.530] [ 13] [INFO ] Authenticate-ADAL [Acquiring token]: STS endpoint (HTTPS://LOGIN.WINDOWS.NET/WATKINSMUSEUM.ORG), resource (https://graph.windows.net), userName (@watkinsmuseum.org).  

[22:31:54.530] [ 13] [INFO ] ADAL: 2020-05-09T03:31:54.5300454Z: edbb9092-d958-4cc2-9bc3-fb3b3b7da52c - AdalLoggerBase.cs: ADAL PCL.Desktop with assembly version '5.2.2.0', file version '5.2.2.0' and informational version '5.2.2' is running...  

[22:31:54.530] [ 13] [INFO ] ADAL: 2020-05-09T03:31:54.5300454Z: edbb9092-d958-4cc2-9bc3-fb3b3b7da52c - AdalLoggerBase.cs: === Token Acquisition started:  

CacheType: Microsoft.IdentityModel.Clients.ActiveDirectory.TokenCache (1 items)  

Authentication Target: User  

, Authority Host: login.windows.net  

[22:31:54.530] [ 13] [INFO ] ADAL: 2020-05-09T03:31:54.5300454Z: edbb9092-d958-4cc2-9bc3-fb3b3b7da52c - AdalLoggerBase.cs: An item matching the requested resource was found in the cache  

[22:31:54.530] [ 13] [INFO ] ADAL: 2020-05-09T03:31:54.5300454Z: edbb9092-d958-4cc2-9bc3-fb3b3b7da52c - AdalLoggerBase.cs: 59.9091110616667 minutes left until token in cache expires  

[22:31:54.530] [ 13] [INFO ] ADAL: 2020-05-09T03:31:54.5300454Z: edbb9092-d958-4cc2-9bc3-fb3b3b7da52c - AdalLoggerBase.cs: A matching item (access token or refresh token or both) was found in the cache  

[22:31:54.530] [ 13] [INFO ] ADAL: 2020-05-09T03:31:54.5300454Z: edbb9092-d958-4cc2-9bc3-fb3b3b7da52c - AdalLoggerBase.cs: === Token Acquisition finished successfully. An access token was returned: Expiration Time: 5/9/2020 4:31:49 AM +00:00  

[22:31:54.530] [ 13] [INFO ] Authenticate-ADAL: successfully acquired an access token. TenantId=dd8faa70-8371-4e3f-9c58-e18c5dd70b82, ExpiresUTC=5/9/2020 4:31:49 AM +00:00, UserInfo=@watkinsmuseum.org, IdentityProvider=https://sts.windows.net/dd8faa70-8371-4e3f-9c58-e18c5dd70b82/.  

[22:31:55.139] [ 13] [INFO ] GetCompanyConfiguration: tenantId=(dd8faa70-8371-4e3f-9c58-e18c5dd70b82), IsDirSyncing=False, IsPasswordSyncing=False, DomainName=, DirSyncFeatures=0, AllowedFeatures=None.  

[22:31:55.139] [ 13] [INFO ] AzureTenantPage: AdminWebService returned the company information for tenant dd8faa70-8371-4e3f-9c58-e18c5dd70b82.  

[22:31:55.139] [ 13] [INFO ] MicrosoftOnlinePersistedStateProvider.Save: saving the persisted state file  

[22:31:55.139] [ 13] [INFO ] MicrosoftOnlinePersistedStateProv

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-05-11*

Hi,  

By default in Windows Server 2016, passwords must meet the following minimum requirements:  

-  Passwords must not contain the user's account name or parts of the user's full name that exceed two consecutive characters.  

-  Passwords must be at least seven characters in length.  

-  Passwords must contain characters from three of the following four categories:  

a. English uppercase characters (A through Z)  

b. English lowercase characters (a through z)  

c. Base 10 digits (0 through 9)  

d. Non-alphabetic characters (for example, !, $, #, %)  

So, select an appropriate password that meets above requirements. Another option is to change the default policy and use the password that matches the new policy
