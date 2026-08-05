---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 401-440"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0401-0440
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0401-0440
family: sccm
documentKind: "doc"
abstract: "Configuring the Appropriate MDT Properties MDT uses wizards to create and manage configuration files. For more information about the standard MDT configuration files, CustomSettings.ini and BootStrap.ini, see Customizing MDT Configuration Files. However, you can customize config"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 401-440

<!-- p.401 -->

Configuring the Appropriate MDT Properties
MDT uses wizards to create and manage configuration files. For more information about
the standard MDT configuration files, CustomSettings.ini and BootStrap.ini, see
Customizing MDT Configuration Files. However, you can customize configuration files to
meet the needs of your organization.

Before configuring the deployment process, select the properties to reference from the
predefined or user-defined properties. The properties selected must include all the
configuration settings to be supplied during the deployment process.

For ZTI deployments using Configuration Manager, provide all configuration settings
required to deploy the target operating system. For LTI deployments, provide a subset
of the configuration settings that are provided automatically; the remainder of the
settings can be provided manually during the deployment process.

The MDT process occurs in the phases defined in the TS.xml file. The Task Sequencer
parses the TS.xml file to identify the appropriate sequence for performing the
deployment process. The phases defined in the TS.xml file include:

     Validate Phase. Performs validation checks to make sure that the operating system
     installation can proceed; specifically blocks installation on server operating
     systems.

     State Capture Phase. Gathers information from the configuration file, databases,
     and the local machine to determine how the image installation process should
     proceed, including whether there is enough space to do a local USMT state
     backup. The scripts also invoke the USMT Scanstate.exe command as appropriate.

     Preinstall Phase. Confirms that the necessary information has been gathered in the
     State Capture Phase for the Refresh Computer scenario. In the New Computer and
     Replace Computer scenarios, the script gathers the necessary information in this
     phase, because these scenarios do not perform the State Capture Phase. Also, a
     backup of the computer can be optionally performed for the Refresh Computer
     scenario.

     Install Phase. Installs the target operating system on the target computers.

     Post Install Phase. Updates the Unattend.xml with information gathered in the
     previous custom actions based on the operating system being deployed.

     State Restore Phase. Invokes the USMT Loadstate.exe command to restore the
     user state that was previously backed up.

<!-- p.402 -->

     The TS.xml file identifies the appropriate steps in each phase based on each type
     of deployment scenario (Refresh Computer, Replace Computer, and New
     Computer). Select the properties required during each phase of the deployment
     process.

     For more information on each of the properties used in each phase, see the
     section, "Properties", in the MDT document Toolkit Reference.

Applying MDT Properties to Groups of Computers
Whenever possible, use group-based rules to apply most computer configuration
settings. Group-based rules allow the same configuration settings to be applied to a
group of client computers. After applying group-based rules, you can supply computer-
specific configuration settings using computer-based rules.

Apply properties to groups of computers by performing the following steps:

   1. Select the method of grouping multiple computers as described in Select the
     Method for Grouping Computers.

   2. Apply the properties to the groupings of computers as described in Apply the
     Properties to the Groups.

Select the Method for Grouping Computers
Different methods can be used to group client computers. After determining how to
group the computers, select the appropriate properties to help group them.

Using the processing rules in MDT, group computers based on any property that might
be applied to a group of computers (such as Make, Model, or DefaultGateway). Table
155 lists methods of grouping computers, a description of the method, and the
properties that can be used to group the computers.

Table 155. Methods for Grouping Computers

                                                                          ﾉ   Expand table

 Grouping          Description                           Properties
 method

 Geographically    Group configuration settings based    DefaultGateway
                   on resources located within a
                   geographic region (such as a shared

<!-- p.403 -->

 Grouping             Description                             Properties
 method

                      folder on a computer within a
                      geographic region).

 Target computer      Group configuration settings based      ArchitectureCapableArchitectureMake
 hardware             on hardware attributes (such as the
 attributes           make of the computer or processor
                      architecture of the target
                      computer).

 Target computer      Group configuration settings based      OSVersion
 software             on hardware attributes (such as the
 attributes           operating system version of the
                      target computer).

 Default attributes   Apply configuration settings to all     Default
                      target computers when the
                      properties are not in other sections.

In most instances, computer groupings can be nested. For example, you can use the
DefaultGateway property to designate the IP subnets on which a computer resides
within a geographic location. Define locations using the user-defined properties in the
[DefaultGateway] section, as shown in Listing 11.

  ７ Note

  A variety of methods can be used to group computers by hardware configuration,
  and the script will search for the substituted value regardless. For instance, if you
  specify Priority=Make , the script substitutes the value for Make that it determines
  through a Windows Management Instrumentation (WMI) call and will look for the
  corresponding section—for example, [Dell Computer Corporation] .

Example: Computer Groupings Selected by Woodgrove Bank

Listing 11 shows an example of how the fictional company, Woodgrove Bank, used
[DefaultGateway] to designate the configuration settings for a specific location. Three

subnets (172.16.0.3, 172.16.1.3, and 172.16.2.3) reside within the NYC location. A
separate section, [NYC] , includes the configuration settings specific to the NYC location.
Similar sections exist for the DALLAS and WASHINGTON locations. This is a special case
that allows multiple default gateways to point to the same section. In many
environments, a one-to-one mapping might be expected between the [DefaultGateway]
section and a corresponding section.

<!-- p.404 -->

Listing 11. Using [DefaultGateway] to Designate Location-Specific Configuration
Settings

  ini

  [Settings]
  Priority=DefaultGateway

  [DefaultGateway]
  172.16.0.3=NYC
  172.16.1.3=NYC
  172.16.2.3=NYC
  172.16.111.3=DALLAS
  172.16.112.3=DALLAS
  172.16.116.3=WASHINGTON
  172.16.117.3=WASHINGTON

  [NYC]
  UDShare=\\NYC-AM-FIL-01\MigData
  SLShare=\\NYC-AM-FIL-01\Logs
  Packages1=NYC00010-Install
  Packages2=NYC00011-Install
  Administrator1=WOODGROVEBANK\NYC Help Desk Staff

  [DALLAS]
  UDShare=\\DAL-AM-FIL-01\MigData
  SLShare=\\DAL-AM-FIL-01\Logs
  Administrator1=WOODGROVEBANK\DAL Help Desk Staff

Apply the Properties to the Groups
After identifying how to group configuration settings, determine which properties and
corresponding configuration settings to apply to each group. Properties that can be
grouped are those you can apply to multiple computers.

Some examples of properties that are typically applied to groups of computers include:

        BackupDir

        BackupShare

        CaptureGroups

        ComputerBackupLocation

        Packages

        SLShare

<!-- p.405 -->

     UDDir

     UDShare

     UDProfiles

     Properties that are not applied to groups of computers are those specific to a
     particular computer. Examples of properties that are not appropriate to apply to
     groups of computers include:

     OSDAdapter0IPAddress

     OSDNewMachineName

     Example: Group-based Configuration Settings Selected by Woodgrove Bank

     Listing 11 showed an example in which Woodgrove Bank selects group-based
     configuration settings:

     In the NYC and DALLAS locations, UDShare , SLShare , and Administrator1 are
     specified for each location.

     The servers that UDShare and SLSShare ( NYC-AM-FIL-01 and DAL-AM-FIL-01 )
     reference are within each respective location.

     The Administrator accounts that Administrator1 ( WOODGROVEBANK\NYC Help Desk
     Staff and WOODGROVEBANK\DAL Help Desk Staff ) reference are unique to each

     respective location.

     In NYC, location-specific packages are designated by Packages1 and Packages2 .

Applying MDT Properties to Individual Computers
After determining the groupings of target computers and configuration settings to be
applied to each group, determine the method for identifying individual computers and
the configuration settings to assign to each computer. The rules for target computers
allow the override or augmentation of group-based processing rules based on the
priority of the computer-based rules.

