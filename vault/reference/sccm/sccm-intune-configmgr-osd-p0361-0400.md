---
title: "OS deployment documentation — pages 361-400"
type: reference
domain: sccm
slug: sccm-intune-configmgr-osd-p0361-0400
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-osd-p0361-0400
family: sccm
documentKind: "doc"
abstract: "images are associated with the specified Image package, select from the drop-down list the associated image to use for this deployment. You can view basic information about each existing image by selecting it. Apply operating system image from an original installation source Ins"
---

# OS deployment documentation — pages 361-400

<!-- p.361 -->

images are associated with the specified Image package, select from the drop-down list
the associated image to use for this deployment. You can view basic information about
each existing image by selecting it.

Apply operating system image from an original installation source
Installs an OS using an OS upgrade package, which is also an original installation source.
Select Browse to open the Select an Operating System Upgrade Package dialog box.
Then select the existing OS upgrade package you want to use. You can view basic
information about each existing image source by selecting it. The results pane at the
bottom of the dialog box displays the associated image source properties. If there are
multiple editions associated with the specified package, use the drop-down list to select
the Edition you want to use.

  ７ Note

  Operating System Upgrade Packages are primarily meant for use with in-place
  upgrades and not for new installations of Windows. When deploying new
  installations of Windows, use the Apply operating system from a captured image
  option and install.wim from the installation source files.

  Deploying new installations of Windows via Operating System Upgrade Packages
  is still supported, but it's dependent on drivers being compatible with this method.
  When installing Windows from an OS upgrade package, drivers are installed while
  still in Windows PE versus simply being injected while in Windows PE. Some drivers
  aren't compatible with being installed while in Windows PE.

  If drivers aren't compatible with being installed while in Windows PE, then create an
  Operating System Image with the install.wim from the original installation source
  files. Then deploy via the Apply operating system from a captured image option
  instead.

Use an unattended or sysprep answer file for a custom installation
Use this option to provide a Windows setup answer file (unattend.xml, unattend.txt, or
sysprep.inf) depending on the OS version and installation method. The file you specify
can include any of the standard configuration options supported by Windows answer
files. For example, you can use it to specify the default Internet Explorer home page.
Specify the package that contains the answer file and the associated path to the file in
the package.

<!-- p.362 -->

  ７ Note

  The Windows setup answer file that you supply can contain embedded task
  sequence variables of the form %varname% , where varname is the name of the
  variable. The Setup Windows and ConfigMgr step substitutes the variable string
  for the actual value of the variable. You can't use these embedded task sequence
  variables in numeric-only fields in an unattend.xml answer file.

If you don't supply a Windows setup answer file, the task sequence automatically
generates an answer file.

Destination
Configure one of the following options:

     Next available partition: Use the next sequential partition not already targeted by
     an Apply Operating System or Apply Data Image step in this task sequence.

     Specific disk and partition: Select the Disk number (starting with 0) and the
     Partition number (starting with 1).

     Specific logical drive letter: Specify the Drive Letter assigned to the partition by
     Windows PE. This drive letter can be different from the drive letter assigned by the
     newly deployed OS.

     Logical drive letter stored in a variable: Specify the task sequence variable
     containing the drive letter assigned to the partition by Windows PE. This variable is
     typically set in the Advanced section of the Partition Properties dialog box for the
     Format and Partition Disk task sequence step.

Select layered driver if applicable

Version 2107 and later supports layered keyboard drivers. These drivers specify other
types of keyboards that are common with Japanese and Korean languages. For more
information, see the LayeredDriver Windows setting.

Choose one of the following options:

     Do not specify: This option is the default, which doesn't configure the
     LayeredDriver setting in the unattend.xml. This behavior is consistent with earlier
     versions of Configuration Manager.
     PC/AT Enhanced keyboard (101/102-key)

<!-- p.363 -->

     Korean PC/AT 101-Key Compatible keyboard or the Microsoft Natural keyboard
     (type 1)
     Korean PC/AT 101-Key Compatible keyboard or the Microsoft Natural keyboard
     (type 2)
     Korean PC/AT 101-Key Compatible keyboard or the Microsoft Natural keyboard
     (type 3)
     Korean keyboard (103/106-key)
     Japanese keyboard (106/109-key)

You can also use the OsdLayeredDriver task sequence variable.

Options for Apply OS Image
Besides the default options, configure the following additional settings on the Options
tab of this task sequence step:

Access content directly from the distribution point

Configure the task sequence to access the OS image directly from the distribution point.
For example, use this option when you deploy operating systems to embedded devices
that have limited storage capacity. When selecting this option, also configure the
package share settings on the Data Access tab of the OS image properties.

  ７ Note

  This setting overrides the deployment option that you configure on the
  Distribution Points page in the Deploy Software Wizard. This override is only for
  the OS image that this step specifies, not for all task sequence content.

  ） Important

  For greatest security, it is strongly recommended not to select this option. This
  option is mainly designed for use on devices with limited storage capacity. This
  option is not meant to help increase the speed of the task sequence. When this
  option is selected, the package hash is not verified for the operating system
  package. Therefore, package integrity cannot be ensured because it is possible for
  users with administrative rights to alter or tamper with package contents.

Apply Windows Settings

<!-- p.364 -->

Use this step to configure the Windows settings for the destination computer. The task
sequence stores these values in the appropriate answer file. Windows Setup uses this
answer file during the Setup Windows and ConfigMgr step.

This task sequence step runs only in Windows PE. It doesn't run in the full OS.

To add this step in the task sequence editor, select Add, select Settings, and select
Apply Windows Settings.

Variables for Apply Windows Settings
Use the following task sequence variables with this step:

     OSDComputerName
     OSDLocalAdminPassword
     OSDProductKey
     OSDRandomAdminPassword
     OSDRegisteredOrgName
     OSDRegisteredUserName
     OSDServerLicenseConnectionLimit
     OSDServerLicenseMode
     OSDTimeZone
     OSDWindowsSettingsInputLocale
     OSDWindowsSettingsSystemLocale
     OSDWindowsSettingsUILanguage
     OSDWindowsSettingsUILanguageFallback
     OSDWindowsSettingsUserLocale

Cmdlets for Apply Windows Settings
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepApplyWindowsSetting
     New-CMTSStepApplyWindowsSetting
     Remove-CMTSStepApplyWindowsSetting
     Set-CMTSStepApplyWindowsSetting

Properties for Apply Windows Settings
On the Properties tab for this step, configure the settings described in this section.

