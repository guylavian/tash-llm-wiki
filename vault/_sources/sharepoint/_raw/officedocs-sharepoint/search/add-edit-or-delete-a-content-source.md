---
title: "Add, edit, or delete a content source in SharePoint Server - SharePoint Server"
description: "Learn how to create a content source to specify what type of content to crawl, schedules for crawling, start addresses, and crawl priority."
ms.topic: article
---
Note

Add, edit, or delete a content source in SharePoint Server

# Add, edit, or delete a content source in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

A content source is a set of options that you use to specify what, when, and how to crawl.

When a Search service application is created, a content source named "Local SharePoint sites" is automatically created and configured for crawling all SharePoint Server sites in the local server farm. You can create additional content sources to specify other content to crawl and how the system should crawl that content. After you create a content source, you can edit or delete it at any time.

Caution

Changing a content source requires a full crawl for that content source.

Before you begin

## Before you begin

Before you begin this operation, see the following article for information about prerequisites regarding the creation of content sources:

- Create a Search service application

Create, edit, or delete a content source

## Create, edit, or delete a content source

**To get to the Manage Content Sources page**

Verify that the user account that is performing this procedure is an administrator for the Search service application.

On SharePoint Server Central Administration home page, navigate to **Application Management > Manage service applications > Search service application**.

On the **Search Administration** page, under **Crawling**, select **Content Sources**.

**To create a content source**

On the **Manage Content Sources** page, select **New Content Source**.

On the **Add Content Source** page, under **Name**, type a name for the new content source in the **Name** box.

Under **Content Source Type**, select the type of content that you want to crawl.

Under **Start Addresses**, type the URLs from which the crawler should begin crawling in the **Type start addresses below (one per line)** box.

Under **Crawl Settings**, select the crawling behavior that you want.

Under **Crawl Schedules**, to specify a schedule for full crawls, select a defined schedule from the **Full Crawl** list. A full crawl involves crawling all content that is specified by the content source, regardless of whether the content has changed. To define a full crawl schedule, select **Create schedule**.

To specify a schedule for incremental crawls, select a defined schedule from the **Incremental Crawl** list. An incremental crawl involves crawling content that is specified by the content source that has changed since the last crawl. To define a schedule, select **Create schedule**. You can change a defined schedule by selecting **Edit schedule**.

Note

For a content source that is of type SharePoint Server sites, you can enable continuous crawls. For more information, see Manage continuous crawls in SharePoint Server.

To set the priority of this content source, under **Content Source Priority**, select **Normal** or **High** from the **Priority** list.

Select **OK**.

**To edit a content source**

You can edit a content source to change the schedule on which the content is crawled, the crawl start addresses, the content source priority, or the name of the crawl. Crawl settings and content source type cannot be changed when you edit a content source.

On the **Manage Content Sources** page, in the list of content sources, point to the name of the content source that you want to edit, click the arrow that appears, and then select **Edit**.

After you make the changes that you want, select **OK**.

**To delete a content source**

On the **Manage Content Sources** page, in the list of content sources, point to the name of the content source that you want to delete, click the arrow that appears, and then select **Delete**.

Select **OK** to confirm that you want to delete this content source.

Starting with the SharePoint Server Subscription Edition Version 23H2 feature update, you have the ability to configure the HTTP protocol version that applications would use to search your content sources.

Note

By default, the search service application search crawler uses the HTTP 1.1 protocol version. The search crawler will use the HTTP 1.0 protocol version when configured so.

You can configure an HTTP protocol version to be applicable to specific content sources. These HTTP protocol versions can be configured only by using the following cmdlets:

- New-SPEnterpriseSearchCrawlContentSource

- Set-SPEnterpriseSearchCrawlContentSource

When you use these PowerShell cmdlets, you can specify the `HttpProtocol` parameter with the following options:

- **Default**: This option refers to the system default one, currently HTTP 1.1.

- **Http_1_0**: This option refers to the HTTP 1.0 protocol.

- **Http_1_1**: This option refers to the HTTP 1.1 protocol.

Additional resources

## Additional resources

- Last updated on 
		2023-09-12