For more information about determining the priority of processing rules, see Priority
Reserved Property, earlier in this guide.

Whenever possible, use group-based rules for most client computer configuration
settings. Group-based rules allow the same configuration settings to be applied to a

<!-- p.406 -->

group of computers. After applying group-based rules, you can apply computer-specific
configuration settings using computer-based rules.

As when grouping computers, more than one method is available for identifying
individual computers. After selecting the method for identifying an individual target
computer, select the appropriate properties.

The processing rules allow the identification of computers based on any property that
you might apply to an individual of computer (such as AssetTag, MACAddress, UUID,
and so on).

Table 156 lists the methods of identifying individual computers, a description of the
method, and the properties that you can use to identify the individual computers.

Table 156. Methods for Identifying Individual Computers

                                                                               ﾉ   Expand table

 Identification        Description                                Properties
 method

 Target computer       Identify the target computer using the     AssetTag, MACAddress,
 hardware attributes   hardware configuration.                    SerialNumber, UUID,
                                                                  Product, Make, and Model

 Target computer       Identify the target computer using the     OSVersion, IsServerOS, and
 software attributes   software or firmware configuration.        OSSKU

 Target computer       Identify the target computer using         AssetTag SerialNumber
 user-defined          attributes that are assigned to the
 attributes            computer but not part of the hardware or
                       software configuration.

Example: Computer Identification Method Selected by Woodgrove

Listing 12 shows an example of how Woodgrove Bank identified computer-based
configuration settings. In this instance, Woodgrove used the MAC address of the
computer to identify the corresponding configuration settings for the computer (for
example, 00:03:FF:CB:4E:C2 and 00:0F:20:35:DE:AC ). The configuration settings for each
computer are listed immediately after the section that corresponds to the computer's
MAC address.

Listing 12. How Woodgrove Identified Client Computers

  ini

<!-- p.407 -->

  [00:03:FF:CB:4E:C2]
  ComputerName=WasW2K
  OverRideProductKey=TTTTT-VVVVV-WWWWW-XXXXX-YYYYY

  [00:0F:20:35:DE:AC]
  ComputerName=HPD530-1
  OverRideProductKey=AAAAA-BBBBB-CCCCC-DDDDD-EEEEE

  [00:03:FF:FE:FF:FF]
  ComputerName=BVMXP
  OverRideProductKey=11111-22222-33333-44444-55555

Example: Computer-based Configuration Settings Selected by Woodgrove

Listing 12 also shows the computer-based configuration settings that Woodgrove Bank
selected. Table 157 lists the computer-specific configuration settings applied to each
computer.

Table 157. Woodgrove Client Computers and the
Corresponding Configuration Settings

                                                                              ﾉ   Expand table

 Target computer       Settings and description

 [00:03:FF:CB:4E:C2]   ComputerName is the name of the computer after deployment—in this case,
                       WasW2K. OverRideProductKey is the product key to be assigned to the
                       computer—in this case, TTTTT-VVVVV-WWWWW-XXXXX-YYYYY.

 [00:0F:20:35:DE:AC]   ComputerName is the name of the computer after deployment—in this case,
                       HPD530-1. OverRideProductKey is the product key to be assigned to the
                       computer—in this case, AAAAA-BBBBB-CCCCC-DDDDD-EEEEE.

 [00:03:FF:FE:FF:FF]   ComputerName is the name of the computer after deployment—in this case,
                       BVMXP.

                       OverRideProductKey is the product key to be assigned to the computer—in
                       this case, 11111-22222-33333-44444-55555.

Configuring MDT Processing Rules
MDT scripts configure computer settings based on rules and configuration settings
stored in the CustomSettings.ini file or in the MDT DB. Configure the MDT processing
rules by completing the following tasks:

<!-- p.408 -->

     Configure the processing rules as described in Configure the Rules in the
     CustomSettings.ini File.

     Configure the processing rules as described in Configure the Rules in the MDT DB.

Configure the Rules in the CustomSettings.ini File
Configure rules in the CustomSettings.ini file. The template version of the
CustomSettings.ini file, along with the organization's rules, becomes the customized
CustomSettings.ini file.

For LTI deployments, configuring group-based settings might be sufficient, because
computer-specific settings can be provided during the MDT installation process. For ZTI
deployments using Configuration Manager, add configuration settings unique to a
specific client computer, because ZTI assumes that all configuration settings necessary
for deployment are configured in advance. These configuration settings can be in
addition to or instead of the group-based rules.

Configure the Rules in the MDT DB
Use the Deployment Workbench to configure the rules for LTI and ZTI deployments in
the MDT DB. The benefits of using the MDT DB include:

     It has a more generic version of CustomSettings.ini. Storing the configuration
     settings in the MDT DB removes most of the detail from the CustomSettings.ini file.
     This change helps make the CustomSettings.ini file more generic so that you can
     use the same file in multiple deployment shares.

     It is a centralized repository for all property configuration settings. Centralizing
     the configuration for all property settings ensures consistency across all
     deployment shares.

     For information about the MDT DB and using it to perform deployments, see
     Performing Deployments Using the MDT DB.

Preparing Disks on Target Computers
Prior to deploying the target operating system on a target computer, the MDT
deployment process prepares the disks on the target computer for deployment. The
disk-preparation process includes the following steps:

   1. Create partitions on one or more drives on the target computers.

<!-- p.409 -->

   2. Format one or more partitions on the target computers.

   3. Prepare the disks on the target computers for BitLocker.

     Disk preparation occurs during the State Capture and Preinstall phases in the MDT
     deployment process. The disk-preparation step completed in the State Capture
     Phase is the disabling of BitLocker on the target computer. The disk-preparation
     steps completed in the Preinstall Phase create and format the partitions on the
     target computer.

To prepare the disks on target computers in MDT

   1. Review the default partition configuration created by MDT as described in Review
     the Default Partition Configuration Created by MDT.

   2. Prepare for deployment to virtual hard disks (VHDs) with native boot as described
     in Prepare for Deployment to Virtual Hard Disks with Native Boot.

   3. Configure task sequence steps based on the Create Virtual Hard Disk task
     sequence step type as described in Configure the Create VHD Disk Task Sequence
     Step Type.

   4. Deploy to computers that support the Unified Extensible Firmware Interface
     specification as described in Deploy to Computers with UEFI.

   5. Review the task sequence steps used for saving and restoring user state
     information as described in Configure Disk Preparation Task Sequence Steps.

   6. Configure the MDT properties used in saving and restoring user state information
     as described in Configure Disk Preparation Properties.

Review the Default Partition Configuration Created by MDT
The MDT deployment processes automatically create the necessary disk partitions to
take full advantage of the features provided by the target computer and operating
system. By default, MDT creates the partition configuration for BIOS-based computers as
described in Table 158.

Table 158. Default Partition Configuration Created by
MDT for BIOS-based Computers

                                                                         ﾉ   Expand table

<!-- p.410 -->

 Partition     File     Size            Description
               system

 BDEDrive      NTFS     512 MB          Unencrypted partition used for starting Windows, also
                                        known as the system partition. This partition is used to
                                        initially start Windows until BitLocker is loaded and the
                                        operating system drive can be read. This partition can also
                                        be shared with the recovery partition.

 OSDisk        NTFS     Remaining       Partition on which Windows is located, also known as the
                        space           operating system drive. If BitLocker is used, this is the
                                        partition that is encrypted.

By default, MDT creates the partition configuration for UEFI-based computers as
described in Table 159.

