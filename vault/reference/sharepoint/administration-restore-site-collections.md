---
title: "Restore site collections in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-restore-site-collections
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/restore-site-collections
family: administration
documentKind: "how-to"
abstract: "Learn how to restore a single site collection in SharePoint Server."
---

# Restore site collections in SharePoint Server - SharePoint Server

Note

Restore site collections in SharePoint Server

# Restore site collections in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can only restore a site collection in SharePoint Server by using PowerShell.

Using PowerShell to restore a site collection in SharePoint Server

## Using PowerShell to restore a site collection in SharePoint Server

You can use PowerShell to restore a site collection manually or as part of a script that can be run at scheduled intervals.

**To restore a site collection by using PowerShell**

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
Restore-SPSite -Identity <SiteCollectionURL> -Path <Backup file> [-DatabaseServer <DatabaseServerName>] [-DatabaseName <ContentDatabaseName>] [-HostHeader <Host header>] [-Force] [-GradualDelete] [-Verbose]
```

Where:

*<SiteCollectionURL>* is URL for the site collection you want to restore.

*<DatabaseServerName>* is name of the database server where the site collection resides.

*<ContentDatabaseName>* is the name of the content database.

If you want to restore the site collection to a specific content database, use the  `DatabaseServer` and  `DatabaseName` parameters to specify the content database. If you do not specify a content database, the site collection will be restored to a content database chosen by SharePoint Server.

If you are restoring a host-named site collection, use the  `Identity` parameter to specify the URL of the host-named site collection and use the  `HostHeader` parameter to specify the URL of the Web application that will hold the host-named site collection.

If you want to overwrite an existing site collection, use the  `Force` parameter.

Note

If the site collection that you are restoring is 1 gigabyte or larger, you can use the **GradualDelete** parameter for better performance during the restore process. When this parameter is used, the site collection that is overwritten is marked as deleted, which immediately prevents any additional access to its content. The data in the marked site collection is then deleted gradually over time by a timer job instead of all at the same time, which reduces the impact on server performance.

For more information, see Restore-SPSite.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

See also

## See also

Concepts

#### Concepts

Back up site collections in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
