---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1161-1200"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1161-1200
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1161-1200
family: sccm
documentKind: "doc"
abstract: "TaskSequenceID Identifies the operating system task sequence to be deployed to the target computer. The task sequence ID is created on the Task Sequences node in the Deployment Workbench. The TaskSequenceID property allows alphanumeric characters, hyphens (-), and underscores (_"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1161-1200

<!-- p.1161 -->

TaskSequenceID
Identifies the operating system task sequence to be deployed to the target computer.
The task sequence ID is created on the Task Sequences node in the Deployment
Workbench. The TaskSequenceID property allows alphanumeric characters, hyphens (-),
and underscores (_). The TaskSequenceID property cannot be blank or contain spaces.

                                                                                  ﾉ   Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                |

 MDT DB                 ✅                |   ZTI (Configuration Manager)   ❌

                                                                                  ﾉ   Expand table

 Value                Description

 task_sequence_id     Identifier of the operating system task sequence defined in the Deployment
                      Workbench for the target operating system being deployed

                      Note:

                      Be sure to use the TaskSequenceID specified in the Deployment Workbench
                      UI, not the GUID of the TaskSequenceID.

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] TaskSequenceID=BareMetal

TaskSequenceName
Specifies the name of the task sequence being run.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

<!-- p.1162 -->

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ❌               |

 MDT DB               ❌               |   ZTI (Configuration Manager)   ❌

                                                                             ﾉ   Expand table

 Value                 Description

 task_sequence_name    Name of the task sequence being run, such as Deploy Windows 8.1 to
                       Reference Computer

                                                                             ﾉ   Expand table

 Example

 None

TaskSequenceVersion
Specifies the version of the task sequence being run.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ❌               |

 MDT DB               ❌               |   ZTI (Configuration Manager)   ❌

                                                                             ﾉ   Expand table

<!-- p.1163 -->

 Value                              Description

 task_sequence_version              Version of the task sequence being run, such as 1.00

                                                                                     ﾉ     Expand table

 Example

 None

TimeZoneName
The time zone in which the target computer is located. This value is inserted into the
appropriate configuration settings in Unattend.xml.

                                                                                     ﾉ     Expand table

 Component              Configured By       |     Scenario                      Property Is Applicable

 BootStrap.ini          ❌                   |     LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                   |

 MDT DB                 ✅                   |     ZTI (Configuration Manager)   ✅

                                                                                     ﾉ     Expand table

 Value                Description

 time_zone_name       The text value that indicates the time zone where the target computer is
                      located

                                                                                     ﾉ     Expand table

 Example

 [Settings] Priority=Default [Default] TimeZoneName=Pacific Standard Time DeployRoot=\\NYC-
 AM-FIL-01\Distribution$ ResourceRoot=\\NYC-AM-FIL-01\Resource$ UDShare=\\NYC-AM-FIL-
 01\MigData$ UDDir=%OSDComputerName% SLShare=\\NYC-AM-FIL-01\Logs$ UDProfiles=Administrator,
 User-01, ExtranetUser UserDataLocation=NONE

ToolRoot

<!-- p.1164 -->

Specifies the UNC path to the Tools\proc_arch folder (where proc_arch is the processor
architecture of the currently running operating system and can have a value of x86 or
x64), which is immediately beneath the root of the folder structure specified in the
DeployRoot property. The Tools\proc_arch folder contains utilities that MDT uses during
the deployment process.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                               ﾉ   Expand table

 Component             Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ❌               |

 MDT DB                ❌               |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value   Description

 path    The UNC or local path to the Tools\proc_arch folder (where proc_arch is the processor
         architecture of the currently running operating system and can have a value of x86 or
         x64) immediately beneath the root of the folder structure specified by the DeployRoot
         property

                                                                               ﾉ   Expand table

 Example

 None

TPMOwnerPassword
The TPM password (also known as the TPM administration password) for the owner of
the target computer. The password can be saved to a file or stored in AD DS.

  ７ Note

<!-- p.1165 -->

  If the TPM ownership is already set or TPM ownership is not allowed, then the
  TPMOwnerPassword property is ignored. If the TPM password is needed and the
  TPMOwnerPassword property is not provided, the TPM password is set to the local
  Administrator password.

                                                                              ﾉ   Expand table

 Component            Configured By   |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)    ✅

                                                                              ﾉ   Expand table

 Value           Description

 password        The TPM password for the owner of the target computer

                                                                              ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] BDEDriveLetter=S: BDEDriveSize=2000 BDEInstall=TPMKey
 BDERecoveryKey=TRUE BDEKeyLocation=C: TPMOwnerPassword=<complex_password> BackupShare=\\NYC-
 AM-FIL-01\Backup$ BackupDir=%OSDComputerName% DeployRoot=\\NYC-AM-FIL-01\Distribution$
 ResourceRoot=\\NYC-AM-FIL-01\Resource$ UDShare=\\NYC-AM-FIL-01\MigData$
 UDDir=%OSDComputerName%

UDDir
The folder in which the user state migration data is stored. This folder exists beneath the
network shared folder specified in UDShare.

                                                                              ﾉ   Expand table

 Component            Configured By   |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅               |

