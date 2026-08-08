---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 921-960"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0921-0960
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0921-0960
family: sccm
documentKind: "doc"
abstract: "Properties ﾉ Expand table Name Description Type This read-only type is set to Recover from Domain Join Failure. Settings ﾉ Expand table Name Description Auto The task sequence step will attempt to join the target computer to a domain. recover Manual If the target computer fails"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 921-960

<!-- p.921 -->

Properties

                                                                                     ﾉ   Expand table

 Name          Description

 Type          This read-only type is set to Recover from Domain Join Failure.

Settings

                                                                                     ﾉ   Expand table

 Name            Description

 Auto            The task sequence step will attempt to join the target computer to a domain.
 recover

 Manual          If the target computer fails to join a domain, the task sequence step will cause the
 recover         task sequencer to pause, allowing the user attempts to join the target computer to a
                 domain.

 No recover      If the target computer is not able to join a domain, the task sequence fails, stopping
                 the task sequence.

Restart computer
This task sequence step restarts the target computer. Following is a brief listing of the
settings that show how this step was originally configured in one of the MDT task
sequence templates.

The default configuration of the Restart computer task sequence step is:

Properties

                                                                                     ﾉ   Expand table

 Name                                         Value

 Type                                         Restart computer

 Name                                         Restart computer

 Description                                  Not specified

<!-- p.922 -->

Settings

                                                                         ﾉ   Expand table

 Name                                           Value

 None                                           None

Options

                                                                         ﾉ   Expand table

 Name                                                   Value

 Disable this step                                      Not selected

 Success codes                                          0 3010

 Continue on error                                      Not selected

 Conditional qualifier                                  Not specified

Restore Groups
This task sequence step restores the previously captured group membership of local
groups on the target computer. Following is a brief listing of the settings that show how
this step was originally configured in one of the MDT task sequence templates.

For more information about what script accomplishes this task and what properties are
used, see ZTIGroups.wsf.

The default configuration of the Restore Groups task sequence step is:

Properties

                                                                         ﾉ   Expand table

 Name                               Value

 Type                               Run Command Line

 Name                               Restore Groups

 Description                        Not specified

<!-- p.923 -->

Settings

                                                                               ﾉ   Expand table

 Name                                        Value

 Command line                                cscript.exe "%SCRIPTROOT%\ZTIGroups.wsf" /restore

 Start in                                    Not specified

 Run this step as the following account      Not specified

Options

                                                                               ﾉ   Expand table

 Name                                Value

 Disable this step                   Not selected

 Success codes                       0 3010

 Continue on error                   Not selected

 Conditional qualifier               If all conditions are true:

                                     - DoCapture does not equal YES

                                     - DoCapture does not equal PREPARE

Restore User State
This task sequence step restores previously captured user state to the target computer.
Following is a brief listing of the settings that show how this step was originally
configured in one of the MDT task sequence templates.

