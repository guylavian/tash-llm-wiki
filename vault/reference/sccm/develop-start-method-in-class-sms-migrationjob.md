---
title: "Start Method"
type: reference
domain: sccm
slug: develop-start-method-in-class-sms-migrationjob
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/migration/start-method-in-class-sms_migrationjob
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the Start Windows Management Instrumentation class method starts the migration job."
---

# Start Method

# Start Method in Class SMS_MigrationJob
The `Start` Windows Management Instrumentation (WMI) class method, in Configuration Manager, starts the migration job.

> [!IMPORTANT]
>  This requires the Manage Migration Job right.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 Start();
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
