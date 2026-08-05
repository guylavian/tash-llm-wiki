---
title: "Sample queries for client status"
type: reference
domain: sccm
slug: develop-sample-queries-client-status-configuration-manager
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/core/understand/sqlviews/sample-queries-client-status-configuration-manager
family: develop
documentKind: "how-to"
abstract: "Sample queries that show how to join common client status views to other views."
---

# Sample queries for client status

# Sample queries for client status in Configuration Manager

The following sample queries demonstrate how to join common client status views to other views.

## Joining client status and collection views

This query lists each client computer in the site, the last time it requested policy, and the collections to which the computer belongs. The query uses the **v_CH_PolicyRequestHistory** view to read the last policy request time and joins, using the **ResourceID** column to the **v_ClientCollectionMembers** view.

```sql
    SELECT        dbo.CH_PolicyRequestHistory.MachineID AS ResourceID, dbo.CH_PolicyRequestHistory.RequestTime, dbo.v_ClientCollectionMembers.CollectionID
    FROM            dbo.CH_PolicyRequestHistory INNER JOIN
                             dbo.v_ClientCollectionMembers ON dbo.CH_PolicyRequestHistory.MachineID = dbo.v_ClientCollectionMembers.ResourceID
```

## See also

[Client status views in Configuration Manager](client-status-views-configuration-manager.md)
