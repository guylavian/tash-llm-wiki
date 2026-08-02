---
title: "InventoryActionStatus Client WMI Class"
type: reference
domain: sccm
slug: develop-inventoryactionstatus-client-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/inventoryactionstatus-client-wmi-class
family: develop
documentKind: "reference"
abstract: "The InventoryActionStatus class is a client Windows Management Instrumentation (WMI) class that defines the status of an inventory action."
---

# InventoryActionStatus Client WMI Class

# InventoryActionStatus Client WMI Class
In Configuration Manager, the `InventoryActionStatus` class is a client Windows Management Instrumentation (WMI) class that defines the status of an inventory action.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class InventoryActionStatus
{
      String InventoryActionID;
      DateTime LastCycleStartedDate;
      UInt32 LastMajorReportVersion;
      UInt32 LastMinorReportVersion;
      DateTime LastReportDate;
};
```

## Methods
 The `InventoryActionStatus` class does not define any methods.

## Properties
 `InventoryActionID`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: [key]

 The inventory action ID.

 `LastCycleStartedDate`
 Data type: `DateTime`

 Access type: Read/Write

 Qualifiers: None

 The time when the last inventory cycle started.

 `LastMajorReportVersion`
 Data type: `UInt32`

 Access type: Read/Write

 Qualifiers: None

 The major version of the last major report.

 `LastMinorReportVersion`
 Data type: `UInt32`

 Access type: Read/Write

 Qualifiers: None

 The minor version on the last report.

 `LastReportDate`
 Data type: `DateTime`

 Access type: Read/Write

 Qualifiers: None

 The date and time of the last report.

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Client Runtime Requirements](../../../../../develop/core/reqs/client-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Client Development Requirements](../../../../../develop/core/reqs/client-development-requirements.md).

## See Also
 [Inventory Agent Client WMI Classes](../../../../../develop/reference/core/clients/client-classes/inventory-agent-client-wmi-classes.md)
