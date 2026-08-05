---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1321-1360"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1321-1360
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1321-1360
family: sccm
documentKind: "doc"
abstract: "Value Description Location distribution\\Control Packages.xml ７ Note This XML file is managed by MDT and should not require modification. ﾉ Expand table Value Description Location distribution\\Control SelectionProfileGroups.xml ７ Note This XML file is managed by MDT and should no"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1321-1360

<!-- p.1321 -->

Value                       Description

Location                    distribution\Control

Packages.xml

 ７ Note

 This XML file is managed by MDT and should not require modification.

                                                                   ﾉ    Expand table

Value                       Description

Location                    distribution\Control

SelectionProfileGroups.xml

 ７ Note

 This XML file is managed by MDT and should not require modification.

                                                                   ﾉ    Expand table

Value                       Description

Location                    distribution\Control

SelectionProfiles.xml

 ７ Note

 This XML file is managed by MDT and should not require modification.

                                                                   ﾉ    Expand table

<!-- p.1322 -->

Value                         Description

Location                      distribution\Control

ServerManager.xml

 ７ Note

 This XML file is managed by MDT and should not require modification.

                                                                   ﾉ    Expand table

Value          Description

Location       program_files\Microsoft Deployment Toolkit\Bin

Settings.xml

 ７ Note

 This XML file is managed by MDT and should not require modification.

                                                                   ﾉ    Expand table

Value                         Description

Location                      distribution\Control

TaskSequenceGroups.xml

 ７ Note

 This XML file is managed by MDT and should not require modification.

                                                                   ﾉ    Expand table

<!-- p.1323 -->

 Value                               Description

 Location                            distribution\Control

TaskSequences.xml

  ７ Note

  This XML file is managed by MDT and should not require modification.

                                                                              ﾉ   Expand table

 Value                               Description

 Location                            distribution\Control

TS.xml

  ７ Note

  This XML file is managed by MDT and should not require modification.

                                                                              ﾉ   Expand table

 Value                 Description

 Location              distribution\Control\task_sequence_id

  ７ Note

  Task_sequence_id is a placeholder for the task sequence ID that was assigned to
  each task sequence when it was created in the Task Sequences node in the
  Deployment Workbench.

Wimscript.ini
This .ini file is an ImageX configuration file that contains the list of folders and files that
will be excluded from an image. It is referenced by ImageX during the LTI Capture Phase.

<!-- p.1324 -->

For assistance with customizing this file, see the section, "Create an ImageX
Configuration File," in the Windows Preinstallation Environment (Windows PE) User's
Guide.

                                                                         ﾉ      Expand table

 Value                    Description

 Location                 distribution\Tools\platform

ZTIBIOSCheck.xml
This XML file contains metadata about BIOSes for target computers. This file is edited
manually and is read by ZTIBIOSCheck.wsf. Extract the necessary information from a
target computer to create an entry in this XML file using the Microsoft Visual Basic®
Scripting Edition (VBScript) program (ZTIBIOS_Extract_Utility.vbs) that is embedded in
this XML file.

                                                                         ﾉ      Expand table

 Value                           Description

 Location                        distribution\Scripts

ZTIConfigure.xml
This XML file is used by the ZTIConfigure.wsf script to translate property values
(specified earlier in the deployment process) to configure settings in the Unattend.xml
file. This file is already customized to make the appropriate translations and should not
require further modification.

                                                                         ﾉ      Expand table

 Value                           Description

 Location                        distribution\Scripts

ZTIGather.xml

  ７ Note

<!-- p.1325 -->

  This XML file is preconfigured and should not require modification. Define custom
  properties in the CustomSettings.ini file or the MDT DB.

                                                                            ﾉ      Expand table

 Value                            Description

 Location                         distribution\Scripts

ZTIUserState_config.xml
This XML file is used by the ZTIUserState.wsf script as a default USMT configuration file.
This file is used by default if no custom configuration file is specified by the
USMTConfigFile property. See the Config.xml File topic in the USMT documentation for
more information on syntax and use.

                                                                            ﾉ      Expand table

 Value                            Description

 Location                         distribution\Scripts

ZTITatoo.mof
This .mof file, when imported into the WMI repository of the target computer using
Mofcomp.exe, creates the Microsoft_BDD_Info WMI class. This class contains
deployment-related information, such as:

     DeploymentMethod

     DeploymentType

     DeploymentTimestamp

     BuildID

     BuildName

     BuildVersion

     OSDPackageID

     OSDProgramName

<!-- p.1326 -->

     OSDAdvertisementID

     TaskSequenceID

     TaskSequenceName

     TaskSequenceVersion

                                                          ﾉ   Expand table

 Value                             Description

 Location                          distribution\Scripts

Related articles
     Task Sequence Steps.
     Properties.
     Scripts.
     Utilities.
     MDT Windows PowerShell Cmdlets.
     Tables and Views in the MDT DB.
     Windows 7 Feature Dependency Reference.
     UDI Reference.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1327 -->

