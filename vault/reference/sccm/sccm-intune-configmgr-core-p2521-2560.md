---
title: "Core infrastructure documentation — pages 2521-2560"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2521-2560
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2521-2560
family: sccm
documentKind: "doc"
abstract: "(String) Status (UInt16) StatusInfo (String) Stepping (String) SystemName (String) UniqueId (UInt16) UpgradeMethod (String) Version (UInt32) VoltageCaps (String) Workgroup Protected Volume Information Namespace: root\\cimv2\\sms class CCM_ProtectedVolumeInfo (String) Name (String)"
---

# Core infrastructure documentation — pages 2521-2560

<!-- p.2521 -->

    (String) Status

    (UInt16) StatusInfo

    (String) Stepping

    (String) SystemName

    (String) UniqueId

    (UInt16) UpgradeMethod

    (String) Version

    (UInt32) VoltageCaps

    (String) Workgroup

Protected Volume Information
Namespace: root\cimv2\sms

class CCM_ProtectedVolumeInfo

    (String) Name

    (String) DriveLetter

    (UInt32) ProtectionType

Protocol
Namespace: root\cimv2

class Win32_NetworkProtocol

    (String) Name

    (String) Caption

    (Boolean) ConnectionlessService

    (String) Description

    (Boolean) GuaranteesDelivery

    (Boolean) GuaranteesSequencing

<!-- p.2522 -->

     (DateTime) InstallDate

     (UInt32) MaximumAddressSize

     (UInt32) MaximumMessageSize

     (Boolean) MessageOriented

     (UInt32) MinimumAddressSize

     (Boolean) PseudoStreamOriented

     (String) Status

     (Boolean) SupportsBroadcasting

     (Boolean) SupportsConnectData

     (Boolean) SupportsDisconnectData

     (Boolean) SupportsEncryption

     (Boolean) SupportsExpeditedData

     (Boolean) SupportsFragmentation

     (Boolean) SupportsGracefulClosing

     (Boolean) SupportsGuaranteedBandwidth

     (Boolean) SupportsMulticasting

     (Boolean) SupportsQualityofService

Quick Fix Engineering
Namespace: root\cimv2

class Win32_QuickFixEngineering

     (String) HotFixID

     (String) ServicePackInEffect

     (String) Caption

     (String) Description

<!-- p.2523 -->

    (String) FixComments

    (DateTime) InstallDate

    (String) InstalledBy

    (String) InstalledOn

    (String) Name

    (String) Status

CCM Recently Used Applications
Namespace: root\cimv2\sms

class CCM_RecentlyUsedApps

    (String) ExplorerFileName

    (String) FolderPath

    (String) LastUserName

    (String) AdditionalProductCodes

    (String) CompanyName

    (String) FileDescription

    (String) FilePropertiesHash

    (UInt32) FileSize

    (String) FileVersion

    (DateTime) LastUsedTime

    (UInt32) LaunchCount

    (String) msiDisplayName

    (String) msiPublisher

    (String) msiVersion

    (String) OriginalFileName

<!-- p.2524 -->

     (String) ProductCode

     (UInt32) ProductLanguage

     (String) ProductName

     (String) ProductVersion

     (String) SoftwarePropertiesHash

Registry
Namespace: root\cimv2

class Win32_Registry

     (String) Name

     (String) Caption

     (UInt32) CurrentSize

     (String) Description

     (DateTime) InstallDate

     (UInt32) MaximumSize

     (UInt32) ProposedSize

     (String) Status

SCSI Controller
Namespace: root\cimv2

class Win32_SCSIController

     (String) DeviceID

     (UInt16) Availability

     (String) Caption

     (UInt32) ConfigManagerErrorCode

     (Boolean) ConfigManagerUserConfig

<!-- p.2525 -->

(UInt32) ControllerTimeouts

(String) Description

(String) DeviceMap

(String) DriverName

(Boolean) ErrorCleared

(String) ErrorDescription

(String) HardwareVersion

(UInt32) Index

(DateTime) InstallDate

(UInt32) LastErrorCode

(String) Manufacturer

(UInt32) MaxDataWidth

(UInt32) MaxNumberControlled

