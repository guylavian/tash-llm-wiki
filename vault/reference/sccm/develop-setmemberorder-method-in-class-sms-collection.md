---
title: "SetMemberOrder Method"
type: reference
domain: sccm
slug: develop-setmemberorder-method-in-class-sms-collection
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/collections/setmemberorder-method-in-class-sms_collection
family: develop
documentKind: "reference"
abstract: "Set the order of the members of a collection. It is used when the members of a server group collection need to be patched in a particular order."
---

# SetMemberOrder Method

# SetMemberOrder Method in Class SMS_Collection
The `SetMemberOrder` Windows Management Instrumentation (WMI) class method, in Configuration Manager, sets the order of the members of a collection. Use this class instance when the members of a  server group collection need to be patched in a particular order.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 SetMemberOrder (
    String CollectionID,
    String ResourceIDs
);

```

#### Parameters
 `CollectionID`
 Data type: `String`

 Qualifiers: [in]

 The ID of a collection.

 `ResourceIDs`
 Data type: `String`

 Qualifiers: [in]

 A string of resource IDs.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Collection Server WMI Class](../../../../../develop/reference/core/clients/collections/sms_collection-server-wmi-class.md)
 [SMS_Site Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_site-server-wmi-class.md)
