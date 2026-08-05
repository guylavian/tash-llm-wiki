---
title: "OS deployment documentation — pages 441-480"
type: reference
domain: sccm
slug: sccm-intune-configmgr-osd-p0441-0480
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-osd-p0441-0480
family: sccm
documentKind: "doc"
abstract: "When you apply software updates to the image, optimize the output by removing any superseded updates. Use the DISM command-line tool, for example: Command dism /Mount-Image /ImageFile:C:\\Data\\install.wim /MountDir:C:\\Mountdir dism /Image:C:\\Mountdir /Cleanup-Image /StartComponen"
---

# OS deployment documentation — pages 441-480

<!-- p.441 -->

When you apply software updates to the image, optimize the output by removing any
superseded updates. Use the DISM command-line tool, for example:

  Command

  dism /Mount-Image /ImageFile:C:\Data\install.wim /MountDir:C:\Mountdir
  dism /Image:C:\Mountdir /Cleanup-Image /StartComponentCleanup /ResetBase
  dism /Unmount-Image /MountDir:C:\Mountdir /Commit

There's an option to automate this process. For more information, see Optimized image
servicing.

Image engineering decisions
When you design your imaging process, there are several options that can affect the
installation of software updates:

     Periodically recapture the image
     Use offline servicing
     Use default image only

Periodically recapture the image
You have an automated process to capture a custom OS image on a regular schedule.
This capture task sequence installs the latest software updates. These updates can
include cumulative, non-cumulative, and other critical updates such as servicing stack
updates (SSU). The deployment task sequence installs any other updates since capture.

For more information on this process, see Create a task sequence to capture an OS.

Advantages: recapture image
     Fewer updates to apply at deployment time per client, which saves time and
     bandwidth during deployment
     Fewer updates to worry about causing restarts
     Customized image for the organization
     Fewer variables at deployment time

Disadvantages: recapture image

     Time to create and capture image, even though it's mostly automated

<!-- p.442 -->

     Increased time to distribute the image to distribution points, which can be seen as
     outage for active deployments
     Time to test through pre-production environments may be longer than OS patch
     cycle, which can make the updated image irrelevant

Use offline servicing
Schedule Configuration Manager to apply software updates to your images.

For more information, see Apply software updates to an image.

Advantages: offline servicing

     Fewer updates to apply at deployment time per client, which saves time and
     bandwidth during deployment
     Fewer updates to worry about causing restarts
     You can schedule the servicing process at the site

Disadvantages: offline servicing

     Manual selection of updates
     Increased time to distribute the image to distribution points
     Only supports CBS-based updates. It can't apply Microsoft 365 Apps updates

   Tip

  You can automate the selection of software updates using PowerShell. Use the Get-
  CMSoftwareUpdate cmdlet to get a list of updates. Then use the New-
  CMOperatingSystemImageUpdateSchedule cmdlet to create the offline servicing
  schedule. The following example shows one method to automate this action:

    PowerShell

    # Get the OS image
    $Win10Image = Get-CMOperatingSystemImage -Name "Windows 10 Enterprise"

    # Get the latest cumulative update for Windows 10 1809
    $OSBuild = "1809"
    $LatestUpdate = Get-CMSoftwareUpdate -Fast | Where
    {$_.LocalizedDisplayName -Like "*Cumulative Update for Windows 10
    Version $OSBuild for x64*" -and $_.LocalizedDisplayName -notlike
    "*Dynamic*"} | Sort-Object ArticleID -Descending | Select -First 1
    Write-Host "Latest update for Windows 10 build" $OSBuild "is"
    $LatestUpdate.LocalizedDisplayName

<!-- p.443 -->

     # Create a new update schedule to apply the latest update
     New-CMOperatingSystemImageUpdateSchedule -Name $Win10Image.Name -
     SoftwareUpdate $LatestUpdate -RunNow -ContinueOnError $True

Use default image only
Use the default Windows install.wim image file in your deployment task sequences.

Advantages: default image

     A known good source, which reduces the risk of image corruption as a possible
     issue
     Eliminates modifications to image as a possible issue

Disadvantages: default image
     Potential for high volume of updates during the deployment
     Increased deployment time for every device
     May not have needed customizations, requires other task sequence steps to
     customize

Flowchart
This flowchart diagram shows the process when you include the Install Software
Updates step in a task sequence.

View the diagram at full size

<!-- p.444 -->

1. Process starts on the client: A task sequence running on a client includes the
  Install Software updates step.
2. Compile and evaluate policies: The client compiles all software update policies
  into WMI RequestedConfigs namespace. (CIAgent.log)
3. Is this instance the first time it's called?
   a. Yes: Go to Full scan
   b. No: Is the step configured with the option to Evaluate software updates from
      cached scan results?
       i. Yes: Go to Scan from cached results
      ii. No: Go to Full scan
4. Scan process: either a full scan or scan from cached results, with monitoring
  process in parallel.

<!-- p.445 -->

   a. Full scan: The task sequence engine calls the software update agent via Update
     Scan API to do a full scan. (WUAHandler.log, ScanAgent.log)
      i. SUM agent scan - full: Normal scan process via Windows Update Agent
        (WUA), which communicates with software update point running WSUS. It
        adds any applicable updates to the local update store. (WindowsUpdate.log,
        UpdateStore.log)
  b. Scan from cached results: The task sequence engine calls the software update
     agent via Update Scan API to scan against cached metadata. (WUAHandler.log,
     ScanAgent.log)
      i. SUM agent scan - cached: The Windows Update Agent (WUA) checks against
        updates already cached in the local update store. (WindowsUpdate.log,
        UpdateStore.log)
   c. Start scan timer: The task sequence engine starts a timer and waits. (This
     process happens in parallel with either the full scan or scan from cached results
     process.)
      i. Monitoring: The task sequence engine monitors the SUM agent for status.
      ii. What's the response from the SUM agent?

              In progress: Has the timer reached the value in task sequence variable
              SMSTSSoftwareUpdateScanTimeout? (Default 1 hour)
                 Yes: The step fails.
                 No: Go to Monitoring
              Failed: The step fails.
              Complete: Go to Enumerate update list
