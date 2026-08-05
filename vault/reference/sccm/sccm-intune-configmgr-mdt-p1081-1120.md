---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1081-1120"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1081-1120
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1081-1120
family: sccm
documentKind: "doc"
abstract: "ﾉ Expand table Value Description TRUE Specifies that the deployment process should wait for drive encryption to finish FALSE Specifies that the deployment process should not wait for drive encryption to finish ﾉ Expand table Example [Settings] Priority=Default [Default] BDEInsta"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1081-1120

<!-- p.1081 -->

                                                                                  ﾉ    Expand table

 Value     Description

 TRUE      Specifies that the deployment process should wait for drive encryption to finish

 FALSE     Specifies that the deployment process should not wait for drive encryption to finish

                                                                                  ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] BDEInstallSuppress=NO BDEDriveLetter=S:
 BDEDriveSize=2000 OSDBitLockerMode=TPMKey OSDBitLockerStartupKeyDrive=C:
 OSDBitLockerCreateRecoveryPassword=AD OSDBitLockerWaitForEncryption=TRUE

OSDComputerName
The new computer name to assign to the target computer.

  ７ Note

  This property can also be set within a task sequence using a customized Set Task
  Sequence Variable task sequence step.

                                                                                  ﾉ    Expand table

 Component               Configured By   |   Scenario                       Property Is Applicable

 BootStrap.ini           ❌               |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini      ✅               |

 MDT DB                  ✅               |   ZTI (Configuration Manager)    ✅

                                                                                  ﾉ    Expand table

 Value                    Description

 computer_name            The new computer name to assign to the target computer

                                                                                  ﾉ    Expand table

<!-- p.1082 -->

 Example

 [Default] OSDComputerName=%_SMSTSMachineName%

OSDDiskAlign
This property is used to pass a value to the align parameter of the create partition
primary command in the DiskPart command. The align parameter is typically used with
hardware RAID Logical Unit Number (LUN) arrays to improve performance when the
logical units (LUs) are not cylinder aligned. The align parameter aligns a primary
partition that is not cylinder aligned at the beginning of a disk and rounds the offset to
the closest alignment boundary. For more information on the align parameter, see
Create partition primary       .

  ７ Note

  This property can be used in conjunction with the OSDDiskOffset property to set
  the offset parameter for the create partition primary command in the DiskPart
  command. For more information, see the OSDDiskOffset property.

                                                                                    ﾉ   Expand table

 Component              Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)    ❌

                                                                                    ﾉ   Expand table

 Value                Description

 alignment_value      Specifies the number of kilobytes (KB) from the beginning of the disk to the
                      closest alignment boundary.

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDDiskAlign=1024 OSDDiskOffset=2048

<!-- p.1083 -->

OSDDiskIndex
Specifies the disk index that will be configured.

                                                                                      ﾉ   Expand table

 Component             Configured By       |   Scenario                        Property Is Applicable

 BootStrap.ini         ❌                   |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini    ✅                   |

 MDT DB                ✅                   |   ZTI (Configuration Manager)     ✅

                                                                                      ﾉ   Expand table

 Value           Description

 disk_index      Specifies the disk index that will be configured (The default value is 0.)

                                                                                      ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDDiskIndex=0

OSDDiskOffset
This property is used to pass a value to the offset parameter of the create partition
primary command in the DiskPart command. For more information on the offset
parameter, see Create partition primary          .

This property can be used in conjunction with the OSDDiskAlign property to set the
align parameter for the create partition primary command in the DiskPart command.
For more information, see the OSDDiskAlign property.

                                                                                      ﾉ   Expand table

 Component             Configured By       |   Scenario                        Property Is Applicable

 BootStrap.ini         ❌                   |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini    ✅                   |

 MDT DB                ✅                   |   ZTI (Configuration Manager)     ❌

<!-- p.1084 -->

                                                                                     ﾉ   Expand table

 Value           Description

 offset_value    Specifies the byte offset at which to create the partition. For master boot record
                 (MBR) disks, the offset rounds to the closest cylinder boundary.

                                                                                     ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDDiskAlign=1024 OSDDiskOffset=2048

