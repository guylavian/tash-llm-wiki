---
title: "AddDistributionPoints Method in SMS_DriverPackage"
type: reference
domain: sccm
slug: develop-adddistributionpoints-method-in-class-sms-driverpackage
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/osd/adddistributionpoints-method-in-class-sms_driverpackage
family: develop
documentKind: "reference"
abstract: "Learn how to use Configuration Manager AddDistributionPoints Windows Management Instrumentation (WMI) class method to add the distribution points for the driver package."
---

# AddDistributionPoints Method in SMS_DriverPackage

# AddDistributionPoints Method in Class SMS_DriverPackage
The `AddDistributionPoints` Windows Management Instrumentation (WMI) class method, in Configuration Manager, adds the distribution points for the driver package.

> [!NOTE]
>  The `AddDistributionPoints` method allows a list of distribution points to be added to a package.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 AddDistributionPoints(
      String SiteCode[],
      String NALPath[]
);
```

#### Parameters
 `SiteCode`
 Data type: `String` Array

 Qualifiers: [in]

 The code for the site to which to add the distribution points.

 `NALPath`
 Data type: `String` Array

 Qualifiers: [in]

 Network abstraction layer (NAL) path to the distribution points.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).

## Remarks
 It is not necessary to refresh the distribution points when using this method.

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_DriverPackage Server WMI Class](../../../develop/reference/osd/sms_driverpackage-server-wmi-class.md)
