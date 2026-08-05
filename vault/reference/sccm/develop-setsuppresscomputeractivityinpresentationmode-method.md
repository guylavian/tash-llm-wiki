---
title: "SetSuppressComputerActivityInPresentationMode Method"
type: reference
domain: sccm
slug: develop-setsuppresscomputeractivityinpresentationmode-method
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/sdk/setsuppresscomputeractivityinpresentationmode-method
family: develop
documentKind: "reference"
abstract: "Learn how to set the value for SuppressComputerActivityInPresentationMode in Configuration Manager using SetSuppressComputerActivityInPresentationMode class."
---

# SetSuppressComputerActivityInPresentationMode Method

# SetSuppressComputerActivityInPresentationMode Method in Class CCM_ClientUXSettings
The `SetSuppressComputerActivityInPresentationMode` Windows Management Instrumentation (WMI) class method, in Configuration Manager, that sets the value for `SuppressComputerActivityInPresentationMode`.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
uint32 SetSuppressComputerActivityInPresentationMode
{
    [IN]    Boolean SuppressComputerActivityInPresentationMode
};
```

## Parameters
 `SuppressComputerActivityInPresentationMode`
 Data type: `Boolean`

 Qualifiers: [id("0"), in]

 `true` to suppress computer activity in presentation mode.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
