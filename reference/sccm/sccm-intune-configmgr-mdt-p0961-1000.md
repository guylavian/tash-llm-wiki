---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 961-1000"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0961-1000
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0961-1000
family: sccm
documentKind: "doc"
abstract: "ConfirmGC Specifies whether the replica is also a global catalog. Ｕ Caution This property value must be specified in uppercase so that the deployment scripts can read it properly. ﾉ Expand table Component Configured By | Scenario Property Is Applicable BootStrap.ini ❌ | LTI (Sta"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 961-1000

<!-- p.961 -->

ConfirmGC
Specifies whether the replica is also a global catalog.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                                    ﾉ   Expand table

 Component            Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)    ✅

                                                                                    ﾉ   Expand table

 Value     Description

 YES       Makes the replica a global catalog if the backup was a global catalog.

 NO        Does not make the replica a global catalog.

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] ConfirmGC=YES

CountryCode
The country code to be configured for the operating system on the target computer.
This property allows only numeric characters. This value is inserted into the appropriate
configuration settings in Unattend.xml.

                                                                                    ﾉ   Expand table

 Component            Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)          ✅

<!-- p.962 -->

 Component              Configured By    |   Scenario                      Property Is Applicable

 CustomSettings.ini     ✅                |

 MDT DB                 ✅                |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ    Expand table

 Value                Description

 country_code         The country code where the target computer is to be deployed

                                                                                ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] AreaCode=206 CountryCode=001 Dialing=TONE
 LongDistanceAccess=9

CriticalReplicationOnly
Specifies whether the promotion operation performs only critical replication and then
continues, skipping the noncritical (and potentially lengthy) portion of replication.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                                ﾉ    Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                |

 MDT DB                 ✅                |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ    Expand table

 Value            Description

 YES              Skips noncritical replication

<!-- p.963 -->

 Value               Description

 NO                  Does not skip noncritical replication

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] CriticalReplicationOnly=YES

CustomDriverSelectionProfile
Specifies the custom selection profile used during driver installation.

                                                                                  ﾉ   Expand table

 Component               Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ✅                 |

 MDT DB                  ✅                 |   ZTI (Configuration Manager)   ❌

                                                                                  ﾉ   Expand table

 Value           Description

 profile         Custom selection profile used during driver installation

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] CustomDriverSelectionProfile=CustomDrivers

CustomPackageSelectionProfile
Specifies the custom selection profile used during package installation.

                                                                                  ﾉ   Expand table

<!-- p.964 -->

 Component               Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ✅                 |

 MDT DB                  ✅                 |   ZTI (Configuration Manager)   ❌

                                                                                    ﾉ   Expand table

 Value           Description

 profile         Custom selection profile used during package installation

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] CustomPackageSelectionProfile=CustomPackages

CustomWizardSelectionProfile
Specifies the custom selection profile used by the wizard for filtering the display of
various items.

                                                                                    ﾉ   Expand table

 Component               Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ✅                 |

 MDT DB                  ✅                 |   ZTI (Configuration Manager)   ❌

                                                                                    ﾉ   Expand table

 Value     Description

 profile   Custom selection profile by the wizard for filtering the display of various items

                                                                                    ﾉ   Expand table

<!-- p.965 -->

 Example

 [Settings] Priority=Default [Default] CustomWizardSelectionProfile=CustomWizard

Database
The property that specifies the database to be used for querying property values from
columns in the table specified in the Table property. The database resides on the
computer specified in the SQLServer property. The instance of Microsoft SQL Server®
on the computer is specified in the Instance property.

                                                                                ﾉ   Expand table

 Component             Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini         ✅                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ❌                 |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value           Description

 database        The name of the database to be used for querying property values

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Computers, Default [Default] OSInstall=YES [Computers] SQLServer=NYC-
 SQL-01 SQLShare=SQL$ Database=MDTDB Instance=SQLEnterprise2005 Table=Computers
 Parameters=SerialNumber, AssetTag ParameterCondition=OR

DatabasePath
Specifies the fully qualified, non-UNC path to a directory on a fixed disk of the target
computer that contains the domain database.

                                                                                ﾉ   Expand table

