---
title: "RemoveBoundary method in class SMS_BoundaryGroup"
type: reference
domain: sccm
slug: develop-removeboundary-method-in-class-sms-boundarygroup
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/removeboundary-method-in-class-sms_boundarygroup
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the RemoveBoundary WMI class method removes boundaries from a boundary group."
---

# RemoveBoundary method in class SMS_BoundaryGroup

# RemoveBoundary Method in Class SMS_BoundaryGroup
The `RemoveBoundary` Windows Management Instrumentation (WMI) class method, in Configuration Manager, removes boundaries from this boundary group.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 RemoveBoundary(
   UInt32 BoundaryID[]
);
```

#### Parameters
 `BoundaryID`
 Data type: `UInt32` Array

 Qualifiers: [in]

 Unique identifier of the boundary.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_BoundaryGroup Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_boundarygroup-server-wmi-class.md)
