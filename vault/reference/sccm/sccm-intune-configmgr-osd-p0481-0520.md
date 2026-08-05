---
title: "OS deployment documentation — pages 481-520"
type: reference
domain: sccm
slug: sccm-intune-configmgr-osd-p0481-0520
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-osd-p0481-0520
family: sccm
documentKind: "doc"
abstract: "Applies to the Check Readiness step. A read-only variable for whether the Current OS to be refreshed is check returned true ( 1 ) or false ( 0 ). If you don't enable the check, the value of this read-only variable is blank. _TS_CRARCH Applies to the Check Readiness step. A read-"
---

# OS deployment documentation — pages 481-520

<!-- p.481 -->

Applies to the Check Readiness step.

A read-only variable for whether the Current OS to be refreshed is check returned true ( 1 ) or
false ( 0 ). If you don't enable the check, the value of this read-only variable is blank.

_TS_CRARCH
Applies to the Check Readiness step.

A read-only variable for whether the Architecture of current OS check returned true ( 1 ) or
false ( 0 ). If you don't enable the check, the value of this read-only variable is blank.

_TS_CRMINOSVER
Applies to the Check Readiness step.

A read-only variable for whether the Minimum OS version check returned true ( 1 ) or false ( 0 ).
If you don't enable the check, the value of this read-only variable is blank.

_TS_CRMAXOSVER
Applies to the Check Readiness step.

A read-only variable for whether the Maximum OS version check returned true ( 1 ) or false ( 0 ).
If you don't enable the check, the value of this read-only variable is blank.

_TS_CRCLIENTMINVER
Applies to the Check Readiness step.

A read-only variable for whether the Minimum client version check returned true ( 1 ) or false
( 0 ). If you don't enable the check, the value of this read-only variable is blank.

_TS_CROSLANGUAGE
Applies to the Check Readiness step.

A read-only variable for whether the Language of current OS check returned true ( 1 ) or false
( 0 ). If you don't enable the check, the value of this read-only variable is blank.

_TS_CRACPOWER

<!-- p.482 -->

Applies to the Check Readiness step.

A read-only variable for whether the AC power plugged in check returned true ( 1 ) or false ( 0 ).
If you don't enable the check, the value of this read-only variable is blank.

_TS_CRNETWORK
Applies to the Check Readiness step.

A read-only variable for whether the Network adapter connected check returned true ( 1 ) or
false ( 0 ). If you don't enable the check, the value of this read-only variable is blank.

_TS_CRUEFI
Applies to the Check Readiness step.

A read-only variable for whether the Computer is in UEFI mode check returned BIOS ( 0 ) or
UEFI ( 1 ). If you don't enable the check, the value of this read-only variable is blank.

_TS_CRWIRED
Applies to the Check Readiness step.

A read-only variable for whether the Network adapter is not wireless check returned true ( 1 )
or false ( 0 ). If you don't enable the check, the value of this read-only variable is blank.

_TS_CRTPMACTIVATED
Starting in version 2111

Applies to the Check Readiness step.

A read-only variable for whether the TPM 2.0 or above is activated check returned inactive ( 0 )
or active ( 1 ). If you don't enable the check, the value of this read-only variable is blank.

_TS_CRTPMENABLED
Starting in version 2111

Applies to the Check Readiness step.

<!-- p.483 -->

A read-only variable for whether the TPM 2.0 or above is enabled check returned disabled ( 0 )
or enabled ( 1 ). If you don't enable the check, the value of this read-only variable is blank.

_TSAppInstallStatus
The task sequence sets this variable with the installation status for the application during the
Install Application step. It sets one of the following values:

     Undefined: The Install Application step hasn't run.

     Error: At least one application failed because of an error during the Install Application
     step.

     Warning: No errors occurred during the Install Application step. One or more
     applications, or a required dependency, didn't install because a requirement wasn't met.

     Success: There are no errors or warnings detected during the Install Application step.

_TSSecureBoot
Use this variable to determine the state of secure boot on a UEFI-enabled device. The variable
can have one of the following values:

      NA : The associated registry value doesn't exist, which means the device doesn't support

     secure boot.
      Enabled : The device has secure boot enabled.
      Disabled : The device has secure boot disabled.

OSDAdapter
Applies to the Apply Network Settings step.

(input)

This task sequence variable is an array variable. Each element in the array represents the
settings for a single network adapter on the computer. Access the settings for each adapter by
combining the array variable name with the zero-based network adapter index and the
property name.

If the Apply Network Settings step configures multiple network adapters, it defines the
properties for the second network adapter by using the index 1 in the variable name. For
example: OSDAdapter1EnableDHCP, OSDAdapter1IPAddressList, and
OSDAdapter1DNSDomain.

<!-- p.484 -->

Use the following variable names to define the properties of the first network adapter for the
step to configure:

OSDAdapter0EnableDHCP

This setting is required. Possible values are True or False . For example:

true : enable Dynamic Host Configuration Protocol (DHCP) for the adapter

OSDAdapter0IPAddressList
Comma-delimited list of IP addresses for the adapter. This property is ignored unless
EnableDHCP is set to false . This setting is required.

OSDAdapter0SubnetMask
Comma-delimited list of subnet masks. This property is ignored unless EnableDHCP is set to
false . This setting is required.

OSDAdapter0Gateways

Comma-delimited list of IP gateway addresses. This property is ignored unless EnableDHCP is
set to false . This setting is required.

OSDAdapter0DNSDomain
Domain Name System (DNS) domain for the adapter.

OSDAdapter0DNSServerList
Comma-delimited list of DNS servers for the adapter. This setting is required.

OSDAdapter0EnableDNSRegistration

