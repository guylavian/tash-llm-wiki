---
title: "Overview — pages 1-40"
type: reference
domain: sccm
slug: sccm-powershell-sccm-sccm-sccm-ps-p0001-0040
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/powershell-sccm-sccm-sccm-ps-p0001-0040
family: sccm
documentKind: "doc"
abstract: "Tell us about your PDF experience. Get started with Configuration Manager cmdlets Article • 07/03/2024 Applies to: Configuration Manager (current branch) Use Windows PowerShell to manage your Configuration Manager hierarchy. You can use PowerShell scripts to automate or extend C"
---

# Overview — pages 1-40

<!-- p.1 -->

                                                            Tell us about your PDF experience.

Get started with Configuration Manager
cmdlets
Article • 07/03/2024

Applies to: Configuration Manager (current branch)

Use Windows PowerShell to manage your Configuration Manager hierarchy. You can use
PowerShell scripts to automate or extend Configuration Manager similar to other
documented approaches using WMI and C#. For more information, see Configuration
Manager SDK.

Run Configuration Manager cmdlets and scripts in PowerShell from the Configuration
Manager console or from a Windows PowerShell session. When you run Configuration
Manager cmdlets by using the Configuration Manager console, your session
automatically runs in the context of the site.

  ７ Note

  All currently supported versions of Configuration Manager current branch support
  Windows PowerShell version 5.1. If you've already installed PowerShell version 7,
  you can still use PowerShell version 5.1. For more information, see Using
  PowerShell 7 side-by-side with Windows PowerShell 5.1.

  The Configuration Manager PowerShell cmdlet library supports PowerShell 7. For
  more information, see Support for PowerShell version 7.

Starting in version 2103, the ConfigurationManager PowerShell module requires
Microsoft .NET version 4.7.2 or later.

PowerShell from the Configuration Manager
console
The easiest method to open PowerShell is directly from the Configuration Manager
console.

   1. Launch the Configuration Manager console. In the upper-left corner, there's a blue
      rectangle. Select the white arrow in the blue rectangle, and choose Connect via
      Windows PowerShell.

<!-- p.2 -->

  2. After Windows PowerShell loads, you'll see a prompt that contains your site code.
     For example, if the site code is "ABC", the prompt looks like: PS ABC:\>

  3. To verify it works, use the Get-CMSite cmdlet. This cmdlet returns information
     about the Configuration Manager site you're currently connected to and any child
     sites. For example, the site server name, installation director, site name, and
     version.

  ７ Note

  When you start PowerShell or the PowerShell ISE from the Configuration Manager
  console, it uses the AllSigned execution policy for the Process scope. If this default
  secure configuration is too much for your environment, there are two options to
  work around it:

       Change the execution policy with a command similar to the following
       example: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
       Import the Configuration Manager PowerShell module.

Import the Configuration Manager PowerShell
module
Connect to Configuration Manager from an existing Windows PowerShell session by
manually loading the Configuration Manager module.

  1. Open a Windows PowerShell session from the Start menu.

  2. Import the Configuration Manager module by using the Import-Module cmdlet.
     Specify the path to the Configuration Manager module, or change to the directory
     that contains the module. By default, the module is at the following path:
     C:\Program Files (x86)\Microsoft Endpoint

     Manager\AdminConsole\bin\ConfigurationManager.psd1

     Starting in version 2111, when you install the Configuration Manager console, the
     path to the module is now added to the system environment variable,
     PSModulePath. For more information, see about_PSModulePath. With this change,
     you can import the module just by its name: Import-Module ConfigurationManager

       ） Important

<!-- p.3 -->

    Make sure you don't import an older version of the module that might exist in
    another folder. After you import the module, use the following commands to
    check the module version and path:

       PowerShell

       (Get-Module -Name ConfigurationManager).Version
       (Get-Module -Name ConfigurationManager).Path

  The following example changes to the module's directory and then imports it:

    PowerShell

    Set-Location 'C:\Program Files (x86)\Microsoft Endpoint
    Manager\AdminConsole\bin'
    Import-Module .\ConfigurationManager.psd1

     Tip

    You can also use the SMS_ADMIN_UI_PATH environment variable. For
    example:

       PowerShell

       Set-Location "$env:SMS_ADMIN_UI_PATH\..\"

    Also, you can use the cd alias to change directories instead of the Set-
    Location cmdlet.

3. If it's the first time importing the Configuration Manager module on this computer,
  you may need to create the site drive. For example:

    PowerShell

    New-PSDrive -Name "ABC" -PSProvider "CMSite" -Root
    "siteserver.contoso.com" -Description "Primary site"

     Tip

<!-- p.4 -->

        When you start PowerShell from the console, it automatically creates the
        PSDrive as a convenience for the currently connected site. If you're in a
        hierarchy, use New-PSDrive to create drives for each site.

   4. To run the Configuration Manager cmdlets, you need to switch the path to the
     Configuration Manager site. In the following example, the site code is ABC :

        PowerShell

        Set-Location ABC:

   5. Confirm that PowerShell properly loaded the Configuration Manager module by
     using the Get-CMSite cmdlet.

Update help
To get the latest information for the Configuration Manager PowerShell module, use the
Update-Help cmdlet. This content is the same as what's published on Microsoft Learn
for the ConfigurationManager module.

  ） Important

  Because of a change in how the updateable content is structured and published
  with the release of version 2103, don't use Update-Help on a version 2010 site.
  Update the site to version 2103 or later, and then update the local help content.

  For more information, see PowerShell version 2103 release notes.

The computer on which you run this cmdlet needs internet access, specifically
pshelpprod.blob.core.windows.net . Then run the following command from an elevated

