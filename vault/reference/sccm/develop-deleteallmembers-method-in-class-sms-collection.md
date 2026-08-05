---
title: "DeleteAllMembers Method"
type: reference
domain: sccm
slug: develop-deleteallmembers-method-in-class-sms-collection
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/collections/deleteallmembers-method-in-class-sms_collection
family: develop
documentKind: "reference"
abstract: "Learn how to delete all members, that is, resources and discovery data, for a collection using the DeleteAllMembers class method."
---

# DeleteAllMembers Method

# DeleteAllMembers Method in Class SMS_Collection
The `DeleteAllMembers` Windows Management Instrumentation (WMI) class method, in Configuration Manager, deletes all members, that is, resources and discovery data, for the collection.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 DeleteAllMembers();
```

#### Parameters
 None.

## Return Values
 An  `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Collection Server WMI Class](../../../../../develop/reference/core/clients/collections/sms_collection-server-wmi-class.md)
 [SMS_Site Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_site-server-wmi-class.md)
