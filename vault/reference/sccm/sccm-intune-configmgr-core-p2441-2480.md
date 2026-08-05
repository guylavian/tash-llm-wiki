---
title: "Core infrastructure documentation — pages 2441-2480"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2441-2480
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2441-2480
family: sccm
documentKind: "doc"
abstract: "(String) DeviceID (String) DriveLetter (String) PersistentVolumeID (UInt32) ProtectionStatus BitLocker Encryption Details Namespace: root\\cimv2 class Win32_BitLockerEncryptionDetails (String) BitlockerPersistentVolumeId (SInt32) Compliant (SInt32) ConversionStatus (String) Devic"
---

# Core infrastructure documentation — pages 2441-2480

<!-- p.2441 -->

     (String) DeviceID

     (String) DriveLetter

     (String) PersistentVolumeID

     (UInt32) ProtectionStatus

BitLocker Encryption Details
Namespace: root\cimv2

class Win32_BitLockerEncryptionDetails

     (String) BitlockerPersistentVolumeId

     (SInt32) Compliant

     (SInt32) ConversionStatus

     (String) DeviceId

     (String) DriveLetter

     (SInt32) EncryptionMethod

     (String) EnforcePolicyDate

     (Boolean) IsAutoUnlockEnabled

     (SInt32) KeyProtectorTypes[]

     (String) MbamPersistentVolumeId

     (SInt32) MbamVolumeType

     (String) NoncomplianceDetectedDate

     (SInt32) ProtectionStatus

     (SInt32) ReasonsForNonCompliance[]

BitLocker Policy
Namespace: root\cimv2

class Win32Reg_MBAMPolicy

<!-- p.2442 -->

     (String) EncodedComputerName

     (UInt32) EncryptionMethod

     (UInt32) FixedDataDriveAutoUnlock

     (UInt32) FixedDataDriveEncryption

     (UInt32) FixedDataDrivePassphrase

     (String) KeyName

     (String) LastConsoleUser

     (UInt32) MBAMMachineError

     (UInt32) MBAMPolicyEnforced

     (UInt32) OsDriveEncryption

     (UInt32) OsDriveProtector

     (DateTime) UserExemptionDate

Boot Configuration
Namespace: root\cimv2

class Win32_BootConfiguration

     (String) Name

     (String) BootDirectory

     (String) ConfigurationPath

     (String) Description

     (String) LastDrive

     (String) ScratchDirectory

     (String) SettingID

     (String) TempDirectory

Browser Helper Object

<!-- p.2443 -->

Namespace: root\cimv2\sms

class SMS_BrowserHelperObject

    (String) FilePropertiesHash

    (String) BinFileVersion

    (String) BinProductVersion

    (String) CLSID

    (String) Description

    (String) FileName

    (String) FilePropertiesHashEx

    (String) FileVersion

    (String) Product

    (String) ProductVersion

    (String) Publisher

    (String) Version

CCM_RAX
Namespace: root\ccm\cimodels

class CCM_RAXInfo

    (String) AppID

    (String) FeedURL

    (String) UserSID

CD-ROM
Namespace: root\cimv2

class Win32_CDROMDrive

    (String) DeviceID

<!-- p.2444 -->

(UInt16) Availability

(UInt16) Capabilities[]

(String) CapabilityDescriptions[]

(String) Caption

(String) CompressionMethod

(UInt32) ConfigManagerErrorCode

(Boolean) ConfigManagerUserConfig

(UInt64) DefaultBlockSize

(String) Description

(String) Drive

(Boolean) DriveIntegrity

(Boolean) ErrorCleared

(String) ErrorDescription

(String) ErrorMethodology

(UInt16) FileSystemFlags

(UInt32) FileSystemFlagsEx

(String) ID

(DateTime) InstallDate

(UInt32) LastErrorCode

(String) Manufacturer

(UInt64) MaxBlockSize

(UInt32) MaximumComponentLength

(UInt64) MaxMediaSize

