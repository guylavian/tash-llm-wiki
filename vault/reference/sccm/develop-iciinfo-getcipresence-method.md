---
title: "ICIINFO::GetCIPresence"
type: reference
domain: sccm
slug: develop-iciinfo-getcipresence-method
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/iciinfo--getcipresence-method
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the ICIINFO::GetCIPresence method gets the current presence for the configuration item, including the compliance state for the configuration item."
---

# ICIINFO::GetCIPresence

# ICIINFO::GetCIPresence Method
The `ICIINFO::GetCIPresence` method, in Configuration Manager, gets the current presence for the configuration item. The presence data includes the compliance state for the configuration item.

## Syntax

```
[IDL]
HRESULT GetCIPresence(
     CIPresence* pCIPresence
);
```

#### Parameters
 `pCIPresence`
 Data type: `CIPresence`

 Qualifiers: [out]

 Pointer to a [CIPresence Enumeration](../../../../../develop/reference/core/clients/client-classes/cipresence-enumeration.md) value indicating the current presence for the configuration item.

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
 [CIPresence Enumeration](../../../../../develop/reference/core/clients/client-classes/cipresence-enumeration.md)
