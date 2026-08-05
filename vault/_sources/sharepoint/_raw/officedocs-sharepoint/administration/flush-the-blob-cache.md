---
title: "Flush the BLOB cache in SharePoint Server - SharePoint Server"
description: "Learn how to clear the contents of the BLOB cache for a web application in SharePoint Server."
ms.topic: how-to
---
Note

Flush the BLOB cache in SharePoint Server

# Flush the BLOB cache in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

A BLOB cache is a disk-based cache that stores binary large objects (BLOBs) such as frequently used image, audio, and video files, and other files that are used to display web pages. Each SharePoint front-end server maintains its own BLOB cache. When you enable a BLOB cache, you specify the file types to include in the cache and also the location of the BLOB cache. The first time that a BLOB file is requested, the file is copied from the database to the BLOB cache on the front-end server. Future requests to the front-end server for that same file are then served from the file that is stored in the BLOB cache, instead of being served from the database. This reduces the network traffic and the load on the database server.

For more information about BLOB caches, see Plan for caching and performance in SharePoint Server.

Flush the BLOB cache

## Flush the BLOB cache

When you flush the BLOB cache, you clear the contents of the BLOB cache for a web application. This is useful if the BLOB cache becomes out of sync with the content. For example, after you restore a content database, the BLOB cache will be out of sync with the content. To correct that situation, you must flush the BLOB cache. The following procedure describes how to flush the BLOB cache for a web application.

Caution

Flushing the BLOB cache for a web application affects all site collections in the web application.

Note

You cannot use the user interface to flush the BLOB cache. Instead, you use Microsoft PowerShell and the SharePoint object model to complete this task.

**To flush the BLOB cache**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running PowerShell cmdlets.

Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and Add-SPShellAdmin.

- Copy the following code and paste it into a text editor, such as Notepad.

```
$webApp = Get-SPWebApplication "<WebApplicationURL>"
[Microsoft.SharePoint.Publishing.PublishingCache]::FlushBlobCache($webApp)
Write-Host "Flushed the BLOB cache for:" $webApp
```

Replace  *<WebApplicationURL>* with the URL of the web application whose BLOB cache you want to clear.

Save the file, and name it FlushBLOBCache.ps1.

Note

You can use a different file name, but you must save the file as an ANSI-encoded text file that has the file name extension .ps1.

Open **SharePoint Management Shell**.

Change to the directory where you saved the file.

At the Microsoft PowerShell command prompt, type the following command.

```
./FlushBLOBCache.ps1
```

See also

## See also

Other Resources

#### Other Resources

Scripting with Windows PowerShell

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
