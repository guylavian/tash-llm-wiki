---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1281-1320"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1281-1320
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1281-1320
family: sccm
documentKind: "doc"
abstract: "Value Description Output BDD.log contains events that all MDT scripts generate. References ZTIUtility.vbs includes support functions and subroutines that the script uses. Location distribution\\Scripts Use cscript ZTIModifyVol.wsf /UtilityVol:value </debug:value> Arguments ﾉ Expa"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1281-1320

<!-- p.1281 -->

 Value          Description

 Output         BDD.log contains events that all MDT scripts generate.

 References     ZTIUtility.vbs includes support functions and subroutines that the script uses.

 Location       distribution\Scripts

 Use            cscript ZTIModifyVol.wsf /UtilityVol:value </debug:value>

Arguments

                                                                                    ﾉ    Expand table

 Value               Description

 /UtilityVol:value   Provides the drive letter of the volume that needs to be configured for a
                     Windows RE Tools partition for use with computers with UEFI (for example, "E:")

 /debug:value        Outputs the event messages to the console and to the .log files. If the value
                     specified in value is:

                     - TRUE, event messages are sent to the console and the .log files

                     - FALSE, event messages are sent only to the .log files (This is the behavior
                     when the argument is not provided.)

Properties

                                                                                    ﾉ    Expand table

 Name                                         Read                         Write

 UtilityVol                                   -

ZTIMoveStateStore.wsf
This script moves the captured user state and backup files to
C:\Windows\Temp\StateStore.

  ７ Note

  This script is run only when deploying images using Configuration Manager.

<!-- p.1282 -->

                                                                                    ﾉ    Expand table

 Value          Description

 Input          Environment variables. Contains the property values, custom property values,
                database connections, deployment rules, and other information that the scripts
                require to complete the deployment process

 Output         - ZTIMoveStateStore.log. Log file that contains events that this script generates

                - BDD.log. Log file that contains events that all MDT scripts generate

 References     ZTIUtility.vbs. Includes support functions and subroutines that the script uses

 Location       distribution\Scripts

 Use            cscript ZTIMoveStateStore.wsf </debug:value>

Arguments

                                                                                    ﾉ    Expand table

 Value            Description

 /debug:value     Outputs the event messages to the console and to the .log files. If the value
                  specified in value is:

                  - TRUE, event messages are sent to the console and the .log files

                  - FALSE, event messages are sent only to the .log files (This is the behavior when
                  the argument is not provided.)

Properties

                                                                                    ﾉ    Expand table

 Name                                  Read                           Write

 None

ZTINextPhase.wsf
This script updates the Phase property to the next phase in the deployment process. The
Task Sequencer uses these phases to determine the sequence in which each task must
be completed. The Phase property includes the following values:

<!-- p.1283 -->

      VALIDATION. Identify that the target computer is capable of running the scripts
      necessary to complete the deployment process.

      STATECAPTURE. Save any user state migration data before deploying the new
      target operating system.

      PREINSTALL. Complete any tasks that need to be done (such as creating new
      partitions) before the target operating system is deployed.

      INSTALL. Install the target operating system on the target computer.

      POSTINSTALL. Complete any tasks that need to be done before restoring the user
      state migration data. These tasks customize the target operating system before
      starting the target computer the first time after deployment (such as installing
      updates or adding drivers).

      STATERESTORE. Restore the user state migration data saved during the State
      Capture Phase.

      For more information about the Phase property, see Phase.

                                                                                   ﾉ    Expand table

Value          Description

Input          Environment variables. Contains the property values, custom property values,
               database connections, deployment rules, and other information that the scripts
               require to complete the deployment process

Output         - ZTINextPhase.log. Log file that contains events that this script generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTINextPhase.wsf </debug:value>

Arguments

                                                                                   ﾉ    Expand table

Value            Description

/debug:value     Outputs the event messages to the console and to the .log files. If the value
                 specified in value is:

<!-- p.1284 -->

 Value          Description

                - TRUE, event messages are sent to the console and the .log files

                - FALSE, event messages are sent only to the .log files (This is the behavior when
                the argument is not provided.)

Properties

                                                                                  ﾉ    Expand table

 Name                                                        Read                Write

 DeploymentMethod                                            -

 Phase                                                       -                   -

ZTINICConfig.wsf
This script configures activated network adapters with values that ZTIGather.wsf
captured based on the properties listed in the CustomSettings.ini file or the MDT DB
(created in the Database node in the Deployment Workbench).

                                                                                  ﾉ    Expand table

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

 Output       - ZTINICConfig.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

 References   - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

              - ZTINicUtility.vbs. Includes support functions and subroutines that the script uses

 Location     distribution\Scripts

 Use          cscript ZTINicConfig.wsf </debug:value> </ForceCapture> </RestoreWithinWinPE>

Arguments

