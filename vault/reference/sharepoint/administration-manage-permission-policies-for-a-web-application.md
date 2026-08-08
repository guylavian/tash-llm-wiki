---
title: "Manage permission policies for a web application in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-manage-permission-policies-for-a-web-application
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/manage-permission-policies-for-a-web-application
family: administration
documentKind: "how-to"
abstract: "Learn how to manage SharePoint Server web application permission policy levels."
---

# Manage permission policies for a web application in SharePoint Server - SharePoint Server

Note

Manage permission policies for a web application in SharePoint Server

# Manage permission policies for a web application in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Permission policy levels provide a centralized way to configure and manage a set of permissions that applies to a subset of users or groups across all the site collections in a web application.

For example, you might want to create a permission policy level for users who will add, edit, or delete items from a list, open a list, and view items, lists, and pages. However, you might want to prevent the same users from creating or deleting lists. You can do this by creating a permission policy level for those users.

While you can configure these same permissions at the site or site collection level, managing permissions for multiple collections can be time-consuming. Permission policy levels enable you to manage permissions at the web application level.

There are default policy levels of Full Control, Full Read, Deny Write, and Deny All permissions, or you can create a custom policy level and specify the permissions that you need.

The procedures in this article cover how to set up and use permission policy levels and assign users to them. You need to be a member of the Farm Administrators group to follow these procedures.

Create, edit, or delete a custom permission policy level

## Create, edit, or delete a custom permission policy level

Permission policy levels contain permissions that apply to specific users or groups at the web application level. You can specify a combination of List, Site, or Personal permissions. You can also specify one of the following levels of site collection permissions:

**Site Collection Administrator:** Has Full Control permission on the whole site collection and can perform any action on any object.

**Site Collection Auditor:** Has Full Read permission on the whole site collection and associated data, such as permissions and configuration information.

If you specify either or both of those permission levels, you cannot specify individual permissions.

The permissions list contains a **Grant** column and a **Deny** column. You can either grant or deny any permission (or all permissions) as part of a permission policy level. By default, no permissions are granted. If a single permission is neither granted nor denied, the permissions set at the site or site collection level will be in effect.

Add a permission policy level

### Add a permission policy level

Use the following procedure to create a permission policy level.

**To add a permission policy level**

Start SharePoint 2016 Central Administration.

On the SharePoint Central Administration website, in the **Application Management** section, click **Manage web applications**.

Click to highlight the line for the web application whose permission policy level that you want to manage.

In the **Policy** group of the ribbon, click **Permission Policy**.

In the Manage permission policy levels dialog, click **Add Permission Policy Level**.

In the Add permission policy level dialog, in the **Name and Description** section, type the name and description for the policy that you want to create.

In the **Site Collection Permissions** section, select the site collection permissions for this policy.

In the **Permissions** section, select the permissions to grant or deny for this permission level.

Select the **Grant All** check box to include all available permissions in this policy.

Select the **Deny All** check box to deny all available permissions in this policy.

Select either the **Grant** or **Deny** check boxes to include or exclude individual List, Site, and Personal permissions from this policy.

Do not click either **Grant** or **Deny** if you want access to be controlled through regular site or site collection permissions.

- Click **Save.**

Edit a permission policy level

### Edit a permission policy level

Use the following procedure to edit a permission policy level.

**To edit a permission policy level**

Start SharePoint 2016 Central Administration.

On the SharePoint Central Administration website, in the **Application Management** section, click **Manage web applications**.

Click to highlight the web application whose permission policy level that you want to manage.

In the **Policy** group of the ribbon, click **Permission Policy**.

In the Manage permission policy levels dialog, click the link for the permission policy level that you want to edit.

On the Edit permission policy level page, edit the settings, and then click **Save**.

Delete a permission policy level

### Delete a permission policy level

You might want to delete a permission policy level if the users or groups for which you created it are no longer required to use it. It is a good practice to review all existing permission policy levels to ensure that they are still required.

**To delete a permission policy level**

Start SharePoint 2016 Central Administration.

On the SharePoint Central Administration website, in the **Application Management** section, click **Manage web applications**.

Click to highlight the web application whose permission policy level that you want to manage.

In the **Policy** group of the ribbon, click **Permission Policy**.

In the Manage permission policy levels dialog, select the check box of the permission policy level that you want to delete, and then click **Delete Selected Permission Policy Levels**.

Click **OK** to confirm the deletion.

Add users to or remove users from a permission policy level

## Add users to or remove users from a permission policy level

You can add users to a permission policy level, edit the policy level settings, and delete users from a permission policy level. The following settings can be specified or changed:

**Zone:** If a website has multiple zones, you can choose the zone that you want the permission policy level to apply to. The default is all zones, which can be specified for Windows users only.

**Permissions:** You can specify a default policy level of Full Control, Full Read, Deny Write, and Deny All permissions, or you can specify a custom permission level that you created.

**System**: This setting enables SharePoint to display **SHAREPOINT\System** for system-related activity regardless of the Windows user accounts that have been configured for the hosting application pool and the SharePoint farm service account. You might want to specify this setting to prevent unnecessary information disclosure to end-users and potential malicious users who would be interested in knowing more about the SharePoint deployment in the enterprise.

Add users to a permission policy level

### Add users to a permission policy level

Use the following procedure to add users to a permission policy level.

**To add users to a permission policy level**

Start SharePoint 2016 Central Administration.

On the SharePoint Central Administration website, in the **Application Management** section, click **Manage web applications**.

Click to highlight the web application whose permission policy level that you want to manage.

In the Policy group of the ribbon, click **User Policy**.

In the Policy for Web Application dialog, click **Add Users**.

In the Add Users dialog, in the **Zone** list, click the zone to which you want the permission policy level to apply and then click **Next**.

In the Add Users dialog, in the **Choose Users** section, type the user names, group names, or e-mail addresses that you want to add to the permission policy level.

In the **Choose Permissions** section, select the permissions that you want the users to have.

In the **Choose System Settings** section, check **Account operates as System** if you want to specify whether a user account should be displayed as SHAREPOINT\System instead of the actual accounts that perform specific tasks within the SharePoint environment.

Click **Finish**.

Edit a permissions policy

### Edit a permissions policy

Use the following procedure to edit the permissions granted by a permission policy level.

**To edit a user permissions policy**

Start SharePoint 2016 Central Administration.

On the SharePoint Central Administration website, in the **Application Management** section, click **Manage web applications**.

Click to highlight the web application whose permission policy level that you want to edit.

In the **Policy** group of the ribbon, click **User Policy**.

In the Policy for Web Application dialog, select the check box next to the user or group that you want to manage, and then click **Edit Permissions of Selected Users**.

On the Edit Users page, in the **Permission Policy Levels** section, select the permissions that you want the users to have.

In the **Choose System Settings** section, click **Account operates as System** to specify whether a user account should be displayed as SHAREPOINT\System instead of the actual accounts that perform specific tasks within the SharePoint environment.

Click **Save**.

Delete users from a permission policy level

### Delete users from a permission policy level

Use the following procedure to delete a user from a permission policy level.

**To delete users from a permission policy level**

Start SharePoint 2016 Central Administration.

On the SharePoint Central Administration website, in the **Application Management** section, click **Manage web applications**.

Click to highlight the web application whose permission policy level that you want to manage.

In the **Policy** group of the ribbon, click **User Policy**.

In the Policy for Web Application dialog, select the check box next to the user or group that you want to delete, click **Delete Selected Users**, and then click **OK**.

See also

## See also

Concepts

#### Concepts

Administration of SharePoint Server

Manage permissions for a web application in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
