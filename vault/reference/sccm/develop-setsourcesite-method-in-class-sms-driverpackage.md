---
title: "SetSourceSite Method in SMS_DriverPackage"
type: reference
domain: sccm
slug: develop-setsourcesite-method-in-class-sms-driverpackage
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/osd/setsourcesite-method-in-class-sms_driverpackage
family: develop
documentKind: "reference"
abstract: "Learn how to set the source site for the driver package."
---

# SetSourceSite Method in SMS_DriverPackage

# SetSourceSite Method in Class SMS_DriverPackage
The `SetSourceSite` Windows Management Instrumentation (WMI) class method, in Configuration Manager, sets the source site for the driver package.

 The following syntax is simplified from Managed Object Format (MOF) code and is intended to show the definition of the method.

## Syntax

```
SInt32 SetSourceSite(
      String SourceSite
);
```

#### Parameters
 `SourceSite`
 Data type: `String`

 Qualifiers: [in]

 The site code of the source site for the driver package.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_DriverPackage Server WMI Class](../../../develop/reference/osd/sms_driverpackage-server-wmi-class.md)