(UInt64) MaxTransferRate

(String) Name

(String) PNPDeviceID

(UInt16) PowerManagementCapabilities[]

(Boolean) PowerManagementSupported

(UInt16) ProtectionManagement

(UInt16) ProtocolSupported

(String) Status

(UInt16) StatusInfo

(String) SystemName

(DateTime) TimeOfLastReset

<!-- p.2526 -->

Serial Port Configuration
Namespace: root\cimv2

class Win32_SerialPortConfiguration

     (String) Name

     (Boolean) AbortReadWriteOnError

     (UInt32) BaudRate

     (Boolean) BinaryModeEnabled

     (UInt32) BitsPerByte

     (String) Caption

     (Boolean) ContinueXMitOnXOff

     (Boolean) CTSOutflowControl

     (String) Description

     (Boolean) DiscardNULLBytes

     (Boolean) DSROutflowControl

     (Boolean) DSRSensitivity

     (String) DTRFlowControlType

     (UInt32) EOFCharacter

     (UInt32) ErrorReplaceCharacter

     (Boolean) ErrorReplacementEnabled

     (UInt32) EventCharacter

     (Boolean) IsBusy

     (String) Parity

     (Boolean) ParityCheckEnabled

     (String) RTSFlowControlType

     (String) SettingID

<!-- p.2527 -->

     (String) StopBits

     (UInt32) XOffCharacter

     (UInt32) XOffXMitThreshold

     (UInt32) XOnCharacter

     (UInt32) XOnXMitThreshold

     (UInt32) XOnXOffInFlowControl

     (UInt32) XOnXOffOutFlowControl

Serial Ports
Namespace: root\cimv2

class Win32_SerialPort

     (String) DeviceID

     (UInt16) Availability

     (Boolean) Binary

     (UInt16) Capabilities[]

     (String) CapabilityDescriptions[]

     (String) Caption

     (UInt32) ConfigManagerErrorCode

     (Boolean) ConfigManagerUserConfig

     (String) Description

     (Boolean) ErrorCleared

     (String) ErrorDescription

     (DateTime) InstallDate

     (UInt32) LastErrorCode

     (UInt32) MaxBaudRate

<!-- p.2528 -->

(UInt32) MaximumInputBufferSize

(UInt32) MaximumOutputBufferSize

(UInt32) MaxNumberControlled

(String) Name

(Boolean) OSAutoDiscovered

(String) PNPDeviceID

(UInt16) PowerManagementCapabilities[]

(Boolean) PowerManagementSupported

(UInt16) ProtocolSupported

(String) ProviderType

(Boolean) SettableBaudRate

(Boolean) SettableDataBits

(Boolean) SettableFlowControl

(Boolean) SettableParity

(Boolean) SettableParityCheck

(Boolean) SettableRLSD

(Boolean) SettableStopBits

(String) Status

(UInt16) StatusInfo

(Boolean) Supports16BitMode

(Boolean) SupportsDTRDSR

(Boolean) SupportsElapsedTimeouts

(Boolean) SupportsIntTimeouts

(Boolean) SupportsParityCheck

(Boolean) SupportsRLSD

<!-- p.2529 -->

     (Boolean) SupportsRTSCTS

     (Boolean) SupportsSpecialCharacters

     (Boolean) SupportsXOnXOff

     (Boolean) SupportsXOnXOffSet

     (String) SystemName

     (DateTime) TimeOfLastReset

Server Feature
Namespace: root\cimv2

class Win32_ServerFeature

     (UInt32) ID

     (String) Name

     (UInt32) ParentID

Services
Namespace: root\cimv2

class Win32_Service

     (String) Name

     (Boolean) AcceptPause

     (Boolean) AcceptStop

     (String) Caption

     (UInt32) CheckPoint

     (String) Description

     (Boolean) DesktopInteract

     (String) DisplayName

     (String) ErrorControl

<!-- p.2530 -->

     (UInt32) ExitCode

     (DateTime) InstallDate

     (String) PathName

     (UInt32) ProcessId

     (UInt32) ServiceSpecificExitCode

     (String) ServiceType

     (Boolean) Started

     (String) StartMode

     (String) StartName

     (String) State

     (String) Status

     (String) SystemName

     (UInt32) TagId

     (UInt32) WaitHint

