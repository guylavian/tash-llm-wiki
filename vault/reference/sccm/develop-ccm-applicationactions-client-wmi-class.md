---
title: "CCM_ApplicationActions Class"
type: reference
domain: sccm
slug: develop-ccm-applicationactions-client-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/sdk/ccm_applicationactions-client-wmi-class
family: develop
documentKind: "reference"
abstract: "Learn how to represent application actions using CCM_ApplicationActions class in Configuration Manager."
---

# CCM_ApplicationActions Class

# CCM_ApplicationActions Client WMI Class
The `CCM_ApplicationActions` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents application actions.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class CCM_ApplicationActions :
{
    DateTime NextGlobalRevalTime;
    DateTime NextRetryTime;
    DateTime NextServiceWindowTime;
};
```

## Methods
 The `CCM_ApplicationActions` class does not define any methods.

## Properties
 `NextGlobalRevalTime`
 Data type: `DateTime`

 Access type: Read/Write

 Qualifiers: none

 Next global reevaluation time.

 `NextRetryTime`
 Data type: `DateTime`

 Access type: Read/Write

 Qualifiers: none

 Next retry time

 `NextServiceWindowTime`
 Data type: `DateTime`

 Access type: Read/Write

 Qualifiers: none

 Next service window time.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
