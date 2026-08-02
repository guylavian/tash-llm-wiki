---
title: "Distributed cache service is unexpectedly configured on server(s) (SharePoint Server 2016) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-distributed-cache-service-is-unexpectedly-configured-on-server-s
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/distributed-cache-service-is-unexpectedly-configured-on-server-s
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: Distributed cache service is unexpectedly configured on server(s), for SharePoint Server 2016."
---

# Distributed cache service is unexpectedly configured on server(s) (SharePoint Server 2016) - SharePoint Server

Note

Distributed cache service is unexpectedly configured on server(s) (SharePoint Server 2016)

# Distributed cache service is unexpectedly configured on server(s) (SharePoint Server 2016)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Distributed cache service is unexpectedly configured on server(s).

**Summary:** The distributed cache service instance should not be configured for the failing servers. Remove the distributed cache service instances from the failing servers.

Typically when you see this rule, it states that the distributed cache service is running on a server that doesn't support this service. The distributed cache service should only run on servers that are assigned to the following roles:

Distributed Cache

Front-end with Distributed Cache

Single-Server Farm

Custom

For more information, see Description of MinRole and associated services in SharePoint Server 2016.

**Cause:** This rule occurs when you have configured the distributed cache service on a server that is not supposed to run this service in a SharePoint Server 2016 farm.

**Resolution: Remove the distributed cache service instances from the failing servers**

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
Remove-SPDistributedCacheServiceInstance
```

For more information, see Remove-SPDistributedCacheServiceInstance.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
