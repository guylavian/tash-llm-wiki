---
title: "Set permissions to published service applications in SharePoint Server - SharePoint Server"
description: "Learn how to configure permissions to the Application Discovery and Load Balancing Service Application and published service applications for the consuming farm in SharePoint Server."
ms.topic: how-to
---
Note

Set permissions to published service applications in SharePoint Server

# Set permissions to published service applications in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

In SharePoint Server, you must establish a relationship between the publishing farm and the consuming farm by giving the consuming farm permission to the Application Discovery and Load Balancing Service Application on the publishing farm. After doing this, the consuming farm can be given permission to other service applications.

Before you begin this operation, review Share service applications across farms in SharePoint Server for information about prerequisites.

Important

You must perform steps 1 through 5 in the PowerShell procedure to obtain the consuming farm ID, which you must have in order to complete either the PowerShell or Central Administration procedures.

Set permission to the Application Discovery and Load Balancing Service Application and any other service application for a consuming farm by using PowerShell

## Set permission to the Application Discovery and Load Balancing Service Application and any other service application for a consuming farm by using PowerShell

The first procedure explains how to set permission to the Application Discovery and Load Balancing Service Application. The second explains how to set permissions to any other service applications.

To set permission to the Application Discovery and Load Balancing Service Application for a consuming farm by using PowerShell

### To set permission to the Application Discovery and Load Balancing Service Application for a consuming farm by using PowerShell

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Get-SPFarm | Select Id
```

For more information, see Get-SPFarm.

On a server in the publishing farm, access the SharePoint Management Shell and at the PowerShell command prompt, type the following commands:

```
$security=Get-SPTopologyServiceApplication | Get-SPServiceApplicationSecurity
$claimprovider=(Get-SPClaimProvider System).ClaimProvider
$principal=New-SPClaimsPrincipal -ClaimType "http://schemas.microsoft.com/sharepoint/2009/08/claims/farmid" -ClaimProvider $claimprovider -ClaimValue <consumingfarmid>
Grant-SPObjectSecurity -Identity $security -Principal $principal -Rights "Full Control"
Get-SPTopologyServiceApplication | Set-SPServiceApplicationSecurity -ObjectSecurity $security
```

Where  *Consumingfarmid* is the GUID value of the consuming farm. This is the ID of the consuming farm that you need in the Central Administration section.

For more information, see the following:

Get-SPTopologyServiceApplication

Set-SPServiceApplicationSecurity

Get-SPServiceApplicationSecurity

New-SPClaimsPrincipal

Get-SPClaimProvider

Grant-SPObjectSecurity

To set permission to a published service application for a consuming farm by using PowerShell

### To set permission to a published service application for a consuming farm by using PowerShell

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
$sa = Get-SPServiceApplication -Name '<Service Application DisplayName>'
$security=Get-SPServiceApplication $sa | Get-SPServiceApplicationSecurity
$claimprovider=(Get-SPClaimProvider System).ClaimProvider
$principal=New-SPClaimsPrincipal -ClaimType "http://schemas.microsoft.com/sharepoint/2009/08/claims/farmid" -ClaimProvider $claimprovider -ClaimValue <consumingfarmid>
Grant-SPObjectSecurity -Identity $security -Principal $principal -Rights <NamedAccessRights>
Set-SPServiceApplicationSecurity $sa -ObjectSecurity $security
```

Where:

- <Service Application DisplayName> is the DisplayName value of the published Service Application from `Get-SPServiceApplication`.

- <Consumingfarmid> is the GUID value of the consuming farm. This is the ID of the consuming farm that you need in Step 5 of the Central  Administration section.

- <NamedAccessRights> is the name of the access right from `(Get-SPServiceApplicationSecurity $sa).NamedAccessRights`.

For more information, see the following:

Get-SPServiceApplication

New-SPClaimsPrincipal

Get-SPServiceApplicationSecurity

Grant-SPObjectSecurity

Set-SPServiceApplicationSecurity

Set permission to the Application Discovery and Load Balancing Service Application and any other published service application for a consuming farm by using Central Administration

## Set permission to the Application Discovery and Load Balancing Service Application and any other published service application for a consuming farm by using Central Administration

This procedure explains how to set permission to any service application, but most specifically, the Application and Load Balancing Service Application.

Important

You must perform steps 1 through 5 in the PowerShell procedure to obtain the consuming farm ID, which you must have in order to complete this procedure.

To set permission to the Application Discovery and Load Balancing Service Application and any other published service application for a consuming farm by using Central Administration

### To set permission to the Application Discovery and Load Balancing Service Application and any other published service application for a consuming farm by using Central Administration

On the server that hosts the SharePoint Central Administration website for the publishing farm, verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.

On Central Administration, click **Application Management**, and then click **Manage service applications**.

Click the row that contains **Application Discovery and Load Balancing Service Application**.

On the ribbon, click **Permissions**.

In the **Connection Permissions** dialog, do the following:

Manually paste the ID of the consuming farm. You found the ID earlier in the PowerShell section when you used  *<consumingfarmid>*.

Click **Add**.

Select the consuming farm ID, and then select the **Full Control** check box.

Click **OK**.

Repeat steps 2 through 5 for any published service applications for which you want to enable access from the consuming farm and assign the necessary permission.

Note

To enable access to the User Profile service application, you must give the consuming farm's web application pool identity (that is, DOMAIN\Username) the permission instead of the consuming farm ID.

See also

## See also

Concepts

#### Concepts

Share service applications across farms in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
