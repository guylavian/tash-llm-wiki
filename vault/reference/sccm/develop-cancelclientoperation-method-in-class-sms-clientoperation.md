---
title: "CancelClientOperation Method"
type: reference
domain: sccm
slug: develop-cancelclientoperation-method-in-class-sms-clientoperation
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/protect/cancelclientoperation-method-in-class-sms_clientoperation
family: develop
documentKind: "reference"
abstract: "The CancelClientOperation Windows Management Instrumentation (WMI) class method cancels a client operation."
---

# CancelClientOperation Method

# CancelClientOperation Method in Class SMS_ClientOperation
The `CancelClientOperation` Windows Management Instrumentation (WMI) class method, in Configuration Manager, that cancels a client operation.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
uint32 CancelClientOperation
{
    [IN]    UInt32 OperationID
};
```

## Parameters
 `OperationID`
 Data type: `UInt32`

 Qualifiers: [id("0"), in]

 OperationID.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).
