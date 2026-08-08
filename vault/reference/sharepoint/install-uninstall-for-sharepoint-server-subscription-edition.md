---
title: "Uninstall SharePoint Server Subscription Edition - SharePoint Server"
type: reference
domain: sharepoint
slug: install-uninstall-for-sharepoint-server-subscription-edition
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/install/uninstall-for-sharepoint-server-subscription-edition
family: install
documentKind: "landing-page"
abstract: "Learn how to uninstall SharePoint Server Subscription Edition in various topologies."
---

# Uninstall SharePoint Server Subscription Edition - SharePoint Server

Note

Uninstall SharePoint Server Subscription Edition

# Uninstall SharePoint Server Subscription Edition

SharePoint Server uninstallation steps are as follows:

Uninstall on Windows Server with Desktop Experience

## Uninstall on Windows Server with Desktop Experience

Click **Start**.

Click **Settings**.

Click **Apps**.

Click **Microsoft SharePoint Subscription Edition Preview**.

Click **Uninstall**.

When prompted that this app and its related information will be uninstalled, click **Uninstall**.

If prompted by the User Account Control (UAC) consent dialog, click **Yes** to allow the Microsoft Setup Bootstrapper app to make changes to your device.

When prompted if you are sure you want to remove Microsoft SharePoint Server Subscription Edition Preview from your computer, click **Yes**.

When prompted with a warning asking if you want to uninstall now, click **OK**.

After setup finishes uninstalling SharePoint, click **Close** to exit.

Uninstall on Windows Server Core

## Uninstall on Windows Server Core

Run SharePoint setup (`setup.exe`) from your **C:\Program Files\Common Files\Microsoft Shared\SERVER16\Server Setup Controller** directory with the following parameters:

- `/config <config file>` (Where `<config file>` is the path to your writable `config.xml` file)

- `/uninstall OSERVER`

```
"$env:CommonProgramFiles\Microsoft Shared\SERVER16\Server Setup Controller\setup.exe" /config "C:\SharePoint Files\config.xml" /uninstall OSERVER   
```

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
