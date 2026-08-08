---
title: "One or more servers can't retrieve People Picker credentials (SharePoint Server 2019) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: One or more servers can't retrieve People Picker credentials, for SharePoint Server."
ms.topic: troubleshooting
---
Note

One or more servers can't retrieve People Picker credentials (SharePoint Server 2019)

# One or more servers can't retrieve People Picker credentials (SharePoint Server 2019)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** One or more servers can't retrieve People Picker credentials.

**Summary:** The People Picker is configured to use specific credentials when searching for users in certain forests or domains. There are one or more servers in this farm that can't retrieve these credentials. Without these credentials, the People Picker won't be able to search for users in those forests or domains from these servers.

**Cause:** The application credential key wasn't found on these servers or they don't have the same application credential key originally used to store the People Picker credentials. Servers must have an application credential key to store and retrieve People Picker credentials. The application credential key must be identical on each server.

**Resolution:** Use the **Set-SPApplicationCredentialKey** cmdlet on each failing server to set the application credential key. If the current People Picker credentials were stored using a different application credential key, you must set the new application credential key on every server in the farm and then save the People Picker credentials again.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
