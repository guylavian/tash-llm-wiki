---
title: "ICIINFO::GetEvalState"
type: reference
domain: sccm
slug: develop-iciinfo-getevalstate-method
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/iciinfo--getevalstate-method
family: develop
documentKind: "reference"
abstract: "The ICIINFO::GetEvalState method, in Configuration Manager, gets the current evaluation state of the configuration item."
---

# ICIINFO::GetEvalState

# ICIINFO::GetEvalState Method
The `ICIINFO::GetEvalState` method, in Configuration Manager, gets the current evaluation state of the configuration item.

## Syntax

```
[IDL]
HRESULT GetEvalState(
     CIEvalState* pCIEvalState
);
```

#### Parameters
 `pCIEvalState`
 Data type: `CIEvalState`

 Qualifiers: [out]

 Pointer to a [CIEvalState Enumeration](../../../../../develop/reference/core/clients/client-classes/cievalstate-enumeration.md) value indicating the evaluation state.

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
 [ICIINFO Interface](../../../../../develop/reference/core/clients/client-classes/iciinfo-interface.md)
 [CIEvalState Enumeration](../../../../../develop/reference/core/clients/client-classes/cievalstate-enumeration.md)