<!-- p.365 -->

User name
Specify the registered user name to associate with the destination computer. The value
that the Capture Windows Settings task sequence step captures can override this value.

Organization name
Specify the registered organization name to associate with the destination computer.
The value that the Capture Windows Settings task sequence step captures can override
this value.

Product key
Specify the product key to use for the Windows installation on the destination
computer.

Server licensing

  ７ Note

  This setting only applies to legacy versions of Windows that are no longer
  supported. Starting in version 2010, the setting is no longer visible in the task
  sequence editor. Existing task sequences that still use this setting will continue to
  function the same.

Maximum connections

  ７ Note

  This setting only applies to legacy versions of Windows that are no longer
  supported. Starting in version 2010, the setting is no longer visible in the task
  sequence editor. Existing task sequences that still use this setting will continue to
  function the same.

Randomly generate the local administrator password and disable
the account on all supported platforms (recommended)
Select this option to set the local administrator password to a randomly generated
string. This option also disables the local administrator account on platforms that

<!-- p.366 -->

support this capability.

Enable the account and specify the local administrator password
Select this option to enable the local administrator account using the specified
password. Enter the password on the Password line and confirm the password on the
Confirm password line.

Time zone
Specify the time zone to configure on the destination computer. The value that the
Capture Windows Settings task sequence step captures can override this value.

Language settings
Use these settings to control the language configuration during OS deployment. If
you're already applying these language settings, this change can help you simplify your
OS deployment task sequence. Instead of using multiple steps per language or separate
scripts, use one instance per language of this step with a condition for that language.

Configure the following settings:

     Input locale (default keyboard layout)
     System locale
     UI language
     UI language fallback
     User locale

For more information on these Windows setup answer file values, see Microsoft-
Windows-International-Core.

  ７ Note

  If you create a custom Windows setup answer file (unattend.xml), this step
  overwrites any existing values. To automate a dynamic process for these settings,
  use the related task sequence variables. For example,
  OSDWindowsSettingsInputLocale.

Auto Apply Drivers
Use this step to match and install drivers as part of the OS deployment.

<!-- p.367 -->

  ） Important

  Stand-alone media can't use the Auto Apply Drivers step. The task sequence has
  no connection to the Configuration Manager site in this scenario.

This task sequence step runs only in Windows PE. It doesn't run in the full OS.

To add this step in the task sequence editor, select Add, select Drivers, and select Auto
Apply Drivers.

   Tip

  For an overview of drivers in Configuration Manager, see Use task sequences to
  install drivers.

Behaviors for Auto Apply Drivers
The Auto Apply Drivers task sequence step performs the following actions:

   1. Scan the hardware and find the plug-and-play IDs for all devices present on the
     system.

   2. Send the list of devices and their plug-and-play IDs to the management point. The
     management point returns a list of compatible drivers from the driver catalog for
     each hardware device. The list includes all enabled drivers regardless of what driver
     package they are in, and drivers tagged with the specified driver category.

   3. For each hardware device, the task sequence picks the best driver. This driver is
     appropriate for the deployed OS, and is on an accessible distribution point.

   4. The task sequence downloads the selected drivers from a distribution point, and
     stages the drivers on the target OS.

      a. When using an OS image, the task sequence places the drivers into the OS
        driver store.

     b. When using an OS upgrade package as an original installation source, the task
        sequence configures Windows Setup with the drivers' location.

   5. During the Setup Windows and ConfigMgr step in the task sequence, Windows
     Setup finds the drivers staged by this step.

<!-- p.368 -->

Variables for Auto Apply Drivers
Use the following task sequence variables with this step:

     OSDAutoApplyDriverBestMatch
     OSDAutoApplyDriverCategoryList
     SMSTSDriverRequestConnectTimeOut
     SMSTSDriverRequestReceiveTimeOut
     SMSTSDriverRequestResolveTimeOut
     SMSTSDriverRequestSendTimeOut

Cmdlets for Auto Apply Drivers
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepAutoApplyDriver
     New-CMTSStepAutoApplyDriver
     Remove-CMTSStepAutoApplyDriver
     Set-CMTSStepAutoApplyDriver

Properties for Auto Apply Drivers
On the Properties tab for this step, configure the settings described in this section.

Install only the best matched compatible drivers

Specifies that the task sequence step installs only the best matched driver for each
hardware device detected.

Install all compatible drivers

The task sequence installs all drivers compatible for each detected hardware device.
Windows Setup then chooses the best driver. This option takes more network
bandwidth and disk space. The task sequence downloads more drivers, but Windows
can select a better driver.

Consider drivers from all categories
The task sequence searches all available driver categories for the appropriate device
drivers.

<!-- p.369 -->

Limit driver matching to only consider drivers in selected
categories

The task sequence searches in the specified driver categories for the appropriate device
drivers.

If you select multiple categories, it returns all matching drivers that are present in any of
the categories. It's equivalent to an OR operation.

Do unattended installation of unsigned drivers on versions of
Windows where this is allowed
This option allows Windows to install drivers without a digital signature.

  ） Important

  This option doesn't apply to operating systems where you can't configure driver
  signing policy.

Capture Network Settings
Use this step to capture Microsoft network settings from the computer running the task
sequence. The task sequence saves these settings in task sequence variables. These
settings override the default settings you configure on the Apply Network Settings
step.

This task sequence step runs only in the full OS. It doesn't run in Windows PE.

To add this step in the task sequence editor, select Add, select Settings, and select
Capture Network Settings.

Variables for Capture Network Settings
Use the following task sequence variables with this step:

        OSDMigrateAdapterSettings
        OSDMigrateNetworkMembership

Cmdlets for Capture Network Settings
Manage this step with the following PowerShell cmdlets:

<!-- p.370 -->

     Get-CMTSStepCaptureNetworkSettings
     New-CMTSStepCaptureNetworkSettings
     Remove-CMTSStepCaptureNetworkSettings
     Set-CMTSStepCaptureNetworkSettings

Properties for Capture Network Settings
On the Properties tab for this step, configure the settings described in this section.

Migrate domain and workgroup membership
Captures the domain and workgroup membership information of the destination
computer.

Migrate network adapter configuration
Captures the network adapter configuration of the destination computer. It captures the
following information:

     Global network settings
     Number of adapters
     The following network settings associated with each adapter: DNS, IP, and port
     filters

Capture Operating System Image
This step captures one or more images from a reference computer. The task sequence
creates a Windows image (.wim) file on the specified network share. Then use the Add
Operating System Image Package wizard to import this image into Configuration
Manager for image-based OS deployments.

