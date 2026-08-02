---
title: "Resuscitate Method"
type: reference
domain: sccm
slug: develop-resuscitate-method-in-class-sms-migrationsitemapping
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/migration/resuscitate-method-in-class-sms_migrationsitemapping
family: develop
documentKind: "reference"
abstract: "Learn how the Resuscitate Windows Management Instrumentation (WMI) class method, in Configuration Manager, resuscitates site mapping."
---

# Resuscitate Method

# Resuscitate Method in Class SMS_MigrationSiteMapping
The `Resuscitate` Windows Management Instrumentation (WMI) class method, in Configuration Manager, resuscitates site mapping.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 Resuscitate();
```

#### Parameters
 None.

## Return Values
 An  `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_MigrationJob Server WMI Class](../../../../develop/reference/core/migration/sms_migrationjob-server-wmi-class.md)
