---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 881-920"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0881-0920
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0881-0920
family: sccm
documentKind: "doc"
abstract: "ﾉ Expand table Name Description Install only matching Injects only the drivers that the target computer requires and that match drivers what is available in Out-of-Box Drivers Install all drivers Installs all drivers Selection profile Installs all drivers in the selected profile"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 881-920

<!-- p.881 -->

                                                                                       ﾉ   Expand table

 Name                        Description

 Install only matching       Injects only the drivers that the target computer requires and that match
 drivers                     what is available in Out-of-Box Drivers

 Install all drivers         Installs all drivers

 Selection profile           Installs all drivers in the selected profile

Install Application
This task sequence step installs applications on the target computer. For more
information about this step type, see Install Software.

The unique properties and settings for the Install Application task sequence step type
are:

Properties

                                                                                       ﾉ   Expand table

 Name               Description

 Type               Set this read-only type to Install Application.

Settings

                                                                                       ﾉ   Expand table

 Name                  Description

 Install multiple      Install mandatory applications that the MandatoryApplications property has
 applications          specified and optional applications that the Applications property has
                       specified. These properties are configured by rules or are specified during the
                       Deployment Wizard interview process. This is the default selection.

 Install a single      The specific application to install. You select the application from a drop-down
 application           list that consists of applications that have been configured in the Applications
                       node of the Deployment Workbench.

 Success codes         A space-delimited list of application installation exit codes that should be used
                       when determining the successful installation of applications.

<!-- p.882 -->

Install Operating System
This task sequence step installs an operating system on the target computer. MDT can
deploy Windows 8.1, Windows 8, Windows 7, Windows Server 2012 R2, Windows Server
2012, and Windows Server 2008 R2 using:

        setup.exe. This method is the traditional method used, initiated by running
        setup.exe from the installation media. MDT uses setup.exe by default.

        imagex.exe. This method installs the operating system image using imagex.exe
        with the /apply option. MDT uses this method when the setup.exe method cannot
        be used (i.e., it falls back to using imagex.exe).

        You can control which of these methods is used by using the ForceApplyFallback
        property, which also affects which operating system task sequences are listed in
        the Deployment Wizard for a specific processor architecture boot image. For more
        information, see the ForceApplyFallback property.

        The unique properties and settings for the Install Operating System task sequence
        step type are:

Properties

                                                                                 ﾉ   Expand table

 Name           Description

 Type           Set this read-only type to Install Operating System.

Settings

                                                                                 ﾉ   Expand table

 Name               Description

 Operating          The name of the operating system to be installed on the target computer. You
 system to          select the operating system from a drop-down list compiled from operating
 install            systems that have been configured in the Operating Systems node of the
                    Deployment Workbench.

 Disk               The disk on which to install the operating system.

 Partition          The partition on which to install the operating system.

<!-- p.883 -->

Install Roles and Features
This task sequence step installs the selected roles and features on the target computer.
For more information about which script accomplishes this task and the properties used,
see ZTIOSRole.wsf.

The unique properties and settings for the Install Roles and Features task sequence step
type are:

Properties

                                                                                 ﾉ   Expand table

 Name            Description

 Type            Set this read-only type to Install Roles and Features.

 Description     Informative text that describes the purpose of the task sequence step.

Settings

                                                                                 ﾉ   Expand table

 Name                                           Description

 Select the operating system for which the      Select the operating system to be deployed to the
 roles are to be installed                      target computer.

 Select the roles and features that should      Select one or more roles and features for
 be installed                                   installation on the target computer.

Install Language Packs Offline
This task sequence step installs updates to the image on the target computer after the
operating system has been deployed but before the target computer has been
restarted. These updates include language packs. For more information about which
script accomplishes this task and which properties you use, see ZTIPatches.wsf.

The unique properties and settings for the Install Language Packs Offline task sequence
step type are:

Properties

<!-- p.884 -->

                                                                               ﾉ   Expand table

 Name            Description

 Type            Set this read-only type to Install Updates Offline.

Settings

                                                                               ﾉ   Expand table

 Name              Description

 Package           The name of the language pack package that should be applied to the target
 Name              computer

  ７ Note

  This task sequence step is valid only when using MDT with Configuration Manager.

Install Language Packs Online
This task sequence step installs language packs to the image on the target computer
after the operating system has been deployed and after the target computer has been
restarted. For more information about which script accomplishes this task and which
properties you use, see ZTILangPacksOnline.wsf.

The unique properties and settings for the Install Language Packs Online task sequence
step type are:

Properties

                                                                               ﾉ   Expand table

 Name        Description

 Type        Set this read-only type to Install Language Packs Online.

Settings

                                                                               ﾉ   Expand table

