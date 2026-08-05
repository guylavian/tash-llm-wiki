---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1121-1160"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1121-1160
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1121-1160
family: sccm
documentKind: "doc"
abstract: "Value Description drive_letter The letter designation for the logical drive that contains the resources ﾉ Expand table Example None ResourceRoot The value of this property is used by the ZTIDrivers.wsf and ZTIPatches.wsf scripts to install drivers and patches to the target compu"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1121-1160

<!-- p.1121 -->

 Value           Description

 drive_letter    The letter designation for the logical drive that contains the resources

                                                                                   ﾉ    Expand table

 Example

 None

ResourceRoot
The value of this property is used by the ZTIDrivers.wsf and ZTIPatches.wsf scripts to
install drivers and patches to the target computer.

  ７ Note

  For LTI, the scripts automatically set the ResourceRoot property to be the same as
  the DeployRoot property. For ZTI, the values in the DeployRoot and ResourceRoot
  properties can be unique.

                                                                                   ﾉ    Expand table

 Component            Configured By      |   Scenario                        Property Is Applicable

 BootStrap.ini        ✅                  |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini   ✅                  |

 MDT DB               ✅                  |   ZTI (Configuration Manager)     ✅

                                                                                   ﾉ    Expand table

 Value           Description

 UNC_path        The UNC path to the shared folder that contains the resources

                                                                                   ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] DeployRoot=\\NYC-AM-FIL-01\Distribution$
 ResourceDrive=R: ResourceRoot=\\NYC-AM-FIL-01\Resource$ UserDataLocation=NONE

<!-- p.1122 -->

Role
The purpose of a computer based on the tasks performed by the user on the target
computer. The Role property lists text values that can be any non-blank value. The Role
property value has a numeric suffix (for example, Role1 or Role2). When defined, a role is
associated with a computer. A computer can perform more than one role.

Typically, the value for the Role property is set by performing a database query in the
MDT DB. The Deployment Workbench can assist in creating the role and property
settings associated with the role, and then the Deployment Workbench can configure
CustomSettings.ini to perform the database query for the Role property and the
property settings associated with the role.

                                                                               ﾉ   Expand table

 Component              Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini          ✅               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅               |

 MDT DB                 ✅               |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value    Description

 Role     The roles to be assigned to an individual computer or a group of computers

                                                                               ﾉ   Expand table

 Example 1

 [Settings] Priority=RoleSettings, Default [Default] SkipCapture=NO UserDataLocation=AUTO
 DeployRoot=\\W2K3-SP1\Distribution$ OSInstall=YES ScanStateArgs=/v:15 /o /c
 LoadStateArgs=/v:7 /c [RoleSettings] SQLServer=w2k3-sp1 Instance=MDT2010 Database=MDTDB
 Netlib=DBNMPNTW SQLShare=SQL_Share Table=RoleSettings Parameters=Role

                                                                               ﾉ   Expand table

 Example 2

 [Settings] Priority=RoleSettings, Default [Default] SkipCapture=NO UserDataLocation=AUTO
 DeployRoot=\\W2K3-SP1\Distribution$ OSInstall=YES Role1=Teller Role2=Woodgrove User

<!-- p.1123 -->

 Example 2

 [RoleSettings] SQLServer=w2k3-sp1 Instance=MDT2010 Database=MDTDB Netlib=DBNMPNTW
 SQLShare=SQL_Share Table=RoleSettings Parameters=Role

SafeModeAdminPassword
Supplies the password for the administrator account when starting the computer in Safe
mode or a variant of Safe mode, such as Directory Services Restore mode.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value       Description

 password    Supplies the password for the administrator account when starting the computer in
             Safe mode or a variant of Safe mode, such as Directory Services Restore mode

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] SafeModeAdminPassword=<complex_password>

ScanStateArgs
Arguments passed to the USMT Scanstate process. The scripts call Scanstate.exe, and
then insert the appropriate logging, progress, and state store parameters. If this value is
not included in the settings file, the user state backup process is skipped.

  ７ Note

  Use the USMTMigFiles property to specify the .xml files to be used by
  Scanstate.exe instead of using the /I parameter in the ScanStateArgs property. This

<!-- p.1124 -->

 prevents the ZTIUserState.wsf script from potentially duplicating the same list of
 .xml files.

 ７ Note

 Do not add any of the following command line arguments when configuring this
 property: /hardlink, /nocompress, /encrypt, /key, or /keyfile. The MDT scripts will
 add these command-line arguments if applicable to the current deployment
 scenario.

                                                                                         ﾉ    Expand table

