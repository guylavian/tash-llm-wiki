---
title: "Show results from Microsoft 365 in on-premises SharePoint with cloud hybrid search - SharePoint Server"
type: reference
domain: sharepoint
slug: hybrid-show-results-from-office-365-in-on-premises-sharepoint-with-cloud-hybrid-search
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/hybrid/show-results-from-office-365-in-on-premises-sharepoint-with-cloud-hybrid-search
family: hybrid
documentKind: "how-to"
abstract: "Learn how to show results from the Microsoft 365 search index when searching from SharePoint Server sites with cloud hybrid search."
---

# Show results from Microsoft 365 in on-premises SharePoint with cloud hybrid search - SharePoint Server

Note

Show results from Microsoft 365 in on-premises SharePoint with cloud hybrid search

# Show results from Microsoft 365 in on-premises SharePoint with cloud hybrid search

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Learn how to show results from the Microsoft 365 search index when searching from SharePoint Server sites with cloud hybrid search.

After you've set up cloud hybrid search, your users get search results from both on-premises and Microsoft 365 content when they use the search center in Office 365. However, your existing search in document libraries in SharePoint Server, such as Team Sites, stops returning results when you've set up cloud hybrid search. If your users need to search from Team Sites, you can set up search from SharePoint Server Team Sites to show results from the search index in Office 365. You use the cloud Search service application to achieve this. Note that searching from a Search Center in Office 365 will be faster than searching from a document library in SharePoint Server because the search index and the search center are in the same environment.

Here's an overview of the cloud hybrid search solution. The light grey lines represent what you're setting up by following the steps in this article.

Follow these steps:

Verify that cloud hybrid search works.

In the cloud search farm, create a result source that defines how to get search results from the search index in Office 365.

In the cloud search farm, set that result source as the default result source for the cloud Search service application.

If your existing on-premises document libraries are in SharePoint Server 2010 and/or SharePoint Server 2013, set up query federation by publishing the cloud Search service application (cloud SSA) so that SharePoint Server 2010 and/or SharePoint Server 2013 can consume the cloud SSA.

Create a result source that defines how to get search results from the search index in Office 365

## Create a result source that defines how to get search results from the search index in Office 365

Verify that the user account that you use to perform this procedure is an administrator for the cloud SSA.

In the cloud search farm, in Central Administration, in the **Application Management** section, select **Manage service applications**.

Select the cloud SSA to which you want to add a result source.

On the Search Administration page for the cloud SSA, in the Quick Launch, select **Result Sources**.

On the **Manage Result Sources** page, select **New Result Source**.

On the **Add Result Source** page, do the following:

In the **General Information** section, in the **Name text** box, type a name for the new result source—for example,  *Microsoft 365 search index*.

(Optional) In the **General Information** section, in the **Description** text box, enter a description of the new result source.

This description will appear as a tooltip when the pointer rests on the result source on certain configuration pages.

In the **Protocol** section, select **Remote SharePoint**.

In the **Remote Service URL** section, enter the address of the root site collection in SharePoint in Microsoft 365 that you want to get search results from, such as `https://adventure-works.sharepoint.com`.

In the **Type** section, select **SharePoint Search Results**.

In the **Query Transform** section, keep the default setting.

In the **Credentials Information** section, select **Default Authentication.**

To save the new result source, select **OK**.

Set the result source as the default result source for the cloud Search service application

## Set the result source as the default result source for the cloud Search service application

Verify that the user account that performs this procedure is an administrator for the cloud SSA.

In the cloud search farm, in Central Administration, in the **Application Management** section, select **Manage service applications**.

Select the cloud SSA for which you want to set the result source as default.

On the **Search Administration** page, in the **Queries and Results** section, select **Result Sources**.

On the **Manage Result Sources** page, point to the result source that you want to set as default, select the arrow that appears, and then select **Set as Default**.

Set up query federation

## Set up query federation

To set up query federation you have to publish the cloud SSA so that it can be consumed by SharePoint Server 2010 or SharePoint Server 2013. For an overview of this approach, see Share service applications across farms in SharePoint Server and select the SharePoint Server version of the article for your consuming environment.

In each of the following steps, when you refer to the SharePoint Server documentation, use the appropriate names and parameters for your cloud search farm and your cloud SSA.

Publish and share the cloud SSA, see Publish service applications in SharePoint Server.

Consume the cloud SSA.

Consuming a published SSA requires exchanging trust certificates between the consuming and the publishing SharePoint on-premises farm. See Exchange trust certificates between farms in SharePoint Server, and select the relevant SharePoint Server version of the article for your consuming environment.

Grant permission to connect to the cloud SSA.

Grant permission to the consuming SharePoint Server 2010 or SharePoint Server 2013 farm to be able to connect the published cloud SSA. See Set permissions to published service applications in SharePoint 2013.

Connect to the cloud SSA.

Once the trust and permissions have been set between the farms, you can configure SharePoint Server 2010 or SharePoint Server 2013 to connect to the cloud SSA on your cloud search farm. See Connect to service applications on remote farms in SharePoint 2013.

Configure web applications to associate with the cloud SSA.

In SharePoint Server 2010 or SharePoint Server 2013, configure the web applications to associate with the new cloud SSA connection. See Add or remove service application connections from a web application in SharePoint 2013.

Related Topics

## Related Topics

Learn about cloud hybrid search for SharePoint in Microsoft 365

Plan cloud hybrid search for SharePoint in Microsoft 365

Configure cloud hybrid search for SharePoint in Microsoft 365

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
