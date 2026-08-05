---
title: "SMS_G_System Class"
type: reference
domain: sccm
slug: develop-sms-g-system-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/manage/sms_g_system-server-wmi-class
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the SMS_G_System WMI class is an SMS Provider server class that serves as the abstract base class for all hardware and software system classes."
---

# SMS_G_System Class

# SMS_G_System Server WMI Class
The `SMS_G_System` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that serves as the abstract base class for all hardware and software system classes, for example, [SMS_G_System_CI_ComplianceState Server WMI Class](../../../../../develop/reference/compliance/sms_g_system_ci_compliancestate-server-wmi-class.md).

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_G_System : SMS_Group
{
     UInt32 ResourceID;
};
```

## Methods
 The `SMS_G_System` class does not define any methods.

## Properties
 `ResourceID`
 Data type: `UInt32`

 Access type: Read/Write

 Qualifiers: None

 See [SMS_Group Server WMI Class](../../../../../develop/reference/core/clients/manage/sms_group-server-wmi-class.md).

## Remarks
 Class qualifiers for this class include:

- Abstract

  For more information about both the class qualifiers and the property qualifiers included in the Properties section, see [Configuration Manager Class and Property Qualifiers](../../../../../develop/reference/misc/class-and-property-qualifiers.md).

## Requirements

### Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

### Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Group Server WMI Class](../../../../../develop/reference/core/clients/manage/sms_group-server-wmi-class.md)