<!-- p.966 -->

 Component             Configured By     |   Scenario                         Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)            ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)      ✅

                                                                                    ﾉ   Expand table

 Value   Description

 path    Specifies the fully qualified, non-UNC path to a directory on a fixed disk of the local
         computer that contains the domain database

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DatabasePath=%DestinationLogicalDrive%\Windows\NTSD

DBID
Specifies the user account used to connect to the computer running SQL Server
(specified by the SQLServer property) using SQL Server authentication. The DBPwd
property provides the password for the user account in the DBID property.

  ７ Note

  SQL Server authentication is not as secure as Integrated Windows authentication.
  Integrated Windows authentication is the recommended authentication method.
  Using the DBID and DBPwd properties stores the credentials in clear text in the
  CustomSettings.ini file and therefore is not secure. For more information about
  using Integrated Windows authentication, see the SQLShare property.

  ７ Note

  This property is configurable only by manually editing the CustomSettings.ini and
  BootStrap.ini files.

                                                                                    ﾉ   Expand table

<!-- p.967 -->

 Component               Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini           ✅               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ✅               |

 MDT DB                  ❌               |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value     Description

 user_id   The name of the user account credentials used to access the computer running SQL
           Server using SQL Server authentication

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Computers, Default [Default] OSInstall=YES [Computers] SQLServer=NYC-
 SQL-01 DBID=SQL_User-01 DBPwd=<complex_password> NetLib=DBNMPNTW Database=MDTDB
 Instance=SQLEnterprise2005 Table=Computers Parameters=SerialNumber, AssetTag
 ParameterCondition=OR

DBPwd
Specifies the password for the user account specified in the DBID property. The DBID
and DBPwd properties provide the credentials for performing SQL Server authentication
to the computer running SQL Server (specified by the SQLServer property).

  ７ Note

  SQL Server authentication is not as secure as Integrated Windows authentication.
  Integrated Windows authentication is the recommended authentication method.
  Using the DBID and DBPwd properties stores the credentials in clear text in the
  CustomSettings.ini file and therefore is not secure. For more information about
  using Integrated Windows authentication, see the SQLShare property.

  ７ Note

  This property is configurable only by manually editing the CustomSettings.ini and
  BootStrap.ini files.

<!-- p.968 -->

                                                                                ﾉ   Expand table

 Component            Configured By    |   Scenario                       Property Is Applicable

 BootStrap.ini        ✅                |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅                |

 MDT DB               ❌                |   ZTI (Configuration Manager)    ✅

                                                                                ﾉ   Expand table

 Value           Description

 user_password   The password for the user account credentials specified in the DBID property for
                 using SQL Server authentication

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Computers, Default [Default] OSInstall=YES [Computers] SQLServer=NYC-
 SQL-01 DBID=SQL_User-01 DBPwd=<complex_password> NetLib=DBNMPNTW Database=MDTDB
 Instance=SQLEnterprise2005 Table=Computers Parameters=SerialNumber, AssetTag
 ParameterCondition=OR

Debug
Controls the verbosity of messages written to the MDT log files. This property can be
configured to help assist in troubleshooting deployments by providing extended
information about the MDT deployment process.

You can set this property by starting the LiteTouch.vbs script with the /debug:true
command-line parameter as follows:

  Windows Command Prompt

  cscript.exe LiteTouch.vbs /debug:true

After the LiteTouch.vbs script is started, the Debug property's value is set to TRUE, and
all other scripts are automatically read the value of this property and provide verbose
information.

  ７ Note

<!-- p.969 -->

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or in the MDT DB. Treat this property as read only.

                                                                                   ﾉ   Expand table

 Component               Configured By      |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌                  |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ❌                  |

 MDT DB                  ❌                  |   ZTI (Configuration Manager)   ✅

                                                                                   ﾉ   Expand table

 Value           Description

 TRUE            Debug logging is enabled, which includes the following:

                 - Verbose messages are logged.

                 - Deprecated messages are logged as errors.

 FALSE           Debug logging is not enabled. This is the default value.

                                                                                   ﾉ   Expand table

 Example

 None

DefaultGateway
The IP address of the default gateway being used by the target computer. The format of
the IP address returned by the property is standard dotted-decimal notation; for
example, 192.168.1.1. Use this property to create a subsection that contains settings
targeted to a group of computers based on the IP subnets on which they are located.

  ７ Note

  This property is dynamically set by MDT scripts and cannot have its value set in
  CustomSettings.ini or the MDT DB. Treat this property as read only. However, you

