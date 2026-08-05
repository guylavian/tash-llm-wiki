---
title: "OS deployment documentation — pages 401-440"
type: reference
domain: sccm
slug: sccm-intune-configmgr-osd-p0401-0440
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-osd-p0401-0440
family: sccm
documentKind: "doc"
abstract: "If installation of a software package fails, continue installing other packages in the list This setting specifies that the step continues if an individual software package installation fails. If you specify this setting, the task sequence continues regardless of any installatio"
---

# OS deployment documentation — pages 401-440

<!-- p.401 -->

If installation of a software package fails, continue installing other
packages in the list

This setting specifies that the step continues if an individual software package
installation fails. If you specify this setting, the task sequence continues regardless of any
installation errors. If you don't specify this setting, and the installation fails, the step
immediately ends.

Retry this step if computer unexpectedly restarts

If one of the package installations unexpectedly restarts the computer, retry this step.
The step enables this setting by default with two retries. You can specify from one to five
retries.

Install Software Updates
Use this step to install software updates on the destination computer. The destination
computer isn't evaluated for applicable software updates until this task sequence step
runs. At that time, the destination computer is evaluated for software updates like any
other Configuration Manager client. For this step to install software updates, first deploy
the updates to a collection of which the target computer is a member.

  ） Important

  For best performance, install the latest version of the Windows Update Agent.

This task sequence step runs only in the full OS. It doesn't run in Windows PE.

To add this step in the task sequence editor, select Add, select Software, and select
Install Software Updates.

Variables for Install Software Updates
Use the following task sequence variables with this step:

      SMSInstallUpdateTarget
      SMSTSMPListRequestTimeoutEnabled
      SMSTSMPListRequestTimeout
      SMSTSSoftwareUpdateScanTimeout
      SMSTSWaitForSecondReboot

<!-- p.402 -->

  ７ Note

  If the client fails to retrieve the management point list from location services, use
  the SMSTSMPListRequestTimeoutEnabled and SMSTSMPListRequestTimeout
  variables. These variables specify how many milliseconds a task sequence waits
  before it retries installing an application or software update. For more information,
  see Task sequence variables.

Cmdlets for Install Software Updates
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepInstallUpdate
     New-CMTSStepInstallUpdate
     Remove-CMTSStepInstallUpdate
     Set-CMTSStepInstallUpdate

For more recommendations and a technical flow chart diagram for this step, see Install
Software Updates.

Properties for Install Software Updates
On the Properties tab for this step, configure the settings described in this section.

Required for installation - Mandatory software updates only

Select this option to install all mandatory software updates with administrator-defined
installation deadlines.

Available for installation - All software updates
Select this option to install all available software updates. First deploy these updates to a
collection of which the computer is a member. The task sequence installs all available
software updates on the destination computers.

Evaluate software updates from cached scan results

By default, this step uses cached scan results from the Windows Update Agent. Disable
this option to instruct the Windows Update Agent to download the latest catalog from

<!-- p.403 -->

the software update point. Enable this option when using a task sequence to capture
and build an OS image.

Many updates have dependencies. For example, install update ABC before update XYZ
appears as applicable. When you disable this setting, and deploy the task sequence to
many clients, they all connect to the software update point at the same time. This
behavior might result in performance issues during the process and download of the
update catalog. If deploying to many clients at once, use the default setting to use
cached scan results. If deploying to a small number of clients at once, uncheck this
option to ensure all software updates are installed on the client.

The SMSTSSoftwareUpdateScanTimeout variable controls the software updates scan
timeout during this step. The default value is 60 minutes. For more information, see Task
sequence variables.

Options for Install Software Updates
Besides the default options, configure the following additional settings on the Options
tab of this task sequence step:

Retry this step if computer unexpectedly restarts

If one of the updates unexpectedly restarts the computer, retry this step. The step
enables this setting by default with two retries. You can specify from one to five retries.

This option only applies to stand-alone task sequences. It doesn't work with OSD task
sequences that deploy an OS and utilize the Setup Windows and ConfigMgr task. For
OSD task sequences that deploy an OS and utilize the Setup Windows and ConfigMgr
task, use the SMSTSWaitForSecondReboot variable instead. For more information, see
Task sequence variables: SMSTSWaitForSecondReboot.

Join Domain or Workgroup
Use this step to add the destination computer to a workgroup or domain.

  ７ Note

  When a Microsoft Entra joined client runs an OS deployment task sequence, the
  client in the new OS won't automatically join Microsoft Entra ID. Even though it's
  not Microsoft Entra joined, the client is still managed.

<!-- p.404 -->

This task sequence step runs only in the full OS. It doesn't run in Windows PE.

To add this step in the task sequence editor, select Add, select General, and select Join
Domain or Workgroup.

Variables for Join Domain or Workgroup
Use the following task sequence variables with this step:

     OSDJoinAccount
     OSDJoinDomainName
     OSDJoinDomainOUName
     OSDJoinPassword
     OSDJoinSkipReboot
     OSDJoinType
     OSDJoinWorkgroupName

Cmdlets for Join Domain or Workgroup
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepJoinDomainWorkgroup
     New-CMTSStepJoinDomainWorkgroup
     Remove-CMTSStepJoinDomainWorkgroup
     Set-CMTSStepJoinDomainWorkgroup

Properties for Join Domain or Workgroup
On the Properties tab for this step, configure the settings described in this section.

Join a workgroup
Select this option to have the destination computer join the specified workgroup. If the
computer is currently a member of a domain, selecting this option causes the computer
to reboot.

Join a domain

Select this option to have the destination computer join the specified domain.

Optionally, enter or browse for an organizational unit (OU) in the specified domain for
the computer to join. If the computer is currently a member of some other domain or a

<!-- p.405 -->

workgroup, this option causes the computer to reboot. If the computer is already a
member of another OU, since Active Directory Domain Services doesn't allow changing
the OU via this method, Windows Setup ignores this setting.

Enter the account which has permission to join the domain
Select Set to enter the username and password for an account with permissions to join
the domain. Enter the account in the format: Domain\account . For more information on
the task sequence domain joining account, see Accounts.

Prepare ConfigMgr Client for Capture
Use this step to remove or configure the Configuration Manager client on the reference
computer. This action prepares the computer for capture as part of the imaging process.

