---
title: "How to view the SQL Statement for reports"
type: reference
domain: sccm
slug: develop-how-to-view-sql-statement-configuration-manager-reports
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/core/understand/sqlviews/how-to-view-sql-statement-configuration-manager-reports
family: develop
documentKind: "how-to"
abstract: "Information to find out what SQL statement is used in a Configuration Manager report."
---

# How to view the SQL Statement for reports

# How to view the SQL statement for Configuration Manager reports

Reports in Configuration Manager can be based on simple SQL statements or very complex ones that prompt the user for information, join several Microsoft SQL Server views, and use filters to limit the results. Use the following procedure to find out what SQL statement is used in a Configuration Manager report.

## To view the SQL statement for a report

1. In the Configuration Manager console, select **Monitoring**.
1. In the **Monitoring** workspace, expand **Reporting**, and then select **Reports**.
1. Select the report for which you want to view the SQL statement and then, in the **Home** tab, in the **Report Group** group, select **Edit**.
1. The Report Builder window opens. In the **Report Data** pane, expand **Datasets** to view the data sets for the report.
1. Double-click a dataset to open the **Dataset Properties** dialog box.

   The first dataset is typically (but not always), the main SQL statement for the report. Other datasets might contain the SQL statements that can be used to present a list of items for a user to choose from, such as a list of computers.
1. You can view and modify the SQL statement for the dataset in the **Query** field.
1. Close the **Dataset Properties** dialog box.
1. Close Report Builder.

## See also

[How to modify Configuration Manager reports](how-to-modify-configuration-manager-reports.md)
