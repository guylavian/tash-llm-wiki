---
title: "Cancel Method"
type: reference
domain: sccm
slug: develop-cancel-method-in-class-ccm-application
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/sdk/cancel-method-in-class-ccm_application
family: develop
documentKind: "reference"
abstract: "Learn how to cancel an application deployment using the Cancel class method in Configuration Manager."
---

# Cancel Method

# Cancel Method in Class CCM_Application
The `Cancel` Windows Management Instrumentation (WMI) class method in Configuration Manager that cancels an application deployment.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
uint32 Cancel
{
    [IN]    String Id
    [IN]    String Revision
    [IN]    Boolean IsMachineTarget
};
```

## Parameters
 `Id`
 Data type: `String`

 Qualifiers: [id("0"), in]

 Application identifier.

 `Revision`
 Data type: `String`

 Qualifiers: [id("1"), in]

 Revision.

 `IsMachineTarget`
 Data type: `Boolean`

 Qualifiers: [id("2"), in]

 `true` if the application targets a device.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