Shares
Namespace: root\cimv2

class Win32_Share

     (String) Name

     (UInt32) AccessMask

     (Boolean) AllowMaximum

     (String) Caption

     (String) Description

     (DateTime) InstallDate

     (UInt32) MaximumAllowed

<!-- p.2531 -->

     (String) Path

     (String) Status

     (UInt32) Type

SW Licensing Product
Namespace: root\cimv2

class SoftwareLicensingProduct

     (String) ID

     (String) ApplicationID

     (String) Description

     (DateTime) EvaluationEndDate

     (UInt32) GracePeriodRemaining

     (UInt32) LicenseStatus

     (String) MachineURL

     (String) Name

     (String) OfflineInstallationId

     (String) PartialProductKey

     (String) ProcessorURL

     (String) ProductKeyID

     (String) ProductKeyURL

     (String) UseLicenseURL

SW Licensing Service
Namespace: root\cimv2

class SoftwareLicensingService

     (String) Version

<!-- p.2532 -->

     (String) ClientMachineID

     (UInt32) IsKeyManagementServiceMachine

     (UInt32) KeyManagementServiceCurrentCount

     (String) KeyManagementServiceMachine

     (String) KeyManagementServiceProductKeyID

     (UInt32) PolicyCacheRefreshRequired

     (UInt32) RequiredClientCount

     (UInt32) VLActivationInterval

     (UInt32) VLRenewalInterval

Software Shortcut
Namespace: root\cimv2\sms

class SMS_SoftwareShortcut

     (String) ShortcutKey

     (String) BinFileVersion

     (String) BinProductVersion

     (String) Description

     (String) FilePropertiesHash

     (String) FilePropertiesHashEx

     (UInt32) FileSize

     (String) FileVersion

     (UInt32) Language

     (String) ParentName

     (String) Product

     (String) ProductCode

<!-- p.2533 -->

    (String) ProductVersion

    (String) Publisher

    (String) ShortcutName

    (UInt32) ShortcutType

    (String) TargetExecutable

SMS_SoftwareTag
Namespace: root\cimv2\sms

class SMS_SoftwareTag

    (String) TagCreatorRegid

    (String) UniqueID

    (String) DisplayVersion

    (Boolean) EntitlementRequired

    (String) ProductName

    (String) SoftwareCreator

    (String) SoftwareCreatorRegid

    (String) SoftwareLicensor

    (String) SoftwareLicensorRegid

    (String) TagCreator

    (SInt32) VersionMajor

    (SInt32) VersionMinor

Sound Devices
Namespace: root\cimv2

class Win32_SoundDevice

    (String) DeviceID

<!-- p.2534 -->

    (UInt16) Availability

    (String) Caption

    (UInt32) ConfigManagerErrorCode

    (Boolean) ConfigManagerUserConfig

    (String) Description

    (UInt16) DMABufferSize

    (Boolean) ErrorCleared

    (String) ErrorDescription

    (DateTime) InstallDate

    (UInt32) LastErrorCode

    (String) Manufacturer

    (UInt32) MPU401Address

    (String) Name

    (String) PNPDeviceID

    (UInt16) PowerManagementCapabilities[]

    (Boolean) PowerManagementSupported

    (String) ProductName

    (String) Status

    (UInt16) StatusInfo

    (String) SystemName

System Account
Namespace: root\cimv2

class Win32_SystemAccount

    (String) Domain

<!-- p.2535 -->

    (String) Name

    (String) Caption

    (String) Description

    (DateTime) InstallDate

    (String) SID

    (UInt8) SIDType

    (String) Status

System Boot Data
Namespace: root\CCM

class CCM_SystemBootData

    (UInt64) SystemStartTime

    (UInt32) BiosDuration

    (UInt16) BootDiskMediaType

    (UInt32) BootDuration

    (UInt32) EventLogStart

    (UInt32) GPDuration

    (String) OSVersion

    (UInt32) UpdateDuration

System Boot Summary
Namespace: root\CCM

