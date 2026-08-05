---
title: "ICIINFO::GetProperty"
type: reference
domain: sccm
slug: develop-iciinfo-getproperty-method
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/iciinfo--getproperty-method
family: develop
documentKind: "reference"
abstract: "Learn how the ICIINFO::GetProperty method, in Configuration Manager, gets a named property value from the configuration item."
---

# ICIINFO::GetProperty

# ICIINFO::GetProperty Method
The `ICIINFO::GetProperty` method, in Configuration Manager, gets a named property value from the configuration item.

## Syntax

```
[IDL]
HRESULT GetProperty(
     LanguageId* pLanguageId,
     LPCWSTR pszPropName,
     LPWSTR* ppszPropValue
);
```

#### Parameters
 `pLanguageId`
 Data type: `LanguageId`

 Qualifiers: [in, out]

 Pointer to the language ID that is used to obtain the property. If there's no localized name for this ID, the method attempts to obtain the language-independent version of the property. If this doesn't exist, the method returns an error. On successful return from the method, this parameter indicates the language ID for the property retrieved.

 `pszPropName`
 Data type: `LPCWSTR`

 Qualifiers: [in]

 Pointer to a null-terminated string specifying the name of the property.

 `ppszPropValue`
 Data type: `LPWSTR`

 Qualifiers: [out]

 Pointer to a null-terminated string specifying the property value.

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
