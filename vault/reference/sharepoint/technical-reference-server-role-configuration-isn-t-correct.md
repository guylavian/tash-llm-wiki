---
title: "Server role configuration isn't correct (SharePoint Server 2016) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-server-role-configuration-isn-t-correct
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/server-role-configuration-isn-t-correct
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: Server role configuration isn't correct, for SharePoint Server."
---

# Server role configuration isn't correct (SharePoint Server 2016) - SharePoint Server

Note

Server role configuration isn't correct (SharePoint Server 2016)

# Server role configuration isn't correct (SharePoint Server 2016)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Server role configuration isn't correct.

**Summary:** This new rule helps ensure that your servers are operating in their optimal MinRole configuration. This rule runs every night at midnight on each server in your SharePoint Server 2016 farm. The rule scans all service instances on the server to detect if any are not in compliance.

**Cause:** A service application on the server isn't correctly configured.

**Resolution: Automatically reconfigures the service to match the expected configuration**

If any service instance is not in compliance, the health rule automatically reconfigures the service to match the expected configuration.

No manual intervention by the SharePoint farm administrator is required.

The automatic repair functionality of this health rule can be disabled by the SharePoint farm administrator while still allowing the health rule to run.

If the health rule detects that a server is out of compliance and the automatic repair functionality is disabled, it generates a health report in Central Administration. The health report identifies which servers are out of compliance and offers the ability to automatically repair the server and also provide instructions about how to manually fix the servers.

For more information, see the Health monitoring section in Overview of MinRole Server Roles in SharePoint Server 2016.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