<!-- p.1166 -->

 Component             Configured By     |   Scenario                       Property Is Applicable

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ✅

                                                                                   ﾉ   Expand table

 Value      Description

 folder     The name of the folder that exists beneath the network shared folder

                                                                                   ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DeployRoot=\\NYC-AM-FIL-01\Distribution$
 ResourceRoot=\\NYC-AM-FIL-01\Resource$ UDShare=\\NYC-AM-FIL-01\MigData$
 UDDir=%OSDComputerName% SLShare=\\NYC-AM-FIL-01\Logs$ UDProfiles=Administrator, User-01,
 ExtranetUser UserDataLocation=NONE SkipCapture=NO

UDProfiles
A comma-delimited list of user profiles that need to be saved by Scanstate.exe during
the State Capture Phase.

                                                                                   ﾉ   Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                   ﾉ   Expand table

 Value                Description

 user_profiles        The list of user profiles to be saved, separated by commas

                                                                                   ﾉ   Expand table

<!-- p.1167 -->

 Example

 [Settings] Priority=Default [Default] DeployRoot=\\NYC-AM-FIL-01\Distribution$
 ResourceRoot=\\NYC-AM-FIL-01\Resource$ UDShare=\\NYC-AM-FIL-01\MigData$
 UDDir=%OSDComputerName% SLShare=\\NYC-AM-FIL-01\Logs$ UDProfiles=Administrator, User-01,
 ExtranetUser UserDataLocation=NONE SkipCapture=NO

UDShare
The network share where user state migration data is stored.

                                                                                 ﾉ   Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                |

 MDT DB                 ✅                |   ZTI (Configuration Manager)   ❌

                                                                                 ﾉ   Expand table

 Value           Description

 UNC_path        The UNC path to the network share where user state migration data is stored

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DeployRoot=\\NYC-AM-FIL-01\Distribution$
 ResourceRoot=\\NYC-AM-FIL-01\Resource$ UDShare=\\NYC-AM-FIL-01\MigData$
 UDDir=%OSDComputerName% SLShare=\\NYC-AM-FIL-01\Logs$ UDProfiles=Administrator, User-01,
 ExtranetUser UserDataLocation=NONE SkipCapture=NO

UILanguage
The default language to be used with the target operating system. If not specified, the
Deployment Wizard uses the language configured in the image being deployed.

                                                                                 ﾉ   Expand table

<!-- p.1168 -->

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ❌

                                                                              ﾉ   Expand table

 Value           Description

 UI_language     The default language for the operating system on the target computer

                                                                              ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] UserLocale=en-us UILanguage=en-us
 KeyboardLocale=0409:00000409

UserDataLocation
The location in which USMT stores user state migration data.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                              ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ❌

                                                                              ﾉ   Expand table

<!-- p.1169 -->

 Value           Description

 blank           If UserDataLocationis not specified or is left blank, the Deployment Wizard will
                 default to using the AUTO behavior.

 UNC_path        The UNC path to the network shared folder where the user state migration data is
                 stored.

 AUTO            The deployment scripts store the user state migration data on a local hard disk if
                 space is available. Otherwise, the user state migration data is saved to a network
                 location, which is specified in the UDShare and UDDir properties.

 NETWORK         The user state migration data is stored in the location designated by the UDShare
                 and UDDir properties.

 NONE            The user state migration data is not saved.

                                                                                     ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSInstall=YES ScanStateArgs=/v:5 /o /c
 LoadStateArgs=/v:5 /c /lac DoCapture=YES BackupShare=\\NYC-AM-FIL-01\Backup$
 BackupDir=%OSDComputerName% UserDataLocation=NETWORK DeployRoot=\\NYC-AM-FIL-
 01\Distribution$ ResourceRoot=\\NYC-AM-FIL-01\Resource$ UDShare=\\NYC-AM-FIL-01\MigData$
 UDDir=%OSDComputerName%

UserDomain
The domain in which a user's credentials (specified in the UserID property) reside.

  ７ Note

  For a completely automated LTI deployment, provide this property in both
  CustomSettings.ini and BootStrap.ini. However, note that storing the user
  credentials in these files stores the credentials in clear text and therefore is not
  secure.

                                                                                     ﾉ   Expand table

 Component               Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini           ✅                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini      ✅                 |

<!-- p.1170 -->

 Component               Configured By    |   Scenario                      Property Is Applicable

 MDT DB                  ✅                |   ZTI (Configuration Manager)   ❌

                                                                                    ﾉ   Expand table

 Value           Description

 domain          The name of the domain where the user account credentials reside

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSInstall=YES ScanStateArgs=/v:5 /o /c
 LoadStateArgs=/v:5 /c /lac DeployRoot=\\NYC-AM-FIL-01\Distribution$ ResourceRoot=\\NYC-AM-
 FIL-01\Resource$ UserDataLocation=NONE UserDomain=WOODGROVEBANK UserID=NYC Help Desk Staff
 UserPassword=<complex_password>

UserID
The user credentials for accessing network resources.

  ７ Note

  For a completely automated LTI deployment, provide this property in both
  CustomSettings.ini and BootStrap.ini. However, note that storing the user
  credentials in these files stores the credentials in clear text and therefore is not
  secure.

                                                                                    ﾉ   Expand table

 Component               Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini           ✅                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ✅                |

 MDT DB                  ✅                |   ZTI (Configuration Manager)   ❌

                                                                                    ﾉ   Expand table

