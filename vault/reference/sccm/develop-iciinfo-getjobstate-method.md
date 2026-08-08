---
title: "ICIINFO::GetJobState"
type: reference
domain: sccm
slug: develop-iciinfo-getjobstate-method
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/iciinfo--getjobstate-method
family: develop
documentKind: "reference"
abstract: "Learn how to get the current operational state of the configuration item that is part of a job or task with ICIINFO::GetJobState."
---

# ICIINFO::GetJobState

# ICIINFO::GetJobState Method
The `ICIINFO::GetJobState` method, in Configuration Manager, gets the current operational state of the configuration item that is part of a job or task.

## Syntax

```
[IDL]
HRESULT GetJobState(
    CIJobState* pCIJobState,
     Percentage* ppctComplete,
     HRESULT* phrStatus
);
```

#### Parameters
 `pCIJobState`
 Data type: `CIJobState`

 Qualifiers: [out]

 Pointer to a [CIJobState Enumeration](../../../../../develop/reference/core/clients/client-classes/cijobstate-enumeration.md) value indicating the current operational state of the configuration item. This parameter retrieves ciStatusError if the state is not available.

 `ppctComplete`
 Data type: `Percentage`

 Qualifiers: [out]

 Pointer to a `Percentage` object indicating the percentage of job completion.

 `phrStatus`
 Data type: `HRESULT`

 Qualifiers: [out]

 Pointer to an `HRESULT` code representing the current status. This parameter indicates an error code if `pCIJobState` retrieves a value of ciStatusError.

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
 [CIJobState Enumeration](../../../../../develop/reference/core/clients/client-classes/cijobstate-enumeration.md)
