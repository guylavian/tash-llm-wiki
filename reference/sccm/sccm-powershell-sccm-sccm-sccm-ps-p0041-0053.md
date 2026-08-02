---
title: "Overview — pages 41-53"
type: reference
domain: sccm
slug: sccm-powershell-sccm-sccm-sccm-ps-p0041-0053
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/powershell-sccm-sccm-sccm-ps-p0041-0053
family: sccm
documentKind: "doc"
abstract: "This set of new cmdlets is for application deployment type return codes. For more general information, see Deployment type Return Codes. Add-CMDeploymentTypeReturnCode Use this cmdlet to add return codes to a supported deployment type. PowerShell $msi_dt = Get-CMDeploymentType -"
---

# Overview — pages 41-53

<!-- p.41 -->

This set of new cmdlets is for application deployment type return codes. For more
general information, see Deployment type Return Codes.

Add-CMDeploymentTypeReturnCode

Use this cmdlet to add return codes to a supported deployment type.

  PowerShell

  $msi_dt = Get-CMDeploymentType -ApplicationName "CenterApp" -
  DeploymentTypeName "InterDept - Windows Installer (.msi file)"
  Add-CMDeploymentTypeReturnCode -InputObject $msi_dt -ReturnCode 1602 -Name
  "User cancel" -CodeType Failure -Description "The user cancelled the
  installation"

For more information, see Add-CMDeploymentTypeReturnCode.

Get-CMDeploymentTypeReturnCode
Use this cmdlet to get the list of return codes from the specified deployment type.

  PowerShell

  Get-CMDeploymentType -ApplicationName "CenterApp" -DeploymentTypeName
  "InterDept - Windows Installer (.msi file)" | Get-CMDeploymentTypeReturnCode

For more information, see Get-CMDeploymentTypeReturnCode.

Remove-CMDeploymentTypeReturnCode

Use this cmdlet to delete return codes from the specified deployment type.

  PowerShell

  $msi_dt = Get-CMDeploymentType -ApplicationName "CenterApp" -
  DeploymentTypeName "InterDept - Windows Installer (.msi file)"
  Remove-CMDeploymentTypeReturnCode -InputObject $msi_dt -ReturnCode 1602

For more information, see Remove-CMDeploymentTypeReturnCode.

Set-CMDeploymentTypeReturnCode
Use this cmdlet to modify return codes for the specified deployment type.

<!-- p.42 -->

  PowerShell

  $msi_dt = Get-CMDeploymentType -ApplicationName "CenterApp" -
  DeploymentTypeName "InterDept - Windows Installer (.msi file)"
  Add-CMDeploymentTypeReturnCode -InputObject $msi_dt -ReturnCode 3010 -Name
  "Always reboot" -CodeType HardReboot -Description "Change soft reboot to
  hard reboot"

For more information, see Set-CMDeploymentTypeReturnCode.

Other new cmdlets

Get-CMClientSettingDeployment
Use this cmdlet to get a deployment of a custom client settings object. You can use this
object with Remove-CMClientSettingDeployment.

For more information on client settings, see How to configure client settings.

  PowerShell

  $clientSetting = Get-CMClientSetting -Name "Software Center customizations"
  $clientSetting | Get-CMClientSettingDeployment

For more information, see Get-CMClientSettingDeployment.

Get-CMDeploymentTypeDetectionClause
Use this cmdlet to get the detection clauses from the specified deployment type.

You can use this cmdlet to get a detection clause from one app and apply it to another,
for example:

  PowerShell

  $appMsi = Get-CMDeploymentType -ApplicationName "CenterApp" -
  DeploymentTypeName "InterDept - Windows Installer (.msi file)"

  $clause1 = Get-CMDeploymentTypeDetectionClause -InputObject $appMsi

  Set-CMScriptDeploymentType -ApplicationName "Configuration Manager console"
  -DeploymentTypeName "Install" -AddDetectionClause $clause1

For more information, see Get-CMDeploymentTypeDetectionClause.

<!-- p.43 -->

Get-CMPersistentUserSettingsGroup
Use this cmdlet to get the list of site-wide settings that you've stored. These settings
follow you on different devices.

For example, Configuration Manager console notifications that are active or you've
dismissed.

For more information, see Get-CMPersistentUserSettingsGroup.

Get-CMSoftwareUpdateContentInfo
Use this cmdlet to get software update content information.

  PowerShell

  $update = Get-CMSoftwareUpdate -ArticleId "5004237" -Fast
  Get-CMSoftwareUpdateContentInfo -InputObject $update[1]

For more information, see Get-CMSoftwareUpdateContentInfo.

Remove-CMPersistentUserSettingsGroup
Use this cmdlet to reset your site-wide settings.

For example, you can restore Configuration Manager console notifications that you've
dismissed. After you run this cmdlet, and you restart the Configuration Manager
console, you'll see all available notifications again.

For more information, see Remove-CMPersistentUserSettingsGroup.

