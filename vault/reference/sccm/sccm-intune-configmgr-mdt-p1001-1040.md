---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1001-1040"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1001-1040
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1001-1040
family: sccm
documentKind: "doc"
abstract: "ﾉ Expand table Value Description Domain Replicates zone data to all DNS server in the AD DS domain Forest Replicates zone data to all DNS server in the AD DS forest Legacy Replicates zone data to all domain controllers in the AD DS domain ﾉ Expand table Example [Settings] Priori"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1001-1040

<!-- p.1001 -->

                                                                                        ﾉ   Expand table

 Value           Description

 Domain          Replicates zone data to all DNS server in the AD DS domain

 Forest          Replicates zone data to all DNS server in the AD DS forest

 Legacy          Replicates zone data to all domain controllers in the AD DS domain

                                                                                        ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DNSZones0DirectoryPartition=Forest

DNSZonesxFileName
Specifies the name of the file that will store the zone information.

  ７ Note

  The x in this properties name is a placeholder for a zero-based array that contains
  DNS configurations.

                                                                                        ﾉ   Expand table

 Component               Configured By     |   Scenario                        Property Is Applicable

 BootStrap.ini           ❌                 |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini      ✅                 |

 MDT DB                  ✅                 |   ZTI (Configuration Manager)     ✅

                                                                                        ﾉ   Expand table

 Value            Description

 file_name        Specifies the name of the file that will store the zone information

                                                                                        ﾉ   Expand table

<!-- p.1002 -->

 Example

 [Settings] Priority=Default [Default] DNSZones0FileName=MyNewZone.dns

DNSZonesxMasterIP
A comma delimited list of IP addresses of the main servers to be used by the DNS server
when updating the specified secondary zones. This property must be specified when
configuring a secondary or stub DNS zone.

  ７ Note

  The x in this properties name is a placeholder for a zero-based array that contains
  DNS configurations.

                                                                                   ﾉ   Expand table

 Component              Configured By     |   Scenario                        Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)     ✅

                                                                                   ﾉ   Expand table

 Value           Description

 IP1,IP2         A comma-delimited list of IP addresses of the main servers

                                                                                   ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DNSZones0MasterIP=192.168.0.1,192.168.0.2

DNSZonesxName
Specifies the name of the zone.

  ７ Note

<!-- p.1003 -->

  The x in this properties name is a placeholder for a zero-based array that contains
  DNS configurations.

                                                                                ﾉ   Expand table

 Component             Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value                Description

 name                 Specifies the name of the zone

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DNSZones0Name=MyNewZone

DNSZonesxScavenge
Configures the Primary DNS server to "scavenge" stale records—that is, to search the
database for records that have aged and delete them.

  ７ Note

  The x in this properties name is a placeholder for a zero-based array that contains
  DNS configurations.

                                                                                ﾉ   Expand table

 Component             Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                 |

<!-- p.1004 -->

 Component              Configured By     |   Scenario                      Property Is Applicable

 MDT DB                 ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                  ﾉ   Expand table

 Value            Description

 TRUE             Allow stale DNS records to be scavenged.

 FALSE            Do not allow stale DNS records to be scavenged.

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DNSZones0Scavenge=TRUE

DNSZonesxType
Specifies the type of zone to create.

  ７ Note

  The x in this properties name is a placeholder for a zero-based array that contains
  DNS configurations.

                                                                                  ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                  ﾉ   Expand table

 Value           Description

 DSPrimary       Creates a primary zone and specifying that it should be stored in AD DS on a DNS
                 server configured as a domain controller

<!-- p.1005 -->

 Value           Description

 DSStub          Creates a stub zone and specifying that it should be stored in AD DS on a DNS
                 server configured as a domain controller

 Primary         Creates a primary zone

 Secondary       Creates a secondary zone

 Stub            Creates a stub zone

                                                                                   ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DNSZones0Type=Secondary

DNSZonesxUpdate
Configures the Primary DNS server to perform dynamic updates.

     ７ Note

     The x in this properties name is a placeholder for a zero-based array that contains
     DNS configurations.

                                                                                   ﾉ   Expand table

 Component              Configured By       |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                   |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                   |

 MDT DB                 ✅                   |   ZTI (Configuration Manager)   ✅

                                                                                   ﾉ   Expand table

 Value                Description

 0                    Does not allow dynamic updates

 1                    Allows dynamic updates

 2                    Allows secure dynamic updates