Configuration Manager captures each volume (drive) from the reference computer to a
separate image within the .wim file. If the referenced computer has multiple volumes,
the resulting .wim file contains a separate image for each volume. This step only
captures volumes that are formatted as NTFS or FAT32. It skips volumes with other
formats, and USB volumes.

The installed OS on the reference computer must be a version of Windows that
Configuration Manager supports. Use the SysPrep tool to prepare the OS on the
reference computer. The installed OS volume and the boot volume must be the same
volume.

<!-- p.371 -->

Specify an account with write permissions to the selected network share. For more
information on the capture OS image account, see Accounts.

This task sequence step runs only in Windows PE. It doesn't run in the full OS.

To add this step in the task sequence editor, select Add, select Images, and select
Capture Operating System Image.

Variables for Capture OS Image
Use the following task sequence variables with this step:

     OSDCaptureAccount
     OSDCaptureAccountPassword
     OSDCaptureDestination
     OSDImageCreator
     OSDImageDescription
     OSDImageVersion
     OSDTargetSystemRoot

Cmdlets for Capture OS Image
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepCaptureSystemImage
     New-CMTSStepCaptureSystemImage
     Remove-CMTSStepCaptureSystemImage
     Set-CMTSStepCaptureSystemImage

Properties for Capture OS Image
On the Properties tab for this step, configure the settings described in this section.

Target
File system path to the location that Configuration Manager uses when storing the
captured OS image.

Description
An optional user-defined description of the captured OS image that's stored in the
image file.

<!-- p.372 -->

Version
An optional user-defined version number to assign to the captured OS image. This value
can be any combination of letters and numbers. It's stored in the image file.

Created by
The optional name of the user that created the OS image. It's stored in the image file.

Capture operating system image account
Enter the Windows account that has permissions to the specified network share. Select
Set to specify the name of the Windows account.

Capture User State
This step uses the User State Migration Tool (USMT) to capture user state and settings
from the computer running the task sequence. This task sequence step is used in
conjunction with the Restore User State task sequence step. This step always encrypts
the USMT state store by using an encryption key that Configuration Manager generates
and manages.

Starting in version 2103, this step and the Restore User State step use the current
highest supported encryption algorithm, AES 256.

  ） Important

  If you have any active user state migrations, before you update the Configuration
  Manager client on those devices, restore the user state. Otherwise, the updated
  client will fail to restore the user state when it tries to use a different encryption
  algorithm. If necessary, you can manually restore the user state and explicitly use
  the USMT parameter /decrypt:3DES .

For more information about managing the user state when deploying operating
systems, see Manage user state.

If you want to save and restore user state settings from a state migration point, use this
step with the Request State Store and Release State Store steps.

This step provides control over a limited subset of the most commonly used USMT
options. Specify additional command-line options using the

<!-- p.373 -->

OSDMigrateAdditionalCaptureOptions task sequence variable.

This task sequence step runs in either Windows PE or the full OS.

To add this step in the task sequence editor, select Add, select User State, and select
Capture User State.

Variables for Capture User State
Use the following task sequence variables with this step:

     _OSDMigrateUsmtPackageID
     OSDMigrateAdditionalCaptureOptions
     OSDMigrateConfigFiles
     OSDMigrateContinueOnLockedFiles
     OSDMigrateEnableVerboseLogging
     OSDMigrateMode
     OSDMigrateSkipEncryptedFiles
     OSDStateStorePath

Cmdlets for Capture User State
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepCaptureUserState
     New-CMTSStepCaptureUserState
     Remove-CMTSStepCaptureUserState
     Set-CMTSStepCaptureUserState

Properties for Capture User State
On the Properties tab for this step, configure the settings described in this section.

User state migration tool package
Specify the package that contains the User State Migration Tool (USMT). The task
sequence uses this version of USMT to capture the user state and settings. This package
doesn't require a program. Specify a package containing the 32-bit or 64-bit version of
USMT. The architecture of USMT depends upon the architecture of the OS from which
the task sequence is capturing state.

<!-- p.374 -->

Capture all user profiles by using standard options
Migrate all user profile information. This option is the default.

If you select this option, but don't select Restore local computer user profiles in the
Restore User State step, the task sequence fails. Configuration Manager can't migrate
the new accounts without assigning them passwords.

When you use the Install an existing image package option of the New Task Sequence
wizard, the resulting task sequence defaults to Capture all user profiles with standard
options. This default task sequence doesn't select the option to Restore local computer
user profiles, or non-domain user accounts.

Select Restore local computer user profiles and provide a password for the account to
migrate. In a manually created task sequence, this setting is found under the Restore
User State step. In a task sequence created by the New Task Sequence wizard, this
setting is found under the step Restore User Files and Settings wizard page.

If you have no local user accounts, this setting doesn't apply.

Customize how user profiles are captured

Select this option to specify a custom profile file for migration. Select Files to select the
configuration files for USMT to use with this step. Specify a custom .xml file that
contains rules that define the user state files to migrate.

Select configuration files

Choose this option and select Files to select the configuration files in the USMT package
you want to use to capture user profiles. To add a configuration file, enter the Filename
and select Add.

Enable verbose logging
Enable this option to generate more detailed log file information. When capturing state,
the task sequence by default generates ScanState.log in the task sequence log folder,
%WinDir%\ccm\logs .

Skip files using encrypted file system
Enable this option to skip capturing files encrypted with the Encrypted File System (EFS).
These files include user profile files. Depending on the OS and USMT versions,

<!-- p.375 -->

encrypted files might not be readable after you restore. For more information, see the
USMT documentation.

Copy by using file system access

Enable this option to specify any of the following settings:

     Continue if some files cannot be captured: Enable this setting to continue the
     migration process even if it can't capture some files. If you disable this option, and
     a file can't be captured, then this step fails. This option is enabled by default.

     Capture locally by using links instead of by copying files: Enable this setting to
     use NTFS hard-links to capture files.

     For more information about migrating data using hard-links, see Hard-Link
     Migration Store.

     Capture in off-line mode (Windows PE only): Enable this setting to capture the
     user state while in Windows PE instead of the full OS.

Capture by using Volume Copy Shadow Services (VSS)
This option allows you to capture files even if they're locked for editing by another
application.

Capture Windows Settings
Use this step to capture the Windows settings from the computer running the task
sequence. The task sequence saves these settings in task sequence variables. These
captured settings override the default settings that you configure on the Apply
Windows Settings step.

