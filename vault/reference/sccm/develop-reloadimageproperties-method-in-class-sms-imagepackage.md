---
title: "ReloadImageProperties Method in SMS_ImagePackage"
type: reference
domain: sccm
slug: develop-reloadimageproperties-method-in-class-sms-imagepackage
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/osd/reloadimageproperties-method-in-class-sms_imagepackage
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the ReloadImageProperties WMI class method reloads image metadata from an image source .wim file."
---

# ReloadImageProperties Method in SMS_ImagePackage

# ReloadImageProperties Method in Class SMS_ImagePackage
The `ReloadImageProperties` Windows Management Instrumentation (WMI) class method, in Configuration Manager, reloads image metadata from an image source .wim file and synchronizes the metadata with the database.

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
 For an example of the use of this method, see [How to Update an Operating System Image Package in Configuration Manager](../../../develop/osd/how-to-update-an-operating-system-image-package.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_ImagePackage Server WMI Class](../../../develop/reference/osd/sms_imagepackage-server-wmi-class.md)
 [GetImageProperties Method in Class SMS_ImagePackage](../../../develop/reference/osd/getimageproperties-method-in-class-sms_imagepackage.md)
 [How to Update an Operating System Image Package in Configuration Manager](../../../develop/osd/how-to-update-an-operating-system-image-package.md)
