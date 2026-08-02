---
title: "The Net.Pipe Listener Adapter isn't available (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-the-net-pipe-listener-adapter-isn-t-available
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/the-net-pipe-listener-adapter-isn-t-available
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: The Net.Pipe Listener Adapter isn't available, for SharePoint Server."
---

# The Net.Pipe Listener Adapter isn't available (SharePoint Server) - SharePoint Server

Note

The Net.Pipe Listener Adapter isn't available (SharePoint Server)

# The Net.Pipe Listener Adapter isn't available (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** The Net.Pipe Listener Adapter isn't available.

**Summary:** The Net.Pipe Listener Adapter is a Windows service that receives activation requests over the net.pipe protocol and passes them to the Windows Process Activation Service.

**Cause:** If the Net.Pipe Listener Adapter service is not installed or started then the SharePoint Health Analyzer rule triggers an alert.

**Resolution: Start the Net.Pipe Listener Adapter service on the server**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

In Server Manager, click **Tools**, and then click **Services**.

In Services, double-click **Net.Pipe Listener Adapter** and make sure it is running.

Note

If the Net.Pipe Listener Adapter service is not found in the Services list you need to install it. The executable you need to run is SMSvcHost.exe and can be found at C:\Windows\Microsoft.NET\Framework64\v4.0.30319\SMSvcHost.exe.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