class CCM_SystemBootSummary

    (UInt32) AverageBootFrequency

    (UInt32) LatestBiosDuration

    (UInt32) LatestBootDuration

<!-- p.2536 -->

    (UInt32) LatestCoreBootDuration

    (UInt32) LatestEventLogStart

    (UInt32) LatestGPDuration

    (UInt32) LatestUpdateDuration

    (UInt32) MaxBiosDuration

    (UInt32) MaxBootDuration

    (UInt32) MaxCoreBootDuration

    (UInt32) MaxEventLogStart

    (UInt32) MaxGPDuration

    (UInt32) MaxUpdateDuration

    (UInt32) MedianBiosDuration

    (UInt32) MedianBootDuration

    (UInt32) MedianCoreBootDuration

    (UInt32) MedianEventLogStart

    (UInt32) MedianGPDuration

    (UInt32) MedianUpdateDuration

System Console Usage
Namespace: root\cimv2\sms

class SMS_SystemConsoleUsage

    (DateTime) SecurityLogStartDate

    (String) TopConsoleUser

    (UInt32) TotalConsoleTime

    (UInt32) TotalConsoleUsers

    (UInt32) TotalSecurityLogTime

<!-- p.2537 -->

System Console User
Namespace: root\cimv2\sms

class SMS_SystemConsoleUser

     (String) SystemConsoleUser

     (DateTime) LastConsoleUse

     (UInt32) NumberOfConsoleLogons

     (UInt32) TotalUserConsoleMinutes

System Devices
Namespace: root\cimv2\sms

class CCM_SystemDevices

     (String) Name

     (String) CompatibleIDs[]

     (String) DeviceID

     (String) HardwareIDs[]

     (Boolean) IsPnP

System Drivers
Namespace: root\cimv2

class Win32_SystemDriver

     (String) Name

     (Boolean) AcceptPause

     (Boolean) AcceptStop

     (String) Caption

     (String) Description

<!-- p.2538 -->

    (Boolean) DesktopInteract

    (String) DisplayName

    (String) ErrorControl

    (UInt32) ExitCode

    (DateTime) InstallDate

    (String) PathName

    (UInt32) ServiceSpecificExitCode

    (String) ServiceType

    (Boolean) Started

    (String) StartMode

    (String) StartName

    (String) State

    (String) Status

    (String) SystemName

    (UInt32) TagId

System Enclosure
Namespace: root\cimv2

class Win32_SystemEnclosure

    (String) Tag

    (Boolean) AudibleAlarm

    (String) BreachDescription

    (String) CableManagementStrategy

    (String) Caption

    (UInt16) ChassisTypes[]

<!-- p.2539 -->

(SInt16) CurrentRequiredOrProduced

(String) Description

(UInt16) HeatGeneration

(Boolean) HotSwappable

(DateTime) InstallDate

(Boolean) LockPresent

(String) Manufacturer

(String) Model

(String) Name

(UInt16) NumberOfPowerCords

(String) OtherIdentifyingInfo

(String) PartNumber

(Boolean) PoweredOn

(Boolean) Removable

(Boolean) Replaceable

(UInt16) SecurityBreach

(UInt16) SecurityStatus

(String) SerialNumber

(String) ServiceDescriptions[]

(UInt16) ServicePhilosophy[]

(String) SKU

(String) SMBIOSAssetTag

(String) Status

(String) TypeDescriptions[]

(String) Version

<!-- p.2540 -->

     (Boolean) VisibleAlarm

Tape Drive
Namespace: root\cimv2

class Win32_TapeDrive

     (String) DeviceID

     (UInt16) Availability

     (UInt16) Capabilities[]

     (String) CapabilityDescriptions[]

     (String) Caption

     (UInt32) Compression

     (String) CompressionMethod

     (UInt32) ConfigManagerErrorCode

     (Boolean) ConfigManagerUserConfig

     (UInt64) DefaultBlockSize

     (String) Description

     (UInt32) ECC

     (UInt32) EOTWarningZoneSize

     (Boolean) ErrorCleared

     (String) ErrorDescription

     (String) ErrorMethodology

     (UInt32) FeaturesHigh

     (UInt32) FeaturesLow

     (String) ID

     (DateTime) InstallDate