This task sequence step runs in either Windows PE or the full OS.

To add this step in the task sequence editor, select Add, select Settings, and select
Capture Windows Settings.

Variables for Capture Windows Settings
Use the following task sequence variables with this step:

     OSDComputerName
     OSDMigrateComputerName

<!-- p.376 -->

     OSDMigrateRegistrationInfo
     OSDMigrateTimeZone
     OSDRegisteredOrgName
     OSDTimeZone

Cmdlets for Capture Windows Settings
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepCaptureWindowsSettings
     New-CMTSStepCaptureWindowsSettings
     Remove-CMTSStepCaptureWindowsSettings
     Set-CMTSStepCaptureWindowsSettings

Properties for Capture Windows Settings
On the Properties tab for this step, configure the settings described in this section.

Migrate computer name
Capture the NetBIOS computer name of the computer.

Migrate registered user and organization names
Capture the registered user and organization names from the computer.

Migrate time zone
Capture the time zone setting on the computer.

Check Readiness
Use this step to verify that the target computer meets the specified deployment
prerequisite conditions.

To add this step in the task sequence editor, select Add, select General, and select
Check Readiness.

None of the following checks are selected by default in new or existing instances of the
step. For more information on each check, see the specific sections below.

<!-- p.377 -->

     Architecture of current OS
     Minimum OS version
     Maximum OS version
     Minimum client version
     Language of current OS
     AC power plugged in
     Network adapter connected
        Network adapter is not wireless
     Computer is in UEFI mode

Starting in version 2103, the task sequence progress displays more information about
readiness checks. If a task sequence fails because the client doesn't meet the
requirements of this step, the user can select an option to Inspect. This action shows the
checks that failed on the device. For more information, see User experiences for OS
deployment.

Starting in version 2111, this step includes checks for TPM 2.0. These checks can help
you better deploy Windows 11.

  ） Important

  To take advantage of this new Configuration Manager feature, after you update the
  site, also update clients to the latest version. While new functionality appears in the
  Configuration Manager console when you update the site and console, the
  complete scenario isn't functional until the client version is also the latest.

The smsts.log includes the outcome of all checks. If one check fails, the task sequence
engine continues to evaluate the other checks. The step doesn't fail until all checks are
complete. If at least one check fails, the step fails, and it returns error code 4316. This
error code translates to "The resource required for this operation does not exist."

Variables for Check Readiness
Use the following task sequence variables with this step:

     _TS_CRMEMORY
     _TS_CRSPEED
     _TS_CRDISK
     _TS_CROSTYPE
     _TS_CRARCH
     _TS_CRMINOSVER

<!-- p.378 -->

     _TS_CRMAXOSVER
     _TS_CRCLIENTMINVER
     _TS_CROSLANGUAGE
     _TS_CRACPOWER
     _TS_CRNETWORK
     _TS_CRUEFI
     _TS_CRWIRED
     _TS_CRTPMACTIVATED (starting in version 2111)
     _TS_CRTPMENABLED (starting in version 2111)

Cmdlets for Check Readiness
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepPrestartCheck
     New-CMTSStepPrestartCheck
     Remove-CMTSStepPrestartCheck
     Set-CMTSStepPrestartCheck

Properties for Check Readiness
On the Properties tab for this step, configure the settings described in this section.

Minimum memory (MB)
Verify that the amount of memory, in megabytes (MB), meets or exceeds the specified
amount. The step enables this setting by default.

Minimum processor speed (MHz)

Verify that the speed of the processor, in megahertz (MHz), meets or exceeds the
specified amount. The step enables this setting by default.

Minimum free disk space (MB)

Verify that the amount of free disk space, in megabytes (MB), meets or exceeds the
specified amount.

Starting in version 2103, it also checks free space on disks without partitions.

<!-- p.379 -->

Current OS to be refreshed is
Verify that the OS installed on the target computer meets the specified requirement. The
step sets this setting to CLIENT by default.

Architecture of current OS
Verify whether the current OS is 32-bit or 64-bit.

Minimum OS version
Verify that the current OS is running a version later than specified. Specify the version
with major version, minor version, and build number. For example, 10.0.16299 .

Maximum OS version

Verify that the current OS is running a version earlier than specified. Specify the version
with major version, minor version, and build number. For example, 10.0.18356 .

Minimum client version

Verify that the Configuration Manager client version is at least the specified version.
Specify the client version in the following format: 5.00.8913.1005 .

Language of current OS
Verify that the current OS language matches what you specify. Select the language
name, and the step compares the associated language code. This check compares the
language that you select to the OSLanguage property of the Win32_OperatingSystem
WMI class on the client.

AC power plugged in
Verify that the device is plugged in and not on battery.

Network adapter connected
Verify that the device has a network adapter that's connected to the network. You can
also select the dependent check to verify that the Network adapter is not wireless.

<!-- p.380 -->

Computer is in UEFI mode
Determine whether the device is configured for UEFI or BIOS.

TPM 2.0 or above is enabled

Starting in version 2111, checks whether the device that's running the task sequence has
a TPM 2.0 that's enabled.

TPM 2.0 or above is activated
Starting in version 2111, if the device has an enabled TPM 2.0, check that it's activated.

Options for Check Readiness

  ７ Note

  If you enable the Continue on error setting on the Options tab of this step, it only
  logs the readiness check results. If a check fails, the task sequence doesn't stop.

Connect To Network Folder
Use this step to create a connection to a shared network folder.

This task sequence step runs in the full OS or Windows PE.

To add this step in the task sequence editor, select Add, select General, and select
Connect To Network Folder.

Variables for Connect To Network Folder
Use the following task sequence variables with this step:

     SMSConnectNetworkFolderAccount
     SMSConnectNetworkFolderDriveLetter
     SMSConnectNetworkFolderPassword
     SMSConnectNetworkFolderPath

Cmdlets for Connect To Network Folder

<!-- p.381 -->

Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepConnectNetworkFolder
     New-CMTSStepConnectNetworkFolder
     Remove-CMTSStepConnectNetworkFolder
     Set-CMTSStepConnectNetworkFolder

Properties for Connect To Network Folder
On the Properties tab for this step, configure the settings described in this section.

Path

Select Browse to specify the network folder path. Use the format \\server\share .

Drive
Select the local drive letter to assign for this connection.

Account
Select Set to specify the user account with permissions to connect to this network
folder. For more information on the task sequence network folder connection account,
see Accounts.

