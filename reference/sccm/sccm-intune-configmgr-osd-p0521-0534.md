---
title: "OS deployment documentation — pages 521-534"
type: reference
domain: sccm
slug: sccm-intune-configmgr-osd-p0521-0534
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-osd-p0521-0534
family: sccm
documentKind: "doc"
abstract: "(input) Specifies the account by which the command line is run. The value is a string of the form username for a local account or domain\\username for a domain one. Specify the account password with the SMSTSRunCommandLineUserPassword variable. ７ Note Use the SMSTSRunCommandLineA"
---

# OS deployment documentation — pages 521-534

<!-- p.521 -->

(input)

Specifies the account by which the command line is run. The value is a string of the form
username for a local account or domain\username for a domain one. Specify the account
password with the SMSTSRunCommandLineUserPassword variable.

  ７ Note

  Use the SMSTSRunCommandLineAsUser variable with this variable to configure the user
  context for this step.

For more information on the task sequence run-as account, see Accounts.

SMSTSRunCommandLineUserPassword
Applies to the Run Command Line step.

(input)

Specifies the password for the account specified by the SMSTSRunCommandLineUserName
variable.

SMSTSRunPowerShellAsUser
Applies to the Run PowerShell Script step.

Use task sequence variables to configure the user context for the Run PowerShell Script step.
You don't need to configure the Run PowerShell Script step with a placeholder account to use
the SMSTSRunPowerShellUserName and SMSTSRunPowerShellUserPassword variables.

Configure SMSTSRunPowerShellAsUser with one of the following values:

      true : Any further Run PowerShell Script steps run in the context of the user specified in
      SMSTSRunPowerShellUserName .

      false : Any further Run PowerShell Script steps run in the context that you configured on

     the step.

SMSTSRunPowerShellUserName
Applies to the Run PowerShell Script step.

(input)

<!-- p.522 -->

Specifies the account by which the PowerShell script is run. The value is a string of the form
username or domain\username. Specify the account password with the
SMSTSRunPowerShellUserPassword variable.

  ７ Note

  To use these variables, configure the Run PowerShell Script step with the setting to Run
  this step as the following account. When you enable this option, if you're setting the user
  name and password with variables, specify any value for the account.

For more information on the task sequence run-as account, see Accounts.

SMSTSRunPowerShellUserPassword
Applies to the Run PowerShell Script step.

(input)

Specifies the password for the account specified by the SMSTSRunPowerShellUserName
variable.

SMSTSSoftwareUpdateScanTimeout
Applies to the Install Software Updates step.

(input)

Control the timeout for the software updates scan during this step. For example, if you expect
numerous updates during the scan, increase the value. The default value is 3600 seconds (60
minutes). The variable value is set in seconds.

SMSTSUDAUsers
Specifies the primary users of the destination computer by using the following format:
<DomainName>\<UserName> . Separate multiple users by using a comma ( , ). For more

information, see Associate users with a destination computer.

Example
contoso\jqpublic, contoso\megb, contoso\janedoh

<!-- p.523 -->

SMSTSWaitCcmexecOperationalTimeout
(input)

Use this variable to control the timeout period for the task sequence to wait for the SMS Agent
Host service (ccmexec) to completely start. Specify this value in seconds. The default timeout
period is 30 minutes, or 1800 seconds.

Examples of SMSTSWaitCcmexecOperationalTimeout
      1800 (default): 30 minutes

      300 : The task sequence waits five minutes for ccmexec to start

SMSTSWaitForSecondReboot
Applies to the Install Software Updates step.

(input)

This optional task sequence variable controls client behavior when a software update
installation triggered by the Install Software Updates task requires multiple restarts. Set this
variable before the Install Software Updates step to prevent a task sequence from failing
because of multiple restarts from software update installation.

This variable is useful when a single Install Software Updates task sequence step installs
software updates that need multiple restarts to finish installing.

Set the SMSTSWaitForSecondReboot value in seconds to specify how long the task sequence
pauses on this step while the computer restarts. Allow sufficient time in case there's multiple
restarts. For example, if you set SMSTSWaitForSecondReboot to 600 , the task sequence
pauses for 10 minutes after a restart before additional steps run.

The SMSTSWaitForSecondReboot variable is intended for use with the Install Software
Updates task, but can be set anywhere in the task sequence to introduce delays after reboots
initiated by tasks other than the Install Software Updates task. For this reason, when this
variable is set before the Install Software Updates task, it's advisable to also set it again after
the Install Software Updates task with a value of 0 . This resets the variable and prevents
unnecessary delays during the task sequence. If there are multiple Install Software Updates
tasks in the task sequence, define the variable to the desired value before the first Install
Software Updates task, and then reset it back to 0 after the last Install Software Updates task.

  ７ Note

