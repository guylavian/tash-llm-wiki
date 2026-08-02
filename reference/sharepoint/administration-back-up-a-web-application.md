---
title: "Back up web applications in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-back-up-a-web-application
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/back-up-a-web-application
family: administration
documentKind: "how-to"
abstract: "Learn how to back up a web application in SharePoint Server by using Central Administration or Microsoft PowerShell."
---

# Back up web applications in SharePoint Server - SharePoint Server

Note

Back up web applications in SharePoint Server

# Back up web applications in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can back up a web application by using the SharePoint Central Administration website, PowerShell, or SQL Server tools. The backup tool that you use depends on the kind of environment that you have deployed, your backup schedule requirements, and service level agreements that you have with your organization.

Before you begin

## Before you begin

Regularly backing up a web application reduces the possibility of data losses that might occur from hardware failures, power outages, or other problems. It is a simple process that can help make sure that all the web application-related data and configurations are available for recovery, if that is required. We recommend that web application backups be created in addition to regular backups at the farm level.

Before you begin this operation, review the following information:

Before you begin, you must create a network folder in which to store the backups. Both the SharePoint Timer Service (SPTimerV4) service account and the server farm user account must have Full Control permissions to this folder. For more information about how to create a backup folder, see Prepare to back up and restore farms in SharePoint Server.

You can back up only one web application at a time by using the procedures in this article. You can back up all web applications by backing up the complete farm.

Backing up a web application does not affect the state of the farm. However, it does require resources and might slightly affect farm performance when the backup is running. You can avoid performance issues by backing up the web application during hours when farm use is lowest, such as outside office hours.

If the web application uses the object cache, you must manually configure two special user accounts for the web application after you restore the web application.

When you back up a web application, the Internet Information Services (IIS) settings and all content databases that are associated with the web application are also backed up.

When you back up a web application that is configured to use forms-based authentication, you must also use a file backup system to protect the Web.config files because the Web.config files were updated manually to register the membership and role providers, and manual changes to the Web.config files are not backed up. Similarly, Web.config files are not restored when you restore a Web application. After recovery, you must update the Web.config files and redeploy the providers. For more information, see Plan for user authentication methods in SharePoint Server.

Use PowerShell to back up a web application

## Use PowerShell to back up a web application

You can use PowerShell to back up a web application manually or as part of a script that can be run at scheduled intervals.

**To back up a web application by using PowerShell**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Note

Alternately, the user can be a member of the **db_backupoperator** fixed database role on all databases that are to be updated if you do not want to assign full rights of the **db_owner** role.

- Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Backup-SPFarm -Directory <BackupFolder> -BackupMethod {Full | Differential} -Item <WebApplicationName> [-Verbose]
```

Where:

*<BackupFolder>* is the path of the folder that you use for storing backup files.

*<WebApplicationName>* is the name of the web application. To display the name of the web application, at the PowerShell command prompt, type the following command:  `Backup-SPFarm -ShowTree`

Note

If you are backing up the web application for the first time, you must use the  `Full` option. You must perform a full backup before you can perform a differential backup.

For more information, see Backup-SPFarm..

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

Use Central Administration to back up a web application

## Use Central Administration to back up a web application

You can use Central Administration to back up a web application.

**To back up a web application by using Central Administration**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

Start Central Administration.

In Central Administration, on the home page, in the **Backup and Restore** section, click **Perform a backup**.

On the Perform a Backup — Step 1 of 2: Select Component to Back Up page, select the web application from the list of components, and then click **Next**.

Note

The web application might consist of several components. You must select the top-level component.

On the Start Backup — Step 2 of 2: Select Backup Options page, in the **Backup Type** section, select either **Full** or **Differential**.

Note

If you are backing up the web application for the first time, you must use the **Full** option. You must perform a full backup before you can perform a differential backup.

In the **Back Up Only Configuration Settings** section, click **Back up content and configuration settings**.

In the **Backup File Location** section, type the Universal Naming Convention (UNC) path of the backup folder, and then click **Start Backup**.

You can view the general status of all backup jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current backup job in the lower part of the page in the **Backup** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the backup to start.

If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Spbackup.log file at the UNC path that you specified in step 6.

Use SQL Server tools to back up a databases that are associated with a web application

## Use SQL Server tools to back up a databases that are associated with a web application

You cannot back up the complete web application by using SQL Server tools. However, you can back up all the databases that are associated with the web application. To back up the complete web application, use either PowerShell or Central Administration.

**To back up a database associated with a web application by using SQL Server tools**

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

Repeat steps 1-10 for each farm database.

See also

## See also

Concepts

#### Concepts

Restore web applications in SharePoint Server

Back up farms in SharePoint Server

Plan for backup and recovery in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
