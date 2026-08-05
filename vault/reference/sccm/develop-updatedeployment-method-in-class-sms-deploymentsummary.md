---
title: "UpdateDeployment Method"
type: reference
domain: sccm
slug: develop-updatedeployment-method-in-class-sms-deploymentsummary
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/apps/updatedeployment-method-in-class-sms_deploymentsummary
family: develop
documentKind: "reference"
abstract: "Learn how to update the summarized results for a specific Classic Deployment in Configuration Manager using UpdateDeployment."
---

# UpdateDeployment Method

# UpdateDeployment Method in Class SMS_DeploymentSummary
The `UpdateDeployment` Windows Management Instrumentation (WMI) class method, in Configuration Manager, updates the summarized results for a specific Classic Deployment.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
sint32 UpdateDeployment (
     uint32 AssignmentID
);
```

#### Parameters
 `AssignmentID`
 Data type: `UInt32`

 Qualifiers: [in]

 Identifier of the configuration item assignment. This identifier is unique only for the site.

## Return Values
 An  `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_DeploymentSummary Server WMI Class](../../../develop/reference/apps/sms_deploymentsummary-server-wmi-class.md)
