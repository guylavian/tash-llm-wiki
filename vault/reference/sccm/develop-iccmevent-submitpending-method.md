---
title: "ICCMEvent::SubmitPending Method"
type: reference
domain: sccm
slug: develop-iccmevent-submitpending-method
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/manage/iccmevent--submitpending-method
family: develop
documentKind: "reference"
abstract: "Learn how to submit an event that is stored by Windows Management Instrumentation (WMI) using the ICcmEvent::SubmitPending method."
---

# ICCMEvent::SubmitPending Method

# ICCMEvent::SubmitPending Method
In Configuration Manager, the `ICcmEvent::SubmitPending` method submits an event that is stored by Windows Management Instrumentation (WMI).

## Syntax

```
[C++]
HRESULT ICcmEvent::SubmitPending(
      BSTR bstrEventID,
      long lFlags
);
```

#### Parameters
 `bstrEventID`
 Data type: `BSTR`

 Qualifiers: [in, optional, defaultvalue("0")]

 Reserved. Must be `null`.

 `lFlags`
 Data type: `long`

 Qualifiers: [in, optional, defaultvalue(0)]

 Reserved. Must be zero.

## Return Values
 An `HRESULT` code. Possible values include, but aren't limited to, the following one:

 S_OK
 The method succeeded.

## Remarks
 Your application should use this method instead of the [Submit method](../../../../../develop/reference/core/servers/manage/iccmevent--submit-method.md) in situations where the Configuration Manager Agent Host (CCMEXEC) service might not be running. Instead of directly calling CCMEXEC to submit the event, this method stores it in WMI. If the service is running, the event is picked up immediately and issued. Otherwise, it's issued the next time the service starts.

## Requirements
 Smscore.dll.

## Runtime Requirements
 For more information, see [Configuration Manager Client Runtime Requirements](../../../../../develop/core/reqs/client-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Client Development Requirements](../../../../../develop/core/reqs/client-development-requirements.md).

## See Also
 [SMSEvent Class (client)](../../../../../develop/reference/core/servers/manage/smsevent-class.md)
 [Submit method](../../../../../develop/reference/core/servers/manage/iccmevent--submit-method.md)