Utilities
Article • 02/12/2024

The scripts used in LTI and ZTI reference utilities that perform specialized tasks
supporting the steps used during the deployment process. Use the following
information to help determine the correct utilities to include in actions and the valid
arguments to provide when running each utility.

The following information is provided for each utility:

      Name. Specifies the name of the utility

      Description. Provides a description of the purpose of the utility

      Location. Indicates the folder where the utility can be found; in the information for
      the location, the following variables are used:

         program_files. This variable points to the location of the Program Files folder on
         the computer where MDT is installed.

         distribution. This variable points to the location of the Distribution folder for
         the deployment share.

         platform. This variable is a placeholder for the operating system platform (x86
         or x64).

      Use.Provides the commands and options that can be specified

      Arguments and description.Indicates the valid arguments to be specified for the
      utility and a brief description of what each argument means

BCDBoot.exe
BCDBoot is a tool used to quickly set up a system partition or repair the boot
environment located on the system partition. The system partition is set up by copying a
small set of boot environment files from an installed Windows image. BCDBoot also
creates a Boot Configuration Data (BCD) store on the system partition, with a new boot
entry that enables Windows to boot to the installed Windows image.

                                                                            ﾉ   Expand table

<!-- p.1328 -->

 Value                Description

 Location             Included in the Windows source files

Arguments

                                                                           ﾉ   Expand table

 Value       Description

             See the command-line help provided by this utility.

BDDRun.exe
This utility is run as an action by the Task Sequencer for executables (such as a script or
other code) that require user interaction. By default, the task sequence cannot run an
executable that requires user interaction. However, this utility allows the Task Sequencer
to run an executable that requires user interaction.

The executable that requires user interaction is provided as an argument to this utility.
This utility runs the executable in a separate command environment.

  ７ Note

  This utility can only be used in LTI deployments. ZTI deployments prohibit any user
  interaction.

                                                                           ﾉ   Expand table

 Value                      Description

 Location                   distribution\Tools\platform

 Use                        BDDRun.exe commandline

Arguments

                                                                           ﾉ   Expand table

<!-- p.1329 -->

 Value                 Description

 commandline           The command to be run that requires user interaction

  ７ Note

  Put double quotation marks around any part of the command-line portion of the
  argument that contains blanks. For example: BDDRun.exe MyAppInstall.exe
  /destinationdir: "%ProgramFiles%\AppName" .

Bootsect.exe
Bootsect.exe updates the master boot code for hard disk partitions to switch between
BOOTMGR and NTLDR. Use this utility to restore the boot sector on the computer.

For more information on Bootsect.exe, see the section, "Bootsect Command-Line
Options," in the Windows Preinstallation Environment (Windows PE) User's Guide.

                                                                                  ﾉ   Expand table

 Value                        Description

 Location                     distribution\Tools\platform

 Use                          bootsect.exe /nt52 C:

Arguments

                                                                                  ﾉ   Expand table

 Value         Description

 /Help         Displays the use instructions listed here.

 /nt52         Applies the master boot code compatible with NTLDR to SYS, ALL, or DriveLetter.
               The operating system installed on SYS, ALL, or DriveLetter must be an earlier version
               of Windows Vista.

 /nt60         Applies the master boot code compatible with BOOTMGR to SYS, ALL, or
               DriveLetter. The operating system installed on SYS, ALL, or DriveLetter must be
               Windows Vista.

 SYS           Updates the master boot code on the system partition used to boot Windows.

<!-- p.1330 -->

 Value           Description

 All             Updates the master boot code on all partitions. ALL does not necessarily update the
                 boot code for each volume. Instead, this option updates the boot code on volumes
                 that can be used as Windows boot volumes, which excludes any dynamic volumes
                 not connected with an underlying disk partition. This restriction is present, because
                 the boot code must be located at the beginning of a disk partition.

 DriveLetter     Updates the master boot code on the volume associated with this drive letter. The
                 boot code will not be updated if either (1) DriveLetter is not associated with a
                 volume or (2) DriveLetter is associated with a volume not connected to an
                 underlying disk partition.

 /Force          Forcibly dismounts the volumes during the boot code update. Use this option with
                 caution.

Compact.exe
Displays or alters the compression of files on NTFS file system partitions.

                                                                                      ﾉ      Expand table

 Value                    Description

 Location                 Included in the Windows source files

Arguments

                                                                                      ﾉ      Expand table

 Value         Description

 /C            Compresses the specified files. Directories will be marked so that files added afterward
               will be compressed.

 /V            Decompresses the specified files. Directories will be marked so that files added
               afterward will not be compressed.

 /S            Performs the specified operation on files in the given directory and in all
               subdirectories. Default dir is the current directory.

 /A            Displays files with the hidden or system attributes. These files are omitted by default.

 /I            Continues performing the specified operation even after errors have occurred. By
               default, Compact.exe stops when an error is encountered.

