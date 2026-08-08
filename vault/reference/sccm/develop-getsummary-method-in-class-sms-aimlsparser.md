---
title: "GetSummary Method in Class SMS_AIMLSParser"
type: reference
domain: sccm
slug: develop-getsummary-method-in-class-sms-aimlsparser
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/asset-intelligence/getsummary-method-in-class-sms_aimlsparser
family: develop
documentKind: "reference"
abstract: "The GetSummary Windows Management Instrumentation (WMI) class method, in Configuration Manager, retrieves the counts of imported Microsoft and non-Microsoft license count."
---

# GetSummary Method in Class SMS_AIMLSParser

# GetSummary Method in Class SMS_AIMLSParser
The `GetSummary` Windows Management Instrumentation (WMI) class method, in Configuration Manager, retrieves the counts of imported Microsoft License count and non-Microsoft license count.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 GetSummary(
     UInt32 MVLSCount;
     UInt32 NonMSLicenseCount;
);
```

#### Parameters
 `MVLSCount`
 Data type: `UInt32`

 Qualifiers: [out]

 Returns the Microsoft License count.

 `NonMSLicenseCount`
 Data type: `UInt32`

 Qualifiers: [out]

 Returns the non-Microsoft License count.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_AIMLSParser Server WMI Class](../../../../../develop/reference/core/clients/asset-intelligence/sms_aimlsparser-server-wmi-class.md)