<!-- p.1006 -->

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DNSZones0Update=1

DoCapture
Indicator of whether an image of the target computer is to be captured. If it is, Sysprep
is run on the target computer to prepare for image creation. After Sysprep has run, a
new WIM image is created and stored in the folder within the shared folder designated
for target computer backups (BackupDir and BackupShare, respectively).

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                               ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value      Description

 YES        Copy the necessary files to run Sysprep on the target computer, run Sysprep on the
            target computer, and capture a WIM image.

 NO         Do not run Sysprep on the target computer, and do not capture a WIM image.

 PREPARE    Copy the necessary files to run Sysprep on the target computer, but do not run
            Sysprep or other image-capture processes.

 SYSPREP    Copy the necessary files to run Sysprep on the target computer, run Sysprep on the
            target computer, but do not capture a WIM image.

            Note:

<!-- p.1007 -->

 Value      Description

            The primary purpose of this value is to allow the creation of a VHD that contains an
            operating system after Sysprep has been run and no image capture is necessary.

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DoCapture=YES DeployRoot=\\NYC-AM-FIL-01\Distribution$
 ResourceRoot=\\NYC-AM-FIL-01\Resource$ UDShare=\\NYC-AM-FIL-01\MigData$
 UDDir=%OSDComputerName%

DomainAdmin
The user account credentials used to join the target computer to the domain specified in
JoinDomain. Specify as UserName.

  ７ Note

  For ZTI, the credentials that Configuration Manager specifies typically are used. If
  the DomainAdmin property is specified, the credentials in the DomainAdmin
  property override the credentials that Configuration Manager specifies.

                                                                                 ﾉ   Expand table

 Component            Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)    ✅

                                                                                 ﾉ   Expand table

 Value                      Description

 domain_admin               The name of the user account credentials

                                                                                 ﾉ   Expand table

<!-- p.1008 -->

 Example

 [Settings] Priority=Default [Default] DomainAdmin=NYCAdmin DomainAdminDomain=WOODGROVEBANK
 DomainAdminPassword=<complex_password>

DomainAdminDomain
The domain in which the user's credentials specified in DomainAdmin reside.

  ７ Note

  For ZTI, the credentials that Configuration Manager specifies typically are used. If
  the DomainAdmin property is specified, the credentials in the DomainAdmin
  property override the credentials that Configuration Manager specifies.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                    Description

 domain_admin_domain      The name of the domain where the user account credentials reside

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DomainAdmin=NYCAdmin DomainAdminDomain=WOODGROVEBANK
 DomainAdminPassword=<complex_password>

DomainAdminPassword
The password used for the domain Administrator account specified in the
DomainAdmin property to join the computer to the domain.

<!-- p.1009 -->

  ７ Note

  For ZTI, the credentials that Configuration Manager specifies typically are used. If
  the DomainAdmin property is specified, the credentials in the DomainAdmin
  property override the credentials that Configuration Manager specifies.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                    Description

 domain_admin_password    The password for the domain Administrator account on the target
                          computer

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DomainAdmin=NYCAdmin DomainAdminDomain=WOODGROVEBANK
 DomainAdminPassword=<complex_password>

DomainLevel
This entry specifies the domain functional level. This entry is based on the levels that
exist in the forest when a new domain is created in an existing forest.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

<!-- p.1010 -->

                                                                               ﾉ   Expand table

 Value       Description

 Level       Sets the domain functional level to one of the following:

             - 2, Windows Server 2003

             - 3, Windows Server 2008

             - 4, Windows Server 2008 R2

             - 5, Windows Server 2012

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DomainLevel=3

DomainNetBiosName
Assigns a NetBIOS name to the new domain.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value           Description

 Name            Assigns a NetBIOS name to the new domain

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DomainNetBiosName=NewDom

<!-- p.1011 -->

DomainOUs
A list of AD DS organizational units (OUs) where the target computer account can be
created. The DomainOUs property lists text values that can be any non-blank value. The
DomainOUs property has a numeric suffix (for example, DomainOUs1 or DomainOUs2).
The values specified by DomainOUs will be displayed in the Deployment Wizard and
selectable by the user. The MachineObjectOU property will then be set to the OU
selected.