Set to true to register the IP address for the adapter in DNS.

OSDAdapter0EnableFullDNSRegistration

Set to true to register the IP address for the adapter in DNS under the full DNS name for the
computer.

<!-- p.485 -->

OSDAdapter0EnableIPProtocolFiltering
Set to true to enable IP protocol filtering on the adapter.

OSDAdapter0IPProtocolFilterList

Comma-delimited list of protocols allowed to run over IP. This property is ignored if
EnableIPProtocolFiltering is set to false .

OSDAdapter0EnableTCPFiltering
Set to true to enable TCP port filtering for the adapter.

OSDAdapter0TCPFilterPortList
Comma-delimited list of ports to be granted access permissions for TCP. This property is
ignored if EnableTCPFiltering is set to false .

OSDAdapter0TcpipNetbiosOptions
Options for NetBIOS over TCP/IP. Possible values are as follows:

      0 : Use NetBIOS settings from DHCP server

      1 : Enable NetBIOS over TCP/IP
      2 : Disable NetBIOS over TCP/IP

OSDAdapter0MacAddress

MAC address used to match settings to the physical network adapter.

OSDAdapter0Name

The name of the network connection as it appears in the network connections control panel
program. The name is between 0 and 255 characters long.

OSDAdapter0Index

Index of the network adapter settings in the array of settings.

Example

<!-- p.486 -->

     OSDAdapterCount = 1
     OSDAdapter0EnableDHCP = FALSE
     OSDAdapter0IPAddressList = 192.168.0.40
     OSDAdapter0SubnetMask = 255.255.255.0
     OSDAdapter0Gateways = 192.168.0.1
     OSDAdapter0DNSSuffix = contoso.com

OSDAdapterCount
Applies to the Apply Network Settings step.

(input)

Specifies the number of network adapters installed on the destination computer. When you set
the OSDAdapterCount value, also set all the configuration options for each adapter.

For example, if you set the OSDAdapter0TCPIPNetbiosOptions value for the first adapter, then
you must configure all the values for that adapter.

If you don't specify this value, the task sequence ignores all OSDAdapter values.

OSDAppInstallRetries
Starting this Configuration Manager 2211 HFRU Kb 16643863 and above

Applies to the Install Application step.

(input)

Specifies the number of times the task sequence step tries to install an application in the case
of failure. The value must be specified to trigger a retry in the case of application installation
failure. Application installation retry is attempted ONLY when 'Install Next Application on
Failure' option is not selected on the task.

Defaults to 0 and task sequence does not retry application installation by default.

OSDAppInstallRetryTimeout
Starting this Configuration Manager 2211 HFRU Kb 16643863 and above

Applies to the Install Application step.

(input)

<!-- p.487 -->

Specifies the time in milliseconds, that the task sequence should wait before retrying an
application installation on failure. The value defaults to 30 seconds (30000 milliseconds). For
example, specify a value of 45000 for a retry delay of 45 seconds.

OSDApplyDriverBootCriticalContentUniqueID
Applies to the Apply Driver Package step.

(input)

Specifies the content ID of the mass storage device driver to install from the driver package. If
this variable isn't specified, no mass storage driver is installed.

OSDApplyDriverBootCriticalHardwareComponent
Applies to the Apply Driver Package step.

(input)

Specifies whether a mass storage device driver is installed, this variable must be scsi.

If OSDApplyDriverBootCriticalContentUniqueID is set, this variable is required.

OSDApplyDriverBootCriticalID
Applies to the Apply Driver Package step.

(input)

Specifies the boot critical ID of the mass storage device driver to install. This ID is listed in the
scsi section of the device driver's txtsetup.oem file.

If OSDApplyDriverBootCriticalContentUniqueID is set, this variable is required.

OSDApplyDriverBootCriticalINFFile
Applies to the Apply Driver Package step.

(input)

Specifies the INF file of the mass storage driver to install.

If OSDApplyDriverBootCriticalContentUniqueID is set, this variable is required.

<!-- p.488 -->

OSDAutoApplyDriverBestMatch
Applies to the Auto Apply Drivers step.

(input)

If there are multiple device drivers in the driver catalog that are compatible with a hardware
device, this variable determines the step's action.

Valid values
      true (default): Only install the best device driver

      false : Installs all compatible device drivers, and Windows chooses the best driver to use

OSDAutoApplyDriverCategoryList
Applies to the Auto Apply Drivers step.

(input)

A comma-delimited list of the driver catalog category unique IDs. The Auto Apply Driver step
only considers the drivers in at least one of the specified categories. This value is optional, and
it's not set by default. Obtain the available category IDs by enumerating the list of
SMS_CategoryInstance objects on the site.

OSDBitLockerPIN
Applies to the Enable BitLocker step.

Specify the PIN for BitLocker encryption. This variable is only valid if the BitLocker mode is TPM
and PIN.

OSDBitLockerRebootCount
Applies to the Disable BitLocker step.

Use this variable to set the number of restarts after which to resume protection.

Valid values

An integer from 1 to 15 .

<!-- p.489 -->

OSDBitLockerRebootCountOverride
Applies to the Disable BitLocker step.

Set this value to override the count set by the step or the OSDBitLockerRebootCount variable.
While the other methods only accept values 1 to 15, if you set this variable to 0, BitLocker
remains disabled indefinitely. This variable is useful when the task sequence sets one value, but
you want to set a separate value on a per-device or per-collection basis.

Valid values
An integer from 0 to 15 .

OSDBitLockerRecoveryPassword
Applies to the Enable BitLocker step.

(input)