Deprecated and removed cmdlets
The following cmdlets to start a deployment are deprecated and may be removed in a
future release:

 Deprecated cmdlet                      Replacement

 Start-                                 New-CMApplicationDeployment with the Simulation
 CMApplicationDeploymentSimulation      parameter

 Start-CMClientSettingDeployment        New-CMClientSettingDeployment

<!-- p.44 -->

 Deprecated cmdlet                    Replacement

 Start-                               New-CMAntimalwarePolicyDeployment
 CMAntimalwarePolicyDeployment

The following cmdlets are no longer available because the underlying features are no
longer supported:

      Add-CMApplicationCatalogWebServicePoint

      Add-CMApplicationCatalogWebsitePoint

      Get-CMApplicationCatalogWebServicePoint

      Get-CMApplicationCatalogWebsitePoint

      Remove-CMApplicationCatalogWebServicePoint

      Remove-CMApplicationCatalogWebsitePoint

      Set-CMApplicationCatalogWebsitePoint

      Get-CMVhd

      New-CMVhd

      Remove-CMVhd

      Set-CMVhd

Cmdlet changes
The following changes have been made to existing cmdlets in this version. Changes may
be new functionality or bug fixes. Some changes may be breaking. If you use one of the
cmdlets or feature areas listed in this section, carefully review the changes to understand
how they may affect your use.

Add-CMDeviceCollectionDirectMembershipRule
For more information, see Add-CMDeviceCollectionDirectMembershipRule.

Bugs that were fixed

Fixed an issue when trying to add thousands of devices as direct membership rules.

<!-- p.45 -->

Add-CMDistributionPoint
For more information, see Add-CMDistributionPoint.

Breaking changes

The default minimum free space changed from 50 MB to 500 MB.

Add-CMTaskSequenceStep
For more information, see Add-CMTaskSequenceStep.

Non-breaking changes

Removed unnecessary parameter StepName.

Disconnect-CMTrackedObject
For more information, see Disconnect-CMTrackedObject.

Non-breaking changes

Added alias Disconnect-CMObject for this cmdlet.

Get-CMApplicationGroup
For more information, see Get-CMApplicationGroup.

Bugs that were fixed

Fixed an issue to get the correct app group path.

Get-CMDeploymentStatusDetails
For more information, see Get-CMDeploymentStatusDetails.

Bugs that were fixed

Fixed query condition to avoid potential type mismatch issue.

Import-CMAntimalwarePolicy
For more information, see Import-CMAntimalwarePolicy.

<!-- p.46 -->

Non-breaking changes

Added support for audit mode policy with potentially unwanted applications. For more
information, see Audit mode for potentially unwanted applications.

Import-CMQuery
For more information, see Import-CMQuery.

Bugs that were fixed

Fixed an issue to unblock the import function.

New-CMAdministrativeUser
For more information, see New-CMAdministrativeUser.

Bugs that were fixed

Fixed an issue when the user name is me .

New-CMApplicationDeployment
For more information, see New-CMApplicationDeployment.

Non-breaking changes

Added the AutoCloseExecutable parameter to enable the application deployment
setting for install behaviors.

New-CMCloudManagementGateway
For more information, see New-CMCloudManagementGateway.

Breaking changes

The ServiceCertPassword parameter is now required.

New-CMMigrationJob
For more information, see New-CMMigrationJob.

Bugs that were fixed

<!-- p.47 -->

Unblocked the migration of software distribution deployment objects.

New-CMSecondarySite
For more information, see New-CMSecondarySite.

Breaking changes

Changed the default minimum free space from 200 MB to 500 MB.

New-CMSoftwareUpdateAutoDeploymentRule
For more information, see New-CMSoftwareUpdateAutoDeploymentRule.

Bugs that were fixed

Fixed an issue with the Product parameter. When there are multiple products with the
same name, it now selects all of them.

New-CMSoftwareUpdateDeployment
For more information, see New-CMSoftwareUpdateDeployment.

Non-breaking changes

Added Description alias to Comment parameter.

New-CMTaskSequence
For more information, see New-CMTaskSequence.

Non-breaking changes

     Extended the maximum length of the Description parameter to 512 characters.

     Added new parameter HighPerformance to support performance setting.

     The legacy InstallationLicensingMode parameter was removed.

     Removed the NewInstallOSImageVhd parameter set.

     Removed the InstallOperatingSystemImageVhd parameter.

New-CMTaskSequenceDeployment

<!-- p.48 -->

For more information, see New-CMTaskSequenceDeployment.

Bugs that were fixed

Fixed an issue with high-performance power plans.

New-CMTSStepApplyDriverPackage
For more information, see New-CMTSStepApplyDriverPackage.

Non-breaking changes

Added a condition to validate a package for the specified PackageId.

New-CMTSStepApplyOperatingSystem
For more information, see New-CMTSStepApplyOperatingSystem.

Bugs that were fixed

Fixed validation issues with the DestinationVariable parameter to allow values that start
with an underscore ( _ ).

Non-breaking changes

Added the LayeredDriver parameter to support layered keyboard driver during OS
deployment.

