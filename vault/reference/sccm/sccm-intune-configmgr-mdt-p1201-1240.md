---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1201-1240"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1201-1240
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1201-1240
family: sccm
documentKind: "doc"
abstract: "Component Configured By | Scenario Property Is Applicable MDT DB ✅ | ZTI (Configuration Manager) ✅ ﾉ Expand table Value Description server_name The name of the WSUS server, specified in HTTP format ﾉ Expand table Example [Settings] Priority=Default [Default] WSUSServer=https://W"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1201-1240

<!-- p.1201 -->

 Component            Configured By     |   Scenario                      Property Is Applicable

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                Description

 server_name          The name of the WSUS server, specified in HTTP format

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] WSUSServer=https://WSUSServerName[Settings]
 Priority=Default [Default] WSUSServer=https://WSUSServerName

WUMU_ExcludeKB
The list of Windows Update/Microsoft Update software updates to ignore (by associated
Knowledge Base articles).

Deployment project team members will want to periodically review the list of updates
being installed by the ZTIWindowsUpdate.wsf script to verify that each update meets
the project's needs and expectations. All updates are logged and recorded in the
ZTIWindowsUpdate.log file, which is generated during deployment. Each update will
indicate its status as INSTALL or SKIP and lists the UpdateID, the update name, and the
QNumber associated with each update. If an update needs to be excluded, that update
should be added to the CustomSettings.ini file (for LTI deployments).

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ❌                 |   ZTI (Configuration Manager)   ❌

                                                                               ﾉ   Expand table

<!-- p.1202 -->

 Value                Description

 WUMU_ExcludeKB       The list of Windows Update/Microsoft Update software updates to ignore by
                      QNumber

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] WUMU_ExcludeKB1=925471

WUMU_ExcludeID
The list of Windows Update/Microsoft Update software updates to ignore (by associated
update ID).

Deployment project team members will want to periodically review the list of updates
being installed by the ZTIWindowsUpdate.wsf script to verify that each update meets
the project's needs and expectations. All updates are logged and recorded in the
ZTIWindowsUpdate.log file, which is generated during deployment. Each update will
indicate its status as INSTALL or SKIP and lists the UpdateID, the update name, and the
QNumber associated with each update. If an update should be excluded, that update
should be added to the CustomSettings.ini file (for LTI deployments).

For example, if the installation of the Windows Malicious Software Removal Tool should
be excluded, look up the line in the ZTIWindowsUpdate.log that shows where the
update was identified and installed, and then select the UpdateID number. For example,
the UpdateID number for the Windows Malicious Software Removal Tool is adbe6425-
6560-4d40-9478-1e35b3cdab4f.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ❌                 |   ZTI (Configuration Manager)   ❌

                                                                               ﾉ   Expand table

<!-- p.1203 -->

 Value                Description

 WUMU_ExcludeID       The list of Windows Update/Microsoft Update software updates to ignore, by
                      UpdateID number

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] WUMU_ExcludeID1={adbe6425-6560-4d40-9478-1e35b3cdab4f}
 [Settings] Priority=Default [Default] WUMU_ExcludeID1={adbe6425-6560-4d40-9478-1e35b3cdab4f}

XResolution
The horizontal resolution of the monitor on the target computer, specified in pixels. In
the example, the value 1024 indicates the horizontal resolution of the monitor is 1,024
pixels. This value is inserted into the appropriate configuration settings in Unattend.xml.

  ７ Note

  The default values (in the Unattend.xml template file) are 1,024 pixels horizontal
  resolution, 768 pixels vertical resolution, 32-bit color depth, and 60 Hz vertical
  refresh rate.

                                                                                  ﾉ   Expand table

 Component               Configured By   |   Scenario                       Property Is Applicable

 BootStrap.ini           ❌               |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini      ✅               |

 MDT DB                  ✅               |   ZTI (Configuration Manager)    ✅

                                                                                  ﾉ   Expand table

 Value                    Description

 horizontal_resolution    The horizontal resolution of the monitor on the target computer in pixels

                                                                                  ﾉ   Expand table

<!-- p.1204 -->

 Example

 [Settings] Priority=Default [Default] BitsPerPel=32 VRefresh=60 XResolution=1024
 YResolution=768[Settings] Priority=Default [Default] BitsPerPel=32 VRefresh=60
 XResolution=1024 YResolution=768

YResolution
The vertical resolution of the monitor on the target computer, specified in pixels. In the
example, the value 768 indicates the vertical resolution of the monitor is 768 pixels. This
value gets inserted into the appropriate configuration settings in Unattend.xml.

  ７ Note

  The default values (in the Unattend.xml template file) are 1,024 pixels horizontal
  resolution, 768 pixels vertical resolution, 32-bit color depth, and 60 Hz vertical
  refresh rate.

                                                                                  ﾉ   Expand table

 Component             Configured By    |   Scenario                        Property Is Applicable

 BootStrap.ini         ❌                |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini    ✅                |

 MDT DB                ✅                |   ZTI (Configuration Manager)     ✅

                                                                                  ﾉ   Expand table

 Value                 Description

 vertical_resolution   The vertical resolution of the monitor on the target computer in pixels

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] BitsPerPel=32 VRefresh=60 XResolution=1024
 YResolution=768[Settings] Priority=Default [Default] BitsPerPel=32 VRefresh=60
 XResolution=1024 YResolution=768