<!-- p.970 -->

  can use this property within CustomSettings.ini or the MDT DB, as shown in the
  following examples, to aid in defining the configuration of the target computer.

                                                                                 ﾉ   Expand table

 Component             Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value                Description

 default_gateway      The IP address of the default gateway in standard dotted-decimal notation

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=DefaultGateway, Default [Default] OSInstall=YES [DefaultGateway]
 192.168.0.1=HOUSTON 11.1.1.11=REDMOND 172.28.20.1=REDMOND [REDMOND]
 Packages001=XXX00004:Program4 Packages002=XXX00005:Program5 [HOUSTON]
 Packages001=XXX00006:Program6 Packages002=XXX00007:Program7 Packages003=XXX00008:Program8

DeployDrive
The value used by the scripts to access files and run programs in the deployment share
that the Deployment Workbench creates. The property returns the drive letter mapped
to the DeployRoot property. ZTIApplications.wsf uses the DeployDrive property when
running any command-line programs with a .cmd or .bat extension.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                 ﾉ   Expand table

<!-- p.971 -->

 Component               Configured By     |   Scenario                        Property Is Applicable

 BootStrap.ini           ❌                 |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini      ❌                 |

 MDT DB                  ❌                 |   ZTI (Configuration Manager)     ✅

                                                                                     ﾉ   Expand table

 Value           Description

 drive_letter    The letter designation for the logical drive where the target operating system is to
                 be installed (such as C or D)

                                                                                     ﾉ   Expand table

 Example

 None

DeploymentMethod
The method being used for the deployment (UNC, media, or Configuration Manager).

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                                     ﾉ   Expand table

 Component               Configured By     |   Scenario                        Property Is Applicable

 BootStrap.ini           ❌                 |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini      ❌                 |

<!-- p.972 -->

 Component               Configured By   |   Scenario                      Property Is Applicable

 MDT DB                  ❌               |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value     Description

 UNC       The deployment is made to the target computer over the network.

 Media     The deployment is made from local media (such as DVD or hard disk) at the target
           computer.

 SCCM      ZTI uses this method for Configuration Manager.

                                                                                ﾉ   Expand table

 Example

 None

DeploymentType
The type of deployment being performed based on the deployment scenario. For ZTI,
this property is set dynamically by MDT scripts and is not configured in
CustomSettings.ini. For LTI, you can bypass the page in the Deployment Wizard on
which the deployment type is selected. In addition, you can specify the deployment type
by passing one of the values listed below to the LiteTouch.wsf script as a command-line
option.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                                ﾉ   Expand table

 Component               Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ✅               |

 MDT DB                  ❌               |   ZTI (Configuration Manager)   ✅

<!-- p.973 -->

                                                                              ﾉ   Expand table

 Value             Description

 NEWCOMPUTER       The target computer is a new computer that has never been a member of the
                   network.

 REFRESH           The target computer is an existing computer on the network that needs the
                   desktop environment standard to be redeployed.

 REPLACE           An existing computer on the network is being replaced with a new computer.
                   The user state migration data is transferred from the existing computer to a
                   new computer.

                                                                              ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DeploymentType=NEWCOMPUTER

DeployRoot
Specifies the UNC or local path to the folder that is the root of the folder structure that
MDT uses. This folder structure contains configuration files, scripts, and other folders
and files that MDT uses. The value of this property is set based on the following MDT
deployment technologies:

     LTI. This property is the UNC path to the deployment share that the Deployment
     Workbench creates. Use this property to select a specific deployment share. The
     most common use of this property is in the BootStrap.ini file to identify a
     deployment share before the connection to the deployment share is established.
     All other deployment share folders are relative to this property (such as device
     drivers, language packs, or operating systems).

     ZTI. This property is the local path to the folder to which the MDT files package is
     copied. The Use Toolkit Package task sequence step copies the MDT files package
     to a local folder on the target computer, and then automatically sets this property
     to the local folder.

         ７ Note

