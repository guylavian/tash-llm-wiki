---
title: "Overview of the upgrade process to SharePoint Server Subscription Edition - SharePoint Server"
type: reference
domain: sharepoint
slug: upgrade-and-update-overview-of-the-upgrade-process-subscription-edition
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/upgrade-and-update/overview-of-the-upgrade-process-subscription-edition
family: upgrade-and-update
documentKind: "upgrade-and-migration-article"
abstract: "Learn about the process of upgrading databases, service applications, My Sites, and site collections to SharePoint Server Subscription Edition."
---

# Overview of the upgrade process to SharePoint Server Subscription Edition - SharePoint Server

Note

Overview of the upgrade process to SharePoint Server Subscription Edition

# Overview of the upgrade process to SharePoint Server Subscription Edition

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

To upgrade from Microsoft SharePoint Server 2019 and Microsoft SharePoint Server 2016 to SharePoint Server Subscription Edition, you use the database-attach method. In the database-attach method, you first create and configure a SharePoint Server Subscription Edition farm. Then you copy the content and service application databases from SharePoint Server 2019 and SharePoint Server 2016, and then attach and upgrade the databases. This upgrades the data to the new version. Site owners can then upgrade individual site collections.

SharePoint Server Subscription Edition supports an upgrade from RTM version of SharePoint Server 2019 and SharePoint Server 2016.

Note

All databases must be upgraded to version 16.0.4351.1000 or higher, otherwise upgrade to SharePoint Server Subscription Edition will be blocked.

After you've configured a new SharePoint Server Subscription Edition environment, you can copy the content and service application databases from SharePoint Server 2019 and SharePoint Server 2016 to the SharePoint Server Subscription Edition environment. You use a backup and restore process to copy the database. You can also choose to set the databases to read-only in SharePoint Server 2019 and SharePoint Server 2016 environments so that users can continue to access their information, but not change it.

Before you attach and upgrade the content databases, review the following information and take any recommended actions.

Ensure that the account that you use to attach the databases is a member of the **db_owner fixed** database role for the content databases that you want to upgrade.

Ensure that the account that you use to create web applications is a member of the Farm administrators group in the SharePoint Central Administration website.

This article helps you to understand the upgrade sequence so that you can plan an upgrade project. To get detailed steps for an upgrade, see Overview of the upgrade process to SharePoint Server Subscription Edition and Upgrade site collections to SharePoint Server Subscription Edition.

Create the SharePoint Server Subscription Edition farm

## Create the SharePoint Server Subscription Edition farm

The first stage in the upgrade process creates the new SharePoint Server Subscription Edition farm:

A server farm administrator installs SharePoint Server Subscription Edition to a new farm. The administrator configures farm settings and tests the environment.

A server farm administrator sets the SharePoint Server 2019 and SharePoint Server 2016 farms to read-only so that users can continue to access the old farm while upgrade is in progress on the new farm.

Copy the SharePoint Server 2019 and SharePoint Server 2016 databases

## Copy the SharePoint Server 2019 and SharePoint Server 2016 databases

The second stage in the upgrade process copies the databases to the new environment. You use SQL Server Management Studio for these tasks.

With the farm and databases in read-only mode, a server farm administrator backs up the content and service application databases from the SQL Server instance on the SharePoint Server 2019 and SharePoint Server 2016 farms.

The server farm administrator restores a copy of the databases to the SQL Server instance on the SharePoint Server Subscription Edition farm and sets the databases to read-write on the new farm.

Upgrade SharePoint Server 2019 and SharePoint Server 2016 databases and service applications

## Upgrade SharePoint Server 2019 and SharePoint Server 2016 databases and service applications

The third stage in the upgrade process upgrades the databases and service applications.

A server farm administrator configures the service applications for the new farm. The following service applications have databases that you can upgrade during this process:

Business Data Connectivity service application

Managed Metadata service application

Search service application

Secure Store Service application

User Profile service application

A server farm administrator creates a web application on the SharePoint Server Subscription Edition farm for each web application on the SharePoint Server 2019 and SharePoint Server 2016 farms.

A server farm administrator installs all server-side customizations.

A server farm administrator then attaches the content databases to the new farm and upgrades the content databases for those web applications.

A server farm administrator confirms that the upgrade is successful.

Upgrade SharePoint Server 2019 and SharePoint Server 2016 site collections

## Upgrade SharePoint Server 2019 and SharePoint Server 2016 site collections

The final stage in the upgrade process is to upgrade the site collections. The upgrade process for My Sites is slightly different from other types of site collections.

Upgrade My Sites

### Upgrade My Sites

Important

This section applies to SharePoint Server Subscription Edition only.

A server farm administrator upgrades the My Site host and then individual users can upgrade their My Sites or the farm administrator can upgrade them by using PowerShell. The following list shows four stages for the My Site host and My Sites during the upgrade process:

The My Site host has not been upgraded. My Sites cannot be upgraded yet.

A server farm administrator has upgraded the My Site host. No My Sites have been upgraded.

Some users have upgraded their My Sites.

All My Sites have been upgraded.

Note

A server farm administrator can choose to force an upgrade of My Sites without waiting for users to upgrade them. For details and steps, read Upgrade site collections to SharePoint Server Subscription Edition.

Upgrade other SharePoint Server 2019 and SharePoint Server 2016 site collections

### Upgrade other SharePoint Server 2019 and SharePoint Server 2016 site collections

For information about how to upgrade a site collection, see Upgrade site collections to SharePoint Server Subscription Edition.

Note

A server farm administrator can also force specific site collections to be upgraded without waiting for the site owners to upgrade them. For details and steps, read Upgrade site collections to SharePoint Server Subscription Edition.

Additional resources

## Additional resources

- Last updated on 
		2023-01-26