Instead of generating a random recovery password, the Enable BitLocker step uses the
specified value as the recovery password. The value must be a valid numerical BitLocker
recovery password.

OSDBitLockerStartupKey
Applies to the Enable BitLocker step.

(input)

Instead of generating a random startup key for the key management option Startup Key on
USB only, the Enable BitLocker step uses the Trusted Platform Module (TPM) as the startup
key. The value must be a valid, 256-bit Base64-encoded BitLocker startup key.

OSDCaptureAccount
Applies to the Capture OS Image step.

(input)

Specifies a Windows account name that has permissions to store the captured image on a
network share (OSDCaptureDestination). Also specify the OSDCaptureAccountPassword.

For more information on the capture OS image account, see Accounts.

<!-- p.490 -->

OSDCaptureAccountPassword
Applies to the Capture OS Image step.

(input)

Specifies the password for the Windows account (OSDCaptureAccount) used to store the
captured image on a network share (OSDCaptureDestination).

OSDCaptureDestination
Applies to the Capture OS Image step.

(input)

Specifies the location where the task sequence saves the captured OS image. The maximum
directory name length is 255 characters. If the network share requires authentication, specify
the OSDCaptureAccount and OSDCaptureAccountPassword variables.

OSDComputerName (input)
Applies to the Apply Windows Settings step.

Specifies the name of the destination computer.

Example
%_SMSTSMachineName% (default)

OSDComputerName (output)
Applies to the Capture Windows Settings step.

Set to the NetBIOS name of the computer. The value is set only if the
OSDMigrateComputerName variable is set to true .

OSDConfigFileName
Applies to the Apply OS Image step.

(input)

<!-- p.491 -->

Specifies the file name of the OS deployment answer file associated with the OS deployment
image package.

OSDDataImageIndex
Applies to the Apply Data Image step.

(input)

Specifies the index value of the image that's applied to the destination computer.

OSDDiskIndex
Applies to the Format and Partition Disk step.

(input)

Specifies the physical disk number to be partitioned.

In version 2010 and earlier, this number can't be larger than 99. In version 2103 and later, the
maximum number is 10,000. This change helps support storage area network (SAN) scenarios.

OSDDNSDomain
Applies to the Apply Network Settings step.

(input)

Specifies the primary DNS server that the destination computer uses.

OSDDNSSuffixSearchOrder
Applies to the Apply Network Settings step.

(input)

Specifies the DNS search order for the destination computer.

OSDDomainName
Applies to the Apply Network Settings step.

(input)

<!-- p.492 -->

Specifies the name of the Active Directory domain that the destination computer joins. The
specified value must be a valid Active Directory Domain Services domain name.

OSDDomainOUName
Applies to the Apply Network Settings step.

(input)

Specifies the RFC 1779 format name of the organizational unit (OU) that the destination
computer joins. If specified, the value must contain the full path.

Example

LDAP://OU=MyOu,DC=MyDom,DC=MyCompany,DC=com

OSDDoNotLogCommand
Applies to the Install Package and Run Command Line steps.

(input)

To prevent potentially sensitive data from being displayed or logged, set this variable to TRUE .
This variable masks the program name in the smsts.log during an Install Package step.

When you set this variable to TRUE , it also hides the command line from the Run Command
Line step in the log file.

OSDEnableTCPIPFiltering
Applies to the Apply Network Settings step.

(input)

Specifies whether TCP/IP filtering is enabled.

Valid values
      true
      false (default)

OSDGPTBootDisk

<!-- p.493 -->

Applies to the Format and Partition Disk step.

(input)

Specifies whether to create an EFI partition on a GPT hard disk. EFI-based computers use this
partition as the startup disk.

Valid values

      true
      false (default)

OSDImageCreator
Applies to the Capture OS Image step.

(input)

An optional name of the user who created the image. This name is stored in the WIM file. The
maximum length of the user name is 255 characters.

OSDImageDescription
Applies to the Capture OS Image step.

(input)

An optional user-defined description of the captured OS image. This description is stored in
the WIM file. The maximum length of the description is 255 characters.

OSDImageIndex
Applies to the Apply OS Image step.

(input)

Specifies the image index value of the WIM file that's applied to the destination computer.

OSDImageVersion
Applies to the Capture OS Image step.

(input)

<!-- p.494 -->

An optional user-defined version number to assign to the captured OS image. This version
number is stored in the WIM file. This value can be any combination of alphanumeric
characters with a maximum length of 32.

OSDInstallDriversAdditionalOptions
Applies to the Apply Driver Package step.

(input)

Specifies additional options to add to the DISM command line when applying a driver package.
The task sequence doesn't verify the command-line options.

To use this variable, enable the setting, Install driver package via running DISM with recurse
option, on the Apply Driver Package step.

For more information, see DISM command-line options.

OSDJoinAccount
Applies to the following steps:

     Apply Network Settings
     Join Domain or Workgroup

(input)

Specifies the domain user account that's used to add the destination computer to the domain.
This variable is required when joining a domain.

For more information on the task sequence domain joining account, see Accounts.

OSDJoinDomainName
Applies to the Join Domain or Workgroup step.

(input)

Specifies the name of an Active Directory domain the destination computer joins. The length of
the domain name must be between 1 and 255 characters.

OSDJoinDomainOUName
Applies to the Join Domain or Workgroup step.

<!-- p.495 -->

(input)

Specifies the RFC 1779 format name of the organizational unit (OU) that the destination
computer joins. If specified, the value must contain the full path. The length of the OU name
must be between 0 and 32,767 characters. This value isn't set if the OSDJoinType variable is set
to 1 (join workgroup).

Example
LDAP://OU=MyOu,DC=MyDom,DC=MyCompany,DC=com