Table 159. Default Partition Configuration Created by
MDT for UEFI-based Computers

                                                                                     ﾉ   Expand table

 Partition      File system    Size          Description

 Description    FAT32          512 MB        Unencrypted partition used for starting Windows. For
                                             more information, see Deploy to Computers with UEFI.
                                             This partition can also be shared with the recovery
                                             partition.

 MSR            Unformatted    128 MB        The Microsoft Reserved Partition (MSR) is a partition on
                                             a data storage device that is labeled with a GUID equal
                                             to E3C9E316-0B5C-4DB8-817D-F92DF00215AE. The
                                             containing storage device has to use the new GUID
                                             Partition Table (GPT) format, not the traditional master
                                             boot record (MBR) partition table format.An MSR
                                             partition is required on every GPT disk and should be
                                             created as the disk is initially partitioned. It should be
                                             located after the EFI System Partition (ESP) and any
                                             OEM service partitions, but—most importantly—the
                                             first data partition must immediately follow it.

 OSDisk         NTFS           Remaining     Partition on which Windows is located, also known as
                               space         the operating system drive. If BitLocker is used, this is
                                             the partition that is encrypted.

In addition to the default MDT partition configurations, you can create custom partition
configurations. For example, the default MDT partition configurations do not include

<!-- p.411 -->

other utility partitions or recovery images. For more information, see Understanding
Disk Partitions.

Prepare for Deployment to Virtual Hard Disks with Native Boot

Native boot allows VHDs to run on a computer without a VM or hypervisor.

  ７ Note

  Only LTI supports deployment to VHDs with native boot.

Native VHD boot has the following dependencies:

     The local disk must have at least two partitions: a system partition that contains
     the Windows boot environment files and Boot Configuration Data (BCD) store and
     a partition to store the VHD file.

     The local disk partition that contains the VHD file must have enough free disk
     space for expanding a dynamic VHD to its maximum size and for the page file
     created when booting the VHD. The page file is created outside of the VHD file,
     unlike in a VM, where the page file is contained inside the VHD.

     You can create LTI task sequences based on the following LTI task sequence
     templates to deploy to VHDs with native boot:

   1. Deploy to VHD Client Task Sequence. Select this LTI task sequence template to
     deploy Windows in a VHD with native boot.

   2. Deploy to VHD Server Task Sequence. Select this LTI task sequence template to
     deploy Windows Server in a VHD with native boot.

     These tasks sequences contain the following task sequence steps, which are used
     to perform deployment to VHDs:

     Create VHD Disk. The step creates the VHD file after the physical partition has
     been created and formatted. For more information about this task sequence step,
     see Configure the Create VHD Disk Task Sequence Step Type.

     Format and Partition VHD. This step formats the .vhd file and is built using the
     Format and Partition Disk task sequence step type. For more information about
     task sequence step type, see Configure Disk Preparation Task Sequence Steps.

     Clear OSDDiskIndexVariable. This step clears the OSDDiskIndexVariable task
     sequence variable that was set during the Create VHD Disk task sequence step.

<!-- p.412 -->

     Clearing the OSDDiskIndexVariable task sequence variable allows other disks to be
     partitioned and formatted as a part of the task sequence.

     For more information about VHDs with native boot, see Understanding Virtual
     Hard Disks with Native Boot.

Configure the Create VHD Disk Task Sequence Step Type

The Create VHD Disk task sequence step type creates a .vhd file in preparation to
performing a deployment to a VHD with native boot support. Table 160 describes how
to configure the Create VHD Disk task sequence step type.

Table 160. Configure Create VHD Disk Task Sequence Step
Type

                                                                                    ﾉ   Expand table

 Setting             Description

 VHD filename path   Specifies the path to the folder where the .vhd file will be created and can
                     contain one of the following value:

                     - Random. This value specifies that the task sequence step will
                     automatically create a unique folder and .vhd file name. The task sequence
                     step automatically places the .vhd file in the folder.

                     - vhd_path. In this case, vhd_path is the path to the folder where you want
                     the task sequence step to create the .vhd file, including the name of the
                     .vhd file.

                     The default value for this setting is Random.

 Diff filename       Specifies the file name for a differencing VHD file:

                     - Random. This value specifies that the task sequence step will
                     automatically create a unique folder and file name for the differencing .vhd
                     file.

                     - vhd_path. In this case, vhd_path is the path to the folder where you want
                     the task sequence step to create the differencing .vhd file, including the
                     name of the .vhd file.

                     - Blank. In this case, no differencing .vhd file is created.

                     The default value for this setting is blank, which indicates that no
                     differencing .vhd file is created.

<!-- p.413 -->

 Setting              Description

 VHD size             Specifies the capacity of the .vhd file, which can be specified in megabytes
                      or as a percentage of the available disk space.

 Dynamically          This option creates a dynamically expanding .vhd file, which will physically
 expanding            increase in size as more data is stored in the .vhd file. The other option is
                      Fixed size. This setting is the default selection.

 Fixed size           This option creates a fixed sized .vhd file, which is created as the size
                      specified in VHD size and does not automatically grow in size. The other
                      option is Dynamically expanding, which is the default selection.

 Retrieve the         This specifies the task sequence variable name used to designate the
 destination drive    destination drive for the task sequence variable. You can specify any valid
 for the VHD file     task sequence variable in this setting. The default value is the
 from a variable      VHDTargetDisk task sequence variable. For more information on the
                      VHDTargetDisk task sequence variable, see the VHDTargetDisk property in
                      the in the MDT document Toolkit Reference.

 Assign the disk      This setting specifies the task sequence variable name used to designate
 index created from   the disk index to be used in deploying the operating system. You can
 the VHD to a         specify any valid task sequence variable in this setting. The default value is
 variable             the OSDDiskIndex task sequence variable. For more information on the
                      OSDDiskIndex task sequence variable, see the OSDDiskIndex property in
                      the in the MDT document Toolkit Reference.

Deploy to Computers with UEFI
The UEFI is a specification that defines a software interface between an operating
system and platform firmware. UEFI is a more secure replacement for the older BIOS
firmware interface, present in some personal computers, which is vulnerable to malware
that performs attacks during startup or power on self-test (POST) processes.

Windows operating systems support firmware revisions that are based on the UEFI
version 2.0 or later specification on 64-bit platforms and Intel Itanium platforms.
Windows also supports firmware revisions that are based on the EFI Version 1.10
specification on Intel Itanium platforms.

Windows supports a subset of the functionality that is defined in the UEFI 2.0
specification. Windows implementations do not explicitly check against higher revisions
of the firmware. The operating system supports higher revisions of the firmware if they
contain the necessary support for Windows.

  ７ Note

<!-- p.414 -->

  The UEFI partitions must be formatted using the FAT32 file system. The NTFS file
  system is not supported for UEFI boot.

By default, MDT creates the appropriate partitions to support UEFI. If you create custom
partition configurations, ensure that you follow the recommendations described in the
Review the Default Partition Configuration Created by MDT section.

For more information, see the following resources:

     UEFI Support and Requirements for Windows Operating Systems

     Recommended UEFI-Based Disk-Partition Configurations

Configure Disk Preparation Task Sequence Steps
MDT includes task sequence templates for LTI and ZTI deployments. These task
sequence templates include the task sequence steps listed in Table 161, which are used
to perform disk-preparation steps.

Table 161. Disk Preparation Task Sequence Steps

                                                                                ﾉ   Expand table

 Task sequence step     Description

 Convert Disk to        Converts a physical disk from a basic disk type to a dynamic disk type;
 Dynamic                available in ZTI task sequences only

 Enable BitLocker       Configures BitLocker on the target computer; available for LTI and ZTI
                        task sequences

 Format and Partition   Creates partitions and formats disks on the target computer; available for
 Disk                   LTI and ZTI task sequences

 Disable BitLocker      Disables BitLocker on the current operating system drive or on a specific
                        drive; available in ZTI task sequences only

 Disable BDE            Disables the BitLocker protectors on the target computer; available in LTI
 Protectors             task sequences only

 Create Virtual Hard    Creates a .vhd file in preparation for deploying Windows to a VHD with
 Disk (VHD)             native boot support.

