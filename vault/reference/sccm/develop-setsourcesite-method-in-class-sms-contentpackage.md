---
title: "SetSourceSite method in class SMS_ContentPackage"
type: reference
domain: sccm
slug: develop-setsourcesite-method-in-class-sms-contentpackage
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/setsourcesite-method-in-class-sms_contentpackage
family: develop
documentKind: "reference"
abstract: "Learn how to change the source site code using SetSourceSite Windows Management Instrumentation (WMI) class method."
---

# SetSourceSite method in class SMS_ContentPackage

# SetSourceSite Method in Class SMS_ContentPackage
The `SetSourceSite` Windows Management Instrumentation (WMI) class method, in Configuration Manager, changes the source site code.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
sint32 SetSourceSite(
     string SourceSite
);
```

#### Parameters
 `SourceSite`
 Data type: `String` Array

 Qualifiers: `[in]`

 The site code of the source site for the package.

## Return Values
 An  `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Application Server WMI Class](../../../../../develop/reference/apps/sms_application-server-wmi-class.md)