<!-- p.885 -->

 Name           Description

 Package        The name of the language pack package that should be applied to the target
 Name           computer

  ７ Note

  This task sequence step is valid only when using MDT with Configuration Manager.

Install Updates Offline
This task sequence step installs updates to the image on the target computer after the
operating system has been deployed but before the target computer has been
restarted. These updates include language packs. For more information about which
script accomplishes this task and which properties you use, see ZTIPatches.wsf.

The unique properties and settings for the Install Updates Offline task sequence step
type are:

Properties

                                                                              ﾉ   Expand table

 Name         Description

 Type         Set this read-only type to Install Updates Offline.

Settings

                                                                              ﾉ   Expand table

 Name           Description

 Selection      The name of the selection profile that should be applied to the target computer
 Profile
                Note:

                When using MDT with Configuration Manager, specify the name of the update
                package that should be applied.

Recover from Domain Join Failure

<!-- p.886 -->

This task sequence step verifies that the target computer has joined a domain. The
unique properties and settings for the Recover from Domain Join Failure task sequence
step type are:

Properties

                                                                                     ﾉ   Expand table

 Name         Description

 Type         Set this read-only type to Recover from Domain Join Failure.

Settings

                                                                                     ﾉ   Expand table

 Name            Description

 Auto            The task sequence step attempts to join the target computer to a domain.
 recover

 Manual          If the target computer fails to join a domain, the task sequence step causes the Task
 recover         Sequencer to pause, allowing you to attempt to join the target computer to a
                 domain.

 No recover      If the target computer is not able to join a domain, the task sequence fails, stopping
                 the task sequence.

Restart computer
This task sequence step restarts the target computer. The unique properties and settings
for the Restart computer task sequence step type are:

Properties

                                                                                     ﾉ   Expand table

 Name             Description

 Type             Set this read-only type to Restart computer.

Settings

<!-- p.887 -->

                                                                                 ﾉ   Expand table

 Name                                Description

 None                                None

Run Command Line
This task sequence step runs the specified commands on the target computer. For more
information about this step type, see Run Command Line.

The unique properties and settings for the Run Command Line task sequence step type
are:

Properties

                                                                                 ﾉ   Expand table

 Name           Description

 Type           Set this read-only type to Run Command Line.

Settings

                                                                                 ﾉ   Expand table

 Name                          Description

 Command Line                  The commands to be run when this task sequence step is
                               processed

 Start in                      The starting folder for the application (The path must be a valid
                               path on the target computer.)

 Run this step as the          Allows specification of user credentials that will be used to run
 following account             the specified command

 Account                       The user credentials that will be used to run the specified
                               command

 Load the user's profile       When selected, loads the user profile for the specified account

Run PowerShell Script

<!-- p.888 -->

This task sequence step runs the specified Windows PowerShell™ script on the target
computer. For more information about what script accomplishes this task and which
properties are used, see ZTIPowerShell.wsf.

The unique properties and settings for the Run PowerShell Script task sequence step
type are:

Properties

                                                                                ﾉ   Expand table

 Name         Description

 Type         Set this read-only type to Run PowerShell Script.

Settings

                                                                                ﾉ   Expand table

 Name          Description

 PowerShell    The Windows PowerShell script to be run when this task sequence step is
 script        processed

 Parameters    The parameters to be passed to the Windows PowerShell script. These parameters
               should be specified the same as if you were adding them to the Windows
               PowerShell script from a command line.

               The parameters provided should be only those parameters the script consumes,
               not for the Windows PowerShell command line.

               The following example would be a valid value for this setting:

               -MyParameter1 MyValue1 -MyParameter2 MyValue2

               The following example would be an invalid value for this setting (bold items are
               incorrect):

               -nologo -executionpolicy unrestricted -File MyScript.ps1 -MyParameter1
               MyValue1 -MyParameter2 MyValue2

               The previous example is invalid, because the value includes Windows PowerShell
               command-line parameters (-nologo and -executionpolicy unrestricted).

  ７ Note

<!-- p.889 -->

  This task sequence step is natively available in System Center 2012 R2
  Configuration Manager as Run PowerShell Script in the General group.

Set Task Sequence Variable
This task sequence step sets the specified task sequence variable to the specified value.
For more information about this step type, see Set Task Sequence Variable.

The unique properties and settings for the Set Task Sequence Variable task sequence
step type are:

Properties

                                                                                    ﾉ   Expand table

 Name        Description

 Type        Set this read-only type to Set Task Sequence Variable.

Settings

                                                                                    ﾉ   Expand table

 Name                               Description

 Task Sequence Variable             The name of the variable to modify

 Value                              The value to assign to the specified variable

