---
title: "DeleteMembershipRules Method"
type: reference
domain: sccm
slug: develop-deletemembershiprules-method-in-class-sms-collection
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/collections/deletemembershiprules-method-in-class-sms_collection
family: develop
documentKind: "reference"
abstract: "The DeleteMembershipRules Windows Management Instrumentation class method, in Configuration Manager, is used to delete multiple membership rules from the collection."
---

# DeleteMembershipRules Method

# DeleteMembershipRules Method in Class SMS_Collection
The `DeleteMembershipRules` Windows Management Instrumentation (WMI) class method, in Configuration Manager, is used to delete multiple membership rules from the collection.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 DeleteMembershipRules(
      SMS_CollectionRule collectionRules[]
);
```

#### Parameters
 `collectionRules`
 Data type: `SMS_CollectionRule` Array

 Qualifiers: [in]

 [SMS_CollectionRule Server WMI Class](sms_collectionrule-server-wmi-class.md) objects to delete.

## Return Values
 An  `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../../core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../core/reqs/server-development-requirements.md).

## See Also
 [SMS_Collection Server WMI Class](sms_collection-server-wmi-class.md)
 [SMS_Site Server WMI Class](../../servers/configure/sms_site-server-wmi-class.md)
