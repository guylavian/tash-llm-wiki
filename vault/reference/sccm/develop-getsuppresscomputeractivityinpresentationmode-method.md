---
title: "GetSuppressComputerActivityInPresentationMode Method"
type: reference
domain: sccm
slug: develop-getsuppresscomputeractivityinpresentationmode-method
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/sdk/getsuppresscomputeractivityinpresentationmode-method
family: develop
documentKind: "reference"
abstract: "Article outlining the use of the GetSuppressComputerActivityInPresentationMode in Configuration Manager."
---

# GetSuppressComputerActivityInPresentationMode Method

# GetSuppressComputerActivityInPresentationMode Method in Class CCM_ClientUXSettings
The `GetSuppressComputerActivityInPresentationMode` Windows Management Instrumentation (WMI) class method, in Configuration Manager, that gets the value for `SuppressComputerActivityInPresentationMode`

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
uint32 GetSuppressComputerActivityInPresentationMode
{
    [OUT]   Boolean SuppressComputerActivityInPresentationMode
};
```

## Parameters
 `SuppressComputerActivityInPresentationMode`
 Data type: `Boolean`

 Qualifiers: [id("0"), out]

 `true` to suppress computer activity in presentation mode.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