OSDJoinPassword
Applies to the following steps:

     Apply Network Settings
     Join Domain or Workgroup

(input)

Specifies the password for the OSDJoinAccount that the destination computer uses to join the
Active Directory domain. If the task sequence environment doesn't include this variable, then
Windows Setup tries a blank password. If the variable OSDJoinType variable is set to 0 (join
domain), this value is required.

OSDJoinSkipReboot
Applies to the Join Domain or Workgroup step.

(input)

Specifies whether to skip restarting after the destination computer joins the domain or
workgroup.

Valid values
      true

      false

OSDJoinType
Applies to the Join Domain or Workgroup step.

<!-- p.496 -->

(input)

Specifies whether the destination computer joins a Windows domain or a workgroup.

Valid values
      0 : Join the destination computer to a Windows domain

      1 : Join the destination computer to a workgroup

OSDJoinWorkgroupName
Applies to the Join Domain or Workgroup step.

(input)

Specifies the name of a workgroup that the destination computer joins. The length of the
workgroup name must be between 1 and 32 characters.

OSDKeepActivation
Applies to the Prepare Windows for Capture step.

(input)

Specifies whether sysprep keeps or resets the product activation flag.

Valid values
      true : keep the activation flag

      false (default): reset the activation flag

OsdLayeredDriver
Starting in version 2107

Applies to the Apply OS Image step

Specify an integer value for the layered driver to install with Windows. For more information,
see the LayeredDriver Windows setting.

Valid values for OsdLayeredDriver

<!-- p.497 -->

                                                                                    ﾉ   Expand table

 Value    Keyboard driver

 0        Do not specify (default)

 1        PC/AT Enhanced keyboard (101/102-key)

 2        Korean PC/AT 101-Key Compatible keyboard or the Microsoft Natural keyboard (type 1)

 3        Korean PC/AT 101-Key Compatible keyboard or the Microsoft Natural keyboard (type 2)

 4        Korean PC/AT 101-Key Compatible keyboard or the Microsoft Natural keyboard (type 3)

 5        Korean keyboard (103/106-key)

 6        Japanese keyboard (106/109-key)

OSDLocalAdminPassword
Applies to the Apply Windows Settings step.

(input)

Specifies the local Administrator account password. If you enable the option to Randomly
generate the local administrator password and disable the account on all supported
platforms, then the step ignores this variable. The specified value must be between 1 and 255
characters.

OSDLogPowerShellParameters
Applies to the Run PowerShell Script step.

(input)

To prevent potentially sensitive data from being logged, the Run PowerShell Script step
doesn't log script parameters in the smsts.log file. To include the script parameters in the task
sequence log, set this variable to TRUE.

OSDMigrateAdapterSettings
Applies to the Capture Network Settings step.

(input)

<!-- p.498 -->

Specifies whether the task sequence captures the network adapter information. This
information includes configuration settings for TCP/IP and DNS.

Valid values
      true (default)

      false

OSDMigrateAdditionalCaptureOptions
Applies to the Capture User State step.

(input)

Specify additional command-line options for the user state migration tool (USMT) that the task
sequence uses to capture user state. The step doesn't expose these settings in the task
sequence editor. Specify these options as a string, which the task sequence appends to the
automatically generated USMT command line for ScanState.

The USMT options specified with this task sequence variable aren't validated for accuracy prior
to running the task sequence.

For more information on available options, see ScanState Syntax.

OSDMigrateAdditionalRestoreOptions
Applies to the Restore User State step.

(input)

Specifies additional command-line options for the user state migration tool (USMT) that the
task sequence uses when restoring the user state. Specify the additional options as a string,
which the task sequence appends to the automatically generated USMT command line for
LoadState.

The USMT options specified with this task sequence variable aren't validated for accuracy prior
to running the task sequence.

For more information on available options, see LoadState Syntax.

OSDMigrateComputerName
Applies to the Capture Windows Settings step.

<!-- p.499 -->

(input)

Specifies whether the computer name is migrated.

Valid values
      true (default). The OSDComputerName (output) variable is set to the NetBIOS name of

     the computer.
      false

OSDMigrateConfigFiles
Applies to the Capture User State step.

(input)

Specifies the configuration files used to control the capture of user profiles. This variable is
used only if OSDMigrateMode is set to Advanced . This comma-delimited list value is set to
perform customized user profile migration.

Example
miguser.xml,migsys.xml,migapps.xml

OSDMigrateContinueOnLockedFiles
Applies to the Capture User State step.

(input)

If USMT can't capture some files, this variable allows the user state capture to proceed.

Valid values
      true (default)

      false

OSDMigrateContinueOnRestore
Applies to the Restore User State step.

(input)

<!-- p.500 -->

Continue the process, even if USMT can't restore some files.

Valid values
      true (default)
      false

OSDMigrateEnableVerboseLogging
Applies to the following steps:

     Capture User State
     Restore User State

(input)

Enables verbose logging for USMT. The step requires this value.

Valid values
      true

      false (default)

OSDMigrateLocalAccounts
Applies to the Restore User State step.

(input)

Specifies whether the local computer account is restored.

Valid values

      true
      false (default)

OSDMigrateLocalAccountPassword
Applies to the Restore User State step.

(input)

<!-- p.501 -->

If the OSDMigrateLocalAccounts variable is true , this variable must contain the password
assigned to all migrated local accounts. USMT assigns the same password to all migrated local
accounts. Consider this password as temporary, and change it later by some other method.

OSDMigrateMode
Applies to the Capture User State step.

(input)

Allows you to customize the files that USMT captures.

