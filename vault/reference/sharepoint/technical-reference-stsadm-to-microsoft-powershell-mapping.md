---
title: "Stsadm to Microsoft PowerShell mapping in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-stsadm-to-microsoft-powershell-mapping
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/stsadm-to-microsoft-powershell-mapping
family: technical-reference
documentKind: "reference"
abstract: "Lists Stsadm operations and their equivalent PowerShell cmdlets."
---

# Stsadm to Microsoft PowerShell mapping in SharePoint Server - SharePoint Server

Note

Stsadm to Microsoft PowerShell mapping in SharePoint Server

# Stsadm to Microsoft PowerShell mapping in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Where there's no one-to-one mapping between the Stsadm operations and PowerShell cmdlets, the table lists the specific PowerShell parameters you must use to get similar functionality.

|  |  |
| --- | --- |
| **Stsadm operation** | **Windows PowerShell cmdlet** |
| **Activatefeature** | Enable-SPFeature |
| **Activateformtemplate** | Enable-SPInfoPathFormTemplate |
| **Addalternatedomain** | New-SPAlternateUrl |
| **Addcontentdb** | Mount-SPContentDatabase  New-SPContentDatabase |
| **Addexemptuseragent** | Add-SPInfoPathUserAgent |
| **Addpath** | New-SPManagedPath |
| **Addpermissionpolicy** | None |
| **Addsolution** | Add-SPSolution |
| **Addtemplate** | None |
| **Adduser** | New-SPUser |
| **Addwppack** | Install-SPWebPartPack |
| **Addzoneurl** | New-SPAlternateUrl |
| **Allowuserformwebserviceproxy** | Set-SPInfoPathWebServiceProxy  Use the **AllowForUserForms** and **Identity** parameters. |
| **Allowwebserviceproxy** | Set-SPInfoPathWebServiceProxy  Use the **AllowWebServiceProxy** and **Identity** parameters. |
| **Authentication** | Set-SPWebApplication  Use the **AuthenticationMethod** or **AuthenticationProvider** parameters. |
| **Backup** | Backup-SPConfigurationDatabase  Backup-SPFarm  Backup-SPSite |
| **Backuphistory** | Get-SPBackupHistory |
| **Binddrservice** | None |
| **Blockedfilelist** | None |
| **Canceldeployment** | None |
| **Changepermissionpolicy** | None |
| **Copyappbincontent** | Install-SPApplicationContent |
| **Createadminvs** | New-SPCentralAdministration |
| **Creategroup** | None |
| **Createsite** | New-SPSite |
| **Createsiteinnewdb** | New-SPSite Use the **ContentDatabase** parameter.  New-SPContentDatabase |
| **Createweb** | New-SPWeb |
| **Databaserepair** | Use Get-SPContentDatabaseOrphanedData to detect orphaned data, but note that it doesn't repair orphaned data. |
| **Deactivatefeature** | Disable-SPFeature |
| **Deactivateformtemplate** | Disable-SPInfoPathFormTemplate |
| **Deleteadminvs** | Remove-SPCentralAdministration |
| **Deletealternatedomain** | Remove-SPAlternateUrl |
| **Deleteconfigdb** | Disconnect-SPConfigurationDatabase |
| **Deletecontentdb** | Dismount-SPContentDatabase |
| **Deletegroup** | None |
| **Deletepath** | Remove-SPManagedPath |
| **Deletepermissionpolicy** | None |
| **Deletesite** | Remove-SPSite |
| **Deletesolution** | Remove-SPSolution |
| **Deletetemplate** | None |
| **Deleteuser** | Remove-SPUser |
| **Deleteweb** | Remove-SPWeb |
| **Deletewppack** | Uninstall-SPWebPartPack |
| **Deletezoneurl** | Remove-SPAlternateUrl |
| **Deploysolution** | Install-SPSolution |
| **Deploywppack** | Install-SPWebPartPack |
| **Disablessc** | None |
| **Displaysolution** | Get-SPSolution |
| **Editcontentdeploymentpath** | Set-SPContentDeploymentPath |
| **Email** | Use Set-SPWebApplication with the -SMTPServer parameter set. |
| **Enablessc** | None |
| **Enumallwebs** | Get-SPContentDatabaseOrphanedData |
| **Enumalternatedomains** | Get-SPAlternateURL |
| **Enumcontentdbs** | Get-SPContentDatabase |
| **Enumdataconnectionfiledependants** | Get-SPDataConnectionFileDependent |
| **Enumdataconnectionfiles** | Get-SPDataConnectionFile |
| **Enumdeployments** | None |
| **Enumexemptuseragents** | Get-SPInfoPathUserAgent |
| **Enumformtemplates** | Get-SPInfoPathFormTemplate |
| **Enumgroups** | None |
| **Enumroles** | None |
| **Enumservices** | Get-SPServiceInstance |
| **Enumsites** | Get-SPSiteAdministration (To run this cmdlet, you must be a member of the Farm Administrators group.)   Get-SPSite (To run this cmdlet, you must be a local administrator on the computer where SharePoint Server is installed.) |
| **Enumsolutions** | Get-SPSolution |
| **Enumsubwebs** | Get-SPWeb |
| **Enumtemplates** | Get-SPWebTemplate |
| **Enumusers** | Get-SPUser |
| **Enumwppacks** | Get-SPWebPartPack |
| **Enumzoneurls** | Get-SPAlternateURL |
| **Execadmsvcjobs** | Start-SPAdminJob |
| **Export** | Export-SPWeb |
| **Extendvs** | New-SPWebApplication |
| **Extendvsinwebfarm** | New-SPWebApplicationExtension |
| **Forcedeletelist** | None |
| **Getadminport** | Get-SPWebApplication  Use the following syntax:  `Get-SPWebApplication -IncludeCentralAdministration| ? {$_.IsAdministrationWebApplication -eq $true}` |
| **Getdataconnectionfileproperty** property | Get-SPDataConnectionFile  Use the following syntax:   `Get-SPDataConnectionFile| where {$_.Name -eq "dataConFileName"}| format-list` |
| **Getformtemplateproperty** property | Get-SPInfoPathFormTemplate  Use the following syntax:   `Get-SPInfoPathFormTemplate| where {$_.DisplayName -eq "formTemplateName"}| format-list` |
| **Getosearchsetting** | None |
| **Getproperty** | Get-SPFarmConfig  Get-SPTimerJob  Disable-SPTimerJob  Enable-SPTimerJob  Set-SPTimerJob  Start-SPTimerJob |
| **Getsitelock** | Get-SPSiteAdministration |
| **Getsiteuseraccountdirectorypath** | Use Get-SPSite to get the site object, then output the UserAccountDirectoryPath property. |
| **Geturlzone** | Get-SPAlternateURL |
| **Import** | Import-SPWeb |
| **Installfeature** | Install-SPFeature |
| **Listlogginglevels** | Get-SPLogLevel |
| **Listqueryprocessoroptions** | None |
| **Listregisteredsecuritytrimmers** | Get-SPEnterpriseSearchSecurityTrimmer |
| **Localupgradestatus** | None. However, Get-SPPendingUpgradeActions provides similar information. |
| **Managepermissionpolicylevel** | None |
| **Mergecontentdbs** | Move-SPSite |
| **Migrateuser** | Move-SPUser |
| **Osearch** | For the **Osearch** parameters **farmcontactemail**, **farmperformancelevel**, **farmserviceaccount**, and **farmservicepassword**, use the Get-SPEnterpriseSearchService and Set-SPEnterpriseSearchService cmdlets.   For the **Osearch** parameters **start** and **stop**, use the Start-SPEnterpriseSearchServiceInstance and Stop-SPEnterpriseSearchServiceInstance cmdlets, respectively.   For the **Osearch** parameter **defaultindexlocation**, use the Get-SPEnterpriseSearchServiceInstance cmdlet. |
| **Osearchdiacriticsensitive** | Use the Get-SPEnterpriseSearchServiceApplication cmdlet to retrieve the specific Search service application, and then use **DiacriticSensitive** parameter from the Set-SPEnterpriseSearchServiceApplication cmdlet. |
| **Profilechangelog** | None.   However, you can use the Stsadm **profilechangelog** operation if you replace the Shared Services Provider (SSP) name with the service application (SA) name:   `stsadm -o profilechangelog-title <SA name>-daysofhistory <number of days>-generateanniversaries` |
| **Provisionservice** | Start-SPServiceInstance |
| **Quiescefarm** | None |
| **Quiescefarmstatus** | None |
| **Quiesceformtemplate** | Stop-SPInfoPathFormTemplate |
| **Reconvertallformtemplates** | Update-SPInfoPathFormTemplate |
| **Refreshdms** | None |
| **Refreshsitedms** | None |
| **Registersecuritytrimmer** | New-SPEnterpriseSearchSecurityTrimmer |
| **Registerwsswriter** | None |
| **Removedataconnectionfile** | Uninstall-SPDataConnectionFile |
| **Removedrservice** | None |
| **Removeexemptuseragent** | Remove-SPInfoPathUserAgent |
| **Removeformtemplate** | Uninstall-SPInfoPathFormTemplate |
| **Removesolutiondeploymentlock** | None |
| **Renameserver** | Rename-SPServer |
| **Renamesite** | Set-SPSite  Use the **Url** parameter. |
| **Renameweb** | Set-SPWeb  Use the **RelativeUrl** parameter. |
| **Restore** | Restore-SPFarm  Restore-SPSite |
| **Retractsolution** | Uninstall-SPSolution |
| **Retractwppack** | None |
| **Runcontentdeploymentjob** | Start-SPContentDeploymentJob |
| **Scanforfeatures** | Install-SPFeature  Use the **Scanforfeatures** parameter. |
| **Setadminport** | Set-SPCentralAdministration |
| **Setapppassword** | Set-SPApplicationCredentialKey Remove-SPApplicationCredentialKey |
| **Setconfigdb** | Connect-SPConfigurationDatabase |
| **Setcontentdeploymentjobschedule** | Set-SPContentDeploymentJob |
| **Setdataconnectionfileproperty** | Set-SPDataConnectionFile |
| **Setformtemplateproperty** | Set-SPInfoPathFormTemplate |
| **Setlogginglevel** | Set-SPLogLevel |
| **Setosearchsetting** | None |
| **Setproperty** | Set-SPFarmConfig  Get-SPTimerJob  Disable-SPTimerJob  Enable-SPTimerJob  Set-SPTimerJob  Start-SPTimerJob |
| **Setqueryprocessoroptions** | None |
| **Setsitelock** | Set-SPSiteAdministration  Use the **LockState** parameter. |
| **Setsiteuseraccountdirectorypath** | Set-SPSite Use the **UserAccountDirectoryPath** parameter. |
| **Setworkflowconfig** | Set-SPWorkflowConfig |
| **Siteowner** | Set-SPSiteAdministration |
| **Sync** | Update-SPProfileSync Clear-SPContentDatabaseSyncData Get-SPContentDatabase (with the -DaysSinceLastProfileSync parameter) |
| **Syncsolution** | Install-SPSolution  Use the **Synchronize** parameter. |
| **Unextendvs** | Remove-SPWebApplication |
| **Uninstallfeature** | Uninstall-SPFeature |
| **Unquiescefarm** | None |
| **Unquiesceformtemplate** | Start-SPInfoPathFormTemplate |
| **Unregistersecuritytrimmer** | Remove-SPEnterpriseSearchSecurityTrimmer |
| **Unregisterwsswriter** | None |
| **Updateaccountpassword** | Set-SPManagedAccount |
| **Updatealerttemplates** | None |
| **Updatefarmcredentials** | None |
| **Upgrade** | None |
| **Upgradeformtemplate** | Install-SPInfoPathFormTemplate |
| **Upgradesolution** | Update-SPSolution |
| **Upgradetargetwebapplication** | None |
| **Uploadformtemplate** | Install-SPInfoPathFormTemplate |
| **Userrole** | Get-SPUser  Move-SPUser  New-SPUser  Remove-SPUser  Set-SPUser |
| **Verifyformtemplate** | Test-SPInfoPathFormTemplate |

See also

## See also

Other Resources

#### Other Resources

Index of Microsoft PowerShell cmdlets for SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2024-08-22