Disable BitLocker
Use this step to disable BitLocker encryption on the current OS drive, or on a specific
drive. This action leaves the key protectors visible in clear text on the hard drive. It
doesn't decrypt the contents of the drive. This action completes almost instantly.

  ７ Note

  BitLocker drive encryption provides low-level encryption of the contents of a disk
  volume.

If you have multiple encrypted drives, disable BitLocker on any data drives before
disabling BitLocker on the OS drive.

This step runs only in the full OS. It doesn't run in Windows PE.

<!-- p.382 -->

To add this step in the task sequence editor, select Add, select Disks, and select Disable
BitLocker.

Variables for Disable BitLocker
Use the following task sequence variables with this step:

     OSDBitLockerRebootCount
     OSDBitLockerRebootCountOverride

Cmdlets for Disable BitLocker
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepDisableBitLocker
     New-CMTSStepDisableBitLocker
     Remove-CMTSStepDisableBitLocker
     Set-CMTSStepDisableBitLocker

Properties for Disable BitLocker
On the Properties tab for this step, configure the settings described in this section.

Current operating system drive

Disables BitLocker on the current OS drive.

Specific drive

Disables BitLocker on a specific drive. Use the drop-down list to specify the drive where
BitLocker is disabled.

Resume protection after Windows has been restarted the specified
number of times

Use this option to specify the number of restarts to keep BitLocker disabled. Instead of
adding multiple instances of this step, set a value between 1 (default) and 15.

You can set and modify this behavior with the task sequence variables
OSDBitLockerRebootCount and OSDBitLockerRebootCountOverride.

<!-- p.383 -->

Download Package Content
Use this step to download any of the following package types:

     OS images
     OS upgrade packages
     Driver packages
     Packages
     Boot images Note 1

This step works well in a task sequence to upgrade an OS in the following scenarios:

     To use a single upgrade task sequence that can work with both x86 and x64
     platforms. Include two Download Package Content steps in the Prepare for
     Upgrade group. Specify conditions on the Options tab to detect the client
     architecture, and download only the appropriate OS upgrade package. Configure
     each Download Package Content step to use the same variable. Use the variable
     for the media path on the Upgrade Operating System step.

     To dynamically download an applicable driver package, use two Download
     Package Content steps with conditions to detect the appropriate hardware type
     for each driver package. Configure each Download Package Content step to use
     the same variable. Use the variable for the Staged content value in the Drivers
     section of the Upgrade Operating System step.

  ７ Note

  When you deploy a task sequence that contains this step, don't select Download all
  content locally before starting the task sequence or Access content directly from
  a distribution point for Deployment options on the Distribution Points page of
  the Deploy Software Wizard.

This step runs in either the full OS or Windows PE. The option to save the package in the
Configuration Manager client cache isn't supported in Windows PE.

  ７ Note

  The Download Package Content task isn't supported for use with stand-alone
  media. For more information, see Unsupported actions for stand-alone media.

To add this step in the task sequence editor, select Add, select Software, and select
Download Package Content.

<!-- p.384 -->

Cmdlets for Download Package Content
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepDownloadPackageContent
     New-CMTSStepDownloadPackageContent
     Remove-CMTSStepDownloadPackageContent
     Set-CMTSStepDownloadPackageContent

Properties for Download Package Content
On the Properties tab for this step, configure the settings described in this section.

Select package

Select the icon to choose the package to download. After you choose one package,
select the icon again to choose another package.

Place into the following location

Choose to save the package in one of the following locations:

     Task sequence working directory: This location is also referred to as the task
     sequence cache.

     Configuration Manager client cache: Use this option to store the content in the
     client cache. By default, this path is %WinDir%\ccmcache .

     Custom path: The task sequence engine first downloads the package to the task
     sequence working directory. It then moves the content to this path you specify.
     The task sequence engine appends the path with the package ID.

Save path as a variable

Save the package's path into a custom task sequence variable. Then use this variable in
another task sequence step.

Configuration Manager adds a numerical suffix to the variable name. For example, you
specify a variable of %MyContent% as a custom variable. It's the root for where the task
sequence stores all referenced content for this step. This content may contain multiple
packages. When you refer to the variable, add a numerical suffix. For the first package,
refer to %MyContent01% . When you refer to the variable in subsequent steps, such as

<!-- p.385 -->

Upgrade Operating System, use %MyContent02% or %MyContent03% , where the number
corresponds to the order that the Download Package Content step lists the packages.

If a package download fails, continue downloading other packages
in the list
If the task sequence fails to download a package, it starts to download the next package
in the list. This behavior applies to all packages in the step. The task sequence ignores
download failures for any referenced package.

Note 1: Use of boot images in the Download Package
Content step
If you configure the task sequence properties to Use a boot image, then adding a boot
image to this step is redundant. Only add a boot image to this step if it's not specified
on the properties of the task sequence.

Example use case
     A single task sequence to pre-download content:
        No associated boot image.
        Runs only in the full OS, likely without user interaction.
        Uses multiple Download Package Content steps with conditions. Depending
        upon the specific language and architecture, it downloads content to the client
        cache to prepare for the OS deployment task sequence.
        There's only one instance of this task sequence, with all of the possible content
        options.

     Multiple OS deployment task sequences:
        A normal OS deployment task sequence.
        Has a boot image referenced in its properties.
        There are multiple instances of this task sequence, with different boot images as
        needed by architecture and language

Enable BitLocker
BitLocker drive encryption provides low-level encryption of the contents of a disk
volume. Use this step to enable BitLocker encryption on at least two partitions on the
hard drive. The first active partition contains the Windows bootstrap code. Another
partition contains the OS. The bootstrap partition must remain unencrypted.

<!-- p.386 -->

To enable BitLocker on a drive while in Windows PE, use the Pre-provision BitLocker
step.

This step runs only in the full OS. It doesn't run in Windows PE.

To add this step in the task sequence editor, select Add, select Disks, and select Enable
BitLocker.

When you specify TPM Only, TPM and Startup Key on USB, or TPM and PIN, the
Trusted Platform Module (TPM) must be in the following state before you can run the
Enable BitLocker step:

        Enabled
        Activated
        Ownership Allowed

You can skip this step for computers that don't have a TPM or when the TPM isn't
enabled. This option makes it easier to manage the task sequence behavior on devices
that can't fully support BitLocker.

