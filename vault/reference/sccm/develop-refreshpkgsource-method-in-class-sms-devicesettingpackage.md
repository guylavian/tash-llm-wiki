---
title: "RefreshPkgSource method in class SMS_DeviceSettingPackage"
type: reference
domain: sccm
slug: develop-refreshpkgsource-method-in-class-sms-devicesettingpackage
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/mdm/refreshpkgsource-method-in-class-sms_devicesettingpackage
family: develop
documentKind: "reference"
abstract: "The RefreshPkgSource class method refreshes the package source at all distribution points."
---

# RefreshPkgSource method in class SMS_DeviceSettingPackage

# RefreshPkgSource Method in Class SMS_DeviceSettingPackage
The `RefreshPkgSource` Windows Management Instrumentation (WMI) class method, in Configuration Manager, refreshes the package source at all distribution points.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 RefreshPkgSource();
```

#### Parameters
 None.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).

## Remarks
 This method copies the latest version of the package to all the distribution points of the package. The source version of the package is incremented, and the package content is replicated to child sites.

 Using this method is the only way to force an update of the source files, other than by creating a `RefreshSchedule` value for the package. For information about the `RefreshSchedule` property, see [SMS_PackageBaseclass Server WMI Class](../../../develop/reference/core/servers/configure/sms_packagebaseclass-server-wmi-class.md).

## Requirements

## See Also
 [SMS_DeviceSettingPackage Server WMI Class](../../../develop/reference/mdm/sms_devicesettingpackage-server-wmi-class.md)
 [SetSourceSite Method in Class SMS_DeviceSettingPackage](../../../develop/reference/mdm/setsourcesite-method-in-class-sms_devicesettingpackage.md)
 [SMS_PackageBaseclass Server WMI Class](../../../develop/reference/core/servers/configure/sms_packagebaseclass-server-wmi-class.md)
