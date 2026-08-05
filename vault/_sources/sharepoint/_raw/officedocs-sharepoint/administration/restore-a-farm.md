---
title: "Restore farms in SharePoint Server - SharePoint Server"
description: "Learn how to restore a SharePoint Server farm."
ms.topic: how-to
---
Note

Restore farms in SharePoint Server

# Restore farms in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can restore a SharePoint Server farm by using the SharePoint Central Administration website, Microsoft PowerShell, or SQL Server tools. The backup tool that you use depends on the kind of environment that you have deployed, the backup schedule, and service level agreements that you have made with your organization.

Before you begin

## Before you begin

Farm-level recovery is performed only after a failure that involves the complete farm, or where partial recovery of part of the farm isn't possible. If you only have to restore part of the farm, a specific database, a service application, a list, or document library, or a specific document, use another recovery method. For more information about alternate forms of recovery, see Related content.

Farm recovery is performed for any of the following reasons:

Restoring a farm after a fire, disaster, equipment failure, or other data-loss event.

Restoring farm configuration settings and data to a specific previous time and date.

Moving a SharePoint Server deployment from one farm to another farm.

Before you begin this operation, review the following information about how to recover a farm in SharePoint:

You can't back up from one version of SharePoint Server 2019 and restore to another version of SharePoint Server 2019. The same applies to SharePoint Servers 2016 and 2013.

Backing up the farm will back up the configuration and Central Administration content databases, but these can't be restored using SharePoint Server tools. For more information about how to back up and restore all of the farm databases, see Move all databases in SharePoint Server.

When you restore the farm by using SharePoint Server, the restore process won't automatically start all of the service applications. You must manually start them by using Central Administration or Microsoft PowerShell. Don't use SharePoint Products Configuration Wizard to start the services because doing this will also reprovision the services and service proxies. For more information, see Start or stop a service in SharePoint Server.

The identifier (ID) of each content database is retained when you restore or reattach a database by using built-in tools. Default change log retention behavior when using built-in tools is as follows:

The change logs for all databases are retained when you restore a farm.

The change log for content databases is retained when you reattach or restore a database.

When a database ID and change log are retained, the search system continues crawling based on the regular schedule that is defined by crawl rules.

When you restore an existing database and don't use the overwrite option, a new ID is assigned to the restored database, and the database change log isn't preserved. The next crawl of the database will add data from the content database to the index.

If a restore is performed and the ID in the backup package is already being used in the farm, a new ID is assigned to the restored database and a warning is added to the restore log. The ability to perform an incremental crawl instead of a full crawl depends on the content database ID being the same as before and the change log token that is used by the search system being valid for the current change sign-in the content database. If the change log isn't preserved, the token isn't valid and the search system has to perform a full crawl.

SharePoint Server backup backs up the Business Data Connectivity service external content type definitions but doesn't back up the data source itself. To protect the data, you should back up the data source when you back up the Business Data Connectivity service or the farm.

If you restore the Business Data Connectivity service or the farm and then restore the data source to a different location, you must change the location information in the external content type definition. If you don't, the Business Data Connectivity service might be unable to locate the data source.

SharePoint Server restores remote Binary Large Objects (BLOB) stores only if you're using the FILESTREAM remote BLOB store provider to put data in remote BLOB stores.

If you're using another provider, you must manually restore the remote BLOB stores.

If you're sharing service applications across farms, be aware that trust certificates that were exchanged aren't included in farm backups. You must back up your certificate store separately or keep the certificates in a separate location. When you restore a farm that shares a service application, you must import and redeploy the certificates, and then re-establish any inter-farm trusts.

For more information, see Exchange trust certificates between farms in SharePoint Server.

After a Web application that is configured to use claims-based authentication is restored, duplicate, or additional claims providers are often visible. If duplicates appear, then you must manually save each Web application zone to remove them. For more information, see Restore web applications in SharePoint Server.

Additional steps are required when you restore a farm that contains a Web application that is configured to use forms-based authentication. For more information, see Restore web applications in SharePoint Server.

Using PowerShell to restore a farm in SharePoint

## Using PowerShell to restore a farm in SharePoint

You can use Microsoft PowerShell to restore a farm.

**To restore a farm by using PowerShell**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you're running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For more information about PowerShell permissions, see Add-SPShellAdmin.

