---
title: "Evaluation of the All collections report"
type: reference
domain: sccm
slug: develop-evaluation-all-collections-report-configuration-manager
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/core/understand/sqlviews/evaluation-all-collections-report-configuration-manager
family: develop
documentKind: "article"
abstract: "Information about all of the collections in the Configuration Manager hierarchy."
---

# Evaluation of the All collections report

# Evaluation of the All collections report in Configuration Manager

The **All collections** report is one of the built-in reports in Configuration Manager and is a good example of a basic report. This report lists all of the collections in the Configuration Manager hierarchy.

To open the report, use the following procedure:

## To examine the properties of the All collections report

1. In the Configuration Manager console, select **Monitoring**.
1. In the **Monitoring** workspace, expand **Reporting**, and then select **Reports**.
1. From the list of reports, select **All collections** and then, in the **Home** tab, in the **Report Group** group, select **Edit**.
1. In the **Report Data** pane of Report Builder, expand **Datasets** and then double-click **DataSet0**.
1. In the **Dataset Properties** dialog box, you can view the SQL query for the report, the fields that will be returned, and the parameters that the report uses.
1. Close the **Dataset Properties** dialog box.
1. Close Report Builder.

## See also

[Evaluation of the computer information for a specific computer report in Configuration Manager](evaluation-computer-information-report-configuration-manager.md)
