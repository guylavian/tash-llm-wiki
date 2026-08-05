---
title: "Databases within this farm are set to read only and will fail to upgrade unless it's set to a read-write state (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: Databases within this farm are set to read only and will fail to upgrade unless it's set to a read-write state, for SharePoint Server."
ms.topic: troubleshooting
---
Note

Databases within this farm are set to read only and will fail to upgrade unless it's set to a read-write state (SharePoint Server)

# Databases within this farm are set to read only and will fail to upgrade unless it's set to a read-write state (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Databases within this farm are set to read only and will fail to upgrade unless it's set to a read-write state.

**Summary:** The databases are set to read-only and can't be upgraded.

**Cause:** The databases are set to read-only.

**Resolution: Set the databases to read-write using SQL Server.**

Verify that the user account that is performing this procedure is a member of the **db_owner** fixed database role in each database.

Start SQL Server Management Studio.

Right-click the content database that you want to make read-only, and then click **Properties**.

Select the **Options** page, and, in the **Other options** list, scroll to the **State** section.

In the **Database Read-Only** row, click the arrow next to **True**, select **False**, and then click **OK**.

Repeat for all other content databases.

Note

When a database is set to read-only, all connections except the one that is setting the read-only flag are stopped. After the read-only flag is set, other connections are enabled.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
