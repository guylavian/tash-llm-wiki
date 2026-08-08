---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1241-1280"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1241-1280
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1241-1280
family: sccm
documentKind: "doc"
abstract: "Value Description Use <script language=\"VBScript\" src=\"WizUtility.vbs\"/> Arguments ﾉ Expand table Value Description None None Properties ﾉ Expand table Name Read Write DefaultFolderPath - DefaultDestinationDisk - DefaultDestinationIsDirty - DefaultDestinationPartition - Deployme"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1241-1280

<!-- p.1241 -->

 Value        Description

 Use          <script language="VBScript" src="WizUtility.vbs"/>

Arguments

                                                                           ﾉ       Expand table

 Value                             Description

 None                              None

Properties

                                                                           ﾉ       Expand table

 Name                                                          Read            Write

 DefaultFolderPath                                                             -

 DefaultDestinationDisk                                        -

 DefaultDestinationIsDirty                                     -

 DefaultDestinationPartition                                   -

 DeploymentType                                                -

 DestinationDisk                                               -

 FolderPath                                                    -

 OSVersion                                                     -

 UserDomain                                                    -

 UserCredentials                                                               -

ZTIApplications.wsf
This script initiates an installation of applications that have been configured in the
Applications node in Deployment Workbench. This script will not attempt to install any
application that:

       Does not support the target computer's platform type

<!-- p.1242 -->

      Does not support the target computer's processor type

      Has an uninstall entry in the registry under
      HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninst
      all

 ７ Note

 If the listed application has any dependent applications defined, this script attempts
 to install those dependent applications before installing the listed application.

                                                                                    ﾉ   Expand table

Value          Description

Input          Environment variables. Contains the property values, custom property values,
               database connections, deployment rules, and other information that the scripts
               require to complete the deployment process

Output         - ZTIApplications.log. Log file that contains events that this script generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     - ZTIConfigFile.vbs. Includes routines for processing XML files

               - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

               - BDDRun.exe. Runs a command that requires user interaction

Location       distribution\Scripts

Use            cscript ZTIApplications.wsf </debug:value>

Arguments

                                                                                    ﾉ   Expand table

Value            Description

/debug:value     Outputs the event messages to the console and to the .log files. If the value
                 specified in value is:

                 - TRUE, event messages are sent to the console and the .log files

                 - FALSE, event messages are sent only to the .log files (this is the behavior when
                 the argument is not provided)

<!-- p.1243 -->

Properties

                                                                               ﾉ     Expand table

 Name                                                           Read             Write

 ApplicationGUID                                                -

 ApplicationSuccessCodes                                        -

 DependentApplications                                          -

 DeploymentMethod                                               -

 InstalledApplications                                          -                -

 ResourceDrive                                                  -

 ResourceRoot                                                   -                -

 SMSTSRebootRequested                                                            -

 SMSTSRetryRequested                                                             -

ZTIAppXmlGen.wsf
This script generates an XML file—ZTIAppXmlGen.xml—to use when automatically
capturing user data (documents) associated with installed applications. It does so
through the HKEY_CLASSES_ROOT\Software\Classes registry key and captures any
applications that:

     Are not associated with one of these file extensions: .mp3, .mov, .wma, .wmv, .chm,
     .evt, .evtx, .exe, .com, or .fon

     Are not associated with Microsoft Office, such as the 2007 Office system or
     Microsoft Office 2003.

     Have a valid open handler listed at
     HKEY_CLASSES_ROOT\application\shell\open\command

                                                                               ﾉ     Expand table

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

<!-- p.1244 -->

Value          Description

Output         - ZTIAppXmlGen.xml.Contains a list of applications installed on the target computer

               - ZTIAppXmlGen.log. Log file that contains events that this script generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTIAppXmlGen.wsf </debug:value>

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

DeploymentMethod                                              -

DeploymentType                                                -

ImageBuild                                                    -

OSCurrentVersion                                              -

USMTMigFiles                                                  -                   -

ZTIAuthorizeDHCP.wsf

<!-- p.1245 -->

This script uses the Netsh tool to configure the target computer so that it is an
authorized DHCP server in AD DS.

For more information about authorizing DHCP servers, see Netsh commands for DHCP.

                                                                                    ﾉ    Expand table

 Value          Description

 Input          Environment variables. Contains the property values, custom property values,
                database connections, deployment rules, and other information that the scripts
                require to complete the deployment process

 Output         - ZTIAuthorizeDHCP.log. Log file that contains events that this script generates

                - BDD.log. Log file that contains events that all MDT scripts generate

 References     - Netsh.exe. A utility used to automate the configuration of networking components

                - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

 Location       distribution\Scripts

 Use            cscript ZTIAuthorizeDHCP.wsf </debug:value>

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

 Name                                          Read                        Write

 IPAddress                                     -

<!-- p.1246 -->