<!-- p.2541 -->

    (UInt32) LastErrorCode

    (String) Manufacturer

    (UInt64) MaxBlockSize

    (UInt64) MaxMediaSize

    (UInt32) MaxPartitionCount

    (String) MediaType

    (UInt64) MinBlockSize

    (String) Name

    (Boolean) NeedsCleaning

    (UInt32) NumberOfMediaSupported

    (UInt32) Padding

    (String) PNPDeviceID

    (UInt16) PowerManagementCapabilities[]

    (Boolean) PowerManagementSupported

    (UInt32) ReportSetMarks

    (String) Status

    (UInt16) StatusInfo

    (String) SystemName

Time Zone
Namespace: root\cimv2

class Win32_TimeZone

    (String) StandardName

    (SInt32) Bias

    (String) Caption

<!-- p.2542 -->

    (SInt32) DaylightBias

    (UInt32) DaylightDay

    (UInt8) DaylightDayOfWeek

    (UInt32) DaylightHour

    (UInt32) DaylightMillisecond

    (UInt32) DaylightMinute

    (UInt32) DaylightMonth

    (String) DaylightName

    (UInt32) DaylightSecond

    (UInt32) DaylightYear

    (String) Description

    (String) SettingID

    (UInt32) StandardBias

    (UInt32) StandardDay

    (UInt8) StandardDayOfWeek

    (UInt32) StandardHour

    (UInt32) StandardMillisecond

    (UInt32) StandardMinute

    (UInt32) StandardMonth

    (UInt32) StandardSecond

    (UInt32) StandardYear

TPM
Namespace: root\CIMv2\Security\MicrosoftTpm

class Win32_Tpm

<!-- p.2543 -->

     (Boolean) IsActivated_InitialValue

     (Boolean) IsEnabled_InitialValue

     (Boolean) IsOwned_InitialValue

     (UInt32) ManufacturerId

     (String) ManufacturerVersion

     (String) ManufacturerVersionInfo

     (String) PhysicalPresenceVersionInfo

     (String) SpecVersion

TPM Status
Namespace: root\cimv2\sms

class SMS_TPM

     (Boolean) IsReady

     (UInt32) Information

     (Boolean) IsApplicable

TS Issued License
Namespace: root\cimv2

class Win32_TSIssuedLicense

     (UInt32) LicenseId

     (DateTime) ExpirationDate

     (DateTime) IssueDate

     (UInt32) KeyPackId

     (UInt32) LicenseStatus

     (String) sHardwareId

     (String) sIssuedToComputer

<!-- p.2544 -->

     (String) sIssuedToUser

TS License Key Pack
Namespace: root\cimv2

class Win32_TSLicenseKeyPack

     (UInt32) KeyPackId

     (UInt32) AvailableLicenses

     (String) Description

     (UInt32) IssuedLicenses

     (UInt32) KeyPackType

     (UInt32) ProductType

     (String) ProductVersion

     (UInt32) TotalLicenses

Uninterruptible Power Supply
Namespace: root\cimv2

class Win32_UninterruptiblePowerSupply

     (String) DeviceID

     (UInt16) ActiveInputVoltage

     (UInt16) Availability

     (Boolean) BatteryInstalled

     (Boolean) CanTurnOffRemotely

     (String) Caption

     (String) CommandFile

     (UInt32) ConfigManagerErrorCode

     (Boolean) ConfigManagerUserConfig

<!-- p.2545 -->

(String) Description

(Boolean) ErrorCleared

(String) ErrorDescription

(UInt16) EstimatedChargeRemaining

(UInt32) EstimatedRunTime

(UInt32) FirstMessageDelay

(DateTime) InstallDate

(Boolean) IsSwitchingSupply

(UInt32) LastErrorCode

(Boolean) LowBatterySignal

(UInt32) MessageInterval

(String) Name

(String) PNPDeviceID

(Boolean) PowerFailSignal

(UInt16) PowerManagementCapabilities[]

(Boolean) PowerManagementSupported

(UInt32) Range1InputFrequencyHigh

