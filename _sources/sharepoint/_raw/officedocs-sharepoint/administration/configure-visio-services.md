---
title: "Configure Visio Services - SharePoint Server"
description: "Configure Visio Services by using SharePoint Central Administration."
ms.topic: how-to
---
Note

Configure Visio Services

# Configure Visio Services

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The following steps show how to create a Visio Graphics Service service application.

To create a service application, you must be a member of the farm administrators group.

Create a Visio Services service application

## Create a Visio Services service application

**To create a Visio Graphics Service service application by using Central Administration**

On the SharePoint Central Administration website Home page, in the **Application Management** section, click **Manage service applications**.

Important

Visio Services requires the SharePoint Server Enterprise Site Collection Features feature to be active on each site collection where you plan to use the Visio Web Access Web Part.

On the ribbon, click **New**, and then click **Visio Graphics Service**.

Type a name for the new service application.

Choose an existing application pool or create a new one.

Choose whether to create a Visio Graphics Service Application Proxy (recommended).

Click **OK**.

If you are using SharePoint Server 2013, you must turn on the Visio Graphics Service on at least one server in your farm. (In Central Administration, click **Manage services on server**.) If you are using SharePoint Server 2016, the Visio Graphics Service is managed automatically by MinRole.

Configure Visio Services Global Settings

## Configure Visio Services Global Settings

**To configure Visio Services Global Settings**

On the SharePoint Central Administration website Home page, in the **Application Management** section, click **Manage service applications**.

Click the Visio Graphics Service service application that you want to configure.

On the Visio Graphics Service Settings page, configure the following settings:

| **Parameter** | **Description** |
| --- | --- |
| **Maximum Diagram Size** | The maximum size in MB of a diagram that can be rendered. A larger size limit may lead to slower performance if the server is under heavy load, whereas a smaller limit may prevent more complex diagrams from being rendered.  
 Valid values range from 1 to 50. The default value is 25 MB. |
| **Minimum Cache Age** | The minimum number of minutes that a diagram is cached in memory. Smaller values allow for more frequent data refresh operations for users, but increase CPU and memory usage on the server.  
 This value is per user per diagram. The interval begins when a user views a diagram. That user cannot refresh that diagram until the interval expires. The interval begins for other users when they first view the diagram.  
 This parameter applies to diagrams with data connections and diagrams with recalculations based on shape sheet functions. The automatic refresh setting in Visio Web Parts is also constrained by this setting.  
 Valid values range from 0 to 34560 minutes. The default value is 5 minutes. |
| **Maximum Cache Age** | The number of minutes after which cached diagrams are purged. Larger values decrease file I/O and CPU load but increase memory usage on the server.  
 Valid values range from 0 to 34560 minutes. The default value is 60 minutes. |
| **Maximum Recalc Duration** | The number of seconds before data refresh operations time out. Longer timeouts will allow for more complex data connected diagrams to be recalculated, but will use more processing power. This applies only to data connected diagrams.  
 This parameter applies to diagrams with data connections and diagrams with recalculations based on shape sheet functions.  
 Valid values range from 10 to 120. The default value is 60 seconds. |
| **Maximum Cache Size** | The maximum cache size in MB (between 100 and 1024000) that can be used. A larger size limit may lead to more disk resource usage by the service, while a smaller limit may impact performance.  
 Valid values range from 100 to 1024000. The default value is 5120 MB. |
| **External Data** | The target application ID in the registered Secure Store Service that is used to reference Unattended Service Account credentials. The Unattended Service Account is a single account that all documents can use to refresh data. It is required when you connect to data sources external to SharePoint Server, such as SQL Server. |

- Click **OK**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
