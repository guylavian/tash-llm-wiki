---
title: "DeleteContextID Method"
type: reference
domain: sccm
slug: develop-deletecontextid-method-in-class-sms-bootimagepackage
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/osd/deletecontextid-method-in-class-sms_bootimagepackage
family: develop
documentKind: "reference"
abstract: "Learn how to delete the status queue that is associated with the specified context ID for the boot image package using the DeleteContextID."
---

# DeleteContextID Method

# DeleteContextID Method in Class SMS_BootImagePackage
The `DeleteContextID` Windows Management Instrumentation (WMI) class method, in Configuration Manager, deletes the status queue that is associated with the specified context ID for the boot image package.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 DeleteContextID(
     String ContextID
);
```

#### Parameters
 `ContextID`
 Data type: `String`

 Qualifiers: [in]

 The ID of the context that is associated with the boot image package status.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_BootImagePackage Server WMI Class](../../../develop/reference/osd/sms_bootimagepackage-server-wmi-class.md)