(Boolean) MediaLoaded

(String) MediaType

<!-- p.2445 -->

     (UInt64) MinBlockSize

     (String) Name

     (Boolean) NeedsCleaning

     (UInt32) NumberOfMediaSupported

     (String) PNPDeviceID

     (UInt16) PowerManagementCapabilities[]

     (Boolean) PowerManagementSupported

     (String) RevisionLevel

     (UInt32) SCSIBus

     (UInt16) SCSILogicalUnit

     (UInt16) SCSIPort

     (UInt16) SCSITargetId

     (UInt64) Size

     (String) Status

     (UInt16) StatusInfo

     (String) SystemName

     (String) VolumeName

     (String) VolumeSerialNumber

Client Diagnostics
Starting in version 2107

Namespace: root\cimv2

class CCM_ClientDiagnostics

     (String) Identifier

     (String) DebugLoggingEnabled

<!-- p.2446 -->

     (UInt32) LogEnabled

     (UInt32) LogLevel

     (UInt32) LogMaxHistory

     (UInt32) LogMaxSize

Client Events
Namespace: root\ccm\invagt

class ClientEvents

     (String) EventName

     (UInt16) Count

Computer System
Namespace: root\cimv2

class Win32_ComputerSystem

     (String) Name

     (UInt16) AdminPasswordStatus

     (Boolean) AutomaticResetBootOption

     (Boolean) AutomaticResetCapability

     (UInt16) BootOptionOnLimit

     (UInt16) BootOptionOnWatchDog

     (Boolean) BootROMSupported

     (String) BootupState

     (String) Caption

     (UInt16) ChassisBootupState

     (SInt16) CurrentTimeZone

     (Boolean) DaylightInEffect

<!-- p.2447 -->

(String) Description

(String) Domain

(UInt16) DomainRole

(UInt16) FrontPanelResetStatus

(Boolean) InfraredSupported

(String) InitialLoadInfo[]

(DateTime) InstallDate

(UInt16) KeyboardPasswordStatus

(String) LastLoadInfo

(String) Manufacturer

(String) Model

(String) NameFormat

(Boolean) NetworkServerModeEnabled

(UInt32) NumberOfProcessors

(String) OEMLogoBitmap

(String) OEMStringArray[]

(SInt64) PauseAfterReset

(UInt16) PowerManagementCapabilities[]

(Boolean) PowerManagementSupported

(UInt16) PowerOnPasswordStatus

(UInt16) PowerState

(UInt16) PowerSupplyState

(String) PrimaryOwnerContact

(String) PrimaryOwnerName

(UInt16) ResetCapability

<!-- p.2448 -->

    (SInt16) ResetCount

    (SInt16) ResetLimit

    (String) Roles[]

    (String) Status

    (String) SupportContactDescription[]

    (UInt16) SystemStartupDelay

    (String) SystemStartupOptions[]

    (UInt8) SystemStartupSetting

    (String) SystemType

    (UInt16) ThermalState

    (UInt64) TotalPhysicalMemory

    (String) UserName

    (UInt16) WakeUpType

Computer System Ex
Namespace: root\cimv2

class CCM_ComputerSystemExtended

    (String) Name

    (UInt16) PCSystemType

Computer System Product
Namespace: root\cimv2

class Win32_ComputerSystemProduct

    (String) IdentifyingNumber

    (String) Name

    (String) Version

<!-- p.2449 -->

    (String) Caption

    (String) Description

    (String) SKUNumber

    (String) UUID

    (String) Vendor

SMS Advanced Client Ports
Namespace: root\cimv2

class Win32Reg_SMSAdvancedClientPorts

    (String) InstanceKey

    (UInt32) HttpsPortName

    (UInt32) PortName

SMS Advanced Client SSL Configurations
Namespace: root\cimv2

class Win32Reg_SMSAdvancedClientSSLConfiguration

    (String) InstanceKey

    (String) CertificateSelectionCriteria

    (String) CertificateStore

    (UInt32) ClientAlwaysOnInternet

    (UInt32) HttpsStateFlags

    (String) InternetMPHostName

    (UInt32) SelectFirstCertificate