For more information about what script accomplishes this task and what properties are
used, see [ZTIUserState.wsf]((scripts.md#ztiuserstatewsf).

For more information about this step type, see Restore User State.

The default configuration of the Restore User State task sequence step is:

Properties

<!-- p.924 -->

                                                                               ﾉ   Expand table

 Name                                     Value

 Type                                     Run Command Line

 Name                                     Restore User State

 Description                              Not specified

Settings

                                                                               ﾉ   Expand table

 Name                                       Value

 Command Line                               cscript.exe "%SCRIPTROOT%\ZTIUserState.wsf" /restore

 Start in                                   Not specified

 Run this step as the following account     Not specified

Options

                                                                               ﾉ   Expand table

 Name                               Value

 Disable this step                  Not selected

 Success codes                      0 3010

 Continue on error                  Not selected

 Conditional qualifier              If all conditions are true:

                                    - If DoCapture does not equal YES

                                    - If DoCapture does not equal PREPARE

Set Image Build
This task sequence step sets the ImageBuild property to the value contained in
OSCurrentVersion. Following is a brief listing of the settings that show how this step
was originally configured in one of the MDT task sequence templates.

<!-- p.925 -->

The default configuration of the Set Image Build task sequence step is:

Properties

                                                                            ﾉ   Expand table

 Name                          Value

 Type                          Set Task Sequence Variable

 Name                          Set Image Build

 Description                   Not specified

Settings

                                                                            ﾉ   Expand table

 Name                                            Value

 Task Sequence Variable                          ImageBuild

 Value                                           %OSCurrentVersion%

Options

                                                                            ﾉ   Expand table

 Name                                                       Value

 Disable this step                                          Not selected

 Success codes                                              0 3010

 Continue on error                                          Not selected

 Conditional qualifier                                      Not specified

Set Image Flags
This task sequence step sets the ImageFlags property to the value contained in OSSKU.
Following is a brief listing of the settings that show how this step was originally
configured in one of the MDT task sequence templates.

<!-- p.926 -->

The default configuration of the Set Image Flags task sequence step is:

Properties

                                                                                 ﾉ   Expand table

 Name                          Value

 Type                          Set Task Sequence Variable

 Name                          Set Image Flags

 Description                   Not specified

Settings

                                                                                 ﾉ   Expand table

 Name                                                               Value

 Task Sequence Variable                                             ImageFlags

 Value                                                              %OSSKU%

Options

                                                                                 ﾉ   Expand table

 Name                                                       Value

 Disable this step                                          Not selected

 Success codes                                              0 3010

 Continue on error                                          Not selected

 Conditional qualifier                                      Not specified

Tattoo
This task sequence step tattoos the target computer with identification and version
information. Following is a brief listing of the settings that show how this step was
originally configured in one of the MDT task sequence templates.

<!-- p.927 -->

For more information about what script accomplishes this task and what properties are
used, see ZTITatoo.wsf.

The default configuration of the Tattoo task sequence step is:

Properties

                                                                                ﾉ   Expand table

 Name                                     Value

 Type                                     Run Command Line

 Name                                     Tattoo

 Description                              Not specified

Settings

                                                                                ﾉ   Expand table

 Name                                              Value

 Command line                                      cscript.exe "%SCRIPTROOT%\ZTITatoo.wsf"

 Start in                                          Not specified

 Run this step as the following account            Not specified

Options

                                                                                ﾉ   Expand table

 Name                                                        Value

 Disable this step                                           Not selected

 Success codes                                               0 3010

 Continue on error                                           Not selected

 Conditional qualifier                                       Not specified

Validate

<!-- p.928 -->

This task sequence step validates that the target computer meets the specified
deployment prerequisite conditions. Following is a brief listing of the settings that show
how this step was originally configured in one of the MDT task sequence templates.

For more information about what script accomplishes this task and what properties are
used, see ZTIValidate.wsf.

The default configuration of the Validate task sequence step is:

Properties

                                                                               ﾉ   Expand table

 Name                                          Value

 Type                                          Validate

 Name                                          Validate

 Description                                   Not specified

Settings

                                                                               ﾉ   Expand table

 Name                          Value

 Ensure minimum memory         Selected. The value selector is set to 768.
 (MB)

 Ensure minimum processor      Selected. The value selector is set to 800.
 speed (MHz)

 Ensure specified image size   Not selected.
 will fit (MB)

 Ensure current operating      Selected. The value selector is set to Server or Client, depending
 system to be refreshed        on the template used to create the task sequence.

Options

                                                                               ﾉ   Expand table

<!-- p.929 -->

 Name                                                        Value

 Disable this step                                           Not selected

 Success codes                                               0 3010

 Continue on error                                           Not selected

 Conditional qualifier                                       Not specified

Windows Update (Pre-Application Installation)
This task sequence step installs updates to the target computer prior to the installation
of applications. Following is a brief listing of the settings that show how this step was
originally configured in one of the MDT task sequence templates.

For more information about what script accomplishes this task and what properties are
used, see ZTIWindowsUpdate.wsf.

The default configuration of the Windows Update (Pre-Application Installation) task
sequence step is:

Properties

                                                                               ﾉ   Expand table

 Name                    Value

 Type                    Run Command Line

 Name                    Windows Update (Pre-Application Installation)

 Description             Not specified

Settings

                                                                               ﾉ   Expand table

 Name                                        Value

 Command line                                 cscript.exe "%SCRIPTROOT%\ZTIWindowsUpdate.wsf"

 Start in                                    Not specified

 Run this step as the following account      Not specified

<!-- p.930 -->

Options

                                                                                 ﾉ   Expand table

 Name                                                        Value

 Disable this step                                           Not selected

 Success codes                                               0 3010

 Continue on error                                           Not selected

 Conditional qualifier                                       Not specified

Windows Update (Post-Application Installation)
This task sequence step is the same as the Windows Update (Pre-Application
Installation) task sequence step.

Wipe Disk
This task sequence step wipes all information from the disk using the Format command.

For more information about what script accomplishes this task and what properties are
used, see ZTIWipeDisk.wsf.

The default configuration of the Wipe Disk task sequence step is:

Properties

                                                                                 ﾉ   Expand table

 Name                Value

 Type                Run Command Line

 Name                Wipe Disk

 Description         This will only run if WipeDisk=TRUE in CustomSettings.ini

Settings

                                                                                 ﾉ   Expand table

<!-- p.931 -->

 Name                                     Value

 Command line                             cscript.exe "%SCRIPTROOT%\ZTIWipeDisk.wsf"

 Start in                                 Not specified

 Run this step as the following account   Not specified

Options

                                                                          ﾉ   Expand table

 Name                                                     Value

 Disable this step                                        Not selected

 Success codes                                            0 3010

 Continue on error                                        Not selected

 Conditional qualifier                                    Not specified

Related articles
      Properties.
      Scripts.
      Support Files.
      Utilities.
      MDT Windows PowerShell Cmdlets.
      Tables and Views in the MDT DB.
      Windows 7 Feature Dependency Reference.
      UDI Reference.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.932 -->

Properties
Article • 02/12/2024

The scripts used in Lite Touch Installation (LTI) and ZTI reference properties to determine
the process steps and configuration settings used during the deployment process. The
scripts create some of these properties automatically. Other properties must be
configured in the CustomSettings.ini file. Some of these properties are:

      Specific to ZTI only

      Specific to LTI only

      For use in both ZTI and LTI

      Use this reference to help determine the correct properties to configure and the
      valid values to include for each property.

      For each property the following information is provided:

      Description.Provides a description of the purpose of the property and any
      pertinent information regarding the customization of the property.

        ７ Note

        Unless explicitly specified for ZTI or LTI only, a property is valid for both ZTI
        and LTI.

      Value and Description.Indicates the valid values to be specified for the property
      and a brief description of what each value means. (Values in italics indicate that a
      value is substituted—for example the value user1, user2 indicates that user1 and
      user2 would be replaced with the actual name of user accounts.)

      Example.Provides an example of a property use as it might appear in the .ini files.

      For more information about these and other task sequence properties that might
      be referenced while performing a ZTI deployment, see Operating System
      Deployment Task Sequence Variables.

      The deployment scripts generally require values to be specified in upper case so
      that they are properly read. Therefore, when specifying property values, use
      uppercase letters.

<!-- p.933 -->

Property Definition
The following sections describe the properties that are available for LTI and ZTI
deployments in MDT.

   Tip

  The properties are sorted in alphabetical order.

_SMSTSOrgName
Customizes the Task Sequencer engine's display banner

                                                                                ﾉ     Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ✅                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ     Expand table

 Value     Description

 name      The name that will be used in the Task Sequencer engine's display banner

                                                                                ﾉ     Expand table

 Example

 [Settings] Priority=Default [Default] _SMSTSOrgName=Woodgrove Bank

ADDSLogPath
Fully qualified, non-UNC directory on a hard disk on the local computer to host the AD
DS log files. If the directory exists it must be empty. If it does not exist, it will be created.

                                                                                ﾉ     Expand table

<!-- p.934 -->

 Component             Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value      Description

 log_path   Fully qualified, non-UNC directory on a hard disk on the local computer to host the AD
            DS log files

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] ADDSLogPath=%DestinationLogicalDrive%\Windows\NTDS

ADDSPassword
Account credentials that can be used when promoting the server to a domain controller.

                                                                                ﾉ   Expand table

 Component             Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value           Description

 password        Account credentials that can be used for the promotion operation

                                                                                ﾉ   Expand table

<!-- p.935 -->

 Example

 [Settings] Priority=Default [Default] ADDSUserName=Administrator
 ADDSUserDomain=WoodGroveBank ADDSPassword=<complex_password>

ADDSUserDomain
This is the domain the account specified by ADDSUserName should be taken from. If
the operation is to create a new forest or to become a member server from a backup
domain controller upgrade there is no default. If the operation is to create a new tree,
the default is the DNS name of the forest the computer is currently joined to. If the
operation is to create a new child domain or a replica then the default is the DNS name
of the domain the computer is joined to. If the operation is to demote the computer and
the computer is a domain controller in a child domain, the default is the DNS name of
the parent domains. If the operation is to demote the computer, and the computer is a
domain controller of a tree root domain, the default is the DNS name of the forest.

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ✅

                                                                             ﾉ   Expand table

 Value           Description

 domain          Domain the UserName account should be taken from

                                                                             ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] ADDSUserName=Administrator
 ADDSUserDomain=WoodGroveBank ADDSPassword=<complex_password>

