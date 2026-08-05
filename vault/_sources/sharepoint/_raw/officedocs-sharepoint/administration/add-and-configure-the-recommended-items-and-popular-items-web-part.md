---
title: "Add and configure the Recommended Items and Popular Items Web Part in SharePoint Server - SharePoint Server"
description: "Learn how to add and configure the Recommended Items and Popular Items Web Part in SharePoint Server."
ms.topic: how-to
---
Note

Add and configure the Recommended Items and Popular Items Web Part in SharePoint Server

# Add and configure the Recommended Items and Popular Items Web Part in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The previous article in this series, Change the Content Search Web Part display template and use Windows PowerShell to start Usage analytics in SharePoint Server, explained how to change the CSWP to log the  *Views*  usage event, and how you can use Microsoft PowerShell to start Usage analytics.

Note

The examples in this series are based on an on-premises SharePoint Server deployment.

Add a Recommended Items Web Part to a page

## Add a Recommended Items Web Part to a page

Navigate to the page where you want to add the Recommended Items Web Part (RIWP). In our Contoso scenario, we want to add the RIWP to our catalog item page. Here's how you do that:

Select the **Settings** menu --> **Edit page**.

In the Web Part Zone where you want to add the Web Part, select **Add a Web Part**.

In the **Categories** list, select **Search-Driven Content**.

In the **Parts** list, select **Recommended Items**, and then **Add**.

In our Contoso scenario, we'll show the RIWP below the CSWP.

About the recommendedfor managed property

## About the recommendedfor managed property

In a previous blog article, we told you about the *UsageAnalyticsId* managed property that is used by Usage analytics to specify how recommendations between individual items should be calculated (see About the UsageAnalyticsID managed property). The result of this calculation is sent to the *recommendedfor* managed property. The RIWP uses the *recommendedfor* managed property to query for recommendations. You don't have to know about this managed property when you configure the RIWP. To understand how the query in the RIWP works, it's important that you keep the *recommendedfor* managed property in mind.

Configure the Recommended Items Web Part

## Configure the Recommended Items Web Part

When you configure the RIWP, you should configure it on an item details page where recommendations are generated. Remember the previous article in this series, when we invited some coworkers to a "Why you should simulate the generation of Views usage events." At the click party, your coworkers click specific items so recommendations are generated. In our Contoso scenario, add the RIWP to an item details page where you know recommendations are generated through the clicking of your coworkers.

Here are the steps to configure the RIWP:

Select the **Settings** menu --> **Edit page**.

In the RIWP, select the **Web Part Menu** --> **Edit Web Part**.

In the Web Part tool pane, select **Change query**. This option opens a dialog.

In the **Build Your Query** dialog, select the following:

In the **Get recommended items for** section, select **A token from the URL** and then select from which URL value that you want to get recommendations. In our Contoso scenario, we want to get recommendations from **{URL.Token.2} (number)**.

In the **Restrict by app** section, select **Specify a URL**, and then enter the URL of your catalog.

You might be thinking "OK, that was easy, but what does it actually mean?" Understanding this process can be a bit difficult. Let's take a closer look.

**A token from the URL** means that we want to obtain recommendations for a value that is used in the URL.

**{URL.Token.2}** is a query variable that represents the second value in the URL as counted from right to left. For example, in the URL  `https://www.contoso.com/computers/desktops/5637145799/5637146352`, the query variable **{URLToken.2}** represents the value *5637145799*. Remember when we connected our publishing site to the catalog (see Stage 5: Connect your publishing site to a catalog in SharePoint Server), we specified that the value of *Group Number* should be used as the second to last value in the URL of our catalog item page. That means the query variable **{URL.Token.2}** represents the value of *Group Number*. Also, we mapped Change the mapping of the UsageAnalyticsID managed property so the Usage analytics calculation would be based on *Group Number*.

**Specify a URL** means that we want to specify from which site we get recommendations, in this case our Authoring site.

But from these settings, it's not clear as to which managed property is used in the query. So, to view more information about the query, select **TEST**. The query that's issued by the Web Part is shown in the **Query text** section.

If we break the query down, we get the following components:

**recommendedfor** is the managed property that is used in the query.

The colon : means "contains".

