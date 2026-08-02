---
title: "UpdateProfileIDForDevices Method"
type: reference
domain: sccm
slug: develop-updateprofileidfordevices-method-in-class-sms-mdmcorpowneddevices
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/mdm/updateprofileidfordevices-method-in-class-sms_mdmcorpowneddevices
family: develop
documentKind: "reference"
abstract: "Update the profile IDs for device serial numbers."
---

# UpdateProfileIDForDevices Method

# UpdateProfileIDForDevices Method in Class SMS_MDMCorpOwnedDevices
The `UpdateProfileIdForDevices` Windows Management Instrumentation (WMI) class method, in Configuration Manager, updates the  profile IDs for device serial numbers.

## Syntax

```
sint32 UpdateProfileIdForDevices(
     String RequestEnrollmentProfileId,
     String DeviceSerialNumbers
);

```

#### Parameters
 `RequestEnrollmentProfileId`
 Data type: `String`

 Qualifiers: [in]

 Enrollment profile ID.

 `DeviceSerialNumbers`
 Data type: `String Array`

 Qualifiers: [in]

 The serial number of the device.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_MDMCorpOwnedDevices Server WMI Class](../../../develop/reference/mdm/sms_mdmcorpowneddevices-server-wmi-class.md)
