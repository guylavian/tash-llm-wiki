---
title: "Stop method"
type: reference
domain: sccm
slug: develop-stop-method-in-class-sms-azureservice
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/stop-method-in-class-sms_azureservice
family: develop
documentKind: "reference"
abstract: "Learn how to use the Stop method to stop a Microsoft Azure service that represents a cloud distribution point for Configuration Manager."
---

# Stop method

# Stop method in class SMS_AzureService

The `Stop` WMI class method in Configuration Manager that's invoked to stop a Microsoft Azure service that represents a cloud distribution point for Configuration Manager.

The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
uint32 Stop
{
    [IN]    UInt32 AzureServiceID
};
```

## Parameters
 `AzureServiceID`
 Data type: `UInt32`

 Qualifiers: [id("0"), in]

 The service identifier key for the `SMS_AzureService` instance on which the current task will be performed.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