<!-- p.1331 -->

 Value      Description

 /F         Forces the compress operation on all specified files, even those which are already
            compressed. Already-compressed files are skipped by default.

 /Q         Reports only the most essential information.

 filename   Specifies a pattern, file, or directory.

Diskpart.exe
Diskpart is a text-mode command interpreter that allows management of objects (disks,
partitions, or volumes) using scripts or direct input in a Command Prompt window.

For more information on Diskpart.exe, see the section, "Diskpart Command-Line
Options," in the Windows Preinstallation Environment (Windows PE) User's Guide.

                                                                                 ﾉ   Expand table

 Value                 Description

 Location              Included in the Windows PE source files

Arguments

                                                                                 ﾉ   Expand table

 Value        Description

              See the guide referenced in the utility description.

Expand.exe
This utility is run to expand (extract) files from compressed files.

                                                                                 ﾉ   Expand table

 Value            Description

 Location         Included in the Windows source files

 Use              Expand.exe -r wuredist.cab -F:wuRedist.xml %temp%

<!-- p.1332 -->

Arguments

                                                                                    ﾉ    Expand table

 Value         Description

 -r            Renames expanded files

 -D            Displays the list of files in the source directory

 Source        Source file specification (Wildcards can be used.)

 -F:Files      Name of files to expand from a .cab file

 Destination   Destination file | path specification (Destination can be a directory. If Source is
               multiple files and -r is not specified, Destination must be a directory.)

ImageX.exe
ImageX is a command-line utility that enables OEMs and corporations to capture,
modify, and apply file-based disk images for rapid deployment. ImageX works with WIM
files for copying to a network, or it can work with other technologies that use WIM
images, such as Windows Setup and Windows Deployment Services.

For more information about ImageX, see the section, "What is ImageX," in the Windows
Preinstallation Environment (Windows PE) User's Guide.

                                                                                    ﾉ    Expand table

 Value                        Description

 Location                     distribution\Tools\platform

Arguments

                                                                                    ﾉ    Expand table

 Value         Description

               See the guide referenced in the utility description.

Microsoft.BDD.PnpEnum.exe

<!-- p.1333 -->

This utility is run to enumerate Plug and Play devices installed on the target computer.

                                                                         ﾉ   Expand table

 Value                        Description

 Location                     distribution\Tools\platform

Arguments

                                                                         ﾉ   Expand table

 Value                                Description

 None                                 -

Mofcomp.exe
Mofcomp.exe is the Managed Object Format compiler that parses a file that contains
Managed Object Format statements and adds the classes and class instances defined in
the file to the WMI repository. Mofcomp.exe provides command-line help on the switch
use options.

                                                                         ﾉ   Expand table

 Value                  Description

 Location               Included in the Windows source files

Arguments

                                                                         ﾉ   Expand table

 Value         Description

               See the command-line help that this utility provides.

Netsh.exe
Netsh.exe is a command-line and scripting utility used to automate the configuration of
networking components. For more information about Netsh.exe, see The Netsh

<!-- p.1334 -->

Command-Line Utility.

                                                                                 ﾉ   Expand table

 Value                 Description

 Location              Included in the Windows source files

Arguments

                                                                                 ﾉ   Expand table

 Value   Description

         See the command-line help that this utility provides or the information found at the URL
         listed in the utility description.

Reg.exe
The Console Registry Tool is used to read and modify registry data.

                                                                                 ﾉ   Expand table

 Value                 Description

 Location              Included in the Windows source files

Arguments

                                                                                 ﾉ   Expand table

 Value        Description

              See the command-line help that this utility provides.

Regsvr32.exe
This utility is used to register files (.dll, .exe, .ocx, and so on) with the operating system.

                                                                                 ﾉ   Expand table

<!-- p.1335 -->

 Value                Description

 Location             Included in the Windows source files

Arguments

                                                                         ﾉ   Expand table

 Value        Description

 file         The name of the file to register or unregister

 /s           Runs the utility in silent mode

 /u           Unregisters the file

Wpeutil.exe
The Windows PE utility (Wpeutil) is a command-line utility with which various commands
can be run in a Windows PE session. For example, an administrator can shut down or
reboot Windows PE, activate or deactivate a firewall, configure language settings, and
initialize a network. MDT uses the utility to initialize Windows PE and network
connections, and start LTI deployments.

For more information on Wpeutil.exe, see the section, "Wpeutil Command-Line
Options," in the Windows Preinstallation Environment (Windows PE) User's Guide.

                                                                         ﾉ   Expand table

 Value               Description

 Location            Included in the Windows PE source files

Arguments

                                                                         ﾉ   Expand table

 Value       Description

             See the guide referenced in the utility description.

Related articles

<!-- p.1336 -->

     Task Sequence Steps.
     Properties.
     Scripts.
     Support Files.
     MDT Windows PowerShell Cmdlets.
     Tables and Views in the MDT DB.
     Windows 7 Feature Dependency Reference.
     UDI Reference.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1337 -->

