---
title: "IAppManagementHandler::CheckReconnectData"
type: reference
domain: sccm
slug: develop-iappmanagementhandler-checkreconnectdata-method
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/iappmanagementhandler--checkreconnectdata-method
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the IAppManagementHandler::CheckReconnectData method checks whether the reconnection data is valid."
---

# IAppManagementHandler::CheckReconnectData

# IAppManagementHandler::CheckReconnectData Method
The `IAppManagementHandler::CheckReconnectData` method, in Configuration Manager, checks whether the reconnection data is valid.

## Syntax

```
[IDL]
HRESULT CheckReconnectData(
     IWbemClassObject* pReconnectData,
     BOOL* pfIsValid,
     BOOL* pfEnforcementFinished
);
```

#### Parameters
 `pReconnectData`
 Data type: `IWbemClassObject`

 Qualifiers: [in]

 .

 `pfIsValid`
 Data type: `BOOL`

 Qualifiers: [out]

 .

 `pfEnforcementFinished`
 Data type: `BOOL`

 Qualifiers: [out]

 .

## Return Values
 An `HRESULT` code. Possible values include, but are not limited to, the following:

 S_OK
 The method succeeded. All other return values indicate failure.

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Client Runtime Requirements](../../../../../develop/core/reqs/client-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Client Development Requirements](../../../../../develop/core/reqs/client-development-requirements.md).

## See Also
 [Configuration Manager Software Development Kit](../../../../../develop/core/misc/system-center-configuration-manager-sdk.md)
 [Configuration Manager Reference](../../../../../develop/reference/configuration-manager-reference.md)