<!-- p.1285 -->

                                                                                  ﾉ       Expand table

 Value                 Description

 /debug:value          Outputs the event messages to the console and to the .log files. If the
                       value specified in value is:

                       - TRUE, event messages are sent to the console and the .log files

                       - FALSE, event messages are sent only to the .log files (This is the behavior
                       when the argument is not provided.)

 /ForceCapture         If there are any local networking adapters with static IP addresses saved,
                       this script captures those settings and saves them to the local
                       environment—for example, C:\MININT\SMSOSD\OSDLogs\Variables.dat.
                       This script can be useful in capturing static IP settings for a large number
                       of computers for automation.

 /RestoreWithinWinPE   When specified, applies any saved static IP network settings to the local
                       computer, when appropriate; used for internal processing only.

Properties

                                                                                  ﾉ       Expand table

 Name                                                               Read              Write

 DeployDrive                                                        -                 -

 DeploymentMethod                                                   -

 DeploymentType                                                     -

 DeployRoot                                                         -

 OSDAdapterCount                                                    -                 -

 OSGuid                                                             -

 OSDMigrateAdapterSettings                                          -

 Phase                                                              -

ZTINICUtility.vbs
This script contains network adapter-related functions and subroutines that the various
scripts in the MDT deployment process call.

<!-- p.1286 -->

                                                                               ﾉ   Expand table

 Value        Description

 Input        None

 Output       None

 References   - CMD.exe. Allows running of command-line tools

              - Netsh.exe. A utility used to automate the configuration of networking components

 Location     distribution\Scripts

 Use          <script language="VBScript" src="ZTINicUtility.vbs"/>

Arguments

                                                                               ﾉ   Expand table

 Value                               Description

 None                                None

Properties

                                                                               ﾉ   Expand table

 Name                                                                   Read         Write

 OSDAdapterAdapterIndexAdapterName                                      -            -

  ７ Note

  AdapterIndexin this property is a placeholder for a zero-based array that contains
  network adapter information.

ZTIOSRole.wsf
This script installs server roles for target computers that are running Windows operating
systems. The script reads the OSRoles, OSRoleServices, and OSFeatures properties to
determine what should be installed.

<!-- p.1287 -->

 ７ Note

 This script is intended to be called only by the Install Roles and Features
 andUninstall Roles and Features task sequence steps. Calling this script directly is
 not supported.

                                                                                   ﾉ       Expand table

Value          Description

Input          Environment variables. Contains the property values, custom property values,
               database connections, deployment rules, and other information that the scripts
               require to complete the deployment process

Output         - ZTIOSRole.log. Log file that contains events that this script generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     - CMD.exe. Allows running of command-line tools

               - OCSetup.exe. Adds to or removes Windows optional components

               - ServerManagerCmd.exe. Installs, configures, and manages Windows Server roles
               and features

               - Sysocmgr.exe. Adds or removes Windows components

               - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTIOSRole.wsf </debug:value>

Arguments

                                                                                   ﾉ       Expand table

Value            Description

/debug:value     Outputs the event messages to the console and to the .log files. If the value
                 specified in value is:

                 - TRUE, event messages are sent to the console and the .log files

                 - FALSE, event messages are sent only to the .log files (This is the behavior when
                 the argument is not provided.)

<!-- p.1288 -->

 Value            Description

 /Uninstall       If provided, this argument indicates that the roles and features will be uninstalled.
                  If not provided, the script assumes the roles and features will be installed.

Properties

                                                                                     ﾉ    Expand table

 Name                                                               Read              Write

 IsServerCoreOS                                                     -

 OSFeatures                                                         -

 OSRoles                                                            -

 OSRoleServices                                                     -

 OSVersion                                                          -

 SMSTSRebootRequested                                                                 -

ZTIPatches.wsf
This script installs updates (language packs, security updates, and so on) that are listed
in the Packages.xml file. The script self-terminates if the deployment is not in one of the
following states:

     Phase equals PREINSTALL

     DeploymentMethod equals SCCM

     The script starts Pkgmgr if DeploymentMethod equals SCCM.

                                                                                     ﾉ    Expand table

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

 Output       - ZTIPatches.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

<!-- p.1289 -->

Value          Description

References     - Expand.exe. Expands compressed files

               - Pkgmgr.exe. Installs or updates Windows Vista offline

               - ZTIConfigFile.vbs. Includes routines for processing XML files

               - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTIPatches.wsf </debug:value>

Arguments

                                                                                   ﾉ   Expand table

Value            Description

/debug:value     Outputs the event messages to the console and to the .log files. If the value
                 specified in value is:

                 - TRUE, event messages are sent to the console and the .log files

                 - FALSE, event messages are sent only to the .log files (This is the behavior when
                 the argument is not provided.)

Properties

                                                                                   ﾉ   Expand table

Name                                                                     Read          Write

Architecture                                                             -

CustomPackageSelectionProfile                                            -

DeployRoot                                                               -

DeploymentMethod                                                         -

DeploymentType                                                           -

DestinationLogicalDrive                                                  -

LanguagePacks                                                            -

<!-- p.1290 -->

 Name                                                                  Read            Write

 OSDAnswerFilePath                                                     -

 OSDPlatformArch                                                       -

 PackageSelectionProfile                                               -

 Phase                                                                 -

 ResourceRoot                                                          -