OSDDiskPartBiosCompatibilityMode
This property specifies whether to disable cache alignment optimizations when
partitioning the hard disk for compatibility with certain types of BIOS.

                                                                                     ﾉ   Expand table

 Component              Configured By      |   Scenario                        Property Is Applicable

 BootStrap.ini          ❌                  |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini     ✅                  |

 MDT DB                 ✅                  |   ZTI (Configuration Manager)     ✅

                                                                                     ﾉ   Expand table

 Value    Description

 TRUE     Enables cache alignment optimizations when partitioning the hard disk for compatibility
          with certain types of BIOS

 FALSE    Disables cache alignment optimizations when partitioning the hard disk for compatibility
          with certain types of BIOS (This is the default value.)

                                                                                     ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDDiskPartBiosCompatibilityMode=TRUE

OSDImageCreator

<!-- p.1085 -->

Specifies the name of the installation account that will be used during OEM
deployments.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                ﾉ   Expand table

 Component            Configured By    |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ❌                |

 MDT DB               ❌                |   ZTI (Configuration Manager)    ✅

                                                                                ﾉ   Expand table

 Value           Description

 image_creator   Specifies the name of the installation account that will be used during OEM
                 deployments

                                                                                ﾉ   Expand table

 Example

 None

OSDImageIndex
Specifies the index of the image in the .wim file. This property is referenced during OEM
deployments.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                ﾉ   Expand table

<!-- p.1086 -->

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌                 |

 MDT DB                 ❌                 |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value           Description

 index           Specifies the index of the image in the WIM file

                                                                                 ﾉ   Expand table

 Example

 None

OSDImagePackageID
Specifies the package ID for the image to install during OEM deployments.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                 ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌                 |

 MDT DB                 ❌                 |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value            Description

 package_ID       Specifies the package ID for the image to install during OEM deployments

<!-- p.1087 -->

                                                                                 ﾉ   Expand table

 Example

 None

OSDInstallEditionIndex
Specifies the index of the image in the WIM file. This property is referenced during OEM
deployments.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                 ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌                 |

 MDT DB                 ❌                 |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value           Description

 index           Specifies the index of the image in the WIM file

                                                                                 ﾉ   Expand table

 Example

 None

OSDInstallType
Specifies the installation type used for OEM deployments. The default is Sysprep.

  ７ Note

<!-- p.1088 -->

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                 ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌                 |

 MDT DB                 ❌                 |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value                Description

 install_type         Specifies the installation type used for OEM deployments

                                                                                 ﾉ   Expand table

 Example

 None

OSDisk
Specifies the drive used to install the operating system during OEM deployments. The
default value is C:.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                 ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌                 |

<!-- p.1089 -->

 Component               Configured By   |   Scenario                         Property Is Applicable

 MDT DB                  ❌               |   ZTI (Configuration Manager)      ✅

                                                                                   ﾉ   Expand table

 Value     Description

 disk      Specifies the drive used to install the operating system during OEM deployments

                                                                                   ﾉ   Expand table

 Example

 None

OSDPartitions
Specifies the number of defined partitions configurations. The maximum number of
partitions that can be configured is two. The default is None.

                                                                                   ﾉ   Expand table

 Component               Configured By   |   Scenario                         Property Is Applicable

 BootStrap.ini           ❌               |   LTI (Stand-alone MDT)            ✅

 CustomSettings.ini      ✅               |

 MDT DB                  ✅               |   ZTI (Configuration Manager)      ❌

                                                                                   ﾉ   Expand table

 Value            Description

 partitions       Specifies the number of defined partitions configurations

                                                                                   ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDPartitions=1 OSDPartitions0Bootable=TRUE
 OSDPartitions0FileSystem=NTFS OSDPartitions0QuickFormat=TRUE OSDPartitions0Size=60

<!-- p.1090 -->

 Example

 OSDPartitions0SizeUnits=GB OSDPartitions0Type=Primary OSDPartitions0VolumeName=OSDisk
 OSDPartitions0VolumeLetterVariable=NewDrive1

OSDPartitionsxBootable
The partition at the specified index should be set bootable. The default first partition is
set bootable.

  ７ Note

  Thex in this properties name is a placeholder for a zero-based array that contains
  partition configurations.

                                                                              ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)   ❌

                                                                              ﾉ   Expand table

 Value           Description

 TRUE            The partition should be set to bootable.

 FALSE           Do not set the partition to bootable.

                                                                              ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDPartitions0Bootable=TRUE

OSDPartitionsxFileSystem
The type of file system for the partition at the specified index. Valid values are NTFS or
FAT32.

<!-- p.1091 -->

  ７ Note

  Thex in this properties name is a placeholder for a zero-based array that contains
  partition configurations.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)   ❌

                                                                               ﾉ   Expand table

 Value                  Description

 file_system            The type of file system for the partition

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDPartitions0FileSystem=NTFS

