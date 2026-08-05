---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1041-1080"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1041-1080
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1041-1080
family: sccm
documentKind: "doc"
abstract: "LanguagePacks A list of the GUIDs for the language packs to be deployed on the target computer. Deployment Workbench specifies these language packs on the OS Packages node. These GUIDs are stored in the Packages.xml file. The LanguagePacks property has a numeric suffix (for exam"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1041-1080

<!-- p.1041 -->

LanguagePacks
A list of the GUIDs for the language packs to be deployed on the target computer.
Deployment Workbench specifies these language packs on the OS Packages node.
These GUIDs are stored in the Packages.xml file. The LanguagePacks property has a
numeric suffix (for example, LanguagePacks001 or LanguagePacks002).

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ❌               |   ZTI (Configuration Manager)   ❌

                                                                             ﾉ   Expand table

 Value                Description

 language_pack_guid   The GUID that the Deployment Workbench specifies for the language packs
                      to install on the target computer. The GUID corresponds to the language
                      pack GUID stored in Packages.xml.

                                                                             ﾉ   Expand table

 Example

  [Settings] Priority=Default [Default] LanguagePacks001={a1923f8d-b07b-44c7-ac1e-
 353b7cc4c1ad}

LoadStateArgs
The arguments passed to the USMT Loadstate process. The ZTI script inserts the
appropriate logging, progress, and state store parameters. If this value is not included in
the settings file, the user state restore process is skipped.

If the Loadstate process finishes successfully, the user state information is deleted. In the
event of a Loadstate failure (or non-zero return code), the local state store is moved to
%WINDIR%\StateStore to prevent deletion and to ensure that no user state information
is lost.

   ７ Note

<!-- p.1042 -->

 Do not add any of the following command-line arguments when configuring this
 property: /hardlink, /nocompress, /decrypt, /key, or /keyfile. The MDT scripts will
 add these command-line arguments if applicable to the current deployment
 scenario.

                                                                                     ﾉ   Expand table

Component               Configured By      |   Scenario                        Property Is Applicable

BootStrap.ini           ❌                  |   LTI (Stand-alone MDT)           ✅

CustomSettings.ini      ✅                  |

MDT DB                  ✅                  |   ZTI (Configuration Manager)     ❌

                                                                                     ﾉ   Expand table

Value           Description

Arguments       The command-line arguments passed to Loadstate.exe.

                The default arguments specified by Deployment Workbench are as follows:

                - /v. Enables verbose output in the Loadstate log. The default is 0. Specify any
                number from 0 to 15. The value 5 enables verbose and status output.

                - /c. When specified, Loadstate will continue to run even if there are nonfatal errors.
                Without the /c option, Loadstate exits on the first error.

                - /lac. Specifies that if the account being migrated is a local (non-domain) account,
                and it does not exist on the destination computer, then USMT will create the
                account but it will be disabled.

                For more information about these and other arguments, see the USMT Help files.

                                                                                     ﾉ   Expand table

Example

[Settings] Priority=Default [Default] OSInstall=YES ScanStateArgs=/v:5 /o /c
LoadStateArgs=/v:5 /c /lac DeployRoot=\\NYC-AM-FIL-01\Distribution$ ResourceRoot=\\NYC-AM-
FIL-01\Resource$ UDShare=\\NYC-AM-FIL-01\MigData$ UDDir=%OSDComputerName%

Location

<!-- p.1043 -->

The geographic location of the target computers. A list of IP addresses that correspond
to the default gateways defined for the computers within that location defines the
Location property. An IP address for a default gateway can be associated with more
than one location.

Typically, the value for the Location property is set by performing a database query on
the database managed using Deployment Workbench. Deployment Workbench can
assist in creating the locations, defining property settings associated with the locations,
and then in configuring CustomSettings.ini to perform the database query for the
Location property and the property settings associated with the locations.

For example, a LocationSettings section in CustomSettings.ini can query the
LocationSettings view in the database for a list of locations that contain the value
specified in the DefaultGateway property listed in the Parameters property. The query
returns all settings associated with each default gateway.

Then the scripts parse each section that corresponds to the locations returned in the
query. For example, the value [Springfield] and the section [Springfield-123 Oak
Street-4th Floor] in CustomSettings.ini can represent the corresponding locations. This

is an example of how one computer can belong to two locations. The
[Springfield] section is for all computers in a larger geographic area (an entire city),