Component                Configured By       |   Scenario                          Property Is Applicable

BootStrap.ini            ❌                   |   LTI (Stand-alone MDT)             ✅

CustomSettings.ini       ✅                   |

MDT DB                   ✅                   |   ZTI (Configuration Manager)       ❌

                                                                                         ﾉ    Expand table

Value           Description

arguments       The command-line arguments passed to Scanstate.exe.

                The default arguments specified by the Deployment Workbench are as follows:

                - /v. Enables verbose output in the Scanstate log. The default is 0. Specify any
                number from 0 to 15. The value 5 enables verbose and status output.

                - /o. Overwrites any existing data in the store. If not specified, Scanstate will fail if the
                store already contains data. This option cannot be specified more than once in a
                Command Prompt window.

                - /c. When specified, Scanstate will continue to run even if there are nonfatal errors.
                Without the /c option, Scanstate exits on the first error.

                For more information about these and other arguments, see the USMT Help files.

                                                                                         ﾉ    Expand table

<!-- p.1125 -->

 Example

 [Settings] Priority=Default [Default] ScanStateArgs=/v:5 /o /c LoadStateArgs=/v:5 /c /lac
 DeployRoot=\\NYC-AM-FIL-01\Distribution$ ResourceRoot=\\NYC-AM-FIL-01\Resource$
 UDShare=\\NYC-AM-FIL-01\MigData$ UDDir=%OSDComputerName%

SerialNumber
The serial number of the target computer. The format for serial numbers is undefined.
Use this property to create a subsection that contains settings targeted to a specific
computer.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                ﾉ    Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ❌                 |

 MDT DB               ❌                 |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ    Expand table

 Value           Description

 serial_number   The format of the serial number is undefined and is determined by the serial
                 number standard of each computer manufacturer.

                                                                                ﾉ    Expand table

 Example

 None

SiteName
Specifies the name of an existing site where you can place the new domain controller.

<!-- p.1126 -->

                                                                                ﾉ   Expand table

 Component              Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅               |

 MDT DB                 ✅               |   ZTI (Configuration Manager)   ❌

                                                                                ﾉ   Expand table

 Value    Description

 name     Specifies the name of an existing site where you can place the new domain controller

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] SiteName=FirstSite

SkipAdminAccounts
Indicates whether the Local Administrators wizard page is skipped.

  ７ Note

  This default value for this property is YES, which means that the Local
  Administrators wizard page will be skipped by default. To display this wizard page,
  you must specifically set the value of this property to NO in CustomSettings.ini or
  in the MDT DB.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                ﾉ   Expand table

<!-- p.1127 -->

 Component             Configured By    |   Scenario                        Property Is Applicable

 BootStrap.ini         ❌                |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini    ✅                |

 MDT DB                ✅                |   ZTI (Configuration Manager)     ❌

                                                                                    ﾉ   Expand table

 Value   Description

 YES     Wizard page is not displayed, and the information on that page is not collected. This is
         the default value.

 NO      Wizard page is displayed, and the information on that page is collected.

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipAdminAccounts=NO
 SkipAdminPassword=NO SkipApplications=NO SkipComputerBackup=NO SkipDomainMembership=NO
 SkipUserData=NO SkipPackageDisplay=NO SkipLocaleSelection=NO SkipProductKey=YES

SkipAdminPassword
Indicates whether the Administrator Password wizard page is skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                    ﾉ   Expand table

 Component             Configured By    |   Scenario                        Property Is Applicable

 BootStrap.ini         ❌                |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini    ✅                |

<!-- p.1128 -->

 Component             Configured By     |   Scenario                       Property Is Applicable

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ    Expand table

 Value   Description

 YES     Wizard page is not displayed, and the information on that page is not collected.

 NO      Wizard page is displayed, and the information on that page is collected. This is the default
         value.

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipAdminPassword=YES
 SkipApplications=NO SkipComputerBackup=NO SkipDomainMembership=NO SkipUserData=NO
 SkipPackageDisplay=NO SkipLocaleSelection=NO SkipProductKey=YES

SkipApplications
Indicates whether the Select one or more applications to install wizard page is skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

