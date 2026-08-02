---
title: "ICCMEvent::Submit Method"
type: reference
domain: sccm
slug: develop-iccmevent-submit-method
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/manage/iccmevent--submit-method
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the ICCMEvent::Submit method submits an event to Windows Management Instrumentation."
---

# ICCMEvent::Submit Method

# ICCMEvent::Submit Method
In Configuration Manager, the `ICcmEvent::Submit` method submits an event to Windows Management Instrumentation (WMI).

## Syntax

```
[C++]
HRESULT ICcmEvent::Submit();
```

#### Parameters
 None.

## Return Values
 An `HRESULT` code. Possible values include, but are not limited to, the following:

 S_OK
 The method succeeded.

## Requirements
 Smscore.dll.

## Runtime Requirements
 For more information, see [Configuration Manager Client Runtime Requirements](../../../../../develop/core/reqs/client-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Client Development Requirements](../../../../../develop/core/reqs/client-development-requirements.md).

## See Also
 [SMSEvent Class (client)](../../../../../develop/reference/core/servers/manage/smsevent-class.md)