ADDSUserName
Account credentials that will be used when promoting the server to a domain controller.

<!-- p.936 -->

                                                                                 ﾉ    Expand table

 Component               Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ✅               |

 MDT DB                  ✅               |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ    Expand table

 Value            Description

 user_name        Account credentials that will be used for the promotion operation

                                                                                 ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] ADDSUserName=Administrator
 ADDSUserDomain=WoodGroveBank ADDSPassword=complex_password

Administrators
A list of user accounts and domain groups that will be added to the local Administrator
group on the target computer. The Administrators property is a list of text values that
can be any non-blank value. The Administrators property has a numeric suffix (for
example, Administrators001 or Administrators002).

                                                                                 ﾉ    Expand table

 Component               Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ✅               |

 MDT DB                  ✅               |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ    Expand table

 Value     Description

 name      The name of a user or group that is to be added to the local Administrator group

<!-- p.937 -->

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] Administrators001=WOODGROVEBANK\NYC Help Desk Staff
 Administrators002=WOODGROVEBANK\North America East Help Desk Staff
 PowerUsers001=WOODGROVEBANK\User01 PowerUsers002=WOODGROVEBANK\User02

AdminPassword
Defines the password that will be assigned to the local Administrator user account on
the target computer. If not specified, the pre-deployment password of the Administrator
user account will be used.

                                                                                  ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                  ﾉ   Expand table

 Value                Description

 admin_password       The password that is to be assigned to the Administrator user account on the
                      target computer

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] Administrators001=WOODGROVEBANK\NYC Help Desk Staff
 AdminPassword=<admin_password>