PowerShell session:

  PowerShell

  Update-Help -Module ConfigurationManager

After you update the Configuration Manager cmdlet help, you can get help about the
cmdlets by using the Get-Help cmdlet. For example:

  PowerShell

<!-- p.5 -->

  Get-Help Get-CMDevice
  Get-Help Get-CMDevice -Examples
  Get-Help Get-CMDevice -Parameter *

For more information, see the following PowerShell blog post: You've got Help!   .

Common parameters
All Configuration Manager cmdlets support the common PowerShell parameters:

     Debug
     ErrorAction
     ErrorVariable
     InformationAction
     InformationVariable
     OutVariable
     OutBuffer
     PipelineVariable
     Verbose
     WarningAction
     WarningVariable

For more information, see about_CommonParameters.

Support for PowerShell version 7
The Configuration Manager PowerShell cmdlet library supports PowerShell version 7. For
more information on PowerShell 7, including directions on how to download and install
it, see Install PowerShell on Windows.

   Tip

  PowerShell 7 runs as pwsh.exe . Earlier versions of PowerShell run as
  powershell.exe .

Cmdlets that don't support PowerShell version 7
The following cmdlets don't support PowerShell 7:

     Import-CMPackage

<!-- p.6 -->

     Import-CMDriverPackage
     Import-CMTaskSequence
     Export-CMPackage
     Export-CMDriverPackage
     Export-CMTaskSequence
     Add-CMReportingServicePoint
     Get-CMReportingServicePoint
     Remove-CMReportingServicePoint
     Set-CMReportingServicePoint

They require the .NET Framework instead of .NET Core that's used with PowerShell
version 7.

Starting in version 2103, if you try to use these cmdlets in a PowerShell version 7
session, they fail with the following error: This cmdlet only supports the ".NET
Framework" runtime.

Known issues with PowerShell version 7
     You can't launch PowerShell 7 directly from the Configuration Manager console.
     Manually start PowerShell 7, and then import the Configuration Manager module.

     Current support is only for the Configuration Manager cmdlets. Other features of
     Configuration Manager that rely on PowerShell may not support version 7. For
     example, Run Scripts, CMPivot, or the Run PowerShell Script task sequence step.

Feedback for PowerShell
If you have feedback on the Configuration Manager PowerShell cmdlets, use the same
options in the Configuration Manager console to send feedback. For more information,
see Product feedback.

When you send a frown, include the following additional information specific to
PowerShell:

     The exact script or command syntax that you used so that Microsoft can try to
     reproduce the issue.

     What behavior you expected compared to the actual behavior.

     The full output when you run it with the Verbose common parameter.

<!-- p.7 -->

     The version and path of the ConfigurationManager module. For example, include
     the output of the following commands:

       PowerShell

        (Get-Module -Name ConfigurationManager).Version
        (Get-Module -Name ConfigurationManager).Path

     If a cmdlet returns an error, use the following command to get exception details:

       PowerShell

        $Error[0].Exception | Format-List * -Force

Preview release notes
The technical preview features article in the core documentation library includes release
notes for PowerShell. For example, see Technical preview version 2202.

Next steps
For more information about what's changed in the most recent release of Configuration
Manager, select the latest Release Notes from the table of contents.

For more information on individual cmdlets, see the Configuration Manager cmdlet
reference.

For more information on learning and getting started with Windows PowerShell, see
PowerShell 101.

<!-- p.8 -->

Configuration Manager cmdlet library
changes for version 2309
Article • 09/20/2023

Applies to: Configuration Manager (current branch)

These release notes summarize changes to the Configuration Manager cmdlet library in
version 2309.

  ７ Note

  Configuration Manager current branch version 2111 is the baseline for these
  changes. For more information, see Configuration Manager cmdlet library
  changes for version 2111.

New cmdlets

New-CMWindows11EditionUpgrade
Use this cmdlet to create a Windows 11 edition upgrade policy. For more information,
see About upgrading windows version in Configuration Manager.

  PowerShell

  New-CMWindows11EditionUpgrade -Name "NewEditionPolicyByKey" -WindowsEdition
  Windows11Enterprise -ProductKey "123ab-cd456-789ef-2j3k4-0ghi1"

Set-UpdateServerApplication
Use this cmdlet to add the missing URL 'http://localhost' to your existing server app. For
more information, see About creating and deploying applications in Configuration
Manager.

  PowerShell

  SET-UpdateServerApplication -TenantId 1E7C0B63-1DAB-4754-8433-AF8F9CFFCF38

<!-- p.9 -->

Cmdlet changes
The following changes have been made to existing cmdlets in this version. Changes may
be new functionality or bug fixes. Some changes may be breaking. If you use one of the
cmdlets or feature areas listed in this section, carefully review the changes to understand
how they may affect your use.

Add-CMDistributionPoint
For more information, see Add-CMDistributionPoint.

Non-breaking changes

Two new parameters have been added to the cmdlet

     InitialMPForLookup: It's required (and requires) when providing -
     PreferredMPEnabled parameter. It expects a string input that represents the
     different lookup MPs separated by the * symbol. MPs are filtered based on the Site
     code of the DP, if the MP's site code is different, an error is thrown.
     PreferredMPEnabled: It's a switch parameter. The presence of the parameter
     indicates that the dynamic MP usage is enabled. PXE has to be enabled on the
     Distribution Point before using this parameter.

Set-CMDistributionPoint
For more information, see Set-CMDistributionPoint.

Non-breaking changes

