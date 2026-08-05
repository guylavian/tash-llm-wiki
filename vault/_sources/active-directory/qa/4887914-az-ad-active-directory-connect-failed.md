---
title: "AZ AD ACTIVE DIRECTORY CONNECT FAILED"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4887914/az-ad-active-directory-connect-failed
question_id: 4887914
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 4
qa_tags: []
---
# AZ AD ACTIVE DIRECTORY CONNECT FAILED

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4887914/az-ad-active-directory-connect-failed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am needing assistance in trying to figure out why AZ fails to connect to sync my users to office 365...Log below

[06:45:30.753] [  1] [INFO ]   

[06:45:30.768] [  1] [INFO ] ================================================================================  

[06:45:30.768] [  1] [INFO ] Application starting  

[06:45:30.768] [  1] [INFO ] ================================================================================  

[06:45:30.784] [  1] [INFO ] Application Version: 1.0.0.0-1446499270  

[06:45:31.486] [  1] [INFO ] App Properties/Metrics:  

[06:45:31.486] [  1] [INFO ]    Runtime.Start=2015-11-12T06:45:30-08:00  

[06:45:31.486] [  1] [INFO ]    Application.Version=1.0.0.0-1446499270  

[06:45:31.486] [  1] [INFO ]    Application.IsDebugBuild=False  

[06:45:31.486] [  1] [INFO ]    Environment.OperatingSystem.VersionString=Microsoft Windows NT 6.0.6002 Service Pack 2  

[06:45:31.486] [  1] [INFO ]    Environment.OperatingSystem.Platform=Win32NT  

[06:45:31.486] [  1] [INFO ]    Environment.OperatingSystem.ServicePack=Service Pack 2  

[06:45:31.486] [  1] [INFO ]    Environment.OperatingSystem.ProductType=DomainController  

[06:45:31.486] [  1] [INFO ]    Environment.OperatingSystem.Sku=7  

[06:45:31.486] [  1] [INFO ]    Environment.OperatingSystem.Language=0409  

[06:45:31.486] [  1] [INFO ]    Environment.Computer.Make=dell inc.  

[06:45:31.486] [  1] [INFO ]    Environment.Computer.Model=precision workstation t7400 

[06:45:31.486] [  1] [INFO ]    Environment.OperatingSystem.IsDomainJoined=True  

[06:45:31.486] [  1] [INFO ]    Runtime.EncodedPageNavigationBytes=  

[06:45:31.486] [ 11] [INFO ] Starting Telemetry Send  

[06:45:31.533] [  1] [INFO ] Acquired sync config changes mutex: True  

[06:45:31.564] [  1] [INFO ] RootPageViewModel.GetInitialPages: Beginning detection for creating initial pages.  

[06:45:31.611] [  1] [WARN ] Password sync is not supported on this install. The current operating system version is 6.0.6002, while the requirement is 6.1.7601.  

[06:45:31.626] [  1] [INFO ] DetectInstalledComponents stage: Checking install context.  

[06:45:31.626] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Online Services Sign-In Assistant for IT Professionals  

[06:45:31.626] [  1] [VERB ] Getting list of installed packages by upgrade code  

[06:45:31.642] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {03c97135-0e31-4334-9215-63827d4f07d4}: verified product code {d8ab93b0-6fbf-44a0-971f-c0669b5ae6dd}.  

[06:45:31.642] [  1] [VERB ] Package=Microsoft Online Services Sign-in Assistant, Version=7.250.4556.0, ProductCode=d8ab93b0-6fbf-44a0-971f-c0669b5ae6dd, UpgradeCode=03c97135-0e31-4334-9215-63827d4f07d4  

[06:45:31.657] [  1] [INFO ] Determining installation action for Microsoft Online Services Sign-In Assistant for IT Professionals (03c97135-0e31-4334-9215-63827d4f07d4)  

[06:45:31.657] [  1] [INFO ] Product Microsoft Online Services Sign-In Assistant for IT Professionals (version 7.250.4556.0) is installed.  

[06:45:31.657] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Azure Active Directory Module for Windows PowerShell  

[06:45:31.657] [  1] [VERB ] Getting list of installed packages by upgrade code  

[06:45:31.657] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {bbf5d0bf-d8ae-4e66-91ab-b7023c1f288c}: verified product code {43cc9c53-a217-4850-b5b2-8c347920e500}.  

[06:45:31.657] [  1] [VERB ] Package=Windows Azure Active Directory Module for Windows PowerShell, Version=1.0.0, ProductCode=43cc9c53-a217-4850-b5b2-8c347920e500, UpgradeCode=bbf5d0bf-d8ae-4e66-91ab-b7023c1f288c  