Configure Disk Preparation Properties

<!-- p.415 -->

Table 162 lists the MDT properties that control the preparation of disks on the target
computers. You can configure these properties in CustomSettings.ini or in the MDT DB.
For more information about the properties in Table 162, see the corresponding section
for each property in the MDT document Toolkit Reference.

Table 162. Disk Preparation Properties

                                                                               ﾉ   Expand table

 Property                            Description

 BDEDriveLetter                      The drive letter for the partition that is not encrypted with
                                     BitLocker, also known as the SYSVOL

 BDEDriveSize                        The size of the BitLocker system partition in megabytes

 BDEInstall                          The type of BitLocker installation you are performing

 BDEInstallSuppress                  Indicates whether the deployment process should skip
                                     BitLocker installation

 BDEKeyLocation                      The location for storing the BitLocker recovery key and
                                     startup key

 BDEPin                              The PIN to be assigned to the target computer when
                                     configuring BitLocker and the BDEInstall or
                                     OSDBitLockerMode properties are set to a value of
                                     TPMPin.

                                     This property can contain numeric only or alphanumeric
                                     values based on the value of the
                                     BDEAllowAlphaNumericPin property.

 BDERecoveryKey                      A Boolean value that indicates whether the process
                                     creates a recovery key for BitLocker

 BDEWaitForEncryption                Indicates whether the deployment process should not
                                     proceed until BitLocker has finished the encryption
                                     process for all specified drives

 DestinationDisk                     Disk number to which the image will be deployed

 DestinationLogicalDrive             The logical drive to which the image will be deployed

 DestinationPartition                Disk partition to which the image will be deployed

 OSDPartitions                       The number of defined partition configurations (The
                                     maximum number of partitions you can configure is two;
                                     the default is none.)

<!-- p.416 -->

 Property                               Description

 OSDPartitionsxBootable                 The partition that should be set to bootable (The default
                                        first partition is set to bootable.)

 OSDPartitionsxFileSystem               The type of file system for the partition (Valid values are
                                        NTFS or FAT32.)

 OSDPartitionsxQuickFormat              Indicates whether the partition should be quick formatted
                                        (The default is TRUE.)

 OSDPartitionsxSize                     The size of the partition

 OSDPartitionsxSizeUnits                The units of measure for specifying the size of the
                                        partition (Valid values are MB, GB, or %. The default value
                                        is MB.)

 OSDPartitionsxType                     The type of partition to be created

 OSDPartitionsxVolumeLetterVariable     The drive letter to be assigned to the partition

 OSDPartitionsxVolumeName               The volume name that will be assigned to the partition

 WipeDisk                               Indicates whether the disk should be wiped

Saving and Restoring User State Information
User state information consists of the user profile information, Internet Explorer
favorites, data files, and other user-specific data stored on the target computer. The
MDT deployment process can automatically capture and restore user state information
on the target computers.

The MDT deployment process uses USMT to save and restore user state information.
During the State Capture Phase in the MDT deployment process, USMT saves the user
state information to a desired location. Later, during the State Restore Phase, USMT
restores this user state information.

To save and restore user state information on target computers in
MDT

   1. Review the task sequence steps used for saving and restoring user state
     information as described in Review User State Information Task Sequence Steps.

   2. Configure the MDT properties used in saving and restoring user state information
     as described in Configure User State Information Properties.

<!-- p.417 -->

   3. Customize the USMT XML control files as described in Configure User State
     Migration XML Control Files.

   4. Configure MDT to perform user state capture in Windows PE (offline) or in the
     existing operating system (online) as described in Configure USMT Offline User
     State Migration.

Review User State Information Task Sequence Steps
MDT includes task sequence templates for LTI and ZTI deployments for Configuration
Manager. These task sequence templates include the task sequence steps listed in Table
163, which are used to save and restore user state information.

Table 163. User State Information Task Sequence Steps

                                                                                 ﾉ   Expand table

 Task sequence        Description
 step

 Generate             Generates an XML file used to identify documents created by applications
 Application          installed on the target computer
 Migration Files

 Capture User         Captures user state information based on the application migration files that
 State                the Generate Application Migration Files task sequence step generates and
                      the user state information properties in CustomSettings.ini or the MDT DB for
                      LTI deployments

 Capture Groups       Captures the group membership of the local groups on the target computer
                      based on the user state information properties in CustomSettings.ini or the
                      MDT DB

 Restore User         Restores the user state information that the Capture User State task
 State                sequence step saved to the target computer

 Restore Groups       Restores the group membership information that the Capture Groups task
                      sequence step saved to the target computer

 Offline User State   Captures user state information while running in Windows PE (offline) instead
 Capture              of the orignial operating system (online). This task sequence step runs the
                      ZTIUserState.wsf script and is run when the following conditions are met:

                      - The _SMSTSMediaType property is not equal to "OEMMedia".

                      - The OSDDiskPart property is not equal to "TRUE".

<!-- p.418 -->

 Task sequence      Description
 step

                    This task sequence step is a part of the Offline USMT group that is run when
                    the USMTOfflineMigration equals "TRUE".

Configure User State Information Properties
Table 164 lists the MDT properties for LTI deployments that control saving and restoring
user state information. You can configure these properties in the CustomSettings.ini file
or in the MDT DB. For more information about the properties in Table 164, see the
corresponding section for each property in the MDT document Toolkit Reference.

Table 164. User State Information Properties for LTI
Deployments

                                                                                 ﾉ   Expand table

 Property                Description

 LoadStateArgs           List of parameters passed to the Loadstate.exe tool

 ScanStateArgs           List of parameters passed to the Scanstate.exe tool

 UserDataLocation        Indicates where the user state migration data should be saved

 UDDir                   The folder in which the user state migration data is stored (This folder
                         exists beneath the network shared folder specified in the UDShare
                         property.)

 UDProfiles              A comma-delimited list of user profiles that the Scanstate.exe tool must
                         save during the State Capture Phase

 UDShare                 The network share in which user state migration data is stored

 USMTOfflineMigration    Indicates whether an USMT offline migration should be performed. An
                         offline migration is performed while the computer is started in Windows
                         PE instead of the operating system currently installed on the target
                         computer.

  ） Important

  USMT will by default capture all local and domain user accounts unless explicitly
  excluded. Any captured local accounts will then, by default, be included in the

<!-- p.419 -->

  restore process. In some circumstances the restore step will fail without the
  inclusion of the /lae parameter to set the password for these local accounts.

Configure User State Migration XML Control Files

USMT uses the default versions of the migration XML files unless the path to the custom
XML control files is indicated. Customize the user state migration XML control files for
USMT by performing the following tasks:

        Configure the XML control files for USMT for LTI deployments as described in
        Configure User State Migration XML Control Files for LTI Deployments.

        Configure the XML control files for USMT for ZTI deployments as described in
        Configure User State Migration XML Control Files for ZTI Deployments.

Configure User State Migration XML Control Files for LTI
Deployments

For LTI deployments, insert one or more lines in the CustomSettings.ini file that contain
the USMTMigFiles property for each of the USMT migration XML control files that you
want to specify. The XML files need to be copied into either the USMT folder or the
Scripts folder in the distribution share.

Use the following format for these lines:

  ini

  USMTMigFiles1=MigApp.xml
  USMTMigFiles2=MigUser.xml
  USMTMigFiles3=MigSys.xml
  USMTMigFiles4=MigCustom.xml
  USMTConfigFile=Config.xml

  ７ Note

  See the MDT document Toolkit Reference for details on configuration settings.

Configure User State Migration XML Control Files for ZTI
Deployments

For ZTI deployments for Configuration Manager, insert a line in the CustomSettings.ini
file that contains the OSDMigrateConfigFiles task sequence variable for the USMT

