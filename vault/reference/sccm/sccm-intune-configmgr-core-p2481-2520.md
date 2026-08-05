---
title: "Core infrastructure documentation — pages 2481-2520"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2481-2520
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2481-2520
family: sccm
documentKind: "doc"
abstract: "(String) friendlyName (String) infoClsid (Boolean) isBound (UInt8) percentage (String) registrationDate (String) vendorName (String) version Network Adapter Namespace: root\\cimv2 class Win32_NetworkAdapter (String) DeviceID (String) AdapterType (Boolean) AutoSense (UInt16) Avail"
---

# Core infrastructure documentation — pages 2481-2520

<!-- p.2481 -->

    (String) friendlyName

    (String) infoClsid

    (Boolean) isBound

    (UInt8) percentage

    (String) registrationDate

    (String) vendorName

    (String) version

Network Adapter
Namespace: root\cimv2

class Win32_NetworkAdapter

    (String) DeviceID

    (String) AdapterType

    (Boolean) AutoSense

    (UInt16) Availability

    (String) Caption

    (UInt32) ConfigManagerErrorCode

    (Boolean) ConfigManagerUserConfig

    (String) Description

    (Boolean) ErrorCleared

    (String) ErrorDescription

    (UInt32) Index

    (DateTime) InstallDate

    (Boolean) Installed

    (UInt32) LastErrorCode

<!-- p.2482 -->

    (String) MACAddress

    (String) Manufacturer

    (UInt32) MaxNumberControlled

    (UInt64) MaxSpeed

    (String) Name

    (String) NetworkAddresses[]

    (String) PermanentAddress

    (String) PNPDeviceID

    (UInt16) PowerManagementCapabilities[]

    (Boolean) PowerManagementSupported

    (String) ProductName

    (String) ServiceName

    (UInt64) Speed

    (String) Status

    (UInt16) StatusInfo

    (String) SystemName

    (DateTime) TimeOfLastReset

Network Adapter Configuration
Namespace: root\cimv2

class Win32_NetworkAdapterConfiguration

    (UInt32) Index

    (Boolean) ArpAlwaysSourceRoute

    (Boolean) ArpUseEtherSNAP

    (String) Caption

<!-- p.2483 -->

(String) DatabasePath

(Boolean) DeadGWDetectEnabled

(String) DefaultIPGateway[]

(UInt8) DefaultTOS

(UInt8) DefaultTTL

(String) Description

(Boolean) DHCPEnabled

(DateTime) DHCPLeaseExpires

(DateTime) DHCPLeaseObtained

(String) DHCPServer

(String) DNSDomain

(String) DNSDomainSuffixSearchOrder[]

(Boolean) DNSEnabledForWINSResolution

(String) DNSHostName

(String) DNSServerSearchOrder[]

(Boolean) DomainDNSRegistrationEnabled

(UInt32) ForwardBufferMemory

(Boolean) FullDNSRegistrationEnabled

(UInt16) GatewayCostMetric[]

(UInt8) IGMPLevel

(String) IPAddress[]

(UInt32) IPConnectionMetric

(Boolean) IPEnabled

(Boolean) IPFilterSecurityEnabled

(Boolean) IPPortSecurityEnabled

<!-- p.2484 -->

(String) IPSecPermitIPProtocols[]

(String) IPSecPermitTCPPorts[]

(String) IPSecPermitUDPPorts[]

(String) IPSubnet[]

(Boolean) IPUseZeroBroadcast

(String) IPXAddress

(Boolean) IPXEnabled

(String) IPXFrameType

(UInt32) IPXMediaType

(String) IPXNetworkNumber[]

(String) IPXVirtualNetNumber

(UInt32) KeepAliveInterval

(UInt32) KeepAliveTime

(String) MACAddress

(UInt32) MTU

(UInt32) NumForwardPackets

(Boolean) PMTUBHDetectEnabled

(Boolean) PMTUDiscoveryEnabled

(String) ServiceName

(String) SettingID

(UInt32) TcpipNetbiosOptions