<!-- p.524 -->

  This variable only applies to OSD task sequences that deploys an OS. It doesn't work with
  any task sequence that doesn't utilize the Setup Windows and ConfigMgr task, such as
  stand-alone task sequences or in-place upgrade task sequences.

TSDebugMode
Set this variable to TRUE on a collection or computer object to which the task sequence is
deployed. Any device that has this variable set will put any task sequence deployed to it into
debug mode.

For more information, see Debug a task sequence.

TSDebugOnError
Set this variable to TRUE to automatically start the task sequence debugger when the task
sequence returns an error.

Set this variable using:

     The Set Task Sequence Variable step

     A collection variable. For more information, see How to set variables.

TSDisableProgressUI
Use this variable to control when the task sequence displays progress to end users. To hide or
display progress at different times, set this variable multiple times in a task sequence.

      true : Hide task sequence progress

      false : Display task sequence progress

TSErrorOnWarning
Applies to the Install Application step.

(input)

Specify whether the task sequence engine considers a detected warning as an error during this
step. The task sequence sets the _TSAppInstallStatus variable to Warning when one or more
applications, or a required dependency, didn't install because it didn't meet a requirement.

<!-- p.525 -->

When you set this variable to True , and the task sequence sets _TSAppInstallStatus to
Warning , the outcome is an error. A value of False is the default behavior.

TSProgressInfoLevel
Specify this variable to control the type of information that the task sequence progress window
displays. Use the following values for this variable:

      1 : Include the current step and total steps to the progress text. For example, 2 of 10.

      2 : Include the current step, total steps, and percentage completed. For example, 2 of 10
     (20% complete).
      3 : Include the percentage completed. For example, (20% complete).

TSUEFIDrive
Use on the properties of a FAT32 partition in the Variable field. When the task sequence
detects this variable, it prepares the disk for transition to UEFI before it restarts the computer.
For more information, see Task sequence steps to manage BIOS to UEFI conversion.

WorkingDirectory
Applies to the Run Command Line step.

(input)

Specifies the starting directory for a command-line action. The specified directory name can't
exceed 255 characters.

Examples
      C:\
      %SystemRoot%

Deprecated variables
The following variables are deprecated:

     OSDAllowUnsignedDriver: Isn't used when deploying Windows Vista and later operating
     systems
     OSDBuildStorageDriverList: Only applies to Windows XP and Windows Server 2003

<!-- p.526 -->

     OSDDiskpartBiosCompatibilityMode: Only needed when deploying Windows XP or
     Windows Server 2003
     OSDInstallEditionIndex: Not needed post-Windows Vista
     OSDPreserveDriveLetter: For more information, see OSDPreserveDriveLetter

OSDPreserveDriveLetter

  ） Important

  This task sequence variable is deprecated.

  During an OS deployment, by default, Windows Setup determines the best drive letter to
  use (typically C:).

Previous behavior: when applying an image, the OSDPreverveDriveLetter variable determines
whether the task sequence uses the drive letter captured in the image file (WIM). Set the value
for this variable to false to use the location that you specify for the Destination setting in the
Apply Operating System task sequence step. For more information, see Apply OS image.

See also
     Task sequence steps
     Using task sequence variables
     Planning considerations for automating tasks

<!-- p.527 -->

Prestart commands for task sequence
media in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can create a prestart command in Configuration Manager to use with boot media,
stand-alone media, and prestaged media. The prestart command is a script or
executable that runs before the task sequence is selected and can interact with the user
in Windows PE. The prestart command can prompt a user for information and save it in
the task sequence environment or query a task sequence variable for information. When
the destination computer boots, the command-line is run before the policy is
downloaded from the management point. Use the following procedures to create a
script to use for the prestart command, distribute the content associated with the
prestart command, and configure the prestart command in media.

Create a script file to use for the Prestart
Command
Task sequence variables can be read and written by using the
Microsoft.SMS.TSEnvironment COM object while the task sequence is running. The
following example illustrates a Visual Basic script file that queries the _SMSTSLogPath
task sequence variable to get the current log location. The script also sets a custom
variable.

  VBScript

  dim osd: set env = CreateObject("Microsoft.SMS.TSEnvironment")
  dim logPath
  ' You can query the environment to get an existing variable.
  logPath = env("_SMSTSLogPath")
  ' You can also set a variable in the OSD environment.
  env("MyCustomVariable") = "varname"

