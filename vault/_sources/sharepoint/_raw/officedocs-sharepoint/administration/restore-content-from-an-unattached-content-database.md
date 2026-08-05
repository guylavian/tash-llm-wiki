---
title: "Restore content from unattached content databases in SharePoint Server - SharePoint Server"
description: "Learn how to restore content from an unattached content database in SharePoint Server."
ms.topic: how-to
---
Note

Restore content from unattached content databases in SharePoint Server

# Restore content from unattached content databases in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can restore content from an unattached content database in SharePoint Server by using the SharePoint Central Administration website or PowerShell. The restore tool that you use depends on the kind of environment that you have deployed, your schedule requirements, and service level agreements that you have made with your organization.

You can restore or copy content, such as sites, site collections, lists, or document libraries, from a content database without having to attach the content database to the farm.

Using PowerShell to recover content from an unattached content database in SharePoint Server

## Using PowerShell to recover content from an unattached content database in SharePoint Server

You can recover content from an unattached content database by using PowerShell. The following procedure shows how to use the  `Get-SPContentDatabase` cmdlet to recover content from an unattached content database. You can also import a list or document library with the  `Import-SPWeb` cmdlet. For more information, see Import a list or document library in SharePoint Server.

**To recover content from an unattached content database by using PowerShell**

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
Get-SPContentDatabase -ConnectAsUnattachedDatabase  -DatabaseName <DatabaseName> -DatabaseServer <DatabaseServer>
```

Where:

*<DatabaseName>* is the name of the unattached database from which you want to recover content.

*<DatabaseServer>* is the name of the database server that hosts the unattached database from which you want to recover content.

For more information, see Get-SPContentDatabase.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

Using Central Administration to recover content from an unattached content database in SharePoint Server

## Using Central Administration to recover content from an unattached content database in SharePoint Server

You can recover content from an unattached content database by using Central Administration.

**To recover content from an unattached content database by using Central Administration**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group and is a member of the **db_owner** fixed database role.

Start Central Administration.

In Central Administration, on the home page, click **Backup and Restore**.

On the Backup and Restore page, in the **Granular Backup** section, click **Recover data from an unattached content database**.

On the Unattached Content Database Data Recovery page, type the database server name in the **Database Server** text box and type the database name in the **Database Name** text box.

Select the database authentication method that you want to use.

Select the **Browse content** option, and then click **Next**.

On the Browse content page, select the site collection, site, and or list that you want to restore, select the **Backup site collection** or **Export site or list** option, and then click **Next**.

Type the file location where you want to store the backup file, and then click **Start Backup**. For more information about using the **Backup site collection** option, see Back up site collections in SharePoint Server.

If you chose **Export site or list** in the previous page, you must select **Export Full Security** and choose the version that you want to export in the **Export Versions** drop-down menu. For more information about using the **Export site or list** option, see Export sites, lists, or document libraries in SharePoint Server.

See also

## See also

Concepts

#### Concepts

Prepare to back up and restore farms in SharePoint Server

Attach or detach content databases in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