[06:45:31.657] [  1] [INFO ] Determining installation action for Microsoft Azure Active Directory Module for Windows PowerShell (bbf5d0bf-d8ae-4e66-91ab-b7023c1f288c)  

[06:45:31.657] [  1] [INFO ] Product Microsoft Azure Active Directory Module for Windows PowerShell (version 1.0.0) is installed.  

[06:45:31.657] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Visual C++ 2013 Redistributable Package  

[06:45:31.657] [  1] [VERB ] Getting list of installed packages by upgrade code  

[06:45:31.657] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {20400cf0-de7c-327e-9ae4-f0f38d9085f8}: verified product code {a749d8e6-b613-3be3-8f5f-045c84eba29b}.  

[06:45:31.657] [  1] [VERB ] Package=Microsoft Visual C++ 2013 x64 Minimum Runtime - 12.0.21005, Version=12.0.21005, ProductCode=a749d8e6-b613-3be3-8f5f-045c84eba29b, UpgradeCode=20400cf0-de7c-327e-9ae4-f0f38d9085f8  

[06:45:31.657] [  1] [INFO ] Determining installation action for Microsoft Visual C++ 2013 Redistributable Package (20400cf0-de7c-327e-9ae4-f0f38d9085f8)  

[06:45:31.657] [  1] [INFO ] Product Microsoft Visual C++ 2013 Redistributable Package (version 12.0.21005) is installed.  

[06:45:31.657] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Directory Sync Tool  

[06:45:31.657] [  1] [VERB ] Getting list of installed packages by upgrade code  

[06:45:31.657] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {bef7e7d9-2ac2-44b9-abfc-3335222b92a7}: no registered products found.  

[06:45:31.657] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {dc9e604e-37b0-4efc-b429-21721cf49d0d}: no registered products found.  

[06:45:31.657] [  1] [INFO ] Determining installation action for Microsoft Directory Sync Tool UpgradeCodes {bef7e7d9-2ac2-44b9-abfc-3335222b92a7}, {dc9e604e-37b0-4efc-b429-21721cf49d0d}  

[06:45:31.657] [  1] [INFO ] DirectorySyncComponent: Product Microsoft Directory Sync Tool is not installed.  

[06:45:31.657] [  1] [INFO ] Performing direct lookup of upgrade codes for: Azure AD Sync Engine  

[06:45:31.657] [  1] [VERB ] Getting list of installed packages by upgrade code  

[06:45:31.657] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {545334d7-13cd-4bab-8da1-2775fa8cf7c2}: verified product code {7b21e0d0-f190-4f2f-b15d-277eb215d68a}.  

[06:45:31.673] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {dc9e604e-37b0-4efc-b429-21721cf49d0d}: no registered products found.  

[06:45:31.673] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {bef7e7d9-2ac2-44b9-abfc-3335222b92a7}: no registered products found.  

[06:45:31.673] [  1] [VERB ] Package=Microsoft Azure AD Connect synchronization services, Version=1.0.9125.0, ProductCode=7b21e0d0-f190-4f2f-b15d-277eb215d68a, UpgradeCode=545334d7-13cd-4bab-8da1-2775fa8cf7c2  

[06:45:31.673] [  1] [INFO ] Determining installation action for Azure AD Sync Engine (545334d7-13cd-4bab-8da1-2775fa8cf7c2)  

[06:45:31.845] [  1] [INFO ] Product Azure AD Sync Engine (version 1.0.9125.0) is installed.  

[06:45:32.001] [  1] [ERROR] AzureADSyncEngineComponent: unexpected value retrieved for upgrade mode (0)  

[06:45:32.001] [  1] [INFO ] Performing direct lookup of upgrade codes for: Azure AD Sync Engine Health Agent  

[06:45:32.001] [  1] [VERB ] Getting list of installed packages by upgrade code  

[06:45:32.001] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {114fb294-8aa6-43db-9e5c-4ede5e32886f}: no registered products found.  

[06:45:32.001] [  1] [INFO ] Determining installation action for Azure AD Sync Engine Health Agent (114fb294-8aa6-43db-9e5c-4ede5e32886f)  

[06:45:32.001] [  1] [INFO ] Product Azure AD Sync Engine Health Agent is not installed.  

[06:45:32.001] [  1] [INFO ] Performing direct lookup of upgrade codes for: Azure AD Connect agent  

[06:45:32.001] [  1] [VERB ] Getting list of installed packages by upgrade code  

[06:45:32.001] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {781f8332-277b-45bf-a5f4-af5a117ffa73}: no registered products found.  

