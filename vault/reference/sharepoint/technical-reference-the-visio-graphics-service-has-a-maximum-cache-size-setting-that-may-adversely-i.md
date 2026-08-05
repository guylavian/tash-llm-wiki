---
title: "The Visio Graphics Service has a maximum cache size setting that may adversely impact performance ((SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-the-visio-graphics-service-has-a-maximum-cache-size-setting-that-may-adversely-i
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/the-visio-graphics-service-has-a-maximum-cache-size-setting-that-may-adversely-i
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: The Visio Graphics Service has a Maximum Cache Size setting that will adversely impact performance, for SharePoint Server."
---

# The Visio Graphics Service has a maximum cache size setting that may adversely impact performance ((SharePoint Server) - SharePoint Server

Note

The Visio Graphics Service has a maximum cache size setting that may adversely impact performance ((SharePoint Server)

# The Visio Graphics Service has a maximum cache size setting that may adversely impact performance ((SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** The Visio Graphics Service has a Maximum Cache Size setting that will adversely impact performance

**Summary:** The Visio Graphics Service has a maximum Cache size setting that will adversely affect performance. If the **Maximum Cache Size** setting is smaller than 1024 MB, it might decrease the expected performance of the Visio Graphics Service.

**Cause:** The **Maximum Cache Size** setting was set smaller than 1024 MB.

**Resolution: Increase the value of the Maximum Cache Size setting**

Verify that the user account that is performing this procedure is an administrator of the Visio Graphics Service service application.

In Central Administration, on the Home page, in the **Application Management** section, click **Manage service applications**.

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
