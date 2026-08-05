---
title: "Repair SharePoint Server Subscription Edition - SharePoint Server"
type: reference
domain: sharepoint
slug: install-repair-sharepoint-server-subscription-edition
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/install/repair-sharepoint-server-subscription-edition
family: install
documentKind: "landing-page"
abstract: "Learn how to repair SharePoint Server Subscription Edition in various topologies."
---

# Repair SharePoint Server Subscription Edition - SharePoint Server

Note

Repair SharePoint Server Subscription Edition

# Repair SharePoint Server Subscription Edition

SharePoint Server repair steps are as follows:

Repair on Windows Server with Desktop Experience

## Repair on Windows Server with Desktop Experience

Click **Start**.

Click **Settings**.

Click **Apps**.

Click **Microsoft SharePoint Subscription Edition Preview**.

Click **Modify**.

If prompted by the User Account Control (UAC) consent dialog, click **Yes** to allow the Microsoft Setup Bootstrapper app to make changes to your device.

In the Microsoft SharePoint Server Subscription Edition Preview setup application, select **Repair** and then click **Continue**.

After setup finishes repairing SharePoint, click **Close** to exit.

If prompted to reboot your computer, click **Yes** to reboot.

After the computer reboots, launch the SharePoint Products Configuration Wizard.

Click **Next**.

If prompted to automatically start or reset services, click **Yes**.

In the Modify server farm Settings page, select **Do not disconnect from this server farm** and then click **Next**.

If prompted whether to modify the SharePoint Central Administration web application settings, select **No, this machine will continue to host the web site** and then, click **Next**.

Click **Next** to begin the repair operation.

After the repair operation has finished, click **Finish**.

Repair on Windows Server Core

## Repair on Windows Server Core

Run SharePoint setup (`setup.exe`) from your **C:\Program Files\Common Files\Microsoft Shared\SERVER16\Server Setup Controller** directory with the following parameters:

`/config <config file>` (Where `<config file>` is the path to your writable `config.xml` file)

`/repair OSERVER`

```
"$env:CommonProgramFiles\Microsoft Shared\SERVER16\Server Setup Controller\setup.exe" /config "C:\SharePoint Files\config.xml" /repair OSERVER  
```

Once SharePoint setup has completed, reboot your test server.

Run the following SharePoint PowerShell cmdlets with their appropriate parameters to repair the server in the farm.

- `Update-SPFlightsConfigFile -FilePath "C:\Program Files\Common Files\microsoft shared\Web Server Extensions\16\CONFIG\SPFlightRawConfig.json"`

- `Install-SPHelpCollection -All`

- `Initialize-SPResourceSecurity`

- `Install-SPService`

- `Install-SPFeature -AllExistingFeatures`

- `New-SPCentralAdministration` (If hosting the Central Administration site on this server)

- `Install-SPApplicationContent`

Note

You can also use the `PSCONFIG.EXE` command line tool or the `PSConfigUI.exe` GUI tool. However, `PSConfigUI.exe` will crash on Windows Server Core if it needs to display a summary of error messages at the end of the sequence due to a dependency on HTML rendering components.

Additional resources

## Additional resources

- Last updated on 
		2023-06-07
