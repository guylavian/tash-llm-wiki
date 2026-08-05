---
title: "Manage the lock status for site collections in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: sites-manage-the-lock-status-for-site-collections
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/sites/manage-the-lock-status-for-site-collections
family: sites
documentKind: "how-to"
abstract: "How to manage lock status for a site collection in SharePoint Server."
---

# Manage the lock status for site collections in SharePoint Server - SharePoint Server

Note

Manage the lock status for site collections in SharePoint Server

# Manage the lock status for site collections in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You use the lock status of a site collection to control the actions allowed on a site collection.

The following table describes the locking options that are available in SharePoint Server.

| **Option** | **Description** |
| --- | --- |
| **Not locked** | Unlocks the site collection and makes it available to users. |
| **Adding content prevented** | Prevents users from adding new content to the site collection. Updates and deletions are still allowed. |
| **Read-only** (blocks additions, updates, and deletions) | Prevents users from adding, updating, or deleting content. When a user attempts to add, update, or delete content, the user receives an error message that informs the user that access is denied and that the user does not have permission to perform the action or access the resource. A read-only lock can be either site collection administrator controlled if the site collection is archived or farm administrator controlled |
| **No access** | Prevents users from accessing the site collection and its content. Users who attempt to access the site receive an error page that informs the user that the website declined to show the webpage. |

Note

If you want to limit the amount of content that can be stored in a site collection, you can apply a quota template to the site collection. When the content storage limit that is specified in the quota template is reached, the site collection is locked automatically until the storage limit quota has been increased or some content has been removed. For more information, see Create, edit, and delete quota templates in SharePoint Server.

Important

The steps in this article apply to SharePoint Server 2016, SharePoint Foundation 2013, and SharePoint Server 2013.

Learn about Locking and unlocking sites for SharePoint in Microsoft 365.

Manage the lock status for a site collection by using Central Administration

## Manage the lock status for a site collection by using Central Administration

Use this procedure to lock or unlock a site collection by using the SharePoint Central Administration website.

**To manage the lock status for a site collection by using Central Administration**

Verify that you have the following administrative credentials.

- You must be a member of the Site Collection Administrators group for the site collection.

Open Central Administration. On the **Application Management** page, in the **Site Collections** section, click **Configure quotas and locks**.

If the site collection you want is not already selected, in the **Site Collection** section, on the **Site Collection** menu, click **Change Site Collection**. Use the **Select Site Collection** page to select a site collection.

On the **Site Collection Quotas and Locks** page, in the **Site Lock Information** section, select one of the following options:

**Not locked** to unlock the site collection and make it available to users.

**Adding content prevented** to prevent users from adding new content to the site collection. Updates and deletions are still allowed.

**Read-only (blocks additions, updates, and deletions)** to prevent users from adding, updating, or deleting content. Choose whether you want this to be farm administrator controlled or site collection administrator controlled.

**No access** to prevent users from accessing the site collection and its content. Users who attempt to access the site receive an error message.

If you select **Adding content prevented**, **Read-only (blocks additions, updates, and deletions)**, or **No access**, type a reason for the lock in the **Additional lock information** box.

Click **OK** when you are done.

Manage the lock status for a site collection by using Microsoft PowerShell

## Manage the lock status for a site collection by using Microsoft PowerShell

Use this procedure to lock or unlock a site collection by using PowerShell.

**To manage the lock status for a site collection by using PowerShell**

Verify that you meet the following minimum requirements: See Add-SPShellAdmin.

Open the SharePoint Management Shell.

At the PowerShell command prompt, type the following command, and then press **ENTER**:

```
Set-SPSite -Identity "<SiteCollection>" -LockState "<State>"
```

Where:

*<SiteCollection>* is the URL of the site collection that you want to lock or unlock.

*<State>* is one of the following values:

**Unlock** to unlock the site collection and make it available to users.

**NoAdditions** to prevent users from adding new content to the site collection. Updates and deletions are still allowed.

**ReadOnly** to prevent users from adding, updating, or deleting content.

**NoAccess** to prevent users from accessing the site collection and its content. Users who attempt to access the site receive an error message.

For more information, see Set-SPSite.

See also

## See also

Concepts

#### Concepts

Create, edit, and delete quota templates in SharePoint Server

Other Resources

#### Other Resources

SharePoint planning guide

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