MDT Windows PowerShell Cmdlets
Article • 02/12/2024

In addition to the Deployment Workbench, MDT deployment shares can be managed
using Windows PowerShell cmdlets. The MDT Windows PowerShell cmdlets are included
in a Windows PowerShell snap-in—Microsoft.BDD.PSSnapIn—which is included with the
installation of MDT.

The MDT cmdlets must be run from a Windows PowerShell console that has the MDT
Windows PowerShell snap-in loaded. For more information on how to start a Windows
PowerShell console that has the MDT Windows PowerShell snap-in loaded, see "Loading
the MDT Windows PowerShell Snap-In".

Table 7 lists the MDT Windows PowerShell cmdlets and provides a brief description of
each cmdlet. Each cmdlet is discussed in further detail in a subsequent section.

Table 7. MDT Windows PowerShell Cmdlets
                                                                              ﾉ   Expand table

 Cmdlet                         Description

 Add-MDTPersistentDrive         Adds a deployment share to the list of MDT persisted drives
                                that can be restored using the Restore-MDTPersistentDrive
                                cmdlet.

 Disable-MDTMonitorService      Disables the MDT monitoring services.

 Enable-MDTMonitorService       Enables the MDT monitoring services.

 Get-                           Displays the statistics of a deployment share, including the
 MDTDeploymentShareStatistics   number of entities per major folder in the deployment share.

 Get-MDTMonitorData             Displays the MDT monitoring information collected for one or
                                more monitored MTD deployments.

 Get-                           Returns the operating system catalog for a specific operating
 MDTOperatingSystemCatalog      system. If the operating system catalog does not exist or is out
                                of date, then the operating system catalog is regenerated.

 Get-MDTPersistentDrive         Displays the list of deployment shares that can be restored
                                using the Restore-MDTPersistentDrive cmdlet.

 Import-MDTApplication          Imports an application into a deployment share.

<!-- p.1338 -->

 Cmdlet                       Description

 Import-MDTDriver             Imports one or more device drivers into a deployment share.

 Import-MDTOperatingSystem    Imports one or more operating systems into a deployment
                              share.

 Import-MDTPackage            Imports one or more operating system packages into a
                              deployment share.

 Import-MDTTaskSequence       Imports a task sequence into a deployment share.

 New-MDTDatabase              Creates or upgrades an MDT DB database that is associated
                              with a deployment share.

 Remove-MDTMonitorData        Removes one or more MDT monitoring data items from the
                              collected MDT monitoring data in a deployment share.

 Remove-MDTPersistentDrive    Removes a deployment share from the list of MDT persisted
                              Windows PowerShell drives that can be restored using the
                              Restore-MDTPersistentDrive cmdlet.

 Restore-MDTPersistentDrive   Creates a Windows PowerShell drive for each deployment
                              share in the list of MDT persisted Windows PowerShell drives.

 Set-MDTMonitorData           Creates a new or updates an existing MDT monitoring data
                              item in the collected MDT monitoring data in a deployment
                              share.

 Test-MDTDeploymentShare      Verifies the integrity of a deployment share.

 Test-MDTMonitorData          Verifies that the MDT monitoring services is configured
                              correctly and running.

 Update-MDTDatabaseSchema     Updates the MDT DB database schema.

 Update-MDTDeploymentShare    Updates a deployment share.

 Update-MDTLinkedDS           Replicates content from a deployment share to a linked
                              deployment share.

 Update-MDTMedia              Replicates content from a deployment share to a deployment
                              media folder.

Add-MDTPersistentDrive
This section describes the Add-MDTPersistentDriveWindows PowerShell cmdlet. Run
this cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-in
loaded. For more information on how to start a Windows PowerShell console that has

<!-- p.1339 -->

the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

   Add-MDTPersistentDrive [-Name] <String> [[-InputObject] <PSObject>]
   [<CommonParameters>]

Description
This cmdlet adds an existing Windows PowerShell drive created using the MDTProvider
to a list of drives that are persisted in the Deployment Workbench or in a Windows
PowerShell session using the Restore-MDTPersistentDrive cmdlet. This cmdlet is called
when you create or open a deployment share in the Deployment Workbench.

  ７ Note

  The list of persisted MDTProvider drives is maintained on a per-user based in the
  user profile.

The list of persisted MDTProvider drives can be displayed using the Get-
MDTPersistentDrive cmdlet.

Parameters
This subsection provides information about the various parameters that can be used
with the Add-MDTPersistentDriveWindows cmdlet.

-Name <String>

Specifies the name of a Windows PowerShell drive created using the MDT provider and
corresponds to an existing deployment share. The name was created using the New-
PSDrive    cmdlet and specifying the MDTProvider in the PSProvider parameter.

For more information on how to create a new Windows PowerShell drive using the
MDTProvider and how to create a deployment share using Windows PowerShell, see the
section "Creating a Deployment Share Using Windows PowerShell" in the MDT
document, Microsoft Deployment Toolkit Samples Guide.

