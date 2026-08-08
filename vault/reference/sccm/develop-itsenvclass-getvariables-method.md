---
title: "ITSEnvClass::GetVariables"
type: reference
domain: sccm
slug: develop-itsenvclass-getvariables-method
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/itsenvclass--getvariables-method
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the GetVariables method gets the variables for the operating system deployment task sequence environment."
---

# ITSEnvClass::GetVariables

# ITSEnvClass::GetVariables Method
In Configuration Manager, the `GetVariables` method gets the variables for the operating system deployment task sequence environment.

## Syntax

```
[IDL]
HRESULT GetVariables(
     VARIANT* variables
);
```

#### Parameters
 `variables`
 Data type: `VARIANT`

 Qualifiers: [out, retval]

 Pointer to the environment variables.

## Return Values
 An `HRESULT` code. Possible values include, but are not limited to, the following value.

 S_OK
 The method succeeded.

## See Also
 [ITSEnvClass Interface](../../../../../develop/reference/core/clients/client-classes/itsenvclass-interface.md)
