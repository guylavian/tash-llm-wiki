---
title: "Run a farm that uses read-only databases in SharePoint Server - SharePoint Server"
description: "Learn how to run a read-only SharePoint Server farm with some or all databases set as read-only."
ms.topic: how-to
---
Note

Run a farm that uses read-only databases in SharePoint Server

# Run a farm that uses read-only databases in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can use Microsoft PowerShell or SQL Server tools to set your SharePoint Server databases to read-only. The tool that you use depends on the kind of environment that you have deployed, your schedule requirements, and service level agreements that you have made with your organization.

Before you begin

## Before you begin

Before you begin this operation, review the following information about the settings that make a read-only farm.

A farm is considered read-only if one of the following is true:

All content databases are set to read-only.

Service application databases are set to read-only.

Note

The Search service application does not function when its databases are set as read-only.

The functionality and user experience in a read-only farm depends on the databases that are set to read-only.

Note

A farm that uses read-only content and service application databases is likely to be part of a disaster recovery environment or a highly available maintenance, update, or upgrade environment.

Prepare users for the read-only experience

## Prepare users for the read-only experience

If you plan to give users access to a read-only site or farm, you should set expectations for tasks that users can complete on the site and the behavior of the user interface (UI).

Sites that use read-only content databases

### Sites that use read-only content databases

The user experience of a site that uses a content database that is set to read-only is characterized by the following:

A statement at the top of the home page states that the site is read-only.

Common tasks that do not require writing to the content database are fully available.

Common tasks that require writing to the content database are not available either because the UI for the task is not available or because the user cannot apply changes to complete the task.

Some common tasks that require writing to the content database and that appear to be available return errors.

Farms that use read-only service application databases

### Farms that use read-only service application databases

The user experience on a farm that uses service application databases that are set to read-only is characterized by the following:

Common tasks that do not require writing to the service databases are fully available.

All common tasks that require writing to the service databases and that appear to be available return errors.

Set content databases to read-only

## Set content databases to read-only

Before you set content databases to read-only, you may need to determine the content database that is associated with a particular site collection.

**To determine the content database that is associated with a site collection by using PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Get-SPContentDatabase -Site <Site URL>
```

Where:

- *<Site URL>* is the site collection URL for which you want to know the associated content database.

The command returns the content database that is associated with the site.

For more information, see Get-SPContentDatabase.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

You can follow these steps to set read/write content databases to be read-only by using SQL Server Management Studio. You can also use the  `Transact-SQL ALTER DATABASE` statement to set content databases to be read-only. For more information, see ALTER DATABASE (Transact-SQL).

Important

Do not perform this procedure on databases in a failover environment that were log-shipped or mirrored. If a database in a failover environment that is either log-shipped or mirrored is set as read-only then no updates are performed and the backup is not valid.

**To set content databases to read-only by using SQL Server**

Verify that the user account that is performing this procedure is a member of the **db_owner** fixed database role in each database.

Start SQL Server Management Studio.

Right-click the content database that you want to make read-only, and then click **Properties**.

Select the **Options** page, and, in the **Other options** list, scroll to the **State** section.

In the **Database Read-Only** row, click the arrow next to **False**, select **True**, and then click **OK**.

Repeat for all other content databases.

Note

When a database is set to read-only, all connections except the one that is setting the read-only flag are stopped. After the read-only flag is set, other connections are enabled.

The site collection that is associated with a read-only content database is automatically set to read-only if the locking status of the site collection was previously None, No Additions, or Read-Only. If the locking status of the site collection was previously No Access, it remains No Access when the database locking status is changed.

Set service application databases to read-only

## Set service application databases to read-only

It is possible to set any service application database to read-only. However, some service applications do not function when their databases are set to read-only, such as those that are associated with Search and Project Server.

**To set service application databases to read-only by using SQL Server**

Verify that the user account that is performing this procedure is a member of the **db_owner** fixed database role in each database.

Start SQL Server Management Studio.

Right-click the database that you want to make read-only, and then click **Properties**.

Select the **Options** page, and, in the **Other options** list, scroll to the **State** section.

In the **Database Read-Only** row, click the arrow next to **False**, select **True**, and then click **OK**.

Repeat for other service application databases as appropriate.

Note

When a database is set to read-only, all connections except the one that is setting the read-only flag are stopped. After the read-only flag is set, other connections are enabled.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