SMS Advanced Client State
Namespace: root\ccm

<!-- p.2450 -->

class CCM_InstalledComponent

    (String) Name

    (String) DisplayName

    (String) Version

Connected Device
Namespace: root\SmsDm

class SMS_ActiveSyncConnectedDevice

    (String) DeviceOEMInfo

    (String) DeviceType

    (String) OS_Major

    (String) OS_Minor

    (String) OS_Platform

    (String) ProcessorArchitecture

    (String) ProcessorLevel

    (String) ProcessorRevision

    (String) InstalledClientID

    (String) InstalledClientServer

    (String) InstalledClientVersion

    (String) LastSyncTime

    (String) OS_AdditionalInfo

    (String) OS_Build

SMS_DefaultBrowser
Namespace: root\cimv2\sms

class SMS_DefaultBrowser

<!-- p.2451 -->

    (String) BrowserProgId

Desktop
Namespace: root\cimv2

class Win32_Desktop

    (String) Name

    (UInt32) BorderWidth

    (String) Caption

    (Boolean) CoolSwitch

    (UInt32) CursorBlinkRate

    (String) Description

    (Boolean) DragFullWindows

    (UInt32) GridGranularity

    (UInt32) IconSpacing

    (String) IconTitleFaceName

    (UInt32) IconTitleSize

    (Boolean) IconTitleWrap

    (String) Pattern

    (Boolean) ScreenSaverActive

    (String) ScreenSaverExecutable

    (Boolean) ScreenSaverSecure

    (UInt32) ScreenSaverTimeout

    (String) SettingID

    (String) Wallpaper

    (Boolean) WallpaperStretched

<!-- p.2452 -->

    (Boolean) WallpaperTiled

Desktop Monitor
Namespace: root\cimv2

class Win32_DesktopMonitor

    (String) DeviceID

    (UInt16) Availability

    (UInt32) Bandwidth

    (String) Caption

    (UInt32) ConfigManagerErrorCode

    (Boolean) ConfigManagerUserConfig

    (String) Description

    (UInt16) DisplayType

    (Boolean) ErrorCleared

    (String) ErrorDescription

    (DateTime) InstallDate

    (Boolean) IsLocked

    (UInt32) LastErrorCode

    (String) MonitorManufacturer

    (String) MonitorType

    (String) Name

    (UInt32) PixelsPerXLogicalInch

    (UInt32) PixelsPerYLogicalInch

    (String) PNPDeviceID

    (UInt16) PowerManagementCapabilities[]

<!-- p.2453 -->

     (Boolean) PowerManagementSupported

     (UInt32) ScreenHeight

     (UInt32) ScreenWidth

     (String) Status

     (UInt16) StatusInfo

     (String) SystemName

Device Info
Namespace: Reserved

class Device_Info

     (String) CertExpiry

     (String) DeviceName

     (String) Manufacturer

     (String) Model

     (String) OS

MDM DevDetail
Namespace: root\cimv2\mdm\dmmap

class MDM_DevDetail_Ext01

     (String) InstanceID

     (String) ParentID

     (String) DeviceHardwareData

     (String) WLANMACAddress

Disk
Namespace: root\cimv2

<!-- p.2454 -->

class Win32_DiskDrive

     (String) DeviceID

     (UInt16) Availability

     (UInt32) BytesPerSector

     (UInt16) Capabilities[]

     (String) CapabilityDescriptions[]

     (String) Caption

     (String) CompressionMethod

     (UInt32) ConfigManagerErrorCode

     (Boolean) ConfigManagerUserConfig

     (UInt64) DefaultBlockSize

     (String) Description

     (Boolean) ErrorCleared

     (String) ErrorDescription

     (String) ErrorMethodology

     (UInt32) Index

     (DateTime) InstallDate

     (String) InterfaceType

     (UInt32) LastErrorCode

     (String) Manufacturer

     (UInt64) MaxBlockSize

     (UInt64) MaxMediaSize

     (Boolean) MediaLoaded

     (String) MediaType

     (UInt64) MinBlockSize