<!-- p.1340 -->

                                                                           ﾉ   Expand table

 Parameter                                                Value

 Required?                                                True

 Position?                                                2 and Named

 Default value                                            None

 Accept pipeline input?                                   True (ByValue)

 Accept wildcard characters?                              False

-InputObject <PSObject>
This parameter specifies a Windows PowerShell drive object that was created earlier in
the process. Enter a PSObject object, such as one generated by the New-PSDrive
cmdlet.

                                                                           ﾉ   Expand table

 Parameter                                                Value

 Required?                                                False

 Position?                                                3 and Named

 Default value                                            -

 Accept pipeline input?                                   True (ByValue)

 Accept wildcard characters?                              False

<CommonParameters>

This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

<!-- p.1341 -->

Outputs
This cmdlet outputs a PSObject type object for the Windows PowerShell drive object
was added to the list of persisted drives.

This cmdlet also outputs a String type object if the Verbose common parameter is
included.

Example 1
  PowerShell

  Add-MDTPersistentDrive -Name DS001

Description

This example adds the deployment share with the Windows PowerShell drive name of
DS001 to the list of persisted drives.

Example 2
  PowerShell

  $MDTPSDrive = New-PSDrive -Name "DS001" -PSProvider "MDTProvider" -Root
  "C:\DeploymentShare$" -Description "MDT Deployment Share" -NetworkPath
  \\WDG-MDT-01\DeploymentShare$ -Verbose
  Add-MDTPersistentDrive -InputObject $MDTPSDrive

Description
This example adds the Windows PowerShell drive name DS001, created by the New-
PSDrive     cmdlet, to the list of persisted MDT drives using the $MDTPSDrive variable.

Example 3
  PowerShell

  New-PSDrive -Name "DS001" -PSProvider "MDTProvider" -Root
  "C:\DeploymentShare$" -Description "MDT Deployment Share" -NetworkPath
  \\WDG-MDT-01\DeploymentShare$ -Verbose | Add-MDTPersistentDrive -Verbose

<!-- p.1342 -->

Description
This example adds the Windows PowerShell drive name DS001, created by the New-
PSDrive    cmdlet, to the list of persisted MDT drives by piping the newly created
Windows PowerShell drive object to the Add-MDTPersistentDrive cmdlet.

Disable-MDTMonitorService
This section describes the Disable-MDTMonitorService Windows PowerShell cmdlet.
Run this cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-
in loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

   Disable-MDTMonitorService [<CommonParameters>]

Description
This cmdlet disables the MDT monitoring service, which runs on the computer where
MDT is installed. The MDT monitoring service collects monitoring information that can
be displayed:

       In the Monitoring node in a deployment share in the Deployment Workbench

       Using the Get-MDTMonitorData cmdlet

       The MDT monitoring service can subsequently be enabled using the Enable-
       MDTMonitorService.

       For more information on the MDT monitoring service, see the section "Monitoring
       MDT Deployments" in the MDT document, Using the Microsoft Deployment Toolkit.

Parameters
This subsection provides information about the various parameters that can be used
with the Disable-MDTMonitorService cmdlet.

<!-- p.1343 -->

<CommonParameters>
This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can accessed by
typing the following command, and then pressing ENTER:

  PowerShell

   Get-Help about_CommonParameters

Outputs
This cmdlet outputs a String type object if the Verbose common parameter is included;
otherwise, no output is generated.

Example 1
  PowerShell

   Disable-MDTMonitorService

Description
This example disables the MDT monitoring service.

Enable-MDTMonitorService
This section describes the Enable-MDTMonitorService Windows PowerShell cmdlet. Run
this cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-in
loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

   Enable-MDTMonitorService [-EventPort] <Int32> [-DataPort] <Int32>
   [<CommonParameters>]

<!-- p.1344 -->

Description
This cmdlet enables the MDT monitoring service, which runs on the computer where
MDT is installed. The MDT monitoring service collects monitoring information that can
be displayed:

     In the Monitoring node in a deployment share in the Deployment Workbench.

     Using the Get-MDTMonitorData cmdlet

     The MDT monitoring service can be disabled using the Disable-
     MDTMonitorService.

     For more information on the MDT monitoring service, see the section "Monitoring
     MDT Deployments" in the MDT document, Using the Microsoft Deployment Toolkit.

Parameters
This subsection provides information about the various parameters that can be used
with the Enable-MDTMonitorService cmdlet.

-EventPort <Int32>

This parameter specifies the TCP port used as the event port for the MDT monitoring
service.

                                                                        ﾉ   Expand table

 Parameter                                                Value

 Required?                                                False

 Position?                                                2 and Named

 Default value                                            9800

 Accept pipeline input?                                   False

 Accept wildcard characters?                              False

-DataPort <Int32>

This parameter specifies the TCP port used as the data port for the MDT monitoring
service.

