---
title: "IDCMAgentCallback::NotifyComplete"
type: reference
domain: sccm
slug: develop-idcmagentcallback-notifycomplete-method
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/idcmagentcallback--notifycomplete-method
family: develop
documentKind: "reference"
abstract: "The IDCMAgentCallback::NotifyComplete method, in Configuration Manager, notifies the caller that a Desired Configuration Management Agent job has completed."
---

# IDCMAgentCallback::NotifyComplete

# IDCMAgentCallback::NotifyComplete Method
The `IDCMAgentCallback::NotifyComplete` method, in Configuration Manager, notifies the caller that a Desired Configuration Management Agent job has completed.

## Syntax

```
[IDL]
HRESULT NotifyComplete(
     IDCMAgentJob* pJob
);
```

#### Parameters
 `pJob`
 Data type: `IDCMAgentJob`

 Qualifiers: [in]

 Pointer to the `IDCMAgentJob` object representing the configuration items and their progress.

## Return Values
 An `HRESULT` code. Possible values include, but aren't limited to, the following one:

 S_OK
 The method succeeded. All other return values indicate failure.

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Client Runtime Requirements](../../../../../develop/core/reqs/client-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Client Development Requirements](../../../../../develop/core/reqs/client-development-requirements.md).

## See Also
 [IDCMAgentCallback Interface](../../../../../develop/reference/core/clients/client-classes/idcmagentcallback-interface.md)