and the [Springfield-123 Oak Street-4th Floor] section is for all computers on the
fourth floor at 123 Oak Street, in Springfield.

                                                                                  ﾉ    Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ✅                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ✅

                                                                                  ﾉ    Expand table

 Value                 Description

 location1,location2   The list of locations to be assigned to an individual computer or a group of
                       computers

                                                                                  ﾉ    Expand table

<!-- p.1044 -->

 Example

 [Settings] Priority=LSettings, Default [Default] UserDataLocation=AUTO DeployRoot=\\W2K3-
 SP1\Distribution$ OSInstall=YES ScanStateArgs=/v:15 /o /c LoadStateArgs=/v:7 /c [LSettings]
 SQLServer=w2k3-sp1 Instance=MDT2010 Database=MDTDB Netlib=DBNMPNTW SQLShare=SQL$
 Table=LocationSettings Parameters=DefaultGateway [Springfield] UDDir=%OSDComputerName%
 UDShare=\\Springfield-FIL-01\UserData [Springfield-123 Oak Street-4th Floor]
 DeployRoot=\\Springfield-BDD-01\Distribution1$

LongDistanceAccess
The dialing digits to gain access to an outside line to dial long distance. The property
can contain only numeric digits. This value is inserted into the appropriate configuration
settings in Unattend.xml.

                                                                               ﾉ   Expand table

 Component              Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅               |

 MDT DB                 ✅               |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                  Description

 language_pack_guid     The GUID that the Deployment Workbench specifies for the language packs
                        to install on the target computer. The GUID corresponds to the language
                        pack GUID stored in Packages.xml.

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] AreaCode=206 CountryCode=001 Dialing=TONE
 LongDistanceAccess=9

MACAddress
The media access control (MAC) layer address of the primary network adapter of the
target computer. The MACAddress property is included on the Priority line so that

<!-- p.1045 -->

property values specific to a target computer can be provided. Create a section for each
MAC address for each of the target computers (such as [00:0F:20:35:DE:AC] or
[00:03:FF:FE:FF:FF] ) that contain target computer-specific settings.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ❌                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                    Description

 mac_address              The MAC address of the target computer

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=MACAddress, Default [Default] CaptureGroups=YES Groups1=NYC Application
 Management Groups2=NYC Help Desk Users [00:0F:20:35:DE:AC] OSDNEWMACHINENAME=HPD530-1
 [00:03:FF:FE:FF:FF] OSDNEWMACHINENAME=BVMXP

MachineObjectOU
The AD DS OU in the target domain where the computer account for the target
computer is created.

  ７ Note

  The OU specified in this property must exist before deploying the target operating
  system.

  ７ Note

  If a computer object already exists in AD DS, specifying MachineObjectOU will not
  cause the computer object to be moved to the specified OU.

<!-- p.1046 -->

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ✅

                                                                             ﾉ   Expand table

 Value       Description

 OU_name     The name of the OU where the computer account for the target computer will be
             created

                                                                             ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] JoinDomain=WOODGROVEBANK
 MachineObjectOU=OU=Reception,OU=NYC,DC=Woodgrovebank,DC=com

Make
The manufacturer of the target computer. The format for Make is undefined. Use this
property to create a subsection that contains settings targeted to a specific computer
manufacturer (most commonly in conjunction with the Model and Product properties).

  ７ Note

  This property is dynamically set by MDT scripts and cannot have its value set in
  CustomSettings.ini or the MDT DB. Treat this property as read only. However, you
  can use this property within CustomSettings.ini or the MDT DB, as shown in the
  following examples, to aid in defining the configuration of the target computer.

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ❌               |

<!-- p.1047 -->

 Component              Configured By    |   Scenario                      Property Is Applicable

 MDT DB                 ❌                |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value           Description

 make            The manufacturer of the target computer

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Make, Default [Default] [Dell Computer Corporation] Subsection=Dell-
 %Model% [Dell-Latitude D600] Packages001=XXX00009:Program9 Packages002=XXX0000A:Program10

MandatoryApplications
A list of application GUIDs that will be installed on the target computer. These
applications are specified on the Applications node in the Deployment Workbench. The
GUIDs are stored in the Applications.xml file. The MandatoryApplications property is a
list of text values that can be any non-blank value. The MandatoryApplications property
has a numeric suffix (for example, MandatoryApplications001 or
MandatoryApplications002).

                                                                                ﾉ   Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                |

 MDT DB                 ❌                |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value                Description

 application_guid     The GUID specified by the Deployment Workbench for the application to be
                      deployed to the target computer. The GUID corresponds to the application
                      GUID stored in the Applications.xml file.

