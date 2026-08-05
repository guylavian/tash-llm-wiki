---
title: "SMS_DPGroupPackages Class"
type: reference
domain: sccm
slug: develop-sms-dpgrouppackages-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/sms_dpgrouppackages-server-wmi-class
family: develop
documentKind: "reference"
abstract: "The SMS_DPGroupPackages WMI class is an SMS Provider server class that represents distribution point packages."
---

# SMS_DPGroupPackages Class

# SMS_DPGroupPackages Server WMI Class
The `SMS_DPGroupPackages` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents distribution point packages.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_DPGroupPackages : SMS_BaseClass
{
    String GroupID;
    String PkgID;
};
```

## Methods
 The `SMS_DPGroupPackages` class does not define any methods.

## Properties
 `GroupID`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: [key]

 Unique identifier for the distribution point group.

 `PkgID`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: [key]

 Package associated with the distribution point group.

## Requirements

### Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

### Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
