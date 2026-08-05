---
title: "Query2"
type: reference
domain: sccm
slug: develop-query2
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/osd/query2
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, Query2 specifies a query that is used to identify the platform that a client computer is running. This information should come from SMS_SupportedPlatforms Server WMI class objects and match the platform information specified in the PlatformApplicabilityCondition node."
---

# Query2

# Query2
`Query2` specifies a query, in Configuration Manager, that is used to identify the platform that a client computer is running.

> [!NOTE]
>  This information should come from `SMS_SupportedPlatforms Server WMI Class` objects and match the platform information specified in the PlatformApplicabilityCondition node.

 The query is run on the client computer and typically inspects Windows Management Instrumentation (WMI) to determine the client platform. For example, `SELECT * FROM Win32_Processor WHERE Architecture=9 AND DataWidth=64`.

 **Type**: Element.

 **Instances**: One.

## Attributes
 None

## See Also
 [Operating System Deployment Driver Supported Platforms Schema](../../../develop/reference/osd/operating-system-deployment-driver-supported-platforms-schema.md)
 [PlatformApplicabilityCondition](../../../develop/reference/osd/platformapplicabilitycondition.md)
 [Query1](../../../develop/reference/osd/query1.md)