OSDPartitionsxQuickFormat
The partition at the specified index should be quick formatted. The default is TRUE.

  ７ Note

  Thex in this properties name is a placeholder for a zero-based array that contains
  partition configurations.

<!-- p.1092 -->

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                 ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)   ❌

                                                                                 ﾉ   Expand table

 Value                Description

 TRUE                 Quick-format the partition.

 FALSE                Do not quick-format the partition.

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDPartitions0QuickFormat=TRUE

OSDPartitionsxSize
The size of the partition at the specified index.

  ７ Note

  Thex in this properties name is a placeholder for a zero-based array that contains
  partition configurations.

                                                                                 ﾉ   Expand table

<!-- p.1093 -->

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ❌

                                                                             ﾉ   Expand table

 Value                           Description

 Size                            Partition size

                                                                             ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDPartitions0Size=60 OSDPartitions0SizeUnits=GB

OSDPartitionsxSizeUnits
The units of measure used when specifying the size of the partition. Valid values are MB,
GB, or %. The default value is MB.

  ７ Note

  Thex in this properties name is a placeholder for a zero-based array that contains
  partition configurations.

                                                                             ﾉ   Expand table

 Component            Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅               |

 MDT DB               ✅               |   ZTI (Configuration Manager)   ❌

                                                                             ﾉ   Expand table

<!-- p.1094 -->

 Value           Description

 size_units      The units of measure used when specifying the size of the partition

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDPartitions0Size=60 OSDPartitions0SizeUnits=GB

OSDPartitionsxType
The type of partition to be created at the specified index.

  ７ Note

  Thex in this properties name is a placeholder for a zero-based array that contains
  partition configurations.

                                                                                    ﾉ   Expand table

 Component              Configured By       |   Scenario                       Property Is Applicable

 BootStrap.ini          ❌                   |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini     ✅                   |

 MDT DB                 ✅                   |   ZTI (Configuration Manager)    ❌

                                                                                    ﾉ   Expand table

 Value                Description

 Primary              Create a primary partition. This is the default value.

 Logical              Create a logical partition.

 Extended             Create an extended partition.

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDPartitions0Type=Primary

<!-- p.1095 -->

OSDPartitionsxVolumeLetterVariable
The property that receives the drive letter that is assigned to the partition being
managed.

  ７ Note

  Thex in this properties name is a placeholder for a zero-based array that contains
  partition configurations.

                                                                                   ﾉ   Expand table

 Component            Configured By      |   Scenario                        Property Is Applicable

 BootStrap.ini        ❌                  |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini   ✅                  |

 MDT DB               ✅                  |   ZTI (Configuration Manager)     ❌

                                                                                   ﾉ   Expand table

 Value                    Description

 volume_letter_variable   The name of the variable that will be assigned the drive letter of the
                          partition being managed

                                                                                   ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDPartitions0VolumeLetterVariable=NewDrive1

OSDPartitionsxVolumeName
The volume name that will be assigned to the partition at the specified index.

  ７ Note

  Thex in this properties name is a placeholder for a zero-based array that contains
  partition configurations.

<!-- p.1096 -->

                                                                               ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)   ❌

                                                                               ﾉ   Expand table

 Value                Description

 volume_name          The volume name that will be assigned to the partition

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSDPartitions0VolumeName=OSDisk

OSDStateStorePath
LTI and ZTI use this property to set the path where the user state migration data will be
stored, which can be a UNC path, a local path, or a relative path.

  ７ Note

  The OSDStateStorePath property takes precedence over the StatePath or
  UserDataLocation property when those properties are also specified.

In a Replace Computer deployment scenario in ZTI, the Restore User State task sequence
step is skipped if the OSDStateStorePath property is set to a valid local or UNC path.
The workaround is to set the USMTLocal property to TRUE. Doing so forces ZTI
UserState.wsf to recognize the path in the OSDStateStorePath property. This is caused
by the Request State Store task sequence step being skipped and the previous value in
the OSDStateStorePath property being retained.

In a Replace Computer deployment scenario in ZTI, where user state migration data and
the entire computer are being backed up, the Backup.wim file is stored in the folder
specified in the OSDStateStorePath property. This may be caused by specifying the
wrong value for the ComputerBackupLocation property.

<!-- p.1097 -->