<!-- p.2455 -->

    (String) Model

    (String) Name

    (Boolean) NeedsCleaning

    (UInt32) NumberOfMediaSupported

    (UInt32) Partitions

    (String) PNPDeviceID

    (UInt16) PowerManagementCapabilities[]

    (Boolean) PowerManagementSupported

    (UInt32) SCSIBus

    (UInt16) SCSILogicalUnit

    (UInt16) SCSIPort

    (UInt16) SCSITargetId

    (UInt32) SectorsPerTrack

    (UInt64) Size

    (String) Status

    (UInt16) StatusInfo

    (String) SystemName

    (UInt64) TotalCylinders

    (UInt32) TotalHeads

    (UInt64) TotalSectors

    (UInt64) TotalTracks

    (UInt32) TracksPerCylinder

Partition
Namespace: root\cimv2

<!-- p.2456 -->

class Win32_DiskPartition

     (String) DeviceID

     (UInt16) Access

     (UInt16) Availability

     (UInt64) BlockSize

     (Boolean) Bootable

     (Boolean) BootPartition

     (String) Caption

     (UInt32) ConfigManagerErrorCode

     (Boolean) ConfigManagerUserConfig

     (String) Description

     (UInt32) DiskIndex

     (Boolean) ErrorCleared

     (String) ErrorDescription

     (String) ErrorMethodology

     (UInt32) HiddenSectors

     (UInt32) Index

     (DateTime) InstallDate

     (UInt32) LastErrorCode

     (String) Name

     (UInt64) NumberOfBlocks

     (String) PNPDeviceID

     (UInt16) PowerManagementCapabilities[]

     (Boolean) PowerManagementSupported

     (Boolean) PrimaryPartition

<!-- p.2457 -->

    (String) Purpose

    (Boolean) RewritePartition

    (UInt64) Size

    (UInt64) StartingOffset

    (String) Status

    (UInt16) StatusInfo

    (String) SystemName

    (String) Type

DMA
Namespace: root\cimv2

class Win32_DeviceMemoryAddress

    (UInt64) StartingAddress

    (String) Caption

    (String) Description

    (UInt64) EndingAddress

    (DateTime) InstallDate

    (String) MemoryType

    (String) Name

    (String) Status

DMA Channel
Namespace: root\cimv2

class Win32_DMAChannel

    (UInt32) DMAChannel

    (UInt16) AddressSize

<!-- p.2458 -->

    (UInt16) Availability

    (Boolean) BurstMode

    (UInt16) ByteMode

    (String) Caption

    (UInt16) ChannelTiming

    (String) Description

    (DateTime) InstallDate

    (UInt32) MaxTransferSize

    (String) Name

    (UInt32) Port

    (String) Status

    (UInt16) TransferWidths[]

    (UInt16) TypeCTiming

    (UInt16) WordMode

Driver - VxD
Namespace: root\cimv2

class Win32_DriverVXD

    (String) Name

    (String) SoftwareElementID

    (UInt16) SoftwareElementState

    (UInt16) TargetOperatingSystem

    (String) Version

    (String) BuildNumber

    (String) Caption

<!-- p.2459 -->

    (String) CodeSet

    (String) Control

    (String) Description

    (String) DeviceDescriptorBlock

    (String) IdentificationCode

    (DateTime) InstallDate

    (String) LanguageEdition

    (String) Manufacturer

    (String) OtherTargetOS

    (String) PM_API

    (String) SerialNumber

    (UInt32) ServiceTableSize

    (String) Status

    (String) V86_API

Embedded Device Information
Namespace: root\cimv2\sms

class CCM_EmbeddedDeviceInformation

    (String) DeviceType

    (String) Model

    (String) OEMName

