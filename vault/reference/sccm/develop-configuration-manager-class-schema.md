---
title: "Configuration Manager Class Schema"
type: reference
domain: sccm
slug: develop-configuration-manager-class-schema
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/core/understand/configuration-manager-class-schema
family: develop
documentKind: "article"
abstract: "Learn how to use Windows Management Instrumentation (WMI) classes that represent the objects in SMS as templates for managed objects."
---

# Configuration Manager Class Schema

# Configuration Manager Class Schema
The Systems Management Server (SMS) class schema is a set of Windows Management Instrumentation (WMI) classes that represent the objects in SMS. Each SMS class is a template for a managed object and all instances of the object use the template. Classes can contain properties and methods: the properties describe the class data and the methods typically perform data management for the class.

## Class categories

The following table describes the categories of classes and how the classes are used.

|Category|Description|
|--------------|-----------------|
|Server|Classes supported on servers running SMS.|
|Advanced Client|Classes supported on SMS Advanced Clients.|

## See also

- [Date and Time Formats](../../../develop/core/understand/date-and-time-formats.md)

- [Interpreting Bitfield Properties](../../../develop/core/understand/interpreting-bitfield-properties.md)

- [Lazy Properties](../../../develop/core/understand/lazy-properties.md)

- [SMS Provider Field Length Restrictions](../../../develop/core/understand/sms-provider-field-length-restrictions.md)