ZTIBackup.wsf
This script performs a backup of the target computer using the ImageX utility. The
backup is stored in the location specified in the BackupDir and BackupShare properties.

                                                                                    ﾉ       Expand table

 Value          Description

 Input          Environment variables. Contains the property values, custom property values,
                database connections, deployment rules, and other information that the scripts
                require to complete the deployment process

 Output         - ZTIBackup.log. Log file that contains events that this script generates

                - ZTIBackup_imagex.log. Log file that contains events that ImageX generates

                - BDD.log. Log file that contains events that all MDT scripts generate

 References     - ImageX.exe. A utility used to create and manage WIM files

                - ZTIBCDUtility.vbs. Includes utility functions used when performing Boot Manager
                tasks

                - ZTIDiskUtility.vbs. Includes support functions and subroutines that the script uses

                - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

 Location       distribution\Scripts

 Use            cscript ZTIBackup.wsf </debug:value>

Arguments

                                                                                    ﾉ       Expand table

 Value            Description

 /debug:value     Outputs the event messages to the console and to the .log files. If the value
                  specified in value is:

                  - TRUE, event messages are sent to the console and the .log files

                  - FALSE, event messages are sent only to the .log files (this is the behavior when
                  the argument is not provided)

<!-- p.1247 -->

Properties

                                                                       ﾉ    Expand table

 Name                                                     Read          Write

 BackupDir                                                -

 BackupDisk                                               -

 BackupDrive                                              -

 BackupFile                                               -

 BackupPartition                                          -

 BackupScriptComplete                                                   -

 BackupShare                                              -

 ComputerBackupLocation                                   -

 DeploymentMethod                                         -

 DeploymentType                                           -

 DestinationLogicalDrive                                  -             -

 DoCapture                                                -

 ImageBuild                                               -

 ImageFlags                                               -

 OSDStateStorePath                                        -

 Phase                                                    -

 TaskSequenceID                                           -

 USMTLocal                                                -

ZTIBCDUtility.vbs
This script contains utility functions that some MDT scripts use when performing Boot
Manager tasks.

                                                                       ﾉ    Expand table

<!-- p.1248 -->

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

 Output       None

 References   BCDEdit.exe. A tool for editing the Windows boot configuration

 Location     - distribution\Scripts

              - program_files\Microsoft Deployment Toolkit\Scripts

 Use          <script language="VBScript" src="ZTIBCDUtility.vbs"/>

Arguments

                                                                               ﾉ   Expand table

 Value                                 Description

 None                                  None

Properties

                                                                               ﾉ   Expand table

 Name                                  Read                          Write

 None

ZTIBde.wsf
This script installs and configures BitLocker on the target computer. BitLocker
configuration is limited to New Computer scenarios that have hard disks configured
with a single partition.

  ７ Note

  For ZTI and UDI deployments, the UILanguage property must be set in
  CustomSettings.ini or in the MDT DB, because ZTIBde.wsf tries to read the locale
  from the UILanguage property.

<!-- p.1249 -->

                                                                                    ﾉ   Expand table

Value          Description

Input          Environment variables. Contains the property values, custom property values,
               database connections, deployment rules, and other information that the scripts
               require to complete the deployment process

Output         - ZTIBde.log. Log file that contains events that this script generates

               - ZTIBdeFix_diskpart.log. Log file that contains events that the Diskpart tool
               generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     - CMD.exe. Allows running of command-line tools

               - Defrag.exe. Defragments the hard disk

               - Diskpart.exe. Utility that allows for the automated management of disks,
               partitions, and volumes

               - ServerManagerCmd.exe

               - ZTIDiskUtility.vbs. Includes support functions and subroutines that the script uses

               - ZTIOSRole.wsf. Installs server roles

               - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTIBde.wsf </debug:value>

Arguments

                                                                                    ﾉ   Expand table

Value            Description

/debug:value     Outputs the event messages to the console and to the .log files. If the value
                 specified in value is:

                 - TRUE, event messages are sent to the console and the .log files

                 - FALSE, event messages are sent only to the .log files (this is the behavior when
                 the argument is not provided)

<!-- p.1250 -->

Properties

                                            ﾉ   Expand table

Name                                 Read        Write

AdminPassword                        -

BDEDriveLetter                       -           -

BDEDriveSize                         -

BDEInstall                           -

BDEInstallSuppress                   -

BDEKeyLocation                       -

BDEPin                               -

BDERecoveryKey                       -

BDESecondPass                        -           -

BdeWaitForEncryption                 -

BitlockerInstalled                   -           -

DeploymentMethod                     -

ISBDE                                -

OSDBitLockerCreateRecoveryPassword   -

OSDBitLockerMode                     -

OSDBitLockerStartupKey               -

OSDBitLockerStartupKeyDrive          -

OSDBitLockerTargetDrive              -

OSDBitLockerWaitForEncryption        -

OSCurrentBuild                       -

OSCurrentVersion                     -

OSFeatures                           -           -

OSRoles                              -           -

OSRoleServices                       -           -

<!-- p.1251 -->

 Name                                                                     Read          Write

 OSVersion                                                                -

 SMSTSRebootRequested                                                     -             -

 SMSTSRetryRequested                                                                    -

 TPMOwnerPassword                                                         -