<!-- p.1345 -->

                                                                         ﾉ   Expand table

 Parameter                                                 Value

 Required?                                                 False

 Position?                                                 3 and Named

 Default value                                             9801

 Accept pipeline input?                                    False

 Accept wildcard characters?                               False

<CommonParameters>
This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

Outputs
This cmdlet outputs a String type object if the Verbose common parameter is included;
otherwise, no output is generated.

Example 1
  PowerShell

  Enable-MDTMonitorService

Description

This example enables the MDT monitoring service on the local computer using the
default value of 9800 for the event port and the value of 9801 for the data port on the
MDT monitoring service.

<!-- p.1346 -->

Example 2
  PowerShell

  Enable-MDTMonitorService -EventPort 7000 -DataPort 7001

Description
This example enables the MDT monitoring service on the local computer using the value
of 7000 for the event port and the value of 7001 for the data port on the MDT
monitoring service.

Get-MDTDeploymentShareStatistics
This section describes the Get-MDTDeploymentShareStatistics Windows PowerShell
cmdlet. Run this cmdlet from a Windows PowerShell console that has the MDT
PowerShell snap-in loaded. For more information on how to start a Windows PowerShell
console that has the MDT PowerShell snap-in loaded, see "Loading the MDT Windows
PowerShell Snap-In".

Syntax
  PowerShell

  Get-MDTDeploymentShareStatistics [-Path <String>] [<CommonParameters>]

Description
This cmdlet displays the statistics of a deployment share based on the MDTProvder drive
that is specified in the Path parameter. The statistics include the number of items in the
specified deployment share:

     Applications

     Drivers

     Operating Systems

     Packages

     Task Sequences

<!-- p.1347 -->

     Selection Profiles

     Linked Deployment Shares

     MDT Media

     Computers in the MDT DB

     Make and Models in the MDT DB

     Locations in the MDT DB

     Roles in the MDT DB

  ７ Note

  The values for the statistics that relate to the MDT DB are not populated and always
  return a value of zero.

Parameters
This subsection provides information about the various parameters that can be used
with the Get-MDTDeploymentShareStatistics cmdlet.

-Path <String>

This parameter specifies the MDTProvider Windows PowerShell drive for the desired
deployment share.

  ７ Note

  If this parameter is not provided, then the Windows PowerShell working directory
  must default to a location within the desired MDTProvider Windows PowerShell
  drive.

                                                                        ﾉ   Expand table

 Parameter                                                Value

 Required?                                                False

 Position?                                                2 and Named

<!-- p.1348 -->

 Parameter                                                  Value

 Default value                                              -

 Accept pipeline input?                                     False

 Accept wildcard characters?                                False

<CommonParameters>
This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

Outputs
This cmdlet outputs a PSObject type object that contains the statistics for the
deployment share.

Example 1
  PowerShell

  Get-MDTDeploymentShareStatistics -Path DS001:

Description
This example returns the deployment share statistics for the deployment share that is
specified in the DS001: MDTProvider Windows PowerShell drive.

Example 2
  PowerShell

  cd DS001:
  Get-MDTDeploymentShareStatistics

<!-- p.1349 -->

Description
This example returns the deployment share statistics for the deployment share that is
specified in the DS001: MDTProvider Windows PowerShell drive. Use the cd command
to set the working directory for Windows PowerShell to the DS001: MDTProvider
Windows PowerShell drive.

Get-MDTMonitorData
This section describes the Get-MDTMonitorData Windows PowerShell cmdlet. Run this
cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-in
loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

   Get-MDTMonitorData [-Path <String>] [-ID <Nullable>] [<CommonParameters>]

Description
This cmdlet displays the MDT monitoring data that is being reported to the deployment
share that is specified in the Path parameter. The following is example output from this
cmdlet:

  PowerShell

   Name                : WDG-REF-01
   PercentComplete     : 100
   Settings            :
   Warnings            : 0
   Errors              : 0
   DeploymentStatus    : 3
   StartTime           : 5/23/2012 6:45:39 PM
   EndTime             : 5/23/2012 8:46:32 PM
   ID                  : 1
   UniqueID            : 94a0830e-f2bb-421c-b1e0-6f86f9eb9fa1
   CurrentStep         : 88
   TotalSteps          : 88
   StepName            :
   LastTime            : 5/23/2012 8:46:32 PM
   DartIP              :
   DartPort            :

<!-- p.1350 -->

  DartTicket         :
  VMHost             : WDG-HOST-01
  VMName             : WDG-REF-01
  ComputerIdentities : {}

  ７ Note

  The MDTProvider Windows PowerShell drive that this cmdlet references must exist
  prior to running this cmdlet.

Parameters
This subsection provides information about the various parameters that you can use
with the Get- MDTMonitorData cmdlet.