<!-- p.974 -->

         For ZTI, this property is dynamically set by the MDT scripts and is not
         configured in CustomSettings.ini or in the MDT DB. Treat this property as read
         only.

                                                                                ﾉ   Expand table

 Component             Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini         ✅                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ❌                 |

 MDT DB                ❌                 |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value                Description

 path                 The UNC or local path to the .

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DeployRoot=\\NYC-AM-FIL-01\Distribution$
 UserDataLocation=NONE

DestinationDisk
Disk number that the image will be deployed to.

                                                                                ﾉ   Expand table

 Component             Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini         ✅                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ❌                 |   ZTI (Configuration Manager)   ❌

                                                                                ﾉ   Expand table

<!-- p.975 -->

 Value                Description

 disk_number          The number of the disk to which the image will be deployed

                                                                                   ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DestinationDisk=0

DestinationLogicalDrive
The logical drive to which the image will be deployed.

                                                                                   ﾉ   Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ✅                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                |

 MDT DB                 ❌                |   ZTI (Configuration Manager)   ❌

                                                                                   ﾉ   Expand table

 Value                         Description

 logical_drive_number          The logical drive to which the image will be deployed

                                                                                   ﾉ   Expand table

 Example 1

 [Settings] Priority=Default [Default] DestinationLogicalDrive=0

                                                                                   ﾉ   Expand table

 Example 2

 [Settings] Priority=Default [Default] DestinationLogicalDrive=0

 [Settings] Priority=Default [Default] InstallDNS=YES DomainNetBIOSName=WoodGroveBank
 NewDomain=Child DomainLevel=3 ForestLevel=3 NewDomainDNSName=newdom.WoodGroveBank.com
 ParentDomainDNSName=WoodGroveBank.com AutoConfigDNS=YES ConfirmGC=YES

<!-- p.976 -->

 Example 2

 CriticalReplicationOnly=NO ADDSUserName=Administrator ADDSUserDomain=WoodGroveBank
 ADDSPassword=<complex_password> DatabasePath=%DestinationLogicalDrive%\Windows\NTDS
 ADDSLogPath=%DestinationLogicalDrive%\Windows\NTDS
 SysVolPath=%DestinationLogicalDrive%\Windows\SYSVOL SafeModeAdminPassword=<complex_password>

DestinationPartition
Disk partition to which the image will be deployed.

                                                                               ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ✅                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                |

 MDT DB               ❌                |   ZTI (Configuration Manager)   ❌

                                                                               ﾉ   Expand table

 Value                 Description

 partition_number      The number of the partition to which the image will be deployed

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DestinationPartition=1

DHCPScopes
Specifies the number of DHCP scopes to configure.

                                                                               ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                |

<!-- p.977 -->

 Component             Configured By         |   Scenario                      Property Is Applicable

 MDT DB                ✅                     |   ZTI (Configuration Manager)   ✅

                                                                                    ﾉ   Expand table

 Value           Description

 scopes          Specifies the number of DHCP scopes to configure

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPScopes=1

DHCPScopesxDescription
The description of the DHCP scope.

  ７ Note

  The x in this properties name is a placeholder for a zero-based array that contains
  DHCP configurations.

                                                                                    ﾉ   Expand table

 Component             Configured By         |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                     |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                     |

 MDT DB                ✅                     |   ZTI (Configuration Manager)   ✅

                                                                                    ﾉ   Expand table

 Value                         Description

 description                   The description of the DHCP scope

                                                                                    ﾉ   Expand table

<!-- p.978 -->

 Example

 [Settings] Priority=Default [Default] DHCPScopes0Description=DHCPScope0

DHCPScopesxEndIP
Specifies the ending IP address for the DHCP scope.

The x in this properties name is a placeholder for a zero-based array that contains DHCP
configurations.

                                                                                ﾉ   Expand table

 Component             Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value           Description

 end_IP          Specifies the ending IP address for the DHCP scope

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPScopes0EndIP=192.168.0.30

DHCPScopesxExcludeEndIP
Specifies the ending IP address for the DHCP scope exclusion. IP addresses that are
excluded from the scope are not offered by the DHCP server to clients obtaining leases
from this scope.

  ７ Note

  The x in this properties name is a placeholder for a zero-based array that contains
  DHCP configurations.

<!-- p.979 -->

                                                                               ﾉ     Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ     Expand table

 Value                Description

 exclude_end_IP       Specifies the ending IP address for the DHCP scope exclusion

                                                                               ﾉ     Expand table

 Example

 [Settings] Priority=Default [Default] DHCPScopes0ExcludeEndIP=192.168.0.15

