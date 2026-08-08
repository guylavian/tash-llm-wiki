---
title: "Automatic Update setting inconsistent across farm servers (SharePoint Server 2016) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: Automatic update setting inconsistent across farm servers, for SharePoint Server."
ms.topic: troubleshooting
---
Note

Automatic Update setting inconsistent across farm servers (SharePoint Server 2016)

# Automatic Update setting inconsistent across farm servers (SharePoint Server 2016)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365.

**Rule Name:** Automatic update setting inconsistent across farm servers.

**Summary:** Servers in the SharePoint farm do not have the same Automatic Update settings configured.

**Cause:** One or more servers in the farm have update settings that are different from the other servers in the farm.

**Resolution: Ensure all servers in the farm have the same update settings**

Verify that you are a member of the Administrators group on the local computer.

In Control Panel, click **System and Security**, and then under **Windows Update**, click **Turn automatic updating on or off**.

On the Choose your Windows Update settings page, make sure that the update settings are the same as other servers in your farm. Change the update settings if needed.

Note

If you can't change the update settings, the update settings may be locked in group policy. If this is the case, ensure the same group policy is being applied to other servers in the farm.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