Two new parameters have been added to the cmdlet

     InitialMPForLookup: This parameter expects a string that represents the different
     lookup MPs separated by the symbol'*'. MPs are filtered out based on the Site
     code of the DP, if the MP's site code is different, an error is thrown.
     PreferredMPEnabled: This parameter is boolean where the $true value for the
     parameter indicates that the dynamic MP usage is enabled. PXE has to be enabled
     on the Distribution Point before using this parameter.

Invoke-CMScript
For more information, see Invoke-CMScript.

Non-breaking changes

<!-- p.10 -->

A new optional parameter, ScheduleTime, has been added to the Invoke-CMScript
cmdlet. It specifies the script runtime(UTC).

  PowerShell

  $ScriptObj = Get-CMScript -ScriptName "test"
  Invoke-CMScript -InputObject $ScriptObj -CollectionId "SMSDM003" -
  ScheduleTime "08/02/2023 07:35:00"

New-CMCloudManagementGateway
For more information, see New-CMCloudManagementGateway.

Non-breaking changes

A new parameter, TenantId, has been added to the New-CMCloudManagementGateway
cmdlet.

How to provide feedback or report issues
Many of the fixes and improvements described in this article are a result of your
feedback.

To send feedback, use the Configuration Manager console. For more information, see
Feedback for PowerShell.

<!-- p.11 -->

Configuration Manager cmdlet library
changes for version 2211
Article • 09/20/2023

Applies to: Configuration Manager (current branch)

These release notes summarize changes to the Configuration Manager cmdlet library in
version 2211.

  ７ Note

  Configuration Manager current branch version 2111 is the baseline for these
  changes. For more information, see Configuration Manager cmdlet library
  changes for version 2111.

New cmdlets
      Get-CMAADTenant: Get an Azure Active Directory (Azure AD) tenant from the site.

      Set-CMCollectionCloudSync: Configure cloud sync features for a collection.

Deprecated and removed cmdlets
The following cmdlets for asset intelligence are deprecated and may be removed in a
future release:

      Add-CMAssetIntelligenceSynchronizationPoint
      Get-CMAssetIntelligenceProxy
      Get-CMAssetIntelligenceSynchronizationPoint
      Remove-CMAssetIntelligenceSynchronizationPoint
      Send-CMAssetIntelligenceCatalogUpdateRequest
      Set-CMAssetIntelligenceSynchronizationPoint
      Sync-CMAssetIntelligenceCatalog

Cmdlet changes
The following changes have been made to existing cmdlets in this version. Changes may
be new functionality or bug fixes. Some changes may be breaking. If you use one of the

<!-- p.12 -->

cmdlets or feature areas listed in this section, carefully review the changes to understand
how they may affect your use.

Add-CMSoftwareUpdatePoint
For more information, see Add-CMSoftwareUpdatePoint.

Non-breaking changes

Added new parameter Wledbat to support LEDBAT configuration for software update
points.

Get-CMDeploymentStatusDetails
For more information, see Get-CMDeploymentStatusDetails.

Bugs that were fixed

Updated the cmdlet to avoid a potential null reference error.

Get-CMDeploymentTypeDetectionClause
For more information, see Get-CMDeploymentTypeDetectionClause.

Non-breaking changes

The cmdlet can now get a detection clause from a script deployment type.

Import-CMApplication
For more information, see Import-CMApplication.

Non-breaking changes

Updated the import logic to align with console. Added new warning messages.

New-CMApplication
For more information, see New-CMApplication.

Non-breaking changes

It can now get an application icon from the specified file.

<!-- p.13 -->

New-CMBoundary
For more information, see New-CMBoundary.

Non-breaking changes

Updated value validation for VPN boundary.

New-CMCoManagementPolicy
For more information, see New-CMCoManagementPolicy.

Non-breaking changes

The cmdlet now supports applicability for Windows 11 on ARM64 devices.

New-CMPackage
For more information, see New-CMPackage.

Non-breaking changes

Added parameter IconLocationFile to use a custom icon from the specified file. For
more information, see Custom icon support for task sequences and packages.

New-CMSoftwareUpdateDeployment
For more information, see New-CMSoftwareUpdateDeployment.

Non-breaking changes

Added parameter PreDownloadUpdateContent to support pre-download for available
software updates.

New-CMTaskSequence
For more information, see New-CMTaskSequence.

Non-breaking changes

Added the IconLocationFile parameter to support specifying an icon for the task
sequence. For more information, see Custom icon support for task sequences and
packages.

<!-- p.14 -->

New-CMTaskSequenceDeployment
For more information, see New-CMTaskSequenceDeployment.

Bugs that were fixed

Fixed an issue with the AllowSharedContent parameter.

Publish-CMThirdPartySoftwareUpdateContent
For more information, see Publish-CMThirdPartySoftwareUpdateContent.

Non-breaking changes

Added the Force parameter to run the command without asking for confirmation.

Set-CMBoundary
For more information, see Set-CMBoundary.

Non-breaking changes

Updated value validation for VPN boundary.

Set-CMPackage
For more information, see Set-CMPackage.

Non-breaking changes

Added parameter IconLocationFile to use a custom icon from the specified file. For
more information, see Custom icon support for task sequences and packages.

Set-CMSoftwareUpdateDeployment
For more information, see Set-CMSoftwareUpdateDeployment.

Non-breaking changes

Added parameter PreDownloadUpdateContent to support pre-download for available
software updates.

Set-CMSoftwareUpdatePoint

<!-- p.15 -->

For more information, see Set-CMSoftwareUpdatePoint.

Non-breaking changes

Added new parameter Wledbat to support LEDBAT configuration for software update
points.

Set-CMSoftwareUpdatePointComponent
For more information, see Set-CMSoftwareUpdatePointComponent.

