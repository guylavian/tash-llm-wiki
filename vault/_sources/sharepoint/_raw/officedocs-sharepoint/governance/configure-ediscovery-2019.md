---
title: "Configure eDiscovery in SharePoint Server - SharePoint Server"
description: "Learn the steps to set up and configure eDiscovery in SharePoint Server and Exchange Server."
ms.topic: how-to
---
Note

Configure eDiscovery in SharePoint Server

# Configure eDiscovery in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This article identifies the steps that are required to configure eDiscovery in SharePoint Server. When you complete the steps that are listed in this article, users will be able to create and work with eDiscovery cases.

Before you configure eDiscovery, you should understand the concepts that are presented in the article eDiscovery and in-place holds in SharePoint Server.

You must perform the following tasks to configure eDiscovery:

Configure communication between SharePoint Server and Exchange Server 2016.

Configure Search to crawl all discoverable content.

Grant permissions.

Create an eDiscovery Center.

Configure communication between SharePoint Server and Exchange Servers 2019 and 2016

## Configure communication between SharePoint Server and Exchange Servers 2019 and 2016

If you will use a SharePoint eDiscovery Center to discover content in Exchange Server, you must configure SharePoint Server and Exchange Server to interact.

Important

To discover content in Exchange Server from a SharePoint eDiscovery Center, you must be running Exchange Server versions 2019, 2016, or 2013.

Perform the following steps:

Ensure that the Exchange Web Service managed API is installed on every front-end server that is running SharePoint Server.

Configure a trust relationship between SharePoint Server and Exchange Server. For information about the trust relationship, see Plan for server-to-server authentication in SharePoint Server.

If you want content from Skype for Business Server to be discoverable, configure the server to archive to Exchange Server 2016. For information about how to configure Skype for Business Server 2015 archiving, see Configure Skype for Business Server 2015 to use Exchange Server archiving.

If you want SharePoint Server 2019 users to link to and share documents that are stored in OneDrive instead of attaching file to Outlook messages, see the Document collaboration section in **What's new in Exchange Server**.

Perform the eDiscovery configuration steps for Exchange. For information about how to configure Exchange Server 2013 for eDiscovery, see Integration with SharePoint.

Configure Search to crawl all discoverable content

## Configure Search to crawl all discoverable content

Content is only discoverable if it is crawled and indexed by the Search service application that is associated with the web application that the eDiscovery Center is in. You should have identified this Search service application when you planned for eDiscovery. To configure the Search service application to crawl the appropriate content, follow these steps:

If content in Exchange Server 2013 must be discoverable, add Exchange Server 2013 as a result source. For information about how to configure a result source, see Configure result sources for search in SharePoint Server.

Ensure that all websites that contain discoverable content are being crawled. For information about how to configure a location to be crawled, see Add, edit, or delete a content source in SharePoint Server.

Ensure that all file shares that contain discoverable content are being crawled.

Grant permissions

## Grant permissions

We recommend that you create a security group to contain all users of the eDiscovery Center. After you create the security group, grant the security group permissions to access all discoverable content.

If you will grant permissions at the web application level, create a user policy that gives the security group full read permissions for each web application that contains discoverable content. For information about how to create a policy for a web application, see Manage permission policies for a web application in SharePoint Server.

Note

When you change permissions at the web application level, Search re-crawls all of the content in the web application.

If you will grant permissions at the site collection level, make the security group a site collection administrator for each site collection that contains discoverable content. For information about how to add a site collection administrator, see Add, change, or remove a site collection administrator.

Important

A site collection administrator must add the security group as an additional site collection administrator by using the **Site Settings** menu. You cannot use Central Administration to make a security group a site collection administrator

Ensure that the security group has permissions to access all file shares and other websites that contain discoverable content.

If you will use a SharePoint eDiscovery Center to discover content in Exchange Server, grant the security group permissions to access Exchange Server mailboxes. For information about how to grant permissions in Exchange, see Integration with SharePoint.

Grant the security group permissions to view the crawl log. For information about how to grant permissions to access the crawl log, see Set-SPEnterpriseSearchCrawlLogReadPermission.

Create an eDiscovery center

## Create an eDiscovery center

An eDiscovery Center is a site collection from which users can create and manage eDiscovery cases. To create an eDiscovery Center, follow the procedure in the article Create a site collection in SharePoint Server, and choose the **eDiscovery Center** site collection type from the **Enterprise** tab. Be aware that an eDiscovery Center must be in a web application that supports claims authentication.

See also

## See also

Concepts

#### Concepts

eDiscovery and in-place holds in SharePoint Server

Configure eDiscovery in SharePoint Server

Search and place a hold on public folders using In-Place eDicovery

Assign eDiscovery permissions in Exchange Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
