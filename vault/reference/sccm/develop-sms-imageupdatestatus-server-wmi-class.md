---
title: "SMS_ImageUpdateStatus Class"
type: reference
domain: sccm
slug: develop-sms-imageupdatestatus-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/osd/sms_imageupdatestatus-server-wmi-class
family: develop
documentKind: "reference"
abstract: "The SMS_ImageUpdateStatus Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents software update installation status of offline servicing image."
---

# SMS_ImageUpdateStatus Class

# SMS_ImageUpdateStatus Server WMI Class
The `SMS_ImageUpdateStatus` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents software update installation status of offline servicing image.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_ImageUpdateStatus : SMS_BaseClass
{
    DateTime AppliedDateTime;
    SInt32 ImageIndex;
    String ImagePackageID;
    SInt32 UpdateID;
    SInt32 UpdateInstallationStatus;
    SInt32 UpdateStatus;
    String UpdateTitle;
};
```

## Methods
 The `SMS_ImageUpdateStatus` class does not define any methods.

## Properties
 `AppliedDateTime`
 Data type: `DateTime`

 Access type: Read/Write

 Qualifiers: none

 Software update installation date.

 `ImageIndex`
 Data type: `SInt32`

 Access type: Read/Write

 Qualifiers: [key]

 Index for offline servicing image.

 `ImagePackageID`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: [key]

 ID for offline servicing image.

 `UpdateID`
 Data type: `SInt32`

 Access type: Read/Write

 Qualifiers: [key]

 ID for software update in offline servicing image.

 `UpdateInstallationStatus`
 Data type: `SInt32`

 Access type: Read/Write

 Qualifiers: none

 Error code for software update installation.

 `UpdateStatus`
 Data type: `SInt32`

 Access type: Read/Write

 Qualifiers: none

 Applicability state for software update.

| Value | Update status |
| ----- | ------------- |
|0|Unknown|
|1|Not Required|
|2|Installed|
|3|Applicable|
|4|Applicability check not supported|
|5|Installed applicability check not supported|

 `UpdateTitle`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: none

 Display name for software update.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).
