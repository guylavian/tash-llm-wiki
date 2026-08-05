---
title: "Manage permissions for a web application in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-manage-permissions-for-a-web-application
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/manage-permissions-for-a-web-application
family: administration
documentKind: "how-to"
abstract: "Learn how to globally enable or disable permissions for SharePoint Server web applications."
---

# Manage permissions for a web application in SharePoint Server - SharePoint Server

Note

Manage permissions for a web application in SharePoint Server

# Manage permissions for a web application in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Sites and site collections have a variety of permissions that you can set, such as adding or editing list items or documents. These permissions are normally given to a user by assigning them to a particular permission level, such as Full Control, Contribute, or View Only.

Each individual permission can be enabled or disabled for an entire web application. (All permissions are enabled by default.) For example, if you know that you'll never be using the Client Object Model or SharePoint Designer to access your sites, you can disable the Use Remote Interfaces permission. Doing so will prevent that permission from being granted to any users regardless of which permission level they're assigned.

If you want to set permissions for specific users or groups in a web application, you can create a permission policy for the web application.

Use the following procedure to update the user permissions for a web application. Be sure you're a member of the Farm Administrator's group before following this procedure.

**To manage permissions for a web application**

Start SharePoint 2016 Central Administration.

On the SharePoint Central Administration website, in the **Application Management** section, click **Manage web applications**.

In the web applications list, click the web application for which you want to manage permissions.

In the **Security** group of the ribbon, click **User Permissions**.

In the **User Permissions for Web Application** dialog, select the check boxes next to the permissions that you want to enable, and clear the check boxes next to those permissions that you want to disable.

You can select all permissions by selecting the **Select All** check box. You can clear all permissions by clearing the **Select All** check box.

Click **Save**.

See also

## See also

Concepts

#### Concepts

Administration of SharePoint Server

Manage permission policies for a web application in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
