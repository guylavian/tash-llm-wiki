---
title: "ICIINFO::GetContextInfo"
type: reference
domain: sccm
slug: develop-iciinfo-getcontextinfo-method
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/iciinfo--getcontextinfo-method
family: develop
documentKind: "reference"
abstract: "The ICIINFO::GetContextInfo method, in Configuration Manager, gets the context information by name from the configuration item."
---

# ICIINFO::GetContextInfo

# ICIINFO::GetContextInfo Method
The `ICIINFO::GetContextInfo` method, in Configuration Manager, gets the context information by name from the configuration item.

## Syntax

```
[IDL]
HRESULT GetContextInfo(
     LPCWSTR pszName,
     LPWSTR* ppszContext
);
```

#### Parameters
 `pszName`
 Data type: `LPCWSTR`

 Qualifiers: [in]

 Pointer to a null-terminated string specifying the name of the context information to retrieve.

 `ppszContext`
 Data type: `LPWSTR`

 Qualifiers: [out]

 Pointer to a null-terminated string specifying the retrieved context information.

## Return Values
 An `HRESULT` code. Possible values include, but are not limited to, the following:

 S_OK
 The method succeeded. All other return values indicate failure.

## Remarks
 This method is used in setting information that is retrieved by certain class handlers in the System Definition Model (SDM) agent.

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Client Runtime Requirements](../../../../../develop/core/reqs/client-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Client Development Requirements](../../../../../develop/core/reqs/client-development-requirements.md).

## See Also
 [ICIINFO Interface](../../../../../develop/reference/core/clients/client-classes/iciinfo-interface.md)