Applications
A list of application GUIDs that should be installed on the target computer. These
applications are specified on the Applications node in Deployment Workbench. These
GUIDs are stored in the Applications.xml file. The Applications property is a list of text

<!-- p.938 -->

values that can be any non-blank value. The Applications property has a numeric suffix
(for example, Applications001 or Applications002).

                                                                                 ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)   ❌

                                                                                 ﾉ   Expand table

 Value                Description

 application_guid     The GUID is specified by Deployment Workbench for the application to be
                      deployed to the target computer. The GUID corresponds to the application
                      GUID stored in the Applications.xml file.

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] Applications001={1D7DF331-47B7-472C-87B3-442597EC2F7D}
 Applications002={9d2b8999-5e4d-4f3d-bb05-edaaf4fe5628}

ApplicationSuccessCodes
A space-delimited list of error codes used by the ZTIApplications script that determine
the successful installation of applications.

  ７ Note

  This property is only applicable to the Install Application task sequence step type
  and when Install multiple applications is selected.

                                                                                 ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

<!-- p.939 -->

 Component              Configured By     |   Scenario                       Property Is Applicable

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                   ﾉ   Expand table

 Value           Description

 error_codes     The error codes that determine when applications have been successfully installed.
                 Default values are 0 and 3010.

                                                                                   ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] ApplicationSuccessCodes=0 3010

ApplyGPOPack
This property is used to determine whether the Apply Local GPO Package task
sequence step is performed.

  ７ Note

  The default value for this property always performs the Apply Local GPO Package
  task sequence step. You must explicitly provide a value of "NO" to override this
  behavior..

                                                                                   ﾉ   Expand table

 Component              Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                   ﾉ   Expand table

<!-- p.940 -->

 Value    Description

 YES      The Apply Local GPO Package task sequence step is performed. This is the default value.

 NO       The Apply Local GPO Package task sequence step is not performed.

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] ApplyGPOPack=NO

Architecture
The processor architecture of the processor that is currently running, which is not
necessarily the processor architecture supported by the target computer. For example,
when running a 32-bit-compatible operating system on a 64-bit processor, Architecture
will indicate that the processor architecture is 32 bit.

Use the CapableArchitecture property to identify the actual processor architecture that
the target computer supports.

  ７ Note

  This property is dynamically set by MDT scripts and is not configured in
  CustomSettings.ini. Treat this property as read only. However, you can use this
  property within CustomSettings.ini, as shown in the following examples, to aid in
  defining the configuration of the target computer.

                                                                                ﾉ   Expand table

 Component              Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌               |

 MDT DB                 ❌               |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

<!-- p.941 -->

 Value                Description

 x86                  Processor architecture is 32 bit.

 x64                  Processor architecture is 64 bit.

                                                                                 ﾉ   Expand table

 Example

 None

AreaCode
The area code to be configured for the operating system on the target computer. This
property allows only numeric characters. This value is inserted into the appropriate
configuration settings in Unattend.xml.

                                                                                 ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value           Description

 area_code       The area code where the target computer is to be deployed

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] AreaCode=206 CountryCode=001 Dialing=TONE
 LongDistanceAccess=9

AssetTag

<!-- p.942 -->

