---
title: "Role conversion using MinRole in SharePoint Servers 2016, 2019, and Subscription Edition - SharePoint Server"
description: "Learn about how to convert your server roles in a SharePoint farm deployment using MinRole. MinRole help administrators select the right server role when provisioning SharePoint Server."
ms.topic: article
---
Note

Role conversion using MinRole in SharePoint Servers 2016, 2019, and Subscription Edition

# Role conversion using MinRole in SharePoint Servers 2016, 2019, and Subscription Edition

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Role Conversion

## Role Conversion

**About Server Role Conversion**

Servers can be converted to a different server role without having to disconnect them from your farm and then rejoining them using the different server role. Servers can be converted to dedicated roles, shared roles, the Custom server role, or the Single-Server Farm server role. Server role conversion can be performed through the SharePoint Central Administration website or Microsoft PowerShell.

Note

You can only convert a server to the Single-Server Farm server role if it is the only SharePoint server in the farm.

Before a server is converted to a different server role, SharePoint will perform a role conversion pre-validation check to ensure the server is ready for role conversion. If the pre-validation check determines that a server isn't ready for role conversion, it will block the role conversion and present a message explaining why the role conversion was blocked. It will also provide instructions to resolve the issue that blocked role conversion. Once the issue is resolved, you can rerun the role conversion.

Note

Role conversion pre-validation was first introduced in the November 2016 Public Update for SharePoint Server 2016 (Feature Pack 1).

**Distributed Cache and role conversion**

Role conversion can't automatically enable, disable, or reconfigure the Distributed Cache service. You must manually enable, disable, or reconfigure the Distributed Cache service before performing role conversion. If this step isn't performed before role conversion, role conversion pre-validation will block the role conversion.

To enable the Distributed Cache service, the administrator runs the **Add-SPDistributedCacheServiceInstance** cmdlet on the target server, specifying the desired role with the **Role** parameter (that is,  `-Role <role name>`). To disable the Distributed Cache service, the administrator runs the **Remove-SPDistributedCacheServiceInstance** cmdlet on the target server.

**Search and role conversion**

Role conversion can't convert a server from a role hosting Search to a role that doesn't host Search if the server is part of an active Search topology. Remove the server from the active Search topology before performing role conversion. If this step isn't performed before role conversion, role conversion pre-validation will block the role conversion.

Note

After you convert a server to a role that hosts Search, you must add the server into the active Search topology.

How to change a server role

## How to change a server role

**To change a server role by using the Central Administration Web site**

Verify that the user account that is performing this procedure is a member of the local Administrators group.

On the Central Administration web site, click **System Settings**.

On the **System Settings** page, click **Convert server role in this farm**.

On the **Role Conversion** page, in the **New Role** area, click the drop-down box to select the new server role for each server to change.

Click **Apply**.

**To change a server role by using PowerShell**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Local Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the Add-SPShellAdmin cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.

Note

If you do not have permissions, contact your setup administrator or SQL Server administrator to request permissions. For more information about PowerShell permissions, see Add-SPShellAdmin.

On the **Start** menu, click **Microsoft SharePoint Products**.

Click **SharePoint Management Shell**.

At the PowerShell command prompt, type the following command:

```
Set-SPServer -Identity <server name> -Role <server role>
```

Where:

*<server name>* is the server to change.

*<server role>* is the name of the new server role, which includes the values: WebFrontEnd, Application, DistributedCache, Search, WebFrontEndWithDistributedCache, ApplicationWithSearch, SingleServerFarm, or Custom.

For more information about how to change a server role by using PowerShell, see Set-SPServer.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
