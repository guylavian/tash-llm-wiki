---
title: "Attach or detach content databases in SharePoint Server - SharePoint Server"
description: "Learn how to attach and detach content databases to your SharePoint Server farm."
ms.topic: how-to
---
Note

Attach or detach content databases in SharePoint Server

# Attach or detach content databases in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can attach or detach SharePoint Server content databases by using the SharePoint Central Administration website or Microsoft PowerShell

Before you begin

## Before you begin

Before you begin this operation, review the following information:

If you want to create a new content database while you attach it, the SharePoint farm service account must be a member of the SQL Server **dbcreator** fixed server role. To attach a content database to a web application, the SharePoint farm service account must have **db_owner** permission for the content database.

If the database already exists, it must be the same version as the SharePoint Server 2016 farm or this operation will fail. To attach a content database that is a different version than the farm, use the To attach or detach a content database by using Windows PowerShell procedure in the following section.

Attaching and detaching content databases

## Attaching and detaching content databases

You might want to attach or detach content databases for the following reasons. You want to add a new content database for new site collections to keep content databases at a manageable size. You are restoring a content database from another farm and you want the sites that it contains to be accessed from a web application. You have archived site collections out of a content database and then detach the content database from the web application. For more information, see Move site collections between databases in SharePoint Server

The steps to add a database and to attach a database are very similar. For more information about how to add a database, see Add content databases in SharePoint Server.

To attach a content database by using Central Administration

### To attach a content database by using Central Administration

Verify that the user account that is being used to perform this operation is a member of the Farm Administrators SharePoint group.

Start Central Administration.

On the SharePoint Central Administration website, click **Application Management**.

On the **Application Management** page, in the **Databases** section, click **Manage content databases**.

On the **Manage Content Databases** page, click **Add a content database**.

On the **Add Content Database** page:

Use the Web Application drop-down menu to select the web application to which you want to attach a content database.

Specify the database server that hosts the database.

Specify the database name. If the database does not already exist, it will be created.

Specify the authentication method for the database, and supply an account name and password if you are using SQL authentication.

Note

The account name and password must already exist as a SQL Server login. We recommend that you use Windows authentication instead of SQL authentication because, by default, SQL authentication sends a nonencrypted password to the computer that is running SQL Server. If you use SQL authentication, the SQL account requires the same SQL permissions as the SharePoint farm service account.

Click **OK**.

To detach a content database by using Central Administration

### To detach a content database by using Central Administration

Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.

On the SharePoint Central Administration website, click **Application Management**.

On the **Application Management** page, in the **Databases** section, click **Manage content databases**.

Select the web application for which you want to detach a content database.

Click the content database that you want to detach.

On the **Manage Content Database Settings** page, select the **Remove content database** check box.

If the content database contains data, you will receive a warning. Click **OK** to continue with the operation.

Click **OK** to confirm the detachment, or click **Cancel** to stop the operation without detaching the database.

After detaching the content database in Central Administration, the content database still exists in SQL Server. If you want to permanently remove the content database, you must do so by using a SQL Server procedure.

To attach or detach a content database by using PowerShell

### To attach or detach a content database by using PowerShell

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Open **SharePoint Management Shell**.

At the PowerShell command prompt, type the appropriate command

**To attach an existing content database:**

```
Mount-SPContentDatabase "<ContentDb>" -DatabaseServer "<DbServer>" -WebApplication http://SiteName
```

Where:

*<ContentDb>* is the content database to be attached.

*<DbServer>* is the name of the database server.

*http://SiteName* is the name of the web application to which the content database is being attached.

**To detach a content database:**

```
Dismount-SPContentDatabase "<ContentdBName>"
```

Where  *<ContentdBName>* is the name of the content database.

Important

If you have multiple content databases that have the same name, you must use the content database GUID in this command instead of using the content database name. To retrieve the GUID of the content database, run the **Get-SPContentDatabase** cmdlet with no arguments.

The **Dismount-SPContentDatabase** cmdlet detaches the content database from the web application, but it does not delete the content database from SQL Server. After a content database is detached, you cannot delete it by using PowerShell. You can only remove it by using SQL Server tools. If you want to delete the content database from SQL Server while you detach it, use the **Remove-SPContentDatabase** cmdlet instead.

For more information, see Dismount-SPContentDatabase and Mount-SPContentDatabase.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

See also

## See also

Other Resources

#### Other Resources

Get-SPContentDatabase

New-SPContentDatabase

Remove-SPContentDatabase

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