ZTIBIOSCheck.wsf
This script checks the BIOS on the target computer, and then looks at a list of BIOSes
that are incompatible with Windows. The list of incompatible BIOSes is stored in the
ZTIBIOSCheck.xml file.

If the BIOS on the target computer is listed in the ZTIBIOSCheck.xml file, then the script
returns a status that indicates the BIOS is incompatible with Windows and the
deployment process should be terminated. For information on populating the list of
incompatible BIOSes, see ZTIBIOSCheck.xml.

                                                                                  ﾉ    Expand table

 Value        Description

 Input        - ZTIBIOSCheck.xml. Contains a list of BIOSes that are known to be incompatible
              with Windows

              - Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

 Output       - ZTIBIOSCheck.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

 References   ZTIUtility.vbs. Includes support functions and subroutines that the script uses

 Location     distribution\Scripts

 Use          cscript ZTIBIOSCheck.wsf </debug:value>

Arguments

                                                                                  ﾉ    Expand table

<!-- p.1252 -->

 Value          Description

 /debug:value   Outputs the event messages to the console and to the .log files. If the value
                specified in value is:

                - TRUE, event messages are sent to the console and the .log files

                - FALSE, event messages are sent only to the .log files (this is the behavior when
                the argument is not provided)

Properties

                                                                                  ﾉ   Expand table

 Name                               Read                            Write

 None

ZTICoalesce.wsf
Configuration Manager requires packages to be numbered sequentially starting with
PACKAGES001, with no gaps in the number sequence. Otherwise, installation will fail.

This script allows you to define and name variables using identifying information about
the program to run—for example, ComputerPackages100, ComputerPackages110, or
CollectionPackages150. Then, when this script is run, Configuration Manager finds all
variables that match a pattern (for example, all variable names that contain the string
Packages) and builds a sequential list, without gaps, using the base name PACKAGES.

For example, if the following variables were defined (using computer variables,
collection variables, or in CustomSettings.ini or the MDT DB, for example):

     ComputerPackages100=XXX00001:Program

     ComputerPackages110=XXX00002:Program

     CollectionPackages150=XXX00003:Program

     Packages001=XXX00004:Program

     After the script runs, the list would be:

     PACKAGES001=XXX00004:Program

     PACKAGES002=XXX00001:Program

<!-- p.1253 -->

      PACKAGES003=XXX00002:Program

      PACKAGES004=XXX00003:Program

      Configuration Manager would then be able to run all four programs.

                                                                                     ﾉ   Expand table

Value          Description

Input          Environment variables. Contains the property values, custom property values,
               database connections, deployment rules, and other information that the scripts
               require to complete the deployment process

Output         - ZTICoalesce.log. Log file that contains events that this script generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTICoalesce.wsf </debug:value>

Arguments

                                                                                     ﾉ   Expand table

Value                     Description

/debug:value              Outputs the event messages to the console and to the .log files. If the
                          value specified in value is:

                          - TRUE, event messages are sent to the console and the .log files

                          - FALSE, event messages are sent only to the .log files (This is the
                          behavior when the argument is not provided.)

/CoalesceDigits:value     Specifies the number of digits that need to be provided when creating
                          the numbering sequence. For example, a value of:

                          - 2 would create PACKAGE03

                          - 3 would create PACKAGE003

                          The default value if this argument is not provided is 3.

<!-- p.1254 -->

Properties

                                                                                   ﾉ    Expand table

 Name                                                    Read                   Write

 CoalescePattern                                         -

 CoalesceTarget                                          -

ZTIConfigFile.vbs
This script contains common routines for processing MDT XML files.

                                                                                   ﾉ    Expand table

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

 Output       - ZTIConfigFile.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

 References   Net.exe

 Location     distribution\Scripts

 Use          <script language="VBScript" src="ZTIConfigFile.vbs"/>

Arguments

                                                                                   ﾉ    Expand table

 Value                                Description

 None                                 None

Properties

                                                                                   ﾉ    Expand table

<!-- p.1255 -->

 Name                                                            Read               Write

 IsSafeForWizardHTML                                             -

 MandatoryApplications                                           -

 SkipGroupSubFolders                                             -

ZTIConfigure.wsf
This script configures the Unattend.xml file with the property values specified earlier in
the MDT deployment process. The script configures the appropriate file based on the
operating system being deployed.

This script reads the ZTIConfigure.xml file to determine how to update the Unattend.xml
file with the appropriate values specified in the deployment properties. The
ZTIConfigure.xml file contains the information to translate properties to settings in the
Unattend.xml file.

                                                                                   ﾉ    Expand table

 Value        Description

 Input        - ZTIConfigure.xml. Contains a list of property values (specified earlier in the
              deployment process) and their corresponding configuration settings

              - Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

 Output       - ZTIConfigure.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

 References   ZTIUtility.vbs. Includes support functions and subroutines that the script uses

 Location     distribution\Scripts

 Use          cscript ZTIConfigure.wsf </debug:value>

