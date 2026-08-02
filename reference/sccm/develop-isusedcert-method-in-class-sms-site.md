---
title: "IsUsedCert Method"
type: reference
domain: sccm
slug: develop-isusedcert-method-in-class-sms-site
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/isusedcert-method-in-class-sms_site
family: develop
documentKind: "reference"
abstract: "Learn how to use the IsUsedCert method to verify whether the specified certificate is used."
---

# IsUsedCert Method

# IsUsedCert Method in Class SMS_Site
The `IsUsedCert` Windows Management Instrumentation (WMI) class method, in Configuration Manager, verifies whether the specified certificate is used.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
Boolean IsUsedCert(
   String Certificate
);
```

#### Parameters
 `Certificate`
 Data type: `String`

 Qualifiers: [in]

 The certificate to check against the site.

## Return Values
 `true` if the specified certificate is used on the site; otherwise `false`.

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Site Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_site-server-wmi-class.md)
 [GetClientInfo Method in Class SMS_Site](../../../../../develop/reference/core/servers/configure/getclientinfo-method-in-class-sms_site.md)