DHCPScopesxExcludeStartIP
Specifies the starting IP address for the DHCP scope exclusion. IP addresses that are
excluded from the scope are not offered by the DHCP server to clients obtaining leases
from this scope.

  ７ Note

  The x in this properties name is a placeholder for a zero-based array that contains
  DHCP configurations.

                                                                               ﾉ     Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)   ✅

<!-- p.980 -->

                                                                                  ﾉ      Expand table

 Value                  Description

 exclude_start_IP       Specifies the starting IP address for the DHCP scope exclusion

                                                                                  ﾉ      Expand table

 Example

 [Settings] Priority=Default [Default] DHCPScopes0ExcludeStartIP=192.168.0.10

DHCPScopesxIP
Specifies the IP subnet of the scope.

The x in this properties name is a placeholder for a zero-based array that contains DHCP
configurations.

                                                                                  ﾉ      Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ✅

                                                                                  ﾉ      Expand table

 Value              Description

 IP                 Specifies the IP subnet of the scope

                                                                                  ﾉ      Expand table

 Example

 [Settings] Priority=Default [Default] DHCPScopes0IP=192.168.0.0

DHCPScopesxName
A user-definable name to be assigned to the scope.

<!-- p.981 -->

The x in this properties name is a placeholder for a zero-based array that contains DHCP
configurations.

                                                                                 ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value           Description

 name            A user-definable name to be assigned to the scope

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPScopes0Name=DHCPScope0

DHCPScopesxOptionDNSDomainName
Specifies the domain name that the DHCP client should use when resolving unqualified
domain names with the DNS.

  ７ Note

  The x in this properties name is a placeholder for a zero-based array that contains
  DHCP configurations.

                                                                                 ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)   ✅

<!-- p.982 -->

                                                                                    ﾉ   Expand table

 Value                 Description

 DNS_domain_name       Specifies the domain name that the DHCP client should use when resolving
                       unqualified domain names with the DNS

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPScopes0OptionDNSDomainName=WoodGroveBank.com

DHCPScopesxOptionDNSServer
Specifies a list of IP addresses for DNS name servers available to the client. When more
than one server is assigned, the client interprets and uses the addresses in the specified
order.

  ７ Note

  The x in this properties name is a placeholder for a zero-based array that contains
  DHCP configurations.

                                                                                    ﾉ   Expand table

 Component             Configured By      |   Scenario                        Property Is Applicable

 BootStrap.ini         ❌                  |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini    ✅                  |

 MDT DB                ✅                  |   ZTI (Configuration Manager)     ✅

                                                                                    ﾉ   Expand table

 Value           Description

 DNS_server      Specifies a list of IP addresses for DNS name servers available to the client

                                                                                    ﾉ   Expand table

<!-- p.983 -->

 Example

 [Settings] Priority=Default [Default] DHCPScopes0OptionDNSServer=192.168.0.2

DHCPScopesxOptionLease
The duration that the DHCP lease is valid for the client.

  ７ Note

  The x in this properties name is a placeholder for a zero-based array that contains
  DHCP configurations.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value       Description

 lease       The duration that the DHCP lease is valid for the client

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPScopes0OptionLease=7

DHCPScopesxOptionNBTNodeType
Specifies the client node type for NetBT clients.

  ７ Note

<!-- p.984 -->

     The x in this properties name is a placeholder for a zero-based array that contains
     DHCP configurations.

                                                                              ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)   ✅

                                                                              ﾉ   Expand table

 Value             Description

 1                 Configures the node type as b-node

 2                 Configures the node type as p-node

 4                 Configures the node type as m-node

 8                 Configures the node type as h-node

                                                                              ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPScopes0OptionNBTNodeType=4

DHCPScopesxOptionPXEClient
Specifies the IP address used for PXE client bootstrap code.

     ７ Note

     The x in this properties name is a placeholder for a zero-based array that contains
     DHCP configurations.

                                                                              ﾉ   Expand table

<!-- p.985 -->

 Component            Configured By    |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)    ✅

                                                                               ﾉ   Expand table

 Value           Description

 PXE_client      Specifies the IP address used for PXE client bootstrap code

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPScopes0OptionPXEClient=192.168.0.252

