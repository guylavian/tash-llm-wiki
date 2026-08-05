---
title: "Product / patch installation or server upgrade required (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: Product / patch installation or server upgrade required for SharePoint Server."
ms.topic: troubleshooting
---
Note

Product / patch installation or server upgrade required (SharePoint Server)

# Product / patch installation or server upgrade required (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Product / patch installation or server upgrade required.

**Summary:** You must install all required products on all servers in the farm, and all products should have the same software update and upgrade level across the farm.

**Cause:** You haven't installed required products or updates, or the server needs to be upgraded.

**Resolution: Install software updates and security updates or upgrade the server.**

- Check if there are any pending updates and restart all the servers.

**Install updates on the server.**

Log on to one server.

Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.

Open **Windows Update**. and check to see if there are any pending updates or a restart is required, schedule the updates or restart the computer.

Repeat the previous steps on all servers.

For more information, see Deploy software updates for SharePoint Server 2016.

If a previous upgrade attempt has failed, you must resolve upgrade issues before attempting upgrade again. You can use the SharePoint Central Administration website to find information about current and previous upgrade attempts and determine issues that may be preventing upgrade from succeeding. To do this in Central Administration, in the **Upgrade and Migration** section, select **Check upgrade status**.

Additional resources

## Additional resources

- Last updated on 
		2024-05-30