<!-- p.1171 -->

 Value       Description

 user_id     The name of the user account credentials used to access the network resources

                                                                                      ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSInstall=YES ScanStateArgs=/v:5 /o /c
 LoadStateArgs=/v:5 /c /lac DeployRoot=\\NYC-AM-FIL-01\Distribution$ ResourceRoot=\\NYC-AM-
 FIL-01\Resource$ UserDataLocation=NONE UserDomain=WOODGROVEBANK UserID=NYC-HelpDesk
 UserPassword=<complex_password>

UserLocale
The user locale to be used with the target operating system. If not specified, the
Deployment Wizard uses the user locale configured in the image being deployed.

                                                                                      ﾉ   Expand table

 Component               Configured By      |   Scenario                       Property Is Applicable

 BootStrap.ini           ❌                  |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini      ✅                  |

 MDT DB                  ✅                  |   ZTI (Configuration Manager)    ✅

                                                                                      ﾉ   Expand table

 Value           Description

 user_locale     The locale for the user on the target computer. The value is specified as a text value
                 (en-us).

                                                                                      ﾉ   Expand table

 Example 1

 [Settings] Priority=Default [Default] UserLocale=en-us KeyboardLocale=0409:00000409

                                                                                      ﾉ   Expand table

<!-- p.1172 -->

 Example 2

 [Settings] Priority=Default [Default] UserLocale=en-us KeyboardLocale=en-us

UserPassword
The password for user credentials specified in the UserID property.

  ７ Note

  For a completely automated LTI deployment, provide this property in both
  CustomSettings.ini and BootStrap.ini. However, note that storing the user
  credentials in these files stores the credentials in clear text and therefore is not
  secure.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ✅                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ❌

                                                                               ﾉ   Expand table

 Value                    Description

 user_password            The password for the user account credentials

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] UserDataLocation=NONE UserDomain=WOODGROVEBANK
 UserID=NYC-HelpDesk UserPassword=<complex_password>

USMTConfigFile
The USMT configuration XML file that should be used when running Scanstate and
Loadstate.

<!-- p.1173 -->

                                                                             ﾉ     Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ❌

                                                                             ﾉ     Expand table

 Value            Description

 USMTConfigFile   The name of the XML configuration file that should be used when running
                  Scanstate.exe and Loadstate.exe

                                                                             ﾉ     Expand table

 Example

 [Settings] Priority=Default [Default] OSInstall=YES ScanStateArgs=/v:5 /o /c
 LoadStateArgs=/v:5 /c /lac DeployRoot=\\NYC-AM-FIL-01\Distribution$ ResourceRoot=\\NYC-AM-
 FIL-01\Resource$ UDShare=\\NYC-AM-FIL-01\MigData$ UDDir=%OSDComputerName% SLShare=\\NYC-AM-
 FIL-01\Logs$ USMTMigFiles1=MigApp.xml USMTMigFiles2=MigUser.xml USMTMigFiles3=MigSys.xml
 USMTMigFiles4=MigCustom.xml USMTConfigFile=USMTConfig.xml UserDataLocation=NONE

USMTLocal
This property specifies whether the USMT user state information is stored locally on the
target computer. This property is primarily used by the ZTIUserState.wsf and
ZTIBackup.wsf scripts to indicate that the Request State Store and Release State Store
task sequence steps for Configuration Manager deployments are skipped. For more
information, see the OSDStateStorePath property.

  ７ Note

  This property should only be used in the circumstance described in the
  OSDStateStorePath property).

                                                                             ﾉ     Expand table

<!-- p.1174 -->

 Component              Configured By   |   Scenario                       Property Is Applicable

 BootStrap.ini          ❌               |   LTI (Stand-alone MDT)          ❌

 CustomSettings.ini     ❌               |

 MDT DB                 ❌               |   ZTI (Configuration Manager)    ✅

                                                                                 ﾉ   Expand table

 Value    Description

 TRUE     The USMT user state information is stored locally on the target computer, and the
          Request State Store and Release State Store task sequence steps are skipped.

 FALSE    The USMT user state information is not stored locally on the target computer, and the
          Request State Store and Release State Store task sequence steps are performed.

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSInstall=YES ScanStateArgs=/v:5 /o /c
 LoadStateArgs=/v:5 /c /lac DeployRoot=\\NYC-AM-FIL-01\Distribution$ ResourceRoot=\\NYC-AM-
 FIL-01\Resource$ UDShare=\\NYC-AM-FIL-01\MigData$ UDDir=%OSDComputerName% SLShare=\\NYC-AM-
 FIL-01\Logs$ USMTLocal=TRUE USMTMigFiles001=MigApp.xml USMTMigFiles002=MigUser.xml
 USMTMigFiles003=MigSys.xml USMTMigFiles004=MigCustom.xml UserDataLocation=NONE

USMTMigFiles
A list of files in XML format that are used by USMT (Scanstate.exe) to identify user state
migration information to be saved. When this property is not specified, the
ZTIUserState.wsf script uses MigApp.xml, MigUser.xml, and MigSys.xml. Otherwise,
ZTIUserState.wsf uses the files explicitly referenced in this property. The USMTMigFiles
property has a numeric suffix (for example, USMTMigFiles001 or USMTMigFiles002).

  ７ Note

  Use this property to specify the XML files to be used by Scanstate.exe instead of
  using the /I parameter in the ScanStateArgs property. This prevents the
  ZTIUserState.wsf script from potentially duplicating the same list of XML files.

  ７ Note

