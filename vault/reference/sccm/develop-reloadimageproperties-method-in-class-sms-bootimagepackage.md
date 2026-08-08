---
title: "ReloadImageProperties method in class SMS_BootImagePackage"
type: reference
domain: sccm
slug: develop-reloadimageproperties-method-in-class-sms-bootimagepackage
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/osd/reloadimageproperties-method-in-class-sms_bootimagepackage
family: develop
documentKind: "reference"
abstract: "Reloads image metadata from a boot image source .wim file and synchronizes the metadata with the database."
---

# ReloadImageProperties method in class SMS_BootImagePackage

# ReloadImageProperties Method in Class SMS_BootImagePackage
The `ReloadImageProperties` Windows Management Instrumentation WMI class method, in Configuration Manager, reloads image metadata from a boot image source .wim file and synchronizes the metadata with the database.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 ReloadImageProperties();
```

#### Parameters
 None.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).

## Remarks
 The application uses this method if the administrator changes the boot image source .wim file outside of the Configuration Manager console. The application should:

1.  Establish a connection to the SMS Provider. For more information, see [SMS Provider fundamentals](../../core/understand/sms-provider-fundamentals.md).

2.  Obtain the [SMS_BootImagePackage Server WMI Class](../../../develop/reference/osd/sms_bootimagepackage-server-wmi-class.md) object to update.

3.  Call `ReloadImageProperties`.

4.  Commit the `SMS_BootImagePackage` object.

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_BootImagePackage Server WMI Class](../../../develop/reference/osd/sms_bootimagepackage-server-wmi-class.md)
 [UpdateImage Method in Class SMS_BootImagePackage](../../../develop/reference/osd/updateimage-method-in-class-sms_bootimagepackage.md)