Create a Package for the Script File and
Distribute the Content
After you create the script or executable for the prestart command, you must create a
package source to host the files for the script or executable, create a package for the

<!-- p.528 -->

files (no program required), and then distribute the content to a distribution point.

For more information about creating a package, see Packages and programs.

For more information about distributing content, see Distribute content.

Configure the Prestart Command in Media
You can configure a prestart command in the Create Task Sequence Media Wizard for
stand-alone media, bootable media, or prestaged media. For more information about
the media types, see Create task sequence media. Use the following procedure to create
a prestart command in media.

To create a prestart command in media
   1. In the Configuration Manager console, click Software Library.

   2. In the Software Library workspace, expand Operating Systems, and then click Task
     Sequences.

   3. On the Home tab, in the Create group, click Create Task Sequence Media to start
     the Create Task Sequence Media Wizard.

   4. On the Select Media Type page, select Stand-alone media, Bootable media, or
     Prestaged media, and then click Next.

   5. Navigate to the Customization page of the wizard. For more information about
     configuring the other pages in the wizard, see Create task sequence media.

   6. On the Customization page, specify the following information, and then click Next.

           Select Enable prestart command.

           In the Command line text box, enter the script or executable that you created
           for the prestart command.

             ） Important

             Use cmd /C <prestart command> to specify the prestart command. For
             example, if you used TSScript.vbs as the name for your prestart
             command script, you would enter cmd /C TSScript.vbs for the command
             line. Where cmd /C opens a new Windows command interpreter window
             and uses the Path environment variable to find the prestart command
             script or executable. You can also specify the full path to the prestart

<!-- p.529 -->

              command, but the drive letter could be different on computers with
              different drive configurations.

           Select Include files for the prestart command.

           Click Set to select the package that is associated with the prestart command
           files.

           Click Browse to select the distribution point that hosts the content for the
           prestart command.

   7. Complete the wizard.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.530 -->

Provisioning mode
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

During an OS deployment task sequence, Configuration Manager places the client in
provisioning mode. (An OS deployment task sequence includes in-place upgrade.) In
this state, the client doesn't process policy from the site. This behavior allows the task
sequence to run without risk of additional deployments running on the client. When the
task sequence completes, either success or handled failure, it exits client provisioning
mode.

If the task sequence unexpectedly fails, the client can be left in provisioning mode. For
example, if the device restarts in the middle of task sequence processing, and it's unable
to recover. An administrator must manually identify and fix clients in this state.

Manually remove provisioning mode
If a client is left in provisioning mode, use this manual process to return the client to
normal operation.

  PowerShell

  Invoke-WmiMethod -Namespace root\CCM -Class SMS_Client -Name
  SetClientProvisioningMode -ArgumentList $false

  ） Important

  One of the changes made by this WMI method is setting a registry value, but it
  makes other changes as well. Just changing the registry value doesn't fully take the
  client out of provisioning mode. If you manually edit the registry, the client may
  exhibit unexpected behaviors.

Client provisioning mode timeout
The task sequence sets a timestamp when it puts the client in provisioning mode. Every
60 minutes, a client in provisioning mode checks the duration of time since the
timestamp. If it's been in provisioning mode for more than 48 hours, the client
automatically exits provisioning mode and restarts its process.

<!-- p.531 -->

48 hours is the default provisioning mode timeout value. You can adjust this timer on a
device by setting the ProvisioningMaxMinutes value in the following registry key:
HKLM\Software\Microsoft\CCM\CcmExec . The value is specified in minutes. If this value

doesn't exist or is 0 , the client uses the default 48 hours.

The timestamp ProvisioningEnabledTime is located in the following registry key:
HKLM\Software\Microsoft\CCM\CcmExec . The timestamp has a value of the last time the

machine entered provisioning mode. The format is epoch (Unix timestamp) and is in
UTC.

This timestamp is also reset to the current time when you manually place the machine in
provisioning mode by using the following command:

  PowerShell

  Invoke-WmiMethod -Namespace root\CCM -Class SMS_Client -Name
  SetClientProvisioningMode -ArgumentList $true

Process flow diagrams
These diagrams show the process flow for the task sequence and the client.

Task sequence
The following diagram shows how the task sequence sets provisioning mode:

<!-- p.532 -->

Client remediation
The following diagram shows how the client exits provisioning mode:

<!-- p.533 -->

<!-- p.534 -->

See also
Setup Windows and ConfigMgr

Upgrade Operating System

Feedback
Was this page helpful?      Yes    No

Provide product feedback