Uninstall Roles and Features
This task sequence step uninstalls the selected roles and features from the target
computer. For more information about which script accomplishes this task and the
properties used, see ZTIOSRole.wsf.

The unique properties and settings for the Uninstall Roles and Features task sequence
step type are:

Properties

<!-- p.890 -->

                                                                                  ﾉ   Expand table

 Name             Description

 Type             Set this read-only type to Uninstall Roles and Features.

 Description      Informative text that describes the purpose of the task sequence step.

Settings

                                                                                  ﾉ   Expand table

 Name                                           Description

 Select the operating system for which the      Select the operating system to be deployed to the
 roles are to be installed                      target computer.

 Select the roles and features that should      Select one or more roles and features for
 be installed                                   unstallation from the target computer.

Validate
This task sequence step verifies that the target computer meets the specified
deployment prerequisite conditions. The unique properties and settings for the Validate
task sequence step type are:

Properties

                                                                                  ﾉ   Expand table

 Name               Description

 Type               Set this read-only type to Validate.

Settings

                                                                                  ﾉ   Expand table

 Name                        Description

 Ensure minimum              When selected, this step verifies that the amount of memory, in
 memory                      megabytes, installed on the target computer meets or exceeds the
                             amount specified. This is a default selection.

<!-- p.891 -->

 Name                     Description

 Ensure minimum           When selected, this step verifies that the speed of the processor, in
 processor speed          megahertz (MHz), installed in the target computer meets or exceeds
                          the amount specified. This is a default selection.

 Ensure specified image   When selected, this step verifies that the amount of free disk space, in
 size will fit            megabytes, on the target computer meets or exceeds the amount
                          specified.

 Ensure current           When selected, this step verifies that the operating system installed on
 operating system to      the target computer meets the requirement specified. This is a default
 be refreshed             selection.

  ７ Note

  This task sequence step is natively available in System Center 2012 R2
  Configuration Manager as Check Readiness in the General group.

Out-of-Box Task Sequence Steps
The following task sequence steps are referenced by one or more of the available task
sequence templates included with MDT. Each of the following examples lists the
preconfigured properties, parameters, and options and can be used as a basis for
building custom task sequences.

Only the task sequence step properties, parameters, and options, and their
corresponding values are listed in the examples.

  ７ Note

  For more information about each task sequence step, see the corresponding topics
  in Common Properties and Options for Task Sequence Step Types and Specific
  Properties and Settings for Task Sequence Step Types.

Apply Network Settings
This task sequence step configures the network adapter on the target computer.
Following is a brief listing of the settings that show how this step was originally
configured in one of the MDT task sequence templates. For more information about
which script accomplishes this task and which properties are used, see ZTINICConfig.wsf.

<!-- p.892 -->

The default configuration of the Apply Network Settings task sequence step is:

Properties

                                                                                  ﾉ   Expand table

 Name                               Value

 Type                               Apply Network Settings

 Name                               Apply Network Settings

 Description                        Not specified

Settings

                                                                                  ﾉ   Expand table

 Name    Value

         No parameters are preconfigured for this step. This causes this step, by default, to
         configure the network adapter to use DHCP.

Options

                                                                                  ﾉ   Expand table

 Name                                                        Value

 Disable this step                                           Not selected

 Success codes                                               0 3010

 Continue on error                                           Not selected

 Conditional qualifier                                       Not specified

  ７ Note

  When using the CustomSettings.ini file to specify the network adapter
  configurations, only the first network adapter will be configured. Edit ZTIGather.xml
  to configure additional network adapters.

<!-- p.893 -->

Apply Patches
This task sequence step installs updates to the image on the target computer after the
operating system has been deployed but before the target computer has been
restarted. Following is a brief listing of the settings that show how this step was
originally configured in one of the MDT task sequence templates. For more information
about which script accomplishes this task and which properties you use, see
ZTIPatches.wsf.

The default configuration of the Install Updates Offline task sequence step is:

Properties

                                                                                   ﾉ   Expand table

 Name                                  Value

 Type                                  Install Updates Offline

 Name                                  Apply Patches

 Description                           Not specified

Settings

                                                                                   ﾉ   Expand table

 Name                Value

 Selection           The name of the profile used when selecting the patches to install on the target
 profile             computer

Options

                                                                                   ﾉ   Expand table

 Name                                                            Value

 Disable this step                                               Not selected

 Success codes                                                   0 3010

 Continue on error                                               Not selected

<!-- p.894 -->

 Name                                                             Value

 Conditional qualifier                                            Not specified

Apply Windows PE
This task sequence step prepares the target computer to start in Windows
Preinstallation Environment (Windows PE). Following is a brief listing of the settings that
show how this step was originally configured in one of the MDT task sequence
templates. For more information about which script accomplishes this task and which
properties you use, see LTIApply.wsf.

