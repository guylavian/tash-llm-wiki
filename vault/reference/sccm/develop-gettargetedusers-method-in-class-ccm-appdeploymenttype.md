---
title: "GetTargetedUsers Method"
type: reference
domain: sccm
slug: develop-gettargetedusers-method-in-class-ccm-appdeploymenttype
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/sdk/gettargetedusers-method-in-class-ccm_appdeploymenttype
family: develop
documentKind: "reference"
abstract: "Learn how to retrieve the targeted users of an application deployment type using GetTargetedUsers class method."
---

# GetTargetedUsers Method

# GetTargetedUsers Method in Class CCM_AppDeploymentType
The `GetTargetedUsers` Windows Management Instrumentation (WMI) class method in Configuration Manager that retrieves the targeted users of an application deployment type.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
uint32 GetTargetedUsers
{
    [IN]    String Id
    [IN]    String Revision
    [OUT]   String Users[]
};
```

## Parameters
 `Id`
 Data type: `String`

 Qualifiers: [id("0"), in]

 Identifier.

 `Revision`
 Data type: `String`

 Qualifiers: [id("1"), in]

 Revision.

 `Users`
 Data type: `String Array`

 Qualifiers: [id("2"), out]

 Targeted users.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