(UInt32) TcpMaxConnectRetransmissions

(UInt32) TcpMaxDataRetransmissions

(UInt32) TcpNumConnections

(Boolean) TcpUseRFC1122UrgentPointer

<!-- p.2485 -->

     (UInt16) TcpWindowSize

     (Boolean) WINSEnableLMHostsLookup

     (String) WINSHostLookupFile

     (String) WINSPrimaryServer

     (String) WINSScopeID

     (String) WINSSecondaryServer

Network Client
Namespace: root\cimv2

class Win32_NetworkClient

     (String) Name

     (String) Caption

     (String) Description

     (DateTime) InstallDate

     (String) Manufacturer

     (String) Status

Network Login Profile
Namespace: root\cimv2

class Win32_NetworkLoginProfile

     (String) Name

     (DateTime) AccountExpires

     (UInt32) AuthorizationFlags

     (UInt32) BadPasswordCount

     (String) Caption

     (UInt32) CodePage

<!-- p.2486 -->

(String) Comment

(UInt32) CountryCode

(String) Description

(UInt32) Flags

(String) FullName

(String) HomeDirectory

(String) HomeDirectoryDrive

(DateTime) LastLogoff

(DateTime) LastLogon

(String) LogonHours

(String) LogonServer

(UInt64) MaximumStorage

(UInt32) NumberOfLogons

(String) Parameters

(DateTime) PasswordAge

(DateTime) PasswordExpires

(UInt32) PrimaryGroupId

(UInt32) Privileges

(String) Profile

(String) ScriptPath

(String) SettingID

(UInt32) UnitsPerWeek

(String) UserComment

(UInt32) UserId

(String) UserType

<!-- p.2487 -->

     (String) Workstations

NT Eventlog File
Namespace: root\cimv2

class Win32_NTEventlogFile

     (String) Name

     (UInt32) AccessMask

     (Boolean) Archive

     (String) Caption

     (Boolean) Compressed

     (String) CompressionMethod

     (DateTime) CreationDate

     (String) Description

     (String) Drive

     (String) EightDotThreeFileName

     (Boolean) Encrypted

     (String) EncryptionMethod

     (String) Extension

     (String) FileName

     (UInt64) FileSize

     (String) FileType

     (String) FSName

     (Boolean) Hidden

     (DateTime) InstallDate

     (UInt64) InUseCount

<!-- p.2488 -->

     (DateTime) LastAccessed

     (DateTime) LastModified

     (String) LogfileName

     (String) Manufacturer

     (UInt32) MaxFileSize

     (UInt32) NumberOfRecords

     (UInt32) OverwriteOutDated

     (String) OverWritePolicy

     (String) Path

     (Boolean) Readable

     (String) Sources[]

     (String) Status

     (Boolean) System

     (String) Version

     (Boolean) Writeable

Office365ProPlusConfigurations
Namespace: root\cimv2

class Office365ProPlusConfigurations

     (String) KeyName

     (String) AutoUpgrade

     (String) CCMManaged

     (String) CDNBaseUrl

     (String) cfgUpdateChannel

     (String) ClientCulture

<!-- p.2489 -->

    (String) ClientFolder

    (String) GPOChannel

    (String) GPOOfficeMgmtCOM

    (String) InstallationPath

    (String) LastScenario

    (String) LastScenarioResult

    (String) OfficeMgmtCOM

    (String) Platform

    (String) SharedComputerLicensing

    (String) UpdateChannel

    (String) UpdatePath

    (String) UpdatesEnabled

    (String) UpdateUrl

    (String) VersionToReport

Office Addin
Namespace: root\ccm\InvAgt

class CCM_OfficeAddin

    (String) Architecture

    (String) ID

    (String) OfficeApp

    (String) Type

    (UInt32) AverageLoadTimeInMilliseconds

    (String) CLSID

    (String) CompanyName