For example, the following CustomSettings.ini file will cause the Backup.wim file to be
stored in the same folder specified in the OSDStateStorePath property:

  ini

  USMTLocal=True
  OSDStateStorePath=\\fs1\Share\Replace

  ComputerBackupLocation=NETWORK
  BackupShare=\\fs1\Share\ComputerBackup
  BackupDir=Client01

                                                                                ﾉ   Expand table

 Component             Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                |

 MDT DB                ✅                |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value   Description

 Path    The path where the user state migration data will be stored, which can be a UNC path, a
         local path, or a relative path

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] USMTLocal=True OSDStateStorePath=\\fs1\Share\Replace
 ComputerBackupLocation=\\fs1\Share\ComputerBackup\Client01

OSDTargetSystemDrive
Specifies the drive where the operating system will be installed during OEM
deployments.

  ７ Note

<!-- p.1098 -->

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read-only.

                                                                                  ﾉ   Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ❌                 |

 MDT DB                ❌                 |   ZTI (Configuration Manager)    ❌

                                                                                  ﾉ   Expand table

 Value           Description

 system_drive    Specifies the drive where the operating system will be installed during OEM
                 deployments

                                                                                  ﾉ   Expand table

 Example

 None

OSDTargetSystemRoot
Specifies the install path where the operating system will be installed during OEM
deployments.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                  ﾉ   Expand table

 Component             Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ❌                 |

<!-- p.1099 -->

 Component              Configured By     |   Scenario                       Property Is Applicable

 MDT DB                 ❌                 |   ZTI (Configuration Manager)    ❌

                                                                                   ﾉ   Expand table

 Value           Description

 system_root     Specifies the install path where the operating system will be installed during OEM
                 deployments

                                                                                   ﾉ   Expand table

 Example

 None

OSFeatures
A comma-delimited list of server feature IDs that will be installed on the target
computer.

  ７ Note

  Not all features listed in the ServerManager.xml file are compatible with all server
  operating systems.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                   ﾉ   Expand table

 Component              Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)    ✅

<!-- p.1100 -->

                                                                                  ﾉ   Expand table

 Value      Description

 ID1,ID2    The server features that are to be installed on the target computer. Valid values are
            located in the program_files\Microsoft Deployment Toolkit\Bin\ServerManager.xml file
            on the MDT server.

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSFeatures=CMAK,MSMQ-Multicasting,RSAT

OSInstall
Indicates whether the target computer is authorized to have the target operating system
installed. If the OSInstall property is not listed, the default is to allow deployment of
operating systems to any target computer.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                  ﾉ   Expand table

 Component               Configured By   |   Scenario                       Property Is Applicable

 BootStrap.ini           ❌               |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini      ✅               |

 MDT DB                  ✅               |   ZTI (Configuration Manager)    ✅

                                                                                  ﾉ   Expand table

 Value     Description

 YES       Deployment of an operating system to the target computer is authorized. This is the
           default value.

 NO        Deployment of an operating system to the target computer is not authorized.

<!-- p.1101 -->

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSInstall=YES

OSRoles
A comma-delimited list of server role IDs that will be installed on the target computer.

  ７ Note

  Not all roles are compatible with all server operating systems.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                    ﾉ   Expand table

 Component               Configured By     |   Scenario                        Property Is Applicable

 BootStrap.ini           ❌                 |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini      ✅                 |

 MDT DB                  ✅                 |   ZTI (Configuration Manager)     ✅

                                                                                    ﾉ   Expand table

 Value           Description

 ID1,ID2         The server role that is to be installed on the target computer.

See "C:\Program Files\Microsoft Deployment Toolkit\Bin\ServerManager.xml" for valid
ID values.

                                                                                    ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSRoles=ADDS

<!-- p.1102 -->

OSRoleServices
A comma-delimited list of server role service IDs that will be installed on the target
computer.

  ７ Note

  Not all server role service IDs are compatible with all server operating systems.

                                                                                     ﾉ   Expand table

 Component              Configured By     |   Scenario                         Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)            ✅

 CustomSettings.ini     ✅                 |

 MDT DB                 ✅                 |   ZTI (Configuration Manager)      ✅

                                                                                     ﾉ   Expand table

 Value    Description

 ID       The server role service that will be installed on the target computer. The valid value is:

          - ADDS-Domain-Controller

                                                                                     ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] OSRoleServices=ADDS-Domain-Controller

OSSKU
The edition of the currently running operating system. The operating system edition is
determined by using the OperatingSystemSKU property of the
Win32_OperatingSystem WMI class. For a list of the editions the OperatingSystemSKU
property returns, see the section, "OperatingSystemSKU," at Win32_OperatingSystem
class .

  ７ Note