**5637145799** is the value of the query variable {URL.Token.2}, which is a *Group Number* value.

**path:"http://ib-perf-8/sites/catalog"** is the URL to our Authoring site.

**(IsDocument:"True" OR contentclass:"STS_ListItem")** narrows the search result down to only documents or list items.

If we put all this information together, we can understand that the query means the following:

From the *URL of the Authoring site*, search for *document or list items* where the value of the managed property *recommendedfor* contains the value that is currently used as the second value in the URL, counting from right to left.

Now we know what the query means. But we're not done with the configuration. In the **SEARCH RESULT PREVIEW** section, we can see that all items in a product group are displayed, for example, all *SV Keyboard E10* (notice that they all have the same value for Group Number in the URL).

All items in the product group are shown because the Usage analytics calculation is performed on the group level. Remember, in Change the Content Search Web Part display template and use Windows PowerShell to start Usage analytics in SharePoint Server, we mapped *UsageAnalyticsId* to *ows_ProductCatalogGroupNumber*. But we only want to display one item per product group, which can be done by grouping search results.

To group search results, do the following steps:

Select **REFINERS --> Show more**.

From the **Group by** menu, select **Show all properties**.

We want to show only one item per product group. Therefore, we select  *ProductCatalogGroupNumberOWSTEXT*  (the managed property of  *Group Number*). We only want to display one item per group. So we leave the value in **Show there results** as **1**.

In the **SEARCH RESULT PREVIEW**, we can now see that only one item per product group is shown.

Select **OK** to save the changes.

In the Web Part tool pane, in the **Number of items** to show field, enter how many items that you want to display in the Web Part.

Select **OK**, and save the page.

Even though it doesn't look good, good recommendations are now displayed on our catalog item page.

About the display template that is used by the Recommended Items Web Part

## About the display template that is used by the Recommended Items Web Part

Just as you do with the Content Search Web Part (CSWP), you use display templates to control how content should be displayed in a RIWP. Stage 11: Upload and apply display templates to the Content Search Web Part in SharePoint Server explains how to upload and apply display templates to the Content Search Web Part. You can do the same for the RIWP. The display template that is used by the RIWP contains important code that logs the two usage events: *Recommendation Displayed* and *Recommendation Clicked*.

In An introduction to recommendations and popular items in SharePoint Server, we told you about the three default usage events in SharePoint Server. The usage events *Recommendation Displayed* and *Recommendation Clicked* are used to record statistics of how visitors have interacted with the content on your website. When an item is displayed as a recommendation, a *Recommendation Displayed* usage event is recorded. When an item is clicked on when it is displayed as a recommendation, a *Recommendation Clicked* usage event is recorded. We'll show you how you can view these statistics in a later article.

In Change the Content Search Web Part display template and use Windows PowerShell to start Usage analytics in SharePoint Server, we changed the CSWP display template to log the *Views* usage event. The logging of the *Recommendation Displayed* and *Recommendation Clicked* usage events are performed in the RIWP. The default display template that is used by the RIWP is *Item_RecommendationsClickLogging*. This display template contains the two functions *LogRecsViewToEventStore* and *LogRecsClickToEventStore*. These two functions log the *Recommendation Displayed* and *Recommendation Clicked* usage events.

When you change your RIWP display template, you should copy the *Item_RecommendationsClickLogging* file, change the copied version, and apply it to your RIWP. That way, you don't have to worry about how to add code in the same manner that we did for the CSWP.

After applying the changed display template to the RIWP, the recommended items are displayed nicely.

Add a Popular Items Web Part to a page

## Add a Popular Items Web Part to a page

You can display the most popular, that is, *the most viewed* items within your catalog by adding a Popular Items Web Part (PIWP) to your category page. It's important to understand that when you add a PIWP to your catalog page, the PIWP will automatically show the most viewed items *within each category*. For example, if a visitor is viewing the *Cameras* category, the PIWP will show the most viewed items within the *Cameras* category. If a visitor is viewing the *Camcorders* category, the PIWP will show the most viewed items within the *Camcorders* category.

To add a PIWP, navigate to the page where you want to add the PIWP. In our Contoso scenario, we'll add a PIWP to our category page. Do the following steps:

Select the **Settings** menu --> **Edit page**.