Arguments

                                                                                   ﾉ    Expand table

<!-- p.1256 -->

Value            Description

/debug:value     Outputs the event messages to the console and to the .log files. If the value
                 specified in value is:

                 - TRUE, event messages are sent to the console and the .log files

                 - FALSE, event messages are sent only to the .log files (This is the behavior when
                 the argument is not provided.)

Properties

                                                                                  ﾉ       Expand table

Name                                                                Read              Write

ComputerName                                                        -                 -

DeploymentType                                                      -

DeploymentMethod                                                    -

DeployRoot                                                          -

DestinationLogicalDrive                                             -

DomainAdminDomain                                                   -

ImageBuild                                                          -

OSDAnswerFilePath                                                   -

OSDAnswerFilePathSysprep                                            -

OSDComputerName                                                     -

Phase                                                               -

TaskSequenceID                                                      -

ZTIConfigureADDS.wsf
                                                                                  ﾉ       Expand table

Value          Description

Input          Environment variables. Contains the property values, custom property values,
               database connections, deployment rules, and other information that the scripts

<!-- p.1257 -->

Value          Description

               require to complete the deployment process

Output         - ZTIConfigureADDS.log. Log file that contains events that this script generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     - Dcpromo.exe. Installs and removes AD DS

               - Net.exe. Performs network management tasks

               - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTIConfigureADDS.wsf </debug:value>

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

Name                                                                Read                Write

ADDSLogPath                                                         -

ADDSPassword                                                        -

ADDSUserDomain                                                      -

ADDSUserName                                                        -

AutoConfigDNS                                                       -

<!-- p.1258 -->

 Name                                                             Read              Write

 ChildName                                                        -

 ConfirmGC                                                        -

 DatabasePath                                                     -

 DomainLevel                                                      -

 DomainNetBiosName                                                -

 ForestLevel                                                      -

 NewDomain                                                        -

 NewDomainDNSName                                                 -

 OSVersion                                                        -

 ParentDomainDNSName                                              -

 ReplicaOrNewDomain                                               -                 -

 ReplicaDomainDNSName                                             -

 ReplicationSourceDC                                              -

 SafeModeAdminPassword                                            -

 SiteName                                                         -

 SysVolPath                                                       -

ZTIConfigureDHCP.wsf
This script configures DHCP on the target computer.

  ７ Note

  DHCP should already be installed on the target computer before running this script.

                                                                                ﾉ       Expand table

 Value         Description

 Input         Environment variables. Contains the property values, custom property values,
               database connections, deployment rules, and other information that the scripts

<!-- p.1259 -->

Value          Description

               require to complete the deployment process

Output         - ZTIConfigureDHCP.log. Log file that contains events that this script generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     - Netsh.exe. A utility that permits automating the configuration of networking
               components

               - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTIConfigureDHCP.wsf </debug:value>

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

Name                                                                        Read         Write

DHCPScopesxDescription                                                      -

DHCPScopesxEndIP                                                            -

DHCPScopesxExcludeStartIP                                                   -

DHCPScopesxExcludeEndIP                                                     -

DHCPScopesxIP                                                               -

DHCPScopesxName                                                             -

<!-- p.1260 -->

 Name                                                              Read        Write

 DHCPScopesxOptionRouter                                           -

 DHCPScopesxOptionDNSDomainName                                    -

 DHCPScopesxOptionDNSServer                                        -

 DHCPScopesxOptionLease                                            -

 DHCPScopesxOptionNBTNodeType                                      -

 DHCPScopesxOptionPXEClient                                        -

 DHCPScopesxOptionWINSServer                                       -

 DHCPScopesxStartIP                                                -

 DHCPScopesxSubnetmask                                             -

 DHCPServerOptionDNSDomainName                                     -

 DHCPServerOptionDNSServer                                         -

 DHCPServerOptionNBTNodeType                                       -

 DHCPServerOptionPXEClient                                         -

 DHCPServerOptionRouter                                            -

 DHCPServerOptionWINSServer                                        -

  ７ Note

  The xin the properties listed here is a placeholder for a zero-based array that
  contains DHCP configuration information.

ZTIConfigureDNS.wsf
This script configures DNS on the target computer. To perform the actual configuration
tasks, the script uses the Dnscmd utility.

For more information about Dnscmd.exe, see Dnscmd Overview.

  ７ Note

  DNS should already be installed on the target computer before running this script.

<!-- p.1261 -->

                                                                                    ﾉ   Expand table

Value          Description

Input          Environment variables. Contains the property values, custom property values,
               database connections, deployment rules, and other information that the scripts
               require to complete the deployment process

Output         - ZTIConfigureDNS.log. Log file that contains events that this script generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     - Dnscmd.exe. Assists administrators with DNS management

               - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTIConfigureDNS.wsf </debug:value>

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

Name                                                                         Read         Write

DNSServerOptionDisableRecursion                                              -

