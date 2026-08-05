---
title: "SMS_MDMDeviceEnrollmentManagers Class"
type: reference
domain: sccm
slug: develop-sms-mdmdeviceenrollmentmanagers-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/mdm/sms_mdmdeviceenrollmentmanagers-server-wmi-class
family: develop
documentKind: "reference"
abstract: "The SMS_MDMDeviceEnrollmentManagers WMI class represents On-premises Mobile Device Management (MDM) device enrollment managers."
---

# SMS_MDMDeviceEnrollmentManagers Class

# SMS_MDMDeviceEnrollmentManagers Server WMI Class
The `SMS_MDMDeviceEnrollmentManagers` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents On-premises Mobile Device Management (MDM) device enrollment managers.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_MDMDeviceEnrollmentManagers : SMS_BaseClass
{
    UInt32 ResourceID;
};

```

## Methods
 The following table lists the methods in the `SMS_MDMDeviceEnrollmentManagers` class.

|Method|Description|
|------------|-----------------|
|[InsertMultipleResourceIds Method in Class SMS_MDMDeviceEnrollmentManagers](../../../develop/reference/mdm/insertmultipleresourceids-method-in-class-sms_mdmdeviceenrollmentmanagers.md)|Inserts multiple resource IDs.|
|[RemoveMultipleResourceIds Method in Class SMS_MDMDeviceEnrollmentManagers](../../../develop/reference/mdm/removemultipleresourceids-method-in-class-sms_mdmdeviceenrollmentmanagers.md)|Deletes multiple resource IDs.|

## Properties
 `ResourceID`
 Data type: `UInt32`

 Access type: Read/Write

 Qualifiers: [key]

 Resource ID.

## Remarks
 Class qualifiers for this class include:

- Dynamic

- Secured

  For more information about both the class qualifiers and the property qualifiers included in the Properties section, see [Configuration Manager Class and Property Qualifiers](../../../develop/reference/misc/class-and-property-qualifiers.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).