<!-- p.1129 -->

                                                                                  ﾉ    Expand table

 Value   Description

 YES     Wizard page is not displayed, and the information on that page is not collected.

 NO      Wizard page is displayed, and the information on that page is collected. This is the default
         value.

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipAdminPassword=NO
 SkipApplications=YES SkipComputerBackup=NO SkipDomainMembership=NO SkipUserData=NO
 SkipPackageDisplay=NO SkipLocaleSelection=NO SkipProductKey=YES

SkipBDDWelcome
Indicates whether the Welcome to Windows Deployment wizard page is skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  ７ Note

  For this property to function properly it must be configured in both
  CustomSettings.ini and BootStrap.ini. BootStrap.ini is processed before a
  deployment share (which contains CustomSettings.ini) has been selected.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

<!-- p.1130 -->

 Component             Configured By     |   Scenario                       Property Is Applicable

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ    Expand table

 Value   Description

 YES     Wizard page is not displayed, and the information on that page is not collected.

 NO      Wizard page is displayed, and the information on that page is collected. This is the default
         value.

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipAdminPassword=YES
 SkipApplications=NO SkipBDDWelcome=YES SkipComputerBackup=NO SkipDomainMembership=NO
 SkipUserData=NO SkipPackageDisplay=NO SkipLocaleSelection=NO SkipProductKey=YES

SkipBitLocker
Indicates whether the Specify the BitLocker configuration wizard page is skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

<!-- p.1131 -->

                                                                                  ﾉ    Expand table

 Value   Description

 YES     Wizard page is not displayed, and the information on that page is not collected.

 NO      Wizard page is displayed, and the information on that page is collected. This is the default
         value.

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipApplications=NO
 SkipBDDWelcome=YES SkipBitLocker=YES SkipComputerBackup=NO SkipDomainMembership=NO
 SkipUserData=NO SkipPackageDisplay=NO SkipLocaleSelection=NO

SkipBuild
Indicates whether the Select a task sequence to execute on this computer wizard page
is skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

This property value must be specified in uppercase letters so that the deployment
scripts can properly read it.

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ    Expand table

 Value   Description

 YES     Wizard page is not displayed, and the information on that page is not collected.

 NO      Wizard page is displayed, and the information on that page is collected. This is the default
         value.

<!-- p.1132 -->

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipAdminPassword=YES
 SkipApplications=NO SkipBDDWelcome=YES SkipBuild=YES SkipComputerBackup=NO
 SkipComputerName=NO SkipDomainMembership=NO SkipFinalSummary=NO SkipSummary=NO
 SkipUserData=NO SkipPackageDisplay=NO SkipLocaleSelection=NO

SkipCapture
Indicates whether the Specify whether to capture an image wizard page is skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ    Expand table

 Value   Description

 YES     The wizard page is not displayed, and the information on that page is not collected.

 NO      The wizard page is displayed, and the information on that page is collected. This is the
         default value.

                                                                                  ﾉ    Expand table

<!-- p.1133 -->

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=YES SkipApplications=NO
 SkipComputerBackup=NO SkipDomainMembership=NO SkipUserData=NO SkipPackageDisplay=NO
 SkipLocaleSelection=NO

SkipComputerBackup
Indicates whether the Specify where to save a complete computer backup wizard page
is skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ    Expand table

 Value   Description

 YES     The wizard page is not displayed, and the information on that page is not collected.

 NO      The wizard page is displayed, and the information on that page is collected. This is the
         default value.

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipAdminPassword=NO
 SkipApplications=NO SkipComputerBackup=YES SkipDomainMembership=NO SkipUserData=NO

<!-- p.1134 -->

 Example

 SkipPackageDisplay=NO SkipLocaleSelection=NO

SkipComputerName
Indicates whether the Configure the computer name wizard page is skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ    Expand table

 Value   Description

 YES     Wizard page is not displayed, and the information on that page is not collected.

 NO      Wizard page is displayed, and the information on that page is collected. This is the default
         value.

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipAdminPassword=NO
 SkipApplications=NO SkipComputerBackup=NO SkipComputerName=YES SkipDomainMembership=NO
 SkipUserData=NO SkipPackageDisplay=NO SkipLocaleSelection=NO

SkipDomainMembership

<!-- p.1135 -->

