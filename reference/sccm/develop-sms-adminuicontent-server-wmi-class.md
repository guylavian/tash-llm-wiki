---
title: "SMS_AdminUIContent Class"
type: reference
domain: sccm
slug: develop-sms-adminuicontent-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/misc/sms-adminuicontent-server-wmi-class
family: develop
documentKind: "reference"
abstract: "Learn how to use the SMS_AdminUIContent class although it has no defined methods."
---

# SMS_AdminUIContent Class

# SMS_AdminUIContent Server WMI Class
For internal use only.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_AdminUIContent : SMS_BaseClass
{
    DateTime CreationDate;
    String Data;
    String Name;
};

```

## Methods
 The `SMS_AdminUIContent` class does not define any methods.

## Properties
 `CreationDate`
 Data type: `DateTime`

 Access type: Read-only

 Qualifiers: None

 Reserved for internal use.

 `Data`
 Data type: `String`

 Access type: Read-only

 Qualifiers: None

 Reserved for internal use.

 `Name`
 Data type:  `String`

 Access type: Read-only

 Qualifiers: [unique, not_null, key]

 Reserved for internal use.

## Remarks
  Class qualifiers for this class include:

- Read

- Secured

  For more information about both the class qualifiers and the property qualifiers included in the Properties section, see [Configuration Manager Class and Property Qualifiers](../../../develop/reference/misc/class-and-property-qualifiers.md).

## Requirements

### Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

### Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).
