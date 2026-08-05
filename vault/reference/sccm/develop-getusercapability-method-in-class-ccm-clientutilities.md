---
title: "GetUserCapability Method"
type: reference
domain: sccm
slug: develop-getusercapability-method-in-class-ccm-clientutilities
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/sdk/getusercapability-method-in-class-ccm_clientutilities
family: develop
documentKind: "reference"
abstract: "The GetUserCapability WMI class method in Configuration Manager."
---

# GetUserCapability Method

# GetUserCapability Method in Class CCM_ClientUtilities

The `GetUserCapability` Windows Management Instrumentation (WMI) class method in Configuration Manager.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
uint32 GetUserCapability
{
    [IN]    UInt32 Feature
    [OUT]   UInt32 Value
};
```

## Parameters
 `Feature`
 Data type: `UInt32`

 Qualifiers: [id("0"), in]

 Feature.

 `Value`
 Data type: `UInt32`

 Qualifiers: [id("1"), out]

 Value.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
