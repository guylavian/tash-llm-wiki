---
title: "SMS_RcmSqlControlProperty Class"
type: reference
domain: sccm
slug: develop-sms-rcmsqlcontrolproperty-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/sms_rcmsqlcontrolproperty-server-wmi-class
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the SMS_RcmSqlControlProperty Windows Management Instrumentation class is an SMS Provider server class."
---

# SMS_RcmSqlControlProperty Class

# SMS_RcmSqlControlProperty Server WMI Class

The `SMS_RcmSqlControlProperty` Windows Management Instrumentation (WMI) class is an SMS Provider server class in Configuration Manager.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_RcmSqlControlProperty :
{
    String PropertyName;
    UInt32 Value;
    String Value1;
    String Value2;
};
```

## Methods
 The `SMS_RcmSqlControlProperty` class does not define any methods.

## Properties
 `PropertyName`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: [key]

 Name of the property.

 `Value`
 Data type: `UInt32`

 Access type: Read/Write

 Qualifiers: none

 Property integer value.

 `Value1`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: none

 First string value of the property.

 `Value2`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: none

 Second string value of the property.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
