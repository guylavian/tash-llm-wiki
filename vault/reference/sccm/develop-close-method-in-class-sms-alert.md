---
title: "Close Method in Class SMS_Alert"
type: reference
domain: sccm
slug: develop-close-method-in-class-sms-alert
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/manage/close-method-in-class-sms_alert
family: develop
documentKind: "reference"
abstract: "Learn how the Close Windows Management Instrumentation (WMI) class method, in Configuration Manager, postpones the alert."
---

# Close Method in Class SMS_Alert

# Close Method in Class SMS_Alert
The `Close` Windows Management Instrumentation (WMI) class method, in Configuration Manager, postpones the alert.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
sint32 Close(
     string Comments,
     datetime SkipUntil
);
```

#### Parameters
 `Comments`
 Data type: `String`

 Qualifiers: `[in, optional]`

 Administrator-supplied comments for the postpone action.

 `SkipUntil`
 Data type: `DateTime`

 Qualifiers: `[out, optional]`

 Don't start the evaluation until the specified time.

## Return Values
 An  `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See also

[SMS_Alert server WMI class](sms_alert-server-wmi-class.md)