In addition, the same functionality can be provided by configuring the
DomainOUList.xml file. The format of the DomainOUList.xml file is as follows:

  XML

  <?xml version="1.0" encoding="utf-8"?>
  <DomainOUs>
  <DomainOU>
    OU=Computers,OU=Tellers,OU=NYC,DC=WOODGROVEBANK,DC=Com
  </DomainOU>
  <DomainOU>
    OU=Computers,OU=Managers,OU=NYC,DC=WOODGROVEBANK,DC=Com
  </DomainOU>
  </DomainOUs>

                                                                              ﾉ   Expand table

 Component            Configured By   |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅               |

 MDT DB               ❌               |   ZTI (Configuration Manager)    ❌

                                                                              ﾉ   Expand table

 Value      Description

 OU         The OU in which the target computer account can be created

                                                                              ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSInstall=Y DomainOUs1=OU=Computers, OU=Tellers,
 OU=NYC, DC=WOODGROVEBANK, DC=Com DomainOUs2=OU=Computers, OU=Managers, OU=NYC,

<!-- p.1012 -->

 Example

 DC=WOODGROVEBANK, DC=Com

DoNotCreateExtraPartition
Specifies that deployments of Windows 7 and Windows Server 2008 R2 will not create
the 300 MB system partition.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                                  ﾉ   Expand table

 Component               Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ✅                 |

 MDT DB                  ✅                 |   ZTI (Configuration Manager)   ❌

                                                                                  ﾉ   Expand table

 Value           Description

 YES             The additional system partition will not be created.

 NO              The additional system partition will be created.

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSInstall=Y DoNotCreateExtraPartition=YES

  ７ Note

  Do not use this property in conjunction with properties to configure BitLocker
  settings.

<!-- p.1013 -->

DoNotFormatAndPartition
This property is used to configure whether MDT performs any of the partitioning and
formatting task sequence steps in task sequences created using the MDT task sequence
templates.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                                 ﾉ   Expand table

 Component             Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)   ❌

                                                                                 ﾉ   Expand table

 Value           Description

 YES             The partitioning and formatting task sequence steps in an MDT task sequence will
                 be performed.

 Any other       The partitioning and formatting task sequence steps in an MDT task sequence will
 value           not be performed. This is the default value.

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSInstall=YES SkipUserData=YES
 USMTOfflineMigration=TRUE DoNotFormatAndPartition=YES OSDStateStorePath=\\WDG-MDT-
 01\StateStore$

DriverGroup
A list of text values that associates out-of-box drivers created in the Deployment
Workbench with each other (typically based on the make and model of a computer). A

<!-- p.1014 -->

driver can be associated with one or more driver groups. The DriverGroup property
allows the drivers within one or more groups to be deployed to a target computer.

The text values in the list can be any non-blank value. The DriverGroup property value
has a numeric suffix (for example, DriverGroup001 or DriverGroup002). After it is
defined, a driver group is associated with a computer. A computer can be associated
with more than one driver group.

For example, there are two sections for each of the computer manufacturers [Mfgr01]
and [Mfgr02]. Two driver groups are defined for the manufacturer Mfgr01: Mfgr01 Video
Drivers and Mfgr01 Network Drivers. For the manufacturer Mfgr02, one driver group is
defined, Mfgr02 Drivers. One driver group, Shared Drivers, is applied to all computers
found in the [Default] section.

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ❌

                                                                             ﾉ   Expand table

 Value                 Description

 driver_group_name     The name of the driver group defined in the Deployment Workbench

                                                                             ﾉ   Expand table

 Example

 [Settings] Priority=Make, Default [Default] DriverGroup001=Shared Drivers :: [Mfgr01]
 DriverGroup001=Mfgr01 Video Drivers DriverGroup002=Mfgr01 Network Drivers [Mfgr02]
 DriverGroup001=Mfgr02 Drivers

DriverInjectionMode
This property is used to control the device drivers that are injected by the Inject Drivers
task sequence step.

                                                                             ﾉ   Expand table

<!-- p.1015 -->

 Component             Configured By        |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                    |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                    |

 MDT DB                ✅                    |   ZTI (Configuration Manager)   ❌

                                                                                   ﾉ   Expand table

 Value   Description

 Auto    Inject only matching drivers from the selection profile or folder. This is the same behavior
         as MDT 2008, which injects all drivers that matched one of the plug and play (PnP)
         identifiers (IDs) on the target computer.

 All     Inject all drivers in the selection profile or folder.

                                                                                   ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DriverInjectionMode=ALL DriverSelectionProfile=Nothing
 DriverPaths001=\\NYC-AM-FIL-01\Drivers$ DriverPaths002=\\NYC-AM-FIL-03\WinDrvs

