---
title: "High level overview to upgrade from SharePoint 2013 to SharePoint Server 2019 - SharePoint Server"
description: "Learn the overview steps required to upgrade SharePoint Server 2013 environment to SharePoint Server 2019."
ms.topic: concept-article
---
Note

High level overview to upgrade from SharePoint 2013 to SharePoint Server 2019

# High level overview to upgrade from SharePoint 2013 to SharePoint Server 2019

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Important

When planning to upgrade from an older SharePoint Server to SharePoint Server 2019, note that it will reach its end-of-life (EOL) stage on July 14th, 2026. It's advisable to upgrade directly to SharePoint Server Subscription Edition.

Overview

## Overview

The upgrade scenario hasn't changed in SharePoint Server 2019. There's no direct upgrade path from 2013 to 2019. To upgrade to SharePoint Server 2019, you must upgrade SharePoint 2013 to SharePoint Server 2016, and then upgrade to SharePoint Server 2019. Your databases must be at a SharePoint Server 2016 RTM version or higher when you upgrade to SharePoint Server 2019. Any database with a lower version is locked and upgrade doesn't start.

For a visual look of the high-level steps, see

| File Type | Download Location |
| --- | --- |
| Visio | Upgrade from SharePoint 2013 to SharePoint Server 2019 |
| PDF | Upgrade from SharePoint 2013 to SharePoint Server 2019 |

Note

The steps for creating and restoring service applications only applies to these six:

- Secure Store service application

- Business Data Connectivity service application

- Managed Metadata service application

- PerformancePoint Services service application

- User Profile service application

- Search service application

For the specific, end to end steps to upgrade SharePoint 2013 to SharePoint Server 2016, see Upgrade to SharePoint Server 2016

Steps to Upgrade

## Steps to Upgrade

2013

### 2013

In SharePoint 2013, if you have any web applications that are in windows authentication mode, you should convert them to claims authentication. Claims authentication is the default mode in SharePoint Server 2016 and SharePoint Server 2019.

Next, upgrade all the site collections from 14 mode to 15 mode by using the Upgrade-SPSite cmdlet. Any database with a 14 version is locked and prevented from upgrading to SharePoint Server 2016. After the site collections are upgraded, create a backup of all content and service application databases from your old farm (for example, SQL2013). Restore these databases to a new farm's SQL Server in SharePoint Server 2016 (for example, SQL2016).

2016

### 2016

In SharePoint Server 2016, build a new temporary farm that includes service applications. When the service applications are created use the existing database names that reside on SQL2016. After the new farm is created, create a new web application with a temporary database. Install any full trust solutions, administrator approved InfoPath forms, etc. Dismount the temporary content database from the web application.

Note

You may need to delete the temporary content database from the SQL Server.

Start the upgrade process to SharePoint Server 2016 by running the Mount-SPContentDatabase cmdlet on the restored content databases from SQL2016. After the upgrade process is complete, perform any individual configuration changes that aren't part of the service application and content databases, such as incoming/outgoing email settings, etc.

2019

### 2019

The steps to upgrade from SharePoint Server 2016 to SharePoint Server 2019 are the same as going from SharePoint 2013 to SharePoint Server 2016 except for converting web applications to claims authentication and upgrading database modes to level 15. These are not required.

Create a backup of all content and service application databases from your temporary farm (for example, SQL2016). Restore these databases to a new farm's SQL Server in SharePoint Server 2019 (for example, SQL2019).

In SharePoint Server 2019, build a new farm that includes service applications. When the service applications are created use the existing database names that reside on SQL2019. After the new farm is created, create a new web application with a temporary database.  Install any full trust solutions, administrator approved InfoPath forms, etc. Dismount the temporary content database from the web application.

Note

You may need to delete the temporary content database from the SQL Server.

Start the upgrade process to SharePoint Server 2019 by running the Mount-SPContentDatabase cmdlet on the restored content databases from SQL2019. After the upgrade process is complete, perform any individual configuration changes that are not part of the service application and content databases, such as incoming/outgoing email settings, etc.

See Also

## See Also

Overview of the upgrade process to SharePoint Server 2019

Additional resources

## Additional resources

- Last updated on 
		2024-11-22