[06:45:32.001] [  1] [INFO ] Determining installation action for Azure AD Connect agent (781f8332-277b-45bf-a5f4-af5a117ffa73)  

[06:45:32.001] [  1] [INFO ] Product Azure AD Connect agent is not installed.  

[06:45:32.001] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft SQL Server 2012 Command Line Utilities  

[06:45:32.001] [  1] [VERB ] Getting list of installed packages by upgrade code  

[06:45:32.001] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {52446750-c08e-49ef-8c2e-1e0662791e7b}: verified product code {9d573e71-1077-4c7e-b4db-4e22a5d2b48b}.  

[06:45:32.001] [  1] [VERB ] Package=Microsoft SQL Server 2012 Command Line Utilities , Version=11.0.2100.60, ProductCode=9d573e71-1077-4c7e-b4db-4e22a5d2b48b, UpgradeCode=52446750-c08e-49ef-8c2e-1e0662791e7b  

[06:45:32.001] [  1] [INFO ] Determining installation action for Microsoft SQL Server 2012 Command Line Utilities (52446750-c08e-49ef-8c2e-1e0662791e7b)  

[06:45:32.001] [  1] [INFO ] Product Microsoft SQL Server 2012 Command Line Utilities (version 11.0.2100.60) is installed.  

[06:45:32.001] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft SQL Server 2012 Express LocalDB  

[06:45:32.001] [  1] [VERB ] Getting list of installed packages by upgrade code  

[06:45:32.001] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {c3593f78-0f11-4d8d-8d82-55460308e261}: verified product code {6c026a91-640f-4a23-8b68-05d589cc6f18}.  

[06:45:32.001] [  1] [VERB ] Package=Microsoft SQL Server 2012 Express LocalDB , Version=11.1.3000.0, ProductCode=6c026a91-640f-4a23-8b68-05d589cc6f18, UpgradeCode=c3593f78-0f11-4d8d-8d82-55460308e261  

[06:45:32.001] [  1] [INFO ] Determining installation action for Microsoft SQL Server 2012 Express LocalDB (c3593f78-0f11-4d8d-8d82-55460308e261)  

[06:45:32.001] [  1] [INFO ] Product Microsoft SQL Server 2012 Express LocalDB (version 11.1.3000.0) is installed.  

[06:45:32.001] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft SQL Server 2012 Native Client  

[06:45:32.001] [  1] [VERB ] Getting list of installed packages by upgrade code  

[06:45:32.001] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {1d2d1fa0-e158-4798-98c6-a296f55414f9}: verified product code {49d665a2-4c2a-476e-9ab8-fcc425f526fc}.  

[06:45:32.001] [  1] [VERB ] Package=Microsoft SQL Server 2012 Native Client , Version=11.0.2100.60, ProductCode=49d665a2-4c2a-476e-9ab8-fcc425f526fc, UpgradeCode=1d2d1fa0-e158-4798-98c6-a296f55414f9  

[06:45:32.001] [  1] [INFO ] Determining installation action for Microsoft SQL Server 2012 Native Client (1d2d1fa0-e158-4798-98c6-a296f55414f9)  

[06:45:32.001] [  1] [INFO ] Product Microsoft SQL Server 2012 Native Client (version 11.0.2100.60) is installed.  

[06:45:32.001] [  1] [INFO ] Performing direct lookup of upgrade codes for: Microsoft Azure AD Connect Azure AD Connector  

[06:45:32.001] [  1] [VERB ] Getting list of installed packages by upgrade code  

[06:45:32.001] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {fb3feca7-5190-43e7-8d4b-5eec88ed9455}: verified product code {706efae8-26a7-4e27-bbd0-2c3c1d7c194d}.  

[06:45:32.001] [  1] [VERB ] Package=Microsoft Azure AD Connect Azure AD Connector, Version=1.0.9125.0, ProductCode=706efae8-26a7-4e27-bbd0-2c3c1d7c194d, UpgradeCode=fb3feca7-5190-43e7-8d4b-5eec88ed9455  

[06:45:32.001] [  1] [INFO ] Determining installation action for Microsoft Azure AD Connect Azure AD Connector (fb3feca7-5190-43e7-8d4b-5eec88ed9455)  

[06:45:32.001] [  1] [INFO ] Product Microsoft Azure AD Connect Azure AD Connector (version 1.0.9125.0) is installed.  

[06:45:32.001] [  1] [INFO ] Determining installation action for Microsoft Azure AD Connection Tool.  

[06:45:32.172] [  1] [WARN ] Failed to read DisplayName registry key: An error occurred while executing the 'Get-ItemProperty' command. Cannot find path 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\MicrosoftAzureADConnectionTool'
 because it does not exist.  

