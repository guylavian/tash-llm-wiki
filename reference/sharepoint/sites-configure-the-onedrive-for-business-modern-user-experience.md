---
title: "Configure the OneDrive modern user experience - SharePoint Server"
type: reference
domain: sharepoint
slug: sites-configure-the-onedrive-for-business-modern-user-experience
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/sites/configure-the-onedrive-for-business-modern-user-experience
family: sites
documentKind: "how-to"
abstract: "Learn how to turn the OneDrive modern user experience on or off in SharePoint Server."
---

# Configure the OneDrive modern user experience - SharePoint Server

Note

Configure the Microsoft OneDrive modern user experience

# Configure the Microsoft OneDrive modern user experience

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

As part of the November 2016 public update for SharePoint Server 2016 (Feature Pack 1), a new modern user experience for Microsoft OneDrive is included. This modern user experience is turned on automatically when you install the public update. However, you can use Microsoft PowerShell to toggle the user experience off and on if you need to.

The OneDrive modern user experience requires an active Software Assurance contract at the time it is enabled, either by installation of the PU or by manual enablement. If you don't have an active Software Assurance contract at the time of enablement, then you must turn the OneDrive modern user experience off.

**Turn the OneDrive modern user experience off**

Make sure you have permissions to administer SharePoint Server with Windows PowerShell, and log in to a server in your SharePoint farm. Open the SharePoint 2016 Management Shell as administrator and run the following script:

```
$Farm = Get-SPFarm
$Farm.OneDriveUserExperienceVersion = [Microsoft.SharePoint.Administration.OneDriveUserExperienceVersion]::Version1
$Farm.Update()
```

**Turn the OneDrive modern user experience on**

Make sure you have permissions to administer SharePoint Server with Windows PowerShell, and log in to a server in your SharePoint farm. Open the SharePoint 2016 Management Shell as administrator and run the following script:

```
$Farm = Get-SPFarm
$Farm.OneDriveUserExperienceVersion = [Microsoft.SharePoint.Administration.OneDriveUserExperienceVersion]::Version2
$Farm.Update()
```

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