Environment
Namespace: root\cimv2

class Win32_Environment

    (String) Name

<!-- p.2460 -->

     (String) UserName

     (String) Caption

     (String) Description

     (DateTime) InstallDate

     (String) Status

     (Boolean) SystemVariable

     (String) VariableValue

Firmware
Namespace: root\cimv2\sms

class SMS_Firmware

     (Boolean) UEFI

     (Boolean) SecureBoot

USM Folder Redirection Health
Namespace: root\cimv2\sms

class SMS_FolderRedirectionHealth

     (String) FolderName

     (String) SID

     (UInt8) HealthStatus

     (DateTime) LastSuccessfulSyncTime

     (UInt8) LastSyncStatus

     (DateTime) LastSyncTime

     (Boolean) OfflineAccessEnabled

     (String) OfflineFileNameFolderGUID

     (Boolean) Redirected

<!-- p.2461 -->

IDE Controller
Namespace: root\cimv2

class Win32_IDEController

     (String) DeviceID

     (UInt16) Availability

     (String) Caption

     (UInt32) ConfigManagerErrorCode

     (Boolean) ConfigManagerUserConfig

     (String) Description

     (Boolean) ErrorCleared

     (String) ErrorDescription

     (DateTime) InstallDate

     (UInt32) LastErrorCode

     (String) Manufacturer

     (UInt32) MaxNumberControlled

     (String) Name

     (String) PNPDeviceID

     (UInt16) PowerManagementCapabilities[]

     (Boolean) PowerManagementSupported

     (UInt16) ProtocolSupported

     (String) Status

     (UInt16) StatusInfo

     (String) SystemName

     (DateTime) TimeOfLastReset

<!-- p.2462 -->

Add Remove Programs (64)
Namespace: root\cimv2

class Win32Reg_AddRemovePrograms64

     (String) ProdID

     (String) DisplayName

     (String) InstallDate

     (String) Publisher

     (String) Version

Add Remove Programs
Namespace: root\cimv2

class Win32Reg_AddRemovePrograms

     (String) ProdID

     (String) DisplayName

     (String) InstallDate

     (String) Publisher

     (String) Version

Installed Executable
Namespace: root\cimv2\sms

class SMS_InstalledExecutable

     (String) ExecutableName

     (String) ProductCode

     (String) BinFileVersion

     (String) BinProductVersion

<!-- p.2463 -->

     (String) Description

     (String) FilePropertiesHash

     (String) FilePropertiesHashEx

     (UInt32) FileSize

     (String) FileVersion

     (Boolean) HasPatchAdded

     (String) InstalledFilePath

     (Boolean) IsSystemFile

     (Boolean) IsVitalFile

     (UInt32) Language

     (String) Product

     (String) ProductVersion

     (String) Publisher

Installed Software
Namespace: root\cimv2\sms

class SMS_InstalledSoftware

     (String) SoftwareCode

     (String) ARPDisplayName

     (String) ChannelCode

     (String) ChannelID

     (String) CM_DSLID

     (String) EvidenceSource

     (DateTime) InstallDate

     (UInt32) InstallDirectoryValidation

<!-- p.2464 -->

    (String) InstalledLocation

    (String) InstallSource

    (UInt32) InstallType

    (UInt32) Language

    (String) LocalPackage

    (String) MPC

    (UInt32) OsComponent

    (String) PackageCode

    (String) ProductID

    (String) ProductName

    (String) ProductVersion

    (String) Publisher

    (String) RegisteredUser

    (String) ServicePack

    (String) SoftwarePropertiesHash

    (String) SoftwarePropertiesHashEx

    (String) UninstallString

    (String) UpgradeCode

    (UInt32) VersionMajor

    (UInt32) VersionMinor

IRQ Table
Namespace: root\cimv2

class Win32_IRQResource

    (UInt32) IRQNumber

