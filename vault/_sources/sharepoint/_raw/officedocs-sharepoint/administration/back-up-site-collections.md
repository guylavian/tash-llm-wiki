---
title: "Back up site collections in SharePoint Server - SharePoint Server"
description: "Learn how to back up a single site collection in SharePoint Server."
ms.topic: how-to
---
Note

Back up site collections in SharePoint Server

# Back up site collections in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can back up a site collection in SharePoint Server by using the SharePoint Central Administration website or Microsoft PowerShell.

Before you begin

## Before you begin

We recommend that you regularly back up the complete farm. However, IT practices might require you to also back up a site collection. For more information about what to back up, see Plan for backup and recovery in SharePoint Server.

Before you begin this operation, review the following information:

You must first create a folder on the local computer or the network in which to store the backups. For better performance, we recommend that you back up to the local computer and then move the backup files to a network folder. For more information about how to create a backup folder, see Prepare to back up and restore farms in SharePoint Server.

If the site collection's **Lock status** is set to **Not locked** or **Adding content prevented**, SharePoint Server temporarily sets the site to **Read-Only** while the backup operation is occurring. SharePoint Server does this to reduce the possibilities of users changing the site collection while it is being backed up. After the backup is complete, the setting is changed back its normal status.

Performing a site collection backup might require resources and might slightly affect farm performance when the backup is running. You can help avoid performance issues by backing up the farm during hours when farm use is lowest, such as outside office hours.

Use PowerShell to back up a site collection in SharePoint Server

## Use PowerShell to back up a site collection in SharePoint Server

You can use PowerShell to back up a site collection manually or as part of a script that can be run at scheduled intervals.

**To back up a site collection by using PowerShell**

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
Backup-SPSite -Identity <SiteCollectionGUIDorURL> -Path <BackupFile> [-Force] [-NoSiteLock] [-UseSqlSnapshot] [-Verbose]
```

Where:

*<SiteCollectionGUIDorURL>* is the ID or URL for the site collection you want to back up.

*<BackupFile>* is the path to where the backup file is located.

If you want to overwrite a previously used backup file, use the  `Force` parameter. You can use the  `NoSiteLock` parameter to keep the read-only lock from being set on the site collection while it is being backed up. However, using this parameter can enable users to change the site collection while it is being backed up and could lead to possible data corruption during backup. To display the site collection GUID or URL at the PowerShell command prompt, type the following command:

```
Get-SPSite | format-list -property id,url
```

If the database server is running an Enterprise Edition of SQL Server, we recommend that you also use the  `UseSqlSnapshot` parameter for more consistent backups. You can also export sites or lists from these snapshots.

Note

If the RBS provider that you are using does not support snapshots, you cannot use snapshots for content deployment or backup. For example, the SQL FILESTREAM provider does not support snapshots.

For more information about how to use SQL snap-shots, see Back up databases to snapshots in SharePoint Server.

For more information, see Backup-SPSite.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

Use Central Administration to back up a site collection in SharePoint Server

## Use Central Administration to back up a site collection in SharePoint Server

You can use Central Administration to back up a site collection.

**To back up a site collection by using Central Administration**

Verify that the user account performing this procedure is a member of the Farm Administrators group. Additionally, verify that the Windows SharePoint Services Timer V4 service has Full Control permissions on the backup folder.

Start Central Administration.

In Central Administration, on the home page, in the **Backup and Restore** section, click **Perform a site collection backup**.

On the **Site collection backup** page, select the site collection from the **Site Collection** list.

Type the local path of the backup file in the **Filename** box.

Note

If you want to reuse a file, select the **Overwrite existing file** check box.

Click **Start Backup**.

You can view the general status of all backup jobs at the top of the Granular Backup Job Status page in the **Readiness** section. You can view the status for the current backup job in the lower part of the page in the **Site Collection Backup** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the backup to start.

If you receive any errors, you can review them in the **Failure Message** column of the Granular Backup Job Status page.

See also

## See also

Concepts

#### Concepts

Plan for backup and recovery in SharePoint Server

Restore site collections in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
