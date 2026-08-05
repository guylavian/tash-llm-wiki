---
title: "Uninstall SharePoint 2013 - SharePoint Server"
description: "SharePoint Server 2013 and SharePoint Foundation 2013 support a limited set of methods to uninstall."
ms.topic: install-set-up-deploy
---
Note

Uninstall SharePoint 2013

# Uninstall SharePoint 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You remove SharePoint 2013 by uninstalling it from Control Panel. When you uninstall SharePoint 2013, most files and subfolders in the installation folders are removed. However, some files are not removed. Also,

Web.config files, index files, log files, and customizations that you might have are not automatically removed when you uninstall SharePoint 2013.

SQL Server databases are detached but are not removed from the database server.

If you uninstall a single server that has a built-in database, SQL Server Express is not removed.

When you uninstall SharePoint 2013, all user data remains in the database files.

Before you begin

## Before you begin

Before you begin this operation, confirm that you have uninstalled all language packs that are on the server.

Uninstall SharePoint 2013

## Uninstall SharePoint 2013

Use this procedure to uninstall SharePoint 2013.

**To uninstall SharePoint 2013**

Verify that you are a member of the Farm Administrators group or a member of the Administrators group on the local computer.

On the computer that runs SharePoint 2013, log on as a local or domain administrator.

Start Control Panel.

In the **Programs** area, click **Uninstall a program**.

In the **Uninstall or change a program** dialog, click **Microsoft SharePoint Server 2013**.

Click **Change**.

On the **Change your installation of Microsoft SharePoint Server 2013** page, click **Remove**, and then click **Continue**.

A confirmation message appears.

Click **Yes** to remove SharePoint 2013.

A warning message appears.

Click **OK** to continue.

A confirmation message appears.

Click **OK**.

You might be prompted to restart the server.

Note

If you did not remove the language template packs before you uninstalled and then reinstalled SharePoint 2013, you must run **Repair** from the SharePoint Products Configuration Wizard for each language template pack on the server. After the repair operation is complete, you must restart the server. Finally, complete the language template pack configuration by running the SharePoint Products Configuration Wizard.

See also

## See also

Other Resources

#### Other Resources

Add web or application servers to farms in SharePoint 2013

Remove a server from a farm in SharePoint 2013

Hardware and software requirements for SharePoint 2013

Install SharePoint 2013 on a single server with a built-in database

Install SharePoint 2013 on a single server with SQL Server

Install SharePoint 2013 across multiple servers for a three-tier farm

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