5. Enumerate update list: The SUM agent enumerates the list of updates returned by
  the scan, determining which are available or mandatory.
6. Are there any updates in the list of scan results?

        Yes: Go to Install updates
        No: Nothing to install, the step successfully completes.

7. Deployment process: The install updates process happens in parallel with the
  deployment monitoring process.
   a. Install updates: The task sequence engine calls the SUM agent via Update
     Deployment API to install all available or only mandatory updates. This behavior
     is based on the configuration of the step, whether you select Required for
     installation - Mandatory software updates only or Available for installation -
     All software updates. You can also specify this behavior using the
     SMSInstallUpdateTarget variable.
      i. SUM agent install: Normal install process using existing cached list of
        updates, with standard content download. Install update via Windows

<!-- p.446 -->

            Update Agent (WUA). (UpdatesDeployment.log, UpdatesHandler.log,
            WuaHandler.log, WindowsUpdate.log)
      b. Start deployment timer and show progress: The task sequence engine starts an
        installation timer, shows subprogress at 10% intervals in TS Progress UI, and
        waits.
          i. Monitoring: The task sequence engine polls the SUM agent for status.
         ii. What's the response from the SUM agent?

                  In progress: Has the installation process been inactive for 8 hours?
                     Yes: The step fails.
                     No: Go to Monitoring
                  Failed: The step fails.
                  Complete: Go to Is the step configured with the option to Evaluate
                  software updates from cached scan results?

Timeouts
The diagram includes two of the timeout variables that apply to this step. There are
other standard timers from other components that can affect this process.

     Update scan timeout: One hour (smsts.log)
     Location request timeout: One hour (LocationServices.log, CAS.log)
     Content download timeout: One hour (DTS.log)
     Inactive distribution point timeout: One hour (LocationServices.log, CAS.log)
     Total install inactive timeout: Eight hours (smsts.log)

Troubleshooting
Use the following resources and additional information to help you troubleshoot issues
with this step:

     Make sure to target your software update deployments to the same collection as
     the task sequence deployment.

     Make sure to include software update points in boundary groups. For more
     information, see Configuration Manager clients don't get software updates.

     To help you troubleshoot the software update management process, see
     Troubleshoot software update management in Configuration Manager.

     To help improve overall performance, reduce the size of the software update
     catalog. For example:

<!-- p.447 -->

        Remove unnecessary classifications, products, and languages. For more
        information, see Configure classifications and products to synchronize.

        Reindex the site database and rebuild statistics. For more information, see the
        FAQ for site sizing and performance.

        Decline unnecessary updates, for example:

            Superseded.

              ７ Note

              Configuration Manager does this action for you. For more information,
              see WSUS cleanup behavior.

            Itanium

            Beta

            Version Next

            ARM

            Versions of Windows you aren't deploying

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.448 -->

In-place upgrade recommendations
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The default task sequence template for Windows in-place upgrade includes groups with
recommended actions to add before and after the upgrade process. These actions are
common among many customers who are successfully upgrading Windows on devices.
This article provides information about these recommended steps during different
phases of the upgrade process.

Prepare for upgrade
If you have an existing task sequence that doesn't already have these actions, manually
add them to your task sequence in the Prepare for Upgrade group.

Battery checks
Add steps in this group to check whether the computer is using battery, or wired power.
This action requires a custom script or utility to run this check.

Battery check example

Use WbemTest and connect to the root\cimv2 namespace. Then run the following
query:

Select BatteryStatus From Win32_Battery where BatteryStatus != 2

If it returns any results, then the device is running on battery. Otherwise, the device is
connected to wired power.

Network/wired connection checks
Add steps in this group to check whether the computer is connected to a network, and
isn't using a wireless connection. This action requires a custom script or utility to run this
check.

Network check example

<!-- p.449 -->

Use WbemTest and connect to the root\cimv2 namespace. Then run the following
query:

Select * From Win32_NetworkAdapter Where NetConnectionStatus = 2 and
PhysicalAdapter = 'True' and NetConnectionID = 'Wi-Fi'

If it returns any results, then the device is running on Wi-Fi. Otherwise, the device is
connected to wired network connection.

Remove incompatible applications
Add steps in this group to remove any applications that are incompatible with the target
version of Windows. The method to uninstall an application varies.

If the application uses Windows Installer, copy the Uninstall program command line
from the Programs tab on the Windows Installer deployment type properties of the
application. Then add a Run Command Line step in this group with the uninstall
program command line. For example:

msiexec /x {150031D8-1234-4BA8-9F52-D6E5190D1CBA} /q

Remove incompatible drivers
Add steps in this group to remove any drivers that are incompatible with the target
version of Windows.

Remove/suspend third-party security
Add steps in this group to remove or suspend third-party security programs, such as
antivirus.

If you're using a third-party disk encryption program, provide its encryption driver to
Windows Setup with the /ReflectDrivers command-line option. Add a Set Task
Sequence Variable step to the task sequence in this group. Set the task sequence
variable to OSDSetupAdditionalUpgradeOptions. Set the value to /ReflectDrivers with
the path to the driver. This task sequence variable appends the Windows Setup
command-line used by the task sequence. Contact your software vendor for any further
guidance on this process.

Download Package Content task sequence step

<!-- p.450 -->

Use the Download Package Content step before the Upgrade Operating System step in
the following scenarios:

     You use a single upgrade task sequence for both x86 and x64 platforms. Include
     two Download Package Content steps in the Prepare for Upgrade group. Set
     conditions on each step to detect the client architecture. This condition causes the
     step to download only the appropriate OS upgrade package. Configure each
     Download Package Content step to use the same variable, and use the variable for
     the media path on the Upgrade Operating System step.

     To dynamically download an applicable driver package, use two Download
     Package Content steps with conditions to detect the appropriate hardware type
     for each driver package. Configure each Download Package Content step to use
     the same variable. Then use that variable for the Staged content value in the
     drivers section on the Upgrade Operating System step.

       ７ Note

       Configuration Manager adds a numerical suffix to this variable name. For
       example, if you specify %mycontent% as a custom variable, the client stores all
       referenced content in this location. When you refer to the variable in a
       subsequent step, such as Upgrade Operating System, use the variable with a
       numerical suffix. In this example, %mycontent01% or %mycontent02% , where the
       number corresponds to the order in which the Download Package Content
       step lists this specific content.

