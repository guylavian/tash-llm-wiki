---
title: "GetEULA Method in Class SMS_UserStateManagementSettings"
type: reference
domain: sccm
slug: develop-geteula-method-in-class-sms-userstatemanagementsettings
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/compliance/geteula-method-in-class-sms_userstatemanagementsettings
family: develop
documentKind: "reference"
abstract: "A Windows Management Instrumentation class method that gets the localized Microsoft Software License Terms text of the configuration item."
---

# GetEULA Method in Class SMS_UserStateManagementSettings

# GetEULA Method in Class SMS_UserStateManagementSettings
The `GetEULA` Windows Management Instrumentation (WMI) class method, in Configuration Manager, gets the localized Microsoft Software License Terms text of the configuration item.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 GetEULA(
      String EULA
);
```

#### Parameters
 `EULA`
 Data type: `String`

 Qualifiers: [out]

 A value identifying the localized license terms.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).

## Remarks
 Your application should call this method only if the `EulaExists` property is set to `true` in the configuration item. This property is defined in the [SMS_ConfigurationItemBaseClass Server WMI Class](../../../develop/reference/compliance/sms_configurationitembaseclass-server-wmi-class.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_ConfigurationItem Server WMI Class](../../../develop/reference/compliance/sms_configurationitem-server-wmi-class.md)
 [SMS_ConfigurationItemBaseClass Server WMI Class](../../../develop/reference/compliance/sms_configurationitembaseclass-server-wmi-class.md)