This step completes any remaining TPM initialization. The remaining actions don't
require physical presence or reboots. The Enable BitLocker step transparently completes
the following remaining TPM initialization actions, if necessary:

        Create endorsement key pair
        Create owner authorization value and escrow the recovery information
        Take ownership
        Create the storage root key, or reset if already present but incompatible

If you want the task sequence to wait for the Enable BitLocker step to complete the
drive encryption process, then select the Wait option. If you don't select the Wait
option, the drive encryption process happens in the background. The task sequence
immediately proceeds to the next step.

BitLocker can be used to encrypt multiple drives on a computer system, both OS and
data drives. To encrypt a data drive, first encrypt the OS drive and complete the
encryption process. This requirement is because the OS drive stores the key protectors
for the data drives. If you encrypt the OS and data drives in the same task sequence,
select the Wait option on the Enable BitLocker step for the OS drive.

If the hard drive is already encrypted, but BitLocker is disabled, then the Enable
BitLocker step re-enables the key protectors and completes quickly. Re-encryption of
the hard drive isn't necessary in this case.

<!-- p.387 -->

Variables for Enable BitLocker
Use the following task sequence variables with this step:

     OSDBitLockerPIN
     OSDBitLockerRecoveryPassword
     OSDBitLockerStartupKey
     OSDRecoveryKeyPollingFrequency (starting in version 2203)
     OSDRecoveryKeyPollingTimeout (starting in version 2203)

Cmdlets for Enable BitLocker
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepEnableBitLocker
     New-CMTSStepEnableBitLocker
     Remove-CMTSStepEnableBitLocker
     Set-CMTSStepEnableBitLocker

Properties for Enable BitLocker
On the Properties tab for this step, configure the settings described in this section.

Choose the drive to encrypt
Specifies the drive to encrypt. To encrypt the current OS drive, select Current operating
system drive. Then configure one of the following options for key management:

     TPM only: Select this option to use only Trusted Platform Module (TPM).

     Startup Key on USB only: Select this option to use a startup key stored on a USB
     flash drive. When you select this option, BitLocker locks the normal boot process
     until a USB device that contains a BitLocker startup key is attached to the
     computer.

     TPM and Startup Key on USB: Select this option to use TPM and a startup key
     stored on a USB flash drive. When you select this option, BitLocker locks the
     normal boot process until a USB device that contains a BitLocker startup key is
     attached to the computer.

     TPM and PIN: Select this option to use TPM and a personal identification number
     (PIN). When you select this option, BitLocker locks the normal boot process until
     the user provides the PIN.

<!-- p.388 -->

To encrypt a specific, non-OS data drive, select Specific drive. Then select the drive from
the list.

Disk encryption mode

Select one of the following encryption algorithms:

      AES_128
      AES_256
      XTS_AES256
      XTS_AES128

By default or if not specified, the step continues to use the default encryption method
for the OS version. If the step runs on a version of Windows that doesn't support the
specified algorithm, it falls back to the OS default. In this circumstance, the task
sequence engine sends status message 11911.

Use full disk encryption

By default, this step only encrypts used space on the drive. This default behavior is
recommended, as it's faster and more efficient. If your organization requires encrypting
the entire drive during setup, then enable this option. Windows Setup waits for the
entire drive to encrypt, which takes a long time, especially on large drives.

    Tip

   You can also use Configuration Manager to create and deploy BitLocker
   management policies. These policies use full disk encryption. To manage BitLocker
   on devices after the task sequence deploys the OS, enable this option. For more
   information, see Plan for BitLocker management.

Choose where to create the recovery key
      In Active Directory: BitLocker creates the recovery password and escrows it in
      Active Directory. This option requires that you extend Active Directory for BitLocker
      key escrow. BitLocker can then save the associated recovery information in Active
      Directory.

      The Configuration Manager database: Starting in version 2203, escrow the
      BitLocker recovery information for the OS volume to Configuration Manager. Use
      this option if you deploy policies for BitLocker management. Use this option

<!-- p.389 -->

      instead of Active Directory or waiting for the Configuration Manager client to
      receive BitLocker management policy after the task sequence. By escrowing the
      recovery information to Configuration Manager during the task sequence, it makes
      sure that the device is fully protected by BitLocker when the task sequence
      completes. This behavior allows for you to immediately recover the OS volume.

           ７ Note

           The client will only escrow its key to the Configuration Manager site if you
           configure one of the following options:

             Create and use a certificate to encrypt the site database for BitLocker
             management.

             Enable the BitLocker client management policy option to Allow recovery
             information to be stored in plain text.

           For more information, see Encrypt recovery data in the database.

To not create a password, select Do not create recovery key . Creating a password is the
recommended option.

  ７ Note

  If Configuration Manager can't escrow the key, by default this task sequence step
  fails.

Wait for BitLocker to complete the drive encryption process on all
drives before continuing task sequence execution
Select this option to allow BitLocker drive encryption to complete prior to running the
next step in the task sequence. If you select this option, BitLocker encrypts the entire
disk volume before the user is able to sign in to the computer.

The encryption process can take hours to complete when encrypting a large hard drive.
Not selecting this option allows the task sequence to proceed immediately.

Skip this step for computers that do not have a TPM or when TPM
is not enabled

<!-- p.390 -->

Select this option to skip drive encryption on a computer that doesn't contain a
supported or enabled TPM. For example, use this option when you deploy an OS to a
virtual machine. By default, this setting is disabled for the Enable BitLocker step. If you
enable this setting, and the device doesn't have a functional TPM, the task sequence
engine logs an error to smsts.log and sends status message 11912. The task sequence
continues past this step.

Format and Partition Disk
Use this step to format and partition a specified disk on the destination computer.

  ） Important

  Every setting you specify for this step applies to a single specified disk. To format
  and partition another disk on the destination computer, add an additional Format
  and Partition Disk step to the task sequence.

This step runs only in Windows PE. It doesn't run in the full OS.

To add this step in the task sequence editor, select Add, select Disks, and select Format
and Partition Disk.

Variables for Format and Partition Disk
Use the following task sequence variables with this step:

     OSDDiskIndex
     OSDGPTBootDisk
     OSDPartitions
     OSDPartitionStyle

Cmdlets for Format and Partition Disk
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepPartitionDisk
     New-CMTSStepPartitionDisk
     Remove-CMTSStepPartitionDisk
     Set-CMTSStepPartitionDisk
     New-CMTSPartitionSetting

<!-- p.391 -->

Properties for Format and Partition Disk
On the Properties tab for this step, configure the settings described in this section.

Disk Number

