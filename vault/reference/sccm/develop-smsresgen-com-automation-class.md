---
title: "SMSResGen COM Automation Class"
type: reference
domain: sccm
slug: develop-smsresgen-com-automation-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/smsresgen-com-automation-class
family: develop
documentKind: "reference"
abstract: "Use the SMSResGen COM class to automate the creation of a data discovery record (DDR)."
---

# SMSResGen COM Automation Class

# SMSResGen COM Automation Class
The `SMSResGen` COM class in Configuration Manager is used to create data discovery records (DDRs).

## Methods

|Name|Description|
|----------|-----------------|
|[ISMSResGen Interface](../../../../../develop/reference/core/servers/configure/ismsresgen-interface.md)|Defines the data discovery record methods.|

## Remarks
`SMSResGen` is found in SMSResGenCtl.dll. Use the [ISMSResGen Interface](../../../../../develop/reference/core/servers/configure/ismsresgen-interface.md) interface to create and use DDRs.

> [!IMPORTANT]
>  The latest version of SMSRsGenCtl.dll is available from NuGet:
>
> - [Microsoft.ConfigurationManagement.SMSRsGenCtl.i386](https://www.nuget.org/packages/Microsoft.ConfigurationManagement.SMSRsGenCtl.i386/)
>
> - [Microsoft.ConfigurationManagement.SMSRsGenCtl.amd64](https://www.nuget.org/packages/Microsoft.ConfigurationManagement.SMSRsGenCtl.amd64/)


Because the `SMSResGen` control is not thread safe, do not try to create more than one instance of this class.

> [!IMPORTANT]
> The function `DDRSendToSMS`, available in previous releases of the SDK and in versions of `SMSRsGen.dll`/`SMSResGenCtl.dll`, has been deprecated and should not be used with Configuration Manager.

The CLSID for `SMSResGen` is 19352BAD-BEE0-4193-95C4-588B6C5DBCD1.

## Requirements

### Runtime Requirements
smsrsgenctl.dll

smsrsgen.dll

For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

### Development Requirements
For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
[ISMSResGen Interface](../../../../../develop/reference/core/servers/configure/ismsresgen-interface.md)