<!-- p.1048 -->

                                                                                ﾉ     Expand table

 Example

 [Settings] Priority=Default [Default] MandatoryApplications001={1D7DF331-47B7-472C-87B3-
 442597EC2F7D} MandatoryApplications002={9d2b8999-5e4d-4f3d-bb05-edaaf4fe5628}
 Administrators001=WOODGROVEBANK\NYC Help Desk Staff

Memory
The amount of memory installed on the target computer in megabytes. For example, the
value 2038 indicates 2,038 MB (or 2 GB) of memory is installed on the target computer.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                ﾉ     Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌                |

 MDT DB                 ❌                |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ     Expand table

 Value           Description

 memory          The amount of memory installed on the target computer in megabytes

                                                                                ﾉ     Expand table

 Example

 None

Model

<!-- p.1049 -->

The model of the target computer. The format for Model is undefined. Use this property
to create a subsection that contains settings targeted to a specific computer model
number for a specific computer manufacturer (most commonly in conjunction with the
Make and Product properties).

  ７ Note

  This property is dynamically set by MDT scripts and cannot have its value set in
  CustomSettings.ini or the MDT DB. Treat this property as read only. However, you
  can use this property within CustomSettings.ini or the MDT DB, as shown in the
  following examples, to aid in defining the configuration of the target computer.

                                                                               ﾉ   Expand table

 Component             Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ❌                |

 MDT DB                ❌                |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                Description

 model                The model of the target computer

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Make, Default [Default] [Dell Computer Corporation] Subsection=Dell-
 %Model% [Dell-Latitude D600] Packages001=XXX00009:Program9 Packages002=XXX0000A:Program10

NetLib
The protocol to be used to communicate with the computer running SQL Server
specified in the SQLServer property.

                                                                               ﾉ   Expand table

<!-- p.1050 -->

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ✅                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                    Description

 DBNMPNTW                 Use the named pipes protocol to communicate.

 DBMSSOCN                 Use TCP/IP sockets to communicate.

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Computers, Default [Default] ScanStateArgs=/v:5 /o /c LoadStateArgs=/v:5
 /c /lac [Computers] SQLServer=NYC-SQL-01 SQLShare=SQL$ NetLib=DBNMPNTW Database=MDTDB
 Instance=SQLEnterprise2005 Table=Computers Parameters=SerialNumber, AssetTag
 ParameterCondition=OR

NewDomain
Indicates the type of a new domain: whether a new domain in a new forest, the root of a
new tree in an existing forest, or a child of an existing domain.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value      Description

 Child      The new domain is a child of an existing domain.

<!-- p.1051 -->

 Value       Description

 Forest      The new domain is the first domain in a new forest of domain trees.

 Tree        The new domain is the root of a new tree in an existing forest.

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] NewDomain=Tree

NewDomainDNSName
Specifies the required name of a new tree in an existing domain or when Setup installs a
new forest of domains.

                                                                                    ﾉ   Expand table

 Component              Configured By    |   Scenario                          Property Is Applicable

 BootStrap.ini          ❌                |   LTI (Stand-alone MDT)             ✅

 CustomSettings.ini     ✅                |

 MDT DB                 ✅                |   ZTI (Configuration Manager)       ✅

                                                                                    ﾉ   Expand table

 Value    Description

 name     Specifies the required name of a new tree in an existing domain or when Setup installs a
          new forest of domains

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] NewDomainDNSName=newdom.WoodGroveBank.com

Order
The sorting order for the result set on a database query. The result set is based on the
configuration settings of the Database, Table, SQLServer, Parameters, and

<!-- p.1052 -->

ParameterCondition properties. More than one property can be provided to sort the
results by more than one property.