<!-- p.2465 -->

    (UInt16) Availability

    (String) Caption

    (String) Description

    (Boolean) Hardware

    (DateTime) InstallDate

    (String) Name

    (Boolean) Shareable

    (String) Status

    (UInt16) TriggerLevel

    (UInt16) TriggerType

    (UInt32) Vector

Keyboard
Namespace: root\cimv2

class Win32_Keyboard

    (String) DeviceID

    (UInt16) Availability

    (String) Caption

    (UInt32) ConfigManagerErrorCode

    (Boolean) ConfigManagerUserConfig

    (String) Description

    (Boolean) ErrorCleared

    (String) ErrorDescription

    (DateTime) InstallDate

    (Boolean) IsLocked

<!-- p.2466 -->

     (UInt32) LastErrorCode

     (String) Layout

     (String) Name

     (UInt16) NumberOfFunctionKeys

     (UInt16) Password

     (String) PNPDeviceID

     (UInt16) PowerManagementCapabilities[]

     (Boolean) PowerManagementSupported

     (String) Status

     (UInt16) StatusInfo

     (String) SystemName

Load Order Group
Namespace: root\cimv2

class Win32_LoadOrderGroup

     (String) Name

     (String) Caption

     (String) Description

     (Boolean) DriverEnabled

     (UInt32) GroupOrder

     (DateTime) InstallDate

     (String) Status

Logical Disk
Namespace: root\cimv2\sms

class SMS_LogicalDisk

<!-- p.2467 -->

(String) DeviceID

(UInt16) Access

(UInt16) Availability

(UInt64) BlockSize

(String) Caption

(Boolean) Compressed

(UInt32) ConfigManagerErrorCode

(Boolean) ConfigManagerUserConfig

(String) Description

(UInt32) DriveType

(Boolean) ErrorCleared

(String) ErrorDescription

(String) ErrorMethodology

(String) FileSystem

(UInt64) FreeSpace

(DateTime) InstallDate

(UInt32) LastErrorCode

(UInt32) MaximumComponentLength

(UInt32) MediaType

(String) Name

(UInt64) NumberOfBlocks

(String) PNPDeviceID

(UInt16) PowerManagementCapabilities[]

(Boolean) PowerManagementSupported

(String) ProviderName

<!-- p.2468 -->

     (String) Purpose

     (UInt64) Size

     (String) Status

     (UInt16) StatusInfo

     (Boolean) SupportsFileBasedCompression

     (String) SystemName

     (String) VolumeName

     (String) VolumeSerialNumber

Memory
Namespace: root\cimv2

class CCM_LogicalMemoryConfiguration

     (String) Name

     (UInt64) AvailableVirtualMemory

     (UInt64) TotalPageFileSpace

     (UInt64) TotalPhysicalMemory

     (UInt64) TotalVirtualMemory

Device Bluetooth
Namespace: Reserved

class Device_Bluetooth

     (Boolean) Enabled

Device Camera
Namespace: Reserved

class Device_Camera

<!-- p.2469 -->

     (Boolean) Enabled

Device Certificates
Namespace: Reserved

class Device_Certificates

     (String) Thumbprint

     (String) Type

     (String) IssuedBy

     (String) IssuedTo

     (DateTime) ValidFrom

     (DateTime) ValidTo

Device Client
Namespace: Reserved

class Device_Client

     (Boolean) DownloadWhenRoaming

     (Boolean) SyncWhenRoaming

Device Client Agent version
Namespace: Reserved

class Device_ClientAgentVersion

     (String) Version

Device Computer System
Namespace: Reserved

class Device_ComputerSystem

<!-- p.2470 -->

  (String) CellularTechnology

  (String) DeviceClientID

  (String) DeviceManufacturer

  (String) DeviceModel

  (String) DMVersion

  (String) FirmwareVersion

  (String) HardwareVersion

  (String) IMEI

  (String) IMSI

  (UInt8) IsActivationLockEnabled

  (UInt8) Jailbroken

  (String) MEID

  (String) OEM

  (String) PhoneNumber

  (String) PlatformType

  (UInt32) ProcessorArchitecture

  (UInt32) ProcessorLevel

  (UInt32) ProcessorRevision

  (String) Product

  (String) ProductVersion

  (String) SerialNumber

  (String) SoftwareVersion

  (String) SubscriberCarrierNetwork

