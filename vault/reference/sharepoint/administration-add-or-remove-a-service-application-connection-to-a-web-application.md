---
title: "Add or remove service application connections from a web application in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-add-or-remove-a-service-application-connection-to-a-web-application
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/add-or-remove-a-service-application-connection-to-a-web-application
family: administration
documentKind: "how-to"
abstract: "Learn how to add or remove service application connections to a service application connection group in SharePoint Server."
---

# Add or remove service application connections from a web application in SharePoint Server - SharePoint Server

Note

Add or remove service application connections from a web application in SharePoint Server

# Add or remove service application connections from a web application in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

When you create a service application in SharePoint Server, a service application connection is created. A service application connection is also referred to as an application proxy. A service application connection associates the service application to web applications via membership in a service application connection group (also referred to as application proxy group).

Important

If you are creating a service application connection to a service application in a remote farm, you should read Share service applications across farms in SharePoint Server to gain a full understanding of the requirements to successfully share service applications across farms.

By default, a new service application connection is added to the farm's Default group of service application connections when you create the service application by using Central Administration. You can override this default membership. If a new service application is created by using Microsoft PowerShell instead of by using Central Administration, the new service application does not automatically become a member of the Default service application connections group unless the **default** parameter is supplied.

Note

For more information about how to create and configure service applications, see Manage service applications in SharePoint Server.

By default, all web applications are associated with the farm's Default group of service application connections, although you can change this setting. You can also create one custom connection group for each web application in the farm. You can change the service applications with which a web application is associated at any time, and you can change the service applications that are included in the Default service application connection group.

Editing a service connection group

## Editing a service connection group

You can add or remove service application connections to a service application connection group by using Central Administration or by using PowerShell cmdlets.

To edit a service connection group by using Central Administration

### To edit a service connection group by using Central Administration

Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.

Start Central Administration.

On the Central Administration Home page, click **Application Management**.

On the Application Management page, in the **Service Applications** section, click **Configure service application associations**.

On the Service Application Associations page, select **Web Applications** from the **View** drop-down menu.

In the list of Web applications, in the **Application Proxy Group** column, click the name of the service application connection group that you want to change.

To add a service connection to the group, select the check box that is next to the service application that you want to add to the connection group. To remove a service application connection from the connection group, clear the check box next to the service application that you want to remove from the connection group. When you have made the changes that you want, click **OK**.

Note

You can also change custom service application connection groups by clicking **Manage Web Applications** from the Central Administration Home page, selecting a listed Web application, and then clicking **Service Connections** on the ribbon. You cannot change the default service applications connection group through this page, however.

To add a service application connection to a service application connection group by using PowerShell

### To add a service application connection to a service application connection group by using PowerShell

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
Add-SPServiceApplicationProxyGroupMember -Identity < the service application proxy group > -Member <members to add to the service application proxy group>
```

For more information, see Add-SPServiceApplicationProxyGroupMember.

To remove a service application connection from a service application connection group by using PowerShell

### To remove a service application connection from a service application connection group by using PowerShell

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
Remove-SPServiceApplicationProxyGroupMember -Identity <SPServiceApplicationProxyGroupPipeBind> -Member <SPServiceApplicationProxyPipeBind >
```

For more information, see Remove-SPServiceApplicationProxyGroupMember.

See also

## See also

Concepts

#### Concepts

Share service applications across farms in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