In the Web Part Zone where you want to add the Web Part, select **Add a Web Part**.

In the **Categories** list, select **Search-Driven Content**.

In the **Parts** list, select **Popular Items**, and then **Add**.

In our Contoso scenario, we'll show the PIWP above the CSWP.

Configure the Popular Items Web Part

## Configure the Popular Items Web Part

Select the **Settings** menu --> **Edit page**.

In the PIWP, select the **Web Part Menu** --> **Edit Web Part**.

In the Web Part tool pane, select **Change query**. This option opens a dialog.

In the **Restrict by app** section, select **Specify a URL** and enter the URL of your Authoring site.

In the **Restrict by** tag section, select **Restrict by current and child navigation terms**.

No results are displayed in the **SEARCH RESULT PREVIEW** section. What's going on?

To see more about the query that the PIWP issues, select **TEST**. On the **TEST** tab, we can see the **Query text**.

The query text means the following:

**path:"http://ib-perf-8/sites/catalog"** is the URL to our Authoring site.

**owstaxIdMetadataAllTagsInfo** is the managed property that is used in the query.

The colon : means "contains".

`91eb9f0d-3e5a-41a8-8487-78dfe234ca7c` is the GUID of the current category. In this example, the current category is *Cameras*.

**(IsDocument:"True" OR contentclass:"STS_ListItem")** narrows the search result down to only documents or list items.

If we put this information together, the query provides us with the following understandings:

From the *URL of the Authoring site*, search for *document or list items* where the value of the managed property *owstaxIdMetadataAllTagsInfo* contains the GUID of the current navigation category or any of the children of the current navigation.

An important piece of information that we can see in the query text is that the PIWP uses the *owstaxIdMetadataAllTagsInfo* managed property in its query. You can't change the query in the PIWP to use another managed property. That means that for the query in the PIWP to work correctly, the *owstaxIdMetadataAllTagsInfo* managed property has to include the value of the managed property that we use to drive managed navigation (for more information, see Stage 8: Assign a category page and a catalog item page to a term in SharePoint Server. In our Contoso scenario, the managed property that drives managed navigation is *owstaxIdProductCatalogItemCategory*. What we have to do is to map the crawled property of *owstaxIdProductCatalogItemCategory* to the *owstaxIdMetadataAllTagsInfo* managed property.

Change the Content Search Web Part display template and use Windows PowerShell to start Usage analytics in SharePoint Server explains how to map a crawled property to a managed property.

Important

You have to do the mapping on the authoring site.

In our Contoso scenario, the correctly mapped *owstaxIdMetadataAllTagsInfo* property looks as follows:

After you've changed the mapping of the property, you must start a full crawl, as explained in Stage 4: Set up search and enable the crawling of your catalog content in SharePoint Server.

There is one important thing that you can't see in the query text, and that is how the search results are sorted. The PIWP sorts search results in a descending order on the *ViewsRecent* managed property. By default, the *ViewsRecent* managed property contains the number of views for an item within the last 14 days. Later in this series, we'll explain how to change this time range, for example, to the past 7 days. This default behavior of the property means that the query issued by the PIWP will do the following tasks:

From the *URL of the authoring site*, search for *document or list items* where the value of the managed property *owstaxIdMetadataAllTagsInfo* contains the GUID of the current navigation category, or any of the children of the current navigation. Sort the search results in *descending order of views for the past 14 days*.

When the full crawl has finished, you'll see search result in the Web Part.

Select **OK** to save the changes, and save the page.

To display the popular items nicely, you can apply a display template in the same manner that you did with the CSWP. For more information, see Stage 11: Upload and apply display templates to the Content Search Web Part in SharePoint Server.

To check that the PIWP is working correctly, go to the *Cameras* section. On this page, the most viewed items within the *Cameras* category are displayed.

When we go to the *Camcorders* category, the most viewed items within the *Camcorders* category are displayed.

Our PIWP is working the way it should. Nice!

So now you know how to configure the RIWP and the PIWP. When you perform these tasks, you should be logged in to your own account.

In the next article of this series, we'll explain how all these configurations work if the website only has anonymous users, that is, users who are not logged in.

Next article in this series

### Next article in this series

Use recommendations and popular items on websites with anonymous users in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-04-27
