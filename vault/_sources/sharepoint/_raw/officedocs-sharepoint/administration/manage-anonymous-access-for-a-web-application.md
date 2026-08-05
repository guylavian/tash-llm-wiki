---
title: "Manage anonymous access for a web application in SharePoint Server - SharePoint Server"
description: "Learn how to grant or deny anonymous access to a web application in SharePoint Server."
ms.topic: how-to
---
Note

Manage anonymous access for a web application in SharePoint Server

# Manage anonymous access for a web application in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can enable or disable anonymous access for a web application. If you enable anonymous access for a web application, site administrators can then grant or deny anonymous access at the site collection, site, or item level. If anonymous access is disabled for a web application, no sites within that web application can be accessed by anonymous users.

Note

Both classic and modern experience sites support anonymous access.

The following permission policies can be specified for anonymous users:

**None:** No policy is specified. This setting gives anonymous users the same default permissions available to NT AUTHORITY\Authenticated Users and All Authenticated Users.

**Deny Write:** This setting enables anonymous users to read all content within the site collections in a web application. You can then restrict the Read access by site collection, site, or item.

**Deny All:** Anonymous users have no access to any part of the web application.

Use the following procedure to configure anonymous access for a web application.

**To configure anonymous access for a web application**

Start SharePoint 2016 Central Administration.

On the SharePoint Central Administration website, in the **Application Management** section, click **Manage web applications**.

Click to highlight the web application whose permission policy that you want to manage.

In the **Security** group of the ribbon, click **Authentication Providers**.

Click the zone where you want to enable anonymous access.

Ensure that the **Enable anonymous access** check box is selected, and click **OK**.

In the **Policy** group of the ribbon, click **Anonymous Policy**.

In the Anonymous Access Restrictions dialog, in the ** Zone ** list, click the zone for which you want the policy to apply.

In the **Permissions** section, select the permission policy that you want anonymous users to have, and then click **Save**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