The asset tag number associated with the target computer. The format for asset tag
numbers is undefined. Use this property to create a subsection that contains settings
targeted to a specific computer.

  ７ Note

  This property is dynamically set by MDT scripts and cannot have its value set in
  CustomSettings.ini or the MDT DB. Treat this property as read only. However, you
  can use this property within CustomSettings.ini or the MDT DB, as shown in the
  following examples, to aid in defining the configuration of the target computer.

                                                                                 ﾉ   Expand table

 Component            Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ❌                 |

 MDT DB               ❌                 |   ZTI (Configuration Manager)    ✅

                                                                                 ﾉ   Expand table

 Value       Description

 asset_tag   The format of the asset tag is undefined and is determined by the asset tag standard
             of each organization.

                                                                                 ﾉ   Expand table

 Example 1

 [Settings] Priority=Default [Default] OSDComputerName=HP-%AssetTag%

                                                                                 ﾉ   Expand table

 Example 2

 [Settings] Priority=AssetTag, Default [Default] OSInstall=YES [0034034931]
 OSDComputerName=HPD530-1 [0034003233] OSDNEWMACHINENAME=BVMXP

AutoConfigDNS

<!-- p.943 -->

Specifies whether the Active Directory Installation Wizard configures DNS for the new
domain if it detects that the DNS dynamic update protocol is not available.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can properly read it.

                                                                               ﾉ   Expand table

 Component              Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅               |

 MDT DB                 ✅               |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value    Description

 YES      Configures DNS for the new domain if the DNS dynamic update protocol is not available

 NO       Does not configure DNS for the domain

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] AutoConfigDNS=YES

BackupDir
The folder in which backups of the target computer are stored. This folder exists
beneath the UNC path specified in the BackupShare property. If the folder does not
already exist, it will be created automatically.

                                                                               ﾉ   Expand table

 Component              Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌               |   LTI (Stand-alone MDT)         ✅

<!-- p.944 -->

 Component              Configured By     |   Scenario                      Property Is Applicable

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                  ﾉ   Expand table

 Value    Description

 Folder   The name of the folder that exists beneath the shared folder specified in the
          BackupShare property

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DoCapture=YES BackupShare=\\NYC-AM-FIL-01\Backup$
 BackupDir=%OSDComputerName% BackupDrive=C:

BackupDrive
The drive to include in the backup of the target computer. This property defaults to the
drive that contains disk 0 partition 1. It can be also set to ALL.

                                                                                  ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                  ﾉ   Expand table

 Value                      Description

 backup_drive               The drive letter of the drive to back up

 ALL                        Back up all drives on the target computer

                                                                                  ﾉ   Expand table

<!-- p.945 -->

 Example

 [Settings] Priority=Default [Default] DoCapture=YES BackupShare=\\NYC-AM-FIL-01\Backup$
 BackupDir=%OSDComputerName% BackupDrive=C:

BackupFile
Specifies the WIM file that will be used by the ZTIBackup.wsf script. For more
information about what script uses this property, see ZTIBackup.wsf.

                                                                                ﾉ   Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                |

 MDT DB                 ✅                |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value           Description

 BackupDir       The name of the Windows Imaging Format (WIM) file to be used during back up.

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DoCapture=YES BackupShare=\\NYC-AM-FIL-01\Backup$
 BackupDir=%OSDComputerName% BackupFile=%OSDComputerName%.wim

BackupShare
The shared folder in which backups of the target computer are stored.

The credentials used to access this shared folder for:

     LTI are the credentials entered in the Deployment Wizard.

     ZTI are the credentials used by the Configuration Manager Advanced Client
     Network Access account.

     The permissions required on this share are as follows:

<!-- p.946 -->

     Domain Computers. Allow the Create Folders/Append Data permission.

     Domain Users. Allow the Create Folders/Append Data permission.

     Creator Owner. Allow the Full Control permission.

                                                                                ﾉ   Expand table

 Component            Configured By    |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)    ✅

                                                                                ﾉ   Expand table

 Value       Description

 UNC_path    The UNC path of the shared folder

             Note:

             The UNC path specified in this property must exist before deploying the target
             operating system.

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DoCapture=YES BackupShare=\\NYC-AM-FIL-01\Backup$
 BackupDir=%OSDComputerName% BackupDrive=C:

BDEAllowAlphaNumericPin
This property configures whether BitLocker PINs contain alphanumeric values.

                                                                                ﾉ   Expand table

 Component            Configured By    |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅                |

<!-- p.947 -->

 Component               Configured By     |   Scenario                        Property Is Applicable

 MDT DB                  ✅                 |   ZTI (Configuration Manager)     ❌

                                                                                      ﾉ   Expand table

 Value    Description

 YES      Alphanumeric characters are allowed in the PIN.

          Note:

          In addition to setting this property to YES, the Allow enhanced PINs for startup group
          policy setting must be enabled.

 NO       Only numeric characters are allowed in the PIN.

                                                                                      ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] BDEInstallSuppress=NO BDEAllowAlphaNumericPin=YES
 BDEDriveLetter=S: BDEDriveSize=2000 BDEInstall=TPMKey BDERecoveryKey=AD BDEKeyLocation=C:

BDEDriveLetter
The drive letter for the partition that is not encrypted by BitLocker, also known as the
System Volume. SYSVOL is the directory that contains the hardware-specific files needed
to load Windows computers after the BIOS has booted the platform.

                                                                                      ﾉ   Expand table

 Component               Configured By     |   Scenario                        Property Is Applicable

 BootStrap.ini           ❌                 |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini      ✅                 |

 MDT DB                  ✅                 |   ZTI (Configuration Manager)     ❌

                                                                                      ﾉ   Expand table

 Value           Description

 drive_letter    The letter designation for the logical drive for the System Volume (such as S or T).

<!-- p.948 -->

 Value           Description

                 The default value is S.

                                                                                     ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] BDEInstallSuppress=NO BDEDriveLetter=S:
 BDEDriveSize=2000 BDEInstall=TPMKey BDERecoveryKey=AD BDEKeyLocation=C:

BDEDriveSize
The size of the BitLocker system partition. The value is specified in megabytes. In the
example, the size of the BitLocker partition to create is almost 2 GB (2,000 MB).

                                                                                     ﾉ   Expand table

 Component               Configured By      |   Scenario                        Property Is Applicable

 BootStrap.ini           ❌                  |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini      ✅                  |

 MDT DB                  ✅                  |   ZTI (Configuration Manager)     ✅

                                                                                     ﾉ   Expand table

 Value              Description

 drive_size         The size of the partition in megabytes; the default sizes are:

                    - Windows 7 and Windows Server 2008 R2: 300 MB

                                                                                     ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] BDEInstallSuppress=NO BDEDriveLetter=S:
 BDEDriveSize=2000 BDEInstall=TPMKey BDERecoveryKey=AD BDEKeyLocation=C:

BDEInstall

<!-- p.949 -->

The type of BitLocker installation to be performed. Protect the target computer using
one of the following methods:

       A TPM microcontroller

       A TPM and an external startup key (using a key that is typically stored on a USB
       flash drive [UFD])

       A TPM and PIN

       An external startup key

                                                                                     ﾉ    Expand table

 Component             Configured By      |   Scenario                         Property Is Applicable

 BootStrap.ini         ❌                  |   LTI (Stand-alone MDT)            ✅

 CustomSettings.ini    ✅                  |

 MDT DB                ✅                  |   ZTI (Configuration Manager)      ❌

                                                                                     ﾉ    Expand table

 Value      Description

 TPM        Protect the computer with TPM only. The TPM is a microcontroller that stores keys,
            passwords, and digital certificates. The microcontroller is typically an integral part of
            the computer motherboard.

 TPMKey     Protect the computer with TPM and a startup key. Use this option to create a startup
            key and to save it on a UFD. The startup key must be present in the port each time the
            computer starts.

 TPMPin     Protect the computer with TPM and a pin. Use this option in conjunction with the
            BDEPin property.

 Key        Protect the computer with an external key (the recovery key) that can be stored in a
            folder, in AD DS, or printed.

                                                                                     ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] BDEInstallSuppress=NO BDEDriveLetter=S:
 BDEDriveSize=2000 BDEInstall=TPMKey BDERecoveryKey=AD BDEKeyLocation=C:

<!-- p.950 -->

BDEInstallSuppress
Indicates whether the deployment process should skip the BitLocker installation.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ❌

                                                                               ﾉ   Expand table

 Value            Description

 YES              Do not attempt to install BitLocker.

 NO               Attempt to install BitLocker.

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] BDEInstallSuppress=YES

BDEKeyLocation
The location for storing the BitLocker recovery key and startup key.

  ７ Note

  If this property is configured using the Deployment Wizard, the property must be
  the drive letter of a removable disk. If the SkipBitLocker property is set to TRUE so

<!-- p.951 -->

  that the Specify the BitLocker configuration wizard page is skipped, this property
  can be set to a UNC path in CustomSettings.ini or in the MDT database (MDT DB).

                                                                                     ﾉ    Expand table

 Component             Configured By      |   Scenario                         Property Is Applicable

 BootStrap.ini         ❌                  |   LTI (Stand-alone MDT)            ✅

 CustomSettings.ini    ✅                  |

 MDT DB                ✅                  |   ZTI (Configuration Manager)      ❌

                                                                                     ﾉ    Expand table

 Value      Description

 Location   Specifies where the recovery key will be stored; must be a UNC path or the drive letter
            of a removable disk. If not set, the first available removable drive will be used.

                                                                                     ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] BDEInstallSuppress=NO BDEDriveLetter=S:
 BDEDriveSize=2000 BDEInstall=TPMKey BDERecoveryKey=AD BDEKeyLocation=C:

BDEPin
The PIN to be assigned to the target computer when configuring BitLocker and the
BDEInstall or OSDBitLockerMode properties are set to TPMPin.

                                                                                     ﾉ    Expand table

 Component             Configured By      |   Scenario                         Property Is Applicable

 BootStrap.ini         ❌                  |   LTI (Stand-alone MDT)            ✅

 CustomSettings.ini    ✅                  |

 MDT DB                ✅                  |   ZTI (Configuration Manager)      ❌

                                                                                     ﾉ    Expand table

<!-- p.952 -->

 Value     Description

 Pin       The PIN to be used for BitLocker. The PIN can be between 4 and 20 digits long.

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] BDEInstallSuppress=NO BDEDriveLetter=S:
 BDEDriveSize=2000 BDEInstall=TPMPin BDEPin=123456789

BDERecoveryKey
A Boolean value that indicates whether the process creates a recovery key for BitLocker.
The key is used for recovering data encrypted on a BitLocker volume. This key is
cryptographically equivalent to a startup key. If available, the recovery key decrypts the
volume master key (VMK), which, in turn, decrypts the full volume encryption key (FVEK).

  ７ Note

  The recovery key is stored in the location specified in the BDEKeyLocation
  property.

                                                                                 ﾉ   Expand table

 Component               Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ✅               |

 MDT DB                  ✅               |   ZTI (Configuration Manager)   ❌

                                                                                 ﾉ   Expand table

 Value                             Description

 AD                                A recovery key is created.

 Not specified                     A recovery key is not created.

                                                                                 ﾉ   Expand table

<!-- p.953 -->

 Example

 [Settings] Priority=Default [Default] BDEInstallSuppress=NO BDEDriveLetter=S:
 BDEDriveSize=2000 BDEInstall=TPMKey BDERecoveryKey=AD BDEKeyLocation=C:

BDEWaitForEncryption
Specifies that the deployment process should not proceed until BitLocker has completed
the encryption process for all specified drives. Specifying TRUE could dramatically
increase the time required to complete the deployment process.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                                  ﾉ   Expand table

 Component               Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ✅               |

 MDT DB                  ✅               |   ZTI (Configuration Manager)   ❌

                                                                                  ﾉ   Expand table

 Value     Description

 TRUE      Specifies that the deployment process should wait for drive encryption to complete.

 FALSE     Specifies that the deployment process should not wait for drive encryption to complete.

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] BDEInstallSuppress=NO BDEDriveLetter=S:
 BDEDriveSize=2000 OSDBitLockerMode=TPMKey OSDBitLockerStartupKeyDrive=C:
 OSDBitLockerCreateRecoveryPassword=AD BDEWaitForEncryption=TRUE

BitsPerPel

<!-- p.954 -->

A setting for displaying colors on the target computer. The property can contain
numeric digits and corresponds to the color quality setting. In the example, 32 indicates
32 bits per pixel for color quality. This value is inserted into the appropriate
configuration settings in Unattend.xml.

  ７ Note

  The default values (in the Unattend.xml template file) are 1,024 pixels horizontal
  resolution, 768 pixels vertical resolution, 32-bit color depth, and 60 Hertz (Hz)
  vertical refresh rate.

                                                                                     ﾉ   Expand table

 Component              Configured By      |   Scenario                        Property Is Applicable

 BootStrap.ini          ❌                  |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini     ✅                  |

 MDT DB                 ✅                  |   ZTI (Configuration Manager)     ✅

                                                                                     ﾉ   Expand table

 Value            Description

 bits_per_pixel   The number of bits per pixel to use for color. The default value is the default for
                  the operating system being deployed.

                                                                                     ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] BitsPerPel=32 VRefresh=60 XResolution=1024
 YResolution=768

BuildID
Identifies the operating system task sequence to be deployed to the target computer.
You create the task sequence ID on the Task Sequences node in the Deployment
Workbench. The BuildID property allows alphanumeric characters, hyphens (-), and
underscores (_). The BuildID property cannot be blank or contain spaces.

<!-- p.955 -->

                                                                                 ﾉ   Expand table

 Component             Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                |

 MDT DB                ✅                |   ZTI (Configuration Manager)   ❌

                                                                                 ﾉ   Expand table

 Value      Description

 build_id   Identifier of the operating system task sequence as defined in the Deployment
            Workbench for the target operating system being deployed

            Note:

            Make certain to use the TaskSequenceID specified in the Deployment Workbench user
            interface (UI) and not the GUID of the TaskSequenceID.

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] BuildID=BareMetal

