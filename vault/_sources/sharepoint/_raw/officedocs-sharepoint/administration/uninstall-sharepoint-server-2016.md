---
title: "Uninstall SharePoint Server 2016, 2019, or Subscription Edition - SharePoint Server"
description: "Learn about the limited set of supported methods to uninstall SharePoint Server."
ms.topic: install-set-up-deploy
---
Note

Uninstall SharePoint Servers 2016 or 2019

# Uninstall SharePoint Servers 2016 or 2019

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You remove SharePoint Server by uninstalling it from Control Panel. When you uninstall SharePoint Server, most files and subfolders in the installation folders are removed. However, some files are not removed. Also,

Web.config files, index files, log files, and customizations that you might have are not automatically removed when you uninstall SharePoint Server.

SQL Server databases are detached but are not removed from the database server.

When you uninstall SharePoint Server, all user data remains in the database files.

Note

To uninstall SharePoint Server Subscription Edition on Windows Server Core, see Uninstall SharePoint Server Subscription Edition.

Before you begin

## Before you begin

Before you begin this operation, confirm that you have uninstalled all language packs that are on the server.

Uninstall SharePoint Servers 2016 or 2019

## Uninstall SharePoint Servers 2016 or 2019

Use this procedure to uninstall SharePoint Server 2016.

**To uninstall SharePoint Servers 2016 or 2019**

Verify that you are a member of the Farm Administrators group or a member of the Administrators group on the local computer.

On the computer that runs SharePoint Server, log on as a local or domain administrator.

Start Control Panel.

In the **Programs** area, click **Uninstall a program**.

In the **Uninstall or change a program** dialog, click **Microsoft SharePoint Server 2016** or **Microsoft SharePoint Server 2019**.

Click **Change**.

On the **Change your installation of Microsoft SharePoint Server** page, click **Remove**, and then click **Continue**.

A confirmation message appears.

Click **Yes** to remove SharePoint Server 2016.

A warning message appears.

Click **OK** to continue.

A confirmation message appears.

Click **OK**.

You might be prompted to restart the server.

Note

If you did not remove the language template packs before you uninstalled and then reinstalled SharePoint Server, you must run **Repair** from the SharePoint Products Configuration Wizard for each language template pack on the server. After the repair operation is complete, you must restart the server. Finally, complete the language template pack configuration by running the SharePoint Products Configuration Wizard.

See also

## See also

Concepts

#### Concepts

Add a server to a SharePoint Server 2016 or SharePoint Server 2019 farm

Remove a server from a farm in SharePoint Server 2016 or SharePoint Server 2019

Hardware and software requirements for SharePoint Server 2016

Hardware and software requirements for SharePoint Server 2019

Install SharePoint Servers 2016 or 2019 on one server

Install SharePoint Servers 2016 or 2019 across multiple servers

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
