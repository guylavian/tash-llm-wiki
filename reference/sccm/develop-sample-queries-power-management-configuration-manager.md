---
title: "Sample queries for power management"
type: reference
domain: sccm
slug: develop-sample-queries-power-management-configuration-manager
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/core/understand/sqlviews/sample-queries-power-management-configuration-manager
family: develop
documentKind: "how-to"
abstract: "Sample queries that show how to join power management views to other views."
---

# Sample queries for power management

# Sample queries for power management in Configuration Manager

The following sample queries demonstrate how to join power management views to other views.

## Joining power management views to discovery views

The following query lists all computers, by Netbios name, that are excluded from power management because the user chose to exclude them.

The query returns the Netbios name and the domain of the computer and also the client opt-out setting where this value is 1 (indicating that the computer has been excluded from power management).

```sql
    SELECT        v_R_System.Name0, v_R_System.Resource_Domain_OR_Workgr0, 
                             v_GS_POWER_MANAGEMENT_CLIENTOPTOUT_SETTINGS.IsClientOptOut0
    FROM            v_R_System INNER JOIN
                             v_GS_POWER_MANAGEMENT_CLIENTOPTOUT_SETTINGS ON 
                             v_R_System.ResourceID = v_GS_POWER_MANAGEMENT_CLIENTOPTOUT_SETTINGS.ResourceID
    WHERE        (v_GS_POWER_MANAGEMENT_CLIENTOPTOUT_SETTINGS.IsClientOptOut0 = 1)
```

## See also

[Power management views in Configuration Manager](power-management-views-configuration-manager.md)
