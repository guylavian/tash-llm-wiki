---
title: "DeleteForUser Method"
type: reference
domain: sccm
slug: develop-deleteforuser-method-in-class-sms-clientpfxcertificate
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/deploy/deleteforuser-method-in-class-sms_clientpfxcertificate
family: develop
documentKind: "reference"
abstract: "Article outlining how to delete a certificate for a user with DeleteForUser class method in Configuration Manager."
---

# DeleteForUser Method

# DeleteForUser Method in Class SMS_ClientPfxCertificate
The `DeleteForUse` Windows Management Instrumentation (WMI) class method, in Configuration Manager, deletes a certificate for a user.

## Syntax

```
 sint32 DeleteForUser(
     String ProfileName,
     String UserName,
     String Thumbprint
);

```

#### Parameters
 `ProfileName`
 Data type: `String`

 Qualifiers: [in]

 The profile name.

 `UserName`
 Data type: `String`

 Qualifiers: [in]

 The user name.

 `Thumbprint`
 Data type: `String`

 Qualifiers: [in]

 The thumbprint for the certificate.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_ClientPfxCertificate Server WMI Class](../../../../../develop/reference/core/clients/deploy/sms_clientpfxcertificate-server-wmi-class.md)
