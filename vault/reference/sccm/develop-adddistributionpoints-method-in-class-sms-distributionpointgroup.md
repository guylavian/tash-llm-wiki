---
title: "AddDistributionPoints method in class SMS_DistributionPointGroup"
type: reference
domain: sccm
slug: develop-adddistributionpoints-method-in-class-sms-distributionpointgroup
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/adddistributionpoints-method-in-class-sms_distributionpointgroup
family: develop
documentKind: "reference"
abstract: "AddDistributionPoints Windows Management Instrumentation (WMI) class method adds distribution points to the distribution point group."
---

# AddDistributionPoints method in class SMS_DistributionPointGroup

# AddDistributionPoints Method in Class SMS_DistributionPointGroup
The `AddDistributionPoints` Windows Management Instrumentation (WMI) class method, in Configuration Manager, adds distribution points to the distribution point group.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
sint32 AddDistributionPoints(
     string DPNALPath[],
     boolean AddTargetedPackages
);
```

#### Parameters
 `DPNALPath`
 Data type: `String` Array

 Qualifiers: `[in]`

 Distribution point NAL path.

 `AddTargetedPackages`
 Data type: `Boolean`

 Qualifiers: `[in, optional]`

 `True` if

## Return Values
 An  `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Application Server WMI Class](../../../../../develop/reference/apps/sms_application-server-wmi-class.md)