ZTIPowerShell.wsf
This script runs a Windows PowerShell script using a custom Windows PowerShell host.

                                                                                  ﾉ    Expand table

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

 Output       - ZTIPowerShell.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

              - Return code. The numeric value returned by the Windows PowerShell script after
              completion, which indicates the completion status of the script.

 References   - Microsoft.BDD.TaskSequencePSHost.exe. Custom Windows PowerShell host used
              to run the Windows PowerShell script.

 Location     distribution\Scripts

 Use          cscript ZTIPowerShell.wsf

Arguments

                                                                                  ﾉ    Expand table

 Value                               Description

 None

<!-- p.1291 -->

Properties

                                                                              ﾉ      Expand table

 Name                               Read                          Write

 None

ZTIPrereq.vbs
This script verifies that the target computer has the prerequisite software installed and
that it is functional. The checks the script performs are:

       Determine whether the Windows Script version is equal to or greater than version
       5.6.

       Verify that errors do not occur when object references are instantiated to
       Wscript.Shell, Wscript.Network, Scripting.FileSystemObject
       MSXML2.DOMDocument, and the Process environment.

       If any one of the checks fails, an error is raised and the script exits the
       ValidatePrereq procedure.

                                                                              ﾉ      Expand table

 Value                                  Description

 Input                                  None

 Output                                 None

 References                             None

 Location                               distribution\Scripts

 Use                                    None

Arguments

                                                                              ﾉ      Expand table

 Value                               Description

 None                                None

<!-- p.1292 -->

Properties

                                                                          ﾉ   Expand table

 Name                            Read                         Write

 None

ZTISCCM.wsf
This script initializes ZTI when deploying using Configuration Manager. The script
performs the following procedure:

   1. If debugging is activated, the script creates the OSD.Debug file.

   2. The script configures these properties:

           ScriptRootis set to the parent folder of the currently running script.

           DeployRoot is set to the parent folder of ScriptRoot.

           ResourceRoot is set to DeployRoot.

           DeploySystemDrive is set to C:.

           DeploymentMethod is set to SCCM.

   3. When DeployRootcontains :\:

           The DeployRoot folder is copied to _SMSTSMDataPath\WDPackage

           ScriptRoot is set to _SMSTSMDataPath\WDPackage\Scripts

           DeployRoot is set to the parent folder of ScriptRoot

           ResourceRoot is set to DeployRoot

   4. When Phase is NULL:

           If the %SystemDrive% environment variable is X:, then DeploymentTypeis set
           to NEWCOMPUTER and Phase is set to PREINSTALL.
           Otherwise,DeploymentType is set to REPLACE and Phase is set to
           VALIDATION.

           If the OldComputer.tag file exists in the parent folder of the current running
           script, DeploymentType is set to REPLACE and Phase is set to VALIDATION.

<!-- p.1293 -->

           Otherwise,DeploymentType is set to REFRESH and Phase is set to
           VALIDATION.

      For more information about these properties, see the Properties article.

                                                                                   ﾉ     Expand table

Value          Description

Input          Environment variables. Contains the property values, custom property values,
               database connections, deployment rules, and other information that the scripts
               require to complete the deployment process

Output         - ZTISCCM.log. Log file that contains events that this script generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTISCCM.wsf </debug:value>

Arguments

                                                                                   ﾉ     Expand table

Value            Description

/debug:value     Outputs the event messages to the console and to the .log files. If the value
                 specified in value is:

                 - TRUE, event messages are sent to the console and the .log files

                 - FALSE, event messages are sent only to the .log files (This is the behavior when
                 the argument is not provided.)

Properties

                                                                                   ﾉ     Expand table

Name                                                          Read                Write

_SMSTSMDataPath                                               -

Architecture                                                  -

<!-- p.1294 -->

 Name                                                         Read                Write

 BDDPackageID                                                 -                   -

 DeploymentMethod                                             -                   -

 DeploymentType                                               -                   -

 DeployRoot                                                   -                   -

 Phase                                                        -                   -

 ResourceRoot                                                 -                   -

 ScriptRoot                                                   -                   -

 ToolRoot                                                     -                   -

ZTISetVariable.wsf
This script sets the specified global task sequence variable that corresponds to the name
contained in VariableName to the value contained in VariableValue.

                                                                                   ﾉ   Expand table

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

 Output       - ZTISetVariable.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

 References   ZTIUtility.vbs. Includes support functions and subroutines that the script uses

 Location     distribution\Scripts

 Use          cscript ZTISetVariable.wsf </debug:value>

Arguments

                                                                                   ﾉ   Expand table

<!-- p.1295 -->

 Value             Description

 /debug:value      Outputs the event messages to the console and to the .log files. If the value
                   specified in value is:

                   - TRUE, event messages are sent to the console and the .log files

                   - FALSE, event messages are sent only to the .log files (This is the behavior when
                   the argument is not provided.)

Properties

                                                                                    ﾉ   Expand table

 Name                                                  Read                    Write

 VariableName                                          -

 VariableValue                                         -

