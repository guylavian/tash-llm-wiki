---
title: "SMS_WhatsNewScenario Class"
type: reference
domain: sccm
slug: develop-sms-whatsnewscenario-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/misc/sms_whatsnewscenario-server-wmi-class
family: develop
documentKind: "reference"
abstract: "SMS_WhatsNewScenario Server WMI Class is for internal use only."
---

# SMS_WhatsNewScenario Class

# SMS_WhatsNewScenario Server WMI Class
For internal use only.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_WhatsNewScenario : SMS_BaseClass
{
    String Name;
    Boolean Completed;
};

```

## Methods
 The `SMS_WhatsNewScenario` class does not define any methods.

## Properties
 `Name`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: none

 Reserved for internal use.

 `Completed`
 Data type: `Boolean`

 Access type: Read/Write

 Qualifiers: none

 Reserved for internal use.

## Remarks
 Class qualifiers for this class include:

- Dynamic

- Embedded

  For more information about both the class qualifiers and the property qualifiers included in the Properties section, see [Configuration Manager Class and Property Qualifiers](../../../develop/reference/misc/class-and-property-qualifiers.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [Configuration Manager Reference](../../../develop/reference/configuration-manager-reference.md)