For example, if Order=Sequence is specified in the CustomSettings.ini file, then an
ORDER BY sequence clause is added to the query. Specifying Order=Make, Model adds
an ORDER BY Make, Model clause to the query.

                                                                                   ﾉ   Expand table

 Component            Configured By      |   Scenario                        Property Is Applicable

 BootStrap.ini        ✅                  |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini   ✅                  |

 MDT DB               ❌                  |   ZTI (Configuration Manager)     ✅

                                                                                   ﾉ   Expand table

 Value                Description

 property1,           Properties to define the sort order for the result set (where propertyn
 property2, ...       represents the properties in the sort criteria)

                                                                                   ﾉ   Expand table

 Example

 [Settings] Priority=Computers, Default [Default] OSInstall=YES ScanStateArgs=/v:5 /o /c
 LoadStateArgs=/v:5 /c /lac [Computers] SQLServer=NYC-SQL-01 SQLShare=SQL$ NetLib=DBNMPNTW
 Database=MDTDB Instance=SQLEnterprise2005 Table=MakeModelSettings Parameters=SerialNumber,
 AssetTag ParameterCondition=OR Order=Make, Model

OrgName
The name of the organization that owns the target computer. This value is inserted into
the appropriate configuration settings in Unattend.xml.

                                                                                   ﾉ   Expand table

 Component            Configured By      |   Scenario                        Property Is Applicable

 BootStrap.ini        ❌                  |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini   ✅                  |

<!-- p.1053 -->

 Component            Configured By    |   Scenario                      Property Is Applicable

 MDT DB               ✅                |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value           Description

 org_name        The name of the organization that owns the target computer

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=MACAddress, Default Properties=CustomProperty, ApplicationInstall
 [Default] OSInstall=YES ScanStateArgs=/v:5 /o /c LoadStateArgs=/v:5 /c /lac
 UserDataLocation=NONE CustomProperty=TRUE OrgName=Woodgrove Bank [00:0F:20:35:DE:AC]
 OSDNEWMACHINENAME=HPD530-1 ApplicationInstall=Custom FullName=Woodgrove Bank User
 [00:03:FF:FE:FF:FF] OSDNEWMACHINENAME=BVMXP ApplicationInstall=Minimum FullName=Woodgrove
 Bank Manager

OSArchitecture
The processor architecture type for the target operating system. This property is
referenced during OEM deployments. Valid values are x86 and x64.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                               ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ❌                |

 MDT DB               ❌                |   ZTI (Configuration Manager)   ❌

                                                                               ﾉ   Expand table

<!-- p.1054 -->

 Value      Description

 x86        The processor architecture type for the operating system is 32 bit.

 x64        The processor architecture type for the operating system is 64 bit.

                                                                                  ﾉ   Expand table

 Example

 None

OSCurrentBuild
The build number of the currently running operating system.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                  ﾉ   Expand table

 Component            Configured By      |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                  |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ❌                  |

 MDT DB               ❌                  |   ZTI (Configuration Manager)    ✅

                                                                                  ﾉ   Expand table

 Value                              Description

 7600                               Windows 7

 9600                               Windows 8.1

                                                                                  ﾉ   Expand table

 Example

 None

<!-- p.1055 -->

OSCurrentVersion
The version number of the currently running operating system.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                              ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ❌               |

 MDT DB               ❌               |   ZTI (Configuration Manager)   ✅

                                                                              ﾉ   Expand table

 Value            Description

 version_number   The operating system major version, minor version, and build numbers
                  (major.minor.build). For example, 6.3.9600 would represent Windows 8.1.

                                                                              ﾉ   Expand table

 Example

 None

OSDAdapterxDescription
Specifies the name of the network connection as it appears in the Control Panel
Network Connections item. The name can be between 0 and 255 characters in length.

This property is for LTI only. For the equivalent property for ZTI, see OSDAdapterxName.

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0Description or

<!-- p.1056 -->

  OSDAdapter1Description.

                                                                                 ﾉ   Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌                |

 MDT DB                 ❌                |   ZTI (Configuration Manager)   ❌

                                                                                 ﾉ   Expand table

 Value           Description

 Description     The name of the network connection as it appears in the Control Panel Network
                 Connections item

                                                                                 ﾉ   Expand table

 Example

 None

OSDAdapterxDNSDomain
Specifies the DNS domain name (DNS suffix) that will be assigned to the network
connection. This property is for ZTI only. For LTI, see the OSDAdapterxDNSSuffix
property.

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0DNSDomain or
  OSDAdapter1DNSDomain.

                                                                                 ﾉ   Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                |   LTI (Stand-alone MDT)         ❌

<!-- p.1057 -->

 Component            Configured By   |   Scenario                      Property Is Applicable

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ✅

                                                                              ﾉ   Expand table

 Value                Description

 DNS_domain_name      A DNS domain name (DNS suffix) that will be assigned to the network
                      connection

                                                                              ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0DNSDomain=WoodGroveBank.com

