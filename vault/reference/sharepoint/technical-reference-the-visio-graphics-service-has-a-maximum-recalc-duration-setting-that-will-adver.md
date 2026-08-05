---
title: "The Visio Graphics Service has a maximum recalc duration setting that will adversely impact user perceived performance ((SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-the-visio-graphics-service-has-a-maximum-recalc-duration-setting-that-will-adver
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/the-visio-graphics-service-has-a-maximum-recalc-duration-setting-that-will-adver
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: The Visio Graphics Service has a maximum recalc duration setting that will adversely impact user perceived performance, for SharePoint Server."
---

# The Visio Graphics Service has a maximum recalc duration setting that will adversely impact user perceived performance ((SharePoint Server) - SharePoint Server

Note

The Visio Graphics Service has a maximum recalc duration setting that will adversely impact user perceived performance ((SharePoint Server)

# The Visio Graphics Service has a maximum recalc duration setting that will adversely impact user perceived performance ((SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** The Visio Graphics Service has a maximum recalc duration setting that will adversely impact user perceived performance

**Summary:** The Visio Graphics Service has a maximum recalculation duration setting that will adversely affect performance. If the **Maximum Recalc Duration** setting is longer than 60 seconds, it might result in large processor load of the Visio Graphics Service and SharePoint Server, decreasing the expected performance of both.

A shorter duration increases performance by only allowing simple data-connected diagrams to be recalculated by the server, minimizing CPU and memory usage. A longer duration allows the recalculation of more complex data-connected diagrams while using more CPU cycles and memory. The default duration is 60 seconds.

**Cause:** The **Maximum Recalc Duration** setting was set longer than 60 seconds.

**Resolution: Decrease the value of the Maximum Recalc Duration setting**

Verify that the user account that is performing this procedure is an administrator of the Visio Graphics Service service application.

In Central Administration, in the **Application Management** section, click **Manage service applications**.

On the Service Applications page, click the Visio Graphics service application.

On the Manage the Visio Graphics Service page, click **Global Settings**.

Ensure that the settings have the values that are listed in the following table. If they do not, type the value in the corresponding text box and click **OK**.

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
