---
title: "GetDependency method"
type: reference
domain: sccm
slug: develop-getdependency-method-in-class-sms-collection
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/collections/getdependency-method-in-class-sms_collection
family: develop
documentKind: "reference"
abstract: "Get the collection relationship info which the input collection depends on."
---

# GetDependency method

# GetDependency method in class SMS_Collection

Starting in version 2010, the `GetDependency` WMI class method in Configuration Manager gets the collection relationship info which the input collection depends on.

The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```MOF
sint32 GetDependency(
    string Relationship[]
);
```

## Parameters

### `Relationship`

Data type: `String[]` (array)

Qualifiers: [out]

JSON string array of collection dependency relationship.

## Return values

An `SInt32` data type that is `0` to indicate success, or non-zero to indicate failure.

For more information about handling returned errors, see [About Configuration Manager errors](../../../../core/understand/about-configuration-manager-errors.md).

## Requirements

### Runtime requirements

For more information, see [Configuration Manager server runtime requirements](../../../../core/reqs/server-runtime-requirements.md).

### Development requirements

For more information, see [Configuration Manager server development requirements](../../../../core/reqs/server-development-requirements.md).

## See also

[SMS_Collection server WMI class](sms_collection-server-wmi-class.md)

[GetDependent method](getdependent-method-in-class-sms_collection.md)
