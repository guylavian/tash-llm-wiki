---
title: "Manage continuous crawls in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: search-manage-continuous-crawls
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/search/manage-continuous-crawls
family: search
documentKind: "how-to"
abstract: "Learn how to enable and disable continuous crawls in SharePoint Server, and how to change the frequency interval of continuous crawls."
---

# Manage continuous crawls in SharePoint Server - SharePoint Server

Note

Manage continuous crawls in SharePoint Server

# Manage continuous crawls in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Enable continuous crawls** is a crawl schedule option that is an alternative to incremental crawls. This option is new in SharePoint Server and applies only to content sources of type **SharePoint Sites**.

Continuous crawls crawl SharePoint Server sites frequently to help keep search results fresh. Like incremental crawls, a continuous crawl crawls content that was added, changed, or deleted since the last crawl. Unlike an incremental crawl, which starts at a particular time and repeats regularly at specified times after that, a continuous crawl automatically starts at predefined time intervals. The default interval for continuous crawls is every 15 minutes. Continuous crawls help ensure freshness of search results because the search index is kept up to date as the SharePoint Server content is crawled so frequently. Thus, continuous crawls are especially useful for crawling SharePoint Server content that is quickly changing.

A single continuous crawl includes all content sources in a Search service application for which continuous crawls are enabled. Similarly, the continuous crawl interval applies to all content sources in the Search service application for which continuous crawls are enabled.

You cannot run multiple full crawls or multiple incremental crawls for the same content source at the same time. However, multiple continuous crawls can run at the same time. Therefore, even if one continuous crawl is processing a large content update, another continuous crawl can start at the predefined time interval and crawl other updates. Continuous crawls of a particular content repository can also occur while a full or incremental crawl is in progress for the same repository.

A continuous crawl doesn't process or retry items that repeatedly return errors. Such errors are retried during a "clean-up" incremental crawl, which automatically runs every four hours for content sources that have continuous crawl enabled. Items that continue to return errors during the incremental crawl will be retried during future incremental crawls, but will not be picked up by the continuous crawls until the errors are resolved.

You can set incremental crawl times on the  *Search_Service_Application_Name*: Add/Edit Content Source page, but you can change the frequency interval for continuous crawls only by using Microsoft PowerShell.

To enable continuous crawls for an existing content source

## To enable continuous crawls for an existing content source

Verify that the user account that is performing this procedure is an administrator for the Search service application.

In Central Administration, in the **Application Management** section, click **Manage service applications**.

Click the Search service application.

On the  *Search_Service_Application_Name*: Search Administration page, in the Quick Launch, under **Crawling**, click **Content Sources**.

On the  *Search_Service_Application_Name*: Manage Content Sources page, click the SharePoint content source for which you want to enable continuous crawl.

In the **Crawl Schedules** section, select **Enable Continuous Crawls**.

Click **OK**.

**Verification:** On the  *Search_Service_Application_Name*: Manage Content Sources page, verify that the **Status** column has the status **Crawling Continuous**.

To enable continuous crawls for a new content source

## To enable continuous crawls for a new content source

Verify that the user account that is performing this procedure is an administrator for the Search service application.

In Central Administration, in the **Application Management** section, click **Manage service applications**.

Click the Search service application.

On the  *Search_Service_Application_Name*: Search Administration page, in the Quick Launch, under **Crawling**, click **Content Sources**.

On the  *Search_Service_Application_Name*: Manage Content Sources page, click **New Content Source**.

Create a content source of the type **SharePoint Sites**.

In the **Name** section, type a name in the **Name** field.

In the **Content Source Type** section, select **SharePoint Sites**.

In the **Start Addresses** section, type the start address or addresses.

In the **Crawl Settings** section, select the crawling behavior for all start addresses.

In the **Crawl Schedules** section, select **Enable Continuous Crawls**.

Click **OK**.

**Verification:** On the  *Search_Service_Application_Name*: Manage Content Sources page, verify that the newly added content source appears and that the **Status** column has the status **Crawling Continuous**.

To disable continuous crawls for a content source

## To disable continuous crawls for a content source

Verify that the user account that is performing this procedure is an administrator for the Search service application.

In Central Administration, in the **Application Management** section, click **Manage service applications**.

Click the Search service application.

On the  *Search_Service_Application_Name*: Search Administration page, in the Quick Launch, under **Crawling**, click **Content Sources**.

On the  *Search_Service_Application_Name*: Manage Content Sources page, click the SharePoint content source for which you want to disable continuous crawls.

In the **Crawl Schedules** section, clear **Enable Incremental Crawls**. This disables continuous crawls.

To confirm that you want to disable continuous crawls, click **OK**.

Optional: click **Edit schedule** to change the schedule for incremental crawls, and then click **OK**.

On the  *Search_Service_Application_Name*: Edit Content Source page, click **OK**.

**Verification:** On the  *Search_Service_Application_Name*: Manage Content Sources page, verify that the **Status** column has changed to **Idle**. This might take some time, because all URLs that remain in the crawl queue are still crawled after you disable continuous crawls.

To disable continuous crawls for all content sources

## To disable continuous crawls for all content sources

Verify that the user account that performs this procedure is an administrator for the Search service application.

Start a SharePoint Management Shell on a server in the farm.

At the Microsoft PowerShell command prompt, type the following commands:

```
$SSA =  Get-SPEnterpriseSearchServiceApplication
$SPContentSources = $SSA | Get-SPEnterpriseSearchCrawlContentSource | WHERE {$_.Type -eq "SharePoint"} 
foreach ($cs in $SPContentSources) 
{ 
  $cs.EnableContinuousCrawls = $false 
  $cs.Update() 
}
```

**Verification:** On the  *Search_Service_Application_Name*: Manage Content Sources page, verify that the **Status** column has changed to **Idle** for all content sources. This might take some time, because all URLs that remain in the crawl queue are still crawled after you disable continuous crawls.

To change the continuous crawl interval

## To change the continuous crawl interval

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

Start a SharePoint Management Shell.

At the Microsoft PowerShell command prompt, type the following commands:

```
$ssa = Get-SPEnterpriseSearchServiceApplication
$ssa.SetProperty("ContinuousCrawlInterval",n)
```

Where:

- *n* is the regular interval in minutes at which you want to continuous crawls to start. The default interval is every 15 minutes. The shortest interval that you can set is 1 minute.

Note

If you reduce the interval, you increase the load on SharePoint Server and the crawler. Make sure that you plan and scale out for this increased consumption of resources accordingly.

See also

## See also

Plan crawling and federation in SharePoint Server

Set-SPEnterpriseSearchCrawlContentSource

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