Non-breaking changes

Added the NonWindowsUpdateMaxRuntimeMins parameter to change the default
maximum run time for non-Windows software updates.

Set-CMTaskSequence
For more information, see Set-CMTaskSequence.

Non-breaking changes

Added the IconLocationFile parameter to support specifying an icon for the task
sequence. For more information, see Custom icon support for task sequences and
packages.

Set-CMTaskSequenceDeployment
For more information, see Set-CMTaskSequenceDeployment.

Bugs that were fixed

Fixed an issue with the AllowSharedContent parameter.

Start-CMTaskSequenceDeployment
For more information, see Start-CMTaskSequenceDeployment.

Bugs that were fixed

Fixed an issue with the AllowSharedContent parameter.

Changes to multiple cmdlets

<!-- p.16 -->

The following folder-related cmdlets now support software update groups and
deployment packages:

     Get-CMFolder
     New-CMFolder
     Remove-CMFolder
     Set-CMFolder
     Move-CMObject
     Add-CMObjectSecurityScope
     Remove-CMObjectSecurityScope

How to provide feedback or report issues
Many of the fixes and improvements described in this article are a result of your
feedback.

To send feedback, use the Configuration Manager console. For more information, see
Feedback for PowerShell.

<!-- p.17 -->

Configuration Manager cmdlet library
changes for version 2207
Article • 08/12/2022

Applies to: Configuration Manager (current branch)

These release notes summarize changes to the Configuration Manager cmdlet library in
version 2207

  ７ Note

  Configuration Manager current branch version 2203 is the baseline for these
  changes. For more information, see Configuration Manager cmdlet library
  changes for version 2203.

New cmdlets

Approve-CMOrchestrationGroupScript
Use this cmdlet to approve an orchestration group script. For more information, see
About orchestration groups in Configuration Manager.

  PowerShell

  $referenceOG = Get-CMOrchestrationGroup -Name $Script:OGName
  $preScript = $referenceOG | Get-CMOrchestrationGroupScript -ScriptType Pre
  $preScript | Approve-CMOrchestrationGroupScript -Comment "Approve"
  Approve-CMOrchestrationGroupScript -ScriptGuid $PreScript.ScriptGuid

Deny-CMOrchestrationGroupScript
Use this cmdlet to deny an orchestration group script. For more information, see About
orchestration groups in Configuration Manager.

  PowerShell

  $referenceOG = Get-CMOrchestrationGroup -Name $Script:OGName
  $preScript = $referenceOG | Get-CMOrchestrationGroupScript -ScriptType Pre
  $preScript | Deny-CMOrchestrationGroupScript -Comment "Deny"

<!-- p.18 -->

  Deny-CMOrchestrationGroupScript -ScriptGuid $PreScript.ScriptGuid -Comment
  "Deny"

Get-CMOrchestrationGroupScript
Use this cmdlet to get a script from the specified orchestration group. For more
information, see About orchestration groups in Configuration Manager.

  PowerShell

  $referenceOG = Get-CMOrchestrationGroup -Name $Script:OGName
  $preScript = $referenceOG | Get-CMOrchestrationGroupScript -ScriptType Pre

Start-CMDPMigration
Use this cmdlet to start migration from source distribution point to destination
distribution point. For more information, see About migration in Configuration Manager.

  PowerShell

  Start-CMDPMigration -SourceDistributionPointName sourceServer.dp -
  DestinationDistributionPointName destinationServer.dp -LockSourceDP 1

Stop-CMDPMigration
Use this cmdlet to stop migration from source distribution point to destination
distribution point. For more information, see About migration in Configuration Manager.

  PowerShell

  Stop-CMDPMigration -SourceDistributionPointName sourceServer.dp -
  DestinationDistributionPointName destinationServer.dp -LockSourceDP 1

Get-CMDPMigrationContentStatus
Use this cmdlet to get the content status of the migration from source distribution point
to destination distribution point. For more information, see About migration in
Configuration Manager.

  PowerShell

<!-- p.19 -->

   Get-CMDPMigrationContentStatus -SourceDistributionPointName sourceServer.dp
   -DestinationDistributionPointName destinationServer.dp

Get-CMDPMigrationStatus
Use this cmdlet to get the status of the migration from source distribution point to
destination distribution point. For more information, see About migration in
Configuration Manager.

   PowerShell

   Get-CMDPMigrationStatus -SourceDistributionPointName sourceServer.dp -
   DestinationDistributionPointName destinationServer.dp

Get-CMTrustedRootCertificationAuthority
Use this cmdlet to get the certificates for trusted root certification authorities from the
site.

   PowerShell

   $ci =Get-CMTrustedRootCertificationAuthority
   $ci =Get-CMTrustedRootCertificationAuthority -ViewDetail

New-CMAADClientApplication
Use this cmdlet to create a client app registration in Azure Active Directory (Azure AD).
When you run this cmdlet, it will prompt you to sign in to your tenant. For more
information on this app registration, see Manually register Azure AD apps for the CMG.

   PowerShell

   $serverApp = New-CMAADServerApplication -AppName $appName
   New-CMAADClientApplication -AppName $name -InputObject $serverApp

New-CMAADServerApplication
Use this cmdlet to create a server app registration in Azure AD. When you run this
cmdlet, it will prompt you to sign in to your tenant. For more information on this app
registration, see Manually register Azure AD apps for the CMG.

<!-- p.20 -->

  PowerShell

  New-CMAADServerApplication -AppName $appName

