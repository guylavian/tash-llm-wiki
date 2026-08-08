---
title: "Attach and restore read-only content databases in SharePoint Server - SharePoint Server"
description: "Learn how to attach and restore a read-only content database in SharePoint Server."
ms.topic: how-to
---
Note

Attach and restore read-only content databases in SharePoint Server

# Attach and restore read-only content databases in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can attach and restore a read-only content database in SharePoint Server by using PowerShell.

Before you begin

## Before you begin

A SharePoint Server farm in which content databases are set to be read-only can be part of a failure recovery environment that runs against mirrored or log-shipped content databases or part of a highly available maintenance or patching environment that provides user access when another version of the farm is being updated.

Before you begin this operation, review the following information about prerequisites:

When you re-attach the read-only databases, they become read-write.

For more information about how to use read-only databases, see Run a farm that uses read-only databases in SharePoint Server.

Using PowerShell to attach and restore a read-only content database

## Using PowerShell to attach and restore a read-only content database

You can use only PowerShell to attach and restore a read-only content database.

**To attach and restore a read-only content database by using PowerShell**

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
Mount-SPContentDatabase -Name <DatabaseName> -WebApplication <WebApplicationID> [-Verbose]
```

Where:

*<DatabaseName>* is name of the read-only database.

*<WebApplicationID>* is ID assigned to the read-only database.

Note

Attaching a content database by using the  `Mount-SPContentDatabase` cmdlet differs from attaching a database in SQL Server by using SQL Server tools.  `Mount-SPContentDatabase` associates the content database with a Web application so that the contents can be read.

For more information, see Mount-SPContentDatabase.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

See also

## See also

Concepts

#### Concepts

Overview of backup and recovery in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