Valid values

      Simple : The task sequence only uses the standard USMT configuration files

      Advanced : The task sequence variable OSDMigrateConfigFiles specifies the configuration

     files that USMT uses

OSDMigrateNetworkMembership
Applies to the Capture Network Settings step.

(input)

Specifies whether the task sequence migrates the workgroup or domain membership
information.

Valid values
      true (default)

      false

OSDMigrateRegistrationInfo
Applies to the Capture Windows Settings step.

(input)

Specifies whether the step migrates user and organization information.

Valid values

<!-- p.502 -->

      true (default). The OSDRegisteredOrgName (output) variable is set to the registered

     organization name of the computer.
      false

OSDMigrateSkipEncryptedFiles
Applies to the Capture User State step.

(input)

Specifies whether encrypted files are captured.

Valid values

      true
      false (default)

OSDMigrateTimeZone
Applies to the Capture Windows Settings step.

(input)

Specifies whether the computer time zone is migrated.

Valid values
      true (default). The variable OSDTimeZone (output) is set to the time zone of the

     computer.
      false

OSDNetworkJoinType
Applies to the Apply Network Settings step.

(input)

Specifies whether the destination computer joins an Active Directory domain or a workgroup.

Value values
      0 : Join an Active Directory domain

<!-- p.503 -->

      1 : Join a workgroup

OSDPartitions
Applies to the Format and Partition Disk step.

(input)

This task sequence variable is an array variable of partition settings. Each element in the array
represents the settings for a single partition on the hard disk. Access the settings defined for
each partition by combining the array variable name with the zero-based disk partition number
and the property name.

Use the following variable names to define the properties for the first partition that this step
creates on the hard disk:

OSDPartitions0Type

Specifies the type of partition. This property is required. Valid values are Primary , Extended ,
Logical , and Hidden .

OSDPartitions0FileSystem
Specifies the type of file system to use when formatting the partition. This property is optional.
If you don't specify a file system, the step doesn't format the partition. Valid values are FAT32
and NTFS .

OSDPartitions0Bootable

Specifies whether the partition is bootable. This property is required. If this value is set to TRUE
for MBR disks, then the step marks this partition as active.

OSDPartitions0QuickFormat
Specifies the type of format that is used. This property is required. If this value is set to TRUE ,
the step performs a quick format. Otherwise, the step performs a full format.

OSDPartitions0VolumeName
Specifies the name that's assigned to the volume when it's formatted. This property is optional.

<!-- p.504 -->

OSDPartitions0Size
Specifies the size of the partition. This property is optional. If this property isn't specified, the
partition is created using all remaining free space. Units are specified by the
OSDPartitions0SizeUnits variable.

OSDPartitions0SizeUnits

The step uses these units to interpret the OSDPartitions0Size variable. This property is
optional. Valid values are MB (default), GB , and Percent .

OSDPartitions0VolumeLetterVariable
When this step creates partitions, it always uses the next available drive letter in Windows PE.
Use this optional property to specify the name of another task sequence variable. The step uses
this variable to save the new drive letter for future reference.

If you define multiple partitions with this task sequence step, the properties for the second
partition are defined by using the 1 index in the variable name. For example:
OSDPartitions1Type, OSDPartitions1FileSystem, OSDPartitions1Bootable,
OSDPartitions1QuickFormat, and OSDPartitions1VolumeName.

OSDPartitionStyle
Applies to the Format and Partition Disk step.

(input)

Specifies the partition style to use when partitioning the disk.

Valid values
      GPT : Use the GUID Partition Table style

      MBR : Use the master boot record partition style

OSDProductKey
Applies to the Apply Windows Settings step.

(input)

Specifies the Windows product key. The specified value must be between 1 and 255 characters.

<!-- p.505 -->

OSDRandomAdminPassword
Applies to the Apply Windows Settings step.

(input)

Specifies a randomly generated password for the local Administrator account in the new OS.

Valid values
      true (default): Windows Setup disables the local Administrator account on the target

     computer

      false : Windows Setup enables the local administrator account on the target computer,

     and sets the account password to the value of OSDLocalAdminPassword

OSDRecoveryKeyPollingFrequency
Applies to the Enable BitLocker step.

Applies to version 2203 and later.

The frequency, in seconds, that the BitLocker action will poll the site database for recovery key
escrow status. Minimum value is 15 seconds. Default value is 300 seconds (5 minutes).

OSDRecoveryKeyPollingTimeout
Applies to the Enable BitLocker step.

Applies to version 2203 and later.

The maximum number of seconds for the BitLocker action to wait for the recovery key to be
escrowed to the site database. Minimum value is 30 seconds. Default value is 1800 seconds (30
minutes).

OSDRegisteredOrgName (input)
Applies to the Apply Windows Settings step.

Specifies the default registered organization name in the new OS. The specified value must be
between 1 and 255 characters.

OSDRegisteredOrgName (output)

<!-- p.506 -->

Applies to the Capture Windows Settings step.

Set to the registered organization name of the computer. The value is set only if the
OSDMigrateRegistrationInfo variable is set to true .

OSDRegisteredUserName
Applies to the Apply Windows Settings step.

(input)

Specifies the default registered user name in the new OS. The specified value must be between
1 and 255 characters.

OSDServerLicenseConnectionLimit
Applies to the Apply Windows Settings step.

(input)

Specifies the maximum number of connections allowed. The specified number must be in the
range between 5 and 9999 connections.

OSDServerLicenseMode
Applies to the Apply Windows Settings step.

(input)

Specifies the Windows Server license mode that's used.

Valid values
      PerSeat

      PerServer

OSDSetupAdditionalUpgradeOptions
Applies to the Upgrade Operating System step.