Post-processing
After you create the task sequence, add more steps in the Post-Processing group of the
task sequence.

  ７ Note

  This task sequence isn't linear. There are conditions on steps that can affect the
  results of the task sequence. This behavior depends on whether it successfully
  upgrades the client computer, or if it has to roll back the client computer to the
  original OS.

The default task sequence template for Windows in-place upgrade includes other
groups with recommended actions to add after the upgrade process. These actions in

<!-- p.451 -->

the Post-Processing group are common among many customers who are successfully
upgrading Windows on devices. If you have an existing task sequence that doesn't
already have these actions, manually add them to your task sequence in the Post-
Processing group.

Apply setup-based drivers
Add steps in this group to install setup-based drivers (.exe) from packages.

Install/enable third-party security
Add steps in this group to install or enable third-party security programs, such as
antivirus.

Set Windows default apps and associations
Add steps in this group to set Windows default apps and file associations.

   1. Prepare a reference computer with app associations you want.

   2. Run the following command line to export:

      dism /online /Export-

      DefaultAppAssociations:"%UserProfile%\Desktop\DefaultAppAssociations.xml"

   3. Add the XML file to a package.

   4. Add a Run Command Line step in this group. Specify the package that contains the
      XML file, and then specify the following command line:

      dism /online /Import-DefaultAppAssociations:DefaultAppAssociations.xml

For more information, see Export or import default application associations.

Apply customizations and personalization
Add steps in this group to apply Start menu customizations, such as organizing program
groups. For more information, see Customize the Start layout.

Rollback

<!-- p.452 -->

When something goes wrong with the upgrade process after the computer restarts,
Windows Setup rolls back the system to the previous OS. The task sequence then
continues with any steps in the Rollback group. After you create the task sequence, add
optional steps in this group as necessary. For example, reverse any changes made to the
system in the Prepare for Upgrade group, such as uninstalling incompatible software.

Run actions on failure
The default task sequence template for Windows in-place upgrade includes a group to
Run actions on failure. This group includes recommended actions to add in case the
upgrade process fails. These actions make it easier to troubleshoot.

Collect logs
To gather logs from the client, add steps in this group.

     A common practice is to copy the log files to a network share. To establish this
     connection, use the Connect to Network Folder step.

     To do the copy operation, use a custom script or utility with either the Run
     Command Line or Run PowerShell Script step.

     Files to collect might include the following logs: %_SMSTSLogPath%\*.log
     %SystemDrive%\$Windows.~BT\Sources\Panther\setupact.log

     For more information on setupact.log and other Windows Setup logs, see
     Windows Setup Log files.

     For more information on Configuration Manager client logs, see Configuration
     Manager client logs.

     For more information on _SMSTSLogPath and other useful variables, see Task
     sequence variables.

Run diagnostic tools
To run diagnostic tools, add steps in this group. Automate these tools for collecting
additional information from the system right after the failure.

One such tool is Windows SetupDiag. It's a standalone diagnostic tool to get details
about why a Windows upgrade was unsuccessful.

     In Configuration Manager, create a package for the tool.

<!-- p.453 -->

     Add a Run Command Line step to this group of your task sequence. Use the
     Package option to reference the tool. The following string is an example
     Command line: SetupDiag.exe /Output:"%_SMSTSLogPath%\SetupDiagResults.log"

   Tip

  Always use the most recent version of SetupDiag for the latest functionality and
  fixes to known issues. For more information, see SetupDiag.

Other recommendations

Windows documentation
Review Windows documentation to Resolve Windows client upgrade errors. This article
also includes detailed information about the upgrade process.

Check minimum disk space
On the default Check Readiness step, enable Ensure minimum free disk space (MB). Set
the value to at least 16384 (16 GB) for a 32-bit OS upgrade package, or 20480 (20 GB)
for 64-bit.

Retry downloading policy
Use the SMSTSDownloadRetryCount task sequence variable to retry downloading
policy. Currently by default, the client retries twice; this variable is set to two (2). If your
clients aren't on a wired intranet network connection, more retries help the client obtain
policy. Using this variable causes no negative side effect, other than delayed failure if it
can't download policy. Also increase the SMSTSDownloadRetryDelay variable from the
default 15 seconds.

Do an inline compatibility assessment
   1. Add a second Upgrade Operating System step early in the Prepare for Upgrade
     group.

      a. Name it Upgrade assessment.

      b. Specify the same upgrade package, and then enable the option to Perform
         Windows Setup compatibility scan without starting upgrade.

<!-- p.454 -->

      c. Enable Continue on error on the Options tab.

   2. Immediately following this Upgrade assessment step, add a Run Command Line
     step. Specify the following command line:

     cmd /c exit %_SMSTSOSUpgradeActionReturnCode%

     This command causes the command prompt to exit with the specified non-zero
     exit code, which the task sequence considers a failure.

   3. On the Options tab, add the following condition:

     Task Sequence Variable _SMSTSOSUpgradeActionReturnCode not equals 3247440400

     This condition means that the task sequence only runs this Run Command Line
     step if the return code isn't a success code.

The return code 3247440400 is the decimal equivalent of
MOSETUP_E_COMPAT_SCANONLY (0xC1900210), which is a successful compatibility
scan with no issues. If the Upgrade Assessment step succeeds and returns 3247440400 ,
the task sequence skips this Run Command Line step, and continues. If the assessment
step returns any other return code, this Run Command Line step runs. Because the
command exits with a non-zero return code, the task sequence also fails. The task
sequence log and status messages include the return code from the Windows Setup
compatibility scan. For more information on _SMSTSOSUpgradeActionReturnCode, see
Task sequence variables.

For more information, see the Upgrade operating system task sequence step.

Convert from BIOS to UEFI
If you want to change the device from BIOS to UEFI during this task sequence, see
Convert from BIOS to UEFI during an in-place upgrade.