The default configuration of the Apply Windows PE task sequence step is:

Properties

                                                                                  ﾉ   Expand table

 Name                                     Value

 Type                                     Run Command Line

 Name                                     Apply Windows PE

 Description                              Not specified

Settings

                                                                                  ﾉ   Expand table

 Name                                             Value

 Command line                                     cscript.exe "%SCRIPTROOT%\LTIApply.wsf" /PE

 Start in                                         Not specified

 Run this step as the following account           Not specified

Options

                                                                                  ﾉ   Expand table

<!-- p.895 -->

 Name                                                         Value

 Disable this step                                            Not selected

 Success codes                                                0 3010

 Continue on error                                            Not selected

 Conditional qualifier                                        Not specified

Backup
This task sequence step backs up the target computer before starting the operating
system deployment. Following is a brief listing of the settings that show how this step
was originally configured in one of the MDT task sequence templates. For more
information about which script accomplishes this task and which properties you use, see
ZTIBackup.wsf.

The default configuration of the Backup task sequence step is:

Properties

                                                                                 ﾉ   Expand table

 Name                                     Value

 Type                                     Run Command Line

 Name                                     Backup

 Description                              Not specified

Settings

                                                                                 ﾉ   Expand table

 Name                                              Value

 Command line                                      cscript.exe "%SCRIPTROOT%\ZTIBackup.wsf"

 Start in                                          Not specified

 Run this step as the following account            Not specified

<!-- p.896 -->

Options

                                                                          ﾉ   Expand table

 Name                                                    Value

 Disable this step                                       Not selected

 Success codes                                           0 3010

 Continue on error                                       Not selected

 Conditional qualifier                                   Not specified

Capture Groups
This task sequence step captures group membership of local groups that exist on the
target computer. Following is a brief listing of the settings that show how this step was
originally configured in one of the MDT task sequence templates. For more information
about which script accomplishes this task and which properties you use, see
ZTIGroups.wsf.

The default configuration of the Capture Groups task sequence step is:

Properties

                                                                          ﾉ   Expand table

 Name                               Value

 Type                               Run Command Line

 Name                               Capture Groups

 Description                        Not specified

Settings

                                                                          ﾉ   Expand table

 Name                                   Value

 Command line                           cscript.exe "%SCRIPTROOT%\ZTIGroups.wsf" /capture

 Start in                               Not specified.

<!-- p.897 -->

 Name                                        Value

 Run this step as the following account      Not specified

Options

                                                                               ﾉ   Expand table

 Name                                                          Value

 Disable this step                                             Not selected

 Success codes                                                 0 3010

 Continue on error                                             Not selected

 Conditional qualifier                                         Not specified

