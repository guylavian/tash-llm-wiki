---
title: "AddDistributionPoints Method in SMS_TaskSequencePackage"
type: reference
domain: sccm
slug: develop-adddistributionpoints-method-in-class-sms-tasksequencepackage
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/osd/adddistributionpoints-method-in-class-sms_tasksequencepackage
family: develop
documentKind: "reference"
abstract: "Learn how the AddDistributionPoints Method adds the distribution points for the task sequence package."
---

# AddDistributionPoints Method in SMS_TaskSequencePackage

# AddDistributionPoints Method in Class SMS_TaskSequencePackage
The `AddDistributionPoints` Windows Management Instrumentation (WMI) class method, in Configuration Manager, adds the distribution points for the task sequence package.

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

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_TaskSequencePackage Server WMI Class](../../../develop/reference/osd/sms_tasksequencepackage-server-wmi-class.md)
