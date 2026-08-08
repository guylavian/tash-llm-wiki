---
title: "ManageDeploymentForDevice Method"
type: reference
domain: sccm
slug: develop-managedeploymentfordevice-method-in-class-sms-application
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/apps/managedeploymentfordevice-method-in-class-sms_application
family: develop
documentKind: "reference"
abstract: "The following syntax is simplified from Managed Object Format (MOF) code and defines the method."
---

# ManageDeploymentForDevice Method

# ManageDeploymentForDevice Method in Class SMS_Application
> [!WARNING]
>  This method is reserved for future use.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 ManageDeploymentForDevice (
     String   AssignmentUniqueID,
     String   ClientGUID,
     UInt32   Action
);

```

#### Parameters
 `AssignmentUniqueID`
 Data type: `String`

 Qualifiers: [in]

 Identifier for the application deployment.

 `ClientGUID`
 Data type: `String`

 Qualifiers: [in]

 Unique identifier of a client.

 `Action`
 Data type: `UInt32`

 Qualifiers: [in, enumeration]

 Activate or deactivate deployment. Possible values are:

|Value|Activate or deactivate|
|-|-|
|1|Activate|
|2|Deactivate|

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
