---
title: "Commit Method"
type: reference
domain: sccm
slug: develop-commit-method-in-class-sms-contentpackage
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/commit-method-in-class-sms_contentpackage
family: develop
documentKind: "reference"
abstract: "A Windows Management Instrumentation class method, which indicates that the content package is ready for processing."
---

# Commit Method

# Commit Method in Class SMS_ContentPackage
The `Commit` Windows Management Instrumentation (WMI) class method, in Configuration Manager, indicates that the content package is ready for processing.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
sint32 Commit();
```

#### Parameters
 None.

## Remarks
 This method needs to be called when all the contents have been added to the content package to start package processing.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Application Server WMI Class](../../../../../develop/reference/apps/sms_application-server-wmi-class.md)