<!-- p.1103 -->

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                ﾉ   Expand table

 Component               Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini      ❌               |

 MDT DB                  ❌               |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value     Description

 edition   The operating system edition. For example, "BUSINESS" for a Business edition of an
           operating system or "ENTERPRISE" for an Enterprise edition of an operating system.

                                                                                ﾉ   Expand table

 Example

 None

OSVersion
The version of the currently running operating system. This property should only be
used to detect if the currently running operating system is Windows PE. Use the
OSVersionNumber property to detect other operating systems.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                ﾉ   Expand table

 Component               Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini           ❌               |   LTI (Stand-alone MDT)         ✅

<!-- p.1104 -->

 Component              Configured By     |   Scenario                      Property Is Applicable

 CustomSettings.ini     ❌                 |

 MDT DB                 ❌                 |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value           Description

 WinPE           Windows PE

 2008R2          Windows Server 2008 R2

 Win7Client      Windows 7

 Other           Operating systems other than those listed, including Windows 8 and Windows
                 Server 2012

                                                                                 ﾉ   Expand table

 Example

 None

OSVersionNumber
The operating system major and minor version number. This property is referenced
during OEM deployments.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                 ﾉ   Expand table

 Component              Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌                 |

 MDT DB                 ❌                 |   ZTI (Configuration Manager)   ✅

<!-- p.1105 -->

                                                                                ﾉ   Expand table

 Value                    Description

 version_number           The operating system major and minor version number

                                                                                ﾉ   Expand table

 Example

 None

OverrideProductKey
The Multiple Activation Key (MAK) string to be applied after the target operating is
deployed to the target computer. The value specified in this property is used by the
ZTILicensing.wsf script during the State Restore Phase to apply the MAK to the target
operating system. The script also configures the volume licensing image to use MAK
activation instead of Key Management Service (KMS). The operating system needs to be
activated with Microsoft after the MAK is applied. This is used when the target computer
is unable to access a server that is running KMS.

                                                                                ﾉ   Expand table

 Component            Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ✅                 |   ZTI (Configuration Manager)    ✅

                                                                                ﾉ   Expand table

 Value      Description

 MAK        The MAK string to be provided to the target operating system

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] ProductKey=AAAAA-BBBBB-CCCCC-DDDDD-EEEEE-FFFFF
 OverrideProductKey=AAAAA-BBBBB-CCCCC-DDDDD-EEEEE-FFFFF

<!-- p.1106 -->

PackageGroup
A list of text values that associates operating system packages with each other (typically
based on the type of operating system package). An operating system package can be
associated with one or more package groups. The PackageGroup property allows the
operating system packages within one or more groups to be deployed to a target
computer.

The text values in the list can be any non-blank value. The PackageGroup property value
has a numeric suffix (for example, PackageGroup001 or PackageGroup002). After it is
defined, a package group is associated with a computer. A computer can be associated
with more than one package group.

  ７ Note

  Operating system packages are created on the OS Packages node in the
  Deployment Workbench.

  ７ Note

  The PackageGroup property can be specified in the format
  PackageGroup1=Updates or PackageGroup001=Updates.

                                                                               ﾉ   Expand table

 Component            Configured By     |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                 |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                 |

 MDT DB               ❌                 |   ZTI (Configuration Manager)   ❌

                                                                               ﾉ   Expand table

 Value                    Description

 package_group_name       Name of the package group to be deployed to the target computer

                                                                               ﾉ   Expand table

<!-- p.1107 -->

 Example

 [Settings] Priority=Default [Default] PackageGroup001=Updates

Packages
The list of Configuration Manager packages to be deployed to the target computer. The
Packages property has a numeric suffix (for example, Packages001 or Packages002).

  ７ Note

  The PackageGroup property can be specified in the format
  PackageGroup1=Updates or PackageGroup001=Updates.

                                                                              ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ❌

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)   ✅

                                                                              ﾉ   Expand table

 Value                          Description

 package_id:program_name        Name of the package to be deployed to the target computer

                                                                              ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] Packages001=NYC00010:Install
 Packages002=NYC00011:Install

PackageSelectionProfile
Profile name used during package installation.

                                                                              ﾉ   Expand table

