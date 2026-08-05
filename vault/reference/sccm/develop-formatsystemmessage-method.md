---
title: "FormatSystemMessage Method"
type: reference
domain: sccm
slug: develop-formatsystemmessage-method
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/manage/formatsystemmessage-method
family: develop
documentKind: "reference"
abstract: "Learn how the FormatSystemMessage method, in Configuration Manager, formats a system error message by using the error code and optional insertion strings."
---

# FormatSystemMessage Method

# FormatSystemMessage Method
The `FormatSystemMessage` method, in Configuration Manager, formats a system error message by using the error code and optional insertion strings.

## Syntax

```
[VBScript]
SMSFormatMessageCtl.FormatSystemMessage
```

#### Parameters
 `MessageID`
 Data type: `int`

 Error message ID.

 `InsertionStrings`
 Data type: `object`

 Optional list of insertion strings.

## Return Value
 A string.

## Requirements
 FormatMessageCtl.dll.

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMSFormatMessageCtl Class](../../../../../develop/reference/core/servers/manage/smsformatmessagectl-class.md)
