---
title: "Enable search alerts in SharePoint Server - SharePoint Server"
description: "Learn how to enable or disable search alerts."
ms.topic: how-to
---
Note

Enable search alerts in SharePoint Server

# Enable search alerts in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Search alerts allow end-users to receive e-mail notification when specified search query results are changed or updated. Search alerts should be enabled when you want allow end-users to create alerts for search queries. Search alerts may be configured on the search query page when a search query is completed and results are displayed. Search alerts are created and configured per-user and are only configurable and viewable by the user who creates them. Search alerts are enabled by default. Use this procedure to enable or disable search alerts.

Before you begin

## Before you begin

Before you begin this operation, have this in place:

A Search service application

A User Profile service application

To enable or disable search alerts

### To enable or disable search alerts

Verify that the user account that is performing this procedure is an administrator for the Search service application.

In Central Administration, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, click the Search service application for which you want to configure search alerts.

On the Search Administration page, in the **System Status** section, locate **Search alerts status**.

The search alerts status displays as **Off** **Enable** or **On** **Disable**.

By default, search alerts are turned **On**. Click **Disable** to turn off search alerts or click **Enable** to turn on search alerts.

The option is now set. Search alerts are sent only if outgoing e-mail is configured. For more information, see Configure outgoing email for a SharePoint Server farm. If you enabled search alerts, users can create search alerts for search queries that they run. To configure search alerts for search queries, users can click the **Alert Me** link that is located on the bottom of the Search Results page. The **Alert Me** link will appear a few minutes after search alerts are turned on. If search alerts are turned off, this icon does not appear.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