ZTITatoo.wsf
This script tattoos the target computer with identification and version information. The
script performs the following procedure:

   1. Locate and copy the ZTITatoo.mof file to the %SystemRoot%\System32\Wbem
     folder. Any preexisting ZTITatoo.mof that exists at the destination will be deleted
     before starting the copy operation.

   2. Mofcomp.exe will be run using the following command:

         exe

         %SystemRoot%\System32\Wbem\Mofcomp.exe -autorecover
         %SystemRoot%\System32\Wbem\ZTITatoo.mof.

   3. For all deployment methods (LTI, ZTI, and UDI), these deployment details are
     written for all deployment methods to the registry at
     HKEY_LOCAL_MACHINE\Software\Microsoft\Deployment 4:

               Deployment Method is set to the deployment method being used and can
               be set to LTI, ZTI, or UDI, depending on the deployment method being
               performed.

<!-- p.1296 -->

       Deployment Source is set to the source for the deployment and can be set to
       OEM, MEDIA, or the value in the DeploymentMethod property.

       Deployment Type is set to the DeploymentType property.

       Deployment Timestamp is set to the current date in WMI date format.

       Deployment Toolkit Version is set to the Version property.

4. For LTI deployments, these deployment details are written to the registry at
  HKEY_LOCAL_MACHINE\Software\Microsoft\Deployment 4:

       Task Sequence ID is set to the TaskSequenceIDproperty.

       Task Sequence Name is set to the TaskSequenceName property.

       Task Sequence Version is set to the TaskSequenceVersion property.

5. For all Configuration Manager deployments (ZTI and UDI for Configuration
  Manager), these deployment details are written to the registry at
  HKEY_LOCAL_MACHINE\Software\Microsoft\Deployment 4:

       OSD Package ID is set to the _SMSTSPackageID task sequence variable.

       OSD Program Name is always set to "\*".

       OSD Advertisement ID is set to the _SMSTSAdvertID task sequence variable.

6. For LTI deployments where an image is being captured, these deployment details
  are written to the registry at
  HKEY_LOCAL_MACHINE\Software\Microsoft\Deployment 4:

       Capture Method is set to the deployment method being used and can be set
       to LTI, ZTI, or UDI, depending on the deployment method being performed.

       Capture Timestamp is set to the current date in WMI date format.

       Capture Toolkit Version is set to the Version property.

       Capture Task Sequence ID is set to the TaskSequenceIDproperty.

       Capture Task Sequence Name is set to the TaskSequenceName property.

       Capture Task Sequence Version is set to the TaskSequenceVersion property.

7. For all Configuration Manager deployments (ZTI and UDI for Configuration
  Manager) in which an image is being captured, these deployment details are

<!-- p.1297 -->

      written to the registry at
      HKEY_LOCAL_MACHINE\Software\Microsoft\Deployment 4:

           Capture OSD Package ID is set to the _SMSTSPackageID task sequence
           variable.

           Capture OSD Program Name is always set to "*****".

           Capture OSD Advertisement ID is set to the _SMSTSAdvertIDtask sequence
           variable.

         ７ Note

         This script is not designed to run on Windows PE.

                                                                                    ﾉ     Expand table

Value          Description

Input          Environment variables. Contains the property values, custom property values,
               database connections, deployment rules, and other information that the scripts
               require to complete the deployment process

Output         - ZTITatoo.log. Log file that contains events that this script generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     - Mofcomp.exe. Command-line .mof file compiler

               - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTITatoo.wsf </debug:value>

Arguments

                                                                                    ﾉ     Expand table

Value            Description

/debug:value     Outputs the event messages to the console and to the .log files. If the value
                 specified in value is:

                 - TRUE, event messages are sent to the console and the .log files

<!-- p.1298 -->

 Value          Description

                - FALSE, event messages are sent only to the .log files (This is the behavior when
                the argument is not provided.)

Properties

                                                                                   ﾉ   Expand table

 Name                                                          Read                Write

 _SMSTSAdvertID                                                -

 _SMSTSPackageID                                               -

 _SMSTSSiteCode                                                -

 DeploymentMethod                                              -

 DeploymentType                                                -

 Version                                                       -

 TaskSequenceID                                                -

 TaskSequenceName                                              -

 TaskSequenceVersion                                           -

ZTIUserState.wsf
This script initializes USMT to capture and restore user state on the target computer.

                                                                                   ﾉ   Expand table

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

 Output       - ZTIUserState.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

 References   - CMD.exe. Allows running of command-line tools

              - Loadstate.exe. Deposits user state data on a target computer

<!-- p.1299 -->

Value          Description

               - Msiexec.exe. Manages the installation of .msi-based applications

               - Scanstate.exe. Collects user data and settings

               - USMT Application Files

               - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTIUserState.wsf </debug:value>

Arguments

                                                                                     ﾉ   Expand table

Value            Description

/debug:value     Outputs the event messages to the console and to the .log files. If the value
                 specified in value is:

                 - TRUE, event messages are sent to the console and the .log files

                 - FALSE, event messages are sent only to the .log files (This is the behavior when
                 the argument is not provided.)

/Capture         -

/Estimate        -

/Restore         -

Properties

                                                                                     ﾉ   Expand table

Name                                                                        Read          Write

Architecture                                                                -

DeploymentMethod                                                            -

DeploymentType                                                              -

DestinationLogicalDrive                                                     -

