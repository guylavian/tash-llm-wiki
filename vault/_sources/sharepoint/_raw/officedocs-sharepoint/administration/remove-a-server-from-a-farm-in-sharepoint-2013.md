---
title: "Remove a server from a farm in SharePoint 2013 - SharePoint Server"
description: "Learn how to remove a web server, application server, or database server from a SharePoint 2013 farm."
ms.topic: how-to
---
Note

Remove a server from a farm in SharePoint 2013

# Remove a server from a farm in SharePoint 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

There are three types of servers in a server farm running SharePoint 2013: web servers, application servers, and database servers. The method that you use to remove a server from a SharePoint farm varies depending on the type of server that you are removing from the farm.

Removing a web server or application server from a SharePoint farm

## Removing a web server or application server from a SharePoint farm

For information about uninstallation procedures that SharePoint 2013 supports, see Uninstall SharePoint 2013.

Removing a server that contains a search topology component can affect future search activities. The extent of that effect depends on the farm search topology. We recommend that you remove or relocate any search topology components from a server before removing the server from the farm.

If you remove a server that hosts a crawl component, no index files are lost. However, you might reduce or remove the capacity to crawl content.

You can lose index files in the following situations:

The farm has only one query component, and you remove the server that hosts the query component.

You have configured the index to be partitioned and you delete the last query component in one of the partitions. In this case, you will lose a portion of the index.

In either of these cases, a full crawl will have to be performed to re-create the index files.

You can deploy specific techniques to build fault tolerance into the search topology. If these techniques are followed, the deliberate or unplanned removal of a server from the topology can be absorbed without losing data and without affecting the ability to crawl or serve queries. (However, performance can still be affected.) For more information, see Technical diagrams for SharePoint Server.

Make sure that the server that you want to remove is not running any important site components. If important services or components (such as a custom Web Part) are running on the server and are not available on another server in the farm, removing the server can damage sites in the farm. For example, if the server that you want to remove is the only application server in the farm that is running the Business Data Connectivity service, removing the server can make any sites that rely on that service stop working correctly.

Remove a web server or an application server from a farm by using Control Panel

### Remove a web server or an application server from a farm by using Control Panel

You can remove a web server or an application server from the server farm by uninstalling SharePoint 2013 from the server through Control Panel. When you uninstall SharePoint 2013 by using Control Panel, you remove the program files and other information from the server.

**To remove a web server or an application server from a farm by using Control Panel**

Verify that the user account that completes this procedure has the following credentials:

- The user account that performs this procedure is a member of the Administrators group on the server.

Stop the services that are running on the server. For information about how to determine which services are running on a specific server and stopping services, see Start or stop a service in SharePoint Server.

On the server that you want to remove from the farm, click **Start**, click **Control Panel**, and then double-click **Programs and Features**.

In the list of currently installed programs, click **SharePoint 2013**, and then click **Uninstall**.

Click **Continue** at the confirmation prompt to uninstall the program.

Remove a server from a SharePoint farm by using Microsoft PowerShell

### Remove a server from a SharePoint farm by using Microsoft PowerShell

Before you remove a database server from a farm, make sure that you have moved any databases stored on that server to a different database server in your farm.

Note

Using PowerShell is the recommended way to remove a server from the farm.

**To remove a server from a SharePoint farm by using PowerShell**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2013 cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

From a PowerShell command prompt, type the following command.

```
Disconnect-SPConfigurationDatabase 
```

Note

This cmdlet only removes the **local SharePoint server** from the SharePoint farm. It can't remove remote SharePoint servers or database servers from the SharePoint farm.

Remove a server from a SharePoint farm by using the PSConfig.exe command-line tool

#### Remove a server from a SharePoint farm by using the PSConfig.exe command-line tool

You can remove a server from the SharePoint farm by using the PSConfig.exe tool which is an alternative interface to perform several operations that control how SharePoint Server 2013 is configured. You must be a member of the Administrators group on the local computer to perform these operations.

**To remove a SharePoint server from a farm by using PSConfig**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PSConfig.exe tool.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions.

From a command prompt, type the following syntax.

```
psconfig.exe -cmd configdb -disconnect
```

Removing a database server from a SharePoint farm

## Removing a database server from a SharePoint farm

To remove a database server from a farm without uninstalling SharePoint and therefore deleting the data that was stored in the database, you must first move any databases that are hosted by that server to another database server in the farm and then use Central Administration to remove the database server from the farm.

You cannot remove a database server if it is the only database server available in the farm, or if it is the database server that hosts the configuration database.

Caution

If you uninstall SharePoint 2013 from the server that is running Central Administration, you will be unable to administer the server farm until you configure another server in the farm to host the Central Administration site.

Remove a database server, web server, or application server from a SharePoint farm by using Central Administration

## Remove a database server, web server, or application server from a SharePoint farm by using Central Administration

If a web server or application server is no longer available, or if uninstalling SharePoint 2013 from Control Panel is not possible, you can remove the web server or application server from the farm by using the SharePoint Central Administration website. Removing a server from the farm by using Central Administration does not uninstall SharePoint 2013 from the server, nor does it make any sites on that server inaccessible. We recommend that you use the process described in Remove a web server or an application server from a farm by using Control Panel to uninstall SharePoint 2013 instead of using Central Administration to remove the server.

Removing the server from the farm by using Central Administration does not delete this information from the server. Use the Central Administration procedure for removing database servers only, or for removing a web server or an application server from the farm when the server is no longer available to uninstall through Control Panel.

You can follow these steps to remove a web server, application server, or database server from the farm. However, we recommend that you remove web servers and application servers from a farm by using Control Panel, instead of by using Central Administration. For information, see Remove a web server or an application server from a farm by using Control Panel.

Before you remove a database server from a farm, make sure that you have moved any databases stored on that server to a different database server in your farm.

**To remove a database server, web server, or application server from a SharePoint farm by using Central Administration**

Verify that the user account that completes this procedure has the following credentials:

The user account that performs this procedure is a member of the Farm Administrators SharePoint group.

The user account that performs this procedure is a member of the Administrators group on the server.

Stop the services that are running on the server. For information about how to determine which services are running on a specific server and stopping services, see Start or stop a service in SharePoint Server.

On the SharePoint Central Administration website, in the **System Settings** section, click **Manage servers in this farm**.

On the **Servers in Farm** page, locate the row that contains the name of the server that you want to remove, and then click **Remove Server**.

In the warning that appears, click **OK** to remove the server or click **Cancel** to stop the operation.

The page updates, and the server that you removed no longer appears in the list of servers.

See also

## See also

Other Resources

#### Other Resources

Install for SharePoint 2013

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
