---
title: "DistributeDeploymentTypeExtension Method"
type: reference
domain: sccm
slug: develop-distributedeploymenttypeextension-method-in-class-sms-deploymenttype
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/apps/distributedeploymenttypeextension-method-in-class-sms_deploymenttype
family: develop
documentKind: "reference"
abstract: "The DistributeDeploymentTypeExtension Windows Management Instrumentation (WMI) class method, in Configuration Manager, schedules a Deployment Type Extension to be distributed throughout the hierarchy."
---

# DistributeDeploymentTypeExtension Method

# DistributeDeploymentTypeExtension Method in Class SMS_DeploymentType
The `DistributeDeploymentTypeExtension` Windows Management Instrumentation (WMI) class method, in Configuration Manager, schedules a Deployment Type Extension to be distributed throughout the hierarchy.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
sint32 DistributeDeploymentTypeExtension (
     string TechnologyExtensionFileName
);
```

#### Parameters
 `TechnologyExtensionFileName`
 Data type: `String`

 Qualifiers: [in]

 Filename of the technology extension.

## Return Values
 An  `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_DeploymentType Server WMI Class](../../../develop/reference/apps/sms_deploymenttype-server-wmi-class.md)
