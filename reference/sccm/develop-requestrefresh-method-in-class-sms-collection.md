---
title: "RequestRefresh Method"
type: reference
domain: sccm
slug: develop-requestrefresh-method-in-class-sms-collection
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/collections/requestrefresh-method-in-class-sms_collection
family: develop
documentKind: "reference"
abstract: "Learn how to trigger a re-evaluation of collection membership by the Configuration Manager collection evaluator component."
---

# RequestRefresh Method

# RequestRefresh Method in Class SMS_Collection
The `RequestRefresh` Windows Management Instrumentation (WMI) class method, in Configuration Manager, triggers a re-evaluation of collection membership by the Configuration Manager collection evaluator component.

 The following syntax is simplified from Managed Object Format (MOF) code and is intended to show the definition of the method.

## Syntax

```
SInt32 RequestRefresh();
```

#### Parameters

> [!NOTE]
>  The previously available parameter `includesubcollections` has been deprecated in Configuration Manager.

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