Device Display

<!-- p.2471 -->

Namespace: Reserved

class Device_Display

     (UInt32) HorizontalResolution

     (UInt64) NumberOfColors

     (UInt32) VerticalResolution

Device Email
Namespace: Reserved

class Device_Email

     (String) OwnerEmailAddress

     (String) SyncDomain

     (String) SyncServer

     (String) SyncUser

     (String) Type

Device Encryption
Namespace: Reserved

class Device_Encryption

     (UInt32) EmailEncryptionAlgorithm

     (UInt32) EmailEncryptionNegotiation

     (Boolean) EmailEncryptionRequired

     (Boolean) EmailSigningAlgorithm

     (Boolean) EmailSigningRequired

     (Boolean) EncryptionCompliance

     (Boolean) PhoneMemoryEncrypted

     (Boolean) StorageCardEncrypted

<!-- p.2472 -->

Device Exchange
Namespace: Reserved

class Device_Exchange

     (Boolean) ConflictResolution

     (SInt32) HTMLEmailTruncation

     (UInt32) MailFormat

     (UInt32) MaxCalendarAge

     (UInt32) MaxEmailAge

     (SInt32) MaxMailFileAttachmentSize

     (UInt32) OffPeakSyncFrequency

     (UInt32) PeakDays

     (String) PeakEndTime

     (String) PeakStartTime

     (UInt32) PeakSyncFrequency

     (SInt32) PlainTextEmailTruncation

     (Boolean) SendEmailImmediately

     (Boolean) SyncCalendar

     (Boolean) SyncContacts

     (Boolean) SyncEmail

     (Boolean) SyncTasks

     (Boolean) SyncWhenRoaming

Device Installed Applications
Namespace: Reserved

class Device_InstalledApplications

<!-- p.2473 -->

     (String) Name

     (String) Version

Device IrDA
Namespace: Reserved

class Device_IrDA

     (Boolean) Enabled

Mobile Device Location
Namespace: Reserved

class MDM_RemoteFind

     (Real32) Latitude

     (Real32) Longitude

Device Memory
Namespace: Reserved

class Device_Memory

     (UInt64) ProgramFree

     (UInt64) ProgramTotal

     (UInt64) RemovableStorageFree

     (UInt64) RemovableStorageTotal

     (UInt64) StorageFree

     (UInt64) StorageTotal

Device OS Information
Namespace: Reserved

<!-- p.2474 -->

class Device_OSInformation

     (String) Language

     (String) Platform

     (String) Version

Device Password
Namespace: Reserved

class Device_Password

     (Boolean) AllowRecoveryPassword

     (UInt32) AutolockTimeout

     (Boolean) Enabled

     (UInt32) Expiration

     (UInt32) History

     (UInt32) MaxAttemptsBeforeWipe

     (UInt32) MinComplexChars

     (UInt32) MinLength

     (UInt8) PasswordQuality

     (UInt32) Type

Device Policy
Namespace: Reserved

class Device_Policy

     (String) Name

     (Boolean) Enforced

Device Power

<!-- p.2475 -->

Namespace: Reserved

class Device_Power

     (UInt32) BacklightACTimeout

     (UInt32) BacklightBatTimeout

     (SInt32) BackupPercent

     (SInt32) BatteryPercent

Mobile Device Security Status
Namespace: Reserved

class MDM_SecurityStatus

     (UInt32) HardwareEncryptionCaps

     (UInt8) PasscodeCompliant

     (UInt8) PasscodeCompliantWithProfiles

     (UInt8) PasscodePresent

     (UInt8) RequireEncryption

Device Windows Security Policy
Namespace: Reserved

class Device_WindowsSecurityPolicy

     (UInt32) ID

     (String) Name

     (UInt32) Value

