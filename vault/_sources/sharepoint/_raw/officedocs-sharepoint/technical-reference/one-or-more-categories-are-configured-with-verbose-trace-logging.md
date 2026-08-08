---
title: "One or more categories are configured with Verbose trace logging (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: One or more categories are configured with verbose trace logging, for SharePoint Server."
ms.topic: troubleshooting
---
Note

One or more categories are configured with Verbose trace logging (SharePoint Server)

# One or more categories are configured with Verbose trace logging (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** One or more categories are configured with Verbose trace logging.

**Summary:** SharePoint Server writes diagnostic logging information to record activity on the server. The logs contain information that can help you diagnose server problems. This rule occurs when diagnostic logging is set to verbose. The verbose setting is appropriate when you have to diagnose a server problem, but you should turn off verbose logging during normal operations.

**Cause:** One or more categories of diagnostic logging are set to verbose.

**Resolution: Reset diagnostic logging to the default level**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, click **Monitoring**.

On the Monitoring page, in the **Reporting** section, click **Configure diagnostic logging**.

On the Diagnostic Logging page, in the **Event Throttling** section, in the **Least critical event to report to the event log** list and **Least critical event to report to the trace log** list, select **Reset to default**.

Click **OK**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