<!-- p.1300 -->

 Name                                                               Read        Write

 ImageBuild                                                         -

 ImageSize                                                          -

 ImageSizeMultiplier                                                -

 InstallFromPath                                                    -

 IsServerOS                                                         -

 LoadStateArgs                                                      -

 OSCurrentVersion                                                   -

 OSDMigrateAdditionalCaptureOptions                                 -           -

 OSDMigrateAdditionalRestoreOptions                                 -           -

 OSDPackagePath                                                     -

 OSDStateStorePath                                                              -

 OSVersion                                                          -

 ScanStateArgs                                                      -

 StatePath                                                          -           -

 UDDir                                                              -

 UDProfiles                                                         -

 UDShare                                                            -

 UserDataLocation                                                   -           -

 USMTConfigFile                                                     -

 USMTEstimate                                                       -           -

 USMTLocal                                                                      -

 USMTMigFiles                                                       -

ZTIUtility.vbs
This script contains utility functions that most of the MDT scripts use.

                                                                           ﾉ   Expand table

<!-- p.1301 -->

Value        Description

Input        Environment variables. Contains the property values, custom property values,
             database connections, deployment rules, and other information that the scripts
             require to complete the deployment process

Output       None

References   - Credentials_ENU.xml. Prompts the user for credentials that will be used when
             connecting to network resources

             - IPConfig.exe. Displays all current TCP/IP network configuration values and
             refreshes DHCP and DNS settings

             - MSHTA.exe. HTML application host

             - Regsvr32.exe. Registers files (.dll, .exe, .ocx, and so on) with the operating system

             - Xcopy.exe. Copies files and directories, including subdirectories

Location     - distribution\Scripts

             - program_files\Microsoft Deployment Toolkit\Scripts

Use          <script language="VBScript" src="ZTIUtility.vbs"/>

Arguments

                                                                                   ﾉ   Expand table

Value                                 Description

None                                  None

Properties

                                                                                   ﾉ   Expand table

Name                                                                                   Read    Write

_SMSTSAdvertID                                                                         -

_SMSTSCurrentActionName                                                                -

_SMSTSCustomProgressDialogMessage                                                      -

_SMSTSInstructionTableSize                                                             -

<!-- p.1302 -->

Name                           Read   Write

_SMSTSLogPath                  -

_SMSTSMachineName              -

_SMSTSNextInstructionPointer   -

_SMSTSOrgName                  -

_SMSTSPackageID                -

_SMSTSPackageName              -

_SMSTSPackagePath              -

_SMSTSReserved1                -

_SMSTSReserved2                -

Architecture                   -

AssetTag                       -

ComputerName                   -

Debug                          -      -

DeploymentMethod               -

DeployRoot                     -

DestinationDisk                -      -

DestinationLogicalDrive        -      -

DestinationPartition           -      -

EventShare                     -

HostName                       -

ImageBuild                     -      -

ImageFlags                            -

ImageIndex                            -

ImageLanguage                         -

ImageProcessor                        -

ImageSize                             -

<!-- p.1303 -->

Name                       Read   Write

InstallFromPath                   -

JoinDomain                 -

LogPath                    -      -

MacAddress                 -

OSCurrentVersion           -

OSDAdvertID                -

OSDAnswerFilePath          -      -

OSDAnswerFilePathSysprep   -      -

OSDComputerName            -      -

OSDPackageID               -

OSDPackagePath             -

OSDTargetSystemDrive       -

OSGUID                            -

OSSKU                      -

OSVersion                  -

Phase                      -

Processor_Architecture     -

ResourceRoot               -

SLShare                    -

SLShareDynamicLogging      -

TaskSequenceID             -

TaskSequenceName                  -

TaskSequenceVersion               -

UDDir                      -

UDShare                    -

UserDomain                 -      -

<!-- p.1304 -->

 Name                                                                                  Read   Write

 UserID                                                                                -      -

 UserPassword                                                                          -      -

 UUID                                                                                  -

 Version                                                                               -      -

 Note: This variable is an internal variable that represents the version of MDT.

 WDSServer                                                                             -

ZTIValidate.wsf
This script ensures that it is safe for the deployment to continue by validating the
condition of the target computer. The script processes are:

     If DeploymentType equals REFRESH and the target computer is a server, the script
     exits.

     If OSInstall exists and is not equal to YES, the script exits.

     Verify that the minimum amount of RAM exists on the target computer; if not, the
     script exits.

     Verify that the processor meets the minimum required speed; if not, the script
     exits.

     Verify that the hard disk size meets the minimum size requirements; if not, the
     script exits.

     Verify that the target computer's operating system is installed on drive C; if not, the
     script exits.

     If DeploymentType = REFRESH, verify that drive C is not compressed by running
      Compact /u C:\ .

                                                                                   ﾉ   Expand table

 Value         Description

 Input         Environment variables. Contains the property values, custom property values,
               database connections, deployment rules, and other information that the scripts
               require to complete the deployment process

<!-- p.1305 -->

Value          Description

Output         - ZTIValidate.log. Log file that contains events that this script generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     - Compact.exe. Displays or alters the compression of files on NTFS file system
               partitions

               - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTIValidate.wsf </debug:value>

Arguments

                                                                                     ﾉ    Expand table

