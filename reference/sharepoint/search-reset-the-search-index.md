---
title: "Reset the search index in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: search-reset-the-search-index
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/search/reset-the-search-index
family: search
documentKind: "how-to"
abstract: "Learn how to reset the SharePoint Server search index."
---

# Reset the search index in SharePoint Server - SharePoint Server

Note

Reset the search index in SharePoint Server

# Reset the search index in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

When you reset the search index in SharePoint Server, all content is immediately removed from the search index and users will not be able to retrieve search results. After you reset the search index, you must perform a full crawl of one or more content sources to create a new search index. Users will be able to retrieve search results again when the full crawl is finished and the new search index is created.

Note

After a search index reset, a full crawl won't restore all analytics features that are powered by the Analytics Processing Component. Examples of analytics features are raising or demoting items in search results based on which search results users have clicked, or displaying the number of times a search result has been viewed. For more information, see Overview of analytics processing in SharePoint Server.

If you can, you should perform a backup and restore of your Search service application instead of a search index reset. These procedures will fully restore all features that are powered by the Analytics Processing Component. For more information, see Back up Search service applications in SharePoint Server and Restore Search service applications in SharePoint Server.

Note

If your SharePoint environment is hybrid and uses cloud hybrid search, you index your on-premises content in your search index in Office 365. See Learn about cloud hybrid search for SharePoint for guidance on deleting metadata of on-premises items from the search index in Office 365.

Before you begin

## Before you begin

Make sure that you are not running a backup of the Search service application.

Reset the search index

## Reset the search index

Use the following procedure to reset the search index.

**To reset the search index**

Verify that the user account that is performing this procedure is an administrator for the Search service application for which you want to reset the search index.

On the SharePoint Central Administration home page, in the **Application Management** section, click **Manage service applications**.

On the Manage Search Applications page, click the Search service application for which you want to reset the search index.

On the Search Administration page, under System Status, verify that the **Administrative status** of the Search service application is **Running** and not **Paused**.

On the Search Administration page, in the **Crawling** section, click **Index Reset**.

On the Index Reset page, verify that the **Deactivate search alerts during reset** check box is checked, and then click **Reset Now**.

In the confirmation dialog that appears, click **OK** to confirm that you want to reset the index.

The Search Administration page opens and the System Status is displayed.

After the search index reset is complete, you must perform a full crawl of all the content sources that you want to include in the search index. For more information, see Add, edit, or delete a content source in SharePoint 2013 Preview. Users will not be able to retrieve search results until you create a new search index. After the full crawl has completed and a new search index has been created, you must also re-enable search alerts. See Enable search alerts.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