OSDAdapterxDNSServerList
This is a comma-delimited list of DNS server IP addresses that will be assigned to the
network connection.

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0DNSServerList or
  OSDAdapter1DNSServerList.

                                                                              ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ✅

                                                                              ﾉ   Expand table

<!-- p.1058 -->

 Value           Description

 DNS_servers     A comma-delimited list of DNS server IP addresses that will be assigned to the
                 network connection

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default]
 OSDAdapter0DNSServerList=192.168.0.254,192.168.100.254

OSDAdapterxDNSSuffix
A DNS suffix that will be assigned to the network connection. This property is for LTI
only. For ZTI, see the OSDAdapterxDNSDomain property.

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0DNSSuffix or
  OSDAdapter1DNSSuffix.

                                                                                  ﾉ   Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ   Expand table

 Value             Description

 DNS_suffix        A DNS suffix that will be assigned to the network connection

                                                                                  ﾉ   Expand table

<!-- p.1059 -->

 Example

 [Settings] Priority=Default [Default] OSDAdapter0DNSSuffix= WoodGroveBank.com

OSDAdapterxEnableDHCP
Specifies whether the network connection will be configured via DHCP.

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0EnableDHCP or
  OSDAdapter1EnableDHCP.

                                                                                   ﾉ   Expand table

 Component            Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)    ✅

                                                                                   ﾉ   Expand table

 Value      Description

 TRUE       The network connection will be configured via DHCP.

 FALSE      The network connection will be configured with static configuration.

                                                                                   ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0EnableDHCP=TRUE

OSDAdapterxEnableDNSRegistration
Specifies whether DNS registration is enabled on the network connection.

<!-- p.1060 -->

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0EnableDNSRegistration or
  OSDAdapter1EnableDNSRegistration.

                                                                               ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                 Description

 TRUE                  Enables DNS registration

 FALSE                 Disables DNS registration

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0EnableDNSRegistration=TRUE

OSDAdapterxEnableFullDNSRegistration
Specifies whether full DNS registration is enabled on the network connection.

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0EnableFullDNSRegistration or
  OSDAdapter1EnableFullDNSRegistration.

                                                                               ﾉ   Expand table

<!-- p.1061 -->

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                Description

 TRUE                 Enables full DNS registration

 FALSE                Disables full DNS registration

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0EnableFullDNSRegistration=TRUE

OSDAdapterxEnableLMHosts
Specifies whether LMHOSTS lookup is enabled on the network connection.

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0EnableLMHosts or
  OSDAdapter1EnableLMHosts.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

<!-- p.1062 -->

 Value                 Description

 TRUE                  Enables LMHOSTS lookup

 FALSE                 Disables LMHOSTS lookup

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0EnableLMHosts=TRUE

OSDAdapterxEnableIPProtocolFiltering
This property specifies whether IP protocol filtering should be enabled on the network
connection.

Thexin this property's name is a placeholder for a zero-based array that contains
network adapter information, such as OSDAdapter0EnableIPProtocolFiltering or
OSDAdapter1EnableIPProtocolFiltering.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                Description

 TRUE                 Enables IP protocol filtering

 FALSE                Disables IP protocol filtering

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0EnableIPProtocolFiltering =TRUE

<!-- p.1063 -->

OSDAdapterxEnableTCPFiltering
Specifies whether TCP/IP filtering should be enabled on the network connection. This
property is for ZTI only. For LTI, see the OSDAdapterxEnableTCPIPFiltering property.

  ７ Note

  Thexin this property's name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0EnableTCPFiltering or
  OSDAdapter1EnableTFiltering.

                                                                                ﾉ   Expand table

 Component            Configured By      |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                  |   LTI (Stand-alone MDT)         ❌

 CustomSettings.ini   ✅                  |

 MDT DB               ✅                  |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value                    Description

 TRUE                     Enables TCP/IP filtering

 FALSE                    Disables TCP/IP filtering

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0EnableTCPFiltering=TRUE

OSDAdapterxEnableTCPIPFiltering
Specifies whether TCP/IP filtering should be enabled on the network connection. This
property is for LTI only. For ZTI, see the OSDAdapterxEnableTCPFiltering property.

  ７ Note

