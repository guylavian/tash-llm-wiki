---
title: "Restart a database-attach upgrade or a site collection upgrade to SharePoint 2013 - SharePoint Server"
type: reference
domain: sharepoint
slug: upgrade-and-update-restart-a-database-attach-upgrade-or-a-site-collection-upgrade-to-sharepoint-201
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/upgrade-and-update/restart-a-database-attach-upgrade-or-a-site-collection-upgrade-to-sharepoint-201
family: upgrade-and-update
documentKind: "upgrade-and-migration-article"
abstract: "Learn how to restart a database-attach upgrade or a site collection upgrade to SharePoint 2013."
---

# Restart a database-attach upgrade or a site collection upgrade to SharePoint 2013 - SharePoint Server

Note

Restart a database-attach upgrade or a site collection upgrade to SharePoint 2013

# Restart a database-attach upgrade or a site collection upgrade to SharePoint 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

In some cases, you might have to restart upgrade to finish a database-attach upgrade from SharePoint 2010 Products to SharePoint 2013. For example: if a template or language pack is missing from the environment, or if you lose the connection to SQL Server, you will have to resolve the issue and then restart upgrade. You might also need to retry or restart a site collection upgrade if it was unable to complete.

Note

One frequent cause of failures during upgrade is that the environment is missing customized features, solutions, or other elements. Be sure that any custom elements that you must have are installed on your front-end web servers before you start the upgrade process. You can use the **Test-SPContentDatabase** Microsoft PowerShell cmdlet to identify any custom elements that your sites might be using. For more information, see Use a trial upgrade to SharePoint 2013 to find potential issues in the article "Use a trial upgrade to find potential issues."

Restart upgrade for a database by using PowerShell

## Restart upgrade for a database by using PowerShell

If the upgrade ran into issues during the database-attach upgrade, you can restart the upgrade process for the database after you have addressed the issue by using a Microsoft PowerShell cmdlet.

**To restart upgrade for a database by using PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

On the **Start** menu, click **All Programs**.

Click **SharePoint 2013**.

Click **SharePoint 2013 Management Shell**.

At the Microsoft PowerShell command prompt (PS C:\>), type the following command:

```
Upgrade-SPContentDatabase <Name>
```

Where:

- *Name* is the database name that you want to upgrade.

You can also use the **-id** parameter and provide the database GUID instead of a database name. You can run the following cmdlet to find the GUID for a content database:

```
Get-SPContentDatabase -Identity <content_database_name>
```

For more information, see Upgrade-SPContentDatabase and Get-SPContentDatabase.

Restart upgrade for a site collection

## Restart upgrade for a site collection

If upgrade ran into issues during a site collection upgrade, you can restart the upgrade process for the site collection after you have addressed the issue. You can use either the Site Settings page or a PowerShell cmdlet to restart upgrade for a site collection.

**To restart upgrade for a site collection**

Verify that the user account that performs this procedure is a site collection administrator.

On the Site Settings page for the site collection, in the **Site Collection Administration** section, click **Site collection upgrade**.

On the Site Collection Upgrade page, click **Upgrade this Site Collection**.

This option starts to upgrade your site collection. A box opens to verify that you want to start the process.

Click **I'm ready** to start the actual upgrade.

Note

The site collection health checks are run automatically in repair mode before the upgrade starts. The results from the health checks are included in the upgrade log for the site collection. If there is an error, you must address it before you can continue to upgrade.

The upgrade starts, and the **Upgrade status** page for the site collection is displayed. This page automatically updates while the upgrade is in progress and displays information about the process, such as the following:

Errors or warnings

When the upgrade started

Where you can find the upgrade log file

After the upgrade is complete, the **Upgrade status** page is displayed in the new user interface with the message, Upgrade Completed Successfully.

- Click **Let's see the new site** to go to the home page.

Farm administrators can restart upgrade by using PowerShell.

**To restart upgrade for a site collection by using PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

On the **Start** menu, click **All Programs**.

Click **SharePoint 2013**.

Click **SharePoint 2013 Management Shell,**.

At the PowerShell command prompt, type the following command:

```
Upgrade-SPSite <http://site> -VersionUpgrade [-Unthrottled]
```

Where:

*<http://site>* is the URL for the site collection.

Add the option **-Unthrottled** option to skip the site collection upgrade queue and start the upgrade immediately.

For more information, see Upgrade-SPSite.

See also

## See also

Other Resources

#### Other Resources

Upgrade from SharePoint 2010 to SharePoint 2013

Additional resources

## Additional resources

- Last updated on 
		2023-01-26