<!-- p.420 -->

migration XML control file that you want to specify. If you specify the
OSDMigrateConfigFiles property, insert another line that sets the OSDMigrateMode
task sequence variable to Advanced.

Use the following format for these lines:

  ini

  OSDMigrateMode=Advanced
  OSDMigrateConfigFiles=MigApp.xml,MigUser.xml

The path to the XML control files is relative to the current folder, which will be the
location of the USMT package. If you keep the XML control files in the USMT package,
update this package each time you modify any of the XML control files. Otherwise, you
can store the XML control files in a separate package or network shared folder and
specify a fully qualified UNC path to the package or network shared folder.

Configure USMT Offline User State Migration

USMT can perform offline migration of user state from a computer. In an offline
migration, the capture is performed in Windows PE instead of the existing operating
system. The advantages of performing an offline user state migration are:

        You do not need to log on to the computer on which you are capturing user state.

        Hardware resources and files are more readily accessible by ScanState and other
        USMT tools.

        Performance may increase on older computers that have limited hardware
        resources and numerous software applications.

        Doing so may help avoid conflicts where a file is in use by another application or
        service.

        You may be able to use an offline migration to recover files and settings if a
        computer no longer starts properly.

        The disadvantage of performing an offline user state migration is that some user
        settings are not captured but rather can only be captured while running USMT in
        the target operating system. For a list of the settings that are not captured when
        performing an offline user state capture, see What Does USMT Migrate?

        You can perform USMT offline user state migration in the MDT:

<!-- p.421 -->

     In a Refresh Computer deployment scenario using LTI, ZTI, or UDI when the value
     of the USMTOfflineMigration property is set to "TRUE"

     In a New Computer deployment scenario using LTI with the Move Data and
     Settings wizard page in the Deployment Wizard or if the value of the
     USMTOfflineMigration property is set to "TRUE"

  ７ Note

  You cannot perform USMT offline user state migration in the MDT New Computer
  deployment scenario using ZTI.8

Joining Target Computers to AD DS Domains
One of the final steps in completing the deployment of a target operating system to the
target computers is joining the computer to an AD DS domain. Although you can
complete this process manually, MDT supports the following automated methods for
joining target computers to AD DS domains:

     Using the Deployment Wizard as described in Join Domains Using the Deployment
     Wizard

     Modifying CustomSettings.ini as described in Join Domains by Modifying the
     CustomSettings.ini File

     Modifying Unattended.xml as described in Join Domains by Modifying the
     Unattended.xml File

     Using the Recover from Domain Join Failure task sequence step type as described
     in Join Domains Using the Recover from Domain Join Failure Task Sequence Step
     Type

     Using the Windows offline domain join feature as described in Join Domains Using
     Offline Domain Join

Join Domains Using the Deployment Wizard
For LTI deployments, the Join the computer to a domain or workgroup wizard page in
the Windows Deploy Wizard in MDT allows you to interactively provide the
configuration settings necessary to join a domain. Table 165 lists the configuration
settings on this wizard page used in joining a domain.

<!-- p.422 -->

Table 165. Configuration Settings on the Join the
computer to a domain or workgroup wizard page for
Joining Domain

                                                                               ﾉ   Expand table

 Setting          Description

 Join a domain    Select to configure the Deployment Wizard to join the target computer to a
                  domain.

 Domain           Specifies the domain to which the target computer is to be joined. This text
                  box is enabled only when you select Join a domain.

 User Name        Specifies the account to be used in joining the target computer to the domain
                  specified in Domain. This text box is enabled only when you select Join a
                  domain.

 Password         Specifies the password for the account specified in User Name. This text box
                  is enabled only when you select Join a domain.

 Domain           Specifies the domain in which the account specified in User Name is located.
                  This text box is enabled only when you select Join a domain.

 Organizational   Specifies the OU in which the computer account will be created in the domain
 Unit             specified in Domain. This text box is enabled only when you select Join a
                  domain.

For more information about completing the Join the computer to a domain or
workgroup wizard page in the Windows Deploy Wizard, see Complete the Deployment
Wizard.

Join Domains by Modifying the CustomSettings.ini File
You can automate the domain-join process for LTI or ZTI deployments by modifying the
properties listed in Table 166 in the CustomSettings.ini file used in the MDT deployment
process.

Table 166. Properties in CustomSettings.ini to Modify for
Joining a Domain

                                                                               ﾉ   Expand table

<!-- p.423 -->

 Property               Description

 DomainAdmin            The user account credentials used to join the target computer to the
                        domain specified in JoinDomain; specify as domain\user_name or
                        user_name@domain.com

 DomainAdminDomain      The domain in which the user's credentials specified in DomainAdmin
                        reside

 DomainAdminPassword    The password used for the domain Administrator account specified in
                        the DomainAdmin property to join the computer to the domain

 JoinDomain             The domain that the target computer joins after the target operating
                        system is deployed (This is the domain in which the computer account
                        for the target computer is created. The JoinDomain property can
                        contain alphanumeric characters, hyphens [-], and underscores [_]. The
                        JoinDomain property cannot be blank or contain spaces.)

 MachineObjectOU        The AD DS OU in the target domain in which the computer account for
                        the target computer is created

Join Domains by Modifying the Unattended.xml File
You can automate the domain-join process for LTI or ZTI deployments by modifying the
settings listed in Table 167 in the Unattended.xml file used in the MDT deployment
process.

Table 167. Settings in Unattended.xml to Modify for
Joining a Domain

                                                                             ﾉ   Expand table

 Setting           Description

 Username          The user account credentials used to join the target computer to the domain
                   specified in JoinDomain

 Domain            The domain in which the user's credentials specified in Username reside

 Password          The password used for the domain Administrator account specified in the
                   Username setting to join the computer to the domain

 JoinDomain        The domain that the target computer joins after the target operating system
                   is deployed

 MachineObjectOU   The AD DS OU in the target domain in which the computer account for the
                   target computer is created

<!-- p.424 -->

For more information about these settings, see Microsoft-Windows-UnattendedJoin       .

Join Domains Using the Recover from Domain Join Failure Task
Sequence Step Type

Task sequence steps based on the Recover from Domain Join Failure task sequence
step type retry the domain-join process using the configuration information specified in
CustomSettings.ini. You can configure the Recover from Domain Join Failure task
sequence step type to recover using one of the following methods:

     Auto Recover (Rerun Join Domain). This method automatically retries the domain-
     join process without intervention. Select this method when you want the MDT
     process to automatically retry the domain-join process.

     Manual Recover (Allow user to Join Domain). This method allows the user
     running the Deployment Wizard to retry the domain-join process. Select this
     method when you want the MDT process to allow the user to retry the domain-join
     process.

     No Recover (Stop script execution). This method automatically terminates the task
     sequence if the computer has not successfully joined the domain. Select this
     method when you want MDT to stop running the task sequence if the computer
     has not successfully joined the domain.

     To configure task sequence steps based on the Recover from
     Domain Join Failure task sequence step type

        1. Select Start, and then point to All Programs. Point to Microsoft Deployment
          Toolkit, and then select Deployment Workbench.

        2. In the Deployment Workbench console tree, go to Deployment
          Workbench/Deployment Shares/deployment_share/Task Sequences (where
          deployment_share is the name of the deployment share in which you will
          configure the task sequence).

        3. In the details pane, select task_sequence_name (where task_sequence_name is
          the name of the task sequence you want to configure).

        4. In the Actions pane, select Properties.

          The task_sequence_name Properties dialog box opens (where
          task_sequence_name is the name of the task sequence you want to configure).