<!-- p.1175 -->

  This property name can be specified using single-digit nomenclature
  (USMTMigFiles1) or triple-digit nomenclature (USMTMigFiles001).

                                                                                    ﾉ    Expand table

 Component               Configured By    |   Scenario                        Property Is Applicable

 BootStrap.ini           ❌                |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini      ✅                |

 MDT DB                  ❌                |   ZTI (Configuration Manager)     ❌

                                                                                    ﾉ    Expand table

 Value           Description

 USMTMigFile     The name of the .xml file to be used as input for Scanstate.exe, on separate lines. If
                 not specified, the default is MigApp.xml, MigUser.xml, and MigSys.xml.

                 Note:

                 If this value is specified, the default files (MigApp.xml, MigUser.xml, and
                 MigSys.xml) must also be added to the list if these files are to be included.

                                                                                    ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] OSInstall=YES ScanStateArgs=/v:5 /o /c
 LoadStateArgs=/v:5 /c /lac DeployRoot=\\NYC-AM-FIL-01\Distribution$ ResourceRoot=\\NYC-AM-
 FIL-01\Resource$ UDShare=\\NYC-AM-FIL-01\MigData$ UDDir=%OSDComputerName% SLShare=\\NYC-AM-
 FIL-01\Logs$ USMTMigFiles001=MigApp.xml USMTMigFiles002=MigUser.xml
 USMTMigFiles003=MigSys.xml USMTMigFiles004=MigCustom.xml UserDataLocation=NONE

USMTOfflineMigration
This property determines whether MDT uses USMT to perform an offline user state
migration. In an offline migration, the capture is performed in Windows PE instead of
the existing operating system.

Offline migration is using USMT is performed for:

     UDI always, regardless of the setting of the USMTOfflineMigration property

<!-- p.1176 -->

    ZTI only for the MDT Refresh Computer deployment scenario and only when the
    USMTOfflineMigration property is set to "TRUE"

        ７ Note

        You cannot perform USMT offline user state migration in the MDT New
        Computer deployment scenario using ZTI.

    LTI for the:

        1. MDT New Computer deployment scenario using the Move Data and Settings
            wizard page in the Deployment Wizard

        2. MDT Refresh Computer deployment scenario and only when the
            USMTOfflineMigration property is set to "TRUE"

    For more information about using MDT and USMT to perform an offline user state
    migration, see "Configure USMT Offline User State Migration".

                                                                                   ﾉ   Expand table

Component               Configured By     |   Scenario                      Property Is Applicable

BootStrap.ini           ❌                 |   LTI (Stand-alone MDT)         ✅

CustomSettings.ini      ✅                 |

MDT DB                  ❌                 |   ZTI (Configuration Manager)   ✅

                                                                                   ﾉ   Expand table

Value           Description

TRUE            MDT uses USMT to perform an offline user state migration.

Any other       MDT does not perform an offline user state migration. Instead, user state migration
value           is captured in the existing operating system. This is the default value.

                                                                                   ﾉ   Expand table

Example

[Settings] Priority=Default [Default] OSInstall=YES SkipUserData=YES
USMTOfflineMigration=TRUE DoNotFormatAndPartition=YES OSDStateStorePath=\\WDG-MDT-
01\StateStore$

<!-- p.1177 -->

UUID
The Universal Unique Identifier (UUID) stored in the System Management BIOS of the
target computer.

The format for UUID is a 16-byte value using hexadecimal digits in the following format:
12345678-1234-1234-1234-123456789ABC. Use this property to create a subsection
that contains settings targeted to a specific computer.

  ７ Note

  This property is dynamically set by MDT scripts and cannot have its value set in
  CustomSettings.ini or the MDT DB. Treat this property as read only. However, you
  can use this property within CustomSettings.ini or the MDT DB, as shown in the
  following examples, to aid in defining the configuration of the target computer.

                                                                                ﾉ   Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌                |

 MDT DB                 ❌                |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value                Description

 UUID                 The UUID of the target computer

                                                                                ﾉ   Expand table

 Example

 None

ValidateDomainCredentialsUNC
This property is used to specify a UNC path to a network shared folder that is used to
validate the credentials provided for joining the target computer to a domain. The

<!-- p.1178 -->

credentials being validated are specified in the DomainAdmin, DomainAdminDomain,
and DomainAdminPassword properties.

  ７ Note

  Ensure that no other properties in MDT use the server sharing the folder in this
  property. Using a server that is already referenced by other MDT properties could
  result in improper validation of the credentials.

                                                                                     ﾉ   Expand table

 Component             Configured By     |   Scenario                        Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)     ❌

                                                                                     ﾉ   Expand table

 Value           Description

 unc_path        Specifies the fully qualified UNC path to a network shared folder

                                                                                     ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] ValidateDomainCredentialsUNC=\\wdg-fs-01\Source$

VHDCreateDiffVHD
This property is used to specify the name of a differencing VHD (also known as a child
VHD) file. A differencing VHD is similar to a dynamically expanding VHD but contains
only the modified disk blocks of the associated parent VHD. The parent VHD is read
only, so you must modify the differencing VHD. The differencing VHD file is created in
the same folder as the parent VHD file, so only the file name is specified in this property.
This property is only valid for the MDT New Computer deployment scenario.

  ７ Note

<!-- p.1179 -->

  All parent VHD files created by MDT are stored in the VHD folder in the root of the
  parent drive.