<!-- p.1205 -->

Providing Properties for Skipped Deployment
Wizard Pages
Table 6 lists the individual Deployment Wizard pages, the property to skip the
corresponding wizard page, and the properties that must be configured when skipping
the wizard page.

If the SkipWizard property is used to skip all the Deployment Wizard pages, provide all
the properties in the Configure these properties column. For examples of various
deployment scenarios that skip Deployment Wizard pages, see the section, "Fully
Automated LTI Deployment Scenario", in the MDT document Microsoft Deployment
Toolkit Samples Guide.

  ７ Note

  In instances where the Configure These Properties column is blank, no properties
  need to be configured when skipping the corresponding wizard page.

Table 6. Deployment Wizard Pages
                                                                          ﾉ   Expand table

 Skip this wizard page       Using this property           Configure these properties

 Welcome                     SkipBDDWelcome

 Specify credentials for     Skipped by providing          - UserID
 connecting to network       properties in next column
 shares                                                    - UserDomain

                                                           - UserPassword

 Task Sequence               SkipTaskSequence              - TaskSequenceID

 Computer Details            SkipComputerName,             - OSDComputerName

                             SkipDomainMembership          - JoinWorkgroup

                                                           -or-

                                                           - JoinDomain

                                                           - DomainAdmin

<!-- p.1206 -->

Skip this wizard page    Using this property    Configure these properties

User Data                SkipUserData           - UDDir

                                                - UDShare

                                                - UserDataLocation

Move Data and Settings   SkipUserData           - UDDir

                                                - UDShare

                                                - UserDataLocation

User Data (Restore)      SkipUserData           - UDDir

                                                - UDShare

                                                - UserDataLocation

Computer Backup          SkipComputerBackup     - BackupDir

                                                - BackupShare

                                                - ComputerBackupLocation

Product Key              SkipProductKey         - ProductKey

                                                -or-

                                                - OverrideProductKey

Language Packs           SkipPackageDisplay     LanguagePacks

Locale and Time          SkipLocaleSelection,   - KeyboardLocale
                         SkipTimeZone
                                                - UserLocale

                                                - UILanguage

                                                - TimeZoneName

Roles and Features       SkipRoles              - OSRoles

                                                - OSRoleServices

                                                - OSFeatures

Applications             SkipApplications       Applications

Administrator Password   SkipAdminPassword      AdminPassword

<!-- p.1207 -->

Skip this wizard page      Using this property   Configure these properties

Local Administrators       SkipAdminAccounts     - Administrators

Capture Image              SkipCapture           - ComputerBackupLocation

Bitlocker                  SkipBitLocker         - BDEDriveLetter

                                                 - BDEDriveSize

                                                 - BDEInstall

                                                 - BDEInstallSuppress

                                                 - BDERecoveryKey

                                                 - TPMOwnerPassword

                                                 - OSDBitLockerStartupKeyDrive

                                                 -
                                                 OSDBitLockerWaitForEncryption

Ready to begin             SkipSummary           -

Operating system           SkipFinalSummary      -
deployment completed
successfully

Operating system           SkipFinalSummary      -
deployment did not
complete successfully

Related articles
    Task Sequence Steps.
    Scripts.
    Support Files.
    Utilities.
    MDT Windows PowerShell Cmdlets.
    Tables and Views in the MDT DB.
    Windows 7 Feature Dependency Reference.
    UDI Reference.

Feedback

<!-- p.1208 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1209 -->

Scripts
Article • 02/12/2024

The scripts used in LTI and ZTI deployments reference properties that determine the
process steps and configuration settings used during the deployment process. Use this
reference section to help it determine the correct scripts to include in actions and the
valid arguments to provide when running each script. The following information is
provided for each script:

      Name.Specifies the name of the script.

      Description.Provides a description of the purpose of the script and any pertinent
      information regarding script customization.

      Input. Indicates the files used for input to the script.

      Output.Indicates the files created or modified by the script.

      References.Indicates other scripts or configuration files that are referenced by the
      script.

      Location.Indicates the folder where the script can be found. In the information for
      the location, the following variables are used:

         program_files. This variable points to the location of the Program Files folder on
         the computer where MDT is installed.

         distribution. This variable points to the location of the Distribution folder for
         the deployment share.

         platform. This variable is a placeholder for the operating system platform (x86
         or x64).

      Use.Provides the commands and options that you can specify.

      Arguments and description. Indicate the valid arguments to be specified for the
      script and a brief description of what each argument means.

      Properties.The properties referenced by the script.

BDD_Autorun.wsf
This script displays a dialog box that indicates the user inserted deployment media
created by the MDT process (such as a bootable DVD or a removable hard disk). The

<!-- p.1210 -->

message is displayed for 15 seconds. If no action is taken, the script starts LiteTouch.vbs.

For more information about LiteTouch.vbs, see LiteTouch.vbs.

                                                                               ﾉ   Expand table

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information required by the
              scripts to complete the deployment process

 Output       None

 References   LiteTouch.vbs. Initiates LTI

 Location     distribution\Scripts

 Use          None

