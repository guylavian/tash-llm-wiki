---
title: "Sample queries for application management"
type: reference
domain: sccm
slug: develop-sample-queries-application-management-configuration-manager
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/core/understand/sqlviews/sample-queries-application-management-configuration-manager
family: develop
documentKind: "how-to"
abstract: "Sample queries that show how to join the most common application management views to other views."
---

# Sample queries for application management

# Sample queries for application management in Configuration Manager

The following sample queries demonstrate how to join the most common application management views to other views.

## Joining package and program deployment and collection views

The following query lists all package and program deployments by advertisement ID, advertisement name, and the collection that was targeted for the deployment. The **v_Advertisement** view is joined to the **v_Collection** view by using the **AdvertisementID** column.

```sql
    SELECT ADV.AdvertisementID, ADV.AdvertisementName, 
    COL.CollectionID, COL.Name as CollectionName 
    FROM v_Advertisement ADV INNER JOIN v_Collection COL 
    ON ADV.CollectionID = COL.CollectionID 
    ORDER BY ADV.AdvertisementID 
```

## See also

[Application management views in Configuration Manager](application-management-views-configuration-manager.md)
