---
title: "RemoveContent method in class SMS_ContentPackage"
type: reference
domain: sccm
slug: develop-removecontent-method-in-class-sms-contentpackage
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/removecontent-method-in-class-sms_contentpackage
family: develop
documentKind: "reference"
abstract: "Learn how to use the RemoteContent class method to remove the content for the given content ID from a package."
---

# RemoveContent method in class SMS_ContentPackage

# RemoveContent Method in Class SMS_ContentPackage
The `RemoveContent` Windows Management Instrumentation (WMI) class method, in Configuration Manager, removes the content for the given content ID from the package.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
sint32 RemoveContent(
     uint32  ContentIDs[],
     boolean bRefreshDPs[],
);
```

#### Parameters
 `ContentIDs`
 Data type: `UInt32` Array

 Qualifiers: `[in, optional]`

 Content identifiers for content to be removed.

 `bRefreshDPs`
 Data type: `Boolean` Array

 Qualifiers: `[in]`

 `true`, if distribution points should be refreshed. The default value is `true`.

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
