---
title: "GetStatus Method"
type: reference
domain: sccm
slug: develop-getstatus-method-in-class-sms-aimlsparser
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/asset-intelligence/getstatus-method-in-class-sms_aimlsparser
family: develop
documentKind: "reference"
abstract: "The GetStatus Windows Management Instrumentation (WMI) class method is used to monitor the status of a previous call to the Import method."
---

# GetStatus Method

# GetStatus Method in Class SMS_AIMLSParser
The `GetStatus` Windows Management Instrumentation (WMI) class method, in Configuration Manager, which is used to monitor the status of a previous call to the `Import` method.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 GetStatus(
     SInt32 Status
);
```

#### Parameters
 `Status`
 Data type: `SInt32`

 Qualifiers: [out]

 When 0, indicates a successful call to `Import`.

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