Indicates whether the Join the computer to a domain or workgroup wizard page is
skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                    ﾉ    Expand table

 Component               Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini           ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini      ✅                 |

 MDT DB                  ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                    ﾉ    Expand table

 Value     Description

 YES       The wizard page is not displayed, and the information on that page is not collected.

 NO        The wizard page is displayed, and the information on that page is collected. This is the
           default value.

                                                                                    ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipAdminPassword=NO
 SkipApplications=NO SkipComputerBackup=NO SkipUserData=NO SkipPackageDisplay=NO
 SkipLocaleSelection=NO SkipDomainMembership=NO

SkipFinalSummary
Indicates whether the Operating system deployment completed successfully wizard
page is skipped.

<!-- p.1136 -->

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  ７ Note

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ    Expand table

 Value   Description

 YES     The wizard page is not displayed, and the information on that page is not collected.

 NO      The wizard page is displayed, and the information on that page is collected. This is the
         default value.

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipApplications=NO
 SkipBDDWelcome=YES SkipComputerBackup=NO SkipComputerName=NO SkipDomainMembership=NO
 SkipFinalSummary=NO SkipUserData=NO SkipPackageDisplay=NO SkipLocaleSelection=NO
 SkipProductKey=YES

SkipGroupSubFolders
By default, when specifying folders to be included when injecting drivers, patches
(packages), and so on, values are specified something like:

  ini

  DriverGroup001=TopFolder\SecondFolder

<!-- p.1137 -->

  PackageGroup001=TopFolder\SecondFolder

This would, by default, also include all sub-folders located under the "SecondFolder." If
SkipGroupSubFolders is set to YES in CustomSettings.ini, this behavior will change so
that the subfolders will be excluded and only the contents of "SecondFolder" will be
added.

To exclude subfolders when matching against groups such as DriverGroup001,
PackageGroup001, and so on, set SkipGroupSubFolders to YES.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                 ﾉ   Expand table

 Component               Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ✅               |

 MDT DB                  ✅               |   ZTI (Configuration Manager)   ❌

                                                                                 ﾉ   Expand table

 Value     Description

 YES       Do not include subfolders when matching against groups.

 NO        Include subfolders when matching against groups. This is the default behavior.

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] SkipGroupSubFolders=NO

SkipLocaleSelection
Indicates whether the Locale Selection wizard page is skipped.

<!-- p.1138 -->

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ    Expand table

 Value   Description

 YES     The wizard page is not displayed, and the information on that page is not collected.

 NO      The wizard page is displayed, and the information on that page is collected. This is the
         default value.

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipApplications=NO
 SkipComputerBackup=NO SkipDomainMembership=NO SkipUserData=NO SkipPackageDisplay=NO
 SkipLocaleSelection=NO

SkipPackageDisplay
Indicates whether the Packages wizard page is skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  Ｕ Caution

<!-- p.1139 -->

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ    Expand table

 Value   Description

 YES     The wizard page is not displayed, and the information on that page is not collected.

 NO      The wizard page is displayed, and the information on that page is collected. This is the
         default value.

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipApplications=NO
 SkipComputerBackup=NO SkipDomainMembership=NO SkipUserData=NO SkipPackageDisplay=YES
 SkipLocaleSelection=NO

SkipProductKey
Indicates whether the Specify the product key needed to install this operating system
wizard page is skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

<!-- p.1140 -->

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ    Expand table

 Value   Description

 YES     The wizard page is not displayed, and the information on that page is not collected.

 NO      The wizard page is displayed, and the information on that page is collected. This is the
         default value.

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipAdminPassword=YES
 SkipApplications=NO SkipComputerBackup=NO SkipDomainMembership=NO SkipUserData=NO
 SkipPackageDisplay=NO SkipLocaleSelection=NO SkipProductKey=YES

SkipRearm
This property is used to configure whether MDT rearms the Microsoft Office 2010 25-
day activation grace period. If Microsoft Office 2010 is captured in a custom image, the
user sees activation notification dialog boxes immediately after the image is deployed
instead of 25-days after deployment.

By default, MDT rearms the Microsoft Office 2010 25-day activation grace period when
running the LTISysprep.wsf script. You can set the value of this property to YES so that
MDT skips the rearming of the Microsoft Office 2010 25-day activation grace period.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

<!-- p.1141 -->

                                                                                 ﾉ   Expand table

 Component             Configured By    |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                |

 MDT DB                ✅                |   ZTI (Configuration Manager)    ❌

                                                                                 ﾉ   Expand table

 Value   Description

 YES     MDT does not rearm the Microsoft Office 2010 25-day activation grace period.

 NO      MDT rearms the Microsoft Office 2010 25-day activation grace period. This is the default
         value.

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSInstall=Y SkipCapture=YES SkipAdminPassword=NO
 SkipProductKey=YES SkipRearm=YES DoCapture=YES