Arguments

                                                                               ﾉ   Expand table

 Value                                Description

 None                                 None

Properties

                                                                               ﾉ   Expand table

 Name                                Read                         Write

 None

BDD_Welcome_ENU.xml
This XML file contains the script code and HTML layout for the Welcome to Windows
Deployment page that is displayed at the start of the Deployment Wizard. This XML file
is read by Wizard.hta, which runs the wizard pages embedded in this XML file.

                                                                               ﾉ   Expand table

<!-- p.1211 -->

 Value        Description

 Input        None

 Output       None

 References   - NICSettings_Definition_ENU.xml. Allows the user to provide configuration settings
              for network adapters

              - Wizard.hta. Displays the Deployment Wizard pages

              - WPEUtil.exe. Initializes Windows PE and network connections; initiates LTI

 Location     distribution\Tools\platform

 Use          mshta.exeWizard.hta BDD_Welcome_ENU.xml

Arguments

                                                                                 ﾉ       Expand table

 Value                               Description

 None                                None

Properties

                                                                                 ﾉ       Expand table

 Name                                                             Read               Write

 KeyboardLocalePE                                                 -

 WelcomeWizardCommand                                                                -

 WizardComplete                                                                      -

Credentials_ENU.xml
This XML file contains the script code and HTML layout for the Specify credentials for
connecting to network shares wizard page in the Deployment Wizard. This XML file is
read by Wizard.hta, which runs the wizard pages embedded in this XML file.

  ７ Note