-Path <String>
This parameter specifies the MDTProvider Windows PowerShell drive for the desired
deployment share.

  ７ Note

  If this parameter is not provided, then the Windows PowerShell working directory
  must default to a location within the desired MDTProvider Windows PowerShell
  drive.

                                                                       ﾉ   Expand table

 Parameter                                               Value

 Required?                                               False

 Position?                                               2 and Named

 Default value                                           -

 Accept pipeline input?                                  False

 Accept wildcard characters?                             False

-ID <Nullable>

<!-- p.1351 -->

This parameter specifies the specific identifier for the deployment of a specific
computer. If this parameter is not specified, then all monitoring data for deployments in
the deployment share are displayed.

                                                                           ﾉ   Expand table

 Parameter                                                   Value

 Required?                                                   False

 Position?                                                   3 and Named

 Default value                                               -

 Accept pipeline input?                                      False

 Accept wildcard characters?                                 False

<CommonParameters>

This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

Outputs
This cmdlet outputs a PSObject type object for each monitored computer, which
contains the monitoring data for the computer.

Example 1
  PowerShell

  Get-MDTMonitorData -Path DS001:

Description

<!-- p.1352 -->

This example returns the monitoring data for all deployments in the deployment share
that is specified in the DS001: MDTProvider Windows PowerShell drive.

Example 2
  PowerShell

  cd DS001:
  Get-MDTMonitorData

Description

This example returns the monitoring data for all deployments in the deployment share
that is specified in the DS001: MDTProvider Windows PowerShell drive. Use the cd
command to set the working directory for Windows PowerShell to the DS001:
MDTProvider Windows PowerShell drive.

Example 3
  PowerShell

  Get-MDTMonitorData -Path DS001: -ID 22

Description
This example returns the monitoring data for the deployment with an ID of 22 in the
deployment share that is specified in the DS001: MDTProvider Windows PowerShell
drive.

Get-MDTOperatingSystemCatalog
This section describes the Get-MDTOperatingSystemCatalog Windows PowerShell
cmdlet. Run this cmdlet from a Windows PowerShell console that has the MDT
PowerShell snap-in loaded. For more information on how to start a Windows PowerShell
console that has the MDT PowerShell snap-in loaded, see "Loading the MDT Windows
PowerShell Snap-In".

Syntax

<!-- p.1353 -->

  PowerShell

  Get-MDTOperatingSystemCatalog [-ImageFile] <String> [-Index] <Int32>
  [<CommonParameters>]

Description
This cmdlet retrieves or creates an operating system catalog for a custom operating
system image so that you can modify the corresponding unattend.xml file using
Windows System Image Manager (WSIM). If no operating system catalog is available or
if the existing operating system catalog is invalid or out of date, this cmdlet will
generate a new operating system catalog.

  ７ Note

  The process of generating a new operating system catalog may take a long time as
  the custom operating system image must be mounted, inspected, and unmounted
  before the operating system catalog creation completes.

Parameters
This subsection provides information about the various parameters that can be used
with the Get-MDTOperatingSystemCatalog cmdlet.

-ImageFile <String>
This parameter specifies the fully qualified path to the custom operating system image
file (.wim file), including the name of the custom operating system image file.

                                                                            ﾉ   Expand table

 Parameter                                                    Value

 Required?                                                    True

 Position?                                                    2 and Named

 Default value                                                -

 Accept pipeline input?                                       False

 Accept wildcard characters?                                  False

<!-- p.1354 -->

-Index <Int32>
This parameter specifies the index of the desired operating system image within the
operating system image file (.wim file).

                                                                        ﾉ   Expand table

 Parameter                                                Value

 Required?                                                True

 Position?                                                3 and Named

 Default value                                            -

 Accept pipeline input?                                   False

 Accept wildcard characters?                              False

<CommonParameters>

This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

Outputs
This cmdlet outputs a PSObject type object that contains the path to the operating
system catalog.

Example 1
  PowerShell

  Get-MDTOperatingSystemCatalog -ImageFile "DS001:\Operating Systems\Windows
  8\sources\install.wim" -Index 2

Description

<!-- p.1355 -->

This example returns the operating system catalog for the operating system image at
the index of 2 in the operating system image file DS001:\Operating Systems\Windows
8\sources\install.wim.

Get-MDTPersistentDrive
This section describes the Get-MDTPersistentDrive Windows PowerShell cmdlet. Run
this cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-in
loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

   Get-MDTPersistentDrive [<CommonParameters>]

Description
This cmdlet displays the list of persisted MDT Windows PowerShell drives. The list of
persisted MDT Windows PowerShell drives is managed using the Add-
MDTPersistentDrive and Remove-MDTPersistentDrive cmdlets or the Deployment
Workbench.

The output from this cmdlet contains the following information:

       Windows PowerShell drive name, such as DS001

       Directory path, such as \\WDG-MDT-01\DeploymentShare$

       Persisted MDT Windows PowerShell drives are similar to persisted network drive
       mappings.

  ７ Note

  This list of persisted MDT Windows PowerShell drives is maintained on a per user
  basis and are stored in the user profile.

