---
title: "SMS_DriverModel Class"
type: reference
domain: sccm
slug: develop-sms-drivermodel-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/osd/sms_drivermodel-server-wmi-class
family: develop
documentKind: "reference"
abstract: "Learn how to represent driver model information for the specified driver in Configuration Manager using SMS_DriverModel class."
---

# SMS_DriverModel Class

# SMS_DriverModel Server WMI Class
The `SMS_DriverModel` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents driver model information for the specified driver.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_DriverModel : SMS_BaseClass
{
    UInt32 CI_ID;
    String CI_UniqueID;
    String ModelManufacture;
    String ModelName;
};
```

## Methods
 The `SMS_DriverModel` class does not define any methods.

## Properties
 `CI_ID`
 Data type: `UInt32`

 Access type: Read-only

 Qualifiers: [key, not_null, read]

 Driver configuration item local unique ID.

 `CI_UniqueID`
 Data type: `String`

 Access type: Read-only

 Qualifiers: [not_null, read]

 Driver configuration item global unique ID.

 `ModelManufacture`
 Data type: `String`

 Access type: Read-only

 Qualifiers: [key, not_null, read]

 Driver configuration item Model manufacturer.

 `ModelName`
 Data type: `String`

 Access type: Read-only

 Qualifiers: [key, not_null, read]

 Driver configuration item Model name.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).
