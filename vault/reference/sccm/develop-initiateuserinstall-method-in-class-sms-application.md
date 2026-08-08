---
title: "InitiateUserInstall Method"
type: reference
domain: sccm
slug: develop-initiateuserinstall-method-in-class-sms-application
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/apps/initiateuserinstall-method-in-class-sms_application
family: develop
documentKind: "reference"
abstract: "InitiateUserInstall method is reserved for future use in Configuration Manager."
---

# InitiateUserInstall Method

# InitiateUserInstall Method in Class SMS_Application
> [!WARNING]
>  This method is reserved for future use.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 InitiateUserInstall (
     String  ModelName,
     String  Username,
     String  ClientGUID
);

```

#### Parameters
 `ModelName`
 Data type: `String`

 Qualifiers: [in]

 Model name of the application.

 `Username`
 Data type: `String`

 Qualifiers: [in]

 Unique user name.

 `ClientGUID`
 Data type: `String`

 Qualifiers: [in]

 Unique identifier of a client.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Application Server WMI Class](../../../develop/reference/apps/sms_application-server-wmi-class.md)