(UInt32) Range1InputFrequencyLow

(UInt32) Range1InputVoltageHigh

(UInt32) Range1InputVoltageLow

(UInt32) Range2InputFrequencyHigh

(UInt32) Range2InputFrequencyLow

(UInt32) Range2InputVoltageHigh

(UInt32) Range2InputVoltageLow

(UInt16) RemainingCapacityStatus

<!-- p.2546 -->

     (String) Status

     (UInt16) StatusInfo

     (String) SystemName

     (UInt32) TimeOnBackup

     (UInt32) TotalOutputPower

     (UInt16) TypeOfRangeSwitching

     (String) UPSPort

USB Controller
Namespace: root\cimv2

class Win32_USBController

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

<!-- p.2547 -->

    (UInt16) PowerManagementCapabilities[]

    (Boolean) PowerManagementSupported

    (UInt16) ProtocolSupported

    (String) Status

    (UInt16) StatusInfo

    (String) SystemName

    (DateTime) TimeOfLastReset

USB Device
Namespace: root\cimv2

class Win32_USBDevice

    (String) DeviceID

    (String) Caption

    (String) ClassGuid

    (UInt32) ConfigManagerErrorCode

    (Boolean) ConfigManagerUserConfig

    (String) CreationClassName

    (String) Description

    (String) Manufacturer

    (String) Name

    (String) PNPDeviceID

    (String) Service

    (String) Status

    (String) SystemCreationClassName

    (String) SystemName

<!-- p.2548 -->

USM User Profile
Namespace: root\cimv2

class Win32_UserProfile

     (String) SID

     (UInt8) HealthStatus

     (String) LastAttemptedProfileDownloadTime

     (String) LastAttemptedProfileUploadTime

     (String) LastBackgroundRegistryUploadTime

     (DateTime) LastDownloadTime

     (DateTime) LastUploadTime

     (DateTime) LastUseTime

     (Boolean) Loaded

     (String) LocalPath

     (UInt32) RefCount

     (Boolean) RoamingConfigured

     (String) RoamingPath

     (Boolean) RoamingPreference

     (Boolean) Special

     (UInt32) Status

Video Controller
Namespace: root\cimv2

class Win32_VideoController

     (String) DeviceID

     (UInt16) AcceleratorCapabilities[]

<!-- p.2549 -->

(String) AdapterCompatibility

(String) AdapterDACType

(UInt32) AdapterRAM

(UInt16) Availability

(String) CapabilityDescriptions[]

(String) Caption

(UInt32) ColorTableEntries

(UInt32) ConfigManagerErrorCode

(Boolean) ConfigManagerUserConfig

(UInt32) CurrentBitsPerPixel

(UInt32) CurrentHorizontalResolution

(UInt64) CurrentNumberOfColors

(UInt32) CurrentNumberOfColumns

(UInt32) CurrentNumberOfRows

(UInt32) CurrentRefreshRate

(UInt16) CurrentScanMode

(UInt32) CurrentVerticalResolution

(String) Description

(UInt32) DeviceSpecificPens

(UInt32) DitherType

(DateTime) DriverDate

(String) DriverVersion

(Boolean) ErrorCleared

(String) ErrorDescription

(UInt32) ICMIntent

<!-- p.2550 -->

(UInt32) ICMMethod

(String) InfFilename

(String) InfSection

(DateTime) InstallDate

(String) InstalledDisplayDrivers

(UInt32) LastErrorCode

(UInt32) MaxMemorySupported

(UInt32) MaxNumberControlled

(UInt32) MaxRefreshRate

(UInt32) MinRefreshRate

(Boolean) Monochrome

(String) Name

(UInt16) NumberOfColorPlanes

(UInt32) NumberOfVideoPages

(String) PNPDeviceID

(UInt16) PowerManagementCapabilities[]

(Boolean) PowerManagementSupported

(UInt16) ProtocolSupported

(UInt32) ReservedSystemPaletteEntries

(UInt32) SpecificationVersion

(String) Status

(UInt16) StatusInfo

(String) SystemName

(UInt32) SystemPaletteEntries

(DateTime) TimeOfLastReset

