---
title: "Distributed cache service is not enabled in this deployment (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: Distributed cache service is not enabled in this deployment, for SharePoint Server."
ms.topic: troubleshooting
---
Note

Distributed cache service is not enabled in this deployment (SharePoint Server)

# Distributed cache service is not enabled in this deployment (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Distributed cache service is not enabled in this deployment.

**Summary:** The Distributed Cache service is started on all servers that run SharePoint products at installation time. However, an administrator that performs maintenance and operational tasks might need to start and stop the Distributed Cache service. This event occurs when the Distributed Cache service is stopped.

**Cause:** The Distributed Cache service is disabled on this server.

**Resolution: Enable the Distributed Cache service by using Microsoft PowerShell.**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Farm Administrators group.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

On the server on which you want to enable the Distributed Cache service, run the following command:

`Add-SPDistributedCacheServiceInstance`

Verify that the Distributed Cache service is started. To do this, in the SharePoint Central Administration website, click **Application Management**. In the **Service Applications** section, click **Manage services on server**. On the **Services on Server** page, make sure that the Distributed Cache service is listed, and the status is **Started**.

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