Open the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Restore-SPFarm -Directory <BackupFolder> -RestoreMethod Overwrite [-BackupId <GUID>]
```

Where:

*<BackupFolder>* is the path of the folder you use for storing backup files.

*<GUID>* is the identifier of the backup to restore from.

Note

If you are not logged on as the Farm account, you are prompted for the Farm account's credentials.

If you don't specify the `BackupId`, the most recent backup will be used. To view the backups for the farm, at the Microsoft PowerShell command prompt, type the following command:

```
Get-SPBackupHistory -Directory <BackupFolder> -ShowBackup [-Verbose]
```

Where:

- *<BackupFolder>* is the path of the folder you use for storing backup files.

You can't use a configuration-only backup to restore content databases together with the configuration.

To restart a service application, at the PowerShell command prompt, type the following command:

```
Start-SPServiceInstance -Identity <ServiceApplicationID>
```

Where *<ServiceApplicationID>* is the GUID of the service application.

For more information about how to restart service applications by using PowerShell, see Start-SPServiceInstance.

For more information about how to restore the farm by using PowerShell_2nd_NoVer, see Restore-SPFarm.PShell_stsadm_deprecated

Using Central Administration to restore a farm

## Using Central Administration to restore a farm

You can use the Central Administration Web site to restore a farm.

**To restore a farm by using Central Administration**

Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.

In Central Administration, on the home page, in the **Backup and Restore** section, click **Restore from a backup**.

On the Restore from Backup—Step 1 of 3: Select Backup to Restore page, from the list of backups, select the backup job that contains the farm backup, and then click **Next**. You can view more details about each backup by clicking the (+) next to the backup.

Note

If the correct backup job does not appear, in the **Backup Directory Location** text box, type the Universal Naming Convention (UNC) path of the correct backup folder, and then click **Refresh**. You cannot use a configuration-only backup to restore the farm.

On the Restore from Backup—Step 2 of 3: Select Component to Restore page, select the check box that is next to the farm, and then click **Next**.

On the Restore from Backup—Step 3 of 3: Select Restore Options page, in the **Restore Component** section, make sure that **Farm** appears in the **Restore the following component** list.

In the **Restore Only Configuration Settings** section, make sure that the **Restore content and configuration settings** option is selected.

In the **Restore Options** section, under **Type of Restore**, select the **Same configuration** option. A dialog will appear that asks you to confirm the operation. Click **OK**.

Note

If the **Restore Only Configuration Settings** section does not appear, the backup that you selected is a configuration-only backup. You must select another backup.

Click **Start Restore**.

You can view the general status of all recovery jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current recovery job in the lower part of the page in the **Restore** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the recovery to start.

If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Sprestore.log file at the UNC path that you specified in step 3.

When the restore process has completed, you may need to restart one or more service applications. In Central Administration, on the home page, in the **Systems Settings** section, click **Manage services on server**. On the Services on Server page, start any services related to service applications that you want to run by clicking **Restart** in the **Action** column next to the service application.

Re-establish any trust relationships. For more information, see Exchange trust certificates between farms in SharePoint Server.

Using SQL Server tools to restore a farm

## Using SQL Server tools to restore a farm

Although you can't restore the complete farm by using SQL Server tools, you can restore most of the farm databases. If you restore the databases by using SQL Server tools, you must restore the farm configuration by using Central Administration or PowerShell. For more information about how to restore the farm's configuration settings, see Restore farm configurations in SharePoint Server.

Note

The search index is not stored in SQL Server. If you use SQL Server tools to back up and restore search, you must perform a full crawl after you restore the content database.

Before you restore SharePoint Server, we recommend that you configure a recovery farm for site and item recovery.

Restore the databases by following these steps:

If possible, back up the live transaction log of the current database to protect any changes that were made after the last full backup.

Restore the last full database backup.

Restore the most recent differential database backup that occurred after the most recent full database backup.

Restore all transaction log backups that occurred after the most recent full or differential database backup.

Use the following procedure to restore your farm databases.

**To restore a farm by using SQL Server tools**

Verify that the user account that is performing this procedure is a member of the **sysadmin** fixed server role.

If the SharePoint Timer service is running, stop the service and wait for several minutes for any currently running stored procedures to finish. Don't restart the service until after you restore all the databases that you have to restore.

Start SQL Server Management Studio and connect to the database server.

In Object Explorer, expand **Databases**.

Right-click the database that you want to restore, point to **Tasks**, point to **Restore**, and then click **Database**.

The database is automatically taken offline during the recovery operation and can't be accessed by other processes.

In the **Restore Database** dialog, specify the destination and the source, and then select the backup set or sets that you want to restore.

The default values for destination and source are appropriate for most recovery scenarios.

In the **Select a page** pane, click **Options**.

In the **Restore options** section, select only **Overwrite the existing database**. Unless your environment or policies require otherwise, don't select the other options in this section.

In the **Recovery state** section:

If you have included all the transaction logs that you must restore, select **RECOVER WITH RECOVERY**.

If you must restore additional transaction logs, select **RECOVER WITH NORECOVERY**.

The third option, **RECOVER WITH STANDBY** isn't used in this scenario.

Note

For more information about these recovery options, see Restore Database (Options Page).

Click **OK** to complete the recovery operation.

Except for the configuration database, repeat steps 4 through 9 for each database that you're restoring.

Important

If you are restoring the User Profile database (by default named "User Profile Service_ProfileDB_<GUID>"), then also restore the Social database (by default named "User Profile Service_SocialDB_<GUID>"). Failing to do this can cause inaccuracies in the User Profile data that might be difficult to detect and fix.

To restore the configuration settings, you must use the existing configuration database or manually create a new database and restore the configuration to that database. For more information about how to restore the farm configuration, see Restore farm configurations in SharePoint Server.

Start the SharePoint Timer service.

Start any service applications that have to be restarted. In Central Administration, on the home page, in the **Systems Settings** section, click **Manage services on server**. On the Services on Server page, start any services related to service applications that you want to run by clicking **Restart** in the **Action** column next to the service application.

Related content

## Related content

The following list shows other recovery methods that you can use when you only need to restore part of your farm:

Back up farms in SharePoint Server

Restore farm configurations in SharePoint Server

Restore web applications in SharePoint Server

Restore content databases in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
