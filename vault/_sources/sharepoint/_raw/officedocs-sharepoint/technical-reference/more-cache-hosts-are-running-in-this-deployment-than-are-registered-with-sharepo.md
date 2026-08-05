---
title: "More cache hosts are running in this deployment than are registered with SharePoint (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: More Cache hosts are running in this deployment than are registered with SharePoint, for SharePoint Server."
ms.topic: troubleshooting
---
Note

More cache hosts are running in this deployment than are registered with SharePoint (SharePoint Server)

# More cache hosts are running in this deployment than are registered with SharePoint (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** More Cache hosts are running in this deployment than are registered with SharePoint.

**Summary:** Some cache hosts are running but not registered with SharePoint Server.

**Cause:**SharePoint Server fails to identify some cache hosts.

**Resolution: Log on to the cache host that is not registered with SharePoint Server, and then manually stop the AppFabric Caching Service.**

Identify the cache hosts that are not registered with SharePoint Server. To do this, in the SharePoint Central Administration website, in the **Monitoring** section, click **Review problems and solutions**, and then find the name of the server in the **Failing Servers** list. If there are multiple failing servers in a server farm, you must repeat the following steps on each failing server.

Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.

On **Server Manager**, click **Tools**, and then select **Services**.

In the **Services** list, double-click **AppFabric Caching Service**.

In the **AppFabric Caching Service Properties (Local Computer)** dialog, click **Stop**.

See also

## See also

Concepts

#### Concepts

Manage the Distributed Cache service in SharePoint Server

Plan for feeds and the Distributed Cache service in SharePoint Server

Other Resources

#### Other Resources

Planning and using the Distributed Cache service

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
