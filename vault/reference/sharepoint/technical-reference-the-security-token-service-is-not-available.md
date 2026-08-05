---
title: "The Security Token Service is not available (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-the-security-token-service-is-not-available
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/the-security-token-service-is-not-available
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: The Security Token Service is not available, for SharePoint Server."
---

# The Security Token Service is not available (SharePoint Server) - SharePoint Server

Note

The Security Token Service is not available (SharePoint Server)

# The Security Token Service is not available (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** The Security Token Service isn't available.

**Summary:** The Security Token Service isn't issuing tokens.

**Cause:** The service could be malfunctioning or in a bad state, some assemblies are missing when you deploy the custom claims provider, or the STS certificate has expired.

**Resolution: Restart the Security Token Service application pool.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

Identify the server on which this event occurs. On the SharePoint Central Administration website, in the **Monitoring** section, select **Review problems and solutions**, and then find the name of the server in the **Failing Servers** column. If there are multiple failing servers in a server farm, you must repeat the following steps on each failing server.

Verify that the user account that is performing the following steps is a member of the Administrators group on the local computer that you identified in the previous step.

Log on to the server on which this event occurs.

Open **Server Manager,** select **Tools**, and then select **Internet Information Services (IIS) Manager**.

In the Internet Information Services management console, in the **Connections** pane, expand the tree view, and then select **Application Pools**.

In the **Application Pools** list, right-click **SecurityTokenServiceApplicationPool**, and then select **Start**. If the application pool is started already, select **Stop** and then, in the **Action** pane, select **Start** to restart it.

**Resolution: Install the missing assemblies into the global assembly cache (GAC) manually.**

Check the event logs and ULS logs on all servers to find out which assemblies of the custom claims provider are missing.

Install the missing assemblies into the global assembly cache manually. For more information, see How to: Install an Assembly into the Global Assembly Cache.

**Resolution: Replace the STS certificate.**

Check in the Application Event Log for the Event ID 8311 to confirm that the STS certificate is expired.

Replace the STS certificate. For more information, see Replace the STS certificate for SharePoint Server.

**Resolution: Update the STS certificate**

Confirm whether the STS certificate has expired by looking for Windows Application event log Event ID 8311 for source "SharePoint Foundation," category Topology, and with "NotTimeValid" in the message. This indicates an expired STS certificate. For more information on updating the STS certificate, please see Replace the STS certificate for SharePoint Server.

Additional resources

## Additional resources

- Last updated on 
		2024-05-30
