---
title: "GetClientVersion Method in"
type: reference
domain: sccm
slug: develop-getclientversion-method-in-class-ccm-softwarecatalogutilities
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/sdk/getclientversion-method-in-class-ccm_softwarecatalogutilities
family: develop
documentKind: "reference"
abstract: "The GetClientVersion Windows Management Instrumentation (WMI) class method returns the client version."
---

# GetClientVersion Method in

# GetClientVersion Method in Class CCM_SoftwareCatalogUtilities
The `GetClientVersion` Windows Management Instrumentation (WMI) class method, in Configuration Manager, that returns the client version.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
uint32 GetClientVersion
{
    [OUT]   String ClientVersion
};
```

## Parameters
 `ClientVersion`
 Data type: `String`

 Qualifiers: [id("0"), out]

 Version number of the installed client software.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