<!-- p.2551 -->

     (UInt16) VideoArchitecture

     (UInt16) VideoMemoryType

     (UInt16) VideoMode

     (String) VideoModeDescription

     (String) VideoProcessor

Virtual Application Packages
Namespace: root\Microsoft\appvirt\client

class Package

     (String) PackageGUID

     (UInt64) CachedLaunchSize

     (UInt16) CachedPercentage

     (UInt64) CachedSize

     (UInt64) LaunchSize

     (String) Name

     (String) SftPath

     (UInt64) TotalSize

     (String) Version

     (String) VersionGUID

Virtual Applications
Namespace: root\Microsoft\appvirt\client

class Application

     (String) Name

     (String) Version

     (String) CachedOsdPath

<!-- p.2552 -->

     (UInt32) GlobalRunningCount

     (DateTime) LastLaunchOnSystem

     (Boolean) Loading

     (String) OriginalOsdPath

     (String) PackageGUID

Virtual Machine (64)
Namespace: root\cimv2

class Win32Reg_SMSGuestVirtualMachine64

     (String) InstanceKey

     (String) PhysicalHostName

     (String) PhysicalHostNameFullyQualified

Virtual Machine
Namespace: root\cimv2

class Win32Reg_SMSGuestVirtualMachine

     (String) InstanceKey

     (String) PhysicalHostName

     (String) PhysicalHostNameFullyQualified

Virtual Machine Details
Namespace: root\vm\VirtualServer

class VirtualMachine

     (String) Name

     (UInt32) CpuUtilization

     (UInt64) DiskBytesRead

<!-- p.2553 -->

    (UInt64) DiskBytesWritten

    (UInt64) DiskSpaceUsed

    (UInt64) HeartbeatCount

    (UInt32) HeartbeatInterval

    (UInt32) HeartbeatPercentage

    (UInt32) HeartbeatRate

    (UInt64) NetworkBytesReceived

    (UInt64) NetworkBytesSent

    (UInt64) PhysicalMemoryAllocated

    (UInt32) Uptime

Volume
Namespace: root\cimv2

class Win32_Volume

    (String) DeviceID

    (UInt16) Access

    (Boolean) Automount

    (UInt16) Availability

    (UInt64) BlockSize

    (UInt64) Capacity

    (String) Caption

    (Boolean) Compressed

    (UInt32) ConfigManagerErrorCode

    (Boolean) ConfigManagerUserConfig

    (String) CreationClassName

<!-- p.2554 -->

(String) Description

(Boolean) DirtyBitSet

(String) DriveLetter

(UInt32) DriveType

(Boolean) ErrorCleared

(String) ErrorDescription

(String) ErrorMethodology

(String) FileSystem

(UInt64) FreeSpace

(Boolean) IndexingEnabled

(DateTime) InstallDate

(String) Label

(UInt32) LastErrorCode

(UInt32) MaximumFileNameLength

(String) Name

(UInt64) NumberOfBlocks

(String) PNPDeviceID

(UInt16) PowerManagementCapabilities[]

(Boolean) PowerManagementSupported

(String) Purpose

(Boolean) QuotasEnabled

(Boolean) QuotasIncomplete

(Boolean) QuotasRebuilding

(UInt32) SerialNumber

(String) Status

<!-- p.2555 -->

    (UInt16) StatusInfo

    (Boolean) SupportsDiskQuotas

    (Boolean) SupportsFileBasedCompression

    (String) SystemCreationClassName

    (String) SystemName

CCM_WebAppInstallInfo
Namespace: root\ccm\cimodels

class CCM_WebAppInstallInfo

    (String) AppDeliveryTypeId

    (UInt32) AppDtRevision

    (String) TargetURL

    (String) UserSID

    (String) URLFileName

    (String) URLPath

SMS_Windows8Application
Namespace: root\cimv2\sms

class SMS_Windows8Application

    (String) FullName

    (String) ApplicationName

    (String) Architecture

    (Boolean) ConfigMgrManaged

    (String) DependencyApplicationNames

    (String) FamilyName

    (String) InstalledLocation