<!-- p.1064 -->

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0EnableTCPIPFiltering or
  OSDAdapter1EnableTCPIPFiltering.

                                                                                ﾉ   Expand table

 Component            Configured By      |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                  |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                  |

 MDT DB               ✅                  |   ZTI (Configuration Manager)   ❌

                                                                                ﾉ   Expand table

 Value                    Description

 TRUE                     Enables TCP/IP filtering

 FALSE                    Disables TCP/IP filtering

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0EnableTCPIPFiltering=TRUE

OSDAdapterxEnableWINS
Specifies whether WINS will be enabled on the network connection.

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0EnableWINS or
  OSDAdapter1EnableWINS.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

<!-- p.1065 -->

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ✅

                                                                             ﾉ   Expand table

 Value                          Description

 TRUE                           Enables WINS

 FALSE                          Disables WINS

                                                                             ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0EnableWINS=TRUE
 OSDAdapter0WINSServerList=192.168.0.1,192.168.100.1

OSDAdapterxGatewayCostMetric
A comma-delimited list of Gateway Cost Metrics specified as either integers or the string
"Automatic" (if empty, uses "Automatic") that will be configured on the connection.

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0GatewayCostMetric or
  OSDAdapter1GatewayCostMetric.

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ✅

<!-- p.1066 -->

                                                                             ﾉ   Expand table

 Value                Description

 cost_metrics         A comma-delimited list of Gateway Cost Metrics

                                                                             ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0GatewayCostMetrics=Automatic

OSDAdapterxGateways
A comma-delimited list of gateways to be assigned to the network connection.

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0Gateways or
  OSDAdapter1Gateways.

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ✅

                                                                             ﾉ   Expand table

 Value                 Description

 gateways              A comma-delimited list of gateways

                                                                             ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0Gateways=192.168.0.1,192.168.100.1

<!-- p.1067 -->

OSDAdapterxIPAddressList
A comma-delimited list of IP addresses to be assigned to the network connection.

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0IPAddressList or
  OSDAdapter1IPAddressList.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ❌

                                                                               ﾉ   Expand table

 Value                    Description

 IP_addresses             A comma delimited list of IP addresses

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0IPAddressList=192.168.0.40,192.168.100.40
 OSDAdapter0SubnetMask=255.255.255.0,255.255.255.0

OSDAdapterxIPProtocolFilterList
A comma-delimited list of IP protocol filters to be assigned to the network connection.
This property can be configured using the CustomSettings.ini file or the MDT DB but not
the Deployment Workbench. If using Configuration Manager it is also configurable
using an Apply Network Settings task sequence step.

  ７ Note

<!-- p.1068 -->

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0IPProtocolFilterList or
  OSDAdapter1IPProtocolFilterList.

                                                                                    ﾉ   Expand table

 Component              Configured By   |    Scenario                          Property Is Applicable

 BootStrap.ini          ❌               |    LTI (Stand-alone MDT)             ✅

 CustomSettings.ini     ✅               |

 MDT DB                 ✅               |    ZTI (Configuration Manager)       ✅

                                                                                    ﾉ   Expand table

 Value                         Description

 protocol_filter_list          A comma-delimited list of IP protocol filters

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0IPProtocolFilterList=a list of approved IP
 protocols

OSDAdapterxMacAddress
Assign the specified configuration settings to the network interface card that matches
the specified MAC address.

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0MacAddress or
  OSDAdapter1MacAddress.

                                                                                    ﾉ   Expand table

<!-- p.1069 -->

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ✅

                                                                             ﾉ   Expand table

 Value                         Description

 MAC_address                   Network adapter MAC address

                                                                             ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0MacAddress=00:0C:29:67:A3:6B

OSDAdapterxName
Assign the specified configuration settings to the network adapter that matches the
specified name. This property is for ZTI only. For the equivalent property for LTI, see
OSDAdapterxDescription.

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0Name or OSDAdapter1Name.

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ❌

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ✅

                                                                             ﾉ   Expand table

<!-- p.1070 -->

 Value                  Description

 name                   Network adapter name

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0Name=3Com 3C920 Integrated Fast Ethernet
 Controller

OSDAdapterxSubnetMask
A comma-delimited list of IP subnet masks to be assigned to the network connection.

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0SubnetMask or
  OSDAdapter1SubnetMask.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                    Description

 subnet_masks             A comma-delimited list of IP subnet masks

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0IPAddressList=192.168.0.40,192.168.100.40
 OSDAdapter0SubnetMask=255.255.255.0,255.255.255.0

<!-- p.1071 -->

