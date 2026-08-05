---
title: "SetIgnorePrereqWarning Method"
type: reference
domain: sccm
slug: develop-setignoreprereqwarning-method-in-class-sms-cm-updatepackages
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/sum/setignoreprereqwarning-method-in-class-sms_cm_updatepackages
family: develop
documentKind: "reference"
abstract: "The SetIgnorePrereqWarning Windows Management Instrumentation class method, in Configuration Manager, updates the ignore prerequisites warning flag of the update packages."
---

# SetIgnorePrereqWarning Method

# SetIgnorePrereqWarning Method in Class SMS_CM_UpdatePackages
The `SetIgnorePrereqWarning` Windows Management Instrumentation (WMI) class method in Configuration Manager updates the ignore prerequisites  warning flag of the update packages.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method:

## Syntax

```
SInt32 SetIgnorePrereqWarning(
     UInt32 flag
);

```

#### Parameters
 `flag`
 Data type: `UInt32`

 Qualifiers: [in]

 Flag to ignore the  prerequisites  warning flag of the update packages. Possible values are:

| Value | Flag |
| ----- | ---- |
|0|NOT_CONTINUE_ON_PREREQ_WARNING. During installation, stop the upgrade if there's a prerequisite warning.|
|1|PREREQ_ONLY. Run only the prerequisite.|
|2|CONTINUE_ON_PREREQ_WARNING. During installation, ignore the prerequisite warning.|

## Return Values
 An `SInt32` data type that is 0 to indicate success or nonzero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

### Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

### Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_CM_UpdatePackages Server WMI Class](../../../develop/reference/sum/sms_cm_updatepackages-server-wmi-class.md)
