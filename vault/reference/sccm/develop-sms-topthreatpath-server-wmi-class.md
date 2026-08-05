---
title: "SMS_TopThreatPath Class"
type: reference
domain: sccm
slug: develop-sms-topthreatpath-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/protect/sms_topthreatpath-server-wmi-class
family: develop
documentKind: "reference"
abstract: "The SMS_ThreatPath Windows Management Instrumentation (WMI) class is an SMS Provider server class in Configuration Manager that represents summarizes the threats path found in 7 days per collection."
---

# SMS_TopThreatPath Class

# SMS_TopThreatPath Server WMI Class
The `SMS_ThreatPath` Windows Management Instrumentation (WMI) class is an SMS Provider server class in Configuration Manager that represents summarizes the threats path found in 7 days per collection.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_ThreatPath : SMS_BaseClass
{
    String CollectionID;
    UInt32 DuplicateCount;
    String Path;
    UInt64 ResourceID;
    UInt64 ThreatID;
    String ThreatName;
    UInt32 TotalCount;
};
```

## Methods
 The `SMS_ThreatPath` class doesn't define any methods.

## Properties
 `CollectionID`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: none

 Identifier of the collection.

 `DuplicateCount`
 Data type: `UInt32`

 Access type: Read/Write

 Qualifiers: none

 Count of members with a threat in that path.

 `Path`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: none

 Path of the threat.

 `ResourceID`
 Data type: `UInt64`

 Access type: Read/Write

 Qualifiers: [key]

 Identifier of the resource.

 `ThreatID`
 Data type: `UInt64`

 Access type: Read/Write

 Qualifiers: none

 Identifier of the threat.

 `ThreatName`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: none

 Name of the threat.

 `TotalCount`
 Data type: `UInt32`

 Access type: Read/Write

 Qualifiers: none

 Total count of members in the collection.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).
