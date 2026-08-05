---
title: "Distributed cache service is not configured on server(s) (SharePoint Server 2016) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: Distributed cache service is not configured on server(s), for SharePoint Server."
ms.topic: troubleshooting
---
Note

Distributed cache service is not configured on server(s) (SharePoint Server 2016)

# Distributed cache service is not configured on server(s) (SharePoint Server 2016)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Distributed cache service is not configured on server(s).

**Summary:** The distributed cache service should be configured for the failing servers. Register the distributed cache host on the failing servers, and then start the service instances.

**Cause:** This rule occurs when you have used the MinRole feature in SharePoint Server 2016 to assign a distributed cache role to a server or servers but haven't registered the distributed cache host or started the service.

**Resolution: Use the Add-SPDistributedCacheServiceInstance cmdlet to register a cache host**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint 2016 Management Shell on each failing server.

Type the following command at the PowerShell command prompt on each failing server:

```
Add-SPDistributedCacheServiceInstance
```

For more information, see Add-SPDistributedCacheServiceInstance.

Related Topics

## Related Topics

Description of MinRole and associated services in SharePoint Server 2016

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