The physical disk number of the disk to format. The number is based on Windows disk
enumeration ordering.

In version 2010 and earlier, this number can't be larger than 99. In version 2103 and
later, the maximum number is 10,000. This change helps support storage area network
(SAN) scenarios.

Variable name to store disk number
Use a task sequence variable to specify the target disk to format. This variable option
supports more complex task sequences with dynamic behaviors. For example, a custom
script can detect the disk and set the variable based on the hardware type. Then you can
use multiple instances of this step to configure different hardware types and partitions.

If you select this property, enter a custom variable name. Add an earlier step in the task
sequence to set the value of this custom variable to an integer value for the physical
disk.

The following mock steps show one example:

        Run PowerShell Script: a custom script to collect target disks
          Sets myOSDisk to 1
          Sets myDataDisk to 2

        Format and Partition Disk for OS disk: specifies myOSDisk variable
          Configures disk 1 as the system disk

        Format and Partition Disk for data disk: specifies myDataDisk variable
          Configures disk 2 for raw storage

A variation of this example uses disk numbers and partitioning plans for different
hardware types.

  ７ Note

  You can still use the existing task sequence variable OSDDiskIndex. However, each
  instance of the Format and Partition Disk step uses the same index value. If you

<!-- p.392 -->

  want to programmatically set the disk number for multiple instances of this step,
  use this variable property.

Disk Type

The type of the disk to format. There are two options to select from the drop-down list:

      Standard (MBR): Master Boot Record
      GPT: GUID Partition Table

  ７ Note

  If you change the disk type from Standard (MBR) to GPT, and the partition layout
  contains an extended partition, the task sequence removes all extended and logical
  partitions from the layout. The task sequence editor prompts to confirm this action
  before changing the disk type.

Volume

Specific information about the partition or volume that the task sequence creates,
including the following attributes:

      Name
      Remaining disk space

To create a new partition, select New to launch the Partition Properties dialog box.
Specify the partition type and size, and if it's a boot partition. To modify an existing
partition, select the partition to be modified, and then select the Properties button. For
more information about how to configure hard drive partitions, see one of the following
articles:

      UEFI/GPT-based hard drive partitions
      BIOS/MBR-based hard drive partitions

To delete a partition, choose the partition, and then select Delete.

Install Application
This step installs the specified applications, or a set of applications defined by a dynamic
list of task sequence variables. When the task sequence runs this step, the application
installation begins immediately without waiting for a policy polling interval.

<!-- p.393 -->

The applications must meet the following criteria:

     The application must have a deployment type of Windows Installer or Script
     installer. Windows app package (.appx, .appxbundle, .msix, .msixbundle file types)
     deployment types aren't supported.

     It must run under the Local System account and not the user account.

     It must not interact with the desktop. The program must run silently or in an
     unattended mode.

     It must not initiate a restart on its own. The application must request a restart by
     using the standard restart code, 3010. This behavior makes sure that this step
     correctly handles the restart. If the application returns a 3010 exit code, the task
     sequence engine restarts the computer. After the restart, the task sequence
     automatically continues.

     If the application checks for running executable files, the task sequence will fail to
     install it. If you don't configure this step to continue on error, then the entire task
     sequence fails.

It's not supported to install applications during an OS deployment task sequence when
the device also has policies assigned for Windows Defender Application Control. In this
scenario, you can't use these applications after the task sequence completes. To work
around this timing issue, deploy the applications after the task sequence completes.

  ７ Note

  Starting in version 2107, when the following conditions are true, there's a seven-
  minute delay before this step:

       The task sequence is running from standalone media.
       The previous step was Restart Computer.
       The current Install Application step doesn't continue on error.

  In versions 2103 and earlier, the step would fail under these conditions. The task
  sequence didn't properly evaluate that the app install was successful.

When this step runs, the application checks the applicability of the requirement rules
and detection method on its deployment types. Based on the results of this check, the
application installs the applicable deployment type. If a deployment type contains
dependencies, the dependent deployment type is evaluated and installed as part of this
step. Application dependencies aren't supported for stand-alone media.

<!-- p.394 -->

  ７ Note

  To install an application that supersedes another application, the content files for
  the superseded application must be available. Otherwise this task sequence step
  fails. For example, Microsoft Visio 2010 is installed on a client or in a captured
  image. When the Install Application step installs Microsoft Visio 2013, the content
  files for Microsoft Visio 2010 (the superseded application) must be available on a
  distribution point. If Microsoft Visio isn't installed at all on a client or captured
  image, the task sequence installs Microsoft Visio 2013 without checking for the
  Microsoft Visio 2010 content files.

  If you retire a superseded app, and the new app is referenced in a task sequence,
  the task sequence fails to start. This behavior is by design: the task sequence
  requires all app references.

This task sequence step runs only in the full OS. It doesn't run in Windows PE.

To add this step in the task sequence editor, select Add, select Software, and select
Install Application.

Variables for Install Application
Use the following task sequence variables with this step:

     _TSAppInstallStatus
     SMSTSMPListRequestTimeoutEnabled
     SMSTSMPListRequestTimeout
     TSErrorOnWarning

  ７ Note

  If the client fails to retrieve the management point list from location services, use
  the SMSTSMPListRequestTimeoutEnabled and SMSTSMPListRequestTimeout task
  sequence variables. These variables specify how many milliseconds a task sequence
  waits before it retries installing an application. For more information, see Task
  sequence variables.

Cmdlets for Install Application
Manage this step with the following PowerShell cmdlets:

<!-- p.395 -->

     Get-CMTSStepInstallApplication
     New-CMTSStepInstallApplication
     Remove-CMTSStepInstallApplication
     Set-CMTSStepInstallApplication

Properties for Install Application
On the Properties tab for this step, configure the settings that are described in this
section.

Install the following applications

The task sequence installs these applications in the specified order.

Configuration Manager filters out any disabled applications, or any applications with the
following settings:

     Only when a user is logged on
     Run with user rights

These applications don't appear in the Select the application to install dialog box.

Install applications according to dynamic variable list
The task sequence installs applications using this base variable name. The base variable
name is for a set of task sequence variables defined for a collection or computer. These
variables specify the applications that the task sequence installs for that collection or
computer. Each variable name consists of its common base name plus a numerical suffix
starting at 01. The value for each variable must contain the name of the application and
nothing else.

For the task sequence to install applications by using a dynamic variable list, enable the
following setting on the General tab of the application Properties: Allow this
application to be installed from the Install Application task sequence action instead of
deploying manually.

  ７ Note

  You can't install applications by using a dynamic variable list for stand-alone media
  deployments.