(input)

<!-- p.507 -->

Specifies the additional command-line options that are added to Windows Setup during an
upgrade. The task sequence doesn't verify the command-line options.

For more information, see Windows Setup Command-Line Options.

OSDStateFallbackToNAA
Applies to the Request State Store step.

(input)

When the computer account fails to connect to the state migration point, this variable specifies
whether the task sequence falls back to use the network access account (NAA).

For more information on the network access account, see Accounts.

Valid values
      true
      false (default)

OSDStateSMPRetryCount
Applies to the Request State Store step.

(input)

Specifies the number of times that the task sequence step tries to find a state migration point
before the step fails. The specified count must be between 0 and 600.

OSDStateSMPRetryTime
Applies to the Request State Store step.

(input)

Specifies the number of seconds that the task sequence step waits between retry attempts. The
number of seconds can be a maximum of 30 characters.

OSDStateStorePath
Applies to the following steps:

<!-- p.508 -->

     Capture User State
     Release State Store
     Request State Store
     Restore User State

(input)

The network share or local path name of the folder where the task sequence saves or restores
the user state. There is no default value.

OSDTargetSystemDrive
Applies to the Apply OS Image step.

(output)

Specifies the drive letter of the partition that contains the OS files after the image is applied.

OSDTargetSystemRoot (input)
Applies to the Capture OS Image step.

Specifies the path to the Windows directory of the installed OS on the reference computer. The
task sequence verifies it as a supported OS for capture by Configuration Manager.

OSDTargetSystemRoot (output)
Applies to the Prepare Windows for Capture step.

Specifies the path to the Windows directory of the installed OS on the reference computer. The
task sequence verifies it as a supported OS for capture by Configuration Manager.

OSDTimeZone (input)
Applies to the Apply Windows Settings step.

Specifies the default time zone setting that's used in the new OS.

Set the value of this variable to the language invariant name of time zone. For example, use the
string in the Std value for a time zone under the following registry key:
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Time Zones .

OSDTimeZone (output)

<!-- p.509 -->

Applies to the Capture Windows Settings step.

Set to the time zone of the computer. The value is set only if the OSDMigrateTimeZone
variable is set to true .

OSDWindowsSettingsInputLocale
Applies to the Apply Windows Settings step.

Specifies the default input locale setting that's used in the new OS.

For more information on the Windows setup answer file value, see Microsoft-Windows-
International-Core - InputLocale.

OSDWindowsSettingsSystemLocale
Applies to the Apply Windows Settings step.

Specifies the default system locale setting that's used in the new OS.

For more information on the Windows setup answer file value, see Microsoft-Windows-
International-Core - SystemLocale.

OSDWindowsSettingsUILanguage
Applies to the Apply Windows Settings step.

Specifies the default user interface language setting that's used in the new OS.

For more information on the Windows setup answer file value, see Microsoft-Windows-
International-Core - UILanguage.

OSDWindowsSettingsUILanguageFallback
Applies to the Apply Windows Settings step.

Specifies the fallback user interface language setting that's used in the new OS.

For more information on the Windows setup answer file value, see Microsoft-Windows-
International-Core - UILanguageFallback.

OSDWindowsSettingsUserLocale

<!-- p.510 -->

Applies to the Apply Windows Settings step.

Specifies the default user locale setting that's used in the new OS.

For more information on the Windows setup answer file value, see Microsoft-Windows-
International-Core - UserLocale.

OSDWipeDestinationPartition
Applies to the Apply Data Image step.

(input)

Specifies whether to delete the files located on the destination partition.

Valid values
       true (default)

       false

OSDWorkgroupName
Applies to the Apply Network Settings step.

(input)

Specifies the name of the workgroup that the destination computer joins.

Specify either this variable or the OSDDomainName variable. The workgroup name can be a
maximum of 32 characters.

SetupCompletePause
Applies to the Upgrade Operating System step.

Use this variable to address timing issues with the Window 10 in-place upgrade task sequence
on high performance devices when Windows setup is complete. When you assign a value in
seconds to this variable, the Windows setup process delays that amount of time before it starts
the task sequence. This timeout provides the Configuration Manager client additional time to
initialize.

The following log entries are common examples of this issue that you can remediate with this
variable:

<!-- p.511 -->

     The TSManager component records entries similar to the following errors in the
     smsts.log:

          log

          Failed to initate policy evaluation for namespace 'root\ccm\policy\machine',
          hr=0x80041010
          Error compiling client config policies. code 80041010
          Task Sequence Manager could not initialize Task Sequence Environment. code
          80041010

     Windows setup records entries similar to the following errors in the setupcomplete.log:

          log

          Running C:\windows\CCM\\TSMBootstrap.exe to resume task sequence
          ERRORLEVEL = -1073741701
          TSMBootstrap did not request reboot, resetting registry
          Exiting setupcomplete.cmd

SMSClientInstallProperties
Applies to the Setup Windows and ConfigMgr step.

(input)

Specifies the client installation properties that the task sequence uses when installing the
Configuration Manager client.

For more information, see About client installation parameters and properties.

SMSConnectNetworkFolderAccount
Applies to the Connect To Network Folder step.

(input)

Specifies the user account that is used to connect to the network share in
SMSConnectNetworkFolderPath. Specify the account password with the
SMSConnectNetworkFolderPassword value.

For more information on the task sequence network folder connection account, see Accounts.

SMSConnectNetworkFolderDriveLetter

<!-- p.512 -->

Applies to the Connect To Network Folder step.

(input)

