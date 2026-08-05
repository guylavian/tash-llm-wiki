---
title: "RefreshPkgSource Method in SMS_ImagePackage"
type: reference
domain: sccm
slug: develop-refreshpkgsource-method-in-class-sms-imagepackage
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/osd/refreshpkgsource-method-in-class-sms_imagepackage
family: develop
documentKind: "reference"
abstract: "The RefreshPkgSource Windows Management Instrumentation (WMI) class method, in Configuration Manager, refreshes the package source at all distribution points."
---

# RefreshPkgSource Method in SMS_ImagePackage

# RefreshPkgSource Method in Class SMS_ImagePackage
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
 The latest version of the package is copied to all the distribution points of the package. The source version of the package is incremented, and the package content is replicated to child sites.

 Using this method is the only way to force an update of the source files, other than by creating a `RefreshSchedule` value for the package. For information about the `RefreshSchedule` property, see [SMS_PackageBaseclass Server WMI Class](../../../develop/reference/core/servers/configure/sms_packagebaseclass-server-wmi-class.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_ImagePackage Server WMI Class](../../../develop/reference/osd/sms_imagepackage-server-wmi-class.md)
