---
title: "One or more services have started or stopped unexpectedly (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-one-or-more-services-have-started-or-stopped-unexpectedly
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/one-or-more-services-have-started-or-stopped-unexpectedly
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: eOne or more services have started or stopped unexpectedly, for SharePoint Server."
---

# One or more services have started or stopped unexpectedly (SharePoint Server) - SharePoint Server

Note

One or more services have started or stopped unexpectedly (SharePoint Server)

# One or more services have started or stopped unexpectedly (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** One or more services have started or stopped unexpectedly.

**Summary:** A critical service required for the SharePoint farm to function isn't running.

**Cause:** One or more critical services aren't running on the specified server.

**Resolution: Start the service that is not running**

Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.

In Server Manager, select **Tools**, and then select **Services**.

Right-click the service that you want to start, and then select **Start**.

Additional resources

## Additional resources

- Last updated on 
		2024-05-30