<!-- p.1108 -->

 Component            Configured By      |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                  |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                  |

 MDT DB               ✅                  |   ZTI (Configuration Manager)   ❌

                                                                                 ﾉ   Expand table

 Value                    Description

 profile_name             Profile name used during package installation

                                                                                 ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] PackageSelectionProfile=CoreApplications

Parameters
The parameters to be passed to a database query that returns property values from
columns in the table specified in the Table property. The table is located in the database
specified in the Database property on the computer specified in the SQLServer
property. The instance of SQL Server on the computer is specified in the Instance
property.

                                                                                 ﾉ   Expand table

 Component            Configured By      |   Scenario                      Property Is Applicable

 BootStrap.ini        ✅                  |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                  |

 MDT DB               ❌                  |   ZTI (Configuration Manager)   ✅

                                                                                 ﾉ   Expand table

 Value                            Description

 parameter1, parameter2           The list of parameters to pass to the database query

<!-- p.1109 -->

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Computers, Default [Default] OSInstall=YES [Computers] SQLServer=NYC-
 SQL-01 SQLShare=SQL$ Database=MDTDB Instance=SQLEnterprise2005 Table=Computers
 Parameters=SerialNumber, AssetTag ParameterCondition=OR

ParameterCondition
Indicator of whether a Boolean AND or OR operation is performed on the properties
listed in the Parameters property.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                                  ﾉ   Expand table

 Component             Configured By    |   Scenario                        Property Is Applicable

 BootStrap.ini         ✅                |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini    ✅                |

 MDT DB                ❌                |   ZTI (Configuration Manager)     ✅

                                                                                  ﾉ   Expand table

 Value   Description

 AND     A Boolean AND operation is performed on the properties listed in the Parameters
         property. Only results that match all properties specified in the Parameters property are
         returned. This is the default value.

 OR      A Boolean OR operation is performed on the properties listed in the Parameters property.
         Results that match any property specified in the Parameters property are returned.

                                                                                  ﾉ   Expand table

 Example

 [Settings] Priority=Computers, Default [Default] OSInstall=YES [Computers] SQLServer=NYC-
 SQL-01 SQLShare=SQL$ Database=MDTDB Instance=SQLEnterprise2005 Table=Computers

<!-- p.1110 -->

 Example

 Parameters=SerialNumber, AssetTag ParameterCondition=OR

ParentDomainDNSName
Specifies the DNS domain name of an existing directory service domain when installing
a child domain.

                                                                               ﾉ   Expand table

 Component             Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅               |

 MDT DB                ✅               |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value   Description

 name    Specifies the DNS domain name of an existing directory service domain when installing a
         child domain

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] ParentDomainDNSName=WoodGroveBank.com

Password
Specifies the password for the user name (account credentials) to use for promoting the
member server to a domain controller.

                                                                               ﾉ   Expand table

 Component             Configured By   |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌               |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅               |

<!-- p.1111 -->

 Component            Configured By    |   Scenario                      Property Is Applicable

 MDT DB               ✅                |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value      Description

 password   Specifies the password for the user name (account credentials) to use for promoting
            the member server to a domain controller

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] Password=<complex_password>

Phase
The current phase of the deployment process. The Task Sequencer uses these phases to
determine which tasks must be completed.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

  Ｕ Caution

  This property value must be specified in uppercase letters so that the deployment
  scripts can properly read it.

                                                                               ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ❌                |

 MDT DB               ❌                |   ZTI (Configuration Manager)   ✅

<!-- p.1112 -->

                                                                                 ﾉ   Expand table

 Value            Description

 VALIDATION       Identifies that the target computer is capable of running the scripts necessary
                  to complete the deployment process.

 STATECAPTURE     Saves any user state migration data before deploying the new target operating
                  system.

 PREINSTALL       Completes any tasks that need to be done (such as creating new partitions)
                  before the target operating system is deployed.

 INSTALL          Installs the target operating system on the target computer.

 POSTINSTALL      Completes any tasks that need to be done before restoring the user state
                  migration data. These tasks customize the target operating system before
                  starting the target computer the first time (such as installing updates or adding
                  drivers).

 STATERESTORE     Restores the user state migration data saved during the State Capture Phase.

                                                                                 ﾉ   Expand table

 Example

 None

Port
The number of the port that should be used when connecting to the SQL Server
database instance that is used for querying property values from columns in the table
specified in the Table property. The database resides on the computer specified in the
SQLServer property. The instance of SQL Server on the computer is specified in the
Instance property. The port used during connection is specified in the Port property.

                                                                                 ﾉ   Expand table

 Component            Configured By    |   Scenario                        Property Is Applicable

 BootStrap.ini        ✅                |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini   ✅                |

 MDT DB               ❌                |   ZTI (Configuration Manager)     ✅