DriverPaths
A list of UNC paths to shared folders where additional device drivers are located. These
device drivers are installed with the target operating system on the target computer.
The MDT scripts copy the contents of these folders to the C:\Drivers folder on the target
computer. The DriverPaths property is a list of text values that can be any non-blank
value. The DriverPaths property has a numeric suffix (for example, DriverPaths001 or
DriverPaths002).

                                                                                   ﾉ   Expand table

 Component             Configured By        |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                    |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                    |

 MDT DB                ❌                    |   ZTI (Configuration Manager)   ❌

                                                                                   ﾉ   Expand table

<!-- p.1016 -->

 Value           Description

 UNC_path        UNC path to the shared folder in which the additional drivers reside

                                                                                  ﾉ     Expand table

 Example

 [Settings] Priority=Default [Default] DriverPaths001=\\NYC-AM-FIL-01\Drivers$
 DriverPaths002=\\NYC-AM-FIL-03\Win8Drvs

DriverSelectionProfile
Profile name used during driver installation.

                                                                                  ﾉ     Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ❌

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ✅

                                                                                  ﾉ     Expand table

 Value                                               Description

 profile_name                                        None

                                                                                  ﾉ     Expand table

 Example

 [Settings] Priority=Default [Default] DriverSelectionProfile=MonitorDrivers

EventService
The EventService property specifies the URL where the MDT monitoring service is
running. By default, the service uses TCP port 9800 to communicate. The MDT
monitoring service collects deployment information on the deployment process that can
be viewed in the Deployment Workbench and using the Get-MDTMonitorData cmdlet.

<!-- p.1017 -->

                                                                               ﾉ   Expand table

 Component             Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                |

 MDT DB                ✅                |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                Description

 url_path             The URL to the MDT monitoring service.

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] EventService=https://WDG-MDT-01:9800 DeployRoot=\\NYC-
 AM-FIL-01\Distribution$ ResourceRoot=\\NYC-AM-FIL-01\Resource$

EventShare
The EventShare property points to a shared folder in which the MDT scripts record
events.

By default, the shared folder is created in C:\Events.

                                                                               ﾉ   Expand table

 Component             Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                |

 MDT DB                ✅                |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value       Description

 UNC_path    The UNC path to the shared folder in which the MDT scripts record events. The
             default share name is Events.

<!-- p.1018 -->

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] EventShare=\\NYC-AM-FIL-01\Events DeployRoot=\\NYC-AM-
 FIL-01\Distribution$ ResourceRoot=\\NYC-AM-FIL-01\Resource$

FinishAction
Specifies the action to be taken when an LTI task sequence finishes, which is after the
Summary wizard page in the Deployment Wizard.

   Tip

  Use this property in conjunction with the SkipFinalSummary property to skip the
  Summary wizard page in the Deployment Wizard and automatically perform the
  action.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                                ﾉ   Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                |

 MDT DB                 ✅                |   ZTI (Configuration Manager)   ❌

                                                                                ﾉ   Expand table

 Value    Description

 action   Where action is one of the following:

          - SHUTDOWN. Shuts down the target computer.

          - REBOOT. Restarts the target computer.

<!-- p.1019 -->

 Value    Description

          - RESTART. Same as REBOOT.

          - LOGOFF. Log off the current user. If the target computer is currently running Windows
          PE, then the target computer will be restarted.

          - blank. Exit the Deployment Wizard without performing any additional actions. This is
          the default setting.

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] FinishAction=REBOOT

ForceApplyFallback
Controls the method used for installed Windows:

     setup.exe. This method is the traditional method, initiated by running setup.exe
     from the installation media. MDT uses this method by default.

     imagex.exe. This method installs the operating system image using imagex.exe
     with the /apply option. MDT uses this method when the setup.exe method cannot
     be used (i.e., MDT falls back to using imagex.exe).

     Besides controlling the method used to install these operating systems, this
     property affects which operating system task sequences are listed in the
     Deployment Wizard for a specific processor architecture boot image. When the
     value of this property is set to NEVER, only operating system task sequences that
     match the processor architecture of the boot image are displayed. If the value of
     this property is set to any other value or is blank, all task sequences that can use
     the imagex.exe installation method are shown, regardless of the processor
     architecture.

                                                                                 ﾉ   Expand table

 Component              Configured By   |   Scenario                       Property Is Applicable

 BootStrap.ini          ❌               |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini     ✅               |

 MDT DB                 ✅               |   ZTI (Configuration Manager)    ❌

