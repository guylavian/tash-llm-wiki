---
title: "Configure syncing with the new OneDrive sync app - SharePoint Server"
type: reference
domain: sharepoint
slug: install-configure-syncing-with-the-onedrive-sync-app
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/install/configure-syncing-with-the-onedrive-sync-app
family: install
documentKind: "how-to"
abstract: "Learn how to configure the new OneDrive sync app (OneDrive.exe) for SharePoint Server Subscription Edition or 2019."
---

# Configure syncing with the new OneDrive sync app - SharePoint Server

Note

Configure syncing with the new OneDrive sync app

# Configure syncing with the new OneDrive sync app

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

When you deploy SharePoint Server Subscription Edition or 2019 in your organization, your users can sync their OneDrive files as well as SharePoint team site files by using the new OneDrive sync app (*OneDrive.exe*) for Windows or Mac. Compared with the previous OneDrive sync app (*Groove.exe*), the new sync app provides:

- Improved performance and reliability

- Files On-Demand

- Support for larger files

- Higher sync limits

- The ability to silently deploy. If your Windows users are already syncing document libraries with the previous OneDrive sync app, they will transition to the new sync app automatically.

- Mac support

Requirements

## Requirements

Install SharePoint Server Subscription Edition or 2019.

Install the OneDrive sync app (download). For deployment info, see:

- Deploy OneDrive apps using Microsoft Endpoint Configuration Manager

- Deploy OneDrive apps by using Intune

- Deploy and configure the new OneDrive sync app for Mac

Configure OneDrive for SharePoint Server 2019.

Recommendations

## Recommendations

1. Allow WNS Traffic

### 1. Allow WNS Traffic

For the best user experience, SharePoint Server Subscription Edition or 2019 will send change notifications to sync apps via WNS web push notifications. This feature ensures sync users quickly have the latest copies of any SharePoint Server file updates. You may need to take steps to ensure outbound requests from your SharePoint Server and your users' computers can reach and properly interact with the WNS service.

For SharePoint Server:

- Allow outbound HTTPS connection to reach *.notify.windows.com

For computers running the OneDrive sync app:

- Allow outbound TLS encrypted TCP/IP socket connection to reach *.wns.windows.com

- Avoid HTTPS decryption for *.wns.windows.com on your proxy server as this likely will disconnect the socket connection.

If either the SharePoint Server or the OneDrive sync app is unable to communicate with the WNS service, then the sync app will fall back to polling the SharePoint Server roughly every two minutes looking for changes.  As a result, your users may see delays of more than two minutes from the time of a server change to when the sync app downloads a changed file.

2. Opt in to sharing improvement information

### 2. Opt in to sharing improvement information

When configuring the SharePoint Server, you can enable sharing of improvement information with Microsoft. Enabling this option allows connected sync apps to send troubleshooting information. This allows the sync app team to proactively detect and correct problems, respond to customer reported problems, and improve the product over time. If this is disabled, customer escalations are harder to investigate and will require the customer to manually gather and provide logs from the impacted computers.

Configure OneDrive for SharePoint Server Subscription Edition or 2019

## Configure OneDrive for SharePoint Server Subscription Edition or 2019

To set up OneDrive with SharePoint Server Subscription Edition or 2019, you can either use Group Policy or set the registry keys directly.

Note

For settings that require an organization ID, if you sync a single domain, you can use **OP1**. Do not use this if you sync multiple domains.

The Known Folder Move settings don't work for SharePoint Server.

Using Group Policy

### Using Group Policy

Configure the following two Group Policy objects to configure OneDrive to be used with SharePoint Server Subscription Edition or 2019:

**Specify SharePoint Server URL and organization name**

The URL (*SharePointOnPremFrontDoorUrl*) is used by the sync app to authenticate the user and to set up syncing of the user's SharePoint Server hosted personal OneDrive site.
The organization name (*SharePointOnPremTenantName*) lets you specify the name of the root folder that will be created in File Explorer. If you don't supply an organization name, the sync app will use the first segment of the URL as the name. For example, office.sharepoint.com would create the folder "office".

**Specify the OneDrive location in a hybrid environment**

This setting (*SharePointOnPremPrioritization*) lets you specify if the sync app should first set up a sync relationship with SharePoint in Microsoft 365 (the default) or the SharePoint on-premises server if the user identity exists in both identity providers. The sync application's **Settings** dialog can be used to "Add Account" the same identity for the other SharePoint realm after the first has been configured (if the user identity exists in both).

You should be able to find these Group Policy objects using the Group Policy Editor (*gpedit.msc*) when navigating to *Computer Configuration\Administrative Templates\OneDrive*. If the OneDrive folder is not present, you can add the OneDrive Group Policy template by copying the following two files from the OneDrive installation folder after you have installed the latest OneDrive sync app on that computer:

- C:\Users\*username*\AppData\Local\Microsoft\OneDrive\*onedrivesyncclientversion*\adm\OneDrive.admx
to
C:\Windows\PolicyDefinitions\OneDrive.admx

- C:\Users\*username*\AppData\Local\Microsoft\OneDrive\*onedrivesyncclientversion*\adm\OneDrive.adml
to
C:\Windows\PolicyDefinitions\en-US\OneDrive.adml

To automate this copying using PowerShell, use:

```
Get-ChildItem -Recurse -Path "$env:LOCALAPPDATA\Microsoft\OneDrive" -Filter "OneDrive.admx" | ? FullName -like "*\adm\OneDrive.admx" | Copy-Item -Destination "$env:WINDIR\PolicyDefinitions" -Force
Get-ChildItem -Recurse -Path "$env:LOCALAPPDATA\Microsoft\OneDrive" -Filter "OneDrive.adml" | ? FullName -like "*\adm\OneDrive.adml" | Copy-Item -Destination "$env:WINDIR\PolicyDefinitions\en-US" -Force
```

More information:
Learn how to manage OneDrive using Group Policy

By setting the registry keys

### By setting the registry keys

Alternatively, you can also directly configure the following underlying registry keys:

| Key | Type | Value | Required |
| --- | --- | --- | --- |
| HKLM:\Software\Policies\Microsoft\OneDrive\SharePointOnPremFrontDoorUrl | String | https://sharepoint.contoso.local | required |
| HKLM:\Software\Policies\Microsoft\OneDrive\SharePointOnPremPrioritization | DWORD (32-bit) | 1 | optional |
| HKLM:\Software\Policies\Microsoft\OneDrive\SharePointOnPremTenantName | String | Contoso | optional |

Mac configuration

### Mac configuration

To configure sync with SharePoint Server in a Mac environment, you can use the *SharePointOnPremFrontDoorUrl*, *SharePointOnPremPrioritizationPolicy*, and *SharePointOnPremTenantName* settings. For more information, see Deploy and configure the new OneDrive sync app for Mac.

Differences between syncing files in SharePoint Server and SharePoint in Microsoft 365

## Differences between syncing files in SharePoint Server and SharePoint in Microsoft 365

If your organization also uses the OneDrive sync app to sync files in Microsoft 365, here's what will be different for users who sync on-premises files.

Single Top-level URL

### Single Top-level URL

If you have deployed multiple on-premises SharePoint Server farms in your enterprise, on a given client computer, you will only specify a single *SharePointOnPremFrontDoorUrl*. For a given user, you must configure their computer with the SharePoint Server URL that hosts their individual OneDrive site or if they don't have a OneDrive site, where the team sites they are most likely to sync are hosted. Your users will be able to start syncing team site content from any of your on-premises SharePoint Server farms by navigating to the web experience of the Team Site and clicking the Sync button on that site.

For example, you have a SharePoint Server farm for your Finance department and another for the rest of your organization. Users who are members of the Finance department have their individual OneDrive site hosted on the Finance department's SharePoint Server farm. For those Finance employees, you use your computer management system to set the *SharePointOnPremFrontDoorUrl* registry key policy on their computer to have your Finance specific farm's URL. For all other employees, you set the SharePointOnPremFrontDoorUrl to your other SharePoint Server farm URL. The sync app will look for and provision the user's OneDrive on the appropriate SharePoint Server farm as needed.

Folder names

### Folder names

The OneDrive sync app creates the following folders on users' computers:

- *OneDrive – Contoso* (for syncing personal My Site files)

- *Contoso* (for syncing SharePoint team site files)

In SharePoint in Microsoft 365, "*Contoso*" is the tenant name that has been set for the SharePoint in Microsoft 365 instance. In SharePoint on-premises, there is no tenant name associated to the instance of SharePoint. You can set this with the "Specify SharePoint Server URL and organization name" group policy, or the sync app will use the first segment of your SharePoint URL.

File thumbnails and previews

### File thumbnails and previews

Thumbnails don't appear in File Explorer for files synced from SharePoint on-premises. If you enable Files On-Demand, and a file is online-only, a file preview won't be available. Image files and Office files will not have a thumbnail in File Explorer until the file is downloaded.

Sharing from File Explorer

### Sharing from File Explorer

When users share files and folders from File Explorer, the sharing option will open the browser instead of the Share dialog.

Privacy settings

### Privacy settings

When setting up SharePoint Server, you'll be prompted to select if clients should send error reports and usage statistics back to Microsoft. If you enable the setting, individual users can opt out by following these steps:

At the far right of the taskbar, in the notification area, right-click the OneDrive cloud icon.

Select **Settings**.

Select the **Settings** tab, and under **Privacy**, clear the option.

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
