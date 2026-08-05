---
title: "The Visio Graphics Service has a minimum cache age setting that will adversely impact performance ((SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: The Visio Graphics Service has a minimum cache age setting that will adversely impact performance, for SharePoint Server."
ms.topic: troubleshooting
---
Note

The Visio Graphics Service has a minimum cache age setting that will adversely impact performance ((SharePoint Server)

# The Visio Graphics Service has a minimum cache age setting that will adversely impact performance ((SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** The Visio Graphics Service has a minimum cache age setting that will adversely impact performance

**Summary:** The Visio Graphics Service has a minimum cache age setting that will adversely affect performance. If the **Minimum Cache Age** setting is shorter than 5 minutes, it might result in large processor and network load of the Visio Graphics Service and SharePoint Server, decreasing the expected performance of both. However, increasing this value means that users will not see their data-connected diagrams refreshing as frequently.

**Cause:** The **Minimum Cache Age** setting was set shorter than 5 minutes.

**Resolution: Increase the value of the Minimum Cache Age setting**

Verify that the user account that is performing this procedure is an administrator of the Visio Graphics Service service application.

In Central Administration, on the Home page, in the **Application Management** section, click **Manage service applications**.

On the Service Applications page, click the Visio Graphics service application.

On the Manage the Visio Graphics Service page, click **Global Settings**.

Ensure that the settings have the values listed in the following table. If they do not, type the values in the corresponding text boxes, and then click **OK**.

| **Setting** | **Value** |
| --- | --- |
| **Maximum Web Drawing Size** | <= 25 (Megabytes) |
| **Minimum Cache Age** | >= 5 (Minutes) |
| **Maximum Cache Age** | <= 60 (Minutes) |
| **Maximum Recalc Duration** | <= 60 (Seconds) |
| **Maximum Cache Size** | >= 5120 (Megabytes) |

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
