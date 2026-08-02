---
title: "Copy databases to the new farm for upgrade to SharePoint Server 2019 - SharePoint Server"
description: "How to copy SharePoint Server 2016 content and service databases to a SharePoint Server 2019 farm."
ms.topic: upgrade-and-migration-article
---
Note

Copy databases to the new farm for upgrade to SharePoint Server 2019

# Copy databases to the new farm for upgrade to SharePoint Server 2019

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

When you upgrade from SharePoint Server 2016 to SharePoint Server 2019, you must use a database attach upgrade, which means that you upgrade only the content for your environment and not the configuration settings. After you have configured a new SharePoint Server 2019 environment, you can copy the content and service application databases from the SharePoint Server 2016 environment to the SharePoint Server 2019 environment. You use a backup and restore process to copy the database, and you can also choose to set the databases to read-only in the SharePoint Server 2016 environment so that users can continue to access their information, but not change it. This article contains the steps that you take to copy the databases.

**Phase 2 of the upgrade process: Copy databases to the new farm**

|  |  |
| --- | --- |
|  | This is the second phase in the process to upgrade SharePoint Server 2016 data and sites to SharePoint Server 2019. The process includes the following phases that must be completed in order:  

 Create the SharePoint Server 2019 farm for a database attach upgrade 
Copy databases to the new farm for upgrade to SharePoint Server 2019  (this phase) 
Upgrade service applications to SharePoint Server 2019 
Upgrade content databases to SharePoint Server 2019.
 
For an overview of the whole process, see Overview of the upgrade process to SharePoint Server 2019. |

Before you begin

## Before you begin

Before you copy the databases, review the following information and take any recommended actions.

Make sure that the account that you use to copy the databases has access to SQL Server Management Studio on both the SharePoint Server 2016 and SharePoint Server 2019 environments and has access to a network location that can be accessed from both environments to store the copies of the databases.

Make sure that the account that you use to set the databases to read-only and read-write is a member of the **db_owner** fixed database role for the content databases that you want to upgrade.

Before you back up the databases, check for and repair all database consistency errors.

Set the earlier version databases to be read-only

## Set the earlier version databases to be read-only

To maintain user access to your original environment, set the SharePoint Server 2016 databases to read-only before you back up the databases. Even if you don't want to maintain access over the long term, set the databases to read-only to make sure that you capture all the data in the backup so that you restore and upgrade the current state of the environment without allowing additional changes to be made. If the databases are set to read-only, users can continue to view content. However, they will be unable to add or change content.

Note

Don't set search databases to read-only at this point. It's best not to interrupt the search experience until you're ready to upgrade the Search service applications. You will handle these databases when you upgrade service applications (the fourth phase in the process to upgrade SharePoint Server 2016 data and sites to SharePoint Server 2019).

Important

Perform this step in the SharePoint Server 2016 environment.

**To set a database to read-only by using SQL Server tools**

Verify that the user account that is performing this procedure is a member of the **db_owner** fixed database role for the databases.

In SQL Server Management Studio, in Object Explorer, connect to an instance of the Database Engine, expand the server, and then expand **Databases**.

Find the database that you want to configure to be read-only, right-click the database, and then click **Properties**.

In the **Database Properties** dialog, in the **Select a page** section, click **Options**.

In the details pane, under **Other options**, in the **State** section, next to **Database Read-Only**, click the arrow, and then select **True**.

You can use Transact-SQL to configure the **READ_ONLY** database availability option. For more information about how to use the **SET** clause of the **ALTER DATABASE** statement, see Setting Database Options.

Back up the SharePoint Server 2016 databases by using SQL Server tools

## Back up the SharePoint Server 2016 databases by using SQL Server tools

You back up the databases in SQL Server Management Studio. A backup copy of the database guarantees that you have the data in a safe state if you must enable the original farm again and is required for a database-attach upgrade. Repeat the procedure for the following databases in the SharePoint Server 2016 server farm:

All content databases (default database name: WSS_Content_ *ID*

The following service application databases:

| **Service application** | **Default database name** |
| --- | --- |
| Business Data Connectivity | BDC_Service_DB_ *ID* |
| Managed Metadata | Managed Metadata Service_ *ID* |
| PerformancePoint | PerformancePoint Service Application_ *ID* |
| Secure Store | Secure_Store_Service_DB_ *ID* |

You do not have to back up the configuration or admin content databases, because you recreated these databases when you set up the SharePoint Server 2019 server farm. Upgrading the configuration or admin content databases and the Central Administration site collection is not supported.

After you complete this procedure, you will have created backups of the read-only content databases.

Important

Perform this step in the SharePoint Server 2016 environment.

**To back up a database by using SQL Server tools**

Verify that the user account that is performing this procedure is a member of the **db_owner** fixed database role for the databases.

In Management Studio, in Object Explorer, connect to an instance of the Database Engine, expand the server, and then expand **Databases**.

Right-click the database that you want to back up, point to **Tasks**, and then click **Back Up**.

The **Back Up Database** dialog appears.

In the **Source** area, in the **Database** box, verify the database name.

In the **Backup type** box, select **Full**.

Under **Backup component**, select **Database**.

In the **Backup set** area, in the **Name** box, either accept the backup set name that is suggested or type a different name for the backup set.

In the **Destination** area, specify the type of backup destination by selecting **Disk** or **Tape**, and then specify a destination. To create a different destination, click **Add**.

Click **OK** to start the backup process.

Repeat the previous procedure to back up all the content and appropriate service application databases that SharePoint Server 2019 uses in your environment.

Copy the backup files to the SharePoint Server 2019 environment

## Copy the backup files to the SharePoint Server 2019 environment

Copy the backup files that you created in the previous procedure from the SharePoint Server 2016 environment to the SharePoint Server 2019 environment.

Restore a backup copy of the database

## Restore a backup copy of the database

After you configure the new SharePoint Server 2019 server farm, you can restore the backup copies of the databases to SQL Server. Start with one database, and then verify that the restoration has worked before you restore the other databases.

Important

Be sure to keep a copy of your original backups in reserve, just in case upgrade fails and you have to troubleshoot and try again. > Perform this step in the SharePoint Server 2016 environment.

**To restore a backup copy of a database by using SQL Server tools**

Verify that the user account that is performing this procedure is a member of the **db_owner** fixed database role for the databases.

After you connect to the appropriate instance of the SQL Server 2014 Database Engine, in Object Explorer, expand the server name.

Right-click **Databases**, and then click **Restore Database**.

The **Restore Database** dialog appears.

In the **Restore Database** dialog, on the **General** page, type the name of the database to be restored in the **To database** list.

Tip

When you type the name for the restored database, you do not have to use the original name. If you want to change the database name from a name with a long GUID to a shorter, friendlier name, this is an opportunity to make that change. Be sure to also change the database and log file names in the file system (the MDF and LDF files) so that they match.

In the **To a point in time** text box, keep the default **(Most recent possible)**.

To specify the source and location of the backup sets to restore, click **From device**, and then use the ellipsis ( **...**) to select the backup file.

In the **Specify Backup** dialog, in the **Backup media** box, be sure that **File** is selected.

In the **Backup location** area, click **Add**.

In the **Locate Backup File** dialog, select the file that you want to restore, click **OK**, and then, in the **Specify Backup** dialog, click **OK**.

In the **Restore Database** dialog, under **Select the backup sets to restore** grid, select the **Restore** check box next to the most recent full backup.

In the **Restore Database** dialog, on the **Options** page, under **Restore options**, select the **Overwrite the existing database** check box.

Click **OK** to start the restore process.

Set the databases to read-write

## Set the databases to read-write

You cannot upgrade a database that is set to read-only. You must set the databases back to read-write on your SharePoint Server 2019 farm before you attach and upgrade them.

Important

Perform this step in the SharePoint Server 2019 environment.

**To set a database to read-write by using SQL Server tools**

In SQL Server Management Studio, in Object Explorer, connect to an instance of the Database Engine, expand the server, and then expand **Databases**.

Select the database that you want to configure to be read-write, right-click the database, and then click **Properties**.

In the **Database Properties** dialog, in the **Select a page** section, click **Options**.

In the details pane, under **Other options**, in the **State** section, next to **Database Read-Only**, click the arrow, and then select **False**.

|  |  |
| --- | --- |
|  | This is the second phase in the process to upgrade SharePoint Server 2016 data and sites to SharePoint Server 2019.  
  Next phase: Upgrade service applications to SharePoint Server 2016 
  For an overview of the whole process, see Overview of the upgrade process to SharePoint Server 2019. |

See also

## See also

Concepts

#### Concepts

Create the SharePoint Server 2019 farm for a database attach upgrade

Upgrade service applications to SharePoint Server 2019

Upgrade content databases to SharePoint Server 2019

Additional resources

## Additional resources

- Last updated on 
		2023-01-26
