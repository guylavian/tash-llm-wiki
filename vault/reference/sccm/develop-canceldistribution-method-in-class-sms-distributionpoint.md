---
title: "CancelDistribution Method"
type: reference
domain: sccm
slug: develop-canceldistribution-method-in-class-sms-distributionpoint
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/canceldistribution-method-in-class-sms_distributionpoint
family: develop
documentKind: "reference"
abstract: "A Windows Management Instrumentation class method that cancels a package distribution."
---

# CancelDistribution Method

# CancelDistribution Method in Class SMS_DistributionPoint
The `CancelDistribution` Windows Management Instrumentation (WMI) class method, in Configuration Manager, cancels a package distribution. If there's a distribution in-progress for the specified package to the specified distribution point, then calling this method cancels the ongoing distribution and the status of the package distribution will be set to fail for this distribution point.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
sint32 CancelDistribution(
     string PackageId,
     string NALPath
);
```

#### Parameters
 `PackageId`
 Data type: `String`

 Qualifiers: `[in]`

 ID for an existing package.

 `NALPath`
 Data type: `String`

 Qualifiers: `[in]`

 Network abstraction layer (NAL) path to the distribution point server.

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
