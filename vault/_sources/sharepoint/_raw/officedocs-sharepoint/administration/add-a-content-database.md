---
title: "Add content databases in SharePoint Server - SharePoint Server"
description: "Learn how to add a content database to your SharePoint Server farm."
ms.topic: how-to
---
Note

Add content databases in SharePoint Server

# Add content databases in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can add a content database to a SharePoint Server farm by using the SharePoint Central Administration website or Microsoft PowerShell. The tool that you use depends on the kind of environment that you have deployed, your schedule requirements, and service level agreements that you have made with your organization.

Before you begin

## Before you begin

You can add a new content database or attach an existing content database from a backup file.

Before you begin this operation, review the following information about prerequisites:

The user account that is performing this operation must be a member of the Farm Administrators SharePoint group.

If you use Windows authentication to connect to SQL Server, the user account must be a member of the **dbcreator** fixed server role on the SQL Server instance where the database is to be created.

Adding a content database to a SharePoint Server web application

## Adding a content database to a SharePoint Server web application

You can use the procedures that are described in this article to create a new content database and attach it to a web application. If you are using Windows authentication to connect to SQL Server, the user account must also be a member the SQL Server **dbcreator** fixed server role on the SQL Server instance where the database will be created. If you are using SQL authentication to connect to SQL Server, the SQL authentication account that you specify when you create the content database must have **dbcreator** permission on the SQL Server instance where the database will be created.

To add a content database to a web application by using Central Administration

### To add a content database to a web application by using Central Administration

Verify that the user account that is performing this operation is a member of the Farm Administrators SharePoint group.

Start Central Administration.

On the SharePoint Central Administration website, click **Application Management**.

In the **Databases** section, click **Manage content databases**.

On the **Manage Content Databases** page, click **Add a content database**.

On the **Add Content Database** page:

Specify a web application for the new database.

Specify a database server to host the new database.

Specify the authentication method that the new database will use and supply an account name and password, if they're necessary.

Important

The account name and password must already exist as a SQL Server login.

Specify the name of the failover database server, if one exists.

Specify the number of top-level sites that can be created before a warning is issued. By default, this is 2,000.

Specify the total number of top-level sites that can be created in the database. By default, this is 5,000.

Click **OK**.

To add a content database to a web application by using PowerShell

### To add a content database to a web application by using PowerShell

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Open **SharePoint Management Shell**.

At the PowerShell command prompt, type the following command:

```
New-SPContentDatabase -Name <ContentDbName> -WebApplication <WebApplicationName>
```

Where:

*<ContentDbName>* is the name of the content database to create.

*<WebApplicationName>* is the name of the web application to which the new database is attached.

For more information, see New-SPContentDatabase.

Note

To attach an existing content database to a web application, use the Microsoft PowerShell cmdlet **Mount-SPContentDatabase**. For more information, see Mount-SPContentDatabase.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

See also

## See also

Concepts

#### Concepts

Attach or detach content databases in SharePoint Server

Move site collections between databases in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