Parameters

<!-- p.1356 -->

This subsection provides information about the various parameters that can be used
with the Get- MDTPersistentDrive cmdlet.

<CommonParameters>

This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

   Get-Help about_CommonParameters

Outputs
This cmdlet outputs a PSObject type object for each MDT persisted drive that is
identical to the PSObject type object that the New-PSDrive   cmdlet returns.

Example 1
  PowerShell

   Get-MDTPersistentDrive

Description
This example displays a list of the MDT persisted drives.

Import-MDTApplication
This section describes the Import-MDTApplication Windows PowerShell cmdlet. Run
this cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-in
loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax

<!-- p.1357 -->

  PowerShell

  Import-MDTApplication [-Path <String>] -Name <String> ApplicationSourcePath
  <String> -DestinationFolder <String> [-Move] [<CommonParameters>]

-or-

  PowerShell

  Import-MDTApplication [-Path <String>] -Name <String> NoSource
  [<CommonParameters>]

-or-

  PowerShell

  Import-MDTApplication [-Path <String>] -Name <String> Bundle
  [<CommonParameters>]

Description
This cmdlet imports an application into a deployment share. The following application
types can be imported using this cmdlet:

       Applications that have source files, using the ApplicationSourcePath,
       DestinationFolder, and Move parameters. The first syntax example illustrates the
       use of this cmdlet for this type of application.

       Applications without source files or with source files located on other network
       shared folders using the NoSource parameter. The second syntax example
       illustrates the use of this cmdlet for this type of application.

       Application bundles, which are used to group a set of related applications, using
       the Bundle parameter. The last syntax example illustrates the use of this cmdlet for
       this type of application.

Parameters
This subsection provides information about the various parameters that can be used
with the Import-MDTApplication cmdlet.

-Path <String>

<!-- p.1358 -->

This parameter specifies the fully qualified path to an existing folder where the
application being imported will be placed within the deployment share. If the
DestinationFolder parameter is used, then the folder specified in the DestinationFolder
parameter is created beneath the folder specified in this parameter. This parameter is
used in all syntax usages for this cmdlet.

  ７ Note

  If this parameter is not provided, the Windows PowerShell working directory must
  default to the desired location within the deployment share.

                                                                          ﾉ   Expand table

 Parameter                                                            Value

 Required?                                                            False

 Position?                                                            Named

 Default value                                                        -

 Accept pipeline input?                                               False

 Accept wildcard characters?                                          False

-Name <String>

This parameter specifies the name of the application to be added to the deployments
share and must be unique within the deployment share. This parameter is used in all
syntax usages for this cmdlet.

                                                                          ﾉ   Expand table

 Parameter                                                            Value

 Required?                                                            True

 Position?                                                            Named

 Default value                                                        -

 Accept pipeline input?                                               False

 Accept wildcard characters?                                          False

<!-- p.1359 -->

-ApplicationSourcePath <String>
This parameter specifies the fully qualified path to the application source files for the
application that will be imported into the deployment share. This parameter is only valid
for use in the first syntax example.

                                                                           ﾉ   Expand table

 Parameter                                                             Value

 Required?                                                             True

 Position?                                                             Named

 Default value                                                         -

 Accept pipeline input?                                                False

 Accept wildcard characters?                                           False

-DestinationFolder <String>
This parameter specifies the folder in the deployment share where the application
source files are to be imported. This folder is created beneath the folder specified in the
Path parameter. This parameter is only valid for use in the first syntax example.

                                                                           ﾉ   Expand table

 Parameter                                                             Value

 Required?                                                             True

 Position?                                                             Named

 Default value                                                         -

 Accept pipeline input?                                                False

 Accept wildcard characters?                                           False

-Move [<SwitchParameter>]
This parameter specifies whether the application's source files should be moved (instead
of copied) from the folder where the application's source files are located, which is
specified in the ApplicationSourcePath parameter.

<!-- p.1360 -->

If this parameter is:

     Specified, then the files are moved and the files in the folder specified in the
     ApplicationSourcePath parameter are deleted

     Not specified, then the files are copied and the files in the folder specified in the
     ApplicationSourcePath parameter are retained

     This parameter is only valid for use in the first syntax example.

                                                                              ﾉ   Expand table

 Parameter                                                               Value

 Required?                                                               False

 Position?                                                               Named

 Default value                                                           -

 Accept pipeline input?                                                  False

 Accept wildcard characters?                                             False

-NoSource [<SwitchParameter>]

This parameter specifies that the application being imported is an application that has
no source files to be copied. When using this parameter, the application source files are:

     On a network shared folder, which is specified in the application installation
     command line or working directory configuration settings

     Already present in the operating system image

     This parameter is only valid for use in the second syntax example.

                                                                              ﾉ   Expand table

 Parameter                                                   Value

 Required?                                                   False

 Position?                                                   Named

 Default value                                               -

 Accept pipeline input?                                      True (ByValue)