Value            Description

/debug:value     Outputs the event messages to the console and to the .log files. If the value
                 specified in value is:

                 - TRUE, event messages are sent to the console and the .log files

                 - FALSE, event messages are sent only to the .log files (This is the behavior when
                 the argument is not provided.)

Properties

                                                                                     ﾉ    Expand table

Name                                                               Read               Write

DeploymentType                                                     -

DestinationLogicalDrive                                            -                  -

ImageBuild                                                         -

ImageMemory                                                        -

ImageProcessorSpeed                                                -

ImageSize                                                          -

<!-- p.1306 -->

 Name                                                       Read            Write

 ImageSizeMultiplier                                        -

 IsServerOS                                                 -

 Memory                                                     -

 OSDPackagePath                                             -

 OSInstall                                                  -

 ProcessorSpeed                                             -

 SMSTSLocalDataDrive                                                        -

 VerifyOS                                                   -

ZTIVHDCreate.wsf
This script is used to create a virtual hard disk (.vhd or .avhd) file on the target computer
and mount the .vhd file as a disk. Then, other portions of the LTI deployment process
deploy the Windows operating system and applications to the newly created virtual
hard disk. The script processes are as follows:

     The Class_Initialize method is used to initialize the VHDInputVariable variable.

     Validate that VHDCreateSource is defined and locates the source .vhd file (if
     specified).

     Generate a random .vhd file name if VHDCreateFilename equals RANDOM or ""
     (null).

     Verify that the folder exists where the .vhd file (specified in VHDCreateFileName) is
     to be created.

     Create the .vhd file using the values in VHDCreateSizePercent,
     VHDCreateSizeMax, and VHDCreateType.

     Create a differencing disk (if specified) using the value in VHDCreateDiffVHD.

     The newly created .vhd file and the optional differencing disk are mounted.

     The disk number of the mounted virtual hard disk is returned.

                                                                           ﾉ    Expand table

<!-- p.1307 -->

Value          Description

Input          Environment variables. Contains the property values, custom property values,
               database connections, deployment rules, and other information that the scripts
               require to complete the deployment process

Output         - ZTIVHDCreate.log. Log file that contains events that this script generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     - ZTIDiskUtility.vbs. Includes support functions and subroutines the script uses

               - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTIVHDCreate.wsf </debug:value>

Arguments

                                                                                   ﾉ    Expand table

Value            Description

/debug:value     Outputs the event messages to the console and to the .log files. If the value
                 specified in value is:

                 - TRUE, event messages are sent to the console and the .log files

                 - FALSE, event messages are sent only to the .log files (This is the behavior when
                 the argument is not provided.)

Properties

                                                                                   ﾉ    Expand table

Name                                                          Read                Write

VHDCreateDiffVHD                                              -

VHDCreateFileName                                             -

VHDCreateSizeMax                                              -

VHDCreateSource                                               -

VHDCreateType                                                 -

<!-- p.1308 -->

 Name                                                  Read              Write

 VHDDisks                                                                -

 VHDInputVariable                                      -

 VHDOutputVariable                                     -

ZTIWindowsUpdate.wsf
This script downloads and installs updates from computers on a corporate network that
are running WSUS, Windows Update, or Microsoft Update using the Windows Update
Agent (WUA) application programming interface (API). By default, this feature is
disabled in each task sequence and must be manually activated to run.

Most enterprises will already have teams and infrastructures in place to update newly
deployed computers over the corporate network. This process involves tracking the
latest set of patches, drivers, and updates available for each desktop configuration and
determining which updates should be downloaded and installed for each configuration.
If the organization already has an established process, this script might not be
necessary. This script was designed to fill a need for deployment teams that might not
have established processes, yet want to ensure that target computers are updated when
deployed.

This script automatically scans the target computer and downloads a wide range of
updates that are found to be applicable. Among these are:

     Windows service packs

     Non-Microsoft drivers that were placed on Windows Update

     The latest hotfix updates

     Microsoft Office updates

     Microsoft Exchange Server and SQL Server updates

     Microsoft Visual Studio® updates

     Some non-Microsoft application updates

   Tip

  Many hardware manufacturers have placed their drivers on Windows Update. These
  drivers no longer need to be maintained in the Out-of-Box Drivers directory.

<!-- p.1309 -->

  Experiment by removing drivers from the distribution share to see which ones are
  available on Windows Update. Note that if the drivers are not included with
  Windows by default, do not remove networking or storage drivers, because the
  operating system will require user input.

MDT supports the ability to deploy an updated version of WUA as part of the operating
system deployment. This helps ensure that target computers are running the correct
version of WUA when they are deployed. It also helps eliminate the need to connect to
the Internet and download the latest version of WUA after deployment.

MDT can also configure WUA to collect updates from computers on the corporate
network that are running WSUS instead of connecting to Microsoft Updates over the
Internet. MDT can optionally configure WUA to use a specific computer running WSUS
using the WSUSServer property.

For additional information and for WUA deployment instructions, see How to Install the
Windows Update Agent on Client Computers         .

