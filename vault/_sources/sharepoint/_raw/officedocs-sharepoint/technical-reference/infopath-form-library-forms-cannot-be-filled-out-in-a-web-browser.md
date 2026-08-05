---
title: "InfoPath form library forms cannot be filled out in a Web browser (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: InfoPath form library forms cannot be filled out in a Web browser, for SharePoint Server."
ms.topic: troubleshooting
---
Note

InfoPath form library forms cannot be filled out in a Web browser (SharePoint Server)

# InfoPath form library forms cannot be filled out in a Web browser (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** InfoPath form library forms cannot be filled out in a Web browser

**Summary:** InfoPath Forms Services users can publish browser-enabled form templates to a SharePoint Server form library but cannot open the forms in a Web browser.

Note

This issue only applies to forms published to form libraries. It does not apply to list forms or to forms that have been uploaded by farm administrators.

**Cause:** One or more of the following might be causing this:

The **Render form templates that are browser-enabled by users** check box in the SharePoint Central Administration website is cleared.

The following Windows PowerShell command has been run:  `Set-SPInfoPathFormsService -AllowUserFormBrowserRendering $false`.

Note

Infopath form service is removed and is no longer supported by Microsoft in SharePoint Server Subscription Edition. We recommend exploring Microsoft Power Apps as a potential alternative to Infopath form service.

**Resolution: Enable browser rendering of user forms by using Central Administration**

Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.

Start Central Administration.

In Central Administration, click **General Application Settings**.

On the General Application Settings page, in the **InfoPath Forms Services** section, click **Configure InfoPath Forms Services**.

On the Configure InfoPath Forms Services page, in the **User Browser-enabled Form Templates** section, select the **Render form templates that are browser-enabled by users** check box.

Click **OK** at the bottom of the page.

**Resolution: Enable browser rendering of user forms by using Microsoft PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Set-SPInfoPathFormsService -AllowUserFormBrowserRendering $true
```

For more information, see Set-SPInfoPathFormsService.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