This step completely removes the Configuration Manager client, instead of only
removing key information. When the task sequence deploys the captured OS image, it
installs a new Configuration Manager client each time.

   Tip

  By default, the task sequence engine only removes the client during the Build and
  capture a reference operating system image task sequence. The task sequence
  engine doesn't remove the client during other capture methods, such as capture
  media or a custom task sequence. You can overide this behavior for an OS
  deployment task sequence. Set the task sequence variable
  SMSTSUninstallCCMClient to TRUE before the Prepare ConfigMgr Client for
  Capture step. This variable and behavior only applies to OS deployment task
  sequences. It removes the client after the next restart of the device.

This task sequence step runs only in the full OS. It doesn't run in Windows PE.

To add this step in the task sequence editor, select Add, select Images, and select
Prepare ConfigMgr Client for Capture.

Variables for Prepare ConfigMgr Client for Capture
Use the following task sequence variables with this step:

     SMSTSUninstallCCMClient

<!-- p.406 -->

Cmdlets for Prepare ConfigMgr Client for Capture
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepPrepareConfigMgrClient
     New-CMTSStepPrepareConfigMgrClient
     Remove-CMTSStepPrepareConfigMgrClient
     Set-CMTSStepPrepareConfigMgrClient

Prepare Windows for Capture
Use this step to specify the Sysprep options when capturing an OS image on the
reference computer. This step runs Sysprep, and then reboots the computer into the
Windows PE boot image specified for the task sequence. This action fails if the reference
computer is joined to a domain.

This step runs only in the full OS. It doesn't run in Windows PE.

To add this step in the task sequence editor, select Add, select Images, and select
Prepare Windows for Capture.

Variables for Prepare Windows for Capture
Use the following task sequence variables with this step:

     OSDKeepActivation
     OSDTargetSystemRoot

Cmdlets for Prepare Windows for Capture
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepPrepareWindows
     New-CMTSStepPrepareWindows
     Remove-CMTSStepPrepareWindows
     Set-CMTSStepPrepareWindows

Properties for Prepare Windows for Capture
On the Properties tab for this step, configure the settings described in this section.

<!-- p.407 -->

Automatically build mass storage driver list
Select this option to have Sysprep automatically build a list of mass storage drivers from
the reference computer. This option enables the Build Mass Storage Drivers option in
the sysprep.inf file on the reference computer. For more information about this setting,
see the Sysprep documentation.

  ） Important

  This option was only applicable in Windows XP. It's no longer applicable in any
  currently supported versions of Windows.

Do not reset activation flag
Select this option to prevent Sysprep from resetting the product activation flag.

Shut down the computer after running this action
This option instructs Sysprep to shutdown the computer instead of its default restart
behavior.

The Windows Autopilot for existing devices task sequence uses this step with this
option.

     If you want the task sequence to refresh the device and then immediately start
     OOBE for Autopilot, leave this option off.

     Enable this option to shut down the device after imaging. Then you can deliver the
     device to a user, who starts OOBE with Autopilot when they turn it on for the first
     time.

  ） Important

  Don't use the Prepare Windows for Capture task with Windows Autopilot for
  existing devices task sequences. The Sysprep.exe command line used during the
  Prepare Windows for Capture task uses the /Generalize parameter. The
  /Generalize parameter removes the AutopilotConfigurationFile.json file used by

  Windows Autopilot, causing the Windows Autopilot deployment not to run during
  the out-of-box (OOBE) experience. Instead, where the Prepare Windows for
  Capture task normally runs, add a Run Command Line task that runs the following
  Sysprep.exe command instead:

<!-- p.408 -->

     Windows Command Prompt

     C:\Windows\System32\sysprep\sysprep.exe /oobe /reboot

  For more information, see Modify the task sequence to account for Sysprep
  command line configuration and Windows Autopilot for existing devices doesn't
  work.

Pre-provision BitLocker
Use this step to enable BitLocker on a drive while in Windows PE. By default, only the
used drive space is encrypted, so encryption times are much faster. You apply the key
management options by using the Enable BitLocker step after the OS installs.

  ） Important

  Pre-provisioning BitLocker requires that the computer has a supported and enabled
  Trusted Platform Module (TPM).

This step runs only in Windows PE. It doesn't run in the full OS.

To add this step in the task sequence editor, select Add, select Disks, and select Pre-
provision BitLocker.

Cmdlets for Pre-provision BitLocker
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepOfflineEnableBitLocker
     New-CMTSStepOfflineEnableBitLocker
     Remove-CMTSStepOfflineEnableBitLocker
     Set-CMTSStepOfflineEnableBitLocker

Properties for Pre-provision BitLocker
On the Properties tab for this step, configure the settings described in this section.

Apply BitLocker to the specified drive

<!-- p.409 -->

Specify the drive for which you want to enable BitLocker. BitLocker only encrypts the
used space on the drive.

Disk encryption mode (Pre-provision BitLocker)

Select one of the following encryption algorithms:

     AES_128
     AES_256
     XTS_AES256
     XTS_AES128

By default or if not specified, the step continues to use the default encryption method
for the OS version. If the step runs on a version of Windows that doesn't support the
specified algorithm, it falls back to the OS default. In this circumstance, the task
sequence engine sends status message 11911.

Use full disk encryption (Pre-provision BitLocker)

By default, this step only encrypts used space on the drive. This default behavior is
recommended, as it's faster and more efficient. If your organization requires encrypting
the entire drive during setup, then enable this option. Windows Setup waits for the
entire drive to encrypt, which takes a long time, especially on large drives.

Skip this step for computers that do not have a TPM or when TPM
is not enabled (Pre-provision BitLocker)

Select this option to skip drive encryption on a computer that doesn't contain a
supported or enabled TPM. For example, use this option when you deploy an OS to a
virtual machine. By default, this setting is enabled for the Pre-provision BitLocker step.
The step fails on a device without a TPM or a TPM that doesn't initialize. If the device
doesn't have a functional TPM, the task sequence engine logs a warning to smsts.log
and sends status message 11912.

Release State Store
Use this step to notify the state migration point that the capture or restore action is
complete. Use this step in conjunction with the Request State Store, Capture User State,
and Restore User State steps. You use these steps to migrate user state data using a
state migration point and the User State Migration Tool (USMT).

<!-- p.410 -->