DNSServerOptionBINDSecondaries                                               -

DNSServerOptionFailOnLoad                                                    -

DNSServerOptionEnableRoundRobin                                              -

<!-- p.1262 -->

 Name                                                                        Read          Write

 DNSServerOptionEnableNetmaskOrdering                                        -

 DNSServerOptionEnableSecureCache                                            -

 DNSServerOptionNameCheckFlag                                                -

 DNSZonesxName                                                               -

 DNSZonesxType                                                               -

 DNSZonesxMasterIP                                                           -

 DNSZonesxDirectoryPartition                                                 -

 DNSZonesxFileName                                                           -

 DNSZonesxScavenge                                                           -

 DNSZonesxUpdate                                                             -

  ７ Note

  The xin the properties listed here is a placeholder for a zero-based array that
  contains DNS configuration information.

ZTIConnect.wsf
The MDT deployment process uses this script to authenticate with a server computer
(such as a computer running SQL Server or another server that has a shared network
folder). When this script is run, it validates that a connection can be created to the
network shared folder specified in the /uncpath argument.

                                                                                    ﾉ   Expand table

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

 Output       - ZTIConnect.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

 References   ZTIUtility.vbs. Includes support functions and subroutines that the script uses

<!-- p.1263 -->

 Value          Description

 Location       distribution\Scripts

 Use            cscript ZTIConnect.wsf /UNCPath:<uncpath> </debug:value>

Arguments

                                                                                    ﾉ     Expand table

 Value                  Description

 /UNCPath:uncpath       Specifies a fully qualified UNC path to a network shared folder

 /debug:value           Outputs the event messages to the console and to the .log files; if the value
                        specified in value is:

                        - TRUE, event messages are sent to the console and the .log files

                        - FALSE, event messages are sent only to the .log files (This is the behavior
                        when the argument is not provided.)

Properties

                                                                                    ﾉ     Expand table

 Name                                  Read                            Write

 None

ZTICopyLogs.wsf
Copy the Smsts.log and BDD.log files to a subfolder beneath the share that the SLShare
property specifies. The subfolder takes the name that OSDComputerName,
_SMSTSMachineName, or HostName specifies.

                                                                                    ﾉ     Expand table

 Value          Description

 Input          Environment variables. Contains the property values, custom property values,
                database connections, deployment rules, and other information that the scripts
                require to complete the deployment process

<!-- p.1264 -->

 Value        Description

 Output       - ZTICopyLogs.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

 References   ZTIUtility.vbs. Includes support functions and subroutines that the script uses

 Location     distribution\Scripts

 Use          cscript ZTICopyLogs.wsf </debug:value>

Arguments

                                                                                   ﾉ   Expand table

 Value         Description

 /debug:       Outputs the event messages to the console and to the .log files. If the value
 value         specified in value is:

               - TRUE, event messages are sent to the console and the .log files

               - FALSE, event messages are sent only to the .log files (This is the behavior when
               the argument is not provided.)

Properties

                                                                                   ﾉ   Expand table

 Name                                Read                           Write

 None

ZTIDataAccess.vbs
This script contains common routines for database access.

                                                                                   ﾉ   Expand table

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts

<!-- p.1265 -->

 Value        Description

              require to complete the deployment process

 Output       - ZTIDataAccess.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

 References   None

 Location     distribution\Scripts

 Use          <script language="VBScript" src="ZTIDataAccess.vbs"/>

Arguments

                                                                                    ﾉ   Expand table

 Value                               Description

 None                                None

Properties

                                                                                    ﾉ   Expand table

 Name                                                      Read                 Write

 _SMSTSReserved1                                           -

 _SMSTSReserved2                                           -

 RulesFile                                                 -

 UserDomain                                                -                    -

 UserID                                                    -                    -

 UserPassword                                              -                    -

ZTIDisableBDEProtectors.wsf
If BitLocker is enabled, this script suspends the BitLocker protectors configured on the
system.

<!-- p.1266 -->

                                                                                     ﾉ   Expand table

Value          Description

Input          Environment variables. Contains the property values, custom property values,
               database connections, deployment rules, and other information that the scripts
               require to complete the deployment process

Output         - ZTIDisableBDEProtectors.log. Log file that contains events that this script
               generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTIDisableBDEProtectors.wsf </debug:value>

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

Name                                                       Read                  Write

ImageBuild                                                 -

ISBDE                                                                            -

OSCurrentBuild                                             -

OSCurrentVersion                                           -

<!-- p.1267 -->

 Name                                                  Read               Write

 OSVersion                                             -