This property is commonly set using a task sequence step created using the Create
Virtual Hard Disk (VHD) task sequence type. You can override the value the Create
Virtual Hard Disk (VHD) task sequence step sets by configuring this property in
CustomSettings.ini.

  ７ Note

  To configure this property in CustomSettings.ini, you must add this property to the
  Properties line in CustomSettings.ini.

For related properties that are used with VHD files, see:

     VHDCreateFileName

     VHDCreateSizeMax

     VHDCreateSource

     VHDCreateType

     VHDDisks

     VHDInputVariable

     VHDOutputVariable

     VHDTargetDisk

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ❌               |   ZTI (Configuration Manager)   ❌

                                                                             ﾉ   Expand table

<!-- p.1180 -->

 Value      Description

 filename   Specifies the name of the differencing VHD file, which is located in the same folder as
            the parent VHD file

            The differencing VHD file cannot have the same name as the parent VHD file.

 RANDOM     Automatically generates a random name for the differencing VHD file, which is
            located in the same folder as the parent VHD file

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] VHDCreateDiffVHD=Win7Diff_C.vhd
 VHDInputVariable=VHDTargetDisk

VHDCreateFileName
This property is used to specify the name of a VHD file. The type of VHD file is based on
the value of the VHDCreateType property. The property only includes the file name, not
the path to the file name, and is valid only for the MDT New Computer deployment
scenario.

  ７ Note

  The VHD files created by MDT are stored in the VHD folder in the root of the parent
  drive.

This property is commonly set using a task sequence step created using the Create
Virtual Hard Disk (VHD) task sequence type. You can override the value the Create
Virtual Hard Disk (VHD) task sequence step sets by configuring this property in
CustomSettings.ini.

  ７ Note

  To configure this property in CustomSettings.ini, you must add this property to the
  Properties line in CustomSettings.ini.

For related properties that are used with VHD files, see:

     VHDCreateDiffVHD

<!-- p.1181 -->

     VHDCreateSizeMax

     VHDCreateSource

     VHDCreateType

     VHDDisks

     VHDInputVariable

     VHDOutputVariable

     VHDTargetDisk

                                                                              ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                |

 MDT DB               ❌                |   ZTI (Configuration Manager)   ❌

                                                                              ﾉ   Expand table

 Value       Description

 file_name   Specifies the name of the VHD file

 RANDOM      Automatically generates a random name for the VHD file, which is located in the VHD
             folder in the root of the parent drive

 Blank       Same a RANDOM

                                                                              ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] VHDCreateSizeMax=130048 VHDCreateType=EXPANDABLE
 VHDCreateFileName=Win7_C.vhd VHDInputVariable=VHDTargetDisk

VHDCreateSizeMax
This property is used to specify the maximum size of a VHD file in megabytes (MB). The
size of the VHD file at creation time is based on the type of VHD file being created. For

<!-- p.1182 -->

more information, see the VHDCreateType property. This property is valid only for the
MDT New Computer deployment scenario.

  ７ Note

  If this property is not specified, the default value for the maximum size of a VHD
  file is 90% of the available disk space on the parent disk.

This property is commonly set using a task sequence step created using the Create
Virtual Hard Disk (VHD) task sequence type. You can override the value that the Create
Virtual Hard Disk (VHD) task sequence step sets by configuring this property in
CustomSettings.ini.

  ７ Note

  To configure this property in CustomSettings.ini, you must add this property to the
  Properties line in CustomSettings.ini.

For related properties that are used with VHD files, see:

     VHDCreateDiffVHD

     VHDCreateFileName

     VHDCreateSource

     VHDCreateType

     VHDDisks

     VHDInputVariable

     VHDOutputVariable

     VHDTargetDisk

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ❌               |   ZTI (Configuration Manager)   ❌

<!-- p.1183 -->

                                                                               ﾉ   Expand table

 Value    Description

 size     The maximum size of the VHD file specified in MB. For example, 130,048 MB equals 127
          GB. The default value is 90% of the available disk space on the parent disk.

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] VHDCreateSizeMax=130048 VHDCreateType=FIXED
 VHDCreateFileName=Win7_C.vhd VHDInputVariable=VHDTargetDisk

VHDCreateSource
This property is used to specify the name of a VHD file that is used as a template
(source) for creating a new VHD file. You can specify the file name using a UNC path,
local path, relative path, or just the file name. If just the file name is specified, then MDT
attempts to find the VHD file on the target computer. This property is valid only for the
MDT New Computer deployment scenario.

This property is commonly set using a task sequence step created using the Create
Virtual Hard Disk (VHD) task sequence type. You can override the value that the
**Create Virtual Hard Disk (VHD)**task sequence step sets by configuring this property
in CustomSettings.ini.

  ７ Note

  To configure this property in CustomSettings.ini, you must add this property to the
  Properties line in CustomSettings.ini.

For related properties that are used with VHD files, see:

        VHDCreateDiffVHD

        VHDCreateFileName

        VHDCreateSizeMax

        VHDCreateType

        VHDDisks

<!-- p.1184 -->

     VHDInputVariable

     VHDOutputVariable

     VHDTargetDisk

                                                                                    ﾉ   Expand table

 Component             Configured By     |   Scenario                        Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ❌                 |   ZTI (Configuration Manager)     ❌

                                                                                    ﾉ   Expand table

 Value   Description

 name    The file name, which can be specified using a UNC path, local path, relative path, or just
         the file name. If just the file name is specified, then MDT attempts to find the VHD file on
         the target computer.

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] VHDCreateSizeMax=130048 VHDCreateSource=\\wdg-mdt-
 01\vhds\win7_template.vhd VHDCreateType=FIXED VHDCreateFileName=Win7_C.vhd
 VHDInputVariable=VHDTargetDisk