For more information about managing the user state when deploying operating
systems, see Manage user state.

If you use the Request State Store step to request access to a state migration point to
capture user state, this step notifies the state migration point that the capture process is
complete. The state migration point then marks the user state data as available for
restore. The state migration point sets the access control permissions for the user state
data so that only the restoring computer has read-only access.

If you use the Request State Store step to request access to a state migration point to
restore user state, this step notifies the state migration point that the restore process is
complete. The state migration point then activates its configured data retention settings.

  ） Important

  Set the Continue on Error option for any steps between the Request State Store
  and Release State Store steps. Every Request State Store step must have a
  matching Release State Store step.

This step runs only in the full OS. It doesn't run in Windows PE.

To add this step in the task sequence editor, select Add, select User State, and select
Release State Store.

Variables for Release State Store
Use the following task sequence variables with this step:

     OSDStateStorePath

Cmdlets for Release State Store
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepReleaseStateStore
     New-CMTSStepReleaseStateStore
     Remove-CMTSStepReleaseStateStore
     Set-CMTSStepReleaseStateStore

Properties for Release State Store
This step doesn't require any settings on the Properties tab.

<!-- p.411 -->

Request State Store
Use this step to request access to a state migration point when capturing or restoring
state.

For more information about managing the user state when deploying operating
systems, see Manage user state.

Use this step in conjunction with the Release State Store, Capture User State, and
Restore User State steps. You use these steps to migrate computer state using a state
migration point and the User State Migration Tool (USMT).

  ７ Note

  When creating a new state migration point, user state storage isn't available for up
  to one hour. To expedite availability, adjust any property settings on the state
  migration point to trigger a site control file update.

This step runs in the full OS and in Windows PE for offline USMT.

To add this step in the task sequence editor, select Add, select User State, and select
Request State Store.

Variables for Request State Store
Use the following task sequence variables with this step:

         OSDStateFallbackToNAA
         OSDStateSMPRetryCount
         OSDStateSMPRetryTime
         OSDStateStorePath

Cmdlets for Request State Store
Manage this step with the following PowerShell cmdlets:

         Get-CMTSStepRequestStateStore
         New-CMTSStepRequestStateStore
         Remove-CMTSStepRequestStateStore
         Set-CMTSStepRequestStateStore

Properties for Request State Store

<!-- p.412 -->

On the Properties tab for this step, configure the settings described in this section.

Capture state from the computer
Find a state migration point that meets the minimum requirements as configured in the
state migration point settings. For example, Maximum number of clients and Minimum
amount of free disk space. This option doesn't guarantee sufficient space is available at
the time of state migration. This option requests access to the state migration point for
the purpose of capturing the user state and settings from a computer.

If the Configuration Manager site has multiple active state migration points, this step
finds a state migration point with available disk space. The task sequence queries the
management point for a list of state migration points, and then evaluates each until it
finds one that meets the minimum requirements.

Restore state from another computer

Request access to a state migration point to restore previously captured user state and
settings to a destination computer.

If there are multiple state migration points, this step finds the state migration point that
has the state for the destination computer.

Number of retries

The number of times that this step tries to find an appropriate state migration point
before failing.

Retry delay (in seconds)
The amount of time in seconds that the task sequence step waits between retry
attempts.

If computer account fails to connect to a state store, use the
network access account

If the task sequence can't access the state migration point using the computer account,
it uses the network access account credentials to connect. This option is less secure
because other computers could use the network access account to access the stored
state. This option might be necessary if the destination computer isn't domain joined.

<!-- p.413 -->

Restart Computer
Use this step to restart the computer running the task sequence. After the restart, the
computer automatically continues with the next step in the task sequence.

This step can be run in either the full OS or Windows PE.

To add this step in the task sequence editor, select Add, select General, and select
Restart Computer.

Variables for Restart Computer
Use the following task sequence variables with this step:

     SMSRebootMessage
     SMSRebootTimeout

Cmdlets for Restart Computer
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepReboot
     New-CMTSStepReboot
     Remove-CMTSStepReboot
     Set-CMTSStepReboot

Properties for Restart Computer
On the Properties tab for this step, configure the settings described in this section.

The boot image assigned to this task sequence
Select this option for the destination computer to use the boot image assigned to the
task sequence. The task sequence uses the boot image to run subsequent steps in
Windows PE.

The currently installed default operating system
Select this option for the destination computer to reboot into the installed OS.

Notify the user before restarting

<!-- p.414 -->

Select this option to display a notification to the user before the destination computer
restarts. The step selects this option by default.

Notification message

Enter a notification message to display to the user before the destination computer
restarts.

Message display time-out
Specify the amount of time in seconds before the destination computer restarts. The
default is 60 seconds.

Restore User State
Use this step to initiate the User State Migration Tool (USMT) to restore user state and
settings to the destination computer. You use this step in conjunction with the Capture
User State step.

For more information about managing the user state when deploying operating
systems, see Manage user state.

Use this step with the Request State Store and Release State Store steps to save or
restore the state settings with a state migration point. This option always decrypts the
USMT state store by using an encryption key that Configuration Manager generates and
manages.

Starting in version 2103, this step and the Capture User State step use the current
highest supported encryption algorithm, AES 256.

  ） Important

  If you have any active user state migrations, before you update the Configuration
  Manager client on those devices, restore the user state. Otherwise, the updated
  client will fail to restore the user state when it tries to use a different encryption
  algorithm. If necessary, you can manually restore the user state and explicitly use
  the USMT parameter /decrypt:3DES .

The Restore User State step provides control over a limited subset of the most
commonly used USMT options. Specify additional command-line options with the
OSDMigrateAdditionalRestoreOptions variable.

<!-- p.415 -->

  ） Important

  If you're using this step for a purpose unrelated to an OS deployment scenario, add
  the Restart Computer step immediately following the Restore User State step.

This step runs only in the full OS. It doesn't run in Windows PE.

To add this step in the task sequence editor, select Add, select User State, and select
Restore User State.

Variables for Restore User State
Use the following task sequence variables with this step:

     _OSDMigrateUsmtRestorePackageID
     OSDMigrateAdditionalRestoreOptions
     OSDMigrateContinueOnRestore
     OSDMigrateEnableVerboseLogging
     OSDMigrateLocalAccounts
     OSDMigrateLocalAccountPassword
     OSDStateStorePath