ZTIDiskpart.wsf
This script creates the disk partitions on the target computer by calling the Diskpart
utility. The parameters used to configure the disk are specified by the Task Sequencer or
in CustomSettings.ini. ZTIDiskpart.wsf is primarily run in New Computer scenarios. The
process works like this:

   1. The MDT deployment process runs the ZTIDiskpart.wsf script based on the steps
     and sequence of steps in the Task Sequencer.

   2. ZTIDiskpart.wsf starts the Diskpart utility and sends it the required configuration
     commands.

   3. ZTIDiskpart.wsf runs Diskpart.exe and provides a .txt file as a command-line
     parameter.

   4. The disk is initially cleaned by sending Diskpart the CLEAN command.

   5. If this is the first disk and no disk configuration has been specified by the Task
     Sequencer or in CustomSettings.ini, a single partition is created to store the
     operating system. However, if a disk configuration has been specified, the disk will
     be configured according to the specified configuration.

   6. If BitLocker is to be enabled, space is reserved at the end of the first disk.

   7. All format commands are queued until after Diskpart has finished. If not explicitly
     specified by the Task Sequencer or in CustomSettings.ini, ZTIDiskpart.wsf performs
     a quick format of drive C using the following command: FORMAT C: /FS:NTFS
     /V:OSDisk /Q /Y .

   8. ZTIDiskpart.wsf copies the ZTIDiskpart_diskpart.log and BDD.log files from the
     RAM disk back to the hard drive.

     Customize the disk configuration of the target computer by providing the required
     information in the Task Sequencer or in CustomSettings.ini.

     For more information about configuring disks, see the MDT document Using the
     Microsoft Deployment Toolkit.

<!-- p.1268 -->

                                                                                    ﾉ   Expand table

Value          Description

Input          Environment variables. Contains the property values, custom property values,
               database connections, deployment rules, and other information that the scripts
               require to complete the deployment process

Output         - ZTIDiskpart.log. Log file that contains events that this script generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     - Diskpart.exe. Utility that allows for the automated management of disks,
               partitions, and volumes

               - Format.com. Formats the hard disk

               - ZTIDiskUtility.vbs. Includes support functions and subroutines that the script uses

               - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTIDiskpart.wsf </debug:value>

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

Name                                                                       Read              Write

BDEDriveLetter                                                             -

<!-- p.1269 -->

 Name                                                                        Read           Write

 BDEDriveSize                                                                -

 BDEInstall                                                                  -

 DeployDrive                                                                 -

 DeploymentType                                                              -

 DestinationDisk                                                             -

 DestinationLogicalDrive                                                                    -

 DoNotCreateExtraPartition                                                   -

 ImageBuild                                                                  -

 OSDDiskIndex                                                                -

 OSDDiskpartBiosCompatibilityMode                                            -              -

 OSDDiskType                                                                 -

 OSDPartitions                                                               -

 OSDPartitionStyle                                                           -

 SMSTSLocalDataDrive                                                                        -

 VolumeLetterVariable                                                        -

ZTIDiskUtility.vbs
This script contains disk-related functions and subroutines that the various scripts in the
MDT deployment process call.

                                                                                      ﾉ   Expand table

 Value          Description

 Input          None

 Output         - ZTIDiskUtility.log. Log file that contains events that this script generates

                - BDD.log. Log file that contains events that all MDT scripts generate

 References     - BcdBoot.exe. Configures the system partition

<!-- p.1270 -->

 Value        Description

              - DiskPart.exe. Utility that allows for the automated management of disks,
              partitions, and volumes

 Location     distribution\Scripts

 Use          <script language="VBScript" src="ZTIDiskUtility.vbs"/>

Arguments

                                                                                  ﾉ    Expand table

 Value                               Description

 None                                None

Properties

                                                                                  ﾉ    Expand table

 Name                                                           Read               Write

 DestinationLogicalDrive                                        -

 UILanguage                                                     -                  -

ZTIDomainJoin.wsf
During the State Restore deployment phase, this script verifies that the computer is
joined to a domain and recovers from failed attempts to join a domain.

                                                                                  ﾉ    Expand table

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

 Output       - ZTIDomainJoin.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

<!-- p.1271 -->

Value        Description

References   - LTISuspend.wsf

             - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location     distribution\Scripts

Use          cscript ZTIDomainJoin.wsf </debug:value>

Arguments

                                                                                  ﾉ    Expand table

Value                         Description

/debug: value                 Outputs the event messages to the console and to the .log files. If
                              the value specified in value is:

                              - TRUE, event messages are sent to the console and the .log files

                              - FALSE, event messages are sent only to the .log files (This is the
                              behavior when the argument is not provided.)

/DomainErrorRecovery:         Attempts to join the computer to the domain. If the value specified
value                         in value is:

                              - AUTO. Retry the domain join process. Restart and retry. This is the
                              default script behavior.

                              - FAIL. Stops all processing. All task sequence processing stops.

                              - MANUAL. Stop processing; allows the user to manually join the
                              computer to the domain.

Properties

                                                                                  ﾉ    Expand table

Name                                                             Read               Write

DomainAdmin                                                      -

DomainAdminDomain                                                -

DomainAdminPassword                                              -

<!-- p.1272 -->

 Name                                                             Read               Write

 DomainErrorRecovery                                              -

 DomainJoinAttempts                                               -                  -

 JoinDomain                                                       -

 JoinWorkgroup                                                    -

 LTISuspend                                                                          -

 MachineObjectOU                                                  -

 SMSTSRebootRequested                                                                -

 SMSTSRetryRequested                                                                 -