<!-- p.396 -->

For example, to install a single application by using a task sequence variable called
AA01, specify the following variable:

                                                                             ﾉ   Expand table

 Variable Name                                   Variable Value

 AA01                                            Microsoft Office

To install two applications, specify the following variables:

                                                                             ﾉ   Expand table

 Variable Name                                   Variable Value

 AA01                                            Microsoft Lync

 AA02                                            Microsoft Office

The following conditions affect the applications installed by the task sequence:

        If the value of a variable contains any information other than the name of the
        application. The task sequence doesn't install the application, and the task
        sequence continues.

        If the task sequence doesn't find a variable with the specified base name and "01"
        suffix, the task sequence doesn't install any applications.

  ） Important

  These values are case-sensitive. For example, "install" is different than "Install". If
  you need to change the value, the task sequence editor doesn't detect a change of
  case. Make another edit at the same time, for example, modify the step description.

If an application fails, continue installing other applications in the
list

This setting specifies that the step continues when an individual application installation
fails. If you specify this setting, the task sequence continues regardless of any installation
errors. If you don't specify this setting, and the installation fails, the step immediately
ends.

<!-- p.397 -->

Clear application content from cache after installing
Delete the app content from the client cache after the step runs. This behavior is
beneficial on devices with small hard drives or when installing lots of large apps in
succession.

Options for Install Application

  ７ Note

  When you select Continue on error on the Options tab of this step, the task
  sequence continues when an application fails to install. When you don't enable this
  option, the task sequence fails, and doesn't install remaining applications.

Besides the default options, configure the following additional settings on the Options
tab of this task sequence step:

Retry this step if computer unexpectedly restarts
If one of the application installations unexpectedly restarts the computer, retry this step.
The step enables this setting by default with two retries. You can specify from one to five
retries.

Install Package
Use this step to install a software package as part of the task sequence. When this step
runs, the installation begins immediately without waiting for a policy polling interval.

The package must meet the following criteria:

      It must run under the Local System account and not a user account.

      It shouldn't interact with the desktop. The program must run silently or in an
      unattended mode.

      It must not initiate a restart on its own. The software must request a restart using
      the standard restart code, 3010. This behavior makes sure that the task sequence
      properly handles the restart. If the software does return a 3010 exit code, the task
      sequence engine restarts the computer. After the restart, the task sequence
      automatically continues.

<!-- p.398 -->

Programs that use the Run another program first option to install a dependent
program aren't supported when deploying an OS. If you enable the package option Run
another program first, and the dependent program already ran on the destination
computer, the dependent program runs and the task sequence continues. However, if
the dependent program hasn't already run on the destination computer, the task
sequence step fails.

This task sequence step runs only in the full OS. It doesn't run in Windows PE.

To add this step in the task sequence editor, select Add, select Software, and select
Install Package.

Known issue with Install Package step and standalone media
created at the central administration site
An error might occur if your task sequence includes the Install Package step and you
create the stand-alone media at a central administration site (CAS). The CAS doesn't
have the necessary client configuration policies. These policies are required to enable
the software distribution agent when the task sequence runs. The following error might
appear in the CreateTsMedia.log file: WMI method
SMS_TaskSequencePackage.GetClientConfigPolicies failed (0x80041001)

For stand-alone media that includes an Install Package step, create the stand-alone
media at a primary site that has the software distribution agent enabled.

Alternatively, use a custom Run PowerShell Script step. Add it after the Setup Windows
and ConfigMgr step and before the first Install Package step. The Run PowerShell
Script step runs the following commands to enable the software distribution agent
before the first Install Package step:

  PowerShell

  $namespace = "root\ccm\policy\machine\requestedconfig"
  $class = "CCM_SoftwareDistributionClientConfig"
  $classArgs = @{
      ComponentName = 'Enable SWDist'
      Enabled = 'true'
      LockSettings='TRUE'
      PolicySource='local'
      PolicyVersion='1.0'
      SiteSettingsKey='1'
  }
  Set-WmiInstance -Namespace $namespace -Class $class -Arguments $classArgs -
  PutType CreateOnly

<!-- p.399 -->

Variables for Install Package
Use the following task sequence variables with this step:

     OSDDoNotLogCommand

Cmdlets for Install Package
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepInstallSoftware
     New-CMTSStepInstallSoftware
     Remove-CMTSStepInstallSoftware
     Set-CMTSStepInstallSoftware

   Tip

  Use content pre-caching to download an applicable OS upgrade package before a
  user installs the task sequence. For more information, see Configure pre-cache
  content.

Properties for Install Package
On the Properties tab for this step, configure the settings described in this section.

Install a single software package
This setting specifies a Configuration Manager software package. The step waits until
the installation completes.

Install software packages according to dynamic variable list

The task sequence installs packages using this base variable name. The base variable
name is for a set of task sequence variables defined for a collection or computer. These
variables specify the packages that the task sequence installs for that collection or
computer. Each variable name consists of its common base name plus a numerical suffix
starting at 001. The value for each variable must contain a package ID and the name of
the software separated by a colon.

For the task sequence to install software by using a dynamic variable list, enable the
following setting on the Advanced tab of the package Properties: Allow this program

<!-- p.400 -->

to be installed from the Install Package task sequence without being deployed.

  ７ Note

  You can't install software packages by using a dynamic variable list for stand-alone
  media deployments.

For example, to install a single software package by using a task sequence variable
called AA001, you specify the following variable:

                                                                             ﾉ   Expand table

 Variable Name                                 Variable Value

 AA001                                         CEN00054:Install

To install three software packages, you would specify the following variables:

                                                                             ﾉ   Expand table

 Variable Name                          Variable Value

 AA001                                  CEN00054:Install

 AA002                                  CEN00107:Install Silent

 AA003                                  CEN00031:Install

The following conditions affect the packages installed by the task sequence:

     If you don't create the value of a variable in the correct format, or it doesn't specify
     a valid package ID and name, the software installation fails.

     If the package ID contains lowercase characters, the software installation fails.

     If the task sequence doesn't find a variable with the specified base name and "001"
     suffix, the task sequence doesn't install any packages. The task sequence
     continues.

  ） Important

  These values are case-sensitive. For example, "install" is different than "Install". If
  you need to change the value, the task sequence editor doesn't detect a change of
  case. Make another edit at the same time, for example, modify the step description.
