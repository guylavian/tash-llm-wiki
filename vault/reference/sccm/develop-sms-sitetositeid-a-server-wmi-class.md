---
title: "SMS_SiteToSiteID_a Class"
type: reference
domain: sccm
slug: develop-sms-sitetositeid-a-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/sms_sitetositeid_a-server-wmi-class
family: develop
documentKind: "reference"
abstract: "Learn how to relate an SMS Site Server object with an SMS Identification Server object using SMS_SiteToSiteID_a."
---

# SMS_SiteToSiteID_a Class

# SMS_SiteToSiteID_a Server WMI Class
The `SMS_SiteToSiteID_a` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that relates an [SMS_Site Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_site-server-wmi-class.md) object with an [SMS_Identification Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_identification-server-wmi-class.md) object representing identifying information for the site.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_SiteToSiteID_a : SMS_BaseAssociation
{
      ref:SMS_Site site;
      ref:SMS_Identification siteIdentification;
};
```

## Methods
 The `SMS_SiteToSiteID_a` class does not define any methods.

## Properties
 `site`
 Data type: `ref:SMS_site`

 Access type: Read/Write

 Qualifiers: [key]

 Reference to an [SMS_Site Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_site-server-wmi-class.md) object path for the site.

 `siteIdentification`
 Data type: `ref:SMS_Identification`

 Access type: Read/Write

 Qualifiers: [key]

 Reference to an [SMS_Identification Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_identification-server-wmi-class.md) object path for the site identification.

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