ZTIDrivers.wsf
This script installs additional device drivers onto the target computer before initiating
the configuration of the operating system. This script reads the Drivers.xml file and
copies the list of device driver files in the Drivers.xml file (created by and managed in the
Drivers node in the Deployment Workbench) to the target computer.

                                                                                    ﾉ      Expand table

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

 Output       - PnpEnum.xml. Contains a list of all devices installed on the target computer

              - ZTIDrivers.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

 References   - Attrib.exe. Sets file and folder attributes

              - CMD.exe. Allows running of command-line tools

              - Microsoft.BDD.PnpEnum.exe. Utility that enumerates Plug and Play devices

              - Reg.exe. The console registry tool for reading and modifying registry data

              - ZTIConfigFile.vbs. Includes routines for processing XML files

<!-- p.1273 -->

Value          Description

               - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTIDrivers.wsf </debug:value>

Arguments

                                                                                   ﾉ   Expand table

Value             Description

/debug:value      Outputs the event messages to the console and to the .log files. If the value
                  specified in value is:

                  - TRUE, event messages are sent to the console and the .log files

                  - FALSE, event messages are sent only to the .log files (This is the behavior when
                  the argument is not provided.)

Properties

                                                                                   ﾉ   Expand table

Name                                                                  Read             Write

Architecture                                                          -

CustomDriverSelectionProfile                                          -

DeploymentMethod                                                      -

DeploymentType                                                        -

DestinationLogicalDrive                                               -                -

DoCapture                                                             -

DriverPaths                                                           -

DriverSelectionProfile                                                -

ImageBuild                                                            -

InstallFromPath                                                       -

<!-- p.1274 -->

 Name                                                                  Read              Write

 OSDAnswerFilePath                                                     -

 OSDAnswerFilePathSysPrep                                              -

 OSDPlatformArch                                                       -

 Phase                                                                 -

 ResourceRoot                                                          -

ZTIExecuteRunbook.wsf
This script runs Orchestrator runbooks on the target computer. An Orchestrator runbook
is the sequence of activities that orchestrate actions on computers and networks. You
can initiate Orchestrator runbooks in MDT using the Execute Runbook task sequence
step type, which in turn runs this script.

                                                                                     ﾉ   Expand table

 Value          Description

 Input          Environment variables contain the property values, custom property values,
                database connections, deployment rules, and other information that the scripts
                require to complete the deployment process.

 Output         - BDD.log contains events that all MDT scripts generate.

                - Return status of the runbook completion.

                - Return parameters from the runbook output.

 References     - ZTIUtility.vbs includes support functions and subroutines that the script uses.

 Location       distribution\Scripts

 Use            cscript ZTIExecuteRunbook.wsf </debug:value>

Arguments

                                                                                     ﾉ   Expand table

 Value            Description

 /debug:value     Outputs the event messages to the console and to the .log files. If the value
                  specified in value is:

<!-- p.1275 -->

 Value           Description

                 - TRUE, event messages are sent to the console and the .log files

                 - FALSE, event messages are sent only to the .log files (This is the behavior when
                 the argument is not provided.)

Properties

                                                                                   ﾉ   Expand table

 Name                                                                                  Read    Write

 OrchestratorServer                                                                    -

 RunbookName                                                                           -

 RunbookID                                                                             -

 RunbookParameterMode                                                                  -

 RunbookParametersxParameterID                                                         -

 RunbookParametersxParameterValue                                                      -

 RunbookOutputParameters                                                                       -

 Note:

 If a runbook returns output parameters, a task sequence variable is created for
 each parameter and the return value of the parameter is assigned to the task
 sequence variable.

This script creates the task sequence variables listed in the following table for internal
script use. Do not set these task sequence variables in CustomSettings.ini or in the MDT
DB.

                                                                                   ﾉ   Expand table

 Name                                     Description

 OrchestratorServer                       Name of the server running Orchestrator specified in
                                          Orchestrator Server in the Execute Runbook task
                                          sequence step

 RunbookName                              Name of the runbook specified in Runbook in the
                                          Execute Runbook task sequence step

<!-- p.1276 -->

 Name                                     Description

 RunbookID                                Identifier assigned to the runbook on the Orchestrator
                                          server

 RunbookParametersxParameterID            Identifier assigned to a specific runbook parameter on
                                          the Orchestrator server

 RunbookParametersxParameterName          Name assigned to a specific runbook parameter on the
                                          Orchestrator server

 RunbookParametersxParameterValue         Value assigned to a specific runbook parameter on the
                                          Orchestrator server

