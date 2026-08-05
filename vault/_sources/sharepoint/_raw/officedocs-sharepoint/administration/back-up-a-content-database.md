---
title: "Back up content databases in SharePoint Server - SharePoint Server"
description: "Learn how to back up a single content database in SharePoint Server."
ms.topic: how-to
---
Note

Back up content databases in SharePoint Server

# Back up content databases in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can back up a content database by using the SharePoint Central Administration website, Microsoft PowerShell, or SQL Server tools. The backup tool that you use depends on the kind of environment that you have deployed, your backup schedule requires, and service level agreements that you have made with your organization.

Before you begin

## Before you begin

SharePoint Server content databases can grow to be very large. Therefore, you might want to back them up separately from farm backups. Regularly backing up content databases reduces data losses that might occur from hardware failures, power outages, or other problems. It is a simple process and helps make sure that all the data is available for recovery, if that is required. You can only back up one content database at a time.

Before you begin this operation, review the following information:

You must create a folder on the local computer or the network in which to store the backups. For better performance, we recommend that you back up to the local computer and then move the backup files to a network folder.

SharePoint Server backup backs up remote Binary Large Objects (BLOB) stores but only if you are using the SQL Filestream remote BLOB store provider to place data in remote BLOB stores.

If you are using another provider you must manually back up these remote BLOB stores.

If you are using SQL Server with Transparent Data Encryption (TDE), and you are backing up your environment by using either SharePoint tools or SQL Server tools, the TDE encryption key in not backed up or restored. You must back up the key manually. When restoring, you must manually restore the key before restoring the data. For more information, see Transparent Data Encryption (TDE).

Use PowerShell to back up a content database in SharePoint Server

## Use PowerShell to back up a content database in SharePoint Server

You can use PowerShell to back up a content database manually or as part of a script that can be run at scheduled intervals.

**To back up a content database by using PowerShell**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Backup-SPFarm -Directory <BackupFolder> -BackupMethod {Full | Differential} -Item <ContentDatabaseName> [-Verbose]
```

Where:

*<BackupFolder>* is the path of the backup folder.

*<ContentDatabaseName>* is the name of the database that you want to back up. To display the name of the content database, type the following command at the PowerShell command prompt:  `Get-SPContentDatabase`.

To view the progress of the backup operation, use the **Verbose** parameter.

Note

If you are backing up the content database for the first time, you must use the **Full** option. You must perform a full backup before you can perform a differential backup.

For more information, see Backup-SPFarm.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

Use Central Administration to back up a content database in SharePoint Server

## Use Central Administration to back up a content database in SharePoint Server

You can use Central Administration to back up a content database.

**To back up a content database by using Central Administration**

Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.

Start Central Administration.

In Central Administration, on the home page, in the **Backup and Restore** section, click **Perform a backup**.

On the Perform a Backup — Step 1 of 2: Select Component to Back Up page, select the content database that you want to back up from the list of components, and then click **Next**.

Note

Not all content databases can be selected in the list. If a database is not selectable, you must use PowerShell to back up the content database.

On the Start Backup — Step 2 of 2: Select Backup Options page, in the **Backup Type** section, select either **Full** or **Differential**.

Note

If you are backing up the content database for the first time, you must use the **Full** option. You must perform a full backup before you can perform a differential backup.

In the **Backup File Location** section, type the Universal Naming Convention (UNC) path of the backup folder, and then click **Start Backup**.

You can view the general status of all backup jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status of the current backup job in the lower part of the page in the **Backup** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the backup to start.

If you receive any errors, review the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Spbackup.log file at the UNC path that you specified in step 5.

Use SQL Server tools to back up a content database in SharePoint Server

## Use SQL Server tools to back up a content database in SharePoint Server

You can use SQL Server tools to back up a content database.

**To back up a content database by using SQL Server tools**

Verify that the user account that is performing this procedure is a member of the SQL Server **db_owner** fixed database role on all databases that are to be backed up.

Open SQL Server Management Studio and connect to the correct instance of the SQL Server Database Engine.

In Object Explorer, expand **Databases**.

Right-click the database that you want to back up, point to **Tasks**, and then click **Back Up**.

In the **Back Up Database** dialog, confirm the database name.

Next, select the kind of backup that you want to perform from the **Backup type** list. For more information about which backup type to use, see Recovery Models (SQL Server).

In the **Backup component** area, click **Database**.

Either use the default name that is provided or specify a name for the backup set in the **Name** text box.

In the **Destination** area, specify where you want to store the backup.

Click **OK** to back up the database.

Repeat steps 1-10 for each content database.

See also

## See also

Concepts

#### Concepts

Restore content databases in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