<!-- p.425 -->

         5. On the Task Sequence tab, in the task sequence hierarchy, go to
           task_sequence_step, and then select the Properties tab.

         6. On the Properties tab, configure the settings listed in Table 168 based on the
           requirements of your organization, and then select OK.

           Table 168. Configuration Settings on the Properties
           Tab of the Recover from Domain Join Failure Task
           Sequence Step Type

                                                                               ﾉ   Expand table

             Setting                   Description

             Type                      Contains the task sequence type, which is always set to
                                       Recover from Domain Join Failure

             Name                      Contains name of the task sequence step displayed in the
                                       task sequence

             Comments                  Provides descriptive information about the task sequence
                                       step

             Auto Recover (Rerun       Select to configure the task sequence step to
             Join Domain)              automatically retry the domain-join process without
                                       intervention

             Manual Recover (Allow     Select to configure the task sequence step to allow the
             user to Join Domain)      user to retry the domain-join process

             No Recover (Stop script   Select to configure the task sequence step to stop the
             execution)                task sequence if the computer has not successfully joined
                                       the domain

Join Domains Using Offline Domain Join
Offline domain join is a process to join a domain without contacting a domain
controller. This process makes it possible to join computers to a domain in locations
where there is no connectivity to a corporate network.

Using offline domain join, target computers can be joined to the domain when they
initially start after the installation of the target operating system. No additional restart is
required to complete the domain-join process, which can significantly reduce the overall
time required for wide-scale VM deployments.

<!-- p.426 -->

The offline domain join is a variant on joining domains by modifying the Unattend.xml
file. The Unattend.xml file includes the Microsoft-Windows-
UnattendJoin/Identification/Provisioning section, which includes the configuration

settings for performing a domain join.

For more information about:

     The offline domain join process, see Offline Domain Join (Djoin.exe) Step-by-Step
     Guide

     Configuring the Unattended.xml file to perform offline join, see the section,
     "Performing an offline domain join by using an unattended operating system
     installation," in Offline Domain Join (Djoin.exe) Step-by-Step Guide

Deploying Software Updates to Target Computers
In addition to the target operating system, applications, device drivers, and other
software components, you may need to apply software updates to all these software
components. These software updates are required to ensure a consistent configuration
baseline for all the target computers.

Deploy software updates to target computers in MDT by:

     Selecting the appropriate strategies for deploying software updates as described in
     Select the Software Update Deployment Strategy

     Deploying software updates using Windows Update Agent-based technologies for
     LTI deployments as described in Deploy Software Updates with Windows Update
     Agent for LTI Deployments

     Deploying software updates using the Deployment Workbench for LTI
     deployments as described in Deploy Software Updates with the Deployment
     Workbench for LTI Deployments

     Deploying software updates using Configuration Manager for ZTI deployments as
     described in Deploy Software Updates with Configuration Manager for ZTI
     Deployments

Select the Software Update Deployment Strategy

The software update deployment strategies are based on when the software updates are
to be installed. You can install software updates:

     As a part of the image deployed to the target computers

<!-- p.427 -->

     After the target operating system is deployed to the target computers

Deploy Software Updates with Windows Update Agent for LTI
Deployments

In LTI deployments, you can install software updates from Windows Update or from
WSUS using a task sequence step that runs the ZTIWindowsUpdate.wsf script. Some of
the LTI task sequence templates provided in MDT include the Windows Update (Pre-
Application Installation) task sequence step and the Windows Update (Post-
Application Installation) task sequence step.

You can also create a custom task sequence step based on the Run Command Line task
sequence step type that runs the following command line:

  Windows Command Prompt

  Cscript.exe "%SCRIPTROOT%\ZTIWindowsUpdate.wsf"

Deploy Software Updates with the Deployment Workbench for LTI
Deployments

In LTI deployments, you can install software updates for Windows in the Packages node
in the Deployment Workbench using a task sequence step based on the Install Updates
Offline task sequence step type. Some of the LTI task sequence templates provided in
MDT include the Apply Patches task sequence step, which is based on the Install
Updates Offline task sequence step type.

You can control the software updates deployed to the target computers by this method
using selection profiles. The Install Updates Offline task sequence step allows you to
specify a selection profile so that you can specify which software updates to deploy. If
you want to deploy software updates based on multiple selection profiles, create a task
sequence step for each selection profile, and then specify the corresponding selection
profile in the task sequence step.

For more information on creating selection profiles, see Create a New Selection Profile
in the Deployment Workbench.

Deploy Software Updates with Configuration Manager for ZTI
Deployments

<!-- p.428 -->

In ZTI deployments using Configuration Manager, you can initiate software updates
using a task sequence step based on the Install Software Updates task sequence step
type. The Install Software Updates task sequence type allows you to install only
mandatory or all software updates in a single task sequence step using one of the
configuration options listed in Table 169.

Table 169. Configuration Settings on the Properties Tab of
the Install Software Updates Type Task Sequence Step

                                                                                ﾉ    Expand table

 Setting                Description

 Name                   Configures the name of the task sequence step displayed in the task
                        sequence hierarchy

 Description            Configures the description text for the task sequence step

 Mandatory Software     Selecting configures the task sequence step to install only mandatory
 Updates                software updates

 All Software Updates   Selecting configures the task sequence step to install all software
                        updates, including mandatory software updates

For more information about the Install Software Updates task sequence type, see the
section, "Install Software Updates," in the section, "Task Sequence Steps in Configuration
Manager," in the Configuration Manager Documentation Library, which is installed with
Configuration Manager.

Managing Device Drivers
Device driver management is a critical component in deploying operating systems to
target computers. The proper device drivers must be available to Windows PE and to the
target operating system for the deployment to be successful.

Manage device drivers using MDT by:

     Selecting the appropriate strategies for managing device drivers as described in
     Select the Device Driver Management Strategy

     Managing device drivers using the Deployment Workbench for LTI deployments as
     described in Control Device Driver Deployments for LTI

<!-- p.429 -->

     Managing device drivers using Configuration Manager for ZTI deployments as
     described in Control Device Driver Deployments Using Configuration Manager for
     ZTI

     Resolving device driver signing issues as described in Resolve Device Driver
     Signing Issues

Select the Device Driver Management Strategy
The following are the high-level strategies for performing device driver management:

     Include all device drivers. This is the default behavior for LTI and ZTI deployments.
     In this strategy, all the drivers are deployed to the target computer. Then, Windows
     PE and the target operating system use Plug-and-Play IDs to identify the device
     drivers needed for the devices on the target computers.

     Include only the device drivers specifically required for the target computer. In
     this strategy, only the device drivers specific to the target computer are deployed
     to the target computer. This requires that you configure the ZTI and LTI process to
     control which device drivers are deployed to the target computer.

     Table 170 lists the advantages and disadvantages of these device driver
     management strategies.

Table 170. Advantages and Disadvantages of Device
Driver Management Strategies

                                                                               ﾉ    Expand table

 Strategy               Advantages                           Disadvantages

 Include all device     - Requires less initial time and     - Images are larger.
 drivers                effort to identify the appropriate
                        drivers.                             - Images require more frequent
                                                             version updates.
                        - Works well when there are
                        fewer device drivers to manage.      - Ongoing management of device
                                                             drivers in the image requires more
                                                             effort, because there are more
                                                             drivers in the image.

                                                             - Does not work well if there are a
                                                             large number of device drivers to
                                                             manage.

<!-- p.430 -->

 Strategy                  Advantages                            Disadvantages

 Include only the device   - Ongoing management of               - Requires more initial time and
 drivers specifically      device drivers in the image           effort to identify the appropriate
 required for the target   requires less effort, because there   drivers.
 computer                  are fewer drivers in the image.
                                                                 - Can introduce unnecessary
                           - Images are smaller.                 management overhead when there
                                                                 are fewer device drivers to manage.
                           - Images require less frequent
                           version updates.

                           - Works well when there is a large
                           number of device drivers to
                           manage.

