---
title: "GetOnlineCount Method"
type: reference
domain: sccm
slug: develop-getonlinecount-method-in-class-sms-cn-clientstatus
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/status/getonlinecount-method-in-class-sms_cn_clientstatus
family: develop
documentKind: "reference"
abstract: "Learn how to get an online count of the selected clients of the target collection using GetOnlineCount class method."
---

# GetOnlineCount Method

# GetOnlineCount Method in Class SMS_CN_ClientStatus
The `GetOnlineCount` Windows Management Instrumentation (WMI) class method, in Configuration Manager, that gets an online count of the selected clients of the target collection.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
uint32 GetOnlineCount
{
    [IN]    String TargetCollectionID
    [IN]    Uint32 TargetResourceIDs[]
};
```

## Parameters
 `TargetCollectionID`
 Data type: `String`

 Qualifiers: [id("0"), in]

 Target collection identifier.

 `TargetResourceIDs`
 Data type: `UInt32` Array

 Qualifiers: [id("1"), in]

 Target client resource identifiers.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