SkipRoles
Indicates whether the Roles and Features wizard page is skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                 ﾉ   Expand table

 Component             Configured By    |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                |

<!-- p.1142 -->

 Component             Configured By     |   Scenario                       Property Is Applicable

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ    Expand table

 Value   Description

 YES     The wizard page is not displayed, and the information on that page is not collected.

 NO      The wizard page is displayed, and the information on that page is collected. This is the
         default value.

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipAdminPassword=YES
 SkipApplications=NO SkipBDDWelcome=YES SkipTaskSequence=Yes SkipComputerBackup=NO
 SkipComputerName=NO SkipDomainMembership=NO SkipFinalSummary=NO SkipRoles=YES SkipSummary=NO
 SkipUserData=NO SkipPackageDisplay=NO SkipLocaleSelection=NO

SkipSummary
Indicates whether the Ready to begin wizard page is skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

<!-- p.1143 -->

                                                                                  ﾉ    Expand table

 Value   Description

 YES     The wizard page is not displayed, and the information on that page is not collected.

 NO      The wizard page is displayed, and the information on that page is collected. This is the
         default value.

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipAdminPassword=YES
 SkipApplications=NO SkipBDDWelcome=YES SkipTaskSequence=Yes SkipComputerBackup=NO
 SkipComputerName=NO SkipDomainMembership=NO SkipFinalSummary=NO SkipSummary=NO
 SkipUserData=NO SkipPackageDisplay=NO SkipLocaleSelection=NO

SkipTaskSequence
Indicates whether the Select a task sequence to execute on this computer wizard page
is skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  ７ Note

  Specify the SkipBuild property when using the Deployment Workbench to
  configure the Deployment Wizard to skip the Select a task sequence to execute on
  this computer wizard page.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

<!-- p.1144 -->

 Component             Configured By     |   Scenario                       Property Is Applicable

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ    Expand table

 Value   Description

 YES     The wizard page is not displayed, and the information on that page is not collected.

 NO      The wizard page is displayed, and the information on that page is collected. This is the
         default value.

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipApplications=NO
 SkipBDDWelcome=YES SkipTaskSequence=NO SkipComputerBackup=NO SkipComputerName=NO
 SkipDomainMembership=NO SkipFinalSummary=NO SkipSummary=NO SkipUserData=NO
 SkipPackageDisplay=NO SkipLocaleSelection=NO

SkipTimeZone
Indicates whether the Set the Time Zone wizard page is skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

<!-- p.1145 -->

 Component             Configured By     |   Scenario                       Property Is Applicable

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ    Expand table

 Value   Description

 YES     The wizard page is not displayed, and the information on that page is not collected.

 NO      The wizard page is displayed, and the information on that page is collected. This is the
         default value.

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipAdminPassword=YES
 SkipApplications=NO SkipBDDWelcome=YES SkipTaskSequence=YES SkipComputerBackup=NO
 SkipComputerName=NO SkipDomainMembership=NO SkipFinalSummary=NO SkipSummary=NO
 SkipTimeZone=NO SkipUserData=NO SkipPackageDisplay=NO SkipLocaleSelection=NO

SkipUserData
Indicates whether the Specify whether to restore user data and Specify where to save
your data and settings wizard page is skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

<!-- p.1146 -->

                                                                                  ﾉ    Expand table

 Value   Description

 YES     The wizard page is not displayed, and the information on that page is not collected.

 NO      The wizard page is displayed, and the information on that page is collected. This is the
         default value.

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=NO SkipCapture=NO SkipAdminPassword=YES
 SkipApplications=NO SkipComputerBackup=NO SkipDomainMembership=NO SkipUserData=NO
 SkipPackageDisplay=NO SkipLocaleSelection=NO SkipProductKey=YES

SkipWizard
Indicates whether the entire Deployment Wizard is skipped.

For other properties that must be configured when this property is set to YES, see
Providing Properties for Skipped Deployment Wizard Pages.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ    Expand table

 Value   Description

 YES     The entire wizard is not displayed, and none of the information on the wizard pages is

<!-- p.1147 -->

 Value   Description

         collected.

 NO      The wizard is displayed, and the information on the enabled wizard pages is collected.
         This is the default value.

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] SkipWizard=YES