Manage BitLocker
If you're using BitLocker Disk Encryption, then by default Windows Setup automatically
suspends it during upgrade. Windows Setup includes the /BitLocker command-line
parameter to control this behavior. If your security requirements need devices to always
have active disk encryption, then use the OSDSetupAdditionalUpgradeOptions task
sequence variable in the Prepare for Upgrade group to include /BitLocker
TryKeepActive . For more information, see Windows Setup Command-line Options.

<!-- p.455 -->

Remove default apps
Some customers remove default provisioned apps in Windows. For example, the Bing
Weather app, or the Microsoft Solitaire Collection. In some situations, these apps return
after upgrading Windows. For more information, see How to keep apps removed from
Windows client from returning during an update.

Add a Run Command Line step to the task sequence in the Prepare for Upgrade group.
Specify a command line similar to the following example:

cmd /c reg add

"HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Appx\AppxAllUserStore\Deprovisione
d\Microsoft.BingWeather_8wekyb3d8bbwe" /f

Next steps
For more information, see the following articles:

     Upgrade Windows to the latest version
     Create a task sequence to upgrade an OS
     About task sequence steps: Upgrade OS

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.456 -->

Preprovision BitLocker in Windows PE
with Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The Pre-provision BitLocker task sequence step in Configuration Manager allows you to
enable BitLocker from the Windows Preinstallation Environment (Windows PE) prior to
operating system deployment. Only the used drive space is encrypted, and therefore,
encryption times are much faster. This is done with a randomly generated clear
protector applied to the formatted volume and encrypting the volume prior to running
the Windows setup process. The ability to pre-provision BitLocker was introduced with
Windows 8 and Windows Server 2012. However, you can pre-provision BitLocker on a
hard drive and install Windows 7 as long as you follow specific steps. After Windows 7
Setup completes, you must set a BitLocker key protector because the Windows 7
BitLocker control panel does not support BitLocker with a clear protector. You must add
a key protector by using the Enable BitLocker step or by using the manage-bde.exe
command-line tool.

Generally, you must do the following to successfully pre-provision BitLocker on a
computer that will install Windows 7:

      Restart the computer in Windows PE

        ） Important

        You must use a boot image with Windows PE 4 or later to pre-provision
        BitLocker. For more information about supported Windows PE versions in
        Configuration Manager, see Dependencies External to Configuration
        Manager.

      Partition and format the hard drive

      Pre-provision BitLocker

      Install Windows 7 with specific operating system and network settings

      Add a key protector to BitLocker

      In Configuration Manager, the recommended way to pre-provision BitLocker on a
      hard drive and install Windows 7 is to create a new task sequence and select Install

<!-- p.457 -->

       an existing image package from the Create New Task Sequence page of the
       Create Task Sequence Wizard. The wizard creates the task sequence steps listed in
       following table.

 ７ Note

 The task sequence might have additional steps depending on how you configured
 the settings in the wizard. For example, you might have the Capture Windows
 Settings step if you selected Captured Microsoft Windows settings on the State
 Migration page of the wizard.

                                                                                   ﾉ    Expand table

Task             Details
sequence
step

Disable          This step disables BitLocker encryption, if it is currently enabled. For more
BitLocker        information, see Disable BitLocker.

Restart          This step restarts the computer in Windows PE by running the boot image
Computer in      assigned to the task sequence. You must use a boot image with Windows PE 4 or
Windows PE       later to pre-provision BitLocker. For more information, see Restart Computer.

Partition Disk   These steps format and partition the specified drive on the destination computer
0 - BIOS         by using BIOS or UEFI. The task sequence uses UEFI when it detects that the
                 destination computer is in UEFI mode. For more information, see Format and
Partition Disk   Partition Disk.
0 - UEFI

Pre-provision    This step enables BitLocker on a drive while in Windows PE. Only the used drive
BitLocker        space is encrypted. Because you partitioned and formatted the hard drive in the
                 previous step, there is no data, and encryption completes very quickly. For more
                 information, see Pre-provision BitLocker.

Apply            This step prepares the answer file that is used to install the operating system on
Operating        the destination computer and sets the OSDTargetSystemDrive task sequence
System           variable to the drive letter of the partition that contains the operating system
                 files. The answer file and variable are used by the Setup Windows and ConfigMgr
                 step to install the operating system. For more information, see Apply Operating
                 System Image.

Apply            This step adds Windows settings to the answer file. The answer file is used by the
Windows          Setup Windows and ConfigMgr step to install the operating system. For more
Settings         information, see Apply Windows Settings.

<!-- p.458 -->

 Task            Details
 sequence
 step

 Apply           This step adds Network settings to the answer file. The answer file is used by the
 Network         Setup Windows and ConfigMgr step to install the operating system. For more
 Settings        information, see Apply Network Settings Step.

 Apply Device    This step matches and installs drivers as part of the operating system
 Drivers         deployment. For more information, see Auto Apply Drivers.

 Setup           This step performs the transition from Windows PE to the new operating system.
 Windows and     This task sequence step is a required part of any operating system deployment. It
 ConfigMgr       installs the Configuration Manager client into the new operating system and
                 prepares for the task sequence to continue execution in the new operating
                 system. For more information, see Setup Windows and ConfigMgr.

 Enable          This step enables BitLocker encryption on the hard drive and sets key protectors.
 BitLocker       Because the hard drive was pre-provisioned with BitLocker, this step completes
                 very quickly. Windows 7 requires that you add a key protector. If you do not use
                 this step, you can run the manage-bde.exe command-line tool to set a key
                 protector. For more information, see Enable BitLocker.

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.459 -->

How to use task sequence variables in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The task sequence engine in the OS deployment feature of Configuration Manager uses
many variables to control its behaviors. Use these variables to:

      Set conditions on steps
      Change behaviors for specific steps
      Use in scripts for more complex actions

For a reference of all available task sequence variables, see Task sequence variables.

Types of variables
There are several types of variables:

      Built-in
      Action
      Custom
      Read-only
      Array

Built-in variables
Built-in variables provide information about the environment where the task sequence
runs. Their values are available throughout the whole task sequence. Typically, the task
sequence engine initializes built-in variables before it runs any steps.

