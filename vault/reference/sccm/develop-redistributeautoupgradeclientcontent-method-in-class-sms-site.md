---
title: "RedistributeAutoUpgradeClientContent Method"
type: reference
domain: sccm
slug: develop-redistributeautoupgradeclientcontent-method-in-class-sms-site
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/redistributeautoupgradeclientcontent-method-in-class-sms_site
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the RedistributeAutoUpgradeClientContent WMI class method redistributes auto-upgrade client content to the specified distribution point."
---

# RedistributeAutoUpgradeClientContent Method

# RedistributeAutoUpgradeClientContent Method in Class SMS_Site
The `RedistributeAutoUpgradeClientContent` Windows Management Instrumentation (WMI) class method, in Configuration Manager, redistributes auto-upgrade client content to the specified distribution point.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 RedistributeAutoUpgradeClientContent(
     String DPNALPath
);
```

#### Parameters
 `DPNALPath`
 Data type: `String`

 Qualifiers: [in]

 Distribution point NAL path.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Site Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_site-server-wmi-class.md)