SLShare
The network shared folder in which the deployment logs are stored at the end of the
deployment process.

                                                                                    ﾉ   Expand table

 Component               Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ✅                 |

 MDT DB                  ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                    ﾉ   Expand table

 Value                Description

 shared_folder        The name of the network shared folder in which script logs are stored

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DeployRoot=\\NYC-AM-FIL-01\Distribution$
 ResourceRoot=\\NYC-AM-FIL-01\Resource$ UDShare=\\NYC-AM-FIL-01\MigData$
 UDDir=%OSDComputerName% SLShare=\\NYC-AM-FIL-01\Logs$ UDProfiles=Administrator, User-01,
 ExtranetUser UserDataLocation=NONE SkipCapture=NO SkipAdminPassword=YES SkipProductKey=YES

SLShareDynamicLogging

<!-- p.1148 -->

The network shared folder in which all MDT logs should be written during deployment.
This is used for advanced real-time debugging only.

                                                                                ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value            Description

 shared_folder    The name of the network shared folder in which script logs are stored

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DeployRoot=\\NYC-AM-FIL-01\Distribution$
 ResourceRoot=\\NYC-AM-FIL-01\Resource$ UDShare=\\NYC-AM-FIL-01\MigData$
 UDDir=%OSDComputerName% SLShare=\\NYC-AM-FIL-01\Logs$ SLShareDynamicLogging=\\NYC-AM-FIL-
 01\Logs$ UDProfiles=Administrator, User-01, ExtranetUser UserDataLocation=NONE
 SkipCapture=NO SkipAdminPassword=YES SkipProductKey=YES

SMSTSAssignUserMode
Specifies whether user device affinity (UDA) should be enabled and whether approval is
required. This property only works with the UDA feature in Configuration Manager.

                                                                                ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ❌

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

<!-- p.1149 -->

 Value       Description

 Auto        The affinity between a user and the target device is established, and approval is
             automatically performed.

 Pending     The affinity between a user and the target device is established, and approval is
             submitted for Configuration Manager administrator approval.

 Disable     The affinity between a user and the target device is not established.

                                                                                     ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] SMSTSAssignUserMode=Auto SMSTSUdaUsers=Fabrikam\Ken,
 Fabrikam\Pilar

SMSTSRunCommandLineUserName
Specifies the user name in Domain\User_Name format that should be used with a Run
Command Line step that is configured to run as a user.

                                                                                     ﾉ   Expand table

 Component              Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)    ✅

                                                                                     ﾉ   Expand table

 Value           Description

 user_name       Specifies the user name in that should be used with a Run Command Line step

                                                                                     ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] SMSTSRunCommandLineUserName=Fabrikam\Ken
 SMSTSRunCommandLineUserPassword=<complex_password>

<!-- p.1150 -->

SMSTSRunCommandLineUserPassword
Specifies the password that should be used with a Run Command Line step that is
configured to run as a user.

                                                                             ﾉ    Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ✅

                                                                             ﾉ    Expand table

 Value            Description

 user_password    Specifies the password that should be used with a Run Command Line step

                                                                             ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] SMSTSRunCommandLineUserName=Fabrikam\Ken
 SMSTSRunCommandLineUserPassword=<complex_password>

SMSTSUdaUsers
Specifies the users who will be assigned affinity with a specific device using the UDA
feature, which is available only in Configuration Manager.

                                                                             ﾉ    Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ❌

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ✅

                                                                             ﾉ    Expand table

<!-- p.1151 -->

 Value        Description

 user1,       The comma-separated list of users in Domain\User_Name format that will be assigned
 user2, ...   affinity with the target device.

              Note:

              You can only use the NetBIOS domain name in this value, such as Fabrikam\Ken. You
              cannot use the fully qualified domain name (fabrikam.com\Ken) or the UPN notation
              (ken@fabrikam.com).

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] SMSTSAssignUserMode=Auto SMSTSUdaUsers=Fabrikam\Ken,
 Fabrikam\Pilar

SQLServer
The identity of the computer running SQL Server that performs a database query that
returns property values from columns in the table specified in the Table property. The
query is based on parameters specified in the Parameters and ParameterCondition
properties. The instance of SQL Server on the computer is specified in the Instance
property.

                                                                                ﾉ   Expand table

 Component             Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini         ✅                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                |

 MDT DB                ❌                |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value                 Description

 SQL_server            The name of the computer running SQL Server

                                                                                ﾉ   Expand table