<!-- p.1113 -->

                                                                              ﾉ   Expand table

 Value      Description

 port       The number of the port used when connecting to SQL Server

                                                                              ﾉ   Expand table

 Example

 [Settings] Priority=Computers, Default [Default] OSInstall=YES [Computers] SQLServer=NYC-
 SQL-01 Database=MDTDB Instance=MDT2010 Port=1433 Table=Computers Parameters=SerialNumber,
 AssetTag ParameterCondition=OR

PowerUsers
A list of user accounts and domain groups to be added to the local Power Users group
on the target computer. The PowerUsers property is a list of text values that can be any
non-blank value. The PowerUsers property has a numeric suffix (for example,
PowerUsers1 or PowerUsers2).

                                                                              ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)   ✅

                                                                              ﾉ   Expand table

 Value     Description

 name      Name of the user or group to be added to the local Power Users group

                                                                              ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] Administrators001=WOODGROVEBANK\NYC Help Desk Staff
 PowerUsers001=WOODGROVEBANK\User01 PowerUsers002=WOODGROVEBANK\User02

<!-- p.1114 -->

PrepareWinRE
This property specifies if the LiteTouchPE.wim file, which includes Windows RE and
optionally DaRT, is applied to the system drive as the recovery partition. This allows the
target computer to use the LiteTouchPE.wim image to perform recovery tasks. DaRT may
optionally be included in the image, which makes DaRT recovery features available on
the target computer.

                                                                                    ﾉ    Expand table

 Component               Configured By     |   Scenario                       Property Is Applicable

 BootStrap.ini           ❌                 |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini      ✅                 |

 MDT DB                  ❌                 |   ZTI (Configuration Manager)    ❌

                                                                                    ﾉ    Expand table

 Value           Description

 YES             The LiteTouchPE.wim file, which includes Windows RE and optionally DaRT, is applied
                 to the system drive as the recovery partition.

 any other       The LiteTouchPE.wim file, which includes Windows RE and optionally DaRT, is not
 value           applied to the system drive as the recovery partition. This is the default value.

                                                                                    ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] PrepareWinRE=YES

Priority
The reserved property that determines the sequence for finding configuration values.
The Priority reserved property lists each section to be searched and the order in which
the sections are searched. When a property value is found, the ZTIGather.wsf script quits
searching for the property, and the remaining sections are not scanned for that
property.

                                                                                    ﾉ    Expand table

<!-- p.1115 -->

 Component            Configured By    |   Scenario                       Property Is Applicable

 BootStrap.ini        ✅                |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ✅                |

 MDT DB               ❌                |   ZTI (Configuration Manager)    ✅

                                                                                ﾉ   Expand table

 Value                 Description

 section1, section2    The sections to be searched in the order they are to be searched

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=MACAddress, Default [Default] UserDataLocation=NONE CustomProperty=TRUE
 [00:0F:20:35:DE:AC] OSDNEWMACHINENAME=HPD530-1 [00:03:FF:FE:FF:FF] OSDNEWMACHINENAME=BVMXP

ProcessorSpeed
The speed of the processor installed on the target computer in MHz. For example, the
value 1995 indicates the processor on the target computer is running at 1,995 MHz or 2
gigahertz.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                ﾉ   Expand table

 Component            Configured By    |   Scenario                       Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini   ❌                |

 MDT DB               ❌                |   ZTI (Configuration Manager)    ✅

                                                                                ﾉ   Expand table

<!-- p.1116 -->

 Value                  Description

 processor_speed        The speed of the processor on the target computer in megahertz

                                                                                ﾉ   Expand table

 Example

 None

Product
The product name of the target computer. With some computer vendors, the make and
model might not be sufficiently unique to identify the characteristics of a particular
configuration (for example, hyperthreaded or non-hyperthreaded chipsets). The Product
property can help to differentiate.

The format for Product is undefined. Use this property to create a subsection that
contains settings targeted to a specific product name for a specific computer model
number for a specific computer manufacturer (most commonly in conjunction with the
Make and Model properties).

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                ﾉ   Expand table

 Component              Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini          ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini     ❌                |

 MDT DB                 ❌                |   ZTI (Configuration Manager)   ✅

                                                                                ﾉ   Expand table

 Value                Description

 product              The product name of the target computer