Either of these strategies can cause problems if taken to the extreme. The "Include all
device drivers" strategy might cause problems when trying to manage tens of thousands
of device drivers because of the larger download sizes and a higher probability of
detecting the wrong device drivers. A complex management structure used in the
"Include only the device drivers specifically required for the target computer" strategy
might be too complex for managing small environments with only two or three different
types of computers and cause you to spend a lot of unnecessary time up front.

In most instances, select a device driver management strategy that is a hybrid of these
strategies and best fits your organization.

Control Device Driver Deployments for LTI

The goal of managing device drivers for LTI deployments is to help ensure that only the
appropriate device drivers are deployed to the target computers without introducing
unnecessary effort and management overhead. The high-level approach to device driver
management using the Deployment Workbench for LTI deployments is as follows:

   1. Create a folder structure in the Out-of-Box Drivers node of the Deployment
     Workbench to organize the device drivers as described in Create Folders to
     Organize Device Drivers for LTI Deployments.

   2. Create selection profiles used to select the device drivers for deployment based on
     the folder structure you created in the previous step as described in Create
     Selection Profiles to Select the Device Drivers for LTI Deployments.

   3. Configure tasks sequences to deploy the device drivers in the selection profiles as
     described in Configure Task Sequences to Deploy Device Drivers in Selection

<!-- p.431 -->

     Profiles for LTI Deployments.

Create Folders to Organize Device Drivers for LTI Deployments

Create folder structures in the Out-of-Box Drivers node in the Deployment Workbench
to provide the level of control you want for deploying device drivers to target
computers. The folder structure groups or categorizes device drivers so that you can
select specific groupings or categories of drivers using selection profiles.

Select any combination of the following methods for creating folder structures:

     Target operating system. Select this method to deploy only the device drivers to
     the target computer based on the respective target operating system.

     Processor architecture of the target computers. Select this method to deploy only
     the device drivers to the target computers based on the respective processor
     architecture (32-bit or 64-bit).

     Manufacturer (make) and model of the target computers. Select this method to
     deploy device drivers to the target computer based on the respective make and
     model of the target computer.

         Tip

        If the name of the folder matches the value that the BIOS returned for make
        and model, you can select the appropriate folder structure based on task
        sequence variables later in the process.

     The complexity of the folder structure that you create is based on the level of
     precision you want for deploying the device drivers. The more precision you want,
     the more complex the folder structure.

     You can also select a method for creating folder structures based on specific
     problems you may be having or to mitigate an existing problem. For example, you
     may have or expect to have one of the following problems:

     Device drivers are being selected for the wrong operating system. In this case,
     you could organize your device drivers by creating the following folder structure in
     the Out-of-Box Drivers node in the Deployment Workbench based on operating
     systems, and then place the device drivers in the corresponding folders:

        Windows 7

<!-- p.432 -->

   Windows Server 2008 R2

   Windows Server 2012

   Windows 8

Device drivers are being selected for the wrong processor architecture. In this
case, you could organize your device drivers by creating the following folder
structure in the Out-of-Box Drivers node in the Deployment Workbench based on
processor architecture, and then place the device drivers in the corresponding
folders:

   x86

   x64

Device drivers are being selected for the wrong make and model of target
computer. In this case, you could organize your device drivers by creating the
following folder structure in the Out-of-Box Drivers node in the Deployment
Workbench based on the make and model of the target computer, and then place
the device drivers in the corresponding folders:

   make_01\

   ...\model_01

   ...\model_02

   ...\model_03

   make_02\

   ...\model_aa

   ...\model_ab

   make_03\

   ...\model_xx

   ...\model_xy

Example: Woodgrove Bank Device Driver Folder Structure for LTI

Woodgrove Bank has decided that it wants to maintain precise control over the
device drivers deployed to target computers. So, its IP pros create a folder
structure in the Out-of-Box Drivers node in the Deployment Workbench that

<!-- p.433 -->

    organizes the device drivers by make and model, operating system, and processor
    architecture:

    make\model\operating_system\architecture

    Figure 14 illustrates the folder structure Woodgrove Bank created.

    Figure 14. Device driver folder structure created by Woodgrove Bank

Create Selection Profiles to Select the Device Drivers for LTI
Deployments

<!-- p.434 -->

Create selection profiles to identify the combination of device drivers that you want to
deploy to specific target computers based on the folder structure you created in the
Out-of-Box Drivers node in the Deployment Workbench. The LTI deployment process
uses selection profiles to determine the device drivers to deploy in the Inject Drivers
task sequence step type, in CustomSettings.ini, and in the MDT DB.

By default, selection profiles deploy the device drivers in the selected folder and
subfolders. Create selection profiles based on the level of control you want to have over
the device drivers being deployed. If you create selection profiles on folders:

     Higher in the folder structure, more device drivers are included, and you have less
     granular control over the device drivers deployed

     Lower in the folder structure, fewer device drivers are included, and you have more
     granular control over the device drivers deployed

   Tip

  Use selection profile names that allow you to easily identify the device drivers
  included in them, such as Windows 7 32-bit and 64-bit Device Drivers, Windows 8
  64-bit Device Drivers, or Fabrikam - Model A532- 32-bit Device Drivers.

Example: Woodgrove Bank Device Driver Selection Profiles for LTI Deployments

Woodgrove Bank has decided that it wants to maintain precise control over the device
drivers deployed to target computers. So, its IT pros create a selection profile for each
leaf-level folder in following folder structure:

make\model\operating_system\architecture

Woodgrove Bank named the selection profiles based on the folder structure in the
format as follows:

make-model-operating_system-architecture

The following is an example of the Woodgrove Bank selection profile naming
convention for 64-bit device drivers for Windows 8 running on a computer with
"Fabrikam" as the make and "FK5323" as the model:

"Fabrikam-FK5323-Win8-x64"

Configure Task Sequences to Deploy Device Drivers in Selection
Profiles for LTI Deployments

<!-- p.435 -->

Modify The configuration for your task sequences to reference the selection profiles and
deploy the appropriate device drivers to the target computers. Selection profiles are
exposed to the LTI deployment process as:

     Selection profiles that can be configured in the Deployment Workbench, the
     CustomSettings.ini file, or the MDT DB

     Device driver groups that can be configured in the CustomSettings.ini file or the
     MDT DB

     Selection profiles and device driver groups are additive. The LTI deployment
     process creates the list of device drivers to deploy based on the union of both
     selection profiles and device driver groups, which can cause unpredictable results,
     because the default selection profile and default device driver group include all
     device drivers. For example, if you specify a selection profile that contains only 64-
     bit device drivers and leave the default device driver group, the result will include
     all device drivers.

     To change this behavior, specify:

     TheNothing device driver group in the CustomSettings.ini file or the MDT DB to
     allow the selection profile to control the device drivers deployed to the target
     computer

     TheNothing selection profile in the Inject Driver task sequence step, the
     CustomSettings.ini file, or the MDT DB to allow the device driver group to control
     the device drivers deployed to the target computer

     A specific set of device drivers for the selection profile and the device driver group
     so that a known set of device drivers is deployed

     The following are strategies for configuring task sequences to control the
     deployment of device drivers for LTI deployments:

     For a single selection profile, modify the Inject Driver task sequence step, which is
     in most of the LTI task sequence templates, to use the selection profile.

     For a limited number of selection profiles, add an Inject Driver task sequence step
     for each selection profile, and then configure each task sequence step with the
     corresponding selection profile.

     Configure a single Inject Driver task sequence step in your task sequence, and
     then override the selection profile specified in the Inject Driver task sequence step
     using the DriverSelectionProfile task sequence variable in the CustomSettings.ini
     file or the MDT DB.

<!-- p.436 -->

  ７ Note

  The selection profile you specify in the DriverSelectionProfile task sequence
  variable overrides all Inject Driver task sequence steps in a task sequence. If
  you have multiple all Inject Driver task sequence steps in your task sequence,
  they all will be overridden.