VHDCreateType
This property is used to specify the type of VHD file that is specified in the
VHDCreateFileName property and can be one of the following VHD file types:

     Fixed VHD file. For this VHD type, the size of the VHD specified at creation is
     allocated and does not change automatically after creation. For example, if you
     create a 24-gigabyte (GB) fixed VHD file, the file will be approximately 24 GB in size
     (with some space used for the internal VHD structure) regardless of how much
     information is stored in the VHD file.

     Dynamically expanding VHD file. For this VHD type, only a small percentage of
     the size of the VHD specified at creation time is allocated. Then, the VHD file

<!-- p.1185 -->

     continues to grow as more and more information is stored in it. However, the VHD
     file cannot grow beyond the size specified at creation. For example, if you create a
     24 GB dynamically expanding VHD, it will be small at creation. However, as
     information is stored in the VHD file, the file will continue to grow but never
     exceed the maximum size of 24 GB.

     This property is only valid for the MDT New Computer deployment scenario.

  ７ Note

  The maximum size of the VHD file is specified in the VHDCreateSizeMax property.

This property is commonly set using a task sequence step created using the Create
Virtual Hard Disk (VHD) task sequence type. You can override the value that the Create
Virtual Hard Disk (VHD) task sequence step sets by configuring this property in
CustomSettings.ini.

  ７ Note

  To configure this property in CustomSettings.ini, you must add this property to the
  Properties line in CustomSettings.ini.

For related properties that are used with VHD files, see:

     VHDCreateDiffVHD

     VHDCreateFileName

     VHDCreateSizeMax

     VHDCreateSource

     VHDDisks

     VHDInputVariable

     VHDOutputVariable

     VHDTargetDisk

                                                                          ﾉ   Expand table

<!-- p.1186 -->

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ❌                 |   ZTI (Configuration Manager)   ❌

                                                                               ﾉ   Expand table

 Value                    Description

 EXPANDABLE               Creates a fixed VHD file

 FIXED                    Creates a dynamically expanding VHD file

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] VHDCreateSizeMax=130048 VHDCreateType=EXPANDABLE
 VHDCreateFileName=Win7_C.vhd VHDInputVariable=VHDTargetDisk

VHDDisks
This property contains a list of the physical drive numbers assigned to VHD files
separated by spaces. Each time a VHD file is created, MDT adds the disk index of the
newly created disk to this property using the Index property of the Win32_DiskDrive
WMI class.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

This property is commonly set using a task sequence step created using the Create
Virtual Hard Disk (VHD) task sequence type. You can override the value that the Create
Virtual Hard Disk (VHD) task sequence step sets by configuring this property in
CustomSettings.ini.

  ７ Note

<!-- p.1187 -->

  To configure this property in CustomSettings.ini, you must add this property to the
  Properties line in CustomSettings.ini.

For related properties that are used with VHD files, see:

     VHDCreateDiffVHD

     VHDCreateFileName

     VHDCreateSizeMax

     VHDCreateSource

     VHDCreateType

     VHDInputVariable

     VHDOutputVariable

     VHDTargetDisk

                                                                                   ﾉ   Expand table

 Component             Configured By      |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                  |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                  |

 MDT DB                ❌                  |   ZTI (Configuration Manager)    ❌

                                                                                   ﾉ   Expand table

 Value                Description

 index1 index2        A list of the physical drive numbers assigned to the VHD files separated by
 index3               spaces—for example, 1 2 5.

                                                                                   ﾉ   Expand table

 Example

 None

VHDInputVariable

<!-- p.1188 -->

This property contains a variable that contains the drive on the target computer where
the VHD files will be created. MDT creates the VHD files in the VHD folder in the root of
this drive.

  ７ Note

  If this property is omitted, MDT attempts to create the VHD files in the VHD folder
  in the root of the first system drive.

This property is commonly set using a task sequence step created using the Create
Virtual Hard Disk (VHD) task sequence type. You can override the value that the Create
Virtual Hard Disk (VHD) task sequence step sets by configuring this property in
CustomSettings.ini.

  ７ Note

  To configure this property in CustomSettings.ini, you must add this property to the
  Properties line in CustomSettings.ini.

For related properties that are used with VHD files, see:

      VHDCreateDiffVHD

      VHDCreateFileName

      VHDCreateSizeMax

      VHDCreateSource

      VHDCreateType

      VHDDrives

      VHDOutputVariable

      VHDTargetDisk

                                                                         ﾉ   Expand table

 Component            Configured By   |    Scenario                Property Is Applicable

 BootStrap.ini        ❌               |    LTI (Stand-alone MDT)   ✅

 CustomSettings.ini   ✅               |

<!-- p.1189 -->

 Component             Configured By     |   Scenario                        Property Is Applicable

 MDT DB                ❌                 |   ZTI (Configuration Manager)     ❌

                                                                                   ﾉ   Expand table

 Value      Description

 variable   Variable that contains the drive letter on the target computer where the VHD files will
            be created. MDT creates the VHD files in the VHD folder in the root of this drive. For
            example, if this property has a value of VHDTargetDisk, the VHDTargetDisk property
            contains the drive letter (such as H).

                                                                                   ﾉ   Expand table

 Example

 VHDCreateSizeMax=130048 VHDCreateType=EXPANDABLE VHDCreateFileName=Win7_C.vhd
 VHDInputVariable=VHDTargetDisk