<!-- p.1020 -->

                                                                               ﾉ   Expand table

 Value                Description

 NEVER                MDT always uses the imagex.exe method if necessary. Only task sequences
                      that deploy an operating system that matches the boot image are displayed
                      in the Deployment Wizard.

 Any other value,     Any task sequence that supports the imagex.exe method is displayed in the
 including blank      Deployment Wizard.

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSInstall=YES ForceApplyFallback=NEVER

ForestLevel
This entry specifies the forest functional level when a new domain is created in a new
forest.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value       Description

 level       Sets the domain functional level to one of the following:

             - 2, Windows Server 2003

             - 3, Windows Server 2008

             - 4, Windows Server 2008 R2

             - 5, Windows Server 2012

<!-- p.1021 -->

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] ForestLevel=3

FullName
The full name of the user of the target computer provided during the installation of the
operating system. This value is inserted into the appropriate configuration settings in
Unattend.xml.

  ７ Note

  This value is different from the user credentials created after the operating system
  is deployed. The FullName property is provided as information to systems
  administrators about the user running applications on the target computer.

                                                                                ﾉ   Expand table

 Component             Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value                Description

 full_name            The full name of the user of the target computer

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=MACAddress, Default Properties=CustomProperty, ApplicationInstall
 [Default] CustomProperty=TRUE OrgName=Woodgrove Bank [00:0F:20:35:DE:AC]
 OSDNEWMACHINENAME=HPD530-1 ApplicationInstall=Custom FullName=Woodgrove Bank User
 [00:03:FF:FE:FF:FF] OSDNEWMACHINENAME=BVMXP ApplicationInstall=Minimum FullName=Woodgrove
 Bank Manager

<!-- p.1022 -->

GPOPackPath
This property is used to override the default path to the folder in which the GPO packs
reside. The path specified in this property is relative to the Templates\GPOPacks folder in
a distribution share. MDT automatically scans a specific subfolder of this folder based on
the operating system being deployed to the target computer, such as
Templates\GPOPacks\operating_system (where operating_system is the operating system
being deployed). Table 3 list the supported operating systems and the subfolders that
correspond to each operating system.

Table 3. Windows Operating Systems and Corresponding GPO Pack
Subfolder

                                                                                 ﾉ   Expand table

 Operating system                              GPO pack subfolder

 Windows 7 with SP1                            Win7SP1-MDTGPOPack

 Windows Server 2008 R2                        WS2008R2SP1-MDTGPOPack

                                                                                 ﾉ   Expand table

 Component             Configured By    |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                |

 MDT DB                ✅                |   ZTI (Configuration Manager)    ❌

                                                                                 ﾉ   Expand table

 Value   Description

 path    The path relative to the distribution_share\Templates\GPOPacks folder (where
         distribution_share is the root folder of the distribution share. The default value is the
         distribution_share\Templates\GPOPacks\operating_system folder (where operating_system
         is a subfolder based on the operating system version).

         In the example below, setting the GPOPackPath property to a value of "Win7-
         HighSecurity" configures MDT to use the distribution_share\Templates\GPOPacks\Win7-
         HighSecurity folder as the folder where the GPO packs are stored.

<!-- p.1023 -->

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] GPOPackPath=Win7-HighSecurity

Groups
The list of local groups on the target computer whose membership will be captured.
This group membership is captured during the State Capture Phase and is restored
during the State Restore Phase. (The default groups are Administrators and Power
Users.) The Groups property is a list of text values that can be any non-blank value. The
Groups property has a numeric suffix (for example, Groups001 or Groups002).

                                                                               ﾉ   Expand table

 Component             Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                |

 MDT DB                ❌                |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value           Description

 group_name      The name of the local group on the target computer for which group membership
                 will be captured

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DeployRoot=\\NYC-AM-FIL-01\Distribution$
 ResourceRoot=\\NYC-AM-FIL-01\Resource$ UDShare=\\NYC-AM-FIL-01\MigData$ CaptureGroups=YES
 Groups001=NYC Application Management Groups002=NYC Help Desk Users

HideShell
This property controls the display of Windows Explorer while the LTI task sequence is
running in the new operating system on the target computer. This property can be used
in conjunction with the DisableTaskMgr property.

