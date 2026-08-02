---
title: "CCM_DownloadProvider Class"
type: reference
domain: sccm
slug: develop-ccm-downloadprovider-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/ccm_downloadprovider-wmi-class
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the CCM_DownloadProvider class defines and registers an Alternate Content Provider (ACP)."
---

# CCM_DownloadProvider Class

# CCM_DownloadProvider WMI Class
The **CCM_DownloadProvider** class, in Configuration Manager, defines and registers an Alternate Content Provider (ACP). It's a non-Microsoft download plug-in that  the Configuration Manager client can use to download content. The provider must be registered on the client by using this class before it can be used.

## Syntax
```
class CCM_DownloadProvider: CCM_Policy
{
    string  LogicalName;
    string  CLSID;
    uint32  Priority;
    String  GlobalSettings;
    string  Reserved;
};

```

#### Parameters
 `LogicalName`
 Data type: String

 Qualifiers: [in, RealKey, NotNull: ToInstance ToSubClass]

 The name of the non-Microsoft provider. This field must match the value specified to the SMS provider.

 `CLSID`
 Data type: String

 Qualifiers: [in, NotNull: ToInstance, ToSubClass]

 The COM class ID corresponding to the interface implementation.

 `Priority`
 Data type: String

 Qualifiers: [in, NotNull: ToInstance ToSubClass]

 Priority in the face of multiple alternate provider choices. For future use. Must be nonzero.

 `GlobalSettings`
 Data type: String

 Qualifiers: [in]

 Provider specific data. Use this property for any client-wide configuration for the provider.

  `PolicySource`  
 Data type: String  

 Qualifiers: [in]  

 The source of the policy, typically "Local" when the instance is created on a client in the root\ccm\policy\machine\RequestedConfig namespace. Not available in root\ccm\policy\machine\ActualConfig namespace that contains compiled policy.

 `Reserved`
 Data type: String

 Qualifiers: [in]

 Reserved for future use.

## Return Values
 None.

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Client Runtime Requirements](../../../../../develop/core/reqs/client-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Client Development Requirements](../../../../../develop/core/reqs/client-development-requirements.md).
