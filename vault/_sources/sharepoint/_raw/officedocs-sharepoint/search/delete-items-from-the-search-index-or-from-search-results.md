---
title: "Delete items from the search index or from search results in SharePoint Server - SharePoint Server"
description: "Learn how to remove an item from the search index or SharePoint Server search results by removing the URL."
ms.topic: how-to
---
Note

Delete items from the search index or from search results in SharePoint Server

# Delete items from the search index or from search results in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

If you want to remove the metadata of an item from the search index or from the search results, you remove the URL of that item. To remove a URL from the search index, use the **Remove the Item from the Index** option that is available through the crawl log. To remove a URL from search results, use the **Search Result Removal** feature that allows for bulk URL removal. This can provide a more efficient method if many search results should be removed.

Note

If your SharePoint environment is hybrid and uses cloud hybrid search, you index your on-premises content in your search index in Office 365. See Learn about cloud hybrid search for SharePoint for guidance on deleting the metadata of an on-premises item and deleting on-premises search results from the search index in Office 365.

For SharePoint Server 2019, removing the URL of an item affects both the **classic** and **modern** search experiences.

Remove an item from the search index

## Remove an item from the search index

**To remove an item from the search index**

Verify that the user account that is performing this procedure is an administrator for the Search service application.

On the SharePoint Server Central Administration home page, in the **Application Management** section, click **Manage service applications**.

On the Manage Search Applications page, click the Search service application.

On the Search Administration page, in the **Diagnostics** section, click **Crawl Log**.

On the Crawl Log page, click **URL View**.

Do one of the following:

If you know the URL of the item that you want to remove, type the URL in the box.

If you do not know the URL of the item that you want to remove, search for it by using the filters **Content Source**, **Status** or **Message**.

Click **Search**.

Find and point to the URL of the item that you want to remove, click the arrow and then click **Remove the item from the Index**.

In the confirmation dialog that appears, click **OK** to confirm that you want to remove the item from the index.

**Verification:** the text **Removed from the search index by Admin** appears under the URL in the crawl log.

Remove an item from the search results

## Remove an item from the search results

**To remove an item from the search results**

Verify that the user account that is performing this procedure is an administrator for the Search service application.

On the SharePoint Server Central Administration home page, in the **Application Management** section, click **Manage service applications**.

On the Manage Search Applications page, click the Search service application.

On the Search Administration page, in the **Queries and Results** section, click **Search Result Removal**.

On the Exclude URLs From Search Results page, in the **URLs to remove** box, type the URLs of the items that you want to remove from the search results.

Click **Remove Now**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
