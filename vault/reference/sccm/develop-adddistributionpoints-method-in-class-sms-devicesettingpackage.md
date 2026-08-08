---
title: "AddDistributionPoints method in class SMS_DeviceSettingPackage"
type: reference
domain: sccm
slug: develop-adddistributionpoints-method-in-class-sms-devicesettingpackage
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/mdm/adddistributionpoints-method-in-class-sms_devicesettingpackage
family: develop
documentKind: "reference"
abstract: "Learn how to add the distribution points for the device setting package using the AddDistributionPoints class in Configuration Manager."
---

# AddDistributionPoints method in class SMS_DeviceSettingPackage

# AddDistributionPoints Method in Class SMS_DeviceSettingPackage
The `AddDistributionPoints` Windows Management Instrumentation (WMI) class method, in Configuration Manager, adds the distribution points for the device setting package.

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

## See Also
 [SMS_DeviceSettingPackage Server WMI Class](../../../develop/reference/mdm/sms_devicesettingpackage-server-wmi-class.md)
