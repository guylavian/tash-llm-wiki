---
title: "The number of Distributed Cache hosts in the farm exceeds the recommended value (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-the-number-of-distributed-cache-hosts-in-the-farm-exceeds-the-recommended-value
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/the-number-of-distributed-cache-hosts-in-the-farm-exceeds-the-recommended-value
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: The number of Distributed Cache hosts in the farm exceeds the recommended value, for SharePoint Server."
---

# The number of Distributed Cache hosts in the farm exceeds the recommended value (SharePoint Server) - SharePoint Server

Note

The number of Distributed Cache hosts in the farm exceeds the recommended value (SharePoint Server)

# The number of Distributed Cache hosts in the farm exceeds the recommended value (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** The number of Distributed Cache hosts in the farm exceeds the recommended value.

**Summary:** On a farm with four or more servers, you must not start the Distributed Cache service on all servers on the farm. You can only run Distributed cache on SharePoint Server 2016 servers that are configured as Distributed cache role in MInRole. If you configure all servers as cache hosts, you may experience reliability and performance problems in the farm. For more information, see Overview of MinRole Server Roles in SharePoint Server 2016.

**Cause:** The Distributed Cache service is started on every server on this farm.

**Resolution: Reduce the number of cache hosts by using Windows PowerShell.**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the Microsoft PowerShell cmdlets.

Farm Administrators group.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

Remove one or more servers from the cache cluster. On each server that you want to remove from the cache cluster, run the following cmdlet:

`Remove-SPDistributedCacheServiceInstance`

Verify that the server is removed from the cache cluster. To do this, in the SharePoint Central Administration website, click **Manage services on server**, and then, on the **Services on Server** page, make sure that the Distributed Cache service is not listed for the server from which you removed the service.

See also

## See also

Concepts

#### Concepts

Manage the Distributed Cache service in SharePoint Server

Plan for feeds and the Distributed Cache service in SharePoint Server

Other Resources

#### Other Resources

Add-SPDistributedCacheServiceInstance

Planning and using the Distributed Cache service

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