For example, _SMSTSLogPath is an environment variable that specifies the path to which
Configuration Manager components write log files. Any task sequence step can access
this environment variable.

The task sequence evaluates some variables before each step. For example,
_SMSTSCurrentActionName lists the name of the current step.

Action variables

<!-- p.460 -->

Task sequence action variables specify configuration settings that a single task sequence
step uses. By default, the step initializes its settings before it runs. These settings are
available only while the associated task sequence step runs. The task sequence adds the
action variable value to the environment before it runs the step. It then removes the
value from the environment after the step runs.

For example, you add the Run Command Line step to a task sequence. This step
includes a Start In property. The task sequence stores a default value for this property as
the WorkingDirectory variable. The task sequence initializes this value before it runs the
Run Command Line step. While this step is running, access the Start In property value
from the WorkingDirectory value. After the step completes, the task sequence removes
the value of the WorkingDirectory variable from the environment. If the task sequence
includes another Run Command Line step, it initializes a new WorkingDirectory variable.
At that time, the task sequence sets the variable to the starting value for the current
step. For more information, see WorkingDirectory.

The default value for an action variable is present when the step runs. If you set a new
value, it's available to multiple steps in the task sequence. If you override a default value,
the new value stays in the environment. This new value overrides the default value for
other steps in the task sequence. For example, you add a Set Task Sequence Variable
step as the first step of the task sequence. This step sets the WorkingDirectory variable
to C:\ . Any Run Command Line step in the task sequence uses the new starting
directory value.

Some task sequence steps mark certain action variables as output. Steps later in the task
sequence read these output variables.

  ７ Note

  Not all task sequence steps have action variables. For example, although there are
  variables associated with the Enable BitLocker action, there are no variables
  associated with the Disable BitLocker action.

Custom variables
These variables are any that Configuration Manager doesn't create. Initialize your own
variables to use as conditions, in command lines, or in scripts.

When you specify a name for a new task sequence variable, follow these guidelines:

<!-- p.461 -->

         The task sequence variable name can include letters, numbers, the underscore
         character ( _ ), and a hyphen ( - ).

         Task sequence variable names have a minimum length of one character and a
         maximum length of 256 characters.

         User-defined variables must begin with a letter ( A-Z or a-z ).

         User-defined variable names can't begin with the underscore character. Only read-
         only task sequence variables are preceded by the underscore character.

         Task sequence variable names aren't case-sensitive. For example, OSDVAR and
         osdvar are the same task sequence variable.

         Task sequence variable names can't begin or end with a space. They also can't have
         embedded spaces. The task sequence ignores any spaces at the beginning or the
         end of a variable name.

There's no set limit to how many task sequence variables you can create. However, the
number of variables is limited by the size of the task sequence environment. The total
size limit for the task sequence environment is 8 KB. For more information, see Reduce
the size of task sequence policy.

Read-only variables
You can't change the value of some variables, which are read-only. Usually the name
begins with an underscore character ( _ ). The task sequence uses them for its
operations. Read-only variables are visible in the task sequence environment.

These variables are useful in scripts or command-lines. For example, running a
command line and piping the output to a log file in _SMSTSLogPath with the other log
files.

   ７ Note

   Read-only task sequence variables can be read by steps in a task sequence but they
   can't be set. For example, use a read-only variable as part of the command line for
   a Run Command Line step. You can't set a read-only variable by using the Set Task
   Sequence Variable step.

Array variables

<!-- p.462 -->

The task sequence stores some variables as an array. Each element in the array
represents the settings for a single object. Use these variables when a device has more
than one object to configure. The following task sequence steps use array variables:

     Apply Network Settings

     Format and Partition Disk

How to set variables
For custom variables or variables that aren't read-only, there are several methods to
initialize and set the value of the variable:

     Set Task Sequence Variable step
     Set Dynamic Variables step
     Run PowerShell Script step
     Collection and device variables
     TSEnvironment COM object
     Prestart command
     Task Sequence Wizard
     Task Sequence Media Wizard

Delete a variable from the environment by using the same methods as creating a
variable. To delete a variable, set the variable value to an empty string.

You can combine methods to set a task sequence variable to different values for the
same sequence. For example, set the default values using the task sequence editor, and
then set custom values using a script.

If you set the same variable by different methods, the task sequence engine uses the
following order:

   1. It evaluates collection variables first.

   2. Device-specific variables override the same variable set on a collection.

   3. Variables set by any method during the task sequence take precedence over
     collection or device variables.

General limitations for task sequence variable values
     Task sequence variable values can't be more than 4,000 characters.

<!-- p.463 -->

     You can't change a read-only task sequence variable. Read-only variables have
     names that start with an underscore character ( _ ).

     Task sequence variable values can be case-sensitive depending on the usage of the
     value. In most cases, task sequence variable values aren't case-sensitive. A variable
     that includes a password is case-sensitive.

Set Task Sequence Variable
Use this step in the task sequence to set a single variable to a single value.

For more information, see Set Task Sequence Variable.

Set Dynamic Variables
Use this step in the task sequence to set one or more task sequence variables. You
define rules in this step to determine which variables and values to use.

For more information, see Set Dynamic Variables.

Run PowerShell Script
Use this step in the task sequence to use a PowerShell script to set a task sequence
variable.

You can specify a script name from a package, or directly enter a PowerShell script in the
step. Then use the step property to Output to task sequence variable to save the script
output to a custom task sequence variable.

For more information on this step, see Run PowerShell Script.

  ７ Note

  You can also use a PowerShell script to set one or more variables with the
  TSEnvironment object. For more information, see How to use variables in a
  running task sequence in the Configuration Manager SDK.

Example scenario with Run PowerShell Script step
Your environment has users in multiple countries/regions, so you want to query the OS
language to set as a condition on multiple language-specific Apply OS steps.

<!-- p.464 -->

1. Add an instance of the Run PowerShell Script to the task sequence before the
  Apply OS steps.

2. Use the option to Enter a PowerShell script to specify the following command:

    PowerShell

    (Get-Culture).TwoLetterISOLanguageName

  For more information on the cmdlet, see Get-Culture. For more information on the
  two-letter ISO language names, see List of ISO 639-1 codes .

