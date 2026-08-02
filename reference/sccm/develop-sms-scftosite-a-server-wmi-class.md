---
title: "SMS_SCFToSite_a Class"
type: reference
domain: sccm
slug: develop-sms-scftosite-a-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/sms_scftosite_a-server-wmi-class
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the SMS_SCFToSite_a WMI class is an SMS Provider server class that uses the SiteCode property to relate SMS_SiteControlFile Server WMI Class objects to SMS_Site Server WMI Class objects."
---

# SMS_SCFToSite_a Class

# SMS_SCFToSite_a Server WMI Class
The `SMS_SCFToSite_a` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that uses the `SiteCode` property to relate [SMS_SiteControlFile Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_sitecontrolfile-server-wmi-class.md) objects to [SMS_Site Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_site-server-wmi-class.md) objects.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_SCFToSite_a : SMS_BaseAssociation
{
      ref:SMS_Site Site;
      ref:SMS_SiteControlFile SiteControlFile;
};
```

## Properties
 `Site`
 Data type: `ref:SMS_Site`

 Access type: Read/Write

 Qualifiers: [key]

 Reference to an [SMS_Site Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_site-server-wmi-class.md) object path.

 `SiteControlFile`
 Data type: `ref:SMS_SiteControlFile`

 Access type: Read/Write

 Qualifiers: [key]

 Reference to an [SMS_SiteControlFile Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_sitecontrolfile-server-wmi-class.md)object path.

## Remarks
 Class qualifiers for this class include:

- Association: ToInstance

- Read (read-only)

  For more information about both the class qualifiers and the property qualifiers included in the Properties section, see [Configuration Manager Class and Property Qualifiers](../../../../../develop/reference/misc/class-and-property-qualifiers.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [Configuration Manager Site Configuration Server WMI Classes](../../../../../develop/reference/core/servers/configure/site-configuration-server-wmi-classes.md)
