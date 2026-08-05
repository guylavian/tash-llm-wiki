---
title: "SMS_WindowsServicingBusinessReadyUpdates Class"
type: reference
domain: sccm
slug: develop-sms-windowsservicingbusinessreadyupdates-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/misc/sms_windowsservicingbusinessreadyupdates-server-wmi-class
family: develop
documentKind: "reference"
abstract: "An internal-only Windows Management Instrumentation class method."
---

# SMS_WindowsServicingBusinessReadyUpdates Class

# SMS_WindowsServicingBusinessReadyUpdates Server WMI Class
For internal use only.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_WindowsServicingBusinessReadyUpdates : SMS_BaseClass
{
     String UpdateID;
};

```

## Methods
 The  `SMS_WindowsServicingBusinessReadyUpdates` class does not define any methods.

## Properties
 `UpdateID`
 Data type: `String`

 Access type: Read

 Qualifiers: [key, not_null]

 Reserved for internal use.

## Remarks
 Class qualifiers for this class include:

- Dynamic

- Read (read-only)

- Secured

  For more information about both the class qualifiers and the property qualifiers included in the Properties section, see [Configuration Manager Class and Property Qualifiers](../../../develop/reference/misc/class-and-property-qualifiers.md).

## Requirements

### Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

### Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).
