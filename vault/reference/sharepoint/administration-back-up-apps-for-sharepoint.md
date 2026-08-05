---
title: "Back up apps for SharePoint in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-back-up-apps-for-sharepoint
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/back-up-apps-for-sharepoint
family: administration
documentKind: "how-to"
abstract: "Learn how to back up apps for SharePoint in SharePoint Server."
---

# Back up apps for SharePoint in SharePoint Server - SharePoint Server

Note

Back up apps for SharePoint in SharePoint Server

# Back up apps for SharePoint in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

We recommend that you regularly back up at the farm level. However, business or IT requirements might require you to back up the apps for SharePoint in addition to normal farm backups. If you regularly back up the apps for SharePoint environment, you reduce the possibility of data losses that might occur from hardware failures, power outages, or other problems. It is a simple process that helps make sure that data and configurations that compose the apps for SharePoint environment are available for recovery, if that is required.

The app for SharePoint content and packages are in the SharePoint Server content databases in individual site collections. All app for SharePoint license and security data is stored in the App Management Service and the Secure Store Service application databases. Additional app for SharePoint data is stored in the SharePoint Server configuration database, in the form of Internet Information Services (IIS) web sites or web applications, and Web Part packages. You must back up the following SharePoint Server databases at the same time:

Content - WSS_Content

Configuration - SharePoint_Config

Secure Store Service application - Secure_Store_Service_DB_<GUID>

App Management service application - App_Management_<GUID>

If you have to eventually restore the databases, you have to restore the same version of each database that you backed up. In other words, don't restore a content database that's six months older than the configuration database.

You can back up an apps for SharePoint environment by using the SharePoint Central Administration website, Microsoft PowerShell, or SQL Server tools.

Back up content databases

## Back up content databases

Content databases can store data for multiple site collections. However, if you have many site collections, we recommend that you add enough content databases to keep the size of each database below 200 GB for optimal system performance. For more information, see Back up content databases in SharePoint Server.

Note

SharePoint Server content databases become very large. We recommend that you back up each content database as a separate process from other database or farm backups.

Back up the configuration database

## Back up the configuration database

The SharePoint Server configuration database stores data about all SharePoint databases and Internet Information Services (IIS) web sites or web applications. This includes trusted solutions, web part packages, site templates, and web application settings, and farm settings that are specific to SharePoint Server, such as default quota and blocked file types. For more information, see Back up farm configurations in SharePoint Server.

Back up the Secure Store Service application database

## Back up the Secure Store Service application database

The Secure Store Service database stores and maps credentials such as account names and passwords. To back up the Secure Store database for an apps for SharePoint environment, see Back up the Secure Store Service in SharePoint Server.

Note

Make sure that you record the passphrase when you back up the Secure Store database. You must have the passphrase available to restore the Secure Store database.

Back up the App Management service application database

## Back up the App Management service application database

The App Management service application database stores the app licenses and permissions for all apps downloaded from the App Catalog site in SharePoint Server. To back up the App Management database, follow the same procedures as most other SharePoint Server service applications. For more information, see Back up service applications in SharePoint Server.

Back up a site collection

## Back up a site collection

You may have multiple site collections that host apps for SharePoint in your environment. When you backup apps for SharePoint you must also back up all site collections where the apps are hosted.

**To back up a site collection by using PowerShell**

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
Backup-SPSite -Identity <SiteCollectionGUIDorURL> -Path <BackupFile> [-Force] [-NoSiteLock] [-UseSqlSnapshot] [-Verbose]
```

Where:

*<SiteCollectionGUIDorURL>* is the ID or URL for the site collection you want to back up.

*<BackupFile>* is the path of where the backup file is located.

If you want to overwrite a previously used backup file, use the  `Force` parameter. You can use the  `NoSiteLock` parameter to keep the read-only lock from being set on the site collection while it is being backed up. However, using this parameter can enable users to change the site collection while it is being backed up and could lead to possible data corruption during backup. To display the site collection GUID or URL at the PowerShell command prompt, type the following command:

```
Get-SPSite | format-list -property id,url
```

If the database server is running an Enterprise Edition of SQL Server, we recommend that you also use the  `UseSqlSnapshot` parameter for more consistent backups. You can also export sites or lists from these snapshots.

Note

If the RBS provider that you are using does not support snapshots, you can't use snapshots for content deployment or backup. For example, the SQL FILESTREAM provider does not support snapshots.

For more information about how to use SQL snap-shots, see Back up databases to snapshots in SharePoint Server.

For more details, see Back up site collections in SharePoint Server

For more information, see Backup-SPSite.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

See also

## See also

Concepts

#### Concepts

Plan for backup and recovery in SharePoint Server

Restore apps for SharePoint in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