<!-- p.1152 -->

 Example

 [Settings] Priority=Computers, Default [Default] OSInstall=YES ScanStateArgs=/v:5 /o /c
 LoadStateArgs=/v:5 /c /lac [Computers] SQLServer=NYC-SQL-01 SQLShare=SQL$ Database=MDTDB
 Instance=SQLEnterprise2005 Table=Computers Parameters=SerialNumber, AssetTag
 ParameterCondition=OR

SQLShare
The name of a shared folder on the computer running SQL Server (specified by the
SQLServer property). The credentials used for authentication are provided by the
UserDomain, UserID, and UserPassword properties (for LTI and ZTI) or by the
Configuration Manager Advanced Client account credentials (ZTI only).

  ７ Note

  This property must be specified to perform Integrated Windows authentication.
  This is the recommended authentication method, rather than using the DBID and
  DBPwd properties (which support the SQL Server authentication method).

                                                                                ﾉ      Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ✅                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                |

 MDT DB                 ❌                |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ      Expand table

 Value                Description

 shared_folder        The name of a shared folder on the computer running SQL Server

                                                                                ﾉ      Expand table

 Example

 [Settings] Priority=Computers, Default Properties=MyCustomProperty [Default] OSInstall=YES
 ScanStateArgs=/v:5 /o /c LoadStateArgs=/v:5 /c /lac [Computers] SQLServer=NYC-SQL-01

<!-- p.1153 -->

 Example

 SQLShare=SQL$ Database=MDTDB Instance=MDT2010 Table=Computers Parameters=SerialNumber,
 AssetTag ParameterCondition=OR

StatePath
This property is used to set the path where the user state migration data will be stored,
which can be a UNC path, a local path, or a relative path. The OSDStateStorePath
property takes precedence over the StatePath or UserDataLocation property when those
properties are also specified.

  ７ Note

  This property is provided for backward compatibility with previous versions of MDT.
  Use the OSDStateStorePath property instead.

                                                                                ﾉ   Expand table

 Component             Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                |

 MDT DB                ❌                |   ZTI (Configuration Manager)   ❌

                                                                                ﾉ   Expand table

 Value   Description

 Path    The path where the user state migration data will be stored, which can be a UNC path, a
         local path, or a relative path

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] StatePath=\\fs1\Share\Replace
 ComputerBackupLocation=\\fs1\Share\ComputerBackup\Client01

StoredProcedure

<!-- p.1154 -->

The name of the stored procedure used when performing a database query that returns
property values from columns in the table or view. The stored procedure is located in
the database specified in the Database property. The computer running SQL Server is
specified in the SQLServer property. The instance of SQL Server on the computer is
specified in the Instance property. The name of the stored procedure is specified in the
StoredProcedure property.

For more information about using a stored procedure to query a SQL Server database,
see the section, "Deploying Applications Based on Earlier Application Versions", in the
MDT document Microsoft Deployment Toolkit Samples Guide.

                                                                               ﾉ   Expand table

 Component             Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini         ✅                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                |

 MDT DB                ❌                |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                Description

 stored_procedure     The name of the stored procedure used to query the SQL Server database

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=DynamicPackages, Default [Default] OSInstall=YES [DynamicPackages]
 SQLDefault=DB_DynamicPackages [DB_DynamicPackages] SQLServer=SERVER1 Database=MDTDB
 StoredProcedure=RetrievePackages Parameters=MacAddress SQLShare=Logs Instance=MDT2013
 Port=1433 Netlib=DBNMPNTW

SupportsHyperVRole
Specifies whether the processor resources on the target computer can support the
Hyper-V server role in Windows Server. This property is True if the value for the
following properties is set to TRUE:

     SupportsNX

     SupportsVT

<!-- p.1155 -->

    Supports64Bit

    Each of the previous properties is set using information from the CPUID interface.
    For further information collected about VMs and information returned from the
    CPUID interface, see the following properties:

    IsHypervisorRunning

    IsVM

    SupportsNX

    SupportsVT

    Supports64Bit

    VMPlatform

 ７ Note

 This property is dynamically set by the MDT scripts and is not configured in
 CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                               ﾉ   Expand table

Component              Configured By   |   Scenario                      Property Is Applicable

BootStrap.ini          ❌               |   LTI (Stand-alone MDT)         ✅

CustomSettings.ini     ❌               |

MDT DB                 ❌               |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

Value    Description

