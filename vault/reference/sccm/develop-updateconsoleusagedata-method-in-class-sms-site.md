---
title: "UpdateConsoleUsageData Method"
type: reference
domain: sccm
slug: develop-updateconsoleusagedata-method-in-class-sms-site
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/updateconsoleusagedata-method-in-class-sms_site
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the UpdateConsoleUsageData WMI class method updates console usage data received from console connections."
---

# UpdateConsoleUsageData Method

# UpdateConsoleUsageData Method in Class SMS_Site
The `UpdateConsoleUsageData` Windows Management Instrumentation (WMI) class method, in Configuration Manager, updates console usage data received from console connections.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 UpdateConsoleUsageData (
    SMS_ConsoleUsageData ConsoleUsageData
);

```

#### Parameters
 `ConsoleUsageData`
 Data type: `SMS_ConsoleUsageData`

 Qualifiers: [in]

 Console usage data.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Site Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_site-server-wmi-class.md)