VHDOutputVariable
This property contains a variable that contains the physical drive number that was
assigned to the newly created VHD file. Each time a VHD file is created, MDT sets this
property to the disk index of the newly created disk using the Index property of the
Win32_DiskDrive WMI class.

This property is commonly set using a task sequence step created using the Create
Virtual Hard Disk (VHD) task sequence type. You can override the value that the Create
Virtual Hard Disk (VHD) task sequence step sets by configuring this property in
CustomSettings.ini.

  ７ Note

  To configure this property in CustomSettings.ini, you must add this property to the
  Properties line in CustomSettings.ini.

For related properties that are used with VHD files, see:

     VHDCreateDiffVHD

     VHDCreateFileName

<!-- p.1190 -->

     VHDCreateSizeMax

     VHDCreateSource

     VHDCreateType

     VHDDisks

     VHDInputVariable

     VHDTargetDisk

                                                                                  ﾉ   Expand table

 Component            Configured By      |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                  |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅                  |

 MDT DB               ❌                  |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ   Expand table

 Value      Description

 Variable   Variable will contains the physical drive number assigned to the newly created VHD file.
            For example, if this property has a value of OSDDiskIndex, the OSDDiskIndex property
            will contain the physical drive number assigned to the newly created VHD file (such as
            4).

                                                                                  ﾉ   Expand table

 Example

 None

VHDTargetDisk
Specifies the drive on the target computer where the VHD is to be created. This property
is later referenced in the VHDInputVariable property.

  ７ Note

<!-- p.1191 -->

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

For related properties that are used with VHD files, see:

        VHDCreateDiffVHD

        VHDCreateFileName

        VHDCreateSizeMax

        VHDCreateSource

        VHDCreateType

        VHDDisks

        VHDInputVariable

        VHDOutputVariable

                                                                                 ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌                 |

 MDT DB                 ❌                 |   ZTI (Configuration Manager)   ❌

                                                                                 ﾉ   Expand table

 Value           Description

 Disk            Specifies the drive where the VHD is to be created

                                                                                 ﾉ   Expand table

 Example

 None

VMHost

<!-- p.1192 -->

Specifies the name of the Hyper-V host running the VM where MDT is running. This
property is available only when the Hyper-V Integration Components are installed and
running.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

Table 4 lists the Windows operating systems that MDT supports and their corresponding
Hyper-V Integration Components support.

Table 4. Windows Operating Systems and
Hyper-V Integration Components Support
                                                                                 ﾉ    Expand table

 Operating system          Hyper-V Integration Components

 Windows PE                Integration Components are unavailable.

 Windows 7                 Available by default in Enterprise, Ultimate, and Professional editions.

 Windows Server 2008 R2    Available by default in all editions.

                                                                                 ﾉ    Expand table

 Component            Configured By    |   Scenario                        Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini   ❌                |

 MDT DB               ❌                |   ZTI (Configuration Manager)     ✅

                                                                                 ﾉ    Expand table

 Value     Description

 Name      The name of the Hyper-V host running the VM where MDT is running

                                                                                 ﾉ    Expand table

<!-- p.1193 -->

 Example

 None

VMName
Specifies the name of the VM where MDT is running. This property is only available
when the Hyper-V Integration Components are installed and running.

Table 5 lists the Windows operating systems supported by MDT and their corresponding
Hyper-V Integration Components support.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

Table 5. Windows Operating Systems and
Hyper-V Integration Components Support
                                                                                 ﾉ    Expand table

 Operating system          Hyper-V Integration Components

 Windows PE                Integration Components are unavailable.

 Windows 7                 Available by default in Enterprise, Ultimate, and Professional editions.

 Windows Server 2008 R2    Available by default in all editions.

                                                                                 ﾉ    Expand table

 Component            Configured By    |   Scenario                        Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini   ❌                |

 MDT DB               ❌                |   ZTI (Configuration Manager)     ✅

                                                                                 ﾉ    Expand table

<!-- p.1194 -->

 Value           Description

 name            The name of the VM where MDT is running

                                                                                    ﾉ   Expand table

 Example

 None

VMPlatform
Specifies specific information about the virtualization environment for the target
computer when the target computer is a VM. The VM platform is determined by using
WMI.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                    ﾉ   Expand table

 Component            Configured By          |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                      |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ❌                      |

 MDT DB               ❌                      |   ZTI (Configuration Manager)   ✅

                                                                                    ﾉ   Expand table

 Value                         Description

 Hyper-V                       Hyper-V

 VirtualBox                    Virtual Box

 VMware                        VMware virtualization platform

 Xen                           Citrix Xen Server

<!-- p.1195 -->

                                                                                    ﾉ   Expand table

 Example

 None

VRefresh
The vertical refresh rate for the monitor on the target computer. The vertical refresh rate
is specified in Hertz. In the example, the value 60 indicates that the vertical refresh rate
of the monitor is 60 Hz. This value is inserted into the appropriate configuration settings
in Unattend.xml.

  ７ Note

  The default values (in the Unattend.xml template file) are 1,024 pixels horizontal
  resolution, 768 pixels vertical resolution, 32-bit color depth, and 60 Hz vertical
  refresh rate.

                                                                                    ﾉ   Expand table

 Component              Configured By     |   Scenario                        Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)     ✅

                                                                                    ﾉ   Expand table

 Value             Description

 refresh_rate      The vertical refresh rate for the monitor on the target computer in Hertz

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] BitsPerPel=32 VRefresh=60 XResolution=1024
 YResolution=768