<!-- p.1212 -->

  This wizard page is only displayed if there is a failure while validating the
  predefined user credentials.

                                                                                    ﾉ   Expand table

 Value        Description

 Input        None

 Output       None

 References   Credentials_scripts.vbs. Contains user credential support functions

 Location     distribution\Scripts

 Use          mshta.exe Wizard.hta /NotWizard /definition:Credentials_ENU.xml
              [/ValidateAgainstDomain:domain &#124; /ValidateAgainstUNCPath:uncpath]
              </DoNotSave> </LeaveShareOpen>

Arguments

                                                                                    ﾉ   Expand table

 Value                               Description

 None                                None

Properties

                                                                                    ﾉ   Expand table

 Name                                Read                          Write

 None

Credentials_scripts.vbs
This script parses the arguments that were provided when loading the
Credentials_ENU.xml file into the Deployment Wizard. It also performs user credential
validation. This script is read by the Credentials_ENU.xml file.

For more information about Credentials_ENU.xml, see the corresponding topic in
Credentials_ENU.xml.

<!-- p.1213 -->

                                                                                   ﾉ   Expand table

 Value         Description

 Input         None

 Output        Event messages are written to these log files:

               - Credentials_scripts.log. Log file that contains events generated by this script

               - BDD.log. Log file that contains events generated by all MDT scripts

 References    None

 Location      distribution\Scripts

 Use           <script language="VBScript" src="Credentials_scripts.vbs"/>

Arguments

                                                                                   ﾉ   Expand table

 Value                                Description

 None                                 None

Properties

                                                                                   ﾉ   Expand table

 Name                                                   Read                   Write

 UserCredentials                                                               -

 UserDomain                                             -

DeployWiz_Definition_ENU.xml
This XML file contains the script code and HTML layout for each wizard page in the
Deployment Wizard. This file is read by Wizard.hta, which runs the wizard pages
embedded in this XML file. This .xml file contains the following wizard pages:

       Welcome

       Specify credentials for connecting to network shares

<!-- p.1214 -->

    Task Sequence

    Computer Details

    User Data

    Move Data and Settings

    User Data (Restore)

    Computer Backup

    Product Key

    Language Packs

    Locale and Time

    Roles and Features

    Applications

    Administrator Password

    Local Administrators

    Capture Image

    BitLocker

    Ready to Begin

                                                                                ﾉ   Expand table

Value        Description

Input        None

Output       None

References   - DeployWiz_Initialization.vbs. Includes support functions and subroutines used by
             the script

             - DeployWiz_Validation.vbs. Includes support functions and subroutines used by
             the script

             - ZTIBackup.wsf. Creates a backup of the target computer

             - ZTIPatches.wsf. Installs updates (language packs, security updates, and so on)

<!-- p.1215 -->

Value        Description

             - ZTIUserState.wsf. Initializes user state migration to capture and restore user state
             on the target computer

Location     distribution\Scripts

Use          None

Arguments

                                                                                  ﾉ   Expand table

Value                               Description

None                                None

Properties

                                                                                  ﾉ   Expand table

Name                                                             Read              Write

DeploymentMethod                                                 -

DeploymentType                                                   -

DoCapture                                                        -

ImageBuild                                                       -

ImageFlags                                                       -

IsBDE                                                            -

IsServerOS                                                       -

JoinDomain                                                       -

OSDComputerName                                                  -

OSVersion                                                        -

SkipAdminAccounts                                                -

SkipAdminPassword                                                -

SkipApplications                                                 -

<!-- p.1216 -->

 Name                                                          Read     Write

 SkipBitLocker                                                 -

 SkipCapture                                                   -

 SkipComputerBackup                                            -

 SkipComputerName                                              -

 SkipDomainMembership                                          -

 SkipLocaleSelection                                           -

 SkipPackageDisplay                                            -

 SkipProductKey                                                -

 SkipRoles                                                     -

 SkipSummary                                                   -

 SkipTaskSequence                                              -

 SkipTimeZone                                                  -

 SkipUserData                                                  -

 TaskSequenceTemplate                                          -

 UserDomain                                                    -

 UserID                                                        -

 UserPassword                                                  -

 USMTOfflineMigration                                          -

DeployWiz_Initialization.vbs
This script initializes the pages in the Deployment Wizard (stored in
DeployWiz_Definition_ENU.xml). It also contains functions and subroutines that the
Deployment Wizard calls during an LTI deployment.

                                                                        ﾉ   Expand table

 Value         Description

 Input         - DomainOUList.xml. Contains a list of domain OUs

<!-- p.1217 -->

Value          Description

               - ListOfLanguages.xml

               - LocationServer.xml. Contains a list of available deployment shares

               - Environment variables. Contains the list of property values, custom properties,
               database connections, deployment rules, and other information that the scripts
               require to complete the deployment process; the environment variables are
               populated by ZTIGather.wsf

Output         Event message are written to these log files:

               - DeployWiz_Initialization.log. Log file that contains events generated by this script

               - BDD.log. Log file that contains events generated by all MDT scripts

References     ZTIApplications.wsf. Initiates application installation

Location       distribution\Scripts

Use            <script language="VBScript" src="DeployWiz_Initialization.vbs"/>

Arguments

                                                                                   ﾉ   Expand table

Value                                  Description

None                                   None

Properties

                                                                                   ﾉ   Expand table

Name                                                                        Read         Write

Architecture                                                                -

Applications                                                                -

BackupDir                                                                   -

BackupFile                                                                  -

BackupShare                                                                 -

BDEInstall                                                                  -

<!-- p.1218 -->

Name                           Read   Write

BDEKeyLocation                 -

BDERecoveryKey                 -

BDEWaitForEncryption           -

CapableArchitecture            -

ComputerBackupLocation         -

CustomWizardSelectionProfile   -

DeploymentType                 -

DeployRoot                     -

DomainAdmin                    -

DomainAdminDomain              -

DomainAdminPassword            -

DomainOUs                      -

ImageBuild                     -

ImageFlags                     -

ImageLanguage                  -

ImageLanguage001               -

ImageProcessor                 -

IsServerOS                     -

KeyboardLocale                 -

KeyboardLocale_Edit            -

LanguagePacks                  -

LanguagePacks001               -

LocalDeployRoot                -

MandatoryApplications          -

OSDComputerName                -

OSCurrentBuild                 -

<!-- p.1219 -->

 Name                                                             Read        Write

 OSDBitLockerCreateRecoveryPassword                               -

 OSDBitLockerMode                                                 -

 OSDBitLockerStartupKeyDrive                                      -

 OSDBitLockerWaitForEncryption                                    -

 OSSKU                                                            -

 OSVersion                                                        -

 OverrideProductKey                                               -

 ProductKey                                                       -

 SkipCapture                                                      -

 SkipDomainMembership                                             -

 TaskSequenceID                                                   -

 TimeZoneName                                                     -

 TSGUID                                                           -

 UDDir                                                            -

 UDShare                                                          -

 UILanguage                                                       -

 UserDataLocation                                                 -

 UserDomain                                                       -

 UserID                                                           -

 UserLocale                                                       -

 UserPassword                                                     -

 WizardSelectionProfile                                           -

DeployWiz_Validation.vbs
This script initializes and validates the information typed in the pages of the Deployment
Wizard (stored in DeployWiz_Definition_ENU.xml). This script contains functions and
subroutines that the Deployment Wizard calls during an LTI deployment.

<!-- p.1220 -->

                                                                                   ﾉ   Expand table

Value          Description

Input          - OperatingSystems.xml. Contains the list of operating systems available for
               deployment

               - Environment variables. Contains the list of property values, custom properties,
               database connections, deployment rules, and other information required by the
               scripts to complete the deployment process; the environment variables are
               populated by ZTIGather.wsf

Output         None

References     - Credentials_ENU.xml. Prompts the user for credentials that will be used when
               connecting to network resources

               - ZTIGather.wsf. Gathers properties and processing rules

Location       distribution\Scripts

Use            <script language="VBScript" src="DeployWiz_Validation.vbs"/>

Arguments

                                                                                   ﾉ   Expand table

Value                                 Description

None                                  None

Properties

                                                                                   ﾉ   Expand table

Name                                                      Read                 Write

Architecture                                              -

DeploymentType                                            -                    -

DeployTemplate                                                                 -

ImageBuild                                                -

ImageProcessor                                            -                    -

<!-- p.1221 -->

 Name                                                    Read                  Write

 OSVersion                                               -

 TaskSequenceID                                                                -

 TSGUID                                                  -

 UserCredentials                                         -

 UserDomain                                                                    -

 UserID                                                                        -

 UserPassword                                                                  -

LiteTouch.vbs
This script is called by the Deployment Wizard to initiate LTI. The script:

       Removes the C:\MININT folder (if it exists)

       Checks that the target computer meets the requirements for running the
       Deployment Wizard by calling ZTIPrereq.vbs

       Starts the Deployment Wizard by running LiteTouch.wsf

                                                                                   ﾉ   Expand table

 Value         Description

 Input         None

 Output        None

 References    - BDDRun.exe

               - ZTIPrereq.vbs. Used to determine whether the target computer meets the
               prerequisites for deploying a new operating system

               - LiteTouch.wsf. The script responsible for controlling the LTI deployment process

 Location      distribution\Scripts

 Use           cscript LiteTouch.vbs </debug:value>

Arguments

<!-- p.1222 -->

                                                                                     ﾉ      Expand table

 Value            Description

 /debug:value     Outputs the event messages to the console and to the .log files. If the value
                  specified in value is:

                  - TRUE, event messages are sent to the console and the .log files

                  - FALSE, event messages are sent only to the .log files (this is the behavior when
                  the argument is not provided)

Properties

                                                                                     ﾉ      Expand table

 Name                                  Read                            Write

 None

LiteTouch.wsf
This script is called by LiteTouch.vbs and is responsible for controlling the LTI
deployment process. This includes:

     Running the Deployment Wizard

     Running the LTI deployment process by using the appropriate task sequence file

                                                                                     ﾉ      Expand table

 Value          Description

 Input          - task_sequence_file.xml. Contains the tasks and sequence of tasks for the LTI
                deployment process

                - Environment variables. Contains the list of property values, custom properties,
                database connections, deployment rules, and other information required by the
                scripts to complete the deployment process; the environment variables are
                populated by ZTIGather.wsf

 Output         - LiteTouch.log. Log file that contains events that this script generates

                - BDD.log. Log file that contains events that all MDT scripts generate

<!-- p.1223 -->

Value        Description

References   - BDD_Welcome_ENU.xml. Displays the Deployment Wizard Welcome page for LTI
             deployment

             - DeployWiz_Definition_ENU.xml. Displays the Deployment Wizard pages for LTI
             deployment

             - Diskpart.exe. Utility that allows the automated management of disks, partitions,
             and volumes

             - LTICleanup.wsf. Performs cleanup tasks after deployment finishes

             - LTICopyScripts.wsf. Copies the deployment scripts to a local hard drive on the
             target computer

             - MSHTA.exe. HTML application host

             - RecEnv.exe. If this utility exists, the user is prompted to determine whether to
             launch Windows Recovery Environment.

             - Regsvr32.exe. Registers files (.dll, .exe, .ocx, and so on) with the operating system

             - Summary_Definition_ENU.xml. Displays the summary results for the LTI
             deployment

             - TsmBootStrap.exe. Task sequence Bootstrap utility

             - Wizard.hta. Displays the Deployment Wizard pages

             - WPEUtil.exe. Initializes Windows PE and network connections; initiates LTI

             - ZTIGather.wsf. Gathers properties and processing rules

             - ZTIPrereq.vbs. Checks that the target computer meets the requirements for
             running the Deployment Wizard

             - ZTINICConfig.wsf. Configures activated network adapters

             - ZTIUtility.vbs. Includes support functions and subroutines the script uses

Location     distribution\Scripts

Use          BDDRun.exe "wscript.exe <ScriptDirectory>\LiteTouch.wsf </debug:value>"

Arguments

<!-- p.1224 -->

                                                                                 ﾉ       Expand table

Value          Description

/debug:value   Outputs the event messages to the console and to the .log files. If the value
               specified in value is:

               - TRUE, event messages are sent to the console and the .log files

               - FALSE, event messages are sent only to the .log files (this is the behavior when
               the argument is not provided)

/Start         Creates a shortcut in the new operating system that runs once the shell starts

Properties

                                                                                 ﾉ       Expand table

Name                                                              Read               Write

_DoNotCleanLiteTouch                                              -

_SMSTSPackageName                                                                    -

AdminPassword                                                     -

Architecture                                                      -                  -

BootPE                                                            -                  -

ComputerBackupLocation                                                               -

ComputerName                                                      -

DeployDrive                                                       -                  -

DeploymentMethod                                                  -                  -

DeploymentType                                                    -                  -

DeployRoot                                                        -                  -

DestinationLogicalDrive                                                              -

DomainAdmin                                                                          -

DomainAdminDomain                                                                    -

DomainAdminPassword                                                                  -

<!-- p.1225 -->

Name                   Read   Write

FinishAction           -

HostName               -

IsServerCoreOS         -

JoinDomain             -

JoinWorkgroup          -      -

KeyboardLocalePE       -

LTISuspend             -

OSDAdapterCount        -

OSDComputerName        -      -

Phase                  -      -

ResourceDrive          -      -

ResourceRoot           -      -

RetVal                        -

SkipBDDWelcome         -

SkipFinalSummary       -      -

SkipWizard             -

SMSTSLocalDataDrive           -

TaskSequenceID         -

TimeZoneName                  -

UserDataLocation       -      -

UserDomain             -

UserID                 -

UserPassword           -

WelcomeWizardCommand   -

WizardComplete         -

<!-- p.1226 -->

LTIApply.wsf
This script is responsible for installing a Windows PE image to the target computer. The
Windows PE image is used to collect information about the target computer and to run
the deployment tasks on the target computer.

                                                                                   ﾉ     Expand table

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information the scripts require
              to complete the deployment process

 Output       - LTIApply.log. Log file that contains events that this script generates

              - LTIApply_wdsmcast.log. Log file that contains events that the Wdsmcast utility
              generates

              - BDD.log. Log file that contains events that all MDT scripts generate

 References   - CMD.exe. Allows the running of command-line tools

              - Bootsect.exe. Applies a boot sector to the hard disk

              - ImageX.exe. A utility used to create and manage WIM files

              - ZTIBCDUtility.vbs. Includes utility functions used when performing Boot Manager
              tasks

              - ZTIConfigFile.vbs. Includes routines for processing XML files

              - ZTIDiskUtility.vbs. Includes support functions and subroutines the script uses

              - ZTIUtility.vbs. Includes support functions and subroutines the script uses

              - Wdsmcast.exe. A utility that target computers use to join a multicast transmission

 Location     distribution\Scripts

 Use          cscript LTIApply.wsf </pe> </post> </debug:value>

Arguments

                                                                                   ﾉ     Expand table

<!-- p.1227 -->

Value          Description

/pe            Uses the process for installing the Windows PE image on the target computer

/post          Cleans up unnecessary files after the installation of an image

/debug:value   Outputs the event messages to the console and to the .log files; if the value
               specified in value is:

               - TRUE, event messages are sent to the console and the .log files

               - FALSE, event messages are sent only to the .log files (this is the behavior when
               the argument is not provided)

Properties

                                                                                 ﾉ     Expand table

Name                                                           Read                Write

Architecture                                                   -

BootPE                                                                             -

DeployRoot                                                     -

DestinationLogicalDrive                                        -                   -

OSGUID                                                         -

OSCurrentVersion                                               -

OSVersion                                                      -

ImageBuild                                                     -

ImageFlags                                                     -

ImageProcessor                                                 -

ISBDE                                                          -

SourcePath                                                                         -

TaskSequenceID                                                 -

UserDomain                                                     -

UserID                                                         -

UserPassword                                                   -

<!-- p.1228 -->

 Name                                                               Read               Write

 WDSServer                                                          -

LTICleanup.wsf
This script removes any files or configuration settings (such as scripts, folders, registry
entries, or automatic logon configuration settings) from the target computer after the
deployment process finishes.

                                                                                      ﾉ   Expand table

 Value          Description

 Input          Environment variables. Contains the list of property values, custom properties,
                database connections, deployment rules, and other information that the scripts
                require to complete the deployment process. The environment variables are
                populated by ZTIGather.wsf.

 Output         - LTICleanup.log. Log file that contains events that this script generates

                - BDD.log. Log file that contains events that all MDT scripts generate

 References     - Bootsect.exe. Applies a boot sector to the hard disk

                - Net.exe. Performs network management tasks

                - RegSvr32.exe. Registers files (.dll, .exe, .ocx, and so on) with the operating system

                - ZTIBCDUtility.vbs. Includes utility functions used when performing Boot Manager
                tasks

                - ZTIUtility.vbs. Includes support functions and subroutines the script uses

 Location       distribution\Scripts

 Use            cscript LTICleanup.wsf </debug:value>

Arguments

                                                                                      ﾉ   Expand table

 Value            Description

 /debug:value     Outputs the event messages to the console and to the .log files. If the value
                  specified in value is:

<!-- p.1229 -->

 Value          Description

                - TRUE, event messages are sent to the console and the .log files

                - FALSE, event messages are sent only to the .log files (this is the behavior when
                the argument is not provided)

Properties

                                                                                   ﾉ   Expand table

 Name                                                            Read               Write

 _DoNotCleanLiteTouch                                            -

 DeployRoot                                                      -

 DestinationLogicalDrive                                         -

 OSVersion                                                       -

LTICopyScripts.wsf
This script copies the deployment scripts for the LTI and ZTI deployment processes to a
local hard drive on the target computer.

                                                                                   ﾉ   Expand table

 Value        Description

 Input        - Summary_Definition_ENU.xml. Displays the summary results for the LTI
              deployment

              - Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

 Output       - LTICopyScripts.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

 References   ZTIUtility.vbs. Includes support functions and subroutines the script uses

 Location     distribution\Scripts

 Use          cscript LTICopyScripts.wsf </debug:value>

<!-- p.1230 -->

Arguments

                                                                                    ﾉ   Expand table

 Value            Description

 /debug:value     Outputs the event messages to the console and to the .log files. If the value
                  specified in value is:

                  - TRUE, event messages are sent to the console and the .log files

                  - FALSE, event messages are sent only to the .log files (this is the behavior when
                  the argument is not provided)

Properties

                                                                                    ﾉ   Expand table

 Name                                    Read                         Write

 None

LTIGetFolder.wsf
This script displays a dialog box that allows the user to browses to a folder. The selected
folder path is stored in the FOLDERPATH environment variable.

                                                                                    ﾉ   Expand table

 Value          Description

 Input          Environment variables. Contains the list of property values, custom properties,
                database connections, deployment rules, and other information that the scripts
                require to complete the deployment process. The environment variables are
                populated by ZTIGather.wsf.

 Output         None

 References     - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

                - WizUtility.vbs. Includes support functions and subroutines that the UI uses (such
                as wizard pages)

 Location       - distribution\Scripts

<!-- p.1231 -->

 Value          Description

                - program_files\Microsoft Deployment Toolkit\Scripts

 Use            cscript LTIGetFolder.wsf </debug:value>

Arguments

                                                                                      ﾉ   Expand table

 Value            Description

 /debug:value     Outputs the event messages to the console and to the .log files. If the value
                  specified in value is:

                  - TRUE, event messages are sent to the console and the .log files

                  - FALSE, event messages are sent only to the .log files (this is the behavior when
                  the argument is not provided)

Properties

                                                                                      ﾉ   Expand table

 Name                                                       Read                  Write

 DefaultFolderPath                                          -

 FolderPath                                                                       -

LTIOEM.wsf
This script is used by an OEM during an LTI OEM scenario to copy the contents of a
media deployment share to the target computer's hard disk to prepare it for duplication.

                                                                                      ﾉ   Expand table

 Value          Description

 Input          Environment variables. Contains the list of property values, custom properties,
                database connections, deployment rules, and other information that the scripts
                require to complete the deployment process. The environment variables are
                populated by ZTIGather.wsf.

<!-- p.1232 -->

Value          Description

Output         - LTIOEM.log. Log file that contains events that this script generates

               - BDD.log. Log file that contains events that all MDT scripts generate

References     - RoboCopy.exe. File and folder copy tool

               - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

Location       distribution\Scripts

Use            cscript LTIOEM.wsf </BITLOCKER &#124; /BDE> </debug:value>

Arguments

                                                                                   ﾉ     Expand table

Value            Description

/debug:value     Outputs the event messages to the console and to the .log files. If the value
                 specified in value is:

                 - TRUE, event messages are sent to the console and the .log files

                 - FALSE, event messages are sent only to the .log files (this is the behavior when
                 the argument is not provided)

/BITLOCKER       Enables BitLocker

/BDE             Enables BitLocker

Properties

                                                                                   ﾉ     Expand table

Name                                                             Read                Write

_DoNotCleanLiteTouch                                                                 -

DeployDrive                                                      -

DeployRoot                                                       -

TSGUID                                                           -

<!-- p.1233 -->

LTISuspend.wsf
This script suspends a task sequence to allow manual tasks to be performed. When this
script runs, it creates a Resume Task Sequence shortcut on the user's desktop that
allows the user to restart the task sequence after all manual tasks are completed.

  ７ Note

  This script is only supported while in the full operating system.

                                                                                    ﾉ    Expand table

 Value          Description

 Input          Environment variables. Contains the list of property values, custom properties,
                database connections, deployment rules, and other information the scripts require
                to complete the deployment process. The environment variables are populated by
                ZTIGather.wsf.

 Output         - LTISuspend.log. Log file that contains events that this script generates

                - BDD.log. Log file that contains events that all MDT scripts generate

 References     - LiteTouch.wsf. Controls the LTI deployment process

                - LTICopyScripts.wsf. Copies the deployment scripts to a local hard drive on the
                target computer

                - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

 Location       distribution\Scripts

 Use            cscript LTISuspend.wsf </debug:value>

Arguments

                                                                                    ﾉ    Expand table

 Value            Description

 /debug:value     Outputs the event messages to the console and to the .log files. If the value
                  specified in value is:

                  - TRUE, event messages are sent to the console and the .log files

<!-- p.1234 -->

 Value          Description

                - FALSE, event messages are sent only to the .log files (this is the behavior when
                the argument is not provided)

 /Resume        -

Properties

                                                                                   ﾉ     Expand table

 Name                                                             Read               Write

 LTISuspend                                                                          -

 SMSTSRebootRequested                                                                -

LTISysprep.wsf
This script prepares the target computer for running Sysprep, runs Sysprep on the target
computer, and then verifies that Sysprep ran successfully.

                                                                                   ﾉ     Expand table

 Value        Description

 Input        Environment variables. Contains the list of property values, custom properties,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process. The environment variables are
              populated by ZTIGather.wsf.

 Output       - LTISysprep.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

 References   - Expand.exe. Expands compressed files

              - Sysprep.exe. Prepares computers for duplication

              - ZTIConfigFile.vbs. Contains routines for processing XML files

              - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

 Location     distribution\Scripts

 Use          cscript LTISysprep.wsf </debug:value>

<!-- p.1235 -->

Arguments

                                                                                   ﾉ      Expand table

 Value            Description

 /debug:value     Outputs the event messages to the console and to the .log files. If the value
                  specified in value is:

                  - TRUE, event messages are sent to the console and the .log files

                  - FALSE, event messages are sent only to the .log files (This is the behavior when
                  the argument is not provided.)

Properties

                                                                                   ﾉ      Expand table

 Name                                                             Read                Write

 Architecture                                                     -

 DeployRoot                                                       -

 DestinationLogicalDrive                                          -

 DoCapture                                                        -

 OSCurrentBuild                                                   -

 OSDAnswerFilePath                                                -

 OSGUID                                                           -

 SourcePath                                                       -                   -

 TaskSequenceID                                                   -

NICSettings_Definition_ENU.xml
This XML file contains the script code and HTML layout for the Configure Static IP
Network Settings wizard page in the Deployment Wizard. During an LTI deployment,
Wizard.hta reads this file and runs the embedded wizard page that prompts for the
required network addressing configuration. If no static IP addressing configuration is
supplied, the deployment scripts will default to using DHCP to obtain the required
network configuration.

<!-- p.1236 -->

                                                                               ﾉ    Expand table

Value        Description

Input        None

Output       None

References   ZTINICUtility.vbs. Includes support functions and subroutines that the script uses

Location     distribution\Scripts

Use          None

Arguments

                                                                               ﾉ    Expand table

Value                               Description

None                                None

Properties

                                                                               ﾉ    Expand table

Name                                                              Read             Write

OSDAdapterxDNSServerList                                                           -

OSDAdapterxDNSSuffix                                                               -

OSDAdapterxGateways                                                                -

OSDAdapterxIPAddressList                                                           -

OSDAdapterxMacAddress                                                              -

OSDAdapterxSubnetMask                                                              -

OSDAdapterxWINSServerList                                                          -

OSDAdapterCount                                                                    -

 ７ Note

<!-- p.1237 -->

  Thexin the property names listed above is a placeholder for a zero-based array that
  contains network adapter information.

Summary_Definition_ENU.xml
This XML file contains the script code and HTML layout for the Deployment Summary
wizard page in the Deployment Wizard. During an LTI deployment, Wizard.hta reads this
file and runs the embedded wizard page that displays the summary results for the LTI
deployment. This XML file contains the following wizard pages:

       Success. Notification regarding the successful completion of the deployment tasks

       Failure. Notification regarding the failure to successfully complete the deployment
       tasks

                                                                               ﾉ   Expand table

 Value         Description

 Input         None

 Output        None

 References    Summary_Scripts.vbs. Includes support functions and subroutines that the wizard
               pages embedded in this XML file use

 Location      distribution\Scripts

 Use           None

Arguments

                                                                               ﾉ   Expand table

 Value                                Description

 None                                 None

Properties

                                                                               ﾉ   Expand table

<!-- p.1238 -->

 Name                                                         Read              Write

 SkipFinalSummary                                             -

 RetVal                                                       -

Summary_scripts.vbs
This script is called by the Summary wizard page of the Deployment Wizard. It contains
functions and subroutines used for initialization and validation.

                                                                                  ﾉ     Expand table

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

 Output       Event message are written to these log files:

              - Summary_scripts.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

 References   None

 Location     distribution\Scripts

 Use          <script language="VBScript" src="Summary_Scripts.vbs"/>

Arguments

                                                                                  ﾉ     Expand table

 Value                               Description

 None                                None

Properties

                                                                                  ﾉ     Expand table

<!-- p.1239 -->

 Name                                                       Read                  Write

 DeploymentType                                             -

 RetVal                                                     -

Wizard.hta
This Hypertext Application displays the Deployment Wizard pages.

                                                                                     ﾉ    Expand table

 Value          Description

 Input          Environment variables. Contains the list of property values, custom properties,
                database connections, deployment rules, and other information that the scripts
                require to complete the deployment process. The environment variables are
                populated by ZTIGather.wsf.

 Output         - Wizard.log. Log file that contains events that this script generates

                - BDD.log. Log file that contains events that all MDT scripts generate

 References     - LTIGetFolder.wsf. Script file that initiates a BrowseForFolder dialog box

                - ZTIConfigFile.vbs. Includes routines for processing XML files

                - ZTIUtility.vbs. Includes support functions and subroutines that the script uses

                - WizUtility.vbs. Includes support functions and subroutines that the script uses

 Location       - distribution\Scripts

                - program_files\Microsoft Deployment Toolkit\Scripts

 Use            mshta.exe Wizard.hta </definition:filename> </NotWizard> </debug:value>

Arguments

                                                                                     ﾉ    Expand table

 Value                    Description

 /debug:value             Outputs the event messages to the console and to the .log files. If the
                          value specified in value is:

                          - TRUE, event messages are sent to the console and the .log files

<!-- p.1240 -->

 Value                  Description

                        - FALSE, event messages are sent only to the .log files (This is the behavior
                        when the argument is not provided.)

 /NotWizard             Used to bypass wizard page prompts

 /Definition:filename   Specifies the XML file that is to be loaded into the wizard

Properties

                                                                                      ﾉ    Expand table

 Name                                                       Read                  Write

 Definition                                                 -

 DefaultFolderPath                                                                -

 FolderPath                                                 -

 WizardComplete                                                                   -

WizUtility.vbs
This script contains functions and subroutines that the various Deployment Wizard
scripts reference.

                                                                                      ﾉ    Expand table

 Value        Description

 Input        Environment variables. Contains the property values, custom property values,
              database connections, deployment rules, and other information that the scripts
              require to complete the deployment process

 Output       - WizUtility.log. Log file that contains events that this script generates

              - BDD.log. Log file that contains events that all MDT scripts generate

 References   LTIGetFolder.wsf. Script file that initiates a BrowseForFolderdialog box

 Location     - distribution\Scripts

              - program_files\Microsoft Deployment Toolkit\Scripts
