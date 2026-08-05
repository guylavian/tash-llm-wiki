---
title: "Disable co-authoring in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: governance-disable-co-authoring
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/governance/disable-co-authoring
family: governance
documentKind: "how-to"
abstract: "Learn how to disable co-authoring functionality in SharePoint Server by using Group Policy or by using PowerShell."
---

# Disable co-authoring in SharePoint Server - SharePoint Server

Note

Disable co-authoring in SharePoint Server

# Disable co-authoring in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Co-authoring in SharePoint Server allows multiple users to work on a document, at any time, without interfering with each other's changes. Although co-authoring is scalable and efficient, some organizations that have hardware limitations may want to turn off co-authoring to minimize effects on server performance.

There are three ways to disable co-authoring:

You can use Group Policy to disable co-authoring functionality on the client-side. For more information, see Group Policy overview for Office 2013.

You can use Microsoft PowerShell to set the DisableCoauthoring server property. This setting disables the co-authoring property for Word and PowerPoint documents on the server. This property applies to documents or presentations in Word 2010, Word 2013, Word Online, PowerPoint 2010, PowerPoint 2013, and PowerPoint Web App.

You can enable the Require Check Out setting in a document library. This setting disables co-authoring in the document library. For more information, see Configure Require Check Out in SharePoint Server 2013.

Turn off co-authoring by using Group Policy

## Turn off co-authoring by using Group Policy

Start **Group Policy Management**.

In **Group Policy Management**, expand the Forest and Domain nodes for the domain where you want to set the policy, and then expand **Group Policy Objects**.

Choose (right-click) the Group Policy Object where your co-authoring settings are configured, and then choose **Edit**.

For Word 2013, expand **User Configuration**, **Administrative Templates**, **Microsoft Word 2013**, **Collaboration Settings**, **Co-authoring**, and then open (double-click) **Prevent Co-authoring**.

For PowerPoint 2013, expand **User Configuration**, **Administrative Templates**, **Microsoft PowerPoint 2013**, **Collaboration Settings**, **Co-authoring**, and then choose **Prevent Co-authoring**.

In the **Prevent Co-authoring Properties** dialog, select **Enabled**, and then choose **OK**.

Turn off co-authoring for Word documents and PowerPoint presentations at the web service level by using Windows PowerShell (save as script and run script)

## Turn off co-authoring for Word documents and PowerPoint presentations at the web service level by using Windows PowerShell (save as script and run script)

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you're running PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For more information about PowerShell permissions, see Permissions and Add-SPShellAdmin.

Paste the following code into a text editor, such as Notepad:

```
$siteurl = "<servername>"
$mysite=new-object Microsoft.SharePoint.SPSite($siteurl)
$mysite.WebApplication.WebService.DisableCoauthoring = $true;
$mysite.WebApplication.WebService.Update();
```

- Specify the following parameter:

| **Parameter** | **Value** |
| --- | --- |
| *servername* | Server name |

Save the file and add the `.ps1` extension, such as SuggestedNameOfFile.ps1.

Note

You can use a different file name, but you must save the file as an ANSI-encoded text file whose extension is `.ps1.`

Start the SharePoint 2013 Management Shell as Administrator.

Change to the directory to which you saved the file.

At the PowerShell command prompt, type the following command:

```
./SuggestedFileName.ps1
```

Turn off co-authoring for Word documents and PowerPoint presentations at the web application level by using Windows PowerShell (save as script and run script)

## Turn off co-authoring for Word documents and PowerPoint presentations at the web application level by using Windows PowerShell (save as script and run script)

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you're running PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For more information about PowerShell permissions, see Permissions and Add-SPShellAdmin.

Paste the following code into a text editor, such as Notepad:

```
$siteurl = "<servername>"
$mysite=new-object Microsoft.SharePoint.SPSite($siteurl)
$mysite.WebApplication.DisableCoauthoring = $true;
$mysite.WebApplication.Update();
```

- Specify the following parameter:

| **Parameter** | **Value** |
| --- | --- |
| *servername* | Server name |

Save the file and add the `.ps1` extension, such as SuggestedNameOfFile.ps1.

Note

You can use a different file name, but you must save the file as an ANSI-encoded text file whose extension is `.ps1.`

Start the SharePoint 2013 Management Shell as Administrator.

Change to the directory to which you saved the file.

At the PowerShell command prompt, type the following command:

```
./SuggestedFileName.ps1
```

See also

## See also

Overview of co-authoring in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
