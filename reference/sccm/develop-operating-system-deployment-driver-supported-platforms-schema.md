---
title: "OS Deployment Driver Supported Platforms Schema"
type: reference
domain: sccm
slug: develop-operating-system-deployment-driver-supported-platforms-schema
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/osd/operating-system-deployment-driver-supported-platforms-schema
family: develop
documentKind: "reference"
abstract: "Learn how to use the OS Deployment Driver Supported Platforms Schema to check which operating systems are compatible."
---

# OS Deployment Driver Supported Platforms Schema

# Operating System Deployment Driver Supported Platforms Schema
The following reference section documents the XML schema that is used to specify the platforms that are supported by an operating system deployment driver in Microsoft Configuration Manager.

 The schema is used in the `SMS_Driver` class `SDMPackageXML` property.

> [!CAUTION]
>  The supported platforms portion of `SDMPackageXML` is the only part of the Driver XML schema that can be edited. You should not make changes to other parts of the XML.

## Supported Platform XML
 \<[PlatformApplicabilityConditions](../../../develop/reference/osd/platformapplicabilityconditions.md)>

 \<[PlatformApplicabilityCondition](../../../develop/reference/osd/platformapplicabilitycondition.md)>

 \<[Query1](../../../develop/reference/osd/query1.md)>\</Query1>

 \<[Query2](../../../develop/reference/osd/query2.md)>\</Query2>

 \</PlatformApplicabilityCondition>

 \</PlatformApplicabilityConditions>

## See Also
 [Operating System Deployment Driver Supported Platforms Schema](../../../develop/reference/osd/operating-system-deployment-driver-supported-platforms-schema.md)
 [PlatformApplicabilityCondition](../../../develop/reference/osd/platformapplicabilitycondition.md)
 [Query1](../../../develop/reference/osd/query1.md)
 [Query2](../../../develop/reference/osd/query2.md)
