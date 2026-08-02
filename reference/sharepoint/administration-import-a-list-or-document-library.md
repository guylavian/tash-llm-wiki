---
title: "Import a list or document library in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-import-a-list-or-document-library
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/import-a-list-or-document-library
family: administration
documentKind: "how-to"
abstract: "Learn how to import a site, list, or document library in SharePoint Server."
---

# Import a list or document library in SharePoint Server - SharePoint Server

Note

Import a list or document library in SharePoint Server

# Import a list or document library in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can import a site, list, or document library in SharePoint Server by using PowerShell.

Before you begin

## Before you begin

Although you can use either PowerShell or Central Administration to export a site, list, or document library, you can use only PowerShell to import a site, list, or document library. For information about how to export lists or libraries, see Export sites, lists, or document libraries in SharePoint Server.

Before you begin this operation, review the following information:

You can use importing as a method of restoring the items, or as a method of moving or copying the items from one farm to another farm. You can import a site, list, or document library from a backup of the current farm, from a backup of another farm, or from a read-only content database. To import from a read-only content database, you must first attach the read-only database. For more information, see Attach and restore read-only content databases in SharePoint Server.

You cannot import a site, list or document library exported from one version of SharePoint Server to another version of SharePoint Server.

Importing a site, list, or document library in SharePoint Server

## Importing a site, list, or document library in SharePoint Server

You can use PowerShell to manually import a site, list, or document library or as part of a script that can be run regularly.

**To import a site, list or document library by using PowerShell**

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
Import-SPWeb -Identity  <SiteURL>  -Path <ImportFileName>  [-Force] [-NoFileCompression] [-Verbose]
```

Where:

*<SiteURL>* is the URL for the site that you are importing to.

*<ImportFileName>* is the name of the file that you are exporting from.

Important

The site or subsite that you are importing must have a template that matches the template of the site specified by  `Identity`.

You can also use the  `Get-SPWeb` cmdlet and pass the ID to  `Import-SPWeb` by using the PowerShell pipeline. The value of the  `Path` parameter specifies the path and file name of the file from which to import the list or library. To include the user security settings with the list or document library, use the  `IncludeUserSecurity` parameter. To overwrite the list or library that you specified, use the  `Force` parameter. You can use the  `UpdateVersions` parameter to specify how versioning conflicts will be handled. To view the progress of the operation, use the  `Verbose` parameter.

The  `NoFileCompression` parameter lets you specify that no file compression is performed during the import process. Using this parameter can lower resource usage up to 30% during the export and import process. If you are importing a site, list, or document library that you exported from Central Administration, or if you exported a site, list, or document library by using PowerShell and you did not use the  `NoFileCompression` parameter in the  `Export-SPWeb` cmdlet, you cannot use this parameter in the  `Import-SPWeb` cmdlet.

Note

There is no facility in the  `Import-SPWeb` cmdlet to import a subset of the items within the export file. Therefore, the import operation will import everything from the file.

For more information, see Import-SPWeb.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

See also

## See also

Concepts

#### Concepts

Export sites, lists, or document libraries in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