DHCPScopesxOptionRouter
Specifies a list of IP addresses for routers on the client subnet. When more than one
router is assigned, the client interprets and uses the addresses in the specified order.
This option is normally used to assign a default gateway to DHCP clients on a subnet.

  ７ Note

  The x in this properties name is a placeholder for a zero-based array that contains
  DHCP configurations.

                                                                               ﾉ   Expand table

 Component            Configured By    |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)    ✅

                                                                               ﾉ   Expand table

<!-- p.986 -->

 Value       Description

 router      Specifies a list of IP addresses for routers on the client subnet

                                                                                      ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPScopes0OptionRouter=192.168.0.253

DHCPScopesxOptionWINSServer
Specifies the IP addresses to be used for NBNSes on the network.

  ７ Note

  The x in this properties name is a placeholder for a zero-based array that contains
  DHCP configurations

                                                                                      ﾉ   Expand table

 Component             Configured By      |   Scenario                           Property Is Applicable

 BootStrap.ini         ❌                  |   LTI (Stand-alone MDT)              ✅

 CustomSettings.ini    ✅                  |

 MDT DB                ✅                  |   ZTI (Configuration Manager)        ✅

                                                                                      ﾉ   Expand table

 Value             Description

 WINS_server       Specifies the IP addresses to be used for NBNSes on the network

                                                                                      ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPScopes0OptionWINSServer=192.168.0.2

DHCPScopesxStartIP

<!-- p.987 -->

The starting IP address for the range of IP addresses that are to be included in the
scope.

  ７ Note

  The x in this properties name is a placeholder for a zero-based array that contains
  DHCP configurations.

                                                                                   ﾉ   Expand table

 Component             Configured By     |   Scenario                        Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)     ✅

                                                                                   ﾉ   Expand table

 Value      Description

 start_IP   The starting IP address for the range of IP addresses that are to be excluded from the
            scope

                                                                                   ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPScopes0StartIP=192.168.0.20

DHCPScopesxSubnetMask
Specifies the subnet mask of the client subnet.

  ７ Note

  The x in this properties name is a placeholder for a zero-based array that contains
  DHCP configurations.

                                                                                   ﾉ   Expand table

<!-- p.988 -->

 Component            Configured By    |   Scenario                        Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)     ✅

                                                                                ﾉ   Expand table

 Value                 Description

 subnet_mask           Specifies the subnet mask of the client IP subnet

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPScopes0SubnetMask=255.255.255.0

DHCPServerOptionDNSDomainName
Specifies the connection-specific DNS domain suffix of client computers.

                                                                                ﾉ   Expand table

 Component            Configured By    |   Scenario                        Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)     ✅

                                                                                ﾉ   Expand table

 Value                 Description

 DNS_domain_name       Specifies the connection-specific DNS domain suffix of client computers

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPServerOptionDNSDomainName=Fabrikam.com

<!-- p.989 -->

DHCPServerOptionDNSServer
Specifies a list of IP addresses to be used as DNS name servers that are available to the
client.

                                                                                     ﾉ   Expand table

 Component              Configured By      |   Scenario                        Property Is Applicable

 BootStrap.ini          ❌                  |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini     ✅                  |

 MDT DB                 ✅                  |   ZTI (Configuration Manager)     ✅

                                                                                     ﾉ   Expand table

 Value           Description

 DNS_server      Specifies a list of IP addresses to be used as DNS name servers that are available to
                 the client

                                                                                     ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPServerOptionDNSServer=192.168.0.1,192.168.0.2

DHCPServerOptionNBTNodeType
Specifies the client node type for NetBT clients.

                                                                                     ﾉ   Expand table

 Component              Configured By      |   Scenario                        Property Is Applicable

 BootStrap.ini          ❌                  |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini     ✅                  |

 MDT DB                 ✅                  |   ZTI (Configuration Manager)     ✅

                                                                                     ﾉ   Expand table

<!-- p.990 -->

 Value           Description

 1               Configures the node type as b-node

 2               Configures the node type as p-node

 4               Configures the node type as m-node

 8               Configures the node type as h-node

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPServerOptionNBTNodeType=4

