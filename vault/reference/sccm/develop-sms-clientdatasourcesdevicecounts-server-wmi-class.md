---
title: "SMS_ClientDataSourcesDeviceCounts Class"
type: reference
domain: sccm
slug: develop-sms-clientdatasourcesdevicecounts-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/deploy/sms_clientdatasourcesdevicecounts-server-wmi-class
family: develop
documentKind: "reference"
abstract: "Learn how to use the SMS_ClientDataSourcesDeviceCounts class in Configuration Manager to represent device counts for client data sources."
---

# SMS_ClientDataSourcesDeviceCounts Class

# SMS_ClientDataSourcesDeviceCounts Server WMI Class
The `SMS_ClientDataSourcesContentStats` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents device counts for client data sources.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_ClientDataSourcesDeviceCounts : SMS_BaseClass
{
    UInt32 ClientCount;
    UInt32 DPCount;
    UInt32 PeerClientCount;
};

```

## Methods
 The `SMS_ClientDataSourcesDeviceCounts` class does not define any methods.

## Properties
 `ClientCount`
 Data type: `UInt32`

 Access type: Read

 Qualifiers: none

 The number of clients.

 `DPCount`
 Data type: `UInt32`

 Access type: Read

 Qualifiers: none

 The number of distribution points.

 `PeerClientCount`
 Data type: `UInt32`

 Access type: Read

 Qualifiers: none

 The number of peer clients.

## Remarks
 Class qualifiers for this class include:

- Dynamic

- Read (read-only)

- Singleton

- Secured

  For more information about both the class qualifiers and the property qualifiers included in the Properties section, see [Configuration Manager Class and Property Qualifiers](../../../../../develop/reference/misc/class-and-property-qualifiers.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