<!-- p.1117 -->

                                                                               ﾉ   Expand table

 Example

 None

ProductKey
The product key string to be configured for the target computer. Before the target
operating system is deployed, the product key specified is automatically inserted into
the appropriate location in Unattend.xml.

                                                                               ﾉ   Expand table

 Component             Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini         ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini    ✅                |

 MDT DB                ✅                |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                Description

 product_key          The product key to be assigned to the target computer

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] ProductKey=AAAAA-BBBBB-CCCCC-DDDDD-EEEEE-FFFFF

Properties
A reserved property that defines any custom, user-defined properties. These user-
defined properties are located by the ZTIGather.wsf script in the CustomSettings.ini file,
BootStrap.ini file, or the MDT DB. These properties are additions to the predefined
properties in MDT.

                                                                               ﾉ   Expand table

<!-- p.1118 -->

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ✅                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                |

 MDT DB               ❌                |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value                                      Description

 custom_property1,custom_property2          Custom, user-defined properties to be resolved

                                                                               ﾉ   Expand table

 Example

 [Settings] Priority=MACAddress, Default Properties=CustomProperty, ApplicationInstall
 [Default] OSInstall=YES ScanStateArgs=/v:5 /o /c LoadStateArgs=/v:5 /c /lac
 UserDataLocation=NONE CustomProperty=TRUE [00:0F:20:35:DE:AC] OSDNEWMACHINENAME=HPD530-1
 ApplicationInstall=Custom [00:03:FF:FE:FF:FF] OSDNEWMACHINENAME=BVMXP
 ApplicationInstall=Minimum

ReplicaDomainDNSName
Specifies the DNS domain name of the domain to replicate.

                                                                               ﾉ   Expand table

 Component            Configured By    |   Scenario                      Property Is Applicable

 BootStrap.ini        ❌                |   LTI (Stand-alone MDT)         ✅

 CustomSettings.ini   ✅                |

 MDT DB               ✅                |   ZTI (Configuration Manager)   ✅

                                                                               ﾉ   Expand table

 Value       Description

 name        Specifies the DNS domain name of the domain to replicate

                                                                               ﾉ   Expand table

<!-- p.1119 -->

 Example

 [Settings] Priority=Default [Default] ReplicaDomainDNSName=WoodGroveBank.com

ReplicaOrNewDomain
Specifies whether to install a new domain controller as the first domain controller in a
new directory service domain or to install it as a replica directory service domain
controller.

                                                                                     ﾉ    Expand table

 Component               Configured By     |   Scenario                        Property Is Applicable

 BootStrap.ini           ❌                 |   LTI (Stand-alone MDT)           ✅

 CustomSettings.ini      ✅                 |

 MDT DB                  ✅                 |   ZTI (Configuration Manager)     ✅

                                                                                     ﾉ    Expand table

 Value        Description

 Replica      Installs the new domain controller as a replica directory service domain controller.

 Domain       Installs the new domain controller as the first domain controller in a new directory
              service domain. You must specify the TreeOrChild entry with a valid value.

                                                                                     ﾉ    Expand table

 Example

 [Settings] Priority=Default [Default] ReplicaOrNewDomain=Domain

ReplicationSourceDC
Indicates the full DNS name of the domain controller from which you replicate the
domain information.

                                                                                     ﾉ    Expand table

<!-- p.1120 -->

 Component             Configured By   |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌               |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ✅               |

 MDT DB                ✅               |   ZTI (Configuration Manager)    ✅

                                                                                ﾉ   Expand table

 Value   Description

 name    Indicates the full DNS name of the domain controller from which you replicate the
         domain information

                                                                                ﾉ   Expand table

 Example

 [Settings] Priority=Default [Default] ReplicationSourceDC=dc01.WoodGroveBank.com

ResourceDrive
The drive letter mapped to the ResourceRoot property for the ZTIDrivers.wsf and
ZTIPatches.wsf scripts to use to install drivers and patches to the target computer.

  ７ Note

  This property is dynamically set by the MDT scripts and is not configured in
  CustomSettings.ini or the MDT DB. Treat this property as read only.

                                                                                ﾉ   Expand table

 Component             Configured By   |   Scenario                       Property Is Applicable

 BootStrap.ini         ❌               |   LTI (Stand-alone MDT)          ✅

 CustomSettings.ini    ❌               |

 MDT DB                ❌               |   ZTI (Configuration Manager)    ✅

                                                                                ﾉ   Expand table