<!-- p.1024 -->

  ７ Note

  This property can be used with the DisableTaskMgr property to help prevent users
  from interrupting the LTI task sequence. For more information, see the
  DisableTaskMgr property.

                                                                                    ﾉ   Expand table

 Component              Configured By     |   Scenario                        Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)     ❌

                                                                                    ﾉ   Expand table

 Value    Description

 YES      Windows Explorer is hidden until the task sequence is complete.

 NO       Windows Explorer is visible while the task sequence is running. This is the default value.

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DisableTaskMgr=YES HideShell=YES

Home_Page
The URL to be used as the Windows Internet Explorer® home page after the target
operating system is deployed.

                                                                                    ﾉ   Expand table

 Component              Configured By     |   Scenario                        Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)     ✅

<!-- p.1025 -->

                                                                                ﾉ   Expand table

 Value   Description

 URL     The URL of the web page to be used as the home page for Internet Explorer on the target
         computer

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] Home_Page=https://portal.woodgrovebank.com

HostName
The IP host name of the target computer (the name assigned to the target computer).

  ７ Note

  This is the computer name of the target computer, not the NetBIOS computer
  name of the target computer. The NetBIOS computer name can be shorter than the
  computer name. Also, this property is dynamically set by MDT scripts and cannot
  have its value set in CustomSettings.ini or the MDT DB. Treat this property as read
  only. However, you can use this property within CustomSettings.ini or the MDT DB,
  as shown in the following examples, to aid in defining the configuration of the
  target computer.

                                                                                ﾉ   Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌                |

 MDT DB                 ❌                |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value                 Description

 host_name             The IP host name assigned to the target computer

<!-- p.1026 -->

                                                                                ﾉ   Expand table

 Example

 None

ImagePackageID
The package ID used for the operating system to install during OEM deployments.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                ﾉ   Expand table

 Component               Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ❌               |

 MDT DB                  ❌               |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value     Description

 None      The package ID used for the operating system to install during OEM deployments

                                                                                ﾉ   Expand table

 Example

 None

InputLocale
A list of input locales to be used with the target operating system. More than one input
locale can be specified for the target operating system. Each locale must be separated
by a semicolon (;). If not specified, the Deployment Wizard uses the input locale
configured in the image being deployed.

<!-- p.1027 -->

Exclude this setting in the Windows User State Migration Tool (USMT) when backing up
and restoring user state information. Otherwise, the settings in the user state
information will override the values specified in the InputLocale property.

                                                                               ﾉ   Expand table

 Component             Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅               |

 MDT DB                ✅               |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                          Description

 input_locale1; input_locale2   The locale for the keyboard attached to the target computer

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] UserLocale=en-us
 InputLocale=0409:00000409;0413:00020409;0413:00000409;0409:00020409

InstallPackageID
The package ID used for the operating system to install during OEM deployments.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                               ﾉ   Expand table

 Component             Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ❌               |

<!-- p.1028 -->

 Component               Configured By   |   Scenario                      Property Is Applicable

 MDT DB                  ❌               |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value     Description

 None      The package ID used for the operating system to install during OEM deployments

                                                                                ﾉ   Expand table

 Example

 None

Instance
The instance of SQL Server used for querying property values from columns in the table
specified in the Table property. The database resides on the computer specified in the
SQLServer property. The instance of SQL Server on the computer is specified in the
Instance property.

                                                                                ﾉ   Expand table

 Component               Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini           ✅               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ✅               |

 MDT DB                  ✅               |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value                               Description

                                     instance

                                                                                ﾉ   Expand table

<!-- p.1029 -->

 Example

 [Settings] Priority=Computers, Default [Default] OSInstall=YES [Computers] SQLServer=NYC-
 SQL-01 Database=MDTDB Instance=SQLEnterprise2005 Table=Computers Parameters=SerialNumber,
 AssetTag ParameterCondition=OR

IPAddress
The IP address of the target computer. The format of the IP address returned by the
property is standard dotted-decimal notation; for example, 192.168.1.1. Use this
property to create a subsection that contains settings targeted to a specific target
computer based on the IP address.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                 ﾉ   Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌                |

 MDT DB                 ❌                |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value           Description

 ip_address      The IP address of the target computer in standard dotted-decimal notation

                                                                                 ﾉ   Expand table

 Example

 None

IsDesktop

<!-- p.1030 -->