Set-CMDefaultBoundaryGroup
Use this cmdlet to modify the properties of a default site boundary group. You can set
the options to include and prefer the cloud-based sources for the clients in default site
boundary group. For more information on boundary groups, see About boundary
groups in Configuration Manager.

  PowerShell

  Set-CMDefaultBoundaryGroup -IncludeCloudBasedSources $true -
  PreferCloudBasedSources $true

Deprecated and removed cmdlets
The following cmdlets are no longer available because the resource access feature is no
longer supported:

     Add-CMCertificateRegistrationPoint
     Import-CMClientCertificatePfx
     Import-CMWirelessProfileConfigurationItem
     New-CMCertificateProfilePfx
     New-CMCertificateProfileScep
     New-CMCertificateProfileTrustedRootCA
     New-CMClientCertificateProfileConfigurationItem
     New-CMEmailProfile
     New-CMRootCertificateProfileConfigurationItem
     New-CMVpnProfileConfigurationItem
     New-CMWirelessProfile
     New-CMWirelessProfileConfigurationItem
     Set-CMCertificateProfilePfx
     Set-CMCertificateProfileScep
     Set-CMCertificateProfileTrustedRootCA
     Set-CMCertificateRegistrationPoint
     Set-CMClientCertificateProfileConfigurationItem
     Set-CMEmailProfile
     Set-CMVpnProfileConfigurationItem

<!-- p.21 -->

     Set-CMWirelessProfile
     Set-CMWirelessProfileConfigurationItem

Cmdlet changes
The following changes have been made to existing cmdlets in this version. Changes may
be new functionality or bug fixes. Some changes may be breaking. If you use one of the
cmdlets or feature areas listed in this section, carefully review the changes to understand
how they may affect your use.

Add-CMManagementPoint
For more information, see Add-CMManagementPoint.

Non-breaking changes

     When you use this cmdlet to enable communication with the cloud management
     gateway, it now by default configures the management point to support both
     internet and intranet clients.
     When you enable cloud gateway, ClientConnectionTypes.InternetAndIntranet is
     now the default value.

Add-CMReportingServicePoint
For more information, see Add-CMReportingServicePoint.

Non-breaking changes

This cmdlet will be blocked to run on PowerShell7, as SOAP is not supported in
PowerShell7. This cmdlet requires the .NET Framework instead of .NET Core that's used
with PowerShell version 7.

Get-CMObjectSecurityScope
For more information, see Get-CMObjectSecurityScope.

Non-breaking changes

You can now use this cmdlet to get the security scope of a specified folder object.

New-CMCloudManagementGateway

<!-- p.22 -->

For more information, see New-CMCloudManagementGateway.

Non-breaking changes

Added parameters VMSSVMSize and Version to support creating a cloud management
gateway (CMG) using a virtual machine scale set.

New-CMCoManagementPolicy
For more information, see New-CMCoManagementPolicy.

Non-breaking changes

     You can now view the policy created as well as prevent creation of second policy
     from this cmdlet.
     You can now also create child policies for each workload, like UI, while creating Co-
     Management policy from this cmdlet.

New-CMComplianceRuleRegistryKeyPermission
For more information, see New-CMComplianceRuleRegistryKeyPermission.

Bugs that were fixed

Fixed an issue in OperandDataType property when creating a rule.

Add-CMComplianceSettingWqlQuery
For more information, see Add-CMComplianceSettingWqlQuery.

Non-breaking changes

When using this cmdlet, you can now specify $null value to the parameter WhereClause.

Set-CMClientSettingComplianceSetting
For more information, see Set-CMClientSettingComplianceSetting.

Non-breaking changes

Added a new parameter ScriptExecutionTimeoutSecs to extend the script execution
timeout value.

Set-CMClientSettingClientCache

<!-- p.23 -->

For more information, see Set-CMClientSettingClientCache.

Non-breaking changes

Added a new parameter MinCacheTombstoneContentMins to support setting the
minimum duration before the client can remove cached content.

Set-CMClientSettingComputerRestart
For more information, see Set-CMClientSettingComputerRestart.

Non-breaking changes and bug fixes

     Extended the validation range of the parameters CountdownMins and
     RebootLogoffNotificationCountdownMins to align with the console.
     Added new parameters CountdownIntervalMins and ServerRebootLowRight to
     align with the console.
     Fixed a property name issue for the parameter NoRebootEnforcement.

Set-CMClientSettingEndpointProtection
For more information, see Set-CMClientSettingEndpointProtection.

Non-breaking changes

You can now specify the defender agent type with the new parameter DefenderAgent.

Get-CMNotification
For more information, see Get-CMNotification.

Non-breaking changes

     You can now use this cmdlet to get built-in notification by using parameter
     IsBuiltIn.
     You can now also use this cmdlet to get notification that could be dismissed by
     using parameter CanDismiss.
     New alias InputObject has been added for parameter NotificationTasks which now
     supports pipeline.

New-CMFolder
For more information, see New-CMFolder.

<!-- p.24 -->

Bugs that were fixed

An issue in folder path validation has been fixed when using this cmdlet to create a new
folder in the console.

Changes to multiple cmdlets
The following folder-related cmdlets now support software update groups and
automatic deployment rules:

     Get-CMFolder
     New-CMFolder
     Remove-CMFolder
     Set-CMFolder
     Move-CMObject
     Add-CMObjectSecurityScope
     Remove-CMObjectSecurityScope

The following cmdlets now have added validation condition for starting or stopping
service while CMG is a virtual machine scale set:

     Start-CMCloudManagementGateway
     Stop-CMCloudManagementGateway

How to provide feedback or report issues
Many of the fixes and improvements described in this article are a result of your
feedback.

To send feedback, use the Configuration Manager console. For more information, see
Feedback for PowerShell.

