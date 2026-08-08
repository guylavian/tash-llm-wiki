---
title: "SMS_DmInvVersion Class"
type: reference
domain: sccm
slug: develop-sms-dminvversion-client-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/sms_dminvversion-client-wmi-class
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, The SMS_DmInvVersion class is a client Windows Management Instrumentation class that represents the device management inventory version."
---

# SMS_DmInvVersion Class

# SMS_DmInvVersion Client WMI Class
The `SMS_DmInvVersion` class is a client Windows Management Instrumentation (WMI) class in Configuration Manager that represents the device management inventory version.

## Syntax

```
Class SMS_DmInvVersion
{
   UInt32 Version
};
```

## Methods
 The `SMS_ActiveSyncConnectedDevice` class doesn't define any methods.

## Properties
 `Version`
 Data type: `UInt32`

 Access type: Read/Write

 Qualifiers: [key]

 The inventory version.

## See Also
 [Device Management Client WMI Classes](../../../../../develop/reference/core/clients/client-classes/device-management-client-wmi-classes.md)