Indicator of whether the computer is a desktop, because the Win32_SystemEnclosure
ChassisType property value is 3, 4, 5, 6, 7, 15, 16, 35, or 36.

  ７ Note

  Only one of the following properties will be true at a time: IsDesktop, IsLaptop,
  IsServer.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                               ﾉ   Expand table

 Component             Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ❌                |

 MDT DB                ❌                |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value           Description

 TRUE            The target computer is a desktop computer.

 FALSE           The target computer is not a desktop computer.

                                                                               ﾉ   Expand table

 Example

 None

IsHypervisorRunning
Specifies whether a hypervisor is present on the target computer. This property is set
using information from the CPUID interface.

<!-- p.1031 -->

For further information collected about VMs and information returned from the CPUID
interface, see the following properties:

     IsVM

     SupportsHyperVRole

     SupportsNX

     SupportsVT

     Supports64Bit

     VMPlatform

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

  ７ Note

  The IsVM property should be used to determine whether the target computer is a
  virtual or physical machine.

                                                                              ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ❌                |

 MDT DB               ❌                |   ZTI (Configuration Manager)   ✅

                                                                              ﾉ   Expand table

 Value                Description

 TRUE                 A hypervisor is detected.

 FALSE                A hypervisor is not detected.

                                                                              ﾉ   Expand table

<!-- p.1032 -->

 Example

 None

IsLaptop
Indicator of whether the computer is a portable computer, because the
Win32_SystemEnclosure ChassisType property value is 8, 9, 10, 11, 12, 14, 18, 21, 30, 31,
or 32.

  ７ Note

  Only one of the following properties will be true at a time: IsDesktop, IsLaptop,
  IsServer.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                ﾉ   Expand table

 Component             Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ❌                 |

 MDT DB                ❌                 |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value           Description

 TRUE            The target computer is a portable computer.

 FALSE           The target computer is not a portable computer.

                                                                                ﾉ   Expand table

<!-- p.1033 -->

 Example

 None

IsServer
Indicator of whether the computer is a server, because the Win32_SystemEnclosure
ChassisType property value is 23 or 28.

                                                                                  ﾉ   Expand table

 Component              Configured By      |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                  |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌                  |

 MDT DB                 ❌                  |   ZTI (Configuration Manager)   ✅

                                                                                  ﾉ   Expand table

 Value                Description

 TRUE                 The target computer is a server.

 FALSE                The target computer is not a server.

                                                                                  ﾉ   Expand table

 Example

 None

IsServerCoreOS
Indicator of whether the current operating system running on the target computer is the
Server Core installation option of the Windows Server operating system.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

<!-- p.1034 -->

                                                                                 ﾉ   Expand table

 Component              Configured By   |   Scenario                       Property Is Applicable

 BootStrap.ini          ❌               |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini     ❌               |

 MDT DB                 ❌               |   ZTI (Configuration Manager)    ✅

                                                                                 ﾉ   Expand table

 Value    Description

 TRUE     The operating system on the target computer is the Server Core installation option of
          Windows Server.

 FALSE    The operating system on the target computer is not the Server Core installation option of
          Windows Server.

                                                                                 ﾉ   Expand table

 Example

 None

IsServerOS
Indicator of whether the current operating system running on the target computer is a
server operating system.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                 ﾉ   Expand table

 Component              Configured By   |   Scenario                       Property Is Applicable

 BootStrap.ini          ❌               |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini     ❌               |

 MDT DB                 ❌               |   ZTI (Configuration Manager)    ✅

<!-- p.1035 -->

                                                                                ﾉ      Expand table

 Value     Description

 TRUE      The operating system on the target computer is a server operating system.

 FALSE     The operating system on the target computer is not a server operating system.

                                                                                ﾉ      Expand table

 Example

 None

IsUEFI
Specifies whether the target computer is currently running with Unified Extensible
Firmware Interface (UEFI). The UEFI is a specification that defines a software interface
between an operating system and platform firmware. UEFI is a more secure replacement
for the older BIOS firmware interface present in some personal computers. For more
information on UEFI, go to https://uefi.org       .

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                ﾉ      Expand table

 Component              Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌               |

 MDT DB                 ❌               |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ      Expand table

 Value    Description

 TRUE     The target computer is currently running with UEFI.

<!-- p.1036 -->

 Value   Description

 FALSE   The target computer is not currently running with UEFI.

         Note:

         It is possible that the target computer may support UEFI, but is running in a compatibility
         mode that emulates the older BIOS firmware interface. In this situation this value of this
         property will set to FALSE even though the target computer supports UEFI.

                                                                                  ﾉ   Expand table

 Example

 None

