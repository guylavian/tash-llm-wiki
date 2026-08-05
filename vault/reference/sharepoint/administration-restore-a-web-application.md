---
title: "Restore web applications in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-restore-a-web-application
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/restore-a-web-application
family: administration
documentKind: "how-to"
abstract: "Learn how to restore a web application in SharePoint Server."
---

# Restore web applications in SharePoint Server - SharePoint Server

Note

Restore web applications in SharePoint Server

# Restore web applications in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can restore a web application in SharePoint Server by using the SharePoint Central Administration website, Microsoft PowerShell, or SQL Server tools. Which backup tool you use depends on what kind of environment you have deployed, what your backup schedule requires, and what service level agreements you have made with your organization.

Before you begin

## Before you begin

When you restore a web application, you also restore the Internet Information Services (IIS) settings and all content databases that are associated with the web application.

Before you begin this operation, review the following information as you prepare to restore a web application:

You can only restore one web application at a time by using the procedures in this article. However, at the same time, you can restore all the web applications in the farm by restoring the complete farm.

If a web application uses the object cache, you must manually configure two special user accounts for the web application after you restore the web application. For more information about the object cache and how to configure these user accounts, see Configure object cache user accounts in SharePoint Server.

You can't use SQL Server tools to restore a web application.

When you restore a web application that is configured to use claims-based authentication, there are additional steps that you must follow after restoring the web application to restore claims-based authentication.

Using PowerShell to restore a web application in SharePoint Server

## Using PowerShell to restore a web application in SharePoint Server

You can use PowerShell to restore a web application manually or as part of a script that can be run at scheduled intervals.

**To restore a web application by using PowerShell**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you're running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For more information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Restore-SPFarm -Directory <BackupFolderName> -RestoreMethod Overwrite -Item  <WebApplicationName> [-BackupId <GUID>] [-Verbose]
```

Where:

*<BackupFolderName>* is the full path of the folder that you use for backup files.

*<WebApplicationName>* is the name of the web application that was backed up.

*<GUID>* is the identifier of the back up to use for the restore operation.

If you don't specify the value of the  `BackupID` parameter, the most recent backup will be used. You can't restore a web application by using a configuration-only backup. You can view the backups for the farm by typing the following:

```
Get-SPBackupHistory -Directory <BackupFolderName> -ShowBackup
```

For more information, see Restore-SPFarm.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

Using Central Administration to restore a web application in SharePoint Server

## Using Central Administration to restore a web application in SharePoint Server

You can use Central Administration to restore a web application.

**To restore a web application by using Central Administration**

Verify that the user account performing this procedure is a member of the Farm Administrators group. Additionally, verify that the SharePoint Timer service and the Farm Database Access account have Full Control permissions on the backup folder.

Start Central Administration.

In Central Administration, on the home page, in the **Backup and Restore** section, click **Restore from a backup**.

On the Restore from Backup — Step 1 of 3: Select Backup to Restore page, from the list of backups, select the backup job that contains the farm or web application backup, and then click **Next**. You can view more details about each backup by clicking the (+) next to the backup.

Note

If the correct backup job does not appear, in the **Current Directory Location** text box, type the Universal Naming Convention (UNC) path of the correct backup folder, and then click **Refresh**. > You cannot use a configuration-only backup to restore the web application.

On the Restore from Backup — Step 2 of 3: Select Component to Restore page, select the check box that is next to the web application, and then click **Next**.

On the Restore from Backup — Step 3 of 3: Select Restore Options page, in the **Restore Component** section, make sure that **Farm\<Web application>** appears in the **Restore the following content** list.

In the **Restore Only Configuration Settings** section, make sure that the **Restore content and configuration settings** option is selected.

In the **Restore Options** section, under **Type of Restore**, select the **Same configuration** option. A dialog appears that asks you to confirm the operation. Click **OK**.

Note

If the **Restore Only Configuration Settings** section does not appear, the backup that you selected is a configuration-only backup. You must select another backup.

Click **Start Restore**.

You can view the general status of all recovery jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current recovery job in the lower part of the page in the **Restore** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the recovery to start.

If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Sprestore.log file at the UNC path that you specified.

Using SQL Server tools to restore databases associated with a web application in SharePoint Server

## Using SQL Server tools to restore databases associated with a web application in SharePoint Server

You can't restore the complete web application by using SQL Server tools. However, you can restore all the databases that are associated with the web application. To restore the complete web application, use either PowerShell or Central Administration.

**To restore databases associated with a web application by using SQL Server tools**

Verify that the user account performing this procedure is a member of the **sysadmin** fixed server role.

If the SharePoint Timer service is running, stop the service and wait for several minutes for any currently running stored procedures to finish. Don't restart the service until after you restore the databases.

Start SQL Server Management Studio and connect to the database server.

In Object Explorer, expand **Databases**.

Right-click the database that you want to restore, point to **Tasks**, point to **Restore**, and then click **Database**.

The database is automatically taken offline during the recovery operation and can't be accessed by other processes.

In the **Restore Database** dialog, specify the destination and the source, and then select the backup set or sets that you want to restore.

The default values for destination and source are appropriate for most recovery scenarios.

In the **Select a page** pane, click **Options**.

In the **Restore options** section, select only **Overwrite the existing database**. Unless the environment or policies require otherwise, don't select the other options in this section.

In the **Recovery state** section:

If you have included all the transaction logs that you must restore, select **RECOVER WITH RECOVERY**.

If you must restore additional transaction logs, select **RECOVER WITH NORECOVERY**.

The third option, **RECOVER WITH STANDBY** is not used in this scenario.

Note

For more information about these recovery options, see Restore Database (Options Page).

Click **OK** to complete the recovery operation.

Repeat steps 4 through 10 for each database that you're restoring.

Start the Windows SharePoint Services Timer service.

Additional steps to restore a web application that uses forms-based authentication in SharePoint Server

## Additional steps to restore a web application that uses forms-based authentication in SharePoint Server

After you restore a web application that uses forms-based authentication, you must follow these steps to reconfigure the web application to use forms-based authentication.

Re-register the membership and role providers in the Web.config file.

Redeploy the providers.

Additional steps to remove duplicate claims providers after restoring a web application that uses claims-based authentication in SharePoint Server

## Additional steps to remove duplicate claims providers after restoring a web application that uses claims-based authentication in SharePoint Server

After a web application that is configured to use claims-based authentication is restored, duplicate, or additional claims providers are often visible. You must use the following process to remove the duplicate providers:

In Central Administration, click **Manage Web application**, select a web application that uses claims-based authentication, and then click **Authentication Providers**.

Select a zone that the web application is associated with to open the **Edit Authentication** page, and then click **Save**.

Repeat for each zone, and then for each web application that uses claims-based authentication.

Additional steps to reconfigure object cache user accounts in SharePoint Server

## Additional steps to reconfigure object cache user accounts in SharePoint Server

If you configured object cache user accounts for the web application, the restore process won't restore these settings. You must reconfigure the settings for the web application. For more information, see Configure object cache user accounts in SharePoint Server.

See also

## See also

Concepts

#### Concepts

Back up web applications in SharePoint Server

Plan for backup and recovery in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
