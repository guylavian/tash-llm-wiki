---
title: "ITSEnvClass::Value Property"
type: reference
domain: sccm
slug: develop-itsenvclass-value-property
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/itsenvclass--value-property
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the Value property contains the value of an operating system deployment task sequence environment variable."
---

# ITSEnvClass::Value Property

# ITSEnvClass::Value Property
In Configuration Manager, the `Value` property contains the value of an operating system deployment task sequence environment variable.

## Syntax

```
[IDL]
HRESULT Value([in] BSTR Name, [in] BSTR Value);

HRESULT Value([in] BSTR Name, [out,retval] BSTR* Value);
```

#### Parameters
 `Name`
 Data type: `BSTR`

 Qualifiers: [in]

 The name of the environment variable.

 `Value`
 Data type: `BSTR`

 Qualifiers: [in; out, retval]

 On input, the value to set for the environment variable. On output, this parameter points to the value that is retrieved for the supplied name.

## Return Values
 An `HRESULT` code. Possible values include, but aren't limited to, the following value.

 S_OK
 The method succeeded.

## Remarks
 The `get_Value` function succeeds with S_OK when called with an invalid variable name, but retrieves an empty string for the value. This behavior differs from the more common return of a non-zero exit code to indicate an invalid variable name input.

## See Also
 [ITSEnvClass Interface](../../../../../develop/reference/core/clients/client-classes/itsenvclass-interface.md)