IsVM
Specifies whether the target computer is a VM based on information gathered from the
CPUID interface. You can determine the specific VM environment using the VMPlatform
property.

For further information collected about VMs and information returned from the CPUID
interface, see the following properties:

     IsHypervisorRunning

     SupportsHyperVRole

     SupportsNX

     SupportsVT

     Supports64Bit

     VMPlatform

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                  ﾉ   Expand table

<!-- p.1037 -->

 Component             Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ❌                 |

 MDT DB                ❌                 |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value                Description

 TRUE                 The target computer is a VM.

 FALSE                The target computer is not a VM.

                                                                                ﾉ   Expand table

 Example

 None

JoinDomain
The domain that the target computer joins after the target operating system is
deployed. This is the domain where the computer account for the target computer is
created. The JoinDomain property can contain alphanumeric characters, hyphens (-),
and underscores (_). The JoinDomain property cannot be blank or contain spaces.

                                                                                ﾉ   Expand table

 Component             Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value                  Description

 domain_name            The name of the domain that the target computer joins

<!-- p.1038 -->

                                                                             ﾉ     Expand table

 Example

 [Settings] Priority=Default [Default] JoinDomain=WOODGROVEBANK
 MachineObjectOU=OU=Reception,OU=NYC,DC=Woodgrovebank,DC=com

JoinWorkgroup
The workgroup that the target computer joins after the target operating system is
deployed. The JoinWorkgroup property can contain alphanumeric characters, hyphens
(-), and underscores (_). The JoinWorkgroup property cannot be blank or contain
spaces.

                                                                             ﾉ     Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ✅

                                                                             ﾉ     Expand table

 Value                  Description

 workgroup_name         The name of the workgroup that the target computer joins

                                                                             ﾉ     Expand table

 Example

 [Settings] Priority=Default [Default] JoinWorkgroup=WDGV_WORKGROUP

KeyboardLocale
A list of keyboard locales to be used with the target operating system. More than one
keyboard locale can be specified for the target operating system. Each locale must be
separated by a semicolon (;). If not specified, the Deployment Wizard uses the keyboard
locale configured in the image being deployed.

<!-- p.1039 -->

Exclude this setting in USMT when backing up and restoring user state information.
Otherwise, the settings in the user state information will override the values specified in
the KeyboardLocale property.

  ７ Note

  For this property to function properly, it must be configured in both
  CustomSettings.ini and BootStrap.ini. BootStrap.ini is processed before a
  deployment share (which contains CustomSettings.ini) has been selected.

                                                                                 ﾉ   Expand table

 Component            Configured By    |   Scenario                        Property Is Applicable

 BootStrap.ini        ✅                |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)     ✅

                                                                                 ﾉ   Expand table

 Value                                Description

 keyboard_locale1; keyboard_locale2   The locale of the keyboard attached to the target computer.

                                      The value can be specified in the following formats:

                                      - Text (en-us)

                                      - Hexadecimal (0409:00000409)

                                                                                 ﾉ   Expand table

 Example 1

 [Settings] Priority=Default [Default] UserLocale=en-us KeyboardLocale=en-us

                                                                                 ﾉ   Expand table

 Example 2

 [Settings] Priority=Default [Default] UserLocale=en-us
 KeyboardLocale=0409:00000409;1809:00001809;041A:0000041A;083b:0001083b

<!-- p.1040 -->

KeyboardLocalePE
The name of the keyboard locale to be used while in Windows PE only.

  ７ Note

  For this property to function properly, it must be configured in both
  CustomSettings.ini and BootStrap.ini. BootStrap.ini is processed before a
  deployment share (which contains CustomSettings.ini) has been selected.

                                                                                   ﾉ   Expand table

 Component            Configured By     |   Scenario                          Property Is Applicable

 BootStrap.ini        ✅                 |   LTI (Stand-alone MDT)             ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)       ✅

                                                                                   ﾉ   Expand table

 Value                 Description

 keyboard_locale       The locale of the keyboard attached to the target computer.

                       The value can be specified in the following formats:

                       - Text (en-us)

                       - Hexadecimal (0409:00000409)

                                                                                   ﾉ   Expand table

 Example 1

 [Settings] Priority=Default [Default] KeyboardLocalePE=en-us

                                                                                   ﾉ   Expand table

 Example 2

 [Settings] Priority=Default [Default] KeyboardLocalePE=0409:00000409
