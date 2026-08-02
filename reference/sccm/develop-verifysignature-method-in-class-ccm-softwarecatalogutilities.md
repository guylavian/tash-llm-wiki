---
title: "VerifySignature Method"
type: reference
domain: sccm
slug: develop-verifysignature-method-in-class-ccm-softwarecatalogutilities
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/sdk/verifysignature-method-in-class-ccm_softwarecatalogutilities
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the VerifySignature WMI class method verifies the data signature."
---

# VerifySignature Method

# VerifySignature Method in Class CCM_SoftwareCatalogUtilities
The `VerifySignature` Windows Management Instrumentation (WMI) class method in Configuration Manager that verifies the data signature.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
uint32 VerifySignature
{
    [IN]    String Data
    [IN]    String DataSignature
    [IN]    String WebServiceID
    [IN]    Boolean VerifyUserAndTimestamp
    [OUT]   Boolean SignatureVerificationPassed
};
```

## Parameters
 `Data`
 Data type: `String`

 Qualifiers: [id("0"), in]

 Data to verify.

 `DataSignature`
 Data type: `String`

 Qualifiers: [id("1"), in]

 Data signature.

 `WebServiceID`
 Data type: `String`

 Qualifiers: [id("2"), in]

 Web Service identifier.

 `VerifyUserAndTimestamp`
 Data type: `Boolean`

 Qualifiers: [id("3"), in]

 `true` to verify the user and timestamp.

 `SignatureVerificationPassed`
 Data type: `Boolean`

 Qualifiers: [id("4"), out]

 `true` if the data signature is valid.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
