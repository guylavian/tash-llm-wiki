---
title: "AppDetectState Enumeration"
type: reference
domain: sccm
slug: develop-appdetectstate-enumeration
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/appdetectstate-enumeration
family: develop
documentKind: "reference"
abstract: "Learn how to define application installation states in Configuration Manager using AppDetectState enumeration."
---

# AppDetectState Enumeration

# AppDetectState Enumeration
In Configuration Manager, the `AppDetectState` enumeration defines application installation states. This enumeration is used by the [IAppManagementHandler Interface](../../../../../develop/reference/core/clients/client-classes/iappmanagementhandler-interface.md).

## Syntax

```
typedef enum tagAppDetectState
{
    appDetectNotFound = 0,
    appDetectInstalled,
    appDetectFailed
}AppDetectState;

```

## Elements
 `appDetectNotFound`
 The application was not found.

 `appDetectInstalled`
 The application is installed.

 `appDetectFailed`
 Application detection failed.

## Remarks
 This enumeration is used by the [IAppManagementHandler Interface](../../../../../develop/reference/core/clients/client-classes/iappmanagementhandler-interface.md).

## See Also
 [Application Management Client Interfaces](../../../../../develop/reference/core/clients/client-classes/application-management-client-interfaces.md)
 [Configuration Manager Software Development Kit](../../../../../develop/core/misc/system-center-configuration-manager-sdk.md)
 [Configuration Manager Reference](../../../../../develop/reference/configuration-manager-reference.md)
