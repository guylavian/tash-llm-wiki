---
title: "AcceptEULA Method in SMS_SoftwareUpdate"
type: reference
domain: sccm
slug: develop-accepteula-method-in-class-sms-softwareupdate
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/sum/accepteula-method-in-class-sms_softwareupdate
family: develop
documentKind: "reference"
abstract: "The AcceptEULA WMI class method accepts or declines the Microsoft Software License Terms of a configuration item."
---

# AcceptEULA Method in SMS_SoftwareUpdate

# AcceptEULA Method in Class SMS_SoftwareUpdate
The `AcceptEULA` Windows Management Instrumentation (WMI) class method, in Configuration Manager, accepts or declines the Microsoft Software License Terms of a configuration item.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 AcceptEULA(
     Boolean Accepted
);
```

#### Parameters
 `Accepted`
 Data type: `Boolean`

 Qualifiers: [in]

 `true` if license terms are accepted.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).

## Remarks
 Your application should call this method only if the `EulaExists` property is set to `true` in the configuration item for the software update. This property is defined in the [SMS_ConfigurationItemBaseClass Server WMI Class](../../../develop/reference/compliance/sms_configurationitembaseclass-server-wmi-class.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_SoftwareUpdate Server WMI Class](../../../develop/reference/sum/sms_softwareupdate-server-wmi-class.md)