Device WLAN
Namespace: Reserved

class Device_WLAN

<!-- p.2476 -->

    (Boolean) Enabled

    (String) EthernetMAC

    (String) WiFiMAC

Modem
Namespace: root\cimv2

class Win32_POTSModem

    (String) DeviceID

    (UInt16) AnswerMode

    (String) AttachedTo

    (UInt16) Availability

    (String) BlindOff

    (String) BlindOn

    (String) Caption

    (String) CompatibilityFlags

    (UInt16) CompressionInfo

    (String) CompressionOff

    (String) CompressionOn

    (UInt32) ConfigManagerErrorCode

    (Boolean) ConfigManagerUserConfig

    (String) ConfigurationDialog

    (String) CountriesSupported[]

    (String) CountrySelected

    (String) CurrentPasswords[]

    (String) DCB

<!-- p.2477 -->

(String) Default

(String) Description

(String) DeviceLoader

(String) DeviceType

(UInt16) DialType

(DateTime) DriverDate

(Boolean) ErrorCleared

(String) ErrorControlForced

(UInt16) ErrorControlInfo

(String) ErrorControlOff

(String) ErrorControlOn

(String) ErrorDescription

(String) FlowControlHard

(String) FlowControlOff

(String) FlowControlSoft

(String) InactivityScale

(UInt32) InactivityTimeout

(UInt32) Index

(DateTime) InstallDate

(UInt32) LastErrorCode

(UInt32) MaxBaudRateToPhone

(UInt32) MaxBaudRateToSerialPort

(UInt16) MaxNumberOfPasswords

(String) Model

(String) ModemInfPath

<!-- p.2478 -->

(String) ModemInfSection

(String) ModulationBell

(String) ModulationCCITT

(UInt16) ModulationScheme

(String) Name

(String) PNPDeviceID

(String) PortSubClass

(UInt16) PowerManagementCapabilities[]

(Boolean) PowerManagementSupported

(String) Prefix

(String) Properties

(String) ProviderName

(String) Pulse

(String) Reset

(String) ResponsesKeyName

(UInt8) RingsBeforeAnswer

(String) SpeakerModeDial

(String) SpeakerModeOff

(String) SpeakerModeOn

(String) SpeakerModeSetup

(String) SpeakerVolumeHigh

(UInt16) SpeakerVolumeInfo

(String) SpeakerVolumeLow

(String) SpeakerVolumeMed

(String) Status

<!-- p.2479 -->

    (UInt16) StatusInfo

    (String) StringFormat

    (Boolean) SupportsCallback

    (Boolean) SupportsSynchronousConnect

    (String) SystemName

    (String) Terminator

    (DateTime) TimeOfLastReset

    (String) Tone

    (String) VoiceSwitchFeature

Motherboard
Namespace: root\cimv2

class Win32_MotherboardDevice

    (String) DeviceID

    (UInt16) Availability

    (String) Caption

    (UInt32) ConfigManagerErrorCode

    (Boolean) ConfigManagerUserConfig

    (String) Description

    (Boolean) ErrorCleared

    (String) ErrorDescription

    (DateTime) InstallDate

    (UInt32) LastErrorCode

    (String) Name

    (String) PNPDeviceID

<!-- p.2480 -->

     (UInt16) PowerManagementCapabilities[]

     (Boolean) PowerManagementSupported

     (String) PrimaryBusType

     (String) RevisionNumber

     (String) SecondaryBusType

     (String) Status

     (UInt16) StatusInfo

     (String) SystemName

NAP Client
Namespace: root\Nap

class NAP_Client

     (String) name

     (String) description

     (String) fixupURL

     (Boolean) napEnabled

     (String) napProtocolVersion

     (String) probationTime

     (UInt32) systemIsolationState

NAP System Health Agent
Namespace: root\Nap

class NAP_SystemHealthAgent

     (UInt32) ID

     (String) description

     (UInt32) fixupState
