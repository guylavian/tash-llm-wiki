---
title: "CCM_InstalledDeploymentType Class"
type: reference
domain: sccm
slug: develop-ccm-installeddeploymenttype-client-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/sdk/ccm_installeddeploymenttype-client-wmi-class
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the CCM_InstalledDeploymentType Windows Management Instrumentation class is an SMS Provider server class that represents an installed deployment type."
---

# CCM_InstalledDeploymentType Class

# CCM_InstalledDeploymentType Client WMI Class
The `CCM_InstalledDeploymentType` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents an installed deployment type.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class CCM_InstalledDeploymentType :
{
    String Id;
    String Revision;
};
```

## Methods
 The `CCM_InstalledDeploymentType` class does not define any methods.

## Properties
 `Id`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: [key]

 Identifier.

 `Revision`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: [key]

 Revision.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
