---
title: "Start profile synchronization manually in SharePoint Server - SharePoint Server"
description: "Learn how to start profile synchronization manually in SharePoint Server."
ms.topic: how-to
---
Note

Start profile synchronization manually in SharePoint Server

# Start profile synchronization manually in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This article describes how to start profile synchronization for SharePoint Server manually. You can start a full synchronization or an incremental synchronization of profile information. You might want to consider starting profile synchronization manually if you have made considerable changes to user profiles, and you don't want to wait for the next scheduled synchronization.

Note that this procedure is only for SharePoint Server farms that are using SharePoint Active Directory Import. If you are using an external identity manager, see the documentation for your identity manager.

You can also configure profile synchronization to run automatically according to a schedule.

Start profile synchronization manually

## Start profile synchronization manually

You can manually start a full synchronization or an incremental synchronization of profile information. You need to be a farm administrator or an administrator of the User Profile service application to perform this procedure.

Usually, an incremental synchronization is fine, but you should use a full synchronization if any of the following are true.

A mapped property has changed. For example, you mapped a new property, or added or changed a mapping associated with a property.

You changed the containers that a connection uses to synchronize with AD DS.

You added or deleted a synchronization connection.

Keep in mind that a full synchronization can take a long time, depending on the size of your directory.

**To start profile synchronization manually**

On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.

On the **Manage Service Applications** page, click the link for the User Profile service application.

On the **Manage Profile Service** page, in the **Synchronization** section, click **Start Profile Synchronization**.

On the **Start Profile Synchronization** page, select **Start Incremental Synchronization** to synchronize only profiles that have changed since the last synchronization, or select **Start Full Synchronization** to synchronize all profiles.

Click **OK**.

Note

Refresh the **Manage Profile Service** page to view the profile synchronization status.

See also

## See also

Concepts

#### Concepts

Overview of profile synchronization in SharePoint Server 2013

Synchronize user and group profiles in SharePoint Server 2013

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