Configure a single Inject Driver task sequence step in the task sequence (which
already exists in most of the LTI task sequence templates), but specify additional
device drivers to be added using the DriverGroup task sequence variable. Because
selection profiles and device driver groups are additive, the device drivers specified
in the DriverGroup task sequence variable are deployed in addition to the device
drivers in the selection profile.

If you want to use the DriverGroup task sequence variable for backward
compatibility with previous versions of MDT, configure the Inject Driver task
sequence step to use the Nothing selection profile.

  ７ Note

  You can also use the DriverPaths property to specify the UNC path to the
  folders containing the device drivers to deploy. However, this method is
  provided for backward compatibility with previous versions of MDT. Instead,
  use selection profiles or the DriverGroup task sequence variable.

Example: Woodgrove Bank Device Driver Task Sequence Configuration for LTI
Deployments

Woodgrove Bank has decided that it wants to maintain precise control over the
device drivers deployed to target computers. Its IT pros have created a device
driver folder structure and selection profile strategy that allows detailed control of
device drivers.

The IT pros configured their task sequences using the Inject Driver task sequence
step in their task sequences with the most common configuration in their
organization, and then used the DriverSelectionProfile task sequence variable in
the CustomSettings.ini file and the MDT DB to override the selection profile
specified in the Inject Driver task sequence step as necessary.

The IT pros added the following line in their CustomSettings.ini file for the
DriverSelectionProfile task sequence variable:

<!-- p.437 -->

  ini

  DriverSelectionProfile =%MAKE%-%MODEL%-Win8-%ARCHITECTURE%

  ７ Note

  The operating system is a static value for the DriverSelectionProfile task sequence
  variable, because the task sequence will deploy only one operating system.

Control Device Driver Deployments Using Configuration Manager
for ZTI

ZTI deployments in Configuration Manager use the driver catalog in Configuration
Manager as the central repository for device drivers. After you import device drivers into
the driver catalog, you can organize them by:

        Device driver packages. Like software packages, device driver packages are
        distributed to distribution points so that they are accessible to the target
        computers. You can create multiple device driver packages to group device drivers
        to be deployed to the target computer, such as the make and model of target
        computer. You can control the device drivers deployed based on the device driver
        packages using the Apply Driver Package task sequence step.

        Device driver categories. Device driver categories allow you to specify a category
        for each device driver you import into the driver catalog. Categories allow you to
        group device drivers based common characteristics, such as all network adapter
        drivers or by processor architecture. You can control the device drivers deployed to
        the target computer based on the device driver categories using the Auto Apply
        Drivers task sequence step.

        Most of the ZTI task sequences created using the MDT task sequence templates
        include the Auto Apply Drivers task sequence step. By default, this step configures
        the task sequence to deploy all device drivers to the target computer, allowing the
        target operating system to select the device drivers required.

        The list that follows provides strategies for configuring task sequences to control
        the deployment of device drivers for ZTI deployments in Configuration Manager:

        Create multiple device driver categories that are configured in multiple Auto Apply
        Drivers task sequence steps. Control the deployment of device drivers by
        performing the following steps:

<!-- p.438 -->

   1. Create device driver categories based on the level of granularity you want in
     controlling the device drivers to be deployed.

   2. Add multiple Auto Apply Drivers task sequence steps based on the number
     of combination categories you want to deploy.

   3. Configure the Auto Apply Drivers task sequence step to use the proper
     combination of device driver categories using the Limit driver matching to
     only consider drivers in selected categories list box.

   4. Configure the task sequence step conditions based on the contents of the
     device driver package.

     For example, if the device driver packages are based on the make and model
     of the target computer, configure the task sequence step to run when the
     Make and Model task sequence variables equal the make and model for the
     device driver package.

Create multiple device driver packages that are configured in multiple Apply
Driver Package task sequence steps. Control the deployment of device drivers by
performing the following steps:

   1. Create device driver packages based on the criteria for limiting the device
     drivers to be deployed.

   2. For each device driver package, add an Apply Driver Package task sequence
     step for each category.

   3. Configure the Apply Driver Package task sequence step to use the
     corresponding device driver package.

   4. Configure the task sequence step conditions based on the contents of the
     device driver package.

     For example, if the device driver packages are based on the make and model
     of the target computer, configure the task sequence step to run when the
     Make and Model task sequence variables equal the make and model for the
     device driver package.

Configure a single Auto Apply Drivers task sequence step in your task sequence,
and then override the selection profile specified in the Auto Apply Drivers task
sequence step using the OSDAutoApplyDriverCategoryList task sequence variable
in the CustomSettings.ini file or the MDT DB. Control the deployment of device
drivers by performing the following steps:

<!-- p.439 -->

1. Create device driver categories based on the level of granularity you want in
  controlling the device drivers to be deployed.

2. Add a new or an existing Auto Apply Drivers task sequence step in your task
  sequence.

3. Configure the Auto Apply Drivers task sequence step to use any of the
  device driver categories using the Limit driver matching to only consider
  drivers in selected categories list box.

    ７ Note

    The device driver category you select is not important, as the category
    will be overridden by the OSDAutoApplyDriverCategoryList task
    sequence variable.

4. Determine GUIDs for each device driver category you created by running the
  following script, substituting strSiteCode with your site code, strServer with
  you Configuration Manager site server, and strDriverCatName with the name
  of a device driver category you created:

    VB

    strSiteCode = "NYC"
    strServer = "CMSERVER"
    strDriverCatName = "Fabrikam"
    set objWMIService= GetObject("winmgmts:
    {impersonationlevel=impersonate}!\\" & strServer &
    "\root\sms\site_" & strSiteCode)

    set DriverGUIDS = objWMIService.ExecQuery("select
    CategoryInstance_UniqueID from CMDB_categoryinstance where
    LocalizedCategoryInstanceName = '" & strDriverCatName & "'")
    For each DriverGuid in DriverGuids
         wscript.echo DriverGuid.CategoryInstance_UniqueID
    Next

5. Modify the CustomSettings.ini file as follows, substituting SECTION with the
  name of a section (such as [Default] ) and GUID with the GUID you retrieved
  in the previous step:

    ini

    [Settings]
    Properties=OSDAutoAPplyDriverCategoryList

<!-- p.440 -->

             [SECTION]
             OSDAutoApplyDriverCategoryList=DriverCategories:GUID

     When performing deployments using stand-alone media, use an Apply Driver
     Package task sequence step, because the Auto Apply Drivers task sequence
     requires connectivity to a management point, and the stand-alone media will not
     attempt a connection to a management point.

Resolve Device Driver Signing Issues

Digital signatures tell you whether a device driver is provided by a legitimate publisher.
Windows features take advantage of code-signing technologies, and requirements for
security in the operating system enforce the use of digital signatures for some kinds of
code.

In many instances, device drivers from vendors are already signed. However, there may
be instances where you modify the files include with the device drivers and need to sign
the device drivers again. For example, you might need to modify an INF file for a device
driver, and then sign the device driver.

Review the following resources to help you resolve device driver signing issues:

     Driver Signing Requirements for Windows

     Device Management and Installation Step-by-Step Guide: Signing and Staging
     Device Drivers in Windows 7 and Windows Server 2008 R2

Running Orchestrator Runbooks
System Center 2012 Orchestrator can tie disparate tasks and procedures together by
using the Runbook Designer graphical user interface to create reliable, flexible, and
efficient end-to-end solutions in the IT environment.

You can carry out the following tasks using Orchestrator:

     Automate processes in your data center, regardless of hardware or platform.

     Automate your IT operations and standardize best practices to improve
     operational efficiency.

     Connect different systems from different vendors without having to know how to
     use scripting and programming languages.
