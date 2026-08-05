---
title: "SMS_ImageServicingScheduledImage Class"
type: reference
domain: sccm
slug: develop-sms-imageservicingscheduledimage-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/osd/sms_imageservicingscheduledimage-server-wmi-class
family: develop
documentKind: "reference"
abstract: "The SMS_ImageServicingScheduledImage WMI class represents all schedules for offline servicing image."
---

# SMS_ImageServicingScheduledImage Class

# SMS_ImageServicingScheduledImage Server WMI Class
The `SMS_ImageServicingScheduledImage` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents all schedules for offline servicing image.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_ImageServicingScheduledImage : SMS_BaseClass
{
    String ImagePackageID;
    SInt32 ScheduleID;
};
```

## Methods
 The `SMS_ImageServicingScheduledImage` class does not define any methods.

## Properties
 `ImagePackageID`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: [key]

 ID for offline servicing image that is installed on client computer.

 `ScheduleID`
 Data type: `SInt32`

 Access type: Read/Write

 Qualifiers: [key]

 ID for offline servicing image installation schedule.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).