<!-- p.2490 -->

     (UInt32) CrashCount

     (String) Description

     (UInt32) ErrorCount

     (String) FileName

     (UInt64) FileSize

     (UInt32) FileTimestamp

     (String) FileVersion

     (String) FriendlyName

     (String) FriendlyNameHash

     (String) IdHash

     (UInt32) LoadBehavior

     (UInt32) LoadCount

     (UInt32) LoadFailCount

     (String) ProductName

     (String) ProductVersion

Office Client Metric
Namespace: root\ccm\InvAgt

class CCM_OfficeClientMetric

     (String) OfficeApp

     (UInt32) CompatibilityErrorCount

     (UInt32) CrashedSessionCount

     (UInt32) MacroCompileErrorCount

     (UInt32) MacroRuntimeErrorCount

     (UInt32) SessionCount

<!-- p.2491 -->

Office Device Summary
Namespace: root\ccm\InvAgt

class CCM_OfficeDeviceSummary

    (Boolean) IsProPlusInstalled

    (Boolean) IsTelemetryEnabled

Office Document Metric
Namespace: root\ccm\InvAgt

class CCM_OfficeDocumentMetric

    (String) OfficeApp

    (UInt32) TotalCloudDocs

    (UInt32) TotalLegacyDocs

    (UInt32) TotalLocalDocs

    (UInt32) TotalMacroDocs

    (UInt32) TotalNonMacroDocs

    (UInt32) TotalUncDocs

Office Document Solution
Namespace: root\ccm\InvAgt

class CCM_OfficeDocumentSolution

    (String) DocumentSolutionId

    (String) OfficeApp

    (UInt32) CompatibilityErrorCount

    (UInt32) CrashCount

    (String) ExampleFileName

<!-- p.2492 -->

     (UInt32) LoadCount

     (UInt32) LoadFailCount

     (UInt32) MacroCompileErrorCount

     (UInt32) MacroRuntimeErrorCount

     (String) Type

Office Macro Error
Namespace: root\ccm\InvAgt

class CCM_OfficeMacroError

     (String) DocumentSolutionId

     (UInt32) ErrorCode

     (UInt32) Count

     (UInt64) LastOccurrence

     (String) Type

Office Product Info
Namespace: root\ccm\InvAgt

class CCM_OfficeProductInfo

     (String) ProductName

     (String) ProductVersion

     (String) Architecture

     (String) Channel

     (UInt32) IsProPlusInstalled

     (String) Language

     (String) LicenseState

<!-- p.2493 -->

Office Vba Rule Violation
Namespace: root\ccm\InvAgt

class CCM_OfficeVbaRuleViolation

     (UInt32) RuleId

     (UInt32) FileCount

     (String) OfficeApp

Office VbaSummary
Namespace: root\ccm\InvAgt

class CCM_OfficeVbaScanResultsSummary

     (UInt32) Design

     (UInt32) Design64

     (UInt32) DuplicateVba

     (Boolean) HasResults

     (UInt32) HasVba

     (UInt32) Inaccessible

     (UInt32) Issues

     (UInt32) Issues64

     (UInt32) IssuesNone

     (UInt32) IssuesNone64

     (UInt32) Locked

     (UInt32) NoVba

     (UInt32) Protected

     (UInt32) RemLimited

     (UInt32) RemLimited64

<!-- p.2494 -->

    (UInt32) RemSignificant

    (UInt32) RemSignificant64

    (UInt32) Score

    (UInt32) Score64

    (UInt32) Total

    (UInt32) Validation

    (UInt32) Validation64

Operating System
Namespace: root\cimv2

class Win32_OperatingSystem

    (String) Name

    (String) BootDevice

    (String) BuildNumber

    (String) BuildType

    (String) Caption

    (String) CodeSet

    (String) CountryCode

    (String) CSDVersion

    (SInt16) CurrentTimeZone

    (Boolean) Debug

    (String) Description

    (Boolean) Distributed

    (UInt8) ForegroundApplicationBoost

    (UInt64) FreePhysicalMemory

<!-- p.2495 -->

(UInt64) FreeSpaceInPagingFiles

(UInt64) FreeVirtualMemory

(DateTime) InstallDate

(DateTime) LastBootUpTime

(DateTime) LocalDateTime

(String) Locale

(String) Manufacturer

(UInt32) MaxNumberOfProcesses

(UInt64) MaxProcessMemorySize

(String) MUILanguages[]

(UInt32) NumberOfLicensedUsers

(UInt32) NumberOfProcesses

(UInt32) NumberOfUsers

(UInt32) OperatingSystemSKU

(String) Organization

(String) OSArchitecture

(UInt32) OSLanguage

(UInt32) OSProductSuite

(UInt16) OSType

(String) OtherTypeDescription

(String) PlusProductID

(String) PlusVersionNumber

(Boolean) Primary

(UInt32) ProductType

(String) RegisteredUser

<!-- p.2496 -->

    (String) SerialNumber

    (UInt16) ServicePackMajorVersion

    (UInt16) ServicePackMinorVersion

    (UInt64) SizeStoredInPagingFiles

    (String) Status

    (String) SystemDevice

    (String) SystemDirectory

    (UInt64) TotalSwapSpaceSize

    (UInt64) TotalVirtualMemorySize

    (UInt64) TotalVisibleMemorySize

    (String) Version

    (String) WindowsDirectory

Operating System Ex
Namespace: root\cimv2

class CCM_OperatingSystemExtended

    (String) Name

    (UInt32) SKU

Operating System Recovery Configuration
Namespace: root\cimv2

class Win32_OSRecoveryConfiguration

    (String) Name

    (Boolean) AutoReboot

    (String) Caption

    (String) DebugFilePath

<!-- p.2497 -->

     (String) Description

     (Boolean) KernelDumpOnly

     (Boolean) OverwriteExistingDebugFile

     (Boolean) SendAdminAlert

     (String) SettingID

     (Boolean) WriteDebugInfo

     (Boolean) WriteToSystemLog

Optional Feature
Namespace: root\cimv2

class Win32_OptionalFeature

     (String) Name

     (String) Caption

     (String) Description

     (DateTime) InstallDate

     (UInt32) InstallState

     (String) Status

Page File Setting
Namespace: root\cimv2

class Win32_PageFileSetting

     (String) Name

     (String) Caption

     (String) Description

     (UInt32) InitialSize

     (UInt32) MaximumSize

<!-- p.2498 -->

     (String) SettingID

Parallel Port
Namespace: root\cimv2

class Win32_ParallelPort

     (String) DeviceID

     (UInt16) Availability

     (UInt16) Capabilities[]

     (String) CapabilityDescriptions[]

     (String) Caption

     (UInt32) ConfigManagerErrorCode

     (Boolean) ConfigManagerUserConfig

     (String) Description

     (Boolean) DMASupport

     (Boolean) ErrorCleared

     (String) ErrorDescription

     (DateTime) InstallDate

     (UInt32) LastErrorCode

     (UInt32) MaxNumberControlled

     (String) Name

     (Boolean) OSAutoDiscovered

     (String) PNPDeviceID

     (UInt16) PowerManagementCapabilities[]

     (Boolean) PowerManagementSupported

     (UInt16) ProtocolSupported

<!-- p.2499 -->

    (String) Status

    (UInt16) StatusInfo

    (String) SystemName

    (DateTime) TimeOfLastReset

BIOS
Namespace: root\cimv2

class Win32_BIOS

    (String) Name

    (String) SoftwareElementID

    (UInt16) SoftwareElementState

    (UInt16) TargetOperatingSystem

    (String) Version

    (UInt16) BiosCharacteristics[]

    (String) BIOSVersion[]

    (String) BuildNumber

    (String) Caption

    (String) CodeSet

    (String) CurrentLanguage

    (String) Description

    (String) IdentificationCode

    (UInt16) InstallableLanguages

    (DateTime) InstallDate

    (String) LanguageEdition

    (String) ListOfLanguages[]

<!-- p.2500 -->

    (String) Manufacturer

    (String) OtherTargetOS

    (Boolean) PrimaryBIOS

    (DateTime) ReleaseDate

    (String) SerialNumber

    (String) SMBIOSBIOSVersion

    (UInt16) SMBIOSMajorVersion

    (UInt16) SMBIOSMinorVersion

    (Boolean) SMBIOSPresent

    (String) Status

PCMCIA Controller
Namespace: root\cimv2

class Win32_PCMCIAController

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

<!-- p.2501 -->

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

Physical Memory
Namespace: root\cimv2

class Win32_PhysicalMemory

    (String) CreationClassName

    (String) Tag

    (String) BankLabel

    (UInt64) Capacity

    (String) Caption

    (UInt16) DataWidth

    (String) Description

    (String) DeviceLocator

    (UInt16) FormFactor

    (Boolean) HotSwappable

    (DateTime) InstallDate

<!-- p.2502 -->

     (UInt16) InterleaveDataDepth

     (UInt32) InterleavePosition

     (String) Manufacturer

     (UInt16) MemoryType

     (String) Model

     (String) Name

     (String) OtherIdentifyingInfo

     (String) PartNumber

     (UInt32) PositionInRow

     (Boolean) PoweredOn

     (Boolean) Removable

     (Boolean) Replaceable

     (String) SerialNumber

     (String) SKU

     (UInt32) Speed

     (String) Status

     (UInt16) TotalWidth

     (UInt16) TypeDetail

     (String) Version

PhysicalDisk
Namespace: root\microsoft\windows\storage

class MSFT_PhysicalDisk

     (String) ObjectId

     (UInt64) AllocatedSize

<!-- p.2503 -->

(UInt16) BusType

(UInt16) CannotPoolReason[]

(Boolean) CanPool

(String) Description

(String) DeviceId

(UInt16) EnclosureNumber

(String) FirmwareVersion

(String) FriendlyName

(UInt16) HealthStatus

(Boolean) IsIndicationEnabled

(Boolean) IsPartial

(UInt64) LogicalSectorSize

(String) Manufacturer

(UInt16) MediaType

(String) Model

(UInt16) OperationalStatus[]

(String) OtherCannotPoolReasonDescription

(String) PartNumber

(String) PhysicalLocation

(UInt64) PhysicalSectorSize

(String) SerialNumber

(UInt64) Size

(UInt16) SlotNumber

(String) SoftwareVersion

(UInt32) SpindleSpeed

<!-- p.2504 -->

     (UInt16) SupportedUsages[]

     (String) UniqueId

     (UInt16) Usage

PNP DEVICE DRIVER
Namespace: root\cimv2

class Win32_PnpEntity

     (String) DeviceID

     (UInt16) Availability

     (String) Caption

     (String) ClassGuid

     (UInt32) ConfigManagerErrorCode

     (Boolean) ConfigManagerUserConfig

     (String) CreationClassName

     (String) Description

     (Boolean) ErrorCleared

     (String) ErrorDescription

     (DateTime) InstallDate

     (UInt32) LastErrorCode

     (String) Manufacturer

     (String) Name

     (String) PNPDeviceID

     (UInt16) PowerManagementCapabilities[]

     (Boolean) PowerManagementSupported

     (String) Service

<!-- p.2505 -->

     (String) Status

     (UInt16) StatusInfo

     (String) SystemCreationClassName

     (String) SystemName

Pointing Device
Namespace: root\cimv2

class Win32_PointingDevice

     (String) DeviceID

     (UInt16) Availability

     (String) Caption

     (UInt32) ConfigManagerErrorCode

     (Boolean) ConfigManagerUserConfig

     (String) Description

     (UInt16) DeviceInterface

     (UInt32) DoubleSpeedThreshold

     (Boolean) ErrorCleared

     (String) ErrorDescription

     (UInt16) Handedness

     (String) HardwareType

     (String) InfFileName

     (String) InfSection

     (DateTime) InstallDate

     (Boolean) IsLocked

     (UInt32) LastErrorCode

<!-- p.2506 -->

     (String) Manufacturer

     (String) Name

     (UInt8) NumberOfButtons

     (String) PNPDeviceID

     (UInt16) PointingType

     (UInt16) PowerManagementCapabilities[]

     (Boolean) PowerManagementSupported

     (UInt32) QuadSpeedThreshold

     (UInt32) Resolution

     (UInt32) SampleRate

     (String) Status

     (UInt16) StatusInfo

     (UInt32) Synch

     (String) SystemName

Portable Battery
Namespace: root\cimv2

class Win32_PortableBattery

     (String) DeviceID

     (UInt16) Availability

     (UInt16) BatteryStatus

     (UInt16) CapacityMultiplier

     (String) Caption

     (UInt16) Chemistry

     (UInt32) ConfigManagerErrorCode

<!-- p.2507 -->

(Boolean) ConfigManagerUserConfig

(String) Description

(UInt32) DesignCapacity

(UInt64) DesignVoltage

(Boolean) ErrorCleared

(String) ErrorDescription

(UInt16) EstimatedChargeRemaining

(UInt32) EstimatedRunTime

(UInt32) ExpectedLife

(UInt32) FullChargeCapacity

(DateTime) InstallDate

(UInt32) LastErrorCode

(String) Location

(String) ManufactureDate

(String) Manufacturer

(UInt16) MaxBatteryError

(UInt32) MaxRechargeTime

(String) Name

(String) PNPDeviceID

(UInt16) PowerManagementCapabilities[]

(Boolean) PowerManagementSupported

(String) SmartBatteryVersion

(String) Status

(UInt16) StatusInfo

(String) SystemName

<!-- p.2508 -->

     (UInt32) TimeOnBattery

     (UInt32) TimeToFullCharge

Ports
Namespace: root\cimv2

class Win32_PortResource

     (UInt64) StartingAddress

     (Boolean) Alias

     (String) Caption

     (String) Description

     (UInt64) EndingAddress

     (DateTime) InstallDate

     (String) Name

     (String) Status

Power Capabilities
Namespace: root\CCM\powermanagementagent

class CCM_PwrMgmtSystemPowerCapabilities

     (UInt32) PreferredPMProfile

     (Boolean) ApmPresent

     (Boolean) BatteriesAreShortTerm

     (Boolean) FullWake

     (Boolean) LidPresent

     (String) MinDeviceWakeState

     (Boolean) ProcessorThrottle

     (String) RtcWake

<!-- p.2509 -->

    (Boolean) SystemBatteriesPresent

    (Boolean) SystemS1

    (Boolean) SystemS2

    (Boolean) SystemS3

    (Boolean) SystemS4

    (Boolean) SystemS5

    (Boolean) UpsPresent

    (Boolean) VideoDimPresent

Power Configurations
Namespace: root\CCM\policy\machine\actualconfig

class CCM_PowerConfig

    (String) PowerConfigID

    (UInt32) DurationInSec

    (String) NonPeakPowerPlan

    (String) NonPeakPowerPlanName

    (String) PeakPowerPlan

    (String) PeakPowerPlanName

    (String) PeakStartTimeHoursMin

    (String) WakeUpTimeHoursMin

Power Management Insomnia Reasons
Namespace: root\CCM\powermanagementagent

class CCM_PwrMgmtLastSuspendError

    (String) Requester

    (String) RequesterType

<!-- p.2510 -->

    (String) RequestType

    (DateTime) Time

    (UInt32) AdditionalCode

    (String) AdditionalInfo

    (String) RequesterInfo

    (Boolean) UnknownRequester

Power Management Daily
Namespace: root\CCM\powermanagementagent

class CCM_PwrMgmtActualDay

    (DateTime) Date

    (String) TypeOfEvent

    (UInt32) hr0_1

    (UInt32) hr1_2

    (UInt32) hr10_11

    (UInt32) hr11_12

    (UInt32) hr12_13

    (UInt32) hr13_14

    (UInt32) hr14_15

    (UInt32) hr15_16

    (UInt32) hr16_17

    (UInt32) hr17_18

    (UInt32) hr18_19

    (UInt32) hr19_20

    (UInt32) hr2_3

<!-- p.2511 -->

    (UInt32) hr20_21

    (UInt32) hr21_22

    (UInt32) hr22_23

    (UInt32) hr23_0

    (UInt32) hr3_4

    (UInt32) hr4_5

    (UInt32) hr5_6

    (UInt32) hr6_7

    (UInt32) hr7_8

    (UInt32) hr8_9

    (UInt32) hr9_10

    (UInt32) minutesTotal

Power Client Opt Out Settings
Namespace: root\ccm\ClientSDK

class CCM_PowerManagementClientOptoutSetting

    (Boolean) AdminAllowOptout

    (Boolean) EffectiveClientOptOut

    (Boolean) IsClientOptOut

Power Management Monthly
Namespace: root\CCM\powermanagementagent

class CCM_PwrMgmtMonth

    (DateTime) MonthStart

    (UInt32) minutesComputerActive

    (UInt32) minutesComputerOn

<!-- p.2512 -->

     (UInt32) minutesComputerShutdown

     (UInt32) minutesComputerSleep

     (UInt32) minutesMonitorOn

     (UInt32) minutesTotal

     (String) TypeOfEvent

Power Settings
Namespace: root\cimv2\sms

class SMS_PowerSettings

     (String) GUID

     (String) ACSettingIndex

     (String) ACValue

     (String) DCSettingIndex

     (String) DCValue

     (String) Name

     (String) UnitSpecifier

Print Jobs
Namespace: root\cimv2

class Win32_PrintJob

     (String) Name

     (String) Caption

     (String) DataType

     (String) Description

     (String) Document

     (String) DriverName

<!-- p.2513 -->

     (DateTime) ElapsedTime

     (String) HostPrintQueue

     (DateTime) InstallDate

     (UInt32) JobId

     (String) JobStatus

     (String) Notify

     (String) Owner

     (UInt32) PagesPrinted

     (String) Parameters

     (String) PrintProcessor

     (UInt32) Priority

     (UInt32) Size

     (DateTime) StartTime

     (String) Status

     (UInt32) StatusMask

     (DateTime) TimeSubmitted

     (UInt32) TotalPages

     (DateTime) UntilTime

Printer Configuration
Namespace: root\cimv2

class Win32_PrinterConfiguration

     (String) Name

     (UInt32) BitsPerPel

     (String) Caption

<!-- p.2514 -->

(Boolean) Collate

(UInt32) Color

(UInt32) Copies

(String) Description

(String) DeviceName

(UInt32) DisplayFlags

(UInt32) DisplayFrequency

(UInt32) DitherType

(UInt32) DriverVersion

(Boolean) Duplex

(String) FormName

(UInt32) HorizontalResolution

(UInt32) ICMIntent

(UInt32) ICMMethod

(UInt32) LogPixels

(UInt32) MediaType

(UInt32) Orientation

(UInt32) PaperLength

(String) PaperSize

(UInt32) PaperWidth

(UInt32) PelsHeight

(UInt32) PelsWidth

(UInt32) PrintQuality

(UInt32) Scale

(String) SettingID

<!-- p.2515 -->

     (UInt32) SpecificationVersion

     (UInt32) TTOption

     (UInt32) VerticalResolution

     (UInt32) XResolution

     (UInt32) YResolution

Printer Device
Namespace: root\cimv2

class Win32_Printer

     (String) DeviceID

     (UInt32) Attributes

     (UInt16) Availability

     (UInt32) AveragePagesPerMinute

     (UInt16) Capabilities[]

     (String) CapabilityDescriptions[]

     (String) Caption

     (UInt32) ConfigManagerErrorCode

     (Boolean) ConfigManagerUserConfig

     (UInt32) DefaultPriority

     (String) Description

     (UInt16) DetectedErrorState

     (String) DriverName

     (Boolean) ErrorCleared

     (String) ErrorDescription

     (UInt32) HorizontalResolution

<!-- p.2516 -->

(DateTime) InstallDate

(UInt32) JobCountSinceLastReset

(UInt16) LanguagesSupported[]

(UInt32) LastErrorCode

(String) Location

(String) Name

(UInt16) PaperSizesSupported[]

(String) PNPDeviceID

(String) PortName

(UInt16) PowerManagementCapabilities[]

(Boolean) PowerManagementSupported

(String) PrinterPaperNames[]

(UInt32) PrinterState

(UInt16) PrinterStatus

(String) PrintJobDataType

(String) PrintProcessor

(String) SeparatorFile

(String) ServerName

(String) ShareName

(Boolean) SpoolEnabled

(DateTime) StartTime

(String) Status

(UInt16) StatusInfo

(String) SystemName

(DateTime) TimeOfLastReset

<!-- p.2517 -->

     (DateTime) UntilTime

     (UInt32) VerticalResolution

Process
Namespace: root\cimv2

class Win32_Process

     (String) Handle

     (String) Caption

     (DateTime) CreationDate

     (String) Description

     (String) ExecutablePath

     (UInt16) ExecutionState

     (UInt32) HandleCount

     (DateTime) InstallDate

     (UInt64) KernelModeTime

     (UInt32) MaximumWorkingSetSize

     (UInt32) MinimumWorkingSetSize

     (String) Name

     (String) OSName

     (UInt64) OtherOperationCount

     (UInt64) OtherTransferCount

     (UInt32) PageFaults

     (UInt32) PageFileUsage

     (UInt32) ParentProcessId

     (UInt32) PeakPageFileUsage

<!-- p.2518 -->

     (UInt64) PeakVirtualSize

     (UInt32) PeakWorkingSetSize

     (UInt32) Priority

     (UInt64) PrivatePageCount

     (UInt32) ProcessId

     (UInt32) QuotaNonPagedPoolUsage

     (UInt32) QuotaPagedPoolUsage

     (UInt32) QuotaPeakNonPagedPoolUsage

     (UInt32) QuotaPeakPagedPoolUsage

     (UInt64) ReadOperationCount

     (UInt64) ReadTransferCount

     (UInt32) SessionId

     (String) Status

     (DateTime) TerminationDate

     (UInt32) ThreadCount

     (UInt64) UserModeTime

     (UInt64) VirtualSize

     (String) WindowsVersion

     (UInt64) WorkingSetSize

     (UInt64) WriteOperationCount

     (UInt64) WriteTransferCount

Processor
Namespace: root\cimv2\sms

class SMS_Processor

<!-- p.2519 -->

(String) DeviceID

(UInt16) AddressWidth

(UInt16) Architecture

(UInt16) Availability

(UInt16) BrandID

(String) Caption

(UInt32) ConfigManagerErrorCode

(Boolean) ConfigManagerUserConfig

(String) CPUHash

(String) CPUKey

(UInt16) CpuStatus

(UInt32) CurrentClockSpeed

(UInt16) CurrentVoltage

(UInt16) DataWidth

(String) Description

(Boolean) ErrorCleared

(String) ErrorDescription

(UInt32) ExtClock

(UInt16) Family

(DateTime) InstallDate

(Boolean) Is64Bit

(Boolean) IsHyperthreadCapable

(Boolean) IsHyperthreadEnabled

(Boolean) IsMobile

(Boolean) IsTrustedExecutionCapable

<!-- p.2520 -->

(Boolean) IsVitualizationCapable

(UInt32) L2CacheSize

(UInt32) L2CacheSpeed

(UInt32) L3CacheSize

(UInt32) L3CacheSpeed

(UInt32) LastErrorCode

(UInt16) Level

(UInt16) LoadPercentage

(String) Manufacturer

(UInt32) MaxClockSpeed

(String) Name

(UInt32) NormSpeed

(UInt32) NumberOfCores

(UInt32) NumberOfLogicalProcessors

(String) OtherFamilyDescription

(Boolean) PartOfDomain

(UInt32) PCache

(String) PNPDeviceID

(UInt16) PowerManagementCapabilities[]

(Boolean) PowerManagementSupported

(String) ProcessorId

(UInt16) ProcessorType

(UInt16) Revision

(String) Role

(String) SocketDesignation