<!-- p.25 -->

Configuration Manager cmdlet library
changes for version 2203
Article • 10/03/2022

Applies to: Configuration Manager (current branch)

These release notes summarize changes to the Configuration Manager cmdlet library in
version 2203.

  ７ Note

  Configuration Manager current branch version 2111 is the baseline for these
  changes. For more information, see Configuration Manager cmdlet library
  changes for version 2111.

New cmdlets
      Get-CMAADTenant: Get an Azure Active Directory (Azure AD) tenant from the site.

      Set-CMCollectionCloudSync: Configure cloud sync features for a collection.

Deprecated and removed cmdlets
The following cmdlets for asset intelligence are deprecated and may be removed in a
future release:

      Add-CMAssetIntelligenceSynchronizationPoint
      Get-CMAssetIntelligenceProxy
      Get-CMAssetIntelligenceSynchronizationPoint
      Remove-CMAssetIntelligenceSynchronizationPoint
      Send-CMAssetIntelligenceCatalogUpdateRequest
      Set-CMAssetIntelligenceSynchronizationPoint
      Sync-CMAssetIntelligenceCatalog

Cmdlet changes
The following changes have been made to existing cmdlets in this version. Changes may
be new functionality or bug fixes. Some changes may be breaking. If you use one of the

<!-- p.26 -->

cmdlets or feature areas listed in this section, carefully review the changes to understand
how they may affect your use.

Add-CMSoftwareUpdatePoint
For more information, see Add-CMSoftwareUpdatePoint.

Non-breaking changes

Added new parameter Wledbat to support LEDBAT configuration for software update
points.

Get-CMDeploymentStatusDetails
For more information, see Get-CMDeploymentStatusDetails.

Bugs that were fixed

Updated the cmdlet to avoid a potential null reference error.

Get-CMDeploymentTypeDetectionClause
For more information, see Get-CMDeploymentTypeDetectionClause.

Non-breaking changes

The cmdlet can now get a detection clause from a script deployment type.

Import-CMApplication
For more information, see Import-CMApplication.

Non-breaking changes

Updated the import logic to align with console. Added new warning messages.

New-CMApplication
For more information, see New-CMApplication.

Non-breaking changes

It can now get an application icon from the specified file.

<!-- p.27 -->

New-CMBoundary
For more information, see New-CMBoundary.

Non-breaking changes

Updated value validation for VPN boundary.

New-CMCoManagementPolicy
For more information, see New-CMCoManagementPolicy.

Non-breaking changes

The cmdlet now supports applicability for Windows 11 on ARM64 devices.

New-CMPackage
For more information, see New-CMPackage.

Non-breaking changes

Added parameter IconLocationFile to use a custom icon from the specified file. For
more information, see Custom icon support for task sequences and packages.

New-CMSoftwareUpdateDeployment
For more information, see New-CMSoftwareUpdateDeployment.

Non-breaking changes

Added parameter PreDownloadUpdateContent to support pre-download for available
software updates.

New-CMTaskSequence
For more information, see New-CMTaskSequence.

Non-breaking changes

Added the IconLocationFile parameter to support specifying an icon for the task
sequence. For more information, see Custom icon support for task sequences and
packages.

<!-- p.28 -->

New-CMTaskSequenceDeployment
For more information, see New-CMTaskSequenceDeployment.

Bugs that were fixed

Fixed an issue with the AllowSharedContent parameter.

Publish-CMThirdPartySoftwareUpdateContent
For more information, see Publish-CMThirdPartySoftwareUpdateContent.

Non-breaking changes

Added the Force parameter to run the command without asking for confirmation.

Set-CMBoundary
For more information, see Set-CMBoundary.

Non-breaking changes

Updated value validation for VPN boundary.

Set-CMPackage
For more information, see Set-CMPackage.

Non-breaking changes

Added parameter IconLocationFile to use a custom icon from the specified file. For
more information, see Custom icon support for task sequences and packages.

Set-CMSoftwareUpdateDeployment
For more information, see Set-CMSoftwareUpdateDeployment.

Non-breaking changes

Added parameter PreDownloadUpdateContent to support pre-download for available
software updates.

Set-CMSoftwareUpdatePoint

<!-- p.29 -->

For more information, see Set-CMSoftwareUpdatePoint.

Non-breaking changes

Added new parameter Wledbat to support LEDBAT configuration for software update
points.

Set-CMSoftwareUpdatePointComponent
For more information, see Set-CMSoftwareUpdatePointComponent.

Non-breaking changes

Added the NonWindowsUpdateMaxRuntimeMins parameter to change the default
maximum run time for non-Windows software updates.

Set-CMTaskSequence
For more information, see Set-CMTaskSequence.

Non-breaking changes

Added the IconLocationFile parameter to support specifying an icon for the task
sequence. For more information, see Custom icon support for task sequences and
packages.

Set-CMTaskSequenceDeployment
For more information, see Set-CMTaskSequenceDeployment.

Bugs that were fixed

Fixed an issue with the AllowSharedContent parameter.

Start-CMTaskSequenceDeployment
For more information, see Start-CMTaskSequenceDeployment.

Bugs that were fixed

Fixed an issue with the AllowSharedContent parameter.

Changes to multiple cmdlets

<!-- p.30 -->

The following folder-related cmdlets now support software update groups and
deployment packages:

     Get-CMFolder
     New-CMFolder
     Remove-CMFolder
     Set-CMFolder
     Move-CMObject
     Add-CMObjectSecurityScope
     Remove-CMObjectSecurityScope

How to provide feedback or report issues
Many of the fixes and improvements described in this article are a result of your
feedback.

