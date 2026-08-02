---
title: "GetNextServiceWindowID Method"
type: reference
domain: sccm
slug: develop-getnextservicewindowid-method-in-class-ccm-servicewindowmanager
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/sdk/getnextservicewindowid-method-in-class-ccm_servicewindowmanager
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the GetNextServiceWindowID WMI class method gets the identifier of the next service window instance closest to the current time."
---

# GetNextServiceWindowID Method

# GetNextServiceWindowID Method in Class CCM_ServiceWindowManager
The `GetNextServiceWindowID` WMI class method, in Configuration Manager, gets the identifier of the next service window instance closest to the current time.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
uint32 GetNextServiceWindowID(
     [OUT] String NextServiceWindowID
);
```

#### Parameters
 `NextServiceWindowID`
 Data type: `String`

 Qualifiers: [out]

 Identifier of the next service window instance closest to the current time.

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
 [CCM_ServicewindowManager Client WMI Class](../../../../../develop/reference/core/clients/sdk/ccm_servicewindowmanager-client-wmi-class.md)
