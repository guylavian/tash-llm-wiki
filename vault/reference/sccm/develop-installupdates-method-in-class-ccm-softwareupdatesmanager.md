---
title: "InstallUpdates Method"
type: reference
domain: sccm
slug: develop-installupdates-method-in-class-ccm-softwareupdatesmanager
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/sdk/installupdates-method-in-class-ccm_softwareupdatesmanager
family: develop
documentKind: "reference"
abstract: "A Windows Management Instrumentation class method that installs software updates, which have been deployed to the client computer."
---

# InstallUpdates Method

# InstallUpdates Method in Class CCM_SoftwareUpdatesManager
The `InstallUpdates` WMI class method, in Configuration Manager, installs software updates that have been deployed to the client computer.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
UInt32 InstallUpdates(
     [IN]  CCM_SoftwareUpdate CCMUpdates[]
);
```

#### Parameters
 `CCMUpdates[]`
 Data type: `CCM_SoftwareUpdate`

 Qualifiers: [in]

 Array of software updates that are installed.

## Return Values
 A `UInt32` data type that is 0 to indicate success or nonzero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Client Runtime Requirements](../../../../../develop/core/reqs/client-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Client Development Requirements](../../../../../develop/core/reqs/client-development-requirements.md).

## See Also
 [CCM_SoftwareUpdatesManager Client WMI Class](../../../../../develop/reference/core/clients/sdk/ccm_softwareupdatesmanager-client-wmi-class.md)
