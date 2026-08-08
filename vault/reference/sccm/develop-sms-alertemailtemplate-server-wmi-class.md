---
title: "SMS_AlertEmailTemplate Class"
type: reference
domain: sccm
slug: develop-sms-alertemailtemplate-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/manage/sms_alertemailtemplate-server-wmi-class
family: develop
documentKind: "reference"
abstract: "Learn how to represent the email template embedded by SMS_Subscription using SMS_AlertEmailTemplate."
---

# SMS_AlertEmailTemplate Class

# SMS_AlertEmailTemplate Server WMI Class
The `SMS_AlertEmailTemplate` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents the email template embedded by `SMS_Subscription`.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_AlertEmailTemplate
{
    UInt32 AlertID,
    String Subject
};
```

## Methods
 The `SMS_AlertEmailTemplate` class does not define any methods.

## Properties
 `AlertID`
 Data type: `UInt32`

 Access type: Read/Write

 Qualifiers: none

 Identifier of the alert.

 `Subject`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: none

 Subject of the email.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