OSDAdapterxTCPFilterPortList
A comma-delimited list of TCP filter ports to be assigned to the network connection.
This property can be configured using the CustomSettings.ini file or the MDT DB but not
the Deployment Workbench. If using Configuration Manager it is also configurable
using an Apply Network Settings task sequence step.

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0TCPFilterPortList or
  OSDAdapter1TCPFilterPortList.

                                                                              ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)   ✅

                                                                              ﾉ   Expand table

 Value            Description

 port_list        A comma-delimited list of TCP/IP filter ports

                                                                              ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0TCPFilterPortList=a list of approved TCP
 ports

OSDAdapterxTCPIPNetBiosOptions
Specifies the TCP/IP NetBIOS options to be assigned to the network connection.

  ７ Note

<!-- p.1072 -->

     Thexin this properties name is a placeholder for a zero-based array that contains
     network adapter information, such as OSDAdapter0TCPIPNetBiosOptions or
     OSDAdapter1TCPIPNetBiosOptions.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                    Description

 0                        Disable IP forwarding.

 1                        Enable IP forwarding.

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0TCPIPNetBiosOptions=0

OSDAdapterxUDPFilterPortList
A comma-delimited list of User Datagram Protocol (UDP) filter ports to be assigned to
the network connection. This property can be configured using the CustomSettings.ini
file and the MDT DB but not the Deployment Workbench. If using Configuration
Manager it is also configurable using an Apply Network Settings task sequence step.

     ７ Note

     Thexin this properties name is a placeholder for a zero-based array that contains
     network adapter information, such as OSDAdapter0UDPFilterPortList or
     OSDAdapter1UDPFilterPortList.

                                                                               ﾉ   Expand table

<!-- p.1073 -->

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value                Description

 port_list            A comma-delimited list of UDP filter ports

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0UDPFilterPortList=a list of approved UDP
 ports

OSDAdapterxWINSServerList
A two-element, comma-delimited list of WINS server IP addresses to be assigned to the
network connection.

  ７ Note

  Thexin this properties name is a placeholder for a zero-based array that contains
  network adapter information, such as OSDAdapter0WINSServerList or
  OSDAdapter1WINSServerList.

                                                                                 ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

<!-- p.1074 -->

 Value                      Description

 WINS_server_list           A comma-delimited list of WINS server IP addresses

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapter0EnableWINS=TRUE
 OSDAdapter0WINSServerList=192.168.0.1,192.168.100.1

OSDAdapterCount
Specifies the number of network connections that are to be configured.

                                                                                 ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value                Description

 count                The number of network adapters

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDAdapterCount=1 OSDAdapter0EnableDHCP=FALSE
 OSDAdapter0IPAddressList=192.168.0.40,192.168.100.40
 OSDAdapter0SubnetMask=255.255.255.0,255.255.255.0
 OSDAdapter0Gateways=192.168.0.1,192.168.100.1 OSDAdapter0EnableWINS=TRUE
 OSDAdapter0WINSServerList=192.168.0.1,192.168.100.1 OSDAdapter0TCPIPNetBiosOptions=0
 OSDAdapter0MacAddress=00:0C:29:67:A3:6B OSDAdapter0GatewayCostMetrics=Automatic
 OSDAdapter0EnableTCPIPFiltering=TRUE OSDAdapter0EnableLMHosts=TRUE
 OSDAdapter0EnableFullDNSRegistration=TRUE OSDAdapter0EnableDNSRegistration=TRUE
 OSDAdapter0DNSSuffix=WoodGroveBank.com

<!-- p.1075 -->

OSDAnswerFilePath
Specifies the path to the answer file to be used during OEM deployments.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                              ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ❌                |

 MDT DB               ❌                |   ZTI (Configuration Manager)   ❌

                                                                              ﾉ   Expand table

 Value       Description

 file_path   Specifies the path to the answer file to be used during OEM deployments

                                                                              ﾉ   Expand table

 Example

 None

OSDBitLockerCreateRecoveryPassword
A Boolean value that indicates whether the process creates a recovery key for BitLocker.
The key is used for recovering data encrypted on a BitLocker volume. This key is
cryptographically equivalent to a startup key. If available, the recovery key decrypts the
VMK, which, in turn, decrypts the FVEK.

  ７ Note

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

<!-- p.1076 -->

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                            Description

 AD                               A recovery key is created.

 Not specified                    A recovery key is not created.

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] BDEInstallSuppress=NO BDEDriveLetter=S:
 BDEDriveSize=2000 OSDBitLockerMode=TPMKey OSDBitLockerCreateRecoveryPassword=AD
 OSDBitLockerStartupKeyDrive=C:

