---
title: "SMS_ClientDataSourcesContent Class"
type: reference
domain: sccm
slug: develop-sms-clientdatasourcescontent-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/deploy/sms_clientdatasourcescontent-server-wmi-class
family: develop
documentKind: "reference"
abstract: "The SMS_ClientDataSourcesContent Windows Management Instrumentation class is an SMS Provider server class, in Configuration Manager."
---

# SMS_ClientDataSourcesContent Class

# SMS_ClientDataSourcesContent Server WMI Class
The `SMS_ClientDataSourcesContent` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents client content data sources per boundary group.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_ClientDataSourcesContent : SMS_BaseClass
{
    UInt64 BranchCacheBytes;
    UInt64 CloudDistributionPointBytes;
    UInt64 DistributionPointBytes;
    UInt32 DpSourceServerCount;
    UInt64 PeerCacheBytes;
    UInt32 SpSourceClientCount;
};

```

## Methods
 The `SMS_ClientDataSourcesContent` class does not define any methods.

## Properties
 `BranchCacheBytes`
 Data type: `UInt64`

 Access type: Read

 Qualifiers: none

 Number of bytes from the branch cache.

 `CloudDistributionPointBytes`
 Data type: `UInt64`

 Access type: Read

 Qualifiers: none

 Number of bytes from cloud distribution points.

 `DistributionPointBytes`
 Data type: `UInt64`

 Access type: Read

 Qualifiers: none

 Number of bytes from distribution points.

 `DpSourceServerCount`
 Data type: `UInt32`

 Access type: Read

 Qualifiers: none

 Number of distribution points that served content.

 `PeerCacheBytes`
 Data type: `UInt64`

 Access type: Read

 Qualifiers: none

 Number of bytes from the peer cache.

 `SpSourceClientCount`
 Data type: `UInt32`

 Access type: Read

 Qualifiers: none

 Number of super peers that served content.

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
