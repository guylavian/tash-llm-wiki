---
title: "GetPortalUrlValue Method"
type: reference
domain: sccm
slug: develop-getportalurlvalue-method-in-class-ccm-softwarecatalogutilities
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/sdk/getportalurlvalue-method-in-class-ccm_softwarecatalogutilities
family: develop
documentKind: "reference"
abstract: "Learn how the GetPortalUrlValue Windows Management Instrumentation (WMI) class method in Configuration Manager that returns the portal url for a client."
---

# GetPortalUrlValue Method

# GetPortalUrlValue Method in Class CCM_SoftwareCatalogUtilities
The `GetPortalUrlValue` Windows Management Instrumentation (WMI) class method in Configuration Manager that returns the portal url for a client.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
uint32 GetPortalUrlValue
{
    [OUT]   String PortalUrl
};
```

## Parameters
 `PortalUrl`
 Data type: `String`

 Qualifiers: [id("0"), out]

 Portal url.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