Specifies the network drive letter to connect to. This value is optional. If it's not specified, then
the network connection isn't mapped to a drive letter. If this value is specified, the value must
be in the range from D to Z. Don't use X, it's the drive letter used by Windows PE during the
Windows PE phase.

Examples
      D:
      E:

SMSConnectNetworkFolderPassword
Applies to the Connect To Network Folder step.

(input)

Specifies the password for the SMSConnectNetworkFolderAccount that is used to connect to
the network share in SMSConnectNetworkFolderPath.

SMSConnectNetworkFolderPath
Applies to the Connect To Network Folder step.

(input)

Specifies the network path for the connection. If you need to map this path to a drive letter,
use the SMSConnectNetworkFolderDriveLetter value.

Example
\\server\share

SMSInstallUpdateTarget
Applies to the Install Software Updates step.

(input)

Specifies whether to install all updates or only mandatory updates.

<!-- p.513 -->

Valid values
      All

      Mandatory

SMSRebootMessage
Applies to the Restart Computer step.

(input)

Specifies the message to be displayed to users before restarting the destination computer. If
this variable isn't set, the default message text is displayed. The specified message can't exceed
512 characters.

Example
Save your work before the computer restarts.

SMSRebootTimeout
Applies to the Restart Computer step.

(input)

Specifies the number of seconds that the warning is displayed to the user before the computer
restarts.

Examples
      0 (default): Don't display a reboot message

      60 : Display the warning for one minute

SMSTSAllowTokenAuthURLForACP
Applies to version 2203 and later

When you use the SMSTSDownloadProgram variable to use an alternate content provider, set
this variable to true to allow it to use token authentication. If you don't set this variable or set
it to false , it skips any token authentication sources. The alternate content provider has to
support token authentication.

<!-- p.514 -->

For more information, see CMG client authentication.

SMSTSAssignmentsDownloadInterval
The number of seconds to wait before the client attempts to download the policy since the last
attempt that returned no policies. By default, the client waits 0 seconds before retrying.

You can set this variable by using a prestart command from media or PXE.

SMSTSAssignmentsDownloadRetry
The number of times a client attempts to download the policy after no policies are found on
the first attempt. By default, the client retries 0 times.

You can set this variable by using a prestart command from media or PXE.

SMSTSAssignUsersMode
Specifies how a task sequence associates users with the destination computer. Set the variable
to one of the following values:

     Auto: When the task sequence deploys the OS to the destination computer, it creates a
     relationship between the specified users and destination computer.

     Pending: The task sequence creates a relationship between the specified users and the
     destination computer. An administrator must approve the relationship to set it.

     Disabled: The task sequence doesn't associate users with the destination computer when
     it deploys the OS.

  ７ Note

  When setting the *SMSTSAssignUsersMode variable, the value specified needs to match
  what is configured on the PXE enabled DP, boot media, or pre-staged media being used
  for imaging.

  If the values don't match, then device affinity isn't set.

  For more information, see Associate users with a destination computer in Configuration
  Manager.

SMSTSDisableStatusRetry

<!-- p.515 -->

In disconnected scenarios, the task sequence engine repeatedly tries to send status messages
to the management point. This behavior in this scenario causes delays in task sequence
processing.

Set this variable to true and the task sequence engine doesn't attempt to send status
messages after the first message fails to send. This first attempt includes multiple retries.

When the task sequence restarts, the value of this variable persists. However, the task sequence
tries sending an initial status message. This first attempt includes multiple retries. If successful,
the task sequence continues sending status regardless of the value of this variable. If status
fails to send, the task sequence uses the value of this variable.

  ７ Note

  Task sequence status reporting relies upon these status messages to display the progress,
  history, and details of each step. If status messages fail to send, they're not queued. When
  connectivity is restored to the management point, they're not sent at a later time. This
  behavior results in task sequence status reporting to be incomplete and missing items.

SMSTSDisableWow64Redirection
Applies to the Run Command Line step.

(input)

By default on a 64-bit OS, the task sequence locates and runs the program in the command
line using the WOW64 file system redirector. This behavior allows the command to find 32-bit
versions of OS programs and DLLs. Setting this variable to true disables the use of the
WOW64 file system redirector. The command finds native 64-bit versions of OS programs and
DLLs. This variable has no effect when running on a 32-bit OS.

SMSTSDownloadAbortCode
This variable contains the abort code value for the external program downloader. This program
is specified in the SMSTSDownloadProgram variable. If the program returns an error code
equal to the value of the SMSTSDownloadAbortCode variable, then the content download fails
and no other download method is attempted.

SMSTSDownloadProgram

<!-- p.516 -->

Use this variable to specify an alternate content provider (ACP). An ACP is a downloader
program that's used to download content. The task sequence uses the ACP instead of the
default Configuration Manager downloader. As part of the content download process, the task
sequence checks this variable. If specified, the task sequence runs the program to download
the content.

SMSTSDownloadRetryCount
The number of times that Configuration Manager attempts to download content from a
distribution point. By default, the client retries 2 times.

SMSTSDownloadRetryDelay
The number of seconds that Configuration Manager waits before it retries to download
content from a distribution point. By default, the client waits 15 seconds before retrying.

SMSTSDriverRequestConnectTimeOut
Applies to the Auto Apply Drivers step.

When requesting the driver catalog, this variable is the number of seconds the task sequence
waits for the HTTP server connection. If the connection takes longer than the timeout setting,
the task sequence cancels the request. By default, the timeout is set to 60 seconds.

SMSTSDriverRequestReceiveTimeOut
Applies to the Auto Apply Drivers step.

When requesting the driver catalog, this variable is the number of seconds the task sequence
waits for a response. If the connection takes longer than the timeout setting, the task sequence
cancels the request. By default, the timeout is set to 480 seconds.

