---
title: "CIDetectInfo Structure"
type: reference
domain: sccm
slug: develop-cidetectinfo-structure
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/cidetectinfo-structure
family: develop
documentKind: "reference"
abstract: "Learn how the CIDetectInfo structure contains identity information for baseline configuration item detection."
---

# CIDetectInfo Structure

# CIDetectInfo Structure
In Configuration Manager, the `CIDetectInfo` structure contains identity information for baseline configuration item detection.

## Syntax

```
struct CIDetectInfo
{
      LPWSTR szCIID;
      LPWSTR szVersion;
};
```

## Members
 szCIID
 ID of the configuration item.

 szVersion
 Version of the configuration item.

## See Also
 [Compliance Settings (DCM) Client Interfaces](../../../../../develop/reference/core/clients/client-classes/compliance-settings--dcm--client-interfaces.md)
