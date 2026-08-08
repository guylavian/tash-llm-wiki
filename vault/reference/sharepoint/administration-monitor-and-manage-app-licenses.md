---
title: "Monitor and manage app licenses in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-monitor-and-manage-app-licenses
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/monitor-and-manage-app-licenses
family: administration
documentKind: "how-to"
abstract: "Learn how SharePoint Server farm administrators assign, monitor, and manage the app for SharePoint Server licenses in SharePoint Server."
---

# Monitor and manage app licenses in SharePoint Server - SharePoint Server

Note

Monitor and manage app licenses in SharePoint Server

# Monitor and manage app licenses in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can use the SharePoint Central Administration website to monitor and manage licenses for apps for SharePoint. Licenses for apps for SharePoint are digital sets of verifiable information that state the user rights for an app for SharePoint. Apps that are distributed through the SharePoint Store are the only apps that have built-in licenses that SharePoint Server recognizes.

Members of the Farm Administrators group manage licenses for apps and can also assign license managers for others to manage app for SharePoint licenses.

Here are the basics of what SharePoint Server does and doesn't provide for apps for SharePoint licensing:

SharePoint Server provides:

Storefront to obtain apps

Storage and renewal of app for SharePoint licenses

User Interface (UI) to assign users to specific app for SharePoint licenses

APIs for developers to query for license information

SharePoint Server doesn't enforce app for SharePoint licenses.

Developers must add code in their apps for SharePoint to retrieve license information and react accordingly.

All apps for SharePoint licenses are bound to a specific SharePoint Server deployment but can be transferred to a different SharePoint Server deployment three times.

Monitoring and managing app licenses

## Monitoring and managing app licenses

A farm administrator or a license manager can check the licenses for all apps for SharePoint on the App Licenses page. It's important to track the number of licenses that are available for each app for SharePoint so that users don't exceed this number. An administrator can assign more users to an app for SharePoint license, purchase more licenses for an app, and also add managers to a license.

**To view app license details**

In Central Administration, click **Apps**.

On the **Apps** page, in the **SharePoint and Office Store** section, click **Manage App Licenses**.

On the **Manage App Licenses** page, click an app for SharePoint in the list to view the license details.

The **Manage App License** page shows detailed licensing information. This includes the name of the app, the developer, and current license details.

In the top section, click the drop-down arrow in the dialog to see purchase details for the selected app for SharePoint.

The app details include the following information:

Number of licenses available for users

License type

App purchaser name

**To add users to the app license**

On the **Manage App Licenses** page, click an app for SharePoint for which you want to add users.

In the **People with a License** section, click **assign people**.

In the dialog that appears below, enter the user name that you want to add and then, click **Add User**.

The user name is added to the list at the bottom of this section and the number of available licenses for this app is refreshed for the selected app for SharePoint.

**To purchase more app licenses**

On the **Manage App Licenses** page, click an app for SharePoint for which you want to purchase more licenses.

In the **People with a License** section, click **buy more licenses**.

The SharePoint Store opens with the specific app showing the details with links to purchase additional licenses. Choose the number of Apps you want to purchase and then click **OK**.

**To remove app licenses**

On the **Manage App Licenses** page, click an app for SharePoint for which you want to remove licenses.

On the **Actions** drop down list, click **Remove this License**.

**Verification:** Optionally, include steps that users should perform to verify that the operation was successful.

**To recover app licenses**

On the **Manage App Licenses** page, click an app for SharePoint for which you want to recover licenses.

On the **Actions** drop down list, click **Recover License**.

The app for SharePoint details shows any changes the administrator has made.

**To add a license manager**

On the **Manage App License** page, in the **License Managers** section, click **add manager**.

Below the License Managers section, the new App manager appears in the list.

See also

## See also

Concepts

#### Concepts

Configure an environment for apps for SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
