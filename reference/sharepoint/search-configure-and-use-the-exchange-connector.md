---
title: "Configure and use the Exchange connector for SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: search-configure-and-use-the-exchange-connector
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/search/configure-and-use-the-exchange-connector
family: search
documentKind: "how-to"
abstract: "Learn how to create a crawl rule and add a content source to crawl Exchange Server public folders."
---

# Configure and use the Exchange connector for SharePoint Server - SharePoint Server

Note

Configure and use the Exchange connector for SharePoint Server

# Configure and use the Exchange connector for SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Before you begin

## Before you begin

Before you begin this operation, review the following information about prerequisites:

Create a Search service application

Ensure that the crawler has at least Read permission to the Exchange Server public folder.

Create a crawl rule

## Create a crawl rule

This following procedure describes how to create a crawl rule. You must create a crawl rule if the default content access account does not have Read permission to the Exchange Server public folders that you want to crawl.

**To create a crawl rule**

Verify that the user account that is performing this procedure is an administrator for the Search service application.

In Central Administration, in the Application Management section, click **Manage Service Applications**.

On the Manage Service Applications page, in the list of service applications, click the Search service application.

On the Search Administration page, in the Crawling section, click **Crawl Rules**.

On the Manage Crawl Rules page, click **New Crawl Rule**.

On the Add Crawl Rule page, in the **Path** section, in the **Path** box, type the path to which the crawl rule will apply. You can use standard wildcard characters in the path.

Note

When creating a crawl rule, the URL that you type inside the **Path** box should be in the following form:  _<protocol>://hostname/*_where  *<protocol>* is the protocol that you want to use (typically http or https), and  *hostname* is the NetBIOS or fully qualified domain name of the server that is running Exchange Server.

In the **Crawl Configuration** section, select **Include all items in this path**.

In the **Specify Authentication** section, select the type of crawl authentication to use. This section is available only if **Include all items in this path** is selected.

Click **OK**.

Add a content source for Exchange Server public folders

## Add a content source for Exchange Server public folders

Use one of the following procedures to create a content source for Exchange Server public folders. Which procedure you should follow depends on the Exchange Server version. You can choose to add a content source to crawl public folders in:

Exchange Server 2007 and Exchange Server 2007 with Service Pack 1 (SP1)

Exchange Server 2007 with Service Pack 2 (SP2) and Exchange 2010

To add a content source for Exchange Server 2007 and Exchange Server 2007 SP1 public folders

### To add a content source for Exchange Server 2007 and Exchange Server 2007 SP1 public folders

Verify that the user account that is performing this procedure is an administrator for the Search service application.

On the SharePoint Central Administration home page, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, click the Search service application.

On the Search Administration page, in the **Crawling** section, click **Content Sources**.

On the Manage Content Sources page, click **New Content Source**.

On the Add Content Source page, in the **Name** box, type a name for the new content source.

In the **Content Source Type** section, select **Exchange Public Folders**.

In the **Start Addresses** section, in the **Type start addresses below (one per line)** box, type the URLs for the Exchange Server public folders that you want to crawl. These URLs are typically in one of the following forms:

*<protocol>*:// *host name*/public

- Where  *<protocol>* can be http or https, and  *host name* is the NetBIOS or fully qualified domain name (FQDN) of the server that is running Exchange Server.

*<protocol>*:// *host name*/public/ *subfolder*

- Where  *<protocol>* can be http or https,  *host name* is the NetBIOS or FQDN of the server that is running Exchange Server, and  *subfolder* is the name of the specific subfolder that you want to crawl.

For example, if you want to crawl all subfolders in the public folder on a server that is named exch-01 and that is in the Contoso domain, and that server does not use SSL, you could type either `https://exch-01/public` or `https://exch-01.contoso.com`. To crawl only a specific subfolder named Bob in the same public folder, type `https://exch-01/public/bob` or `https://exch-01.contoso.com/bob`.

Note

For performance reasons, you cannot add the same start addresses to multiple content sources.

In the **Crawl Settings** section, select the crawling behavior that you want.

In the **Crawl Schedules** section, you can choose to specify when to start full and incremental crawls:

To create a full crawl schedule, click the **Create Schedule** link below the **Full Crawl** list.

To create an incremental crawl schedule, click the **Create schedule** link below the **Incremental Crawl** list.

- Click **OK**.

To add content sources for Exchange Server 2007 SP2 and Exchange 2010 public folders

### To add content sources for Exchange Server 2007 SP2 and Exchange 2010 public folders

Verify that the user account that is performing this procedure is an administrator for the Search service application.

Open a web browser and go to the Outlook Web Access webpage for the Exchange Server that contains the public folders that you want to crawl.

Log on to Outlook Web Access using any user account that has Read permissions on the public folders that you want to crawl.

Go to the public folder that you want to crawl, right-click the folder, and then select **Open in New Window**.

When the new window opens, go to the address bar and copy the complete URL. This is the Outlook Web Access public folder address.

On the SharePoint Central Administration home page, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, click the Search service application.

On the Search Administration page, in the **Crawling** section, click **Content Sources**.

Click **New Content Source**.

On the Add Content Source page, in the **Name** box, type a name for the new content source.

In the **Content Source Type** section, select **Exchange Public Folders**.

In the **Start Addresses** section, paste the Outlook Web Access public folder address that you copied in step 5.

In the **Crawl Settings** section, select the crawling behavior that you want.

In the **Crawl Schedules** section, you can choose to specify when to start full and incremental crawls:

To create a full crawl schedule, click the **Create Schedule** link below the **Full Crawl** list.

To create an incremental crawl schedule, click the **Create schedule** link below the **Incremental Crawl** list.

- Click **OK**.

Additional resources

## Additional resources

- Last updated on 
		2023-04-27