[06:45:32.172] [  1] [INFO ] Product Microsoft Azure AD Connection Tool is not installed.  

[06:45:32.172] [  1] [INFO ] Performing direct lookup of upgrade codes for: Azure Active Directory Connect  

[06:45:32.172] [  1] [VERB ] Getting list of installed packages by upgrade code  

[06:45:32.172] [  1] [INFO ] GetInstalledPackagesByUpgradeCode {d61eb959-f2d1-4170-be64-4dc367f451ea}: verified product code {b8c6506c-843a-4e91-9a91-975260716ac1}.  

[06:45:32.172] [  1] [VERB ] Package=Microsoft Azure AD Connect, Version=1.0.9125.0, ProductCode=b8c6506c-843a-4e91-9a91-975260716ac1, UpgradeCode=d61eb959-f2d1-4170-be64-4dc367f451ea  

[06:45:32.172] [  1] [INFO ] Determining installation action for Azure Active Directory Connect (d61eb959-f2d1-4170-be64-4dc367f451ea)  

[06:45:32.172] [  1] [INFO ] Product Azure Active Directory Connect (version 1.0.9125.0) is installed.  

[06:45:32.172] [  1] [INFO ] DetectInstalledComponents stage: Sync engine is already installed and meets version requirement.  

[06:45:32.172] [  1] [INFO ] DetectInstalledComponents: Marking Sync Engine as successfully installed.  

[06:45:32.203] [  1] [INFO ] Checking for DirSync conditions.  

[06:45:32.203] [  1] [INFO ] DirSync not detected. Checking for AADSync/AADConnect upgrade conditions.  

[06:45:32.203] [  1] [INFO ] Sync engine is already installed. Checking for additonal conditions.  

[06:45:32.203] [  1] [INFO ] Sync engine is present. Performing clean install.  

[06:45:32.375] [  1] [INFO ] Starting a background thread in User sign-in. Background Task Id: 1.  

[06:45:32.375] [ 10] [WARN ] Password sync is not supported on this install. The current operating system version is 6.0.6002, while the requirement is 6.1.7601.  

[06:45:32.798] [  1] [INFO ] Property TargetServers failed validation with error At least one server must be specified.  

[06:45:32.798] [  1] [INFO ] Property TargetServerList failed validation with error One or more errors exist.  

[06:45:32.798] [  1] [INFO ] Property ExistingServerName failed validation with error A server name must be provided.  

[06:45:32.970] [  1] [INFO ] Property TargetServers failed validation with error At least one server must be specified.  

[06:45:32.970] [  1] [INFO ] Property TargetServerList failed validation with error One or more errors exist.  

[06:45:32.970] [  1] [INFO ] Property ExistingServerName failed validation with error A server name must be provided.  

[06:45:35.372] [  1] [INFO ] Starting a background thread in User sign-in. Background Task Id: 2.  

[06:45:35.372] [  1] [INFO ] Page transition from "User Sign-In" [SelectSignInPageViewModel] to "Connect to Azure AD" [AzureTenantPageViewModel]  

[06:45:35.528] [  1] [WARN ] Failed to read IAzureActiveDirectoryContext.AzureADUsername registry key: An error occurred while executing the 'Get-ItemProperty' command. Property IAzureActiveDirectoryContext.AzureADUsername does not exist at path HKEY_CURRENT_USER\SOFTWARE\Microsoft\Azure
 AD Connect.  

[06:45:35.544] [  1] [INFO ] Property Username failed validation with error The Microsoft Azure account name cannot be empty.  

[06:46:16.013] [  1] [INFO ] Property Password failed validation with error A Microsoft Azure password is required.  

[06:46:22.578] [ 13] [INFO ] AzureTenantPage: Beginning Windows Azure tenant credentials validation.  

[06:46:22.774] [ 13] [INFO ] DiscoverAdalEndpoints: authority=login.windows.net/rembrandtfruit.onmicrosoft.com, awsServiceResource=https://graph.windows.net.  

[06:46:23.023] [ 13] [WARN ] Failed to read AdalEnabled registry key: An error occurred while executing the 'Get-ItemProperty' command. Property AdalEnabled does not exist at path HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Azure AD Connect.  

[06:46:23.023] [ 13] [INFO ] Authenticate: SIA authentication is enabled.  

[06:46:23.023] [ 13] [INFO ] Authenticate-SIA: authenticating credentials and retrieving company configuration  

[06:46:23.928] [ 13] [INFO ] Authenticate: tenantId=(1deb59ba-06f6-477c-9eec-fb8cb3c9df74), IsDirSyncing=False, IsPasswordSyncing=False, DomainName=, DirSyncFeatures=0, AllowedFeatures=None.  