3. For the option to Output to task sequence variable, specify CurrentOSLanguage .

4. On the Apply OS step for the English language image, create the following
  condition: Task Sequence Variable CurrentOSLanguage equals "en"

<!-- p.465 -->

         Tip

        For more information on how to create a condition on a step, see How to
        access variables - Step condition.

   5. Save and deploy the task sequence.

When the Run PowerShell Script step runs on a device with the English language
version of Windows, the command returns the value en . It then saves that value into the
custom variable. When the Apply OS step for the English language image runs on the
same device, the condition evaluates to true. If you have multiple instances of the Apply
OS step for different languages, the task sequence dynamically runs the step that
matches the OS language.

Collection and device variables
You can define custom task sequence variables for devices and collections. Variables that
you define for a device are referred to as per-device task sequence variables. Variables
defined for a collection are referred to as per-collection task sequence variables. If
there's a conflict, per-device variables take precedence over per-collection variables.
This behavior means that task sequence variables that are assigned to a specific device
automatically have a higher priority than variables that are assigned to the collection
that contains the device.

<!-- p.466 -->

For example, device XYZ is a member of collection ABC. You assign MyVariable to
collection ABC with a value of 1. You also assign MyVariable to device XYZ with a value
of 2. The variable that's assigned to XYZ has higher priority than the variable that's
assigned to collection ABC. When a task sequence with this variable runs on XYZ,
MyVariable has a value of 2.

You can hide per-device and per-collection variables so that they aren't visible in the
Configuration Manager console. When you use the option Do not display this value in
the Configuration Manager console, the value of the variable isn't displayed in the
console. The task sequence log file (smsts.log) or the task sequence debugger won't
show the variable value either. The variable can still be used by the task sequence when
it runs. If you no longer want these variables to be hidden, delete them first. Then
redefine the variables without selecting the option to hide them.

  ２ Warning

  If you include variables in the Run Command Line step's command line, the task
  sequence log file displays the full command line including the variable values. To
  prevent potentially sensitive data from appearing in the log file, set the task
  sequence variable OSDDoNotLogCommand to TRUE .

You can manage per-device variables at a primary site or at a central administration site.
Configuration Manager doesn't support more than 1,000 assigned variables for a device.

  ） Important

  When you use per-collection variables for task sequences, consider the following
  behaviors:

        Changes to collections are always replicated throughout the hierarchy. Any
        changes that you make to collection variables apply not just to members of
        the current site, but to all members of the collection throughout the hierarchy.

        When you delete a collection, this action also deletes the task sequence
        variables that you configured for the collection.

Create task sequence variables for a device

   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace, and select the Devices node.

<!-- p.467 -->

   2. Select the target device and select Properties.

   3. In the Properties dialog box, switch to the Variables tab.

   4. For each variable that you want to create, select the New icon. Specify the Name
     and Value of the task sequence variable. If you want to hide the variable so that it's
     not visible in the Configuration Manager console, select the option Do not display
     this value in the Configuration Manager console.

   5. After you've added all the variables to the device properties, select OK.

Create task sequence variables for a collection

   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace, and select the Device Collections node. Select the target collection and
     choose Properties.

   2. In the Properties dialog box, switch to the Collection Variables tab.

   3. For each variable that you want to create, select the New icon. Specify the Name
     and Value of the task sequence variable. If you want to hide the variable so that it's
     not visible in the Configuration Manager console, select the option Do not display
     this value in the Configuration Manager console.

   4. Optionally, specify the priority for Configuration Manager to use when the task
     sequence variables are evaluated.

   5. After you've added all the variables to the collection properties, select OK.

TSEnvironment COM object
To work with variables from a script, use the TSEnvironment object.

For more information, see How to use variables in a running task sequence in the
Configuration Manager SDK.

Prestart command
The prestart command is a script or executable that runs in Windows PE before the user
selects the task sequence. The prestart command can query a variable or prompt the
user for information, and then save it in the environment. Use the TSEnvironment COM
object to read and write variables from the prestart command.

For more information, see Prestart commands for task sequence media.

<!-- p.468 -->

Task Sequence Wizard
After you select a task sequence in the Task Sequence Wizard window, the page to edit
task sequence variables includes an Edit button. You can use accessible keyboard
shortcuts to edit the variables. This change helps in cases where a mouse isn't available.

Task Sequence Media Wizard
Specify variables for task sequences that run from media. When using media to deploy
the OS, you add the task sequence variables and specify their values when you create
the media. The variables and their values are stored on the media.

  ７ Note

  Task sequences are stored on stand-alone media. However, all other types of
  media, such as prestaged media, retrieve the task sequence from a management
  point.

When you run a task sequence from media, you can add a variable on the
Customization page of the wizard.

Use the media variables in place of per-collection or per-computer variables. If the task
sequence is running from media, per-computer and per-collection variables don't apply
and aren't used.

   Tip

  The task sequence writes the package ID and prestart command line to the
  CreateTSMedia.log file on the computer that runs the Configuration Manager
  console. This log file includes the value for any task sequence variables. Review this
  log file to verify the value for the task sequence variables.

For more information, see Create task sequence media.

How to access variables
After you specify the variable and its value by using one of the methods from the
previous section, use it in your task sequences. For example, access default values for
built-in task sequence variables, or make a step conditional on the value of a variable.

Use the following methods to access variable values in the task sequence environment:

<!-- p.469 -->

        Use in a step
        Step condition
        Custom script
        Windows setup answer file

Use in a step
Specify a variable value for a setting in a task sequence step. In the task sequence editor,
edit the step, and specify the variable name as the field value. Enclose the variable name
in percent signs ( % ).

For example, use the variable name as part of the Command Line field of the Run
Command Line step. The following command line writes the computer name to a text
file.

cmd.exe /c echo %_SMSTSMachineName% > C:\File.txt

Step condition
Use built-in or custom task sequence variables as part of a condition on a step or group.
The task sequence evaluates the variable value before it runs the step or group.