VSSMaxSize

<!-- p.1196 -->

This property is used to pass a value to the maxsize parameter of the vssadmin resize
shadowstorage command in the Vssadmin command. The maxsize parameter is used
to specify the maximum amount of space on the target volume that can be used for
storing shadow copies. For more information on the maxsize parameter, see Vssadmin
resize shadowstorage      .

                                                                                    ﾉ    Expand table

 Component            Configured By      |   Scenario                         Property Is Applicable

 BootStrap.ini        ❌                  |   LTI (Stand-alone MDT)            ✅

 CustomSettings.ini   ✅                  |

 MDT DB               ✅                  |   ZTI (Configuration Manager)      ✅

                                                                                    ﾉ    Expand table

 Value           Description

 maxsize_value   Specifies the maximum amount of space that can be used for storing shadow
                 copies. The value can be specified in bytes or as a percentage of the target
                 volume.

                 To specify the value:

                 - In bytes, the value must be 300 MB or greater and accept the following suffixes:
                 KB, MB, GB, TB, PB and EB. You can also use B, K, M, G, T, P, and E as suffixes—for
                 example:

                 VSSMaxSize=60G

                 - As a percentage, use the % character as the suffix to the numeric value—for
                 example:

                 VSSMaxSize=20%

                 Note:

                 If a suffix is not supplied, the default suffix is bytes. For example, VSSMaxSize=1024
                 indicates that the VSSMaxSize will be set to 1,024 bytes.

                 If the value is set to UNBOUNDED, then there is no limit placed on the amount of
                 storage space that can be used—for example:

                 VSSMaxSize=UNBOUNDED

<!-- p.1197 -->

                                                                             ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] VSSMaxSize=25%

WDSServer
The computer running Windows Deployment Services that is used for installing
Windows Deployment Services images. The default value is the server running Windows
Deployment Services from which the image was initiated.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ❌               |

 MDT DB               ❌               |   ZTI (Configuration Manager)   ❌

                                                                             ﾉ   Expand table

 Value           Description

 WDS_server      The name of the computer running Windows Deployment Services

                                                                             ﾉ   Expand table

 Example

 None

WindowsSource
MDT uses this property to set the location of the sources\sxs folder in a network shared
folder that contains the operating system source files. This property is used when:

<!-- p.1198 -->

     MDT is running a custom task sequence or deploying a custom image

     MDT is installing roles or features in Windows 8 and Windows Server 2012

     The computer does not have access to the Internet

     When the situation described in the bulleted list above occurs, MDT may be unable
     to find the operating system source files locally, and the installation will attempt to
     download the files from the Internet. Because the computer does not have Internet
     access, the process will fail. Setting this property to the appropriate value helps
     prevent this problem from occurring.

                                                                                 ﾉ   Expand table

 Component               Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ✅               |

 MDT DB                  ❌               |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value           Description

 folder_unc      A UNC path to the Sources\sxs folder for the operating system being deployed.

                 Note:

                 The UNC path must include the Sources\sxs folder.

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] WindowsSource=%DeployRoot%\Operating Systems\Windows
 8\Sources\sxs

WipeDisk
Specifies whether the disk should be wiped. If WipeDisk is TRUE, the ZTIWipeDisk.wsf
script will clean the disk using the Format command. The Format command is not the
most "secure" way of wiping the disk.

<!-- p.1199 -->

Securely wiping the disk should be done so in a manner that follows the U.S.
Department of Defense standard 5220.22-M, which states, "To clear magnetic disks,
overwrite all locations three times (first time with a character, second time with its
complement, and the third time with a random character)."

When MDT wipes the disk, it uses the Format command with the /P:3 switch, which
instructs Format to zero every sector on the volume and to perform the operation three
times. There is no way to tell the Format command to use a particular character or a
random character.

  ７ Note

  If the disk must be securely wiped, a non-Microsoft secure disk wipe tool should be
  added to the task sequence using the Run Command Line task sequence step.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                   ﾉ   Expand table

 Component              Configured By       |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                   |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                   |

 MDT DB                 ✅                   |   ZTI (Configuration Manager)   ✅

                                                                                   ﾉ   Expand table

 Value    Description

 TRUE     If WipeDisk is set to TRUE, the Win32_DiskPartition at DiskIndex 0 and Index 0 will be
          formatted.

 FALSE    The disk will not be formatted.

                                                                                   ﾉ   Expand table

<!-- p.1200 -->

 Example

 [Settings] Priority=Default [Default] WipeDisk=TRUE

WizardSelectionProfile
Profile name used by the wizard for filtering the display of various items.

                                                                                  ﾉ   Expand table

 Component            Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ   Expand table

 Value           Description

 profile_name    Profile name used by the wizard for filtering the display of various items

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] WizardSelectionProfile=SelectTaskSequenceOnly

WSUSServer
This is the name of the Windows Server Update Services (WSUS) server that the target
computer should use when scanning for, downloading, and installing updates.

For more information about what script uses this property, see ZTIWindowsUpdate.wsf.

                                                                                  ﾉ   Expand table

 Component            Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅                 |
