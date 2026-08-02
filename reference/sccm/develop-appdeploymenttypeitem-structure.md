---
title: "AppDeploymentTypeItem Structure"
type: reference
domain: sccm
slug: develop-appdeploymenttypeitem-structure
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/appdeploymenttypeitem-structure
family: develop
documentKind: "reference"
abstract: "Learn about the AppDeploymentTypeItem structure that contains detection results for an individual deployment type."
---

# AppDeploymentTypeItem Structure

# AppDeploymentTypeItem Structure
In Configuration Manager, the `AppDeploymentTypeItem` structure contains detection results for an individual deployment type.

## Syntax

```
typedef struct tagAppDeploymentTypeItem
{
    LPWSTR szId;
    DWORD dwRevision;
    AppDetectState eDetectState;
    DWORD dwErrorCode;
}AppDeploymentTypeItem, *PAppDeploymentTypeItem;
```

## Members
 `szId`
 ID of the deployment item.

 `dwRevision`
 Revision.

 `eDetectState`
 Detect state.

 dwErrorCode
 Error code.

## See Also
 [Configuration Manager Software Development Kit](../../../../../develop/core/misc/system-center-configuration-manager-sdk.md)
 [Configuration Manager Reference](../../../../../develop/reference/configuration-manager-reference.md)