[06:46:24.146] [ 13] [WARN ] Failed to read AdalEnabled registry key: An error occurred while executing the 'Get-ItemProperty' command. Property AdalEnabled does not exist at path HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Azure AD Connect.  

[06:46:24.146] [ 13] [INFO ] AzureTenantPage: connecting to AAD PowerShell using admin credentials.  

[06:46:25.878] [ 13] [INFO ] AzureTenantPage: successfully connected to Azure via AAD PowerShell.  

[06:46:26.424] [ 13] [INFO ] AzureTenantPage: Successfully retrieved company information for tenant 1deb59ba-06f6-477c-9eec-fb8cb3c9df74.  

[06:46:26.440] [ 13] [INFO ] AzureTenantPage: DirectorySynchronizationEnabled=False  

[06:46:26.440] [ 13] [INFO ] AzureTenantPage: DirectorySynchronizationStatus=Disabled  

[06:46:26.440] [ 13] [INFO ] PowershellHelper: lastDirectorySyncTime=null  

[06:46:26.658] [ 13] [INFO ] AzureTenantPage: Successfully retrieved 3 domains from the tenant.  

[06:46:26.658] [ 24] [ERROR] A terminating unhandled exception occurred.  

Exception Data (Raw): System.AggregateException: One or more errors occurred. ---> System.ArgumentNullException: Value cannot be null.  

Parameter name: state  

   at Microsoft.Online.Deployment.Types.PersistedState.MicrosoftOnlinePersistedStateProvider.SetStateElementInternal(PersistedStateElement element, PersistedStateContainer state)  

   at Microsoft.Online.Deployment.Types.PersistedState.MicrosoftOnlinePersistedStateProvider.SetStateElement(PersistedStateElement element)  

   at Microsoft.Online.Deployment.OneADWizard.UI.WizardPages.AzureTenantPageViewModel.ValidateCredentials()  

   at System.Threading.Tasks.Task.Execute()  

   --- End of inner exception stack trace ---  

---> (Inner Exception #0) System.ArgumentNullException: Value cannot be null.  

Parameter name: state  

   at Microsoft.Online.Deployment.Types.PersistedState.MicrosoftOnlinePersistedStateProvider.SetStateElementInternal(PersistedStateElement element, PersistedStateContainer state)  

   at Microsoft.Online.Deployment.Types.PersistedState.MicrosoftOnlinePersistedStateProvider.SetStateElement(PersistedStateElement element)  

   at Microsoft.Online.Deployment.OneADWizard.UI.WizardPages.AzureTenantPageViewModel.ValidateCredentials()  

   at System.Threading.Tasks.Task.Execute()<---

[06:46:26.689] [ 23] [INFO ] Starting Telemetry Send  

[06:46:26.689] [  1] [INFO ] Page transition from "Connect to Azure AD" [AzureTenantPageViewModel] to "Error" [ErrorPageViewModel]  

[09:06:16.369] [  1] [INFO ] Opened log file at path C:\Users\root\AppData\Local\AADConnect\trace-20151112-064530.log

## Answer (community) — community member

*upvotes: 0 · updated: 2015-11-18*

Hi EWBrandt,

Please let me know the update on the status of the issue at your earliest convenience.

Thanks,  

Jason Jiang

## Answer (community) — community member

*upvotes: 0 · updated: 2015-11-17*

Hi EWBrandt,  

Thanks for your update.  

Check if the issue could be related to proxy. I suggest you temporarily bypass proxy/firewall to check it (open port 80,443).

Could you please capture the detailed steps you have done and the error message post here?  

If possible, use another Office 365 administrator account to see the result.  

Regards,  

Jason Jiang

## Answer (community) — community member

*upvotes: 0 · updated: 2015-11-16*

Hi Sorry for the late response...I am using Microsoft Azure Active Directory Connect

I receive the message after I enter my office 365 credentials.

I am running this program on windows server 2008 SP2

## Answer (community) — community member

*upvotes: 0 · updated: 2015-11-15*

Hi EWBrandt,

Any updates on your side? Please let us know if you need further assistance.

Thanks,  

Jason Jiang

## Answer (community) — community member

*upvotes: 0 · updated: 2015-11-13*

Hi EWBrandt,  

To help us troubleshoot the issue, I’d like to confirm the following information with you:  

-  Which tool are you using, DirSync, AADsync or AAD connect?  

-  When do you receive this error message?  

Please also give us the detailed local environment you are using.  

Thanks,  

Jason Jiang
