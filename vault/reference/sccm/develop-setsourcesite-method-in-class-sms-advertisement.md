---
title: "SetSourceSite method in class SMS_Advertisement"
type: reference
domain: sccm
slug: develop-setsourcesite-method-in-class-sms-advertisement
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/setsourcesite-method-in-class-sms_advertisement
family: develop
documentKind: "reference"
abstract: "Learn how the SetSourceSite Windows Management Instrumentation (WMI) class method, in Configuration Manager, sets the source site code for the advertisement."
---

# SetSourceSite method in class SMS_Advertisement

# SetSourceSite Method in Class SMS_Advertisement
The `SetSourceSite` Windows Management Instrumentation (WMI) class method, in Configuration Manager, sets the source site code for the advertisement.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
sint32 SetSourceSite(
     string SourceSite,
);
```

#### Parameters
 `SourceSite`
 Data type: `String`

 Qualifiers: `[in]`

 The site code of the source site for the advertisement.

## Return Values
 An  `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

### Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

### Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Advertisement Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_advertisement-server-wmi-class.md)