To add a condition that evaluates a variable value, do the following steps:

    1. In the task sequence editor, select the step or group to which you want to add the
        condition.

    2. Switch to the Options tab for the step or group. Click Add Condition, and select
        Task Sequence Variable.

    3. In the Task Sequence Variable dialog box, specify the following settings:

             Variable: The name of the variable. For example, _SMSTSInWinPE .

             Condition: The condition to evaluate the variable value. The following
             conditions are available:
                Exists
                Not exists
                Equals
                Not equals
                Greater than
                Greater than or equals
                Less than

<!-- p.470 -->

               Less than or equals
               Like (supports wildcards of * and ? )
               Not like (version 2103 or later)

           Value: The value of the variable to check. For example, false .

The three examples above form a common condition to test whether the task sequence
is running from a boot image in Windows PE:

  Task Sequence Variable _SMSTSInWinPE equals "false"

See this condition on the Capture Files and Settings group of the default task sequence
template to install an existing OS image.

For more information about conditions, see Task sequence editor - Conditions.

Custom script
Read and write variables by using the Microsoft.SMS.TSEnvironment COM object while
the task sequence is running.

The following Windows PowerShell example queries the _SMSTSLogPath variable to get
the current log location. The script also sets a custom variable.

  PowerShell

  # Create an object to access the task sequence environment
  $tsenv = New-Object -ComObject Microsoft.SMS.TSEnvironment

  # Query the environment to get an existing variable
  # Set a variable for the task sequence log path
  $LogPath = $tsenv.Value("_SMSTSLogPath")

  # Or, convert all of the variables currently in the environment to
  PowerShell variables
  $tsenv.GetVariables() | % { Set-Variable -Name "$_" -Value
  "$($tsenv.Value($_))" }

  # Write a message to a log file
  Write-Output "Hello world!" | Out-File -FilePath "$LogPath\mylog.log" -
  Encoding "Default" -Append

  # Set a custom variable "startTime" to the current time
  $tsenv.Value("startTime") = (Get-Date -Format HH:mm:ss) + ".000+000"

Windows setup answer file

<!-- p.471 -->

The Windows setup answer file that you supply can have embedded task sequence
variables. Use the form %varname% , where varname is the name of the variable. The
Setup Windows and ConfigMgr step replaces the variable name string for the actual
variable value. These embedded task sequence variables can't be used in numeric-only
fields in an unattend.xml answer file.

For more information, see Setup Windows and ConfigMgr.

See also
     Task sequence steps

     Task sequence variables

     Planning considerations for automating tasks

     Task sequence editor

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.472 -->

Task sequence variables
07/17/2025

Applies to: Configuration Manager (current branch)

This article is a reference for all of the available variables in alphabetical order. Use the browser
Find function (typically CTRL + F) to find a specific variable. The variable notes if it's specific to
particular step. The article on task sequence steps includes the list of variables specific to each
step.

For more information, see Using task sequence variables.

Task sequence variable reference

_OSDDetectedWinDir
The task sequence scans the computer's hard drives for a previous operating system
installation when Windows PE starts. The Windows folder location is stored in this variable. You
can configure your task sequence to retrieve this value from the environment and use it to
specify the same Windows folder location to use for the new operating system installation.

_OSDDetectedWinDrive
The task sequence scans the computer's hard drives for a previous operating system
installation when Windows PE starts. The hard drive location for where the operating system is
installed is stored in this variable. You can configure your task sequence to retrieve this value
from the environment and use it to specify the same hard drive location to use for the new
operating system.

_OSDMigrateUsmtPackageID
Applies to the Capture User State step.

(input)

Specifies the package ID of the Configuration Manager package that contains the USMT files.
This variable is required.

_OSDMigrateUsmtRestorePackageID

<!-- p.473 -->

Applies to the Restore User State step.

(input)

Specifies the package ID of the Configuration Manager package that contains the USMT files.
This variable is required.

_SMSTSAdvertID
Stores the current running task sequence deployment unique ID. It uses the same format as a
Configuration Manager software distribution deployment ID. If the task sequence is running
from stand-alone media, this variable is undefined.

Example
ABC20001

_SMSTSAppInstallNeedsRetry
Starting this Configuration Manager 2211 HFRU Kb 16643863 and above

Applies to the Install Application step.

This value is set to true if the previous application failed to install and is required to be retried.

This value is set to false otherwise.

_SMSTSAssetTag
Applies to the Set Dynamic Variables step.

Specifies the asset tag for the computer.

_SMSTSBootImageID
If the current running task sequence references a boot image package, this variable stores the
boot image package ID. If the task sequence doesn't reference a boot image package, this
variable isn't set.

Example
ABC00001

<!-- p.474 -->

_SMSTSBootUEFI
The task sequence sets this variable when it detects a computer that's in UEFI mode.

_SMSTSClientCache
The task sequence sets this variable when it caches content on the local drive. The variable
contains the path to the cache. If this variable doesn't exist, then there's no cache.

_SMSTSClientGUID
Stores the value of Configuration Manager client GUID. If the task sequence is running from
standalone media, this variable isn't set.

Example
0a1a9a4b-fc56-44f6-b7cd-c3f8ee37c04c

_SMSTSCurrentActionName
Specifies the name of the currently running task sequence step. This variable is set before the
task sequence manager runs each individual step.

Example
run command line

_SMSTSDefaultGateways
Applies to the Set Dynamic Variables step.

Specifies the default gateways used by the computer.

_SMSTSDownloadOnDemand
If the current task sequence is running in download-on-demand mode, this variable is true .
Download-on-demand mode means the task sequence manager downloads content locally
only when it must access the content.

_SMSTSInWinPE

<!-- p.475 -->

When the current task sequence step is running in Windows PE, this variable is true . Test this
task sequence variable to determine the current OS environment.

_SMSTSIPAddresses
Applies to the Set Dynamic Variables step.

Specifies the IP addresses used by the computer.

_SMSTSLastActionName
Stores the name of the last action that was run. This variable relates to
_SMSTSLastActionRetCode. The task sequence logs these values to the smsts.log file. This
variable is beneficial when troubleshooting a task sequence. When a step fails, a custom script
can include the step name along with the return code.