New-CMTSStepUpgradeOperatingSystem
For more information, see New-CMTSStepUpgradeOperatingSystem.

Non-breaking changes

Added new parameter SoftwareUpdate to specify a feature update for the Upgrade OS
task sequence step.

Publish-CMPrestageContent
For more information, see Publish-CMPrestageContent.

Bugs that were fixed

Fixed potential invalid object issue.

<!-- p.49 -->

Remove-CMApplicationGroup
For more information, see Remove-CMApplicationGroup.

Bugs that were fixed

Fixed an issue to get the correct app group path when using the pipeline.

Set-CMAntimalwarePolicy
For more information, see Set-CMAntimalwarePolicy.

Non-breaking changes

Added the parameter PuaProtection to support potentially unwanted applications.

Set-CMApplicationDeployment
For more information, see Set-CMApplicationDeployment.

Non-breaking changes

Added the AutoCloseExecutable parameter to enable the application deployment
setting for install behaviors.

Set-CMClientSetting
For more information, see Set-CMClientSetting.

Non-breaking changes

Added a meaningful deprecation message for the SoftwareMetering parameter.

Set-CMClientSettingSoftwareUpdate
For more information, see Set-CMClientSettingSoftwareUpdate.

Non-breaking changes

Added the parameter EnableWsusCertPinning to support certificate pinning.

Set-CMDeploymentType
For more information, see Set-CMDeploymentType.

<!-- p.50 -->

Bugs that were fixed

Fixed an issue with the AddRequirement parameter to add new rules.

Set-CMMsiDeploymentType
For more information, see Set-CMMsiDeploymentType.

Bugs that were fixed

Update the deployment type according to the installer type to avoid resetting the
configurations when you change the content location.

Non-breaking changes

Add support for specifying a folder path to the ContentLocation parameter.

Set-CMTaskSequence
For more information, see Set-CMTaskSequence.

Non-breaking changes

Added new parameter HighPerformance to support performance setting for task
sequence.

Set-CMTSStepApplyDriverPackage
For more information, see Set-CMTSStepApplyDriverPackage.

Non-breaking changes

Added a condition to validate a package for the specified PackageId.

Set-CMTSStepApplyOperatingSystem
For more information, see Set-CMTSStepApplyOperatingSystem.

Bugs that were fixed

Fixed an issue with the Destination parameter.

Non-breaking changes

<!-- p.51 -->

Added the LayeredDriver parameter to support layered keyboard driver during OS
deployment.

Set-CMTSStepUpgradeOperatingSystem
For more information, see Set-CMTSStepUpgradeOperatingSystem.

Non-breaking changes

Added new parameter SoftwareUpdate to specify a feature update for the Upgrade OS
task sequence step.

Start-CMDistributionPointUpgrade
For more information, see Start-CMDistributionPointUpgrade.

Breaking changes

Set the default minimum free space to 500 MB.

Update-CMDistributionPoint
For more information, see Update-CMDistributionPoint.

Bugs that were fixed

Fixed an issue to update content from both install and uninstall folders when they're
different.

How to provide feedback or report issues
Many of the fixes and improvements described in this article are a result of your
feedback.

To send feedback, use the Configuration Manager console. For more information, see
Feedback for PowerShell.

<!-- p.52 -->

Configuration Manager cmdlet library
privacy statement
Article • 10/03/2022

This privacy statement covers the features for the Configuration Manager PowerShell
cmdlet library.

Usage data
The Configuration Manager PowerShell cmdlet library lets you manage a Configuration
Manager hierarchy by using Windows PowerShell cmdlets and scripts. The cmdlet library
collects information about how you use the cmdlets in the library to identify trends and
usage patterns. The cmdlet library also collects the types and numbers of errors that you
receive when you use the cmdlets.

Information collected, processed, or
transmitted
The collected usage data includes starting, stopping, and terminating of cmdlets,
running of deprecated cmdlets, and activity metrics for SMS Provider operations that are
related to the cmdlets. This information isn't personally identifiable. Collected error
information includes errors that cmdlets return and error details for exception errors.
Some error detail reports might inadvertently include individual identifiers, like a serial
number for a device that is connected to your computer. The cmdlet library filters and
anonymizes information that's in the error reports to remove individual identifiers
before transmission to Microsoft.

Use of information
Microsoft uses this information to improve the quality, security, and integrity of the
products and services they offer.

Choice and control
The Configuration Manager cmdlet library enables this usage data feature by default.
There are two registry keys that control this functionality.

<!-- p.53 -->

To fully opt out, set the CeipLevel entry to 0 in the following two registry keys. They're
for each of the Event Tracing for Windows (ETW) providers:

     HKLM\Software\Microsoft\ConfigMgr10\PowerShell\Microsoft.ConfigurationManageme

     nt.PowerShell.Provider : opts out of usage data for the drive provider

     HKLM\Software\Microsoft\ConfigMgr10\PowerShell\Microsoft.ConfigurationManageme

     nt.PowerShell.Cmdlets : opts out of usage data for the cmdlets

Changes to the usage data settings are specific to the local computer.
