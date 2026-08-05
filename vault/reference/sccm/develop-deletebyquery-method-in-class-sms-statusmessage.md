---
title: "DeleteByQuery Method"
type: reference
domain: sccm
slug: develop-deletebyquery-method-in-class-sms-statusmessage
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/manage/deletebyquery-method-in-class-sms_statusmessage
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the DeleteByQuery WMI class method deletes status messages specified by a WQL query."
---

# DeleteByQuery Method

# DeleteByQuery Method in Class SMS_StatusMessage
The `DeleteByQuery` Windows Management Instrumentation (WMI) class method, in Configuration Manager, deletes status messages specified by a WQL query.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
UInt32 DeleteByQuery(
      String WQLSelect
);
```

#### Parameters
 `WQLSelect`
 Data type: `String`

 Qualifiers: [in]

 A WQL SELECT statement.

## Return Values
 A `UInt32` data type that indicates the number of rows deleted.

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_StatusMessage Server WMI Class](../../../../../develop/reference/core/servers/manage/sms_statusmessage-server-wmi-class.md)
