---
title: "Sample queries for content management"
type: reference
domain: sccm
slug: develop-sample-queries-content-management-configuration-manager
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/core/understand/sqlviews/sample-queries-content-management-configuration-manager
family: develop
documentKind: "how-to"
abstract: "Sample queries that show how to join the most common content management views to other views."
---

# Sample queries for content management

# Sample queries for content management in Configuration Manager

The following sample queries demonstrate how to join the most common content management views to other views.

## Joining software distribution and package status views

The following query lists all packages by package ID and package name, the current status of each package, the Network Abstraction Layer (NAL) path for the distribution point, and the last time the package was refreshed on the distribution point. The **v_Package** view is joined to the **v_PackageStatusDetailSumm** status view and **v_DistributionPoint** software distribution view by using the **PackageID** columns.

```sql
    SELECT PCK.PackageID, PCK.Name as PackageName, PSD.Targeted, 
    PSD.Installed, PSD.Retrying, PSD.Failed, DP.ServerNALPath, 
    DP.LastRefreshTime 
    FROM v_Package PCK INNER JOIN v_PackageStatusDetailSumm PSD 
    ON PCK.PackageID = PSD.PackageID INNER JOIN v_DistributionPoint DP 
    ON PCK.PackageID = DP.PackageID 
    ORDER BY PCK.PackageID 
```

## See also

[Content management views in Configuration Manager](content-management-views-configuration-manager.md)
