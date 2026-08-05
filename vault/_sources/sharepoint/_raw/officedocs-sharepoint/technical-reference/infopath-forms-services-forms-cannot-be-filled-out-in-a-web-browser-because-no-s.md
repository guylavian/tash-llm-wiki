---
title: "InfoPath Forms Services forms cannot be filled out in a Web browser because no State Service connection is configured (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: InfoPath Forms Services forms cannot be filled out in a Web browser because no State Service connection is configured."
ms.topic: troubleshooting
---
Note

InfoPath Forms Services forms cannot be filled out in a Web browser because no State Service connection is configured (SharePoint Server)

# InfoPath Forms Services forms cannot be filled out in a Web browser because no State Service connection is configured (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** InfoPath Forms Services forms cannot be filled out in a Web browser because no State Service connection is configured.

**Summary:** InfoPath Forms Services depends on the Web application having a service connection to a State Service Proxy to store data across HTTP requests. Without a service connection, users cannot successfully open or fill browser-enabled InfoPath forms.

**Cause:** No service connection for the State Service is configured for the Web application that is in the Health Analyzer alert.

Note

Infopath form service is removed and is no longer supported by Microsoft in SharePoint Server Subscription Edition. We recommend exploring Microsoft Power Apps as a potential alternative to Infopath form service.

**Resolution: Configure a service connection by using the SharePoint Central Administration website**

Verify that the user account performing this procedure is a member of the Farm Administrators group.

If a State Service already exists, you must associated the State Service with the Web application mentioned tin the health analyzer rule.

In Central Administration, under **Application Management**, click ** Manage web applications **.

On the Web Applications page, click the Web application for which you want to configure a service connection, and then click **Service Connections** on the ribbon.

In the **Configure Service Application Associations** dialog, ensure that the **State Service** check box is selected, and then click **OK**.

**Create a new State Service application by using Microsoft PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 Products cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
New-SPStateServiceDatabase -Name "State Service Database" | New-SPStateServiceApplication -Name "StateServiceApp1" | New-SPStateServiceApplicationProxy -DefaultProxyGroup
```

For more information, see New-SPStateServiceApplication.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