CapableArchitecture
The processor architecture of the processor supported by the target computer, not the
current processor architecture that is running. For example, when running a 32-bit-
compatible operating system on a 64-bit processor, CapableArchitecture will indicate
that the processor architecture is 64 bit.

Use the Architecture property to see the processor architecture that is currently running.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                 ﾉ   Expand table

<!-- p.956 -->

 Component             Configured By      |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                  |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ❌                  |

 MDT DB                ❌                  |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value                Description

 x86                  Processor architecture is 32 bit.

 x64                  Processor architecture is 64 bit.

                                                                                 ﾉ   Expand table

 Example

 None

CaptureGroups
Controls whether the group membership of local groups on the target computer is
captured. This group membership is captured during the State Capture Phase and is
restored during the State Restore Phase.

  ７ Note

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                                 ﾉ   Expand table

 Component             Configured By      |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                  |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                  |

 MDT DB                ✅                  |   ZTI (Configuration Manager)   ✅

<!-- p.957 -->

                                                                                     ﾉ   Expand table

 Value   Description

 NO      Captures no group membership information.

 ALL     Captures the membership of all local groups on the target computer.

 YES     Captures the membership of the Administrator and Power Users built-in groups and the
         groups listed in the groups' properties. This is the default value if some other value is
         specified. (YES is the typical value.)

                                                                                     ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DeployRoot=\\NYC-AM-FIL-01\Distribution$
 ResourceRoot=\\NYC-AM-FIL-01\Resource$ UDShare=\\NYC-AM-FIL-01\MigData$ CaptureGroups=YES
 Groups1=NYC Application Management Groups2=NYC Help Desk Users

ChildName
Specifies whether to append the DNS label at the beginning of the name of an existing
directory service domain when installing a child domain.

                                                                                     ﾉ   Expand table

 Component              Configured By      |      Scenario                      Property Is Applicable

 BootStrap.ini          ❌                  |      LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                  |

 MDT DB                 ✅                  |      ZTI (Configuration Manager)   ✅

                                                                                     ﾉ   Expand table

 Value                 Description

 name                  The name of the child domain

                                                                                     ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] ChildName=childdom.parentdom.WoodGroveBank.com

<!-- p.958 -->

ComputerBackupLocation
The network shared folder where the computer backup is stored. If the target folder
does not already exist, it is automatically created.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                                      ﾉ   Expand table

 Component               Configured By     |   Scenario                        Property Is Applicable

 BootStrap.ini           ❌                 |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini      ✅                 |

 MDT DB                  ✅                 |   ZTI (Configuration Manager)     ✅

                                                                                      ﾉ   Expand table

 Value           Description

 blank           Same as AUTO.

 UNC_path        The UNC path to the network shared folder where the backup is stored.

 AUTO            Creates a backup on a local hard disk if space is available. Otherwise, the backup is
                 saved to a network location specified in the BackupShare and BackupDir properties.

 NETWORK         Creates a backup on a network location specified in BackupShare and BackupDir.

 NONE            No backup will be performed.

                                                                                      ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DeployRoot=\\NYC-AM-FIL-01\Distribution$
 ResourceRoot=\\NYC-AM-FIL-01\Resource$ UDShare=\\NYC-AM-FIL-01\MigData$
 ComputerBackupLocation=NETWORK BackupShare=\\NYC-AM-FIL-01\Backup$
 BackupDir=%OSDComputerName% UDDir=%OSDComputerName% SLShare=\\NYC-AM-FIL-01\Logs$
 UDProfiles=Administrator, User-01, ExtranetUser UserDataLocation=NONE

<!-- p.959 -->

ComputerName
This property has been deprecated. Use OSDComputerName instead.

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ❌

 CustomSettings.ini   ❌               |

 MDT DB               ❌               |   ZTI (Configuration Manager)   ❌

                                                                             ﾉ   Expand table

 Value                            Description

 None                             None

                                                                             ﾉ   Expand table

 Example

 None

ConfigFileName
Specifies the name of the configuration file used during OEM deployments.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ❌               |

 MDT DB               ❌               |   ZTI (Configuration Manager)   ✅

<!-- p.960 -->

                                                                                 ﾉ   Expand table

 Value           Description

 file_name       Specifies the name of the configuration file used during OEM deployments

                                                                                 ﾉ   Expand table

 Example

 None

ConfigFilePackage
Specifies the package ID for the configuration package used during OEM deployments.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                 ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌                 |

 MDT DB                 ❌                 |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value       Description

 package     Specifies the package ID for the configuration package used during OEM deployments

                                                                                 ﾉ   Expand table

 Example

 None