Cmdlets for Restore User State
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepRestoreUserState
     New-CMTSStepRestoreUserState
     Remove-CMTSStepRestoreUserState
     Set-CMTSStepRestoreUserState

Properties for Restore User State
On the Properties tab for this step, configure the settings described in this section.

User state migration tool package
Specify the package that contains the version of USMT for this step to use. This package
doesn't require a program. When the step runs, the task sequence uses the version of
USMT in the specified package. Specify a package containing the 32-bit or 64-bit

<!-- p.416 -->

version of USMT. The architecture of USMT depends upon the architecture of the OS to
which the task sequence is restoring state.

Restore all captured user profiles with standard options

Restores the captured user profiles with the standard options. To customize the options
that USMT restores, select Customize user profile capture.

Customize how user profiles are restored
Allows you to customize the files that you want to restore to the destination computer.
Select Files to specify the configuration files in the USMT package you want to use for
restoring the user profiles. To add a configuration file, enter the name of the file in the
Filename box, and then select Add. The Files pane lists the configuration files that USMT
uses. The .xml file you specify defines which user file USMT restores.

Restore local computer user profiles

Restores the local computer user profiles. These profiles aren't for domain users. Assign
new passwords to the restored local user accounts. USMT can't migrate the original
passwords. Enter the new password in the Password box, and confirm the password in
the Confirm Password box.

Continue if some files cannot be restored

Continues restoring user state and settings even if USMT is unable to restore some files.
The step enables this option by default. If you disable this option, and USMT encounters
errors while restoring files, this step fails immediately. USMT doesn't restore all files.

Enable verbose logging

Enable this option to generate more detailed log file information. When restoring state,
the task sequence by default generates Loadstate.log in the task sequence log folder,
%WinDir%\ccm\logs .

Run Command Line
Use this step to run the specified command line.

The command being run must meet the following criteria:

<!-- p.417 -->

     It shouldn't interact with the desktop. The command must run silently or in an
     unattended mode.

     It must not initiate a restart on its own. The command must request a restart using
     the standard restart code, 3010. This behavior makes sure that the task sequence
     properly handles the restart. If the command does return a 3010 exit code, the task
     sequence engine restarts the computer. After the restart, the task sequence
     automatically continues.

This step can be run in the full OS or Windows PE.

To add this step in the task sequence editor, select Add, select General, and select Run
Command Line.

Variables for Run Command Line
Use the following task sequence variables with this step:

     OSDDoNotLogCommand
     SMSTSDisableWow64Redirection
     SMSTSRunCommandLineUserName
     SMSTSRunCommandLineUserPassword
     SMSTSRunCommandLineAsUser
     WorkingDirectory

Cmdlets for Run Command Line
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepRunCommandLine
     New-CMTSStepRunCommandLine
     Remove-CMTSStepRunCommandLine
     Set-CMTSStepRunCommandLine

Properties for Run Command Line
On the Properties tab for this step, configure the settings described in this section.

Command line

Specifies the command line that the task sequence runs. This field is required. Include
file name extensions, for example, .vbs and .exe. Include all required settings files and

<!-- p.418 -->

command-line options.

If you don't specify the file name extension, Configuration Manager tries .com, .exe, and
.bat. If the file name has an extension that's not an executable type, Configuration
Manager tries to apply a local association. For example, if the command line is
readme.gif, Configuration Manager starts the application specified on the destination
computer for opening .gif files.

Examples:

setup.exe /a

cmd.exe /c copy Jan98.dat c:\sales\Jan98.dat

  ７ Note

  To run successfully, precede command-line actions with the cmd.exe /c command.
  Example of these actions include output redirection, piping, and copy commands.

Output to task sequence variable

Use this setting to save the command output to a custom task sequence variable.

  ７ Note

  Configuration Manager limits this output to the last 1000 characters.

Disable 64-bit file system redirection

By default, 64-bit operating systems use the WOW64 file system redirector to run
command lines. This behavior is to properly find 32-bit versions of OS executables and
libraries. Select this option to disable the use of the WOW64 file system redirector.
Windows runs the command using native 64-bit versions of OS executables and
libraries. This option has no effect when running on a 32-bit OS.

Start in
Specifies the executable folder for the program, up to 127 characters. This folder can be
an absolute path on the destination computer or a path relative to the distribution point
folder that contains the package. This field is optional.

<!-- p.419 -->

Examples:

c:\officexp

i386

  ７ Note

  The Browse button browses the local computer for files and folders. Anything you
  select must also exist on the destination computer. It must exist in the same
  location and with the same file and folder names.

Package

When you specify files or programs on the command line that aren't already present on
the destination computer, select this option to specify the Configuration Manager
package that contains the necessary files. The package doesn't require a program. If the
specified files exist on the destination computer, this option isn't required.

Time-out

Specifies a value that represents how long Configuration Manager allows the command
line to run. This value can be from one minute to 999 minutes. The default value is 15
minutes. This option is disabled by default.

  ） Important

  If you enter a value that doesn't allow enough time for the specified command to
  complete successfully, this step fails. The entire task sequence could fail depending
  on step or group conditions. If the time-out expires, Configuration Manager
  terminates the command-line process.

Run this step as the following account

Specifies that the command line is run as a Windows user account other than the Local
System account.

  ７ Note

<!-- p.420 -->

  To run simple scripts or commands with another account after installing the OS,
  first add the account to the computer. Additionally, you may need to restore
  Windows user profiles to run more complex programs, such as a Windows Installer.

Account
Specifies the Windows user account this step uses to run the command line. The
command line runs with the permissions of the specified account. Select Set to specify
the local user or domain account. For more information on the task sequence run-as
account, see Accounts.

  ） Important

  If this step specifies a user account and runs in Windows PE, the action fails. You
  can't join Windows PE to a domain. The smsts.log file records this failure.

Options for Run Command Line
Besides the default options, configure the following additional settings on the Options
tab of this task sequence step:

Success codes
Include other exit codes from the script that the step should evaluate as success.

Run PowerShell Script
Use this step to run the specified Windows PowerShell script.