OSDBitLockerMode
The type of BitLocker installation to be performed. Protect the target computer using
one of the following methods:

      A TPM microcontroller

      A TPM and an external startup key (using a key that is typically stored on a UFD)

      A TPM and PIN

      An external startup key

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

<!-- p.1077 -->

 Component             Configured By      |   Scenario                         Property Is Applicable

 MDT DB                ✅                  |   ZTI (Configuration Manager)      ✅

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

            Note:

            This value is not valid when using ZTI.

 Key        Protect the computer with an external key (the recovery key) that can be stored in a
            folder, in AD DS, or printed.

                                                                                     ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] BDEInstallSuppress=NO BDEDriveLetter=S:
 BDEDriveSize=2000 OSDBitLockerMode=TPM OSDBitLockerCreateRecoveryPassword=AD

OSDBitLockerRecoveryPassword
Instead of generating a random recovery password, the Enable BitLocker task sequence
action uses the specified value as the recovery password. The value must be a valid
numerical BitLocker recovery password.

                                                                                     ﾉ    Expand table

 Component             Configured By      |   Scenario                         Property Is Applicable

 BootStrap.ini         ❌                  |   LTI (Stand-alone MDT)            ✅

 CustomSettings.ini    ✅                  |

<!-- p.1078 -->

 Component            Configured By   |    Scenario                      Property Is Applicable

 MDT DB               ✅               |    ZTI (Configuration Manager)   ✅

                                                                              ﾉ    Expand table

 Value                       Description

 password                    A valid 48-digit password

                                                                              ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] BDEInstallSuppress=NO BDEDriveLetter=S:
 BDEDriveSize=2000 OSDBitLockerMode=TPMKey OSDBitLockerCreateRecoveryPassword=AD
 OSDBitLockerRecoveryPassword=621280128854709621167486709731081433315062587367
 OSDBitLockerStartupKeyDrive=C:

OSDBitLockerStartupKey
Instead of generating a random startup key for the key management option Startup Key
on USB only, the Enable BitLocker task sequence action uses the value as the startup
key. The value must be a valid, Base64-encoded BitLocker startup key.

                                                                              ﾉ    Expand table

 Component            Configured By   |    Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |    LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |    ZTI (Configuration Manager)   ✅

                                                                              ﾉ    Expand table

 Value                  Description

 startupkey             Base64-encoded BitLocker startup key

                                                                              ﾉ    Expand table

<!-- p.1079 -->

 Example

 [Settings] Priority=Default [Default] BDEInstallSuppress=NO BDEDriveLetter=S:
 BDEDriveSize=2000 BDEInstall=KEY OSDBitLockerCreateRecoveryPassword=AD
 OSDBitLockerStartupKey=8F4922B8-2D8D-479E-B776-12629A361049

OSDBitLockerStartupKeyDrive
The location for storing the BitLocker recovery key and startup key.

                                                                                    ﾉ   Expand table

 Component             Configured By     |   Scenario                        Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini    ✅                 |

 MDT DB                ✅                 |   ZTI (Configuration Manager)     ✅

                                                                                    ﾉ   Expand table

 Value      Description

 location   The storage location for the recovery key and startup key (either local to the target
            computer or to a UNC that points to a shared network folder)

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] BDEInstallSuppress=NO BDEDriveLetter=S:
 BDEDriveSize=2000 OSDBitLockerMode=TPMKey OSDBitLocker CreateRecoveryPassword=AD
 OSDBitLockerStartupKeyDrive=C:

OSDBitLockerTargetDrive
Specifies the drive to be encrypted. The default drive is the drive that contains the
operating system.

                                                                                    ﾉ   Expand table

<!-- p.1080 -->

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value                Description

 drive                The drive that is to be encrypted

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] BDEInstallSuppress=NO BDEDriveLetter=S:
 BDEDriveSize=2000 BDERecoveryPassword=TRUE OSDBitLockerMode=TPMKey
 OSDBitLockerCreateRecoveryPassword=AD OSDBitLockerTargetDrive=C:

OSDBitLockerWaitForEncryption
Specifies that the deployment process should not proceed until BitLocker has completed
the encryption process for all specified drives. Specifying TRUE could dramatically
increase the time required to complete the deployment process.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                 ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)   ✅
