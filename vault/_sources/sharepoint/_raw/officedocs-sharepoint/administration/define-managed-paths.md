---
title: "Define managed paths in SharePoint Server - SharePoint Server"
description: "Learn how to add a managed path for a web application in SharePoint Server."
ms.topic: how-to
---
Note

Define managed paths in SharePoint Server

# Define managed paths in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can specify the paths in the URL namespace of a web application to use for site collections. This is known as a managed path. You can specify that one or more site collections exist at a specified path.

There are two types of managed paths that you can create:

A wildcard inclusion allows you to append multiple site collections to the path that you specify. For example, if you add /engineering as a wildcard inclusion off of your root site of http://contoso, then you'll be able to create multiple site collections off of http://contoso/engineering.

An explicit inclusion allows you to create a single site collection with the specified address. For example, if you add /finance as an explicit inclusion off of your root site of http://contoso, then you'll be able to create a single site collection with the address http://contoso/finance.

Note that the root of a web application is automatically included as an explicit inclusion. Changing the root to a wildcard inclusion is not supported.

Define managed paths for a web application by using Central Administration

## Define managed paths for a web application by using Central Administration

Use the procedures that are described here to add or delete managed paths for a web application by using Central Administration.

**To add a managed path by using Central Administration**

Verify that the user account that is performing this task is a member of the Farm Administrators SharePoint group.

On the SharePoint Central Administration website, click **Application Management**.

On the **Application Management** page, click **Manage web applications**.

Click the web application for which you want to manage paths.

The ribbon becomes active.

In the **Manage** group of the ribbon, click **Managed Paths**.

On the **Define Managed Paths** page, in the **Add a New Path** section, type the path to include.

Click **Check URL** to confirm that the path does not already exist.

In the **Type** list, select either **Wildcard inclusion** or **Explicit inclusion** to identify the type of path.

The **Wildcard inclusion** type includes all paths that are subordinate to the specified path. The **Explicit inclusion** type includes only the site that is indicated by the specified path. Sites subordinate to the specified path are not included.

Click **Add Path**.

When you have finished adding paths, click **OK**.

**To remove a managed path by using Central Administration**

Verify that the user account that is performing this task is a member of the Farm Administrators SharePoint group.

On the SharePoint Central Administration website, click **Application Management**.

On the **Application Management** page, click **Manage web applications**.

Click the web application for which you want to manage paths. The ribbon becomes active.

In the **Manage** group of the ribbon, click **Managed Paths**.

On the **Define Managed Paths** page, in the **Included Paths** section, click the check box next to the path that you want to remove.

Click **Delete selected paths**.

Caution

Be sure that you want to remove the selected path before you perform this action. You'll have no additional opportunity to confirm. Deletion is immediate.

After you are finished removing paths, click **OK**.

See also

## See also

Other Resources

#### Other Resources

New-SPManagedPath

Get-SPManagedPath

Remove-SPManagedPath

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
