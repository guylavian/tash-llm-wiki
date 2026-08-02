---
title: "ICIINFO::GetSdmTypeName"
type: reference
domain: sccm
slug: develop-iciinfo-getsdmtypename-method
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/iciinfo--getsdmtypename-method
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the ICIINFO::GetSdmTypeName method gets the fully qualified name of a configuration item."
---

# ICIINFO::GetSdmTypeName

# ICIINFO::GetSdmTypeName Method
The `ICIINFO::GetSdmTypeName` method, in Configuration Manager, gets the fully qualified name of a configuration item.

## Syntax

```
[IDL]
HRESULT GetSdmTypeName(
     LPWSTR* ppszTypeName
);
```

#### Parameters
 `ppszTypeName`
 Data type: `LPWSTR`

 Qualifiers: [out]

 Pointer to a string that represents the fully qualified name of the configuration item.

## Return Values
 An `HRESULT` code. Possible values include, but aren't limited to, the following one:

 S_OK
 The method succeeded. All other return values indicate failure.

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Client Runtime Requirements](../../../../../develop/core/reqs/client-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Client Development Requirements](../../../../../develop/core/reqs/client-development-requirements.md).

## See Also
 [ICIINFO Interface](../../../../../develop/reference/core/clients/client-classes/iciinfo-interface.md)