Obtain the latest version of the WUA stand-alone installer for:

     x86 versions (WindowsUpdateAgent30-x86.exe) at
     https://go.microsoft.com/fwlink/?LinkID=100334

     x64 version (WindowsUpdateAgent30-x64.exe) at
     https://go.microsoft.com/fwlink/?LinkID=100335

     Windows 7 and later include the most recent version of WUA, so no upgrade is
     necessary.

     For more information, see Updating Windows Update Agent.

     When enabled in the Task Sequencer, this script runs multiple times while in the
     State Restore Phase of operating system deployment. It is first run after the
     operating system has started for the first time. Ensure that the latest updates and
     service packs are installed before the installation of any applications that might
     depend on specific updates or service packs being installed on the target
     computer. For example, an application might be dependent on the latest version of
     the Microsoft .NET Framework being installed.

     This script also runs after the installation of applications, which ensures that the
     latest application service packs and updates have been applied. For example, use
     this script to ensure that the latest updates are applied to Microsoft Office 2010 or
     the 2007 Office system.

<!-- p.1310 -->

It is possible, during the installation of one or more updates, the target computer
will need to be restarted to allow an update installation to finish fully. To ensure
that updates are properly installed, if the script detects that the installation of an
update requires the target computer to be restarted, the script automatically
restarts the target computer and resumes if additional updates have been detected
and are pending installation. The script exits if it determines that the target
computer is fully up to date. An error will be logged if, while updating the target
computer, the script has seven unsuccessful attempts to install the updates and
the target computer still requires a restart.

During run time, the script performs the following tasks:

Configure the target computer to use a WSUS server, if the WSUSServer property
was specified.

Verify that the latest version of the WUA is installed on the target computer.

Search the target computer for applicable updates that are not already installed
and that might be typically hidden.

Each update has an associated UpdateID and QNumber property:

   The UpdateID property is in GUID form, such as 67da2176-5c57-4614-a514-
   33abbdd51f67.

   The QNumber property is a numerical value, such as 987654.

The script compares the UpdateID and KBArticle property values against the list of
exclusions specified in the following MDT properties:

   WUMU_ExcludeID. A list of UpdateIDs to exclude; any update with an UpdateID
   found in this list will not be installed.

   WUMU_ExcludeKB. A list of QNumbers to exclude; any update with a
   QNumber found in this list will not be installed.

   In addition, any update that requires user input will be excluded and not
   installed.

All updates that require approval of an End User License Agreement (EULA) will
automatically be approved by the script. Be sure to manually read and check each
EULA before running this script in a production environment.

The activity for each update is written to the ZTIWindowsUpdate.log file, with the
string INSTALL or SKIP if the update has been approved for installation, along with

<!-- p.1311 -->

      the UpdateID, a short description of the update, and the QNumber.

      Each update to be installed is downloaded and installed in batches.

      The target computer might require more than one restart during the update
      installation.

 ７ Note

 Windows Internet Explorer 7 requires user interaction, so it is not installed using
 this script.

 ７ Note

 By default, include QNumber 925471 in the WUMU_ExcludeKB list to prevent
 Windows Vista Ultimate from installing extra language packs.

                                                                                    ﾉ    Expand table

Value           Description

Input           Environment variables. Contains the property values, custom property values,
                database connections, deployment rules, and other information that the scripts
                require to complete the deployment process

Output          - ZTIWindowsUpdate.log. Log file that contains events that this script generates

                - BDD.log. Log file that contains events that all MDT scripts generate

References      - Expand.exe. Expands compressed files

                - Net.exe. Performs network management tasks

                - WindowsUpdateAgent30-x86.exe. Installs WUA

                - WindowsUpdateAgent30-x64.exe. Installs WUA

                - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location        distribution\Scripts

Use             cscript ZTIWindowsUpdate.wsf </debug:value> </UpdateCommand:"
                <IsInstalled=0&#124;1> <IsHidden=0&#124;1>"> </Query:true&#124;false>

Arguments

<!-- p.1312 -->

                                                                             ﾉ    Expand table

Value                  Description

/debug:value           Outputs the event messages to the console and to the .log files. If
                       the value specified in value is:

                       - TRUE, event messages are sent to the console and the .log files

                       - FALSE, event messages are sent only to the .log files (This is the
                       behavior when the argument is not provided.)

/UpdateCommand:param   - IsInstalled. Set to 0 to query for updates that are not installed.

                       - IsHidden. Set to 0 to query for updates that are hidden.

/Query:value           - True. Query only for required updates. Do not download and install
                       any binaries.

                       - False. Query for and install required updates. Download and install
                       binaries.

 ７ Note

 When specified, UpdateCommand requires at least one option.

 ７ Note

 If specifying both options for UpdateCommand, they must be separated by and.

 ７ Note

 The default value for UpdateCommand is IsInstalled=0 and IsHidden=0.

 ７ Note

 For more information about UpdateCommand, see IUpdateSearcher::Search
 Method    .

Properties

<!-- p.1313 -->

                                                                                    ﾉ    Expand table

 Name                                                              Read              Write

 Architecture                                                      -

 DoCapture                                                         -

 InstalledUpdates                                                                    -

 MSIT_WU_Count                                                     -                 -

 NoAutoUpdate_Previous                                             -                 -

 SMSTSRebootRequested                                              -                 -

 SMSTSRetryRequested                                               -                 -

 WSUSServer                                                        -

 WUMU_ExcludeID                                                    -

 WUMU_ExcludeKB                                                    -