DHCPServerOptionPXEClient
Specifies the IP address used for PXE client bootstrap code.

                                                                               ﾉ   Expand table

 Component            Configured By    |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)    ✅

                                                                               ﾉ   Expand table

 Value           Description

 PXE_client      Specifies the IP address used for PXE client bootstrap code

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPServerOptionPXEClient=192.168.0.252

DHCPServerOptionRouter

<!-- p.991 -->

Specifies a list of IP addresses for routers on the client subnet. When more than one
router is assigned, the client interprets and uses the addresses in the specified order.
This option is normally used to assign a default gateway to DHCP clients on a subnet.

                                                                                      ﾉ   Expand table

 Component             Configured By      |   Scenario                           Property Is Applicable

 BootStrap.ini         ❌                  |   LTI (Stand-alone MDT)              ✅

 CustomSettings.ini    ✅                  |

 MDT DB                ✅                  |   ZTI (Configuration Manager)        ✅

                                                                                      ﾉ   Expand table

 Value       Description

 router      Specifies a list of IP addresses for routers on the client subnet

                                                                                      ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPServerOptionRouter=192.168.0.253

DHCPServerOptionWINSServer
Specifies the IP addresses to be used for NBNSes on the network.

                                                                                      ﾉ   Expand table

 Component             Configured By      |   Scenario                           Property Is Applicable

 BootStrap.ini         ❌                  |   LTI (Stand-alone MDT)              ✅

 CustomSettings.ini    ✅                  |

 MDT DB                ✅                  |   ZTI (Configuration Manager)        ✅

                                                                                      ﾉ   Expand table

 Value             Description

 WINS_server       Specifies the IP addresses to be used for NBNSes on the network

<!-- p.992 -->

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DHCPServerOptionWINSServer=192.168.0.2

Dialing
The type of dialing supported by the telephony infrastructure where the target
computer is located. This value is inserted into the appropriate configuration settings in
Unattend.xml.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                                  ﾉ   Expand table

 Component               Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ✅                 |

 MDT DB                  ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                  ﾉ   Expand table

 Value           Description

 PULSE           The telephony infrastructure supports pulse dialing.

 TONE            The telephony infrastructure supports touch-tone dialing.

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] AreaCode=206 CountryCode=001 Dialing=TONE
 LongDistanceAccess=9

DisableTaskMgr

<!-- p.993 -->

This property controls a user's ability to start Task Manager by pressing CTRL+ALT+DEL.
After the user starts Task Manager, they could interrupt the LTI task sequence while
running in the new operating system on the target computer. This property is used in
conjunction with the HideShell property and is only valid when the HideShell property
is set to YES.

  ７ Note

  This property and the HideShell property must both be set to YES to prevent the
  user pressing CTRL+ALT+DEL and interrupting the LTI task sequence.

                                                                              ﾉ   Expand table

 Component             Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅               |

 MDT DB                ✅               |   ZTI (Configuration Manager)   ❌

                                                                              ﾉ   Expand table

 Value   Description

 YES     Prevent the user from being able to start Task Manager by pressing CTRL+ALT+DEL and
         subsequently interrupting the LTI task sequence.

 NO      Allow the user to start Task Manager by pressing CTRL+ALT+DEL and subsequently
         interrupt the LTI task sequence. This is the default value.

                                                                              ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DisableTaskMgr=YES HideShell=YES

DNSServerOptionBINDSecondaries
Determines whether to use fast transfer format for transfer of a zone to DNS servers
running legacy BIND implementations.

By default, all Windows-based DNS servers use a fast zone transfer format. This format
uses compression, and it can include multiple records per TCP message during a

<!-- p.994 -->

connected transfer. This format is also compatible with more recent BIND-based DNS
servers that run version 4.9.4 and later.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                               ﾉ   Expand table

 Component            Configured By    |    Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |    LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |    ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value            Description

 TRUE             Allows BIND secondaries

 FALSE            Does not allow to BIND secondaries

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DNSServerOptionBINDSecondaries=TRUE

DNSServerOptionDisableRecursion
Determines whether or not the DNS server uses recursion. By default, the DNS Server
service is enabled to use recursion.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

<!-- p.995 -->

                                                                              ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ✅

                                                                              ﾉ   Expand table

 Value            Description

 TRUE             Disables recursion on the DNS server

 FALSE            Enables recursion on the DNS server

                                                                              ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DNSServerOptionDisableRecursion=TRUE

