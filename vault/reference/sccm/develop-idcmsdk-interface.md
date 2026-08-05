---
title: "IDCMSDK Interface"
type: reference
domain: sccm
slug: develop-idcmsdk-interface
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/idcmsdk-interface
family: develop
documentKind: "reference"
abstract: "The interface represents the Desired Configuration Management SDK and defines methods used to perform operations on baseline configuration items."
---

# IDCMSDK Interface

# IDCMSDK Interface
The `IDCMSDK` interface, in Configuration Manager, represents the Desired Configuration Management SDK and defines methods used to perform operations on baseline configuration items. The interface inherits from `IDispatch`.

## In This Section
 The following table lists the methods in the `IDCMSDK` interface.

|Method|Description|
|------------|-----------------|
|[IDCMSDK::EvaluateBaseline](../../../../../develop/reference/core/clients/client-classes/idcmsdk--evaluatebaseline-method.md)|Runs discover operation for the provided configuration item ID.|
|[IDCMSDK::GetAssignedBaselines](../../../../../develop/reference/core/clients/client-classes/idcmsdk--getassignedbaselines-method.md)|Retrieves the assigned baseline configuration items.|
|[IDCMSDK::GetBaselineComplianceReport](../../../../../develop/reference/core/clients/client-classes/idcmsdk--getbaselinecompliancereport-method.md)|Retrieves the cached discovery report for the specified configuration item baseline.|
|[IDCMSDK::GetBaselineInfo](../../../../../develop/reference/core/clients/client-classes/idcmsdk--getbaselineinfo-method.md)|Retrieves the configuration item information for the specified configuration item baseline.|
|[IDCMSDK::SetEvaluationCallback](../../../../../develop/reference/core/clients/client-classes/idcmsdk--setevaluationcallback-method.md)|Retrieves an existing evaluation job by ID.|

## UUID
 The UUID for `IDCMSDK` is 08595CA8-6A42-4ce1-A1D6-8B6C2811A555.

## See Also
 [Compliance Settings (DCM) Client Interfaces](../../../../../develop/reference/core/clients/client-classes/compliance-settings--dcm--client-interfaces.md)
 [IDCMAgentCallback Interface](../../../../../develop/reference/core/clients/client-classes/idcmagentcallback-interface.md)
