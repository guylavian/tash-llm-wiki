---
title: "SMS_AdminCategory Class"
type: reference
domain: sccm
slug: develop-sms-admincategory-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/sms_admincategory-server-wmi-class
family: develop
documentKind: "reference"
abstract: "Learn how to represent an association between the admin account and an RBA secured category in Configuration Manager using SMS_AdminCategory."
---

# SMS_AdminCategory Class

# SMS_AdminCategory Server WMI Class
The `SMS_AdminCategory` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents an association between the admin account and an RBA secured category.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_AdminCategory : SMS_BaseClass
{
    UInt32 AdminID;
    String CategoryID;
};
```

## Methods
 The `SMS_AdminCategory` class does not define any methods.

## Properties
 `AdminID`
 Data type: `UInt32`

 Access type: Read/Write

 Qualifiers: [key]

 ID of the associated account.

 `CategoryID`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: [key]

 ID of the associated RBA secured category.

## Requirements

### Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

### Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