<!-- p.2556 -->

    (Boolean) IsFramework

    (String) Publisher

    (String) PublisherId

    (String) Version

SMS_Windows8ApplicationUserInfo
Namespace: root\cimv2\sms

class SMS_Windows8ApplicationUserInfo

    (String) FullName

    (String) UserSecurityId

    (String) InstallState

    (String) UserAccountName

Windows Update
Namespace: root\cimv2

class Win32Reg_SMSWindowsUpdate

    (String) InstanceKey

    (UInt32) AUOptions

    (UInt32) NoAutoUpdate

    (UInt32) UseWUServer

Windows Update Agent Version
Namespace: root\cimv2\sms

class Win32_WindowsUpdateAgentVersion

    (String) Version

<!-- p.2557 -->

Write Filter State
Namespace: root\cimv2\sms

class CCM_WriteFilterState

     (Boolean) WriteFilterEnabled

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2558 -->

Security and privacy for hardware
inventory in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This topic contains security and privacy information for hardware inventory in
Configuration Manager.

Security best practices for hardware inventory
Use the following security best practices for when you collect hardware inventory data
from clients:

                                                                                   ﾉ   Expand table

 Security best         More information
 practice

 Sign and encrypt      When clients communicate with management points by using HTTPS, all
 inventory data        data that they send is encrypted by using SSL. However, when client
                       computers use HTTP to communicate with management points on the
                       intranet, client inventory data and collected files can be sent unsigned and
                       unencrypted. Make sure that the site is configured to require signing and
                       use encryption. In addition, if clients can support the SHA-256 algorithm,
                       select the option to require SHA-256.

 Do not collect        You can use IDMIF and NOIDMIF file collection to extend hardware inventory
 IDMIF and             collection. When necessary, Configuration Manager creates new tables or
 NOIDMIF files in      modifies existing tables in the Configuration Manager database to
 high-security         accommodate the properties in IDMIF and NOIDMIF files. However,
 environments          Configuration Manager does not validate IDMIF and NOIDMIF files, so these
                       files could be used to alter tables that you do not want altered. Valid data
                       could be overwritten by invalid data. In addition, large amounts of data
                       could be added and the processing of this data might cause delays in all
                       Configuration Manager functions. To mitigate these risks, configure the
                       hardware inventory client setting Collect MIF files as None.

Security issues for hardware inventory
Collecting inventory exposes potential vulnerabilities. Attackers can perform the
following:

<!-- p.2559 -->

     Send invalid data, which will be accepted by the management point even when the
     software inventory client setting is disabled and file collection is not enabled.

     Send excessively large amounts of data in a single file and in lots of files, which
     might cause a denial of service.

     Access inventory information as it is transferred to Configuration Manager.

     Because a user with local administrative privileges can send any information as
     inventory data, do not consider inventory data that is collected by Configuration
     Manager to be authoritative.

     Hardware inventory is enabled by default as a client setting.

Privacy information for hardware inventory
Hardware inventory allows you to retrieve any information that is stored in the registry
and in WMI on Configuration Manager clients. Software inventory allows you to discover
all files of a specified type or to collect any specified files from clients. Asset Intelligence
enhances the inventory capabilities by extending hardware and software inventory and
adding new license management functionality.

Hardware inventory is enabled by default as a client setting and the WMI information
collected is determined by options that you select. Software inventory is enabled by
default but files are not collected by default. Asset Intelligence data collection is
automatically enabled, although you can select the hardware inventory reporting classes
to enable.

Inventory information is not sent to Microsoft. Inventory information is stored in the
Configuration Manager database. When clients use HTTPS to connect to management
points, the inventory data that they send to the site is encrypted during the transfer. If
clients use HTTP to connect to management points, you have the option to enable
inventory encryption. The inventory data is not stored in encrypted format in the
database. Information is retained in the database until it is deleted by the site
maintenance tasks Delete Aged Inventory History or Delete Aged Collected Files every
90 days. You can configure the deletion interval.

Before you configure hardware inventory, software inventory, file collection, or Asset
Intelligence data collection, consider your privacy requirements.

Feedback

<!-- p.2560 -->

Was this page helpful?      Yes    No

Provide product feedback