ZTIWipeDisk.wsf
This script formats the target computer's hard disk. The script:

     Exits if WipeDisk is not equal to TRUE

     Determines the appropriate drive to format

     Formats the drive by calling cmd /c format <Drive> /fs:ntfs /p:3 /Y (where
     <Drive> is the drive letter of the hard disk drive to be formatted)

                                                                                    ﾉ    Expand table

 Value          Description

 Input          Environment variables. Contains the property values, custom property values,
                database connections, deployment rules, and other information that the scripts
                require to complete the deployment process

 Output         - ZTIWipeDisk.log. Log file that contains events that this script generates

                - BDD.log. Log file that contains events that all MDT scripts generate

 References     - CMD.exe. Allows running of command-line tools

<!-- p.1314 -->

Value          Description

               - Format.com. Formats the hard disk

               - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use                cscript ZTIWipeDisk.wsf </debug:value>

Arguments

                                                                                     ﾉ   Expand table

Value               Description

/debug:value        Outputs the event messages to the console and to the .log files. If the value
                    specified in value is:

                    - TRUE, event messages are sent to the console and the .log files

                    - FALSE, event messages are sent only to the .log files (This is the behavior when
                    the argument is not provided.)

Properties

                                                                                     ﾉ   Expand table

Name                                            Read                        Write

WipeDisk                                        -

Related articles
      Task Sequence Steps.
      Properties.
      Support Files.
      Utilities.
      MDT Windows PowerShell Cmdlets.
      Tables and Views in the MDT DB.
      Windows 7 Feature Dependency Reference.
      UDI Reference.

<!-- p.1315 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1316 -->

Support Files
Article • 02/12/2024

The utilities and scripts used in LTI and ZTI deployments reference external configuration
files to determine the process steps and configuration settings used during the
deployment process.

The following information is provided for each utility:

      Name. Specifies the name of the file

      Description. Provides a description of the purpose of the file

      Location. Indicates the folder where the file can be found; in the information for
      the location, the following variables are used:

         program_files. This variable points to the location of the Program Files folder on
         the computer where MDT is installed.

         distribution. This variable points to the location of the Distribution folder for
         the deployment share.

         platform. This variable is a placeholder for the operating system platform (x86
         or x64).

ApplicationGroups.xml

  ７ Note

  This XML file is managed by MDT and should not require modification.

                                                                            ﾉ   Expand table

 Value                           Description

 Location                        distribution\Control

Applications.xml

  ７ Note

<!-- p.1317 -->

  This XML file is managed by MDT and should not require modification.

                                                                         ﾉ   Expand table

 Value                          Description

 Location                       distribution\Control

BootStrap.ini
The configuration file used when the target computer is not able to connect to the
appropriate deployment share. This situation occurs in the New Computer and the
Replace Computer scenarios.

                                                                         ﾉ   Expand table

 Value                          Description

 Location                       distribution\Control

CustomSettings.ini
The primary configuration file for the MDT processing rules used in all scenarios.

                                                                         ﾉ   Expand table

 Value                          Description

 Location                       distribution\Control

Deploy.xml

  ７ Note

  This XML file is managed by MDT and should not require modification.

                                                                         ﾉ   Expand table

<!-- p.1318 -->

Value         Description

Location      program_files\Microsoft Deployment Toolkit\Control

DriverGroups.xml

 ７ Note

 This XML file is managed by MDT and should not require modification.

                                                                   ﾉ    Expand table

Value                         Description

Location                      distribution\Control

Drivers.xml

 ７ Note

 This XML file is managed by MDT and should not require modification.

                                                                   ﾉ    Expand table

Value                         Description

Location                      distribution\Control

LinkedDeploymentShares.xml

 ７ Note

 This XML file is managed by MDT and should not require modification.

                                                                   ﾉ    Expand table

<!-- p.1319 -->

Value                        Description

Location                     distribution\Scripts

ListOfLanguages.xml

 ７ Note

 This XML file is managed by MDT and should not require modification.

                                                                   ﾉ    Expand table

Value                        Description

Location                     distribution\Scripts

MediaGroups.xml

 ７ Note

 This XML file is managed by MDT and should not require modification.

                                                                   ﾉ    Expand table

Value                        Description

Location                     distribution\Scripts

Medias.xml

 ７ Note

 This XML file is managed by MDT and should not require modification.

                                                                   ﾉ    Expand table

<!-- p.1320 -->

Value                        Description

Location                     distribution\Scripts

OperatingSystemGroups.xml

 ７ Note

 This XML file is managed by MDT and should not require modification.

                                                                   ﾉ    Expand table

Value                       Description

Location                    distribution\Control

OperatingSystems.xml

 ７ Note

 This XML file is managed by MDT and should not require modification.

                                                                   ﾉ    Expand table

Value                       Description

Location                    distribution\Control

PackageGroups.xml

 ７ Note

 This XML file is managed by MDT and should not require modification.

                                                                   ﾉ    Expand table
