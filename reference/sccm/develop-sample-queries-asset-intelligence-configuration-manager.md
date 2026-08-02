---
title: "Sample queries for asset intelligence"
type: reference
domain: sccm
slug: develop-sample-queries-asset-intelligence-configuration-manager
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/core/understand/sqlviews/sample-queries-asset-intelligence-configuration-manager
family: develop
documentKind: "how-to"
abstract: "Sample queries that show how to join the most common Asset Intelligence views to other views."
---

# Sample queries for asset intelligence

# Sample queries for asset intelligence in Configuration Manager

The following sample queries demonstrate how to join the most common Asset Intelligence views to other views.

## Joining asset intelligence views

The following sample query demonstrates how to join asset intelligence views to asset intelligence hardware inventory and discovery views. Most often, the asset intelligence hardware inventory views will be used when creating asset intelligence reports for resources and joined to other views by using the **ResourceID** column. The asset intelligence views can be joined to the asset intelligence hardware inventory views to list product information by using the **SoftwareCode** column.

This sample query lists the publisher, product, installation date, and installation path for software identified during a hardware inventory on the Workstation1 computer. The query results are sorted by the latest installation date and then product name. The query joins the **v_GS_INSTALLED_SOFTWARE** asset intelligence hardware inventory view to the **v_LU_SoftwareCode** asset intelligence view by using the **SoftwareCode0** and **SoftwareCode** columns, respectively, and then joins the asset intelligence views, **v_LU_SoftwareList** and **v_LU_SoftwareCode** by using the **SoftwareID** columns. Finally, the query joins the **v_GS_INSTALLED_SOFTWARE** view with the **v_R_System** discovery view by using the **ResourceID** column. A LEFT OUTER JOIN is used when joining the views to display only information contained in the **v_GS_INSTALLED_SOFTWARE** view.

```sql
    SELECT v_LU_SoftwareList.CommonPublisher AS Publisher, 
      v_LU_SoftwareList.CommonName AS [Product Name], 
      v_LU_SoftwareList.CommonVersion AS Version, 
      v_GS_INSTALLED_SOFTWARE.InstallDate0 AS [Install Date], 
      v_GS_INSTALLED_SOFTWARE.InstalledLocation0 AS Path 
    FROM v_GS_INSTALLED_SOFTWARE LEFT OUTER JOIN v_LU_SoftwareCode ON 
      v_GS_INSTALLED_SOFTWARE.SoftwareCode0 = v_LU_SoftwareCode.SoftwareCode INNER JOIN v_LU_SoftwareList ON
	  v_LU_SoftwareList.SoftwareID = v_LU_SoftwareCode.SoftwareID LEFT OUTER JOIN v_R_System ON
	  v_GS_INSTALLED_SOFTWARE.ResourceID = v_R_System.ResourceID
	WHERE (v_R_System.Netbios_Name0 LIKE 'Workstation1') 
    ORDER BY [Install Date] DESC, [Product Name] 
```

## See also

[Asset intelligence views in Configuration Manager](asset-intelligence-views-configuration-manager.md)
