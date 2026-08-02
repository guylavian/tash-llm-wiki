---
title: "AppContentInfo Structure"
type: reference
domain: sccm
slug: develop-appcontentinfo-structure
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/appcontentinfo-structure
family: develop
documentKind: "reference"
abstract: "The AppContentInfo structure provides information about the application content."
---

# AppContentInfo Structure

# AppContentInfo Structure
In Configuration Manager, the `AppContentInfo` structure contains information about the application content.

## Syntax

```
struct AppContentInfo
{
    LPCWSTR szContentId;
    LPCWSTR szContentVersion;
    LPCWSTR szLocalPath;
};
```

## Members
 `szContentId`
 The content id.

 `szContentVersion`
 The content version.

 `szLocalPath`
 The local path.

## See Also
 [Configuration Manager Software Development Kit](../../../../../develop/core/misc/system-center-configuration-manager-sdk.md)
 [Configuration Manager Reference](../../../../../develop/reference/configuration-manager-reference.md)