The script must meet the following criteria:

     It shouldn't interact with the desktop. The script must run silently or in an
     unattended mode.

     It must not initiate a restart on its own. The script must request a restart using the
     standard restart code, 3010. This behavior makes sure that the task sequence
     properly handles the restart. If the script does return a 3010 exit code, the task
     sequence engine restarts the computer. After the restart, the task sequence
     automatically continues.

<!-- p.421 -->

     Use signed PowerShell scripts in Unicode format. ANSI format, which is the default,
     doesn't work with this step.

This step can be run in the full OS or Windows PE. To run this step in Windows PE,
enable PowerShell in the boot image. Enable the WinPE-PowerShell component from
the Optional Components tab in the properties for the boot image. For more
information about how to modify a boot image, see Manage boot images.

  ７ Note

  PowerShell isn't enabled by default on Windows Embedded operating systems.

  ２ Warning

  Some antimalware software may inadvertently trigger events for this task sequence
  step. To allow these scripts to run without interference, configure the antimalware
  software to exclude %windir%\temp\smstspowershellscripts .

To add this step in the task sequence editor, select Add, select General, and select Run
PowerShell Script.

Variables for Run PowerShell Script
Use the following task sequence variables with this step:

     OSDLogPowerShellParameters
     SMSTSRunPowerShellAsUser
     SMSTSRunPowerShellUserName
     SMSTSRunPowerShellUserPassword

Cmdlets for Run PowerShell Script
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepRunPowerShellScript
     New-CMTSStepRunPowerShellScript
     Remove-CMTSStepRunPowerShellScript
     Set-CMTSStepRunPowerShellScript

Properties for Run PowerShell Script

<!-- p.422 -->

On the Properties tab for this step, configure the settings described in this section.

Package
Specify the Configuration Manager package that contains the PowerShell script. One
package can contain multiple PowerShell scripts.

Script name

Specifies the name of the PowerShell script to run. This field is required.

Enter a PowerShell script

Directly enter Windows PowerShell code in this step. This feature lets you run
PowerShell commands during a task sequence without first creating and distributing a
package with the script.

When you add or edit a script, the PowerShell script window provides the following
actions:

        Edit the script directly

        Open an existing script from file

        Browse to an existing approved script in Configuration Manager

Parameters
Specifies the parameters passed to the PowerShell script. These parameters are the
same as the PowerShell script parameters on the command line.

Provide parameters consumed by the script, not for the Windows PowerShell command
line.

The following example contains valid parameters:

-MyParameter1 MyValue1 -MyParameter2 MyValue2

The following example contains invalid parameters. The first two items are Windows
PowerShell command-line parameters (-NoLogo and -ExecutionPolicy Unrestricted).
The script doesn't consume these parameters.

<!-- p.423 -->

-NoLogo -ExecutionPolicy Unrestricted -File MyScript.ps1 -MyParameter1 MyValue1 -
MyParameter2 MyValue2

