---
title: "Disable RBS on content databases in SharePoint Server - SharePoint Server"
description: "Learn how to disable Remote BLOB Storage (RBS) on any SharePoint Server content database."
ms.topic: how-to
---
Note

Disable RBS on content databases in SharePoint Server

# Disable RBS on content databases in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can disable Remote BLOB Storage (RBS) on any content database. After you disable RBS on a content database, binary large objects (BLOBs) are stored inline in SQL Server for all subsequent writes to the content database. This article describes how to disable RBS on a content database.

You can disable RBS on a content database by setting the active provider name to the empty string in Microsoft PowerShell. Each content database has a **RemoteBlobStorageSettings** property that can be used to invoke the **SetActiveProviderName** method.

This action does not change the storage location of any BLOBs that have previously been stored in RBS or inline storage. Disabling RBS does not uninstall RBS. We do not recommend that you uninstall RBS.

Before you begin this operation, review the following information about prerequisites:

Disable RBS for a content database

## Disable RBS for a content database

This operation can be performed on any Web server in the farm. You only have to perform the operation one time on one Web server for each content database for which you want to disable RBS.

Caution

Do not use the **Disable()** method on the **RemoteBlobStorageSettings** object. This method is used only to uninstall RBS, and we do not recommend that you just disable the writing of new BLOBs into RBS. To completely remove RBS, perform the below task and then use Move-SPSite to move all sites into a non-RBS enabled database. This will allow you to delete the content database that previously had RBS enabled.

You must use Microsoft PowerShell cmdlets to disable RBS. There is no user interface option for this task.

**To disable RBS by using PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following commands:

```
$site=Get-SPSite "<http://yourSiteURL>"
$rbss=$site.ContentDatabase.RemoteBlobStorageSettings
$rbss.SetActiveProviderName("")
```

Where  http://yourSiteURL is the Web application that is attached to the content database that is being disabled for RBS.

For more information, see Get-SPSite.

See also

## See also

Concepts

#### Concepts

Set a content database to use RBS with FILESTREAM in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