To send feedback, use the Configuration Manager console. For more information, see
Feedback for PowerShell.

<!-- p.31 -->

Configuration Manager cmdlet library
changes for version 2111
Article • 10/03/2022

Applies to: Configuration Manager (current branch)

These release notes summarize changes to the Configuration Manager cmdlet library in
version 2111.

  ７ Note

  Configuration Manager current branch version 2107 is the baseline for these
  changes. For more information, see Configuration Manager cmdlet library
  changes for version 2107.

Module changes
When you install the Configuration Manager console, the path to the
ConfigurationManager PowerShell module is now added to the system environment
variable, PSModulePath. For example, by default, this path is C:\Program Files
(x86)\Microsoft Endpoint Manager\AdminConsole\bin .

With this change, it's easier to import this module with the following command: Import-
Module ConfigurationManager

For more information, see about_PSModulePath.

New cmdlets
      Get-CMDeploymentTypeRequirement: Use this cmdlet to get the requirement rules
      for the specified deployment type. You can use the returned object to add the
      same rules to another deployment type.

      Remove-CMSoftwareUpdateFromPackage: Use this cmdlet to remove the specified
      software update from a package.

      Set-CMApplicationSupersedence: Use this cmdlet to set deployment type
      supersedence for the specified application.

<!-- p.32 -->

Orchestration groups
For more information about this feature, see Orchestration groups in Configuration
Manager.

     Get-CMOrchestrationGroup: Use this cmdlet to get an orchestration group object
     by name or ID. You can use this object to start, remove, or configure the
     orchestration group.

     Invoke-CMOrchestrationGroup: Use this cmdlet to start orchestration.

     New-CMOrchestrationGroup: Use this cmdlet to create a new orchestration group.

     Remove-CMOrchestrationGroup: Use this cmdlet to remove the specified
     orchestration group.

     Set-CMOrchestrationGroup: Use this cmdlet to configure an orchestration group.

Role-based administration
For more information on security roles and permissions, see Fundamentals of role-based
administration in Configuration Manager.

     Get-CMSecurityRolePermission: Use this cmdlet to get the permissions for the
     specified security role.

     Set-CMSecurityRolePermission: Use this cmdlet to configure a security role with
     specific permissions.

Folder management
For more information on folders, see How to use the Configuration Manager console.

     Get-CMFolder: Use this cmdlet to get all customized folders or folders from the
     specified parent path.

     New-CMFolder: Use this cmdlet to create a new folder under the specified parent
     folder path.

     Remove-CMFolder: Use this cmdlet to remove the specified folder.

     Set-CMFolder: Use this cmdlet to configure the specified folder. For example,
     rename it or move it to another folder.

<!-- p.33 -->

Deprecated and removed cmdlets
The following cmdlets are deprecated and may be removed in a future release:

 Deprecated cmdlet                                     Replacement

 Add-CMDeploymentTypeSupersedence                      Set-CMApplicationSupersedence

 Remove-CMDeploymentTypeSupersedence                   Set-CMApplicationSupersedence

 Set-CMDeploymentTypeSupersedence                      Set-CMApplicationSupersedence

The following cmdlets are no longer available because the underlying feature is no
longer supported:

     Get-CMTSStepConvertDisk
     New-CMTSStepConvertDisk
     Remove-CMTSStepConvertDisk
     Set-CMTSStepConvertDisk

Cmdlet changes
The following changes have been made to existing cmdlets in this version. Changes may
be new functionality or bug fixes. Some changes may be breaking. If you use one of the
cmdlets or feature areas listed in this section, carefully review the changes to understand
how they may affect your use.

Add-CMDeviceCollectionDirectMembershipRule
For more information, see Add-CMDeviceCollectionDirectMembershipRule.

Bugs that were fixed

Fixed an issue when adding a rule by resource object.

Add-CMDistributionPoint
Bugs that were fixed

You can't specify the central administration site (CAS) for the SiteCode parameter, which
doesn't support any client-facing site system roles.

Get-CMClientSetting

<!-- p.34 -->

For more information, see Get-CMClientSetting.

Non-breaking changes

Added support to return the value for the Disable Deadline Randomization setting in the
Computer Agent group.

Get-CMPersistentUserSettingsGroup
For more information, see Get-CMPersistentUserSettingsGroup.

Bugs that were fixed

Fixed an issue with the Name parameter to filter on setting groups.

Get-CMUserDeviceAffinity
For more information, see Get-CMUserDeviceAffinity.

Non-breaking changes

Add parameter ShowApprovedOnly to filter out non-approved affinities.

New-CMBoundary
For more information, see New-CMBoundary.

Non-breaking changes

Added new parameter ValueStartsWith to support improvements to VPN boundary
types.

New-CMTSPartitionSetting
For more information, see New-CMTSPartitionSetting.

Non-breaking changes

Set default value for AssignVolumeLetter.

New-CMTSStepApplyWindowsSetting
For more information, see New-CMTSStepApplyWindowsSetting.

<!-- p.35 -->

Breaking changes

Removed the following unsupported parameters:

     MaximumConnection
     ServerLicensing

New-CMTSStepPrestartCheck
For more information, see New-CMTSStepPrestartCheck.

Non-breaking changes

Added new parameters for TPM existence check:

     CheckTpmEnabled
     CheckTpmActivated

New-CMWdacSetting
For more information, see New-CMWdacSetting.

Non-breaking changes

Added support for new platform rules for Windows 10 ARM64 and Windows 10 multi-
session.

Remove-CMPersistentUserSettingsGroup
For more information, see Remove-CMPersistentUserSettingsGroup.

Bugs that were fixed