If a parameter value includes a special character or a space, use single quotation marks
( ' ) around the value. Using double quotation marks ( " ) may cause the task sequence
step to incorrectly process the parameter.

For example: -Arg1 '%TSVar1%' -Arg2 '%TSVar2%'

You can also set this property to a variable. For example, if you specify
%MyScriptVariable% , when the task sequence runs the script, it adds the value of this

custom variable to the PowerShell command line.

PowerShell execution policy

Determine which PowerShell scripts (if any) you allow to run on the computer. Choose
one of the following execution policies:

     AllSigned: Only run scripts signed by a trusted publisher.

     Undefined: Don't define any execution policy.

     Bypass: Load all configuration files and run all scripts. If you download an unsigned
     script from the internet, Windows PowerShell doesn't prompt for permission
     before running the script.

  ） Important

  PowerShell 1.0 doesn't support Undefined and Bypass execution policies.

Output to task sequence variable

Save the script output to a custom task sequence variable.

  ７ Note

  Configuration Manager limits this output to the last 1000 characters.

For an example of how to use this step property, see How to set variables.

Start in

<!-- p.424 -->

Specify the starting folder for the script, up to 127 characters. This folder can be an
absolute path on the destination computer or a path relative to the distribution point
folder that contains the package. This field is optional.

  ７ Note

  The Browse button browses the local computer for files and folders. Anything you
  select must also exist on the destination computer. It must exist in the same
  location and with the same file and folder names.

Time-out

Specify a value that represents how long Configuration Manager allows the PowerShell
script to run. This value can be from one minute to 999 minutes. The default value is 15
minutes. This option is disabled by default.

  ） Important

  If you enter a value that doesn't allow enough time for the specified script to
  complete successfully, this step fails. The entire task sequence could fail depending
  on step or group conditions. If the time-out expires, Configuration Manager
  terminates the PowerShell process.

Run this step as the following account

Specify that the PowerShell script is run as a Windows user account other than the Local
System account.

  ７ Note

  To run simple scripts or commands with another account after installing the OS,
  first add the account to the computer. Additionally, you may need to restore
  Windows user profiles to run more complex actions.

Account

Specify the Windows user account this step uses to run the PowerShell script. The
specified account must be a local administrator on the system and the script runs with

<!-- p.425 -->

the permissions of this account. Select Set to specify the local user or domain account.
For more information on the task sequence run-as account, see Accounts.

  ） Important

  If this step specifies a user account and runs in Windows PE, the action fails. You
  can't join Windows PE to a domain. The smsts.log file records this failure.

Options for Run PowerShell Script
Besides the default options, configure the following additional settings on the Options
tab of this task sequence step:

Success codes

Include other exit codes from the script that the step should evaluate as success.

Run Task Sequence
This step runs another task sequence. It creates a parent-child relationship between the
task sequences. With child task sequences, you can create more modular, reusable task
sequences.

To add this step in the task sequence editor, select Add, select General, and select Run
Task Sequence.

Specifications and limitations for Run Task Sequence
Consider the following points when you add a child task sequence to a task sequence:

     The parent and child task sequences are effectively combined into a single policy
     that the client runs.

     The environment is global. If the parent task sequence sets a variable, and then the
     child task sequence changes that variable, it retains the latest value. If the child
     task sequence creates a new variable, it's available for the rest of the parent task
     sequence.

     Status messages are sent per normal for a single task sequence operation.

<!-- p.426 -->

     The task sequence writes entries to the smsts.log file, with new log entries that
     make it clear when a child task sequence starts.

     You can't select a task sequence with a boot image reference. For any deployment
     that requires a boot image, specify it on the parent task sequence.

     If a child task sequence is disabled, the deployment fails. You can't use the
     Continue on error option to work around this limitation.

     If a child task sequence contains steps that are considered high impact, Software
     Center doesn't detect it and show the high-impact notification. Modify the
     properties of the parent task sequence, on the User Notification tab, to specify that
     This is a high-impact task sequence.

     If a child task sequence has a missing package reference, viewing the parent task
     sequence doesn't detect this state. If you edit the parent task sequence, it detects
     any missing references in child task sequences when you make changes to the
     parent.

Cmdlets for Run Task Sequence
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepRunTaskSequence
     New-CMTSStepRunTaskSequence
     Remove-CMTSStepRunTaskSequence
     Set-CMTSStepRunTaskSequence

Properties for Run Task Sequence
On the Properties tab for this step, configure the settings described in this section.

Select task sequence to run
Select Browse to select the child task sequence. The Select a Task Sequence dialog box
doesn't display the parent task sequence.

Set Dynamic Variables
Use this step to perform the following actions:

<!-- p.427 -->

   1. Gather information from the computer and its environment. Then set specified task
     sequence variables with the information.

   2. Evaluate defined rules. Set task sequence variables based on the rules that evaluate
     to true.

This step can be run in either the full OS or Windows PE.

To add this step in the task sequence editor, select Add, select General, and select Set
Dynamic Variables.

Variables for Set Dynamic Variables
The task sequence automatically sets the following read-only task sequence variables:

     _SMSTSMake
     _SMSTSModel
     _SMSTSMacAddresses
     _SMSTSIPAddresses
     _SMSTSSerialNumber
     _SMSTSAssetTag
     _SMSTSUUID

Cmdlets for Set Dynamic Variables
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepSetDynamicVariable
     New-CMTSStepSetDynamicVariable
     Remove-CMTSStepSetDynamicVariable
     Set-CMTSStepSetDynamicVariable
     New-CMTSRule

Properties for Set Dynamic Variables
On the Properties tab for this step, configure the settings described in this section.

Dynamic rules and variables
To set a dynamic variable for use in the task sequence, add a rule. Then set a value for
each variable specified in the rule. Additionally, add one or more variables without
adding a rule. When you add a rule, choose from the following categories:

<!-- p.428 -->

     Computer: Evaluate values for hardware asset tag, UUID, serial number, or MAC
     address. Set multiple values as necessary. If any value is true, then the rule
     evaluates as true. For example, the following rule evaluates as true if the device
     serial number is 5892087 and the MAC address is 22-A4-5A-13-78-26:

      IF Serial Number = 5892087 OR MAC address = 26-78-13-5A-A4-22 THEN

     Location: Evaluate values for the default network gateway

     Make and Model: Evaluate values for the make and model of a computer. Both the
     make and model must evaluate to true for the rule to evaluate to true.

     Specify an asterisk ( * ) and question mark ( ? ) as wild cards characters. The asterisk
     matches multiple characters and the question mark matches a single character. For
     example, the string DELL*900? matches both DELL-ABC-9001 and DELL9009 .

     Task Sequence Variable: Add a task sequence variable, condition, and value to
     evaluate. The conditions are the same as for step conditions. The rule evaluates to
     true when the value set for the variable meets the specified condition.

     Specify one or more variables to set for a rule that evaluates to true, or set
     variables without using a rule. Select an existing variable, or create a custom
     variable.

        Existing task sequence variables: Select one or more variables from a list of
        existing task sequence variables. Array variables aren't available to select.

        Custom task sequence variables: Define a custom task sequence variable. You
        can also specify an existing task sequence variable. This setting is useful to
        specify an existing variable array, such as OSDAdapter, since variable arrays
        aren't in the list of existing task sequence variables.

After you select the variables for a rule, provide a value for each variable. The variable is
set to the specified value when the rule evaluates to true. For each variable, you can
select Do not display this value to hide the value of the variable. By default, some
existing variables hide values, such as the OSDCaptureAccountPassword variable.

  ） Important

  When you import a task sequence with the Set Dynamic Variables step,
  Configuration Manager removes any variable values marked as Do not display this
  value. After you import the task sequence, re-enter the value for the dynamic
  variable.

<!-- p.429 -->

When you use the option Do not display this value, the value of the variable isn't
displayed in the task sequence editor. The task sequence log file (smsts.log) or the task
sequence debugger won't show the variable value either. The variable can still be used
by the task sequence when it runs. If you no longer want these variables to be hidden,
delete them first. Then redefine the variables without selecting the option to hide them.

  ２ Warning

  If you include variables in the Run Command Line step's command line, the task
  sequence log file displays the full command line including the variable values. To
  prevent potentially sensitive data from appearing in the log file, set the task
  sequence variable OSDDoNotLogCommand to TRUE .

Set Task Sequence Variable
Use this step to set the value of a variable that's used with the task sequence.

This step can be run in either the full OS or Windows PE.

To add this step in the task sequence editor, select Add, select General, and select Set
Task Sequence Variable.

Variables for Set Task Sequence Variable
Task sequence variables are read by task sequence actions and specify the behavior of
those actions. For more information about specific task sequence variables and how to
use them, see the following articles:

     How to use task sequence variables
     Task sequence variables

Cmdlets for Set Task Sequence Variable
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepSetVariable
     New-CMTSStepSetVariable
     Remove-CMTSStepSetVariable
     Set-CMTSStepSetVariable

<!-- p.430 -->

Properties for Set Task Sequence Variable
On the Properties tab for this step, configure the settings described in this section.

Task sequence variable

Specify the name of a task sequence built-in or action variable, or specify your own
user-defined variable name.

Do not display this value

Enable this option to mask sensitive data stored in task sequence variables. For example,
when specifying a password.

  ７ Note

  Enable this option and then set the value of the task sequence variable. Otherwise
  the variable value isn't set as you intend, which may cause unexpected behaviors
  when the task sequence runs.

When you use the option Do not display this value, the value of the variable isn't
displayed in the task sequence editor. The task sequence log file (smsts.log) or the task
sequence debugger won't show the variable value either. The variable can still be used
by the task sequence when it runs. If you no longer want this variable to be hidden,
delete it first. Then redefine the variable without selecting the option to hide it.

  ２ Warning

  If you include variables in the Run Command Line step's command line, the task
  sequence log file displays the full command line including the variable values. To
  prevent potentially sensitive data from appearing in the log file, set the task
  sequence variable OSDDoNotLogCommand to TRUE .

Value

The task sequence sets the variable to this value. Set this task sequence variable to the
value of another task sequence variable with the syntax %varname% .

Setup Windows and ConfigMgr

<!-- p.431 -->

Use this step to perform the transition from Windows PE to the new OS. This task
sequence step is a required part of any OS deployment. It installs the Configuration
Manager client into the new OS, and prepares for the task sequence to continue
execution in the new OS.

This step is responsible for transitioning the task sequence from Windows PE to the full
OS. The step runs both in Windows PE and the full OS because of this transition.
However, since the transition starts in Windows PE, it can only be added during the
Windows PE portion of the task sequence.

This step replaces sysprep.inf or unattend.xml directory variables, such as %WINDIR% and
%ProgramFiles% , with the Windows PE installation directory, X:\Windows . The task

sequence ignores variables specified by using these environment variables.

To add this step in the task sequence editor, select Add, select Images, and select Setup
Windows and ConfigMgr.

Behaviors for Setup Windows and ConfigMgr
This step performs the following actions:

Preliminaries: Windows PE

   1. Substitute task sequence variables in the unattend.xml file.

   2. Download the package that contains the Configuration Manager client. Add the
     package to the deployed image.

Set up Windows

     Image-based installation

        1. Disable the Configuration Manager client in the image, if it exists. In other
           words, disable Autostart for the Configuration Manager client service.

        2. Update the registry in the deployed image to start the deployed OS with the
           same drive letter as the reference computer.

        3. Restart to the deployed OS.

        4. Windows mini-setup runs by using the previously specified sysprep.inf or
           unattend.xml answer file that has all end-user interaction suppressed. If you

<!-- p.432 -->

           use the Apply Network Settings step to join a domain, then that information
           is in the answer file. Windows mini-setup joins the computer to the domain.

     Setup.exe-based installation. Runs Setup.exe that follows the typical Windows
     setup process:

        1. Copy the OS upgrade package, specified in the Apply Operating System
           step, to the hard disk drive.

        2. Restart to the newly deployed OS.

        3. Windows mini-setup runs by using the previously specified sysprep.inf or
           unattend.xml answer file that has all user interface settings suppressed. If you
           use the Apply Network Settings step to join a domain, then that information
           is in the answer file. Windows mini-setup joins the computer to the domain.

Set up the Configuration Manager client
  1. After Windows mini-setup finishes, the task sequence resumes by using
     setupcomplete.cmd. For more information, see Run a script after setup is complete
     (SetupComplete.cmd).

  2. Enable or disable the local Administrator account, based on the option selected in
     the Apply Windows Settings step.

  3. Install the Configuration Manager client by using the previously downloaded
     package, and installation properties specified in this step. The client installs in
     "provisioning mode". This mode prevents the client from processing new policy
     requests until the task sequence completes. For more information, see Provisioning
     mode.

  4. Wait for the client to be fully operational.

The step completes
The task sequence continues running the next step.

  ７ Note

  The task sequence transitions from Windows PE to the newly installed Windows OS
  during the Setup Windows and ConfigMgr task. When the newly installed
  Windows starts for the first time, Windows Setup runs. At the end of Windows
  Setup, the task sequence is relaunched by the Windows Setup script

<!-- p.433 -->

  SetupComplete.cmd. This results in the task sequence running entirely within
  Windows Setup. Windows group policy normally doesn't process until after
  Windows Setup is complete, so therefore group policy isn't processed until the task
  sequence is complete. This behavior is consistent across different versions of
  Windows. For more information on the order of operations, see Run a script after
  setup is complete (SetupComplete.cmd).

  Although group policy doesn't normally run until Windows Setup and the task
  sequence completes, Windows and the task sequence engine don't block group
  policy from running. Some actions such as scripts, application installs, or certain
  task sequence steps run during the task sequence can trigger group policy
  evaluation. For example, the Install Software Updates task may trigger group
  policy evaluation when it sets WSUS server. A script that calls gpupdate could also
  trigger a group policy refresh.

Variables for Setup Windows and ConfigMgr
Use the following task sequence variables with this step:

     SMSClientInstallProperties

Cmdlets for Setup Windows and ConfigMgr
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepSetupWindowsAndConfigMgr
     New-CMTSStepSetupWindowsAndConfigMgr
     Remove-CMTSStepSetupWindowsAndConfigMgr
     Set-CMTSStepSetupWindowsAndConfigMgr

Properties for Setup Windows and ConfigMgr
On the Properties tab for this step, configure the settings described in this section.

Client package

Select Browse, then choose the Configuration Manager client installation package to
use with this step.

Use pre-production client package when available

<!-- p.434 -->

If there's a pre-production client package available, and the computer is a member of
the piloting collection, the task sequence uses this package instead of the production
client package. The pre-production client is a newer version for testing in the production
environment. Select Browse, then choose the pre-production client installation package
to use with this step.

Installation Properties
The task sequence step automatically specifies site assignment and the default
configuration. Use this field to specify any additional installation properties to use when
you install the client. To enter multiple installation properties, separate them with a
space.

Specify command-line options to use during client installation. For example, enter
/skipprereq: silverlight.exe to inform CCMSetup.exe to not install the Microsoft

Silverlight prerequisite. For more information about available command-line options for
CCMSetup.exe, see About client installation properties.

When you run an OS deployment task sequence on an internet-based client, that's
either Microsoft Entra joined or uses token-based authentication, you need to specify
the CCMHOSTNAME property in the Setup Windows and ConfigMgr step. For example,
CCMHOSTNAME=OTTERFALLS.CLOUDAPP.NET/CCM_Proxy_MutualAuth/12345678907927939 .

Options for Setup Windows and ConfigMgr

  ７ Note

  Don't enable Continue on error on the Options tab. If there's an error during this
  step, the task sequence fails whether or not you enable this setting.

Upgrade Operating System
Use this step to upgrade an earlier version of Windows to a later version of Windows.

This task sequence step runs only in the full OS. It doesn't run in Windows PE.

To add this step in the task sequence editor, select Add, select Images, and select
Upgrade Operating System.

   Tip

<!-- p.435 -->

  Windows 11 and Windows 10 media include multiple editions. When you configure
  a task sequence to use an OS upgrade package or OS image, be sure to select a
  supported edition.

  Use content pre-caching to download an applicable OS upgrade package before a
  user installs the task sequence. For more information, see Configure pre-cache
  content.

Variables for Upgrade OS
Use the following task sequence variables with this step:

     _SMSTSOSUpgradeActionReturnCode
     SetupCompletePause
     OSDSetupAdditionalUpgradeOptions

Cmdlets for Upgrade OS
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepUpgradeOperatingSystem
     New-CMTSStepUpgradeOperatingSystem
     Remove-CMTSStepUpgradeOperatingSystem
     Set-CMTSStepUpgradeOperatingSystem

Properties for Upgrade OS
On the Properties tab for this step, configure the settings described in this section.

Upgrade package

Select this option to specify the Windows OS upgrade package to use for the upgrade.

Source path

Specifies a local or network path to the Windows media that Windows Setup uses. This
setting corresponds to the Windows Setup command-line option /InstallFrom .

You can also specify a variable, such as %MyContentPath% or %DPC01% . When you use a
variable for the source path, set its value earlier in the task sequence. For example, use

<!-- p.436 -->

the Download Package Content step to specify a variable for the location of the OS
upgrade package. Then, use that variable for the source path for this step.

Edition

Specify the edition within the OS media to use for the upgrade.

Product key

Specify the product key to apply to the upgrade process.

Install the following feature updates

Starting in version 2103, select this option to upgrade a client's Windows OS by using a
feature update. This option uses content that you synchronize through the software
update point. The size of the servicing ESD file is generally smaller than the OS upgrade
package and WIM image file.

Select the new button (gold asterisk), and add a feature update.

  ７ Note

  You can only add feature updates.

If your environment supports multiple languages or architectures, add multiple feature
updates to the step. The client uses the first applicable update that's not superseded by
any other deployed updates.

The user experience with a feature update in a task sequence is the same as with an OS
upgrade package.

Provide the following driver content to Windows Setup during
upgrade

Add drivers to the destination computer during the upgrade process. The drivers must
be compatible with Windows 10 or later. This setting corresponds to the Windows Setup
command-line option /InstallDriver . For more information, see Windows Setup
command-line options.

Specify one of the following options:

<!-- p.437 -->

     Driver package: Select Browse and choose an existing driver package from the list.

     Staged content: Select this option to specify the location for the driver content.
     You can specify a local folder, network path, or a task sequence variable. When you
     use a variable for the source path, set its value earlier in the task sequence. For
     example, by using the Download Package Content step.

   Tip

  If you want to have dynamic content for multiple types of hardware:

       Use multiple instances of this step with conditions for the hardware types and
       separate driver content.

       Use multiple instances of the Download Package Content step. Place the
       content in a common location, and then use the Staged content option. The
       benefit of this method is the task sequence has a single Upgrade OS step.

  ７ Note

  This option is not compatible with feature updates.

Time-out (minutes)

Specify the number of minutes before Configuration Manager fails this step. This option
is useful if Windows Setup stops processing but doesn't terminate.

Perform Windows Setup compatibility scan without starting
upgrade

Perform the Windows Setup compatibility scan without starting the upgrade process.
This setting corresponds to the Windows Setup command-line option /Compat ScanOnly .
Deploy the entire OS upgrade package with this option.

When you enable this option, this step doesn't put the Configuration Manager client
into provisioning mode. Windows Setup runs silently in the background, and the client
continues to function as normal. For more information, see Provisioning mode.

Setup returns an exit code as a result of the scan. The following table provides some of
the more common exit codes:

<!-- p.438 -->

                                                                            ﾉ   Expand table

 Exit code                                          Details

 MOSETUP_E_COMPAT_SCANONLY (0xC1900210)             No compatibility issues ("success").

 MOSETUP_E_COMPAT_INSTALLREQ_BLOCK                  Actionable compatibility issues.
 (0xC1900208)

 MOSETUP_E_COMPAT_MIGCHOICE_BLOCK                   Selected migration choice isn't available.
 (0xC1900204)                                       For example, an upgrade from Enterprise
                                                    to Professional.

 MOSETUP_E_COMPAT_SYSREQ_BLOCK (0xC1900200)         Not eligible for Windows 10.

 MOSETUP_E_COMPAT_INSTALLDISKSPACE_BLOCK            Not enough free disk space.
 (0xC190020E)

For more information about this parameter, see Windows Setup Command-Line
Options.

Ignore any dismissible compatibility messages
Specifies that Setup completes the installation, ignoring any dismissible compatibility
messages. This setting corresponds to the Windows Setup command-line option
/Compat IgnoreWarning .

Dynamically update Windows Setup with Windows Update
Enable setup to perform Dynamic Update operations, such as search, download, and
install updates. This setting corresponds to the Windows Setup command-line option
/DynamicUpdate . This setting isn't compatible with Configuration Manager software

updates. Enable this option when you manage updates with stand-alone Windows
Server Update Services (WSUS) or Windows Update for Business.

Override policy and use default Microsoft Update

Temporarily override the local policy in real time to run Dynamic Update operations. The
computer gets updates from Windows Update.

Feedback

<!-- p.439 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.440 -->

Install Software Updates
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The Install Software Updates step is commonly used in Configuration Manager task
sequences. When installing or updating the OS, it triggers the software updates
components to scan for and deploy updates. This step can cause challenges for some
customers, such as long timeout delays or missed updates. Use the information in this
article to help mitigate common issues with this step, and for better troubleshooting
when things go wrong.

For more information on the step, see Install Software Updates

Recommendations
To help this process be successful, use the following recommendations:

      Use offline servicing
      Single index
      Reduce image size

Use offline servicing
Use Configuration Manager to regularly install applicable software updates to your
image files. This practice then reduces the number of updates that you need to install
during the task sequence.

For more information, see Apply software updates to an image.

Single index
Many image files include multiple indexes, such as for different editions of Windows.
Reduce the image file to a single index that you require. This practice reduces the
amount of time to apply software updates to the image. It also enables the next
recommendation to reduce the image size.

Automate this process when you add an OS image to the site. For more information, see
Add an OS image.

Reduce image size
