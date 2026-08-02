---
title: "EvaluateAllAutoDeployment Method"
type: reference
domain: sccm
slug: develop-evaluateallautodeployment-method-in-class-sms-autodeployment
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/sum/evaluateallautodeployment-method-in-class-sms_autodeployment
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the EvaluateAllAutoDeployment WMI class method evaluates all automatic deployments."
---

# EvaluateAllAutoDeployment Method

# EvaluateAllAutoDeployment Method in Class SMS_AutoDeployment
The `EvaluateAllAutoDeployment` Windows Management Instrumentation (WMI) class method, in Configuration Manager, evaluates all automatic deployments.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 EvaluateAllAutoDeployment();

```

#### Parameters
 None.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

### Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

### Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_AutoDeployment Server WMI Class](../../../develop/reference/sum/sms_autodeployment-server-wmi-class.md)