SMSTSDriverRequestResolveTimeOut
Applies to the Auto Apply Drivers step.

When requesting the driver catalog, this variable is the number of seconds the task sequence
waits for HTTP name resolution. If the connection takes longer than the timeout setting, the
task sequence cancels the request. By default, the timeout is set to 60 seconds.

SMSTSDriverRequestSendTimeOut

<!-- p.517 -->

Applies to the Auto Apply Drivers step.

When sending a request for the driver catalog, this variable is the number of seconds the task
sequence waits to send the request. If the request takes longer than the timeout setting, the
task sequence cancels the request. By default, the timeout is set to 60 seconds.

SMSTSErrorDialogTimeout
When an error occurs in a task sequence, it displays a dialog box with the error. The task
sequence automatically dismisses it after the number of seconds specified by this variable. By
default, this value is 900 seconds (15 minutes).

SMSTSLanguageFolder
Use this variable to change the display language of a language neutral boot image.

SMSTSLocalDataDrive
Specifies where the task sequence stores temporary cache files on the destination computer
while it's running.

Set this variable before the task sequence starts, such as by setting a collection variable. Once
the task sequence starts, Configuration Manager defines the _SMSTSMDataPath variable based
on what the SMSTSLocalDataDrive variable was defined to.

SMSTSMP
Use this variable to specify the URL or IP address of the Configuration Manager management
point.

SMSTSMPListRequestTimeoutEnabled
Applies to the following steps:

      Install Application
      Install Software Updates

(input)

If the client isn't on the intranet, use this variable to enable repeated MPList requests to refresh
the client. By default, this variable is set to True .

<!-- p.518 -->

When clients are on the internet, set this variable to False to avoid unnecessary delays.

SMSTSMPListRequestTimeout
Applies to the following steps:

     Install Application
     Install Software Updates

(input)

If the task sequence fails to retrieve the management point list (MPList) from location services,
this variable specifies how many milliseconds it waits before it retries the step. By default, the
task sequence waits 60000 milliseconds (60 seconds) before it retries. It retries up to three
times.

SMSTSPeerDownload
Use this variable to enable the client to use Windows PE peer cache. Setting this variable to
true enables this functionality.

SMSTSPeerRequestPort
A custom network port that Windows PE peer cache uses for the initial broadcast. The default
port configured in client settings is 8004.

SMSTSPersistContent
Use this variable to temporarily persist content in the task sequence cache. This variable is
different from SMSTSPreserveContent, which keeps content in the Configuration Manager
client cache after the task sequence is complete. SMSTSPersistContent uses the task sequence
cache, SMSTSPreserveContent uses the Configuration Manager client cache.

SMSTSPostAction
Specifies a command that's run after the task sequence completes. Just before exiting the task
sequence, the TSManager process spawns the specified post action. It doesn't wait or record
any status, just exits after calling that command.

For example, specify shutdown.exe /r /t 30 /f to restart the computer 30 seconds after the
task sequence completes.

<!-- p.519 -->

SMSTSPreferredAdvertID
Forces the task sequence to run a specific targeted deployment on the destination computer.
Set this variable through a prestart command from media or PXE. If this variable is set, the task
sequence overrides any required deployments.

SMSTSPreserveContent
This variable flags the content in the task sequence to be kept in the Configuration Manager
client cache after the deployment. This variable is different from SMSTSPersistContent, which
only keeps the content for the duration of the task sequence. SMSTSPersistContent uses the
task sequence cache, SMSTSPreserveContent uses the Configuration Manager client cache. Set
SMSTSPreserveContent to true to enable this functionality.

SMSTSRebootDelay
Specifies how many seconds to wait before the computer restarts. If this variable is zero (0), the
task sequence manager doesn't display a notification dialog before reboot.

Example
     0 : don't display a notification

     60 : display a notification for one minute

SMSTSRebootDelayNext
Use this variable with the existing SMSTSRebootDelay variable. If you want any later reboots to
happen with a different timeout than the first, set SMSTSRebootDelayNext to a different value
in seconds.

Example
You want to give users a 60-minute reboot notification at the start of a Windows in-place
upgrade task sequence. After that first long timeout, you want additional timeouts to only be
60 seconds. Set SMSTSRebootDelay to 3600 , and SMSTSRebootDelayNext to 60 .

SMSTSRebootMessage

<!-- p.520 -->

Specifies the message to display in the restart notification dialog. If this variable isn't set, a
default message appears.

Example
The task sequence is restarting this computer

SMSTSRebootRequested
Indicates that a restart is requested after the current task sequence step is completed. If the
task sequence step requires a restart to complete the action, set this variable. After the
computer restarts, the task sequence continues to run from the next task sequence step.

      HD : Restart to the installed OS
      WinPE : Restart to the associated boot image

SMSTSRetryRequested
Requests a retry after the current task sequence step is completed. If this task sequence
variable is set, also configure the SMSTSRebootRequested variable. After the computer is
restarted, the task sequence manager reruns the same task sequence step.

SMSTSRunCommandLineAsUser
Applies to the Run Command Line step.

Use task sequence variables to configure the user context for the Run Command Line step. You
don't need to configure the Run Command Line step with a placeholder account to use the
SMSTSRunCommandLineUserName and SMSTSRunCommandLineUserPassword variables.

Configure SMSTSRunCommandLineAsUser with one of the following values:

      true : Any further Run Command Line steps run in the context of the user specified in

      SMSTSRunCommandLineUserName .

      false : Any further Run Command Line steps run in the context that you configured on

     the step.

SMSTSRunCommandLineUserName
Applies to the Run Command Line step.
