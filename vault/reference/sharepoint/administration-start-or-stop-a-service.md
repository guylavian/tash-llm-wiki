---
title: "Start or stop a service in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-start-or-stop-a-service
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/start-or-stop-a-service
family: administration
documentKind: "how-to"
abstract: "Learn how to start and stop a service in SharePoint Server."
---

# Start or stop a service in SharePoint Server - SharePoint Server

Note

Start or stop a service in SharePoint Server

# Start or stop a service in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint Server includes services that reside on individual servers in the farm. In some cases, you can configure global service settings and start or stop a service. Services are managed directly in the SharePoint Central Administration website instead of through a separate administration site. You can also remotely monitor and manage services. Additionally, you can manage services by using Microsoft PowerShell.

Starting or stopping a service

## Starting or stopping a service

You can manage services by using Central Administration or by using PowerShell.

**To start or stop a service by using Central Administration**

Confirm that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.

On the Central Administration home page, click **System Settings**.

On the System Settings page, in the **Servers** section, click **Manage services on server**.

To change the server on which you want to start or stop the service, on the **Server** menu, click **Change Server**, and then click the server name that you want.

By default, only configurable services are displayed. To view all services, on the **View** menu, click **All**.

To start or stop a service, click **Restart** or **Stop** in the **Action** column of the relevant service.

Click **OK** to start or stop the service.

**To start a service by using Microsoft PowerShell**

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
Start-SPServiceInstance -Identity <ServiceGUID>
```

Where *<ServiceGUID>* is the GUID of the service. If you do not know the service GUID, you can retrieve a list of all services in the farm together with their GUIDs by using the **Get-SPServiceInstance** cmdlet.

For more information, see Start-SPServiceInstance.

**To stop a service by using PowerShell**

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Stop-SPServiceInstance -Identity <ServiceGUID>
```

Where  *<ServiceGUID>* is the GUID of the service. If you do not know the service GUID, you can retrieve a list of all services in the farm together with their GUIDs by using the **Get-SPServiceInstance** cmdlet.

For more information, see Stop-SPServiceInstance. We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

See also

## See also

Concepts

#### Concepts

Administration of SharePoint Server

Other Resources

#### Other Resources

Get-SPServiceInstance

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
