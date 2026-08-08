---
title: "IDCMAgentCallback::NotifyError"
type: reference
domain: sccm
slug: develop-idcmagentcallback-notifyerror-method
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/idcmagentcallback--notifyerror-method
family: develop
documentKind: "reference"
abstract: "Learn how to notify the caller that a Desired Configuration Management Agent job has failed to be completed using IDCMAgentCallback::NotifyError."
---

# IDCMAgentCallback::NotifyError

# IDCMAgentCallback::NotifyError Method
The `IDCMAgentCallback::NotifyError` method, in Configuration Manager, notifies the caller that a Desired Configuration Management Agent job has failed to be completed.

## Syntax

```
[IDL]
HRESULT NotifyError(
     IDCMAgentJob* pJob,
     HRESULT hrError,
     MessageId msgId
);
```

#### Parameters
 `pJob`
 Data type: `IDCMAgentJob`

 Qualifiers: [in]

 Pointer to the `IDCMAgentJob` object representing the configuration items and their progress.

 `hrError`
 Data type: `HRESULT`

 Qualifiers: [in]

 `HRESULT` code representing the error.

 `msgId`
 Data type: `MessageId`

 Qualifiers: [in]

 Nothing is returned for this parameter.

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