Fixed a query issue when remove settings group by name.

Set-CMBoundary
For more information, see Set-CMBoundary.

Non-breaking changes

Added new parameter ValueStartsWith to support improvements to VPN boundary
types.

<!-- p.36 -->

Set-CMDeviceVariable
For more information, see Set-CMDeviceVariable.

Non-breaking changes

The parameter VariableName is now case-insensitive.

Set-CMDistributionPoint
For more information, see Set-CMDistributionPoint.

Non-breaking changes

Added new parameter EnableMaintenanceMode to support to manage maintenance
mode.

Set-CMSoftwareUpdatePoint
For more information, see Set-CMSoftwareUpdatePoint.

Bugs that were fixed

Fixed an issue with regular expression processing when trying to clear the WSUS access
account from a software update point.

Set-CMSoftwareUpdatePointComponent
For more information, see Set-CMSoftwareUpdatePointComponent.

Breaking changes

Removed the deprecated parameter EnableSynchronization from this cmdlet. To set the
synchronization schedule, use the Schedule parameter.

For example, to disable the synchronization schedule:

  PowerShell

  Set-CMSoftwareUpdatePointComponent -Name "Contoso-
  SiteSysSrv.Western.Contoso.com" -Schedule $null

Set-CMTSStepApplyWindowsSetting

<!-- p.37 -->

For more information, see Set-CMTSStepApplyWindowsSetting.

Breaking changes

Removed the following unsupported parameters:

     MaximumConnection
     ServerLicensing

Set-CMTSStepPrestartCheck
For more information, see Set-CMTSStepPrestartCheck.

Non-breaking changes

Added new parameters for TPM existence check:

     CheckTpmEnabled
     CheckTpmActivated

Changes to multiple cmdlets
The following changes were made across multiple cmdlets of a similar type.

Import and export verbs
This change applies to all cmdlets with import and export verbs. For example, Import-
CMAADClientApplication and Export-CMApplication.

Non-breaking changes

To allow for consistent parameter use across these cmdlets, they all have aliases for the
parameter to specify the import path: FilePath , FileName , ImportFilePath , Path

Configure application deployment types
This change applies to all cmdlets with set verbs to configure application deployment
types. These cmdlet names use the pattern Set-CM*DeploymentType , where * is the
application technology. For example, Set-CMMsiDeploymentType.

Bugs that were fixed

Fixed a requirement rule name issue with these cmdlets.

<!-- p.38 -->

Create requirement rules
This change applies to all cmdlets with the name pattern New-CMRequirementRule* , where
* is the type of rule. For example, New-CMRequirementRuleExistential.

Bugs that were fixed

Fixed a requirement rule name issue with these cmdlets.

How to provide feedback or report issues
Many of the fixes and improvements described in this article are a result of your
feedback.

To send feedback, use the Configuration Manager console. For more information, see
Feedback for PowerShell.

<!-- p.39 -->

Configuration Manager cmdlet library
changes for version 2107
Article • 10/03/2022

Applies to: Configuration Manager (current branch)

These release notes summarize changes to the Configuration Manager cmdlet library in
version 2107.

  ７ Note

  Configuration Manager current branch version 2103 is the baseline for these
  changes. For more information, see Configuration Manager cmdlet library
  changes for version 2103.

New cmdlets for app deployment types

Manage install behaviors for application deployment
types
This set of new cmdlets is for application deployment type installation behavior. For
more general information on the install behavior feature, see Check for running
executable files.

Add-CMDeploymentTypeInstallBehavior
Use this cmdlet to add to the specified deployment type the executable files that need
to close for the app install to succeed.

  PowerShell

  $msi_dt = Get-CMDeploymentType -ApplicationName "CenterApp" -
  DeploymentTypeName "InterDept - Windows Installer (.msi file)"
  Add-CMDeploymentTypeInstallBehavior -InputObject $msi_dt -ExeFileName
  "notepad.exe" -DisplayName "Notepad"

For more information, see Add-CMDeploymentTypeInstallBehavior.

<!-- p.40 -->

Get-CMDeploymentTypeInstallBehavior
Use this cmdlet to get from the specified deployment type the list of executable files
that need to close for the app install to succeed.

  PowerShell

  $msi_dt = Get-CMDeploymentType -ApplicationName "CenterApp" -
  DeploymentTypeName "InterDept - Windows Installer (.msi file)"
  Get-CMDeploymentTypeInstallBehavior -InputObject $msi_dt

For more information, see Get-CMDeploymentTypeInstallBehavior.

Remove-CMDeploymentTypeInstallBehavior

Use this cmdlet to remove from the specified deployment type the executable files that
need to close for the app install to succeed.

  PowerShell

  $msi_dt = Get-CMDeploymentType -ApplicationName "CenterApp" -
  DeploymentTypeName "InterDept - Windows Installer (.msi file)"
  Remove-CMDeploymentTypeInstallBehavior -InputObject $msi_dt -ExeFileName
  "notepad.exe"

For more information, see Remove-CMDeploymentTypeInstallBehavior.

Set-CMDeploymentTypeInstallBehavior

Use this cmdlet to modify the executable files that need to close for the app install to
succeed.

  PowerShell

  $msi_dt = Get-CMDeploymentType -ApplicationName "CenterApp" -
  DeploymentTypeName "InterDept - Windows Installer (.msi file)"
  Set-CMDeploymentTypeInstallBehavior -InputObject $msi_dt -ExeFileName
  "notepad.exe" -NewExeFileName "calc.exe" -DisplayName "Calculator"

For more information, see Set-CMDeploymentTypeInstallBehavior.

Manage return codes for application deployment types