DNSServerOptionEnableNetmaskOrdering
Determines whether the DNS server reorders address (A) resource records within the
same resource record that is set in the server's response to a query based on the IP
address of the source of the query.

By default, the DNS Server service uses local subnet priority to reorder A resource
records.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                              ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

<!-- p.996 -->

 Component            Configured By   |   Scenario                      Property Is Applicable

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ✅

                                                                             ﾉ     Expand table

 Value                 Description

 TRUE                  Enables netmask ordering

 FALSE                 Disables netmask ordering

                                                                             ﾉ     Expand table

 Example

 [Settings] Priority=Default [Default] DNSServerOptionEnableNetmaskOrdering=TRUE

DNSServerOptionEnableRoundRobin
Determines whether the DNS server uses the round robin mechanism to rotate and
reorder a list of resource records if multiple resource records exist of the same type that
exist for a query answer.

By default, the DNS Server service uses round robin.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                             ﾉ     Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ✅

<!-- p.997 -->

                                                                               ﾉ   Expand table

 Value                    Description

 TRUE                     Enables round robin

 FALSE                    Disables round robin

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DNSServerOptionEnableRoundRobin=TRUE

DNSServerOptionEnableSecureCache
Determines whether the DNS server attempts to clean up responses to avoid cache
pollution. This setting is enabled by default. By default, DNS servers use a secure
response option that eliminates adding unrelated resource records that are included in a
referral answer to their cache. In most cases, any names that are added in referral
answers are typically cached, and they help expedite the resolution of subsequent DNS
queries.

With this feature, however, the server can determine that referred names are potentially
polluting or insecure and then discard them. The server determines whether to cache
the name that is offered in a referral on the basis of whether it is part of the exact,
related, DNS domain name tree for which the original queried name was made.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

<!-- p.998 -->

                                                                               ﾉ   Expand table

 Value                    Description

 TRUE                     Enables cache security

 FALSE                    Disables cache security

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DNSServerOptionEnableSecureCache=TRUE

DNSServerOptionFailOnLoad
Specifies that loading of a zone should fail when bad data is found.

  Ｕ Caution

  This property value must be specified in uppercase so that the deployment scripts
  can read it properly.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                       Description

 TRUE                        Enable fail on load

 FALSE                       Disable fail on load

                                                                               ﾉ   Expand table

<!-- p.999 -->

 Example

 [Settings] Priority=Default [Default] DNSServerOptionFailOnLoad=TRUE

DNSServerOptionNameCheckFlag
Specifies which character standard is used when checking DNS names.

                                                                                 ﾉ   Expand table

 Component             Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                |

 MDT DB                ✅                |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value   Description

 0       Uses ANSI characters that comply with Internet Engineering Task Force (IETF) Request for
         Comments (RFCs). This value corresponds to the Strict RFC (ANSI) selection when
         configuring DNS in the Deployment Workbench.

 1       Uses ANSI characters that do not necessarily comply with IETF RFCs. This value
         corresponds to the Non RFC (ANSI) selection when configuring DNS in the Deployment
         Workbench.

 2       Uses multibyte UCS Transformation Format 8 (UTF-8) characters. This is the default
         setting. This value corresponds to the Multibyte (UTF-8) selection when configuring DNS
         in the Deployment Workbench.

 3       Uses all characters. This value corresponds to the All names selection when configuring
         DNS in the Deployment Workbench.

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DNSServerOptionNameCheckFlag=2

DNSZones
Specifies the number of DNS zones to configure.

<!-- p.1000 -->

                                                                                ﾉ   Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                |

 MDT DB                 ✅                |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value           Description

 zones           Specifies the number of DNS zones to configure

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] DNSZones=1 DNSZones0Name=MyNewZone
 DNSZones0DirectoryPartition=Forest DNSZones0FileName=MyNewZone.dns
 DNSZones0MasterIP=192.168.0.1,192.168.0.2 DNSZones0Type=Secondary

DNSZonesxDirectoryPartition
Specifies the directory partition on which to store the zone when configuring secondary
or stub zones.

  ７ Note

  The x in this properties name is a placeholder for a zero-based array that contains
  DNS configurations.

                                                                                ﾉ   Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                |

 MDT DB                 ✅                |   ZTI (Configuration Manager)   ✅