ZTIGather.wsf
This script gathers the properties and processing rules that control the deployment
process. The properties and rules (also known as local properties) are explicitly defined in
this script and contained in the ZTIGather.xml file, in the CustomSettings.ini file, and in
the MDT DB (created in the Database node in the Deployment Workbench).

                                                                                   ﾉ      Expand table

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

 Output       - ZTIGather.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

 References   - Wpeutil.exe. Initializes Windows PE and network connections; initiates LTI

              - ZTIDataAccess.vbs. Contains routines for database access

              - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

 Location     distribution\Scripts

 Use          cscript ZTIGather.wsf </debug:value> </localonly> </inifile:ini_file_name>

Arguments

                                                                                   ﾉ      Expand table

<!-- p.1277 -->

 Value                    Description

 /debug:value             Outputs the event messages to the console and to the .log files. If the
                          value specified in value is:

                          - TRUE, event messages are sent to the console and the .log files

                          - FALSE, event messages are sent only to the .log files (This is the behavior
                          when the argument is not provided.)

 /localonly               Returns only information about the target computer and the current
                          operating system installed on the target computer; does not parse the
                          input .ini file (specified in the /inifile argument); returns properties and
                          rules specified in the .ini file

                          If not specified, the script returns information about the target computer
                          and the currently installed operating system; parses the .ini file

 /inifile:ini_file_name   Name and path of the input .ini file that contains the properties and rules
                          used in the deployment processIf not specified, the script uses the default
                          value in CustomSettings.ini

Properties

                                                                                       ﾉ    Expand table

 Name                                   Read                             Write

 All                                    -                                -

ZTIGroups.wsf
This script captures and restores the local group membership on the target computer.
This script is called with the**/capture** argument to back up the group membership
from the target computer before deploying the operating system. The CaptureGroups
property contains the list of groups that script backs up. The script is called with
the**/restore** argument to restore the group membership after the operating system
is deployed. When performing a restore operation, it restores the membership of all
groups that were backed up when the script was run using the /capture argument.

  ７ Note

  When restoring group membership, the script does not create any destination
  groups that do not already exist on the target computer. Therefore, be sure to

<!-- p.1278 -->

 include all required groups in the reference computer when building the image file.

                                                                                   ﾉ       Expand table

Value          Description

Input          Environment variables. Contains the property values, custom property values,
               database connections, deployment rules, and other information that the scripts
               require to complete the deployment process

Output         - ZTIGroups.log. Log file that contains events that this script generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript ZTIGroups.wsf </debug:value> </backup> </restore>

Arguments

                                                                                   ﾉ       Expand table

Value            Description

/debug:value     Outputs the event messages to the console and to the .log files. If the value
                 specified in value is:

                 - TRUE, event messages are sent to the console and the .log files

                 - FALSE, event messages are sent only to the .log files (This is the behavior when
                 the argument is not provided.)

/capture         Backs up the group membership of the local groups on the target computer as
                 specified in the CaptureGroups property

/restore         Restores the group membership to the local groups backed up earlier in the
                 deployment process

Properties

                                                                                   ﾉ       Expand table

<!-- p.1279 -->

 Name                                                    Read                   Write

 CaptureGroups                                           -

 Groups                                                  -                      -

 HostName                                                -

ZTILangPacksOnline.wsf
This script installs language packs for Windows operating systems. The script is
expecting the language pack CAB files in a folder structure containing at least one
folder.

                                                                                    ﾉ    Expand table

 Value          Description

 Input          Environment variables. Contains the property values, custom property values,
                database connections, deployment rules, and other information that the scripts
                require to complete the deployment process

 Output         - ZTILangPacksOnline.log. Log file that contains events that this script generates

                - BDD.log. Log file that contains events that all MDT scripts generate

 References     - CMD.exe. Allows running of command-line tools

                - Lpksetup.exe. The Language Pack Setup tool used to add or remove language
                packs

                - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

 Location       distribution\Scripts

 Use            cscript ZTILangPacksOnline.wsf </debug:value>

Arguments

                                                                                    ﾉ    Expand table

 Value            Description

 /debug:value     Outputs the event messages to the console and to the .log files. If the value
                  specified in value is:

<!-- p.1280 -->

 Value            Description

                  - TRUE, event messages are sent to the console and the .log files

                  - FALSE, event messages are sent only to the .log files (This is the behavior when
                  the argument is not provided.)

Properties

                                                                                     ﾉ   Expand table

 Name                                              Read                      Write

 Architecture                                      -

 OSVersion                                         -

ZTIModifyVol.wsf
This script modifies a volume to set the GPT ID and attributes for utility volumes, which
is necessary for creating Windows RE partitions on computers with UEFI. This script
needs to be called when deploying to computers with UEFI for these situations:

     LTI deployments where custom partition (volume) structures are being created,
     such as creating five partitions instead of the standard four partitions that are
     typically created for use with UEFI

     All ZTI and UDI deployments

  ７ Note

  This script is intended to be called only when creating partitions structures for use
  with UEFI. This script should not be called when creating partition structures to be
  used in deployments without UEFI.

                                                                                     ﾉ   Expand table

 Value          Description

 Input          Environment variables. Contains the property values, custom property values,
                database connections, deployment rules, and other information that the scripts
                require to complete the deployment process
