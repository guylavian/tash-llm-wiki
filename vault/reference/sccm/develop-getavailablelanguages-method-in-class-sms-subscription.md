---
title: "GetAvailableLanguages Method"
type: reference
domain: sccm
slug: develop-getavailablelanguages-method-in-class-sms-subscription
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/manage/getavailablelanguages-method-in-class-sms_subscription
family: develop
documentKind: "reference"
abstract: "Learn how to use the GetAvailableLanguages method on the SMS_Subscription class to obtain a list of available languages."
---

# GetAvailableLanguages Method

# GetAvailableLanguages Method in Class SMS_Subscription
The `GetAvailableLanguages` Windows Management Instrumentation (WMI) class method, in Configuration Manager, gets the available languages.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
sint32 GetAvailableLanguages(
     UInt32 LocaleIDs[]
);
```

#### Parameters
 `LocaleIDs`
 Data type: `UInt32`  array

 Qualifiers: `[out]`

 The identifiers of the locales associated with the localized information.

## Return Values
 An  `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See also

[SMS_Alert server WMI class](sms_alert-server-wmi-class.md)
