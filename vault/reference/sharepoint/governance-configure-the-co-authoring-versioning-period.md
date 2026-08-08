---
title: "Configure the co-authoring versioning period in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: governance-configure-the-co-authoring-versioning-period
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/governance/configure-the-co-authoring-versioning-period
family: governance
documentKind: "how-to"
abstract: "Learn how to specify how often SharePoint Server stores a version of a document that is being edited."
---

# Configure the co-authoring versioning period in SharePoint Server - SharePoint Server

Note

Configure the co-authoring versioning period in SharePoint Server

# Configure the co-authoring versioning period in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The CoauthoringVersionPeriod property specifies, in minutes, how often SharePoint stores a version of a document that is being edited. This article describes how to use Microsoft PowerShell to configure the CoauthoringVersionPeriod property. For more information about document library versioning, see Configure versioning for co-authoring in SharePoint 2013.

Configure the co-authoring versioning period in SharePoint Server 2013

## Configure the co-authoring versioning period in SharePoint Server 2013

When versioning is turned on, SharePoint Server 2013 takes periodic snapshots of documents, saving them for later reference. This information can provide an edit trail that may be useful for seeing who changed a document, rolling back to an earlier version, or for compliance reasons.

You can configure the CoauthoringVersionPeriod property by using the Microsoft PowerShell. If the value is set to 0, SharePoint Server 2013 captures every change made by a new user in a different version of the document. If the value is set to a very large number, SharePoint Server 2013 creates one version for the whole editing session. This latter behavior matches the behavior of files that are not co-authored and files that were created in earlier versions of SharePoint Server 2013 or SharePoint Foundation.

**To configure the co-authoring versioning period by using Windows PowerShell (save as script and run script)**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2013 cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and Add-SPShellAdmin.

- Paste the following code into a text editor, such as Notepad:

```
$siteurl ="<ServerName>" 
$mysite=new-object Microsoft.SharePoint.SPSite($siteurl)
$mysite.WebApplication.WebService.CoauthoringVersionPeriod = <Time>
$mysite.WebApplication.WebService.Update()
```

Specify the following parameters:

**Parameters to configure the co-authoring versioning period**

| **Parameter** | **Value** |
| --- | --- |
| *ServerName* | Server name |
| *Time* | Number in minutes |

Save the file and add the .ps1 extension, such as SuggestedNameOfFile.ps1.

Note

You can use a different file name, but you must save the file as an ANSI-encoded text file whose extension is .ps1.

Start the SharePoint 2013 Management Shell as Administrator.

Change to the directory to which you saved the file.

At the PowerShell command prompt, type the following command:

```
./SuggestedFileName.ps1
```

See also

## See also

Concepts

#### Concepts

Configure versioning for co-authoring in SharePoint 2013

Overview of co-authoring in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