_SMSTSLastActionRetCode
Stores the return code from the last action that was run. This variable can be used as a
condition to determine if the next step is run.

Example
0

_SMSTSLastActionSucceeded
     If the last step succeeded, this variable is true .

     If the last step failed, it's false .

     If the task sequence skipped the last action, because the step is disabled or the associated
     condition evaluated to false, this variable isn't reset. It still holds the value for the
     previous action.

_SMSTSLastContentDownloadLocation
This variable contains the last location where the task sequence downloaded or attempted to
download content. Inspect this variable instead of parsing the client logs for this content
location.

<!-- p.476 -->

_SMSTSLaunchMode
Specifies that the task sequence started via one of the following methods:

     SMS: The Configuration Manager client, such as when a user starts it from Software
     Center
     UFD: Legacy USB media
     UFD+FORMAT: Newer USB media
     CD: A bootable CD
     DVD: A bootable DVD
     PXE: Network boot with PXE
     HD: Prestaged media on a hard disk

_SMSTSLogPath
Stores the full path of the log directory. Use this value to determine where the task sequence
steps log their actions. This value isn't set when a hard drive isn't available.

_SMSTSMacAddresses
Applies to the Set Dynamic Variables step.

Specifies the MAC addresses used by the computer.

_SMSTSMachineName
Stores and specifies the computer name. Stores the name of the computer that the task
sequence uses to log all status messages. To change the computer name in the new OS, use
the OSDComputerName variable.

_SMSTSMake
Applies to the Set Dynamic Variables step.

Specifies the make of the computer.

_SMSTSMDataPath
Specifies the path defined by the SMSTSLocalDataDrive variable. This path specifies where the
task sequence stores temporary cache files on the destination computer while it's running.
When you define SMSTSLocalDataDrive before the task sequence starts, such as by setting a

<!-- p.477 -->

collection variable, Configuration Manager then defines the _SMSTSMDataPath variable once
the task sequence starts.

_SMSTSMediaType
Specifies the type of media used to initiate the installation, which includes:

      BootMedia : Boot Media

      FullMedia : Full Media

      PXE : PXE
      OEMMedia : Prestaged Media

_SMSTSModel
Applies to the Set Dynamic Variables step.

Specifies the model of the computer.

_SMSTSMP
Stores the URL or IP address of a Configuration Manager management point.

_SMSTSMPPort
Stores the port number of a Configuration Manager management point.

_SMSTSOrgName
Stores the branding title name that the task sequence displays in the progress dialog.

_SMSTSOSUpgradeActionReturnCode
Applies to the Upgrade operating system step.

Stores the exit code value that Windows Setup returns to indicate success or failure. This
variable is useful with the /Compat command-line option.

Example

On the completion of a compat-only scan, take action in later steps depending on the failure
or success exit code. On success, initiate the upgrade. Or set a marker in the environment to

<!-- p.478 -->

collect with hardware inventory. For example, add a file or set a registry key. Use this marker to
create a collection of computers that are ready to upgrade, or that require action before
upgrade.

_SMSTSPackageID
Stores the current running task sequence ID. This ID uses the same format as a Configuration
Manager package ID.

Example
HJT00001

_SMSTSPackageName
Stores the current running task sequence name. A Configuration Manager administrator
specifies this name when creating the task sequence.

Example
Deploy Windows 10 task sequence

_SMSTSRunFromDP
Set to true if the current task sequence is running in run-from-distribution-point mode. This
mode means the task sequence manager obtains required package shares from distribution
point.

_SMSTSSerialNumber
Applies to the Set Dynamic Variables step.

Specifies the serial number of the computer.

_SMSTSSetupRollback
Specifies whether Windows Setup performed a rollback operation during an in-place upgrade.
The variable values can be true or false .

_SMSTSSiteCode

<!-- p.479 -->

Stores the site code of the Configuration Manager site.

Example
ABC

_SMSTSTimezone
This variable stores the time zone information in the following format:

Bias,StandardBias,DaylightBias,StandardDate.wYear,wMonth,wDayOfWeek,wDay,wHour,wMinute,wS
econd,wMilliseconds,DaylightDate.wYear,wMonth,wDayOfWeek,wDay,wHour,wMinute,wSecond,wMill

iseconds,StandardName,DaylightName

Example
For the time zone Eastern Time (US and Canada):

300,0,-60,0,11,0,1,2,0,0,0,0,3,0,2,2,0,0,0,Eastern Standard Time,Eastern Daylight Time

_SMSTSType
Specifies the type of the current running task sequence. It can have one of the following values:

      1: A generic task sequence
      2: An OS deployment task sequence

_SMSTSUseCRL
When the task sequence uses HTTPS to communicate with the management point, this variable
specifies whether it uses the certificate revocation list (CRL).

_SMSTSUserStarted
Specifies whether a user started the task sequence. This variable is set only if the task sequence
is started from Software Center. For example, if _SMSTSLaunchMode is set to SMS .

This variable can have the following values:

      true : Specifies that the task sequence is manually started by a user from Software Center.

<!-- p.480 -->

      false : Specifies that the task sequence is initiated automatically by the Configuration

     Manager scheduler.

_SMSTSUseSSL
Specifies whether the task sequence uses SSL to communicate with the Configuration Manager
management point. If you configure your site systems for HTTPS, the value is set to true .

_SMSTSUUID
Applies to the Set Dynamic Variables step.

Specifies the UUID of the computer.

_SMSTSWTG
Specifies if the computer is running as a Windows To Go device.

_TS_CRMEMORY
Applies to the Check Readiness step.

A read-only variable for whether the Minimum memory (MB) check returned true ( 1 ) or false
( 0 ). If you don't enable the check, the value of this read-only variable is blank.

_TS_CRSPEED
Applies to the Check Readiness step.

A read-only variable for whether the Minimum processor speed (MHz) check returned true ( 1 )
or false ( 0 ). If you don't enable the check, the value of this read-only variable is blank.

_TS_CRDISK
Applies to the Check Readiness step.

A read-only variable for whether the Minimum free disk space (MB) check returned true ( 1 ) or
false ( 0 ). If you don't enable the check, the value of this read-only variable is blank.

_TS_CROSTYPE
