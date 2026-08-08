---
title: "Restore content databases in SharePoint Server - SharePoint Server"
description: "Learn how to restore a content database in SharePoint Server."
ms.topic: how-to
---
Note

Restore content databases in SharePoint Server

# Restore content databases in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can restore a content database in SharePoint Server by using the SharePoint Central Administration website, PowerShell, or SQL Server tools. The restore tool that you use depends on the kind of environment that you have deployed, your schedule requirements, and service level agreements that you have made with your organization.

Before you begin

## Before you begin

You can restore any content database or several content databases, one at a time. For information about how to back up all the content databases in a farm at the same time, see Back up farms in SharePoint Server.

Before you begin this operation, review the following information about how to restore a content database:

SharePoint Server restores remote Binary Large Objects (BLOB) stores but only if you are using the SQL Filestream remote BLOB store provider to place data in remote BLOB stores.

If you are using another provider you must manually restore these remote BLOB stores.

Using PowerShell to restore a SharePoint content database

## Using PowerShell to restore a SharePoint content database

You can use PowerShell to restore a content database.

To restore a content database by using PowerShell

### To restore a content database by using PowerShell

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
Restore-SPFarm -Directory <BackupFolder> -RestoreMethod Overwrite -Item <ContentDatabase> [-BackupId <GUID>] [-Verbose]
```

Where:

*<BackupFolder>* is the name and path for the backup folder where the service application was backed up.

*<ContentDatabase>* is the name of the content database.

If you do not use the  `BackupId` parameter, the most recent backup will be used. To view all of the backups for the farm, type the following command at the PowerShell command prompt:

```
Get-SPBackupHistory -Directory <Backup folder>
```

For more information, see Restore-SPFarm.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

Using Central Administration to restore a SharePoint content database

## Using Central Administration to restore a SharePoint content database

You can use Central Administration to restore a farm or components of a farm.

To restore a content database by using Central Administration

### To restore a content database by using Central Administration

Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.

Start Central Administration.

In Central Administration, on the home page, in the **Backup and Restore** section, click **Restore from a backup**.

On the Restore from Backup — Step 1 of 3: Select Backup to Restore page, from the list of backups, select the backup job that contains the content database backup, and then click **Next**.

Note

If the correct backup job does not appear, in the **Current Directory Location** text box, enter the path of the correct backup folder, and then click **Refresh**.

On the Restore from Backup — Step 2 of 3: Select Component to Restore page, select the check box that is next to the content database, and then click **Next**.

Note

If the content database is not selectable, you must use PowerShell or SQL Server tools to restore the content database.

On the Restore from Backup — Step 3 of 3: Select Restore Options page, in the **Restore Options** section, under **Type of Restore**, click the **Same configuration** option. A dialog appears that asks you to confirm the operation. Click **OK**.

Click **Start Restore**.

You can view the general status of all recovery jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current recovery job in the lower part of the page in the **Restore** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the recovery to start.

If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Sprestore.log file at the UNC path that you specified in step 2.

Using SQL Server tools to restore a SharePoint content database

## Using SQL Server tools to restore a SharePoint content database

You can use SQL Server tools to restore a content database by following these steps:

If possible, back up the live transaction log of the content database to protect any changes that were made after the last full backup.

Restore the last full database backup.

Restore the most recent differential database backup that occurred after the most recent full database backup.

Restore all transaction log backups that occurred after the most recent full or differential database backup.

To restore a content database by using SQL Server tools

### To restore a content database by using SQL Server tools

Verify that the user account performing this procedure is a member of the **sysadmin** fixed server role.

If the SharePoint Timer service is running, stop the service and wait for several minutes for any currently running stored procedures to finish. Do not restart the service until after you restore the content databases.

Start SQL Server Management Studio and connect to the database server.

In Object Explorer, expand **Databases**.

Right-click the database that you want to restore, point to **Tasks**, point to **Restore**, and then click **Database**.

The database is automatically taken offline during the recovery operation and cannot be accessed by other processes.

In the **Restore Database** dialog, specify the destination and the source, and then select the backup set or sets that you want to restore.

The default values for destination and source are appropriate for most recovery scenarios.

In the **Select a page** pane, click **Options**.

In the **Restore options** section, select only **Overwrite the existing database**. Unless the environment or policies require otherwise, do not select the other options in this section.

In the **Recovery state** section:

If you have included all the transaction logs that you must restore, select **RECOVER WITH RECOVERY**.

If you must restore additional transaction logs, select **RECOVER WITH NORECOVERY**.

The third option, **RECOVER WITH STANDBY** is not used in this scenario.

Note

For more information about these recovery options, see Restore Database (Options Page).

Click **OK** to complete the recovery operation.

Repeat steps 4 through 10 for each database that you are restoring.

Start the SharePoint Timer service.

See also

## See also

Concepts

#### Concepts

Back up content databases in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
