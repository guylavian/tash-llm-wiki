---
title: "AddDistributionPointGroup Method"
type: reference
domain: sccm
slug: develop-adddistributionpointgroup-method-in-class-sms-contentpackage
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/adddistributionpointgroup-method-in-class-sms_contentpackage
family: develop
documentKind: "reference"
abstract: "The AddDistributionPointGroup Windows Management Instrumentation class method, in Configuration Manager, adds the content package to a set of distribution point groups."
---

# AddDistributionPointGroup Method

# AddDistributionPointGroup Method in Class SMS_ContentPackage
The `AddDistributionPointGroup` Windows Management Instrumentation (WMI) class method, in Configuration Manager, adds the content package to a set of distribution point groups.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
sint32 AddDistributionPointGroup (
     string DistributionPointGroup[],
);
```

#### Parameters
 `DistributionPointGroup`
 Data type: `String` Array

 Qualifiers: `[in]`

 Array of distribution point groups.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Application Server WMI Class](../../../../../develop/reference/apps/sms_application-server-wmi-class.md)
