---
title: "Application pools recycle when memory limits are exceeded (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: Application pools recycle when memory limits are exceeded, for SharePoint Server."
ms.topic: troubleshooting
---
Note

Application pools recycle when memory limits are exceeded (SharePoint Server)

# Application pools recycle when memory limits are exceeded (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Application pools recycle when memory limits are exceeded.

**Summary:** Application pools recycle because memory limits have been enabled and exceeded. Recycling based on memory limits is not usually necessary in a 64-bit environment, and therefore recycling should not be enabled. Unnecessary recycling can result in dropped requests from the recycled worker process and slow performance for end users who are making requests to the new worker process.

**Cause:** Application pools are configured to recycle when memory limits are exceeded.

**Resolution: Change the application pool recycling settings in Internet Information Services (IIS).**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

Identify the server on which this event occurs. On the SharePoint Central Administration website, in the **Monitoring** section, click **Review problems and solutions**, and then find the name of the server in the **Failing Servers** column. If there are multiple failing servers in a server farm, you must repeat the following steps on each failing server.

Verify that the user account that is performing the following steps is a member of the Administrators group on the local computer that you identified in the previous step.

Log on to the server on which this event occurs.

In Server Manager, click **Tools**, and then click **Internet Information Services (IIS) Manager**.

In the Internet Information Services management console, in the **Connections** pane, expand the tree view, and then click **Application Pools**.

In the **Application Pools** list, right-click the application pool on which you want to disable the memory limits, and then click **Recycling**.

In the **Edit Application Pool Recycling Settings** dialog, in the **Memory Based Maximums** section, clear the **Virtual memory usage (in KB)** and **Private memory usage (in KB)** check boxes, and then click **Next**.

In the **Recycling Events to Log** dialog, click **Finish**.

See also

## See also

Other Resources

#### Other Resources

Recycling Settings for an Application Pool <recycling>

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