TRUE     The processor resources of the target computer can support the Hyper-V server role in
         Windows Server.

FALSE    The processor resources of the target computer cannot support the Hyper-V server role
         in Windows Server.

                                                                               ﾉ   Expand table

<!-- p.1156 -->

 Example

 None

SupportsNX
Specifies whether the processor resources on the target computer support the No
Execute (NX) technology. The NX technology is used in processors to segregate areas of
memory for use by either storage of processor instructions (code) or for storage of data.
This property is set using information from the CPUID interface.

For further information collected about VMs and information returned from the CPUID
interface, see the following properties:

     IsHypervisorRunning

     IsVM

     SupportsHyperVRole

     SupportsVT

     Supports64Bit

     VMPlatform

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                              ﾉ   Expand table

 Component            Configured By   |    Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |    LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ❌               |

 MDT DB               ❌               |    ZTI (Configuration Manager)   ✅

                                                                              ﾉ   Expand table

<!-- p.1157 -->

 Value       Description

 TRUE        The processor resources of the target computer support NX technology.

 FALSE       The processor resources of the target computer do not support NX technology.

                                                                                ﾉ    Expand table

 Example

 None

SupportsVT
Specifies whether the processor resources on the target computer support the
Virtualization Technology (VT) feature. VT is used to support current virtualized
environments, such as Hyper-V. This property is set using information from the CPUID
interface.

For further information collected about VMs and information returned from the CPUID
interface, see the following properties:

     IsHypervisorRunning

     IsVM

     SupportsHyperVRole

     SupportsNX

     Supports64Bit

     VMPlatform

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                ﾉ    Expand table

 Component                 Configured By   |   Scenario                   Property Is Applicable

 BootStrap.ini             ❌               |   LTI (Stand-alone MDT)      ✅

<!-- p.1158 -->

 Component               Configured By   |   Scenario                      Property Is Applicable

 CustomSettings.ini      ❌               |

 MDT DB                  ❌               |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value     Description

 TRUE      The processor resources of the target computer support VT technology.

 FALSE     The processor resources of the target computer do not support VT technology.

                                                                                ﾉ   Expand table

 Example

 None

Supports64Bit
Specifies whether the processor resources on the target computer support Windows 64-
bit operating systems. Most modern virtualization environments require 64-bit
processor architecture. This property is set using information from the CPUID interface.

For further information collected about VMs and information returned from the CPUID
interface, see the following properties:

     IsHypervisorRunning

     IsVM

     SupportsHyperVRole

     SupportsNX

     SupportsVT

     VMPlatform

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

<!-- p.1159 -->

                                                                               ﾉ   Expand table

 Component              Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌               |

 MDT DB                 ❌               |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value    Description

 TRUE     The processor resources of the target computer support a Windows 64-bit operating
          system.

 FALSE    The processor resources of the target computer do not support a Windows 64-bit
          operating system.

                                                                               ﾉ   Expand table

 Example

 None

SysVolPath
Specifies the fully qualified, non-UNC path to a directory on a fixed disk of the local
computer.

                                                                               ﾉ   Expand table

 Component              Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅               |

 MDT DB                 ✅               |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

<!-- p.1160 -->

 Value   Description

 path    Specifies the fully qualified, non-UNC path to a directory on a fixed disk of the local
         computer

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] SysVolPath=%DestinationLogicalDrive%\Windows\Sysvol

Table
The name of the table or view to be used in performing a database query that returns
property values from columns in the table or view. The query is based on parameters
specified in the Parameters and ParameterCondition properties. The table or view is
located in the database specified in the Database property. The computer running SQL
Server is specified in the SQLServer property. The instance of SQL Server on the
computer is specified in the Instance property.

                                                                                    ﾉ   Expand table

 Component             Configured By     |   Scenario                         Property Is Applicable

 BootStrap.ini         ✅                 |   LTI (Stand-alone MDT)            ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ❌                 |   ZTI (Configuration Manager)      ✅

                                                                                    ﾉ   Expand table

 Value            Description

 table_name       The name of the table or view to be queried for property values

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Computers, Default [Default] OSInstall=YES ScanStateArgs=/v:5 /o /c
 LoadStateArgs=/v:5 /c /lac [Computers] SQLServer=NYC-SQL-01 SQLShare=SQL$ Database=MDTDB
 Instance=MDT2010 Table=Computers Parameters=SerialNumber, AssetTag ParameterCondition=OR