Capture User State
This task sequence step captures the user state for user profiles that exist on the target
computer. Following is a brief listing of the settings that show how this step was
originally configured in one of the MDT task sequence templates. For more information
about what script accomplishes this task and what properties are used, see
[ZTIUserState.wsf]((scripts.md#ztiuserstatewsf). For more information about this step
type, see Capture User State.

The default configuration of the Capture User State task sequence step is:

Properties

                                                                               ﾉ   Expand table

 Name                                     Value

 Type                                     Run Command Line

 Name                                     Capture User State

 Description                              Not specified

Settings

<!-- p.898 -->

                                                                               ﾉ   Expand table

 Name                                       Value

 Command line                               cscript.exe "%SCRIPTROOT%\ZTIUserState.wsf" /capture

 Start in                                   Not specified

 Run this step as the following account     Not specified

Options

                                                                               ﾉ   Expand table

 Name                                                        Value

 Disable this step                                           Not selected

 Success codes                                               0 3010

 Continue on error                                           Not selected

 Conditional qualifier                                       Not specified

Check BIOS
This task sequence step checks the basic input/output system (BIOS) of the target
computer to ensure that it is compatible with the operating system you are deploying.
Following is a brief listing of the settings that show how this step was originally
configured in one of the MDT task sequence templates. For more information about
which script accomplishes this task and which properties are used, see
[ZTIBIOSCheck.wsf]((scripts.md#ztibioscheckwsf).

The default configuration of the Check BIOS task sequence step is:

Properties

                                                                               ﾉ   Expand table

 Name                                     Value

 Type                                     Run Command Line

 Name                                     Check BIOS

<!-- p.899 -->

 Name                                     Value

 Description                              Not specified

Settings

                                                                                  ﾉ   Expand table

 Name                                             Value

 Command line                                     cscript.exe "%SCRIPTROOT%\ZTIBIOSCheck.wsf"

 Start in                                         Not specified

 Run this step as the following account           Not specified

Options

                                                                                  ﾉ   Expand table

 Name                                                             Value

 Disable this step                                                Not selected

 Success codes                                                    0 3010

 Continue on error                                                Not selected

 Conditional qualifier                                            Not specified

Configure
This task sequence step configures the Unattend.xml file with the required property
values that are applicable to the operating system you are deploying to the target
computer. Following is a brief listing of the settings that show how this step was
originally configured in one of the MDT task sequence templates. For more information
about which script accomplishes this task and which properties you use, see
[ZTIConfigure.wsf]((scripts.md#zticonfigurewsf).

The default configuration of the Configure task sequence step is:

Properties

<!-- p.900 -->

                                                                                  ﾉ   Expand table

 Name                                     Value

 Type                                     Run Command Line

 Name                                     Configure

 Description                              Not specified

Settings

                                                                                  ﾉ   Expand table

 Name                                             Value

 Command line                                     cscript.exe "%SCRIPTROOT%\ZTIConfigure.wsf"

 Start in                                         Not specified

 Run this step as the following account           Not specified

Options

                                                                                  ﾉ   Expand table

 Name                                                             Value

 Disable this step                                                Not selected

 Success codes                                                    0 3010

 Continue on error                                                Not selected

 Conditional qualifier                                            Not specified

Copy Scripts
This task sequence step copies the deployment scripts used during the deployment
processes to a local hard disk on the target computer. Following is a brief listing of the
settings that show how this step was originally configured in one of the MDT task
sequence templates. For more information about which script accomplishes this task
and which properties you use, see LTICopyScripts.wsf.

The default configuration of the Copy Scripts task sequence step is:

<!-- p.901 -->

Properties

                                                                                  ﾉ   Expand table

 Name                                     Value

 Type                                     Run Command Line

 Name                                     Copy Scripts

 Description                              Not specified

Settings

                                                                                  ﾉ   Expand table

 Name                                             Value

 Command line                                     cscript.exe "%SCRIPTROOT%\LTICopyScripts.wsf"

 Start in                                         Not specified

 Run this step as the following account           Not specified

Options

                                                                                  ﾉ   Expand table

 Name                                                             Value

 Disable this step                                                Not selected

 Success codes                                                    0 3010

 Continue on error                                                Not selected

 Conditional qualifier                                            Not specified

Copy Sysprep Files
This task sequence step copies the Sysprep files to the target computer. Following is a
brief listing of the settings that show how this step was originally configured in one of
the MDT task sequence templates. For more information about which script
accomplishes this task and which properties you use, see LTISysprep.wsf.

<!-- p.902 -->

The default configuration of the Copy Sysprep Files task sequence step is:

Properties

                                                                                ﾉ   Expand table

 Name                                     Value

 Type                                     Run Command Line

 Name                                     Copy Sysprep Files

 Description                              Not specified

Settings

                                                                                ﾉ   Expand table

 Name                                             Value

 Command line                                     cscript.exe "%SCRIPTROOT%\LTISysprep.wsf"

 Start in                                         Not specified

 Run this step as the following account           Not specified

Options

                                                                                ﾉ   Expand table

 Name                                                          Value

 Disable this step                                             Not selected

 Success codes                                                 0 3010

 Continue on error                                             Not selected

 Conditional qualifier                                         Not specified

Create BitLocker Partition
This task sequence step sets the BDEInstall property to True, indicating that BitLocker
should be installed on the target computer. The unique properties and settings for the

<!-- p.903 -->

Create BitLocker Partition task sequence step type are:

Properties

                                                                                  ﾉ   Expand table

 Name                         Value

 Type                         Set Task Sequence Variable

 Name                         Create BitLocker Partition

 Description                  None

Settings

                                                                                  ﾉ   Expand table

 Name                                                               Value

 Task Sequence Variable                                             BDE Install

 Value                                                              True

Options

                                                                                  ﾉ   Expand table

 Name                                                      Value

 Disable this step                                         Not selected

 Success codes                                             0 3010

 Continue on error                                         Not selected

 Conditional qualifier                                     Not specified

Create WIM
This task sequence step creates a backup of the target computer. The unique properties
and settings for the Create WIM task sequence step type are:

<!-- p.904 -->

Properties

                                                                                ﾉ   Expand table

 Name                                     Value

 Type                                     Run Command Line

 Name                                     Create WIM

 Description                              None

Settings

                                                                                ﾉ   Expand table

 Name                                             Value

 Command line                                     cscript.exe "%SCRIPTROOT%\ZTIBackup.wsf"

 Start in                                         Not specified

 Run this step as the following account           Not specified

Options

                                                                                ﾉ   Expand table

 Name                                                        Value

 Disable this step                                           Not selected

 Success codes                                               0 3010

 Continue on error                                           Not selected

 Conditional qualifier                                       Not specified

Disable BDE Protectors
If BitLocker is installed on the target computer, this task sequence step disables the
BitLocker protectors.

The unique properties and settings for the Disable BDE Protectors task sequence step
type are:

<!-- p.905 -->

Properties

                                                                           ﾉ   Expand table

 Name                             Value

 Type                             Run Command Line

 Name                             Disable BDE Protectors

 Description                      None

Settings

                                                                           ﾉ   Expand table

 Name                                 Value

 Command line                         cscript.exe
                                      "%SCRIPTROOT%\ZTIDisableBDEProtectors.wsf"

 Start in                             Not specified

 Run this step as the following       Not specified
 account

Options

                                                                           ﾉ   Expand table

 Name                                                      Value

 Disable this step                                         Not selected

 Success codes                                             0 3010

 Continue on error                                         Not selected

 Conditional qualifier                                     Not specified

Enable BitLocker
This task sequence step enables BitLocker on the target computer. Following is a brief
listing of the settings that show how this step was originally configured in one of the

<!-- p.906 -->

MDT task sequence templates. For more information about which script accomplishes
this task and what properties are used, see ZTIBde.wsf.

The default configuration of the Enable BitLocker task sequence step is:

Properties

                                                                           ﾉ   Expand table

 Name                                     Value

 Type                                     Enable BitLocker

 Name                                     Enable BitLocker

 Description                              None

Settings

                                                                           ﾉ   Expand table

 Name                                                         Value

 Current operating system drive                               Selected

 TPM only                                                     Selected

 Startup key on USB only                                      Not selected

 TPM and startup key on USB                                   Not selected

 Specific drive                                               Not selected

 In Active Directory                                          Selected

 Do not create a recovery key                                 Not selected

 Wait for BitLocker to complete                               Not selected

Options

                                                                           ﾉ   Expand table

 Name                             Value

 Disable this step                Not selected

<!-- p.907 -->

 Name                              Value

 Success codes                     0 3010

 Continue on error                 Not selected

 Conditional qualifier             BdeInstallSuppress does not equal YES

Enable OEM Disk Configuration
This task sequence step sets the DeploymentTypeproperty to NEWCOMPUTER, which
allows the target computer's disk to be partitioned and formatted.

The unique properties and settings for the Enable OEM Disk Configuration task
sequence step type are:

Properties

                                                                           ﾉ   Expand table

 Name                      Value

 Type                      Set Task Sequence Variable

 Name                      Enable OEM Disk Configuration

 Description               None

Settings

                                                                           ﾉ   Expand table

 Name                                                   Value

 Task Sequence Variable                                 DeploymentType

 Value                                                  NEWCOMPUTER

Options

                                                                           ﾉ   Expand table

<!-- p.908 -->

 Name                                                     Value

 Disable this step                                        Not selected

 Success codes                                            0 3010

 Continue on error                                        Not selected

 Conditional qualifier                                    Not specified

End Phase
This task sequence step ends the current deployment phase and restarts the target
computer. Following is a brief listing of the settings that show how this step was
originally configured in one of the MDT task sequence templates.

The default configuration of the End Phase task sequence step is:

Properties

                                                                          ﾉ   Expand table

 Name                                  Value

 Type                                  Restart computer

 Name                                  End Phase

 Description                           Not specified

Settings

                                                                          ﾉ   Expand table

 Name                                           Value

 None                                           None

Options

                                                                          ﾉ   Expand table

<!-- p.909 -->

 Name                                                         Value

 Disable this step                                            Not selected

 Success codes                                                0 3010

 Continue on error                                            Not selected

 Conditional qualifier                                        Not specified

Execute Sysprep
This task sequence step starts Sysprep on the target computer. Following is a brief
listing of the settings that show how this step was originally configured in one of the
MDT task sequence templates. For more information about what script accomplishes
this task and what properties are used, see LTISysprep.wsf.

The default configuration of the Execute Sysprep task sequence step is:

Properties

                                                                                ﾉ   Expand table

 Name                                     Value

 Type                                     Run Command Line

 Name                                     Execute Sysprep

 Description                              None

Settings

                                                                                ﾉ   Expand table

 Name                                             Value

 Command line                                     cscript.exe "%SCRIPTROOT%\LTISysprep.wsf"

 Start in                                         Not specified

 Run this step as the following account           Not specified

Options

<!-- p.910 -->

                                                                               ﾉ   Expand table

 Name                                                        Value

 Disable this step                                           Not selected

 Success codes                                               0 3010

 Continue on error                                           Not selected

 Conditional qualifier                                       Not specified

Force Diskpart Action
If the C:\oem.wsf file exists, this task sequence step deletes the C:\oem.wsf file, which
will allow the Format and Partition Disk task sequence step to run. Following is a brief
listing of the settings that show how this step was originally configured in one of the
MDT task sequence templates.

The default configuration of the Force Diskpart Action task sequence step is:

Properties

                                                                               ﾉ   Expand table

 Name                                Value

 Type                                Run Command Line

 Name                                Force Diskpart Action

 Description                         Not specified

Settings

                                                                               ﾉ   Expand table

 Name                                        Value

 Command line                                cmd.exe /c if exist c:\oem.wsf del /q c:\oem.wsf

 Start in                                    Not specified

 Run this step as the following account      Not specified

<!-- p.911 -->

Options

                                                                           ﾉ   Expand table

 Name                                                       Value

 Disable this step                                          Not selected

 Success codes                                              0.1

 Continue on error                                          Selected

 Conditional qualifier                                      None

Format and Partition Disk
This task sequence step configures and formats disk partitions on the target computer.
Following is a brief listing of the settings that show how this step was originally
configured in one of the MDT task sequence templates.

For more information about what script accomplishes this task and what properties are
used, see ZTIDiskpart.wsf.

The default configuration of the Format and Partition Disk task sequence step is:

Properties

                                                                           ﾉ   Expand table

 Name                           Value

 Type                           Format and Partition Disk

 Name                           Format and Partition Disk

 Description                    Not specified

Settings

                                                                           ﾉ   Expand table

 Name                Value

 Disk number         0

<!-- p.912 -->

Name                Value

Disk type           Standard (MBR)

Volume              Within the Volume setting, the following sub-settings are configured:

                    - Partition Name. OSDisk

                    - Partition Type. Primary

                    - Use a percentage of remaining space. Selected

                    - Size(%). 100

                    - Use specific drive size. Not selected

                    - Make this a boot partition. Selected

                    - File System. NTFS

                    - Quick Format. Selected

                    - Variable. Not specified

Options

                                                                                  ﾉ   Expand table

Name                                                          Value

Disable this step                                             Not selected

Success codes                                                 0 3010

Continue on error                                             Not selected

Conditional qualifier                                         Not specified

 ７ Note

 When using the CustomSettings.ini file to specify the hard disk and partition
 configurations, only the first hard disk and first two partitions will be configured.
 Edit ZTIGather.xml to configure additional hard disks or partitions.

Gather local only

<!-- p.913 -->

This task sequence step gathers deployment configurations settings from local sources
that apply to the target computer. Following is a brief listing of the settings that show
how this step was originally configured in one of the MDT task sequence templates.

For more information about what script accomplishes this task and what properties are
used, see ZTIGather.wsf.

The default configuration of the Gather local only task sequence step is:

Properties

                                                                                ﾉ   Expand table

 Name                                   Value

 Type                                   Gather

 Name                                   Gather local only

 Description                            Not specified

Settings

                                                                                ﾉ   Expand table

 Name                                                                Value

 Gather only local data                                              Selected

 Gather local data and process rules                                 Not selected

 Rules file                                                          Not specified

Options

                                                                                ﾉ   Expand table

 Name                                                       Value

 Disable this step                                          Not selected

 Success codes                                              0 3010

 Continue on error                                          Not selected

<!-- p.914 -->

 Name                                                       Value

 Conditional qualifier                                      None

Generate Application Migration File
This task sequence step generates the ZTIAppXmlGen.xml file, which contains a list of
file associations that are installed on the target computer. Following is a brief listing of
the settings that show how this step was originally configured in one of the MDT task
sequence templates.

For more information about what script accomplishes this task and what properties are
used, see ZTIAppXmlGen.wsf.

The default configuration of the Generate Application Migration File task sequence
step is:

Properties

                                                                              ﾉ   Expand table

 Name                      Value

 Type                      Run Command Line

 Name                      Generate Application Migration File

 Description               Not specified

Settings

                                                                              ﾉ   Expand table

 Name                                      Value

 Command Line                              cscript.exe "%SCRIPTROOT%\ZTIAppXmlGen.wsf" /capture

 Start in                                  Not specified

 Run this step as the following account    Not specified

Options

<!-- p.915 -->

                                                                                 ﾉ   Expand table

 Name                                                             Value

 Disable this step                                                Not selected

 Success codes                                                    0 3010

 Continue on error                                                Not selected

 Conditional qualifier                                            None

Inject Drivers
This task sequence step injects drivers that have been configured for deployment to the
target computer. Following is a brief listing of the settings that show how this step was
originally configured in one of the MDT task sequence templates.

For more information about what script accomplishes this task and what properties are
used, see ZTIDrivers.wsf.

The default configuration of the Inject Drivers task sequence step is:

Properties

                                                                                 ﾉ   Expand table

 Name                                            Value

 Type                                            Inject Drivers

 Name                                            Inject Drivers

 Description                                     Not specified

Settings

                                                                                 ﾉ   Expand table

 Name                    Value

 Install only            Injects only the drivers which are required by the target computer and
 matching drivers        match with what is available in Out-of-Box Drivers

 Install all drivers     Injects all drivers

<!-- p.916 -->

 Name                    Value

 Selection profile       Injects drivers which are associated with the selected profile

Options

                                                                                    ﾉ     Expand table

 Name                                                            Value

 Disable this step                                               Not selected

 Success codes                                                   0 3010

 Continue on error                                               Not selected

 Conditional qualifier                                           Not specified

Install Applications
This task sequence step installs applications on the target computer. Following is a brief
listing of the settings that show how this step was originally configured in one of the
MDT task sequence templates.

For more information about what script accomplishes this task and what properties are
used, see ZTIApplications.wsf.

The default configuration of the Install Applications task sequence step is:

Properties

                                                                                    ﾉ     Expand table

 Name                                     Value

 Type                                     Install Applications

 Name                                     Install Applications

 Description                              Not specified

Settings

<!-- p.917 -->

                                                                                    ﾉ   Expand table

 Name                                                                Value

 Install multiple applications                                       Selected

 Install a single application                                        Not selected

Options

                                                                                    ﾉ   Expand table

 Name                                                       Value

 Disable this step                                          Not selected

 Success codes                                              0 3010

 Continue on error                                          Not selected

 Conditional qualifier                                      Not specified

Install Operating System
This task sequence step installs an operating system on the target computer. Following
is a brief listing of the settings that show how this step was originally configured in one
of the MDT task sequence templates.

The default configuration of the Install Operating System task sequence step is:

Properties

                                                                                    ﾉ   Expand table

 Name                            Value

 Type                            Install Operating System

 Name                            Install Operating System

 Description                     Not specified

Settings

<!-- p.918 -->

                                                                                   ﾉ    Expand table

 Name                    Value

 Operating system to     This value corresponds to the operating system that was selected when
 install                 the task sequence was created.

 Disk                    The disk where the operating system is to be installed.

 Partition               The partition where the operating system is to be installed.

Options

                                                                                   ﾉ    Expand table

 Name                                                        Value

 Disable this step                                           Not selected

 Success codes                                               0 3010

 Continue on error                                           Not selected

 Conditional qualifier                                       Not specified

Next Phase
This task sequence step updates the Phase property to the next phase in the
deployment process. Following is a brief listing of the settings that show how this step
was originally configured in one of the MDT task sequence templates.

For more information about what script accomplishes this task and what properties are
used, see ZTINextPhase.wsf.

The default configuration of the Next Phase task sequence step is:

Properties

                                                                                   ﾉ    Expand table

 Name                                   Value

 Type                                   Run Command Line

 Name                                   Next Phase

<!-- p.919 -->

 Name                                     Value

 Description                              Not specified

Settings

                                                                                  ﾉ   Expand table

 Name                                             Value

 Command line                                     cscript.exe "%SCRIPTROOT%\ZTINextPhase.wsf"

 Start in                                         Not specified

 Run this step as the following account           Not specified

Options

                                                                                  ﾉ   Expand table

 Name                                                             Value

 Disable this step                                                Not selected

 Success codes                                                    0 3010

 Continue on error                                                Not selected

 Conditional qualifier                                            Not specified

Post-Apply Cleanup
This task sequence step cleans up unnecessary files after the installation of an image on
the target computer. Following is a brief listing of the settings that show how this step
was originally configured in one of the MDT task sequence templates.

For more information about what script accomplishes this task and what properties are
used, see LTIApply.wsf.

The default configuration of the Post-Apply Cleanup task sequence step is:

Properties

<!-- p.920 -->

                                                                                  ﾉ   Expand table

 Name                                     Value

 Type                                     Run Command Line

 Name                                     Post-Apply Cleanup

 Description                              Not specified

Settings

                                                                                  ﾉ   Expand table

 Name                                             Value

 Command line                                     cscript.exe "%SCRIPTROOT%\LTIApply.wsf" /post

 Start in                                         Not specified

 Run this step as the following account           Not specified

Options

                                                                                  ﾉ   Expand table

 Name                                                             Value

 Disable this step                                                Not selected

 Success codes                                                    0 3010

 Continue on error                                                Not selected

 Conditional qualifier                                            Not specified

Recover from Domain
This task sequence step will verify the target computer has joined a domain. For more
information about which script accomplishes this task and which properties are used,
see ZTIDomainJoin.wsf.

The unique properties and settings for the Recover from Domain task sequence step
type are:
