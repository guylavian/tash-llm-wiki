---
title: "SMS_WinPEOptionalComponentInBootImage Class"
type: reference
domain: sccm
slug: develop-sms-winpeoptionalcomponentinbootimage-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/osd/sms_winpeoptionalcomponentinbootimage-server-wmi-class
family: develop
documentKind: "reference"
abstract: "This is an SMS Provider server class in Configuration Manager. It represents the association between a boot image package and a WinPE optional component."
---

# SMS_WinPEOptionalComponentInBootImage Class

# SMS_WinPEOptionalComponentInBootImage Server WMI Class
The `SMS_WinPEOptionalComponentInBootImage` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents the association between a boot image package and a WinPE optional component.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_WinPEOptionalComponentInBootImage : SMS_BaseClass
{
    String Architecture;
    UInt32 ComponentID;
    String DependentComponentNames[];
    UInt32 DependentIds[];
    Boolean IsRequired;
    String Name;
    String PackageID;
    UInt64 Size;
};
```

## Methods
 The `SMS_WinPEOptionalComponentInBootImage` class does not define any methods.

## Properties
 `Architecture`
 Data type: `String`

 Access type: Read

 Qualifiers: [key]

 The architecture of WinPE optional component associated with the SMS_WinPEOptionalComponentInfo object.

 `ComponentID`
 Data type: `UInt32`

 Access type: Read

 Qualifiers: [key]

 The unique identifier of the WinPE optional component associated with the SMS_WinPEOptionalComponentInfo object.

 `DependentComponentNames`
 Data type: `String` Array

 Access type: Read

 Qualifiers: none

 The name of dependent WinPE optional components associated with the SMS_WinPEOptionalComponentInfo object.

 `DependentIds`
 Data type: `UInt32` Array

 Access type: Read

 Qualifiers: none

 The unique identifier of dependent WinPE optional component associated with the SMS_WinPEOptionalComponentInfo object.

 `IsRequired`
 Data type: `Boolean`

 Access type: Read

 Qualifiers: none

 The required flag of WinPE optional component associated with the SMS_WinPEOptionalComponentInfo object.

 `Name`
 Data type: `String`

 Access type: Read

 Qualifiers: none

 The name of WinPE optional component associated with the SMS_WinPEOptionalComponentInfo object.

 `PackageID`
 Data type: `String`

 Access type: Read

 Qualifiers: [key]

 The unique identifier of the boot image associated with the SMS_BootImagePackage object.

 `Size`
 Data type: `UInt64`

 Access type: Read

 Qualifiers: none

 The size of WinPE optional component associated with the SMS_WinPEOptionalComponentInfo object.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).
