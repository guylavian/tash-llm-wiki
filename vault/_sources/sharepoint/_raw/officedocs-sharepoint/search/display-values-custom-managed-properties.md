---
title: "How to display values from custom managed properties in classic search results - option 1 in SharePoint Server - SharePoint Server"
description: "Learn one option for displaying values from custom managed properties in SharePoint Server."
ms.topic: how-to
---
Note

How to display values from custom managed properties in classic search results - option 1 in SharePoint Server

# How to display values from custom managed properties in classic search results - option 1 in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

In this article, you'll learn:

How to display a custom icon

How to find a managed property name

How to change an item display template to show values from custom managed properties - option 1

About click tracking and automatically improved relevancy

How to display a custom icon

## How to display a custom icon

In Understanding how search results are displayed in SharePoint Server we explained how the icons Word, PDF, and Excel are displayed for classic search results. In our Search Center scenario, we wanted to add the following custom icon next to all search results that belong to the newly created *TechNet content* result type:

TN

To display a custom icon for classic search results, here's what you should do:

Add the custom icon to a SharePoint Server library.

In our Search Center scenario, we added the custom icon to the **Images** library.

Open the item display template that is referenced from the result type for which you want to display a custom icon.

In our Search Center scenario, we also removed the if statement: *if (ctx.CurrentItem.IsContainer)*.

On a search page, enter a query that will trigger the new result type.

In our Search Center scenario, we entered "result type." Search results that are TechNet publications now have a custom icon next to them. Great!

So users of our Search Center could now easily distinguish the search results that were published on TechNet. But, we also wanted to add information from custom site columns so that users could see important information about each search result without having to click it.

In Understanding how search results are displayed in SharePoint Server we explained that site columns are "transformed" into managed properties during crawl. We also explained that only managed properties that are listed in an item display template can be displayed in search results. So, to display custom information in your search results, you must have to add managed properties to an item display template. Hence, the next thing that you should do is find the managed property name that corresponds to the custom site column that you want to use.

How to find a managed property name

## How to find a managed property name

Before you start to search for a managed property name, it's important that you know a bit about the naming convention for managed properties. For more information about this, see About the naming convention for automatically created crawled and managed properties.

Depending on your permission level, you can search for managed properties from three places:

| **Permission level** | **Search from this location** |
| --- | --- |
| Search service application administrator | Central Administration --> Managed Service Application --> Search Service Application --> Search Schema |
| Site collection administrator | Site Settings --> Search Schema (in the Site Collection Administration section) |
| Site collection owner | Site Settings --> Schema (in the Search section) |

Here's what you should do:

Go to **Site settings** > **Search Schema**.

On the **Managed Properties** page, in the **Managed property** field, enter the name of the site column that you want to find the managed property name of. Remember that managed property names don't contain spaces. Therefore, if your site column name contains a space, leave it out.

In our Search Center scenario, we wanted to find the managed property name for the site column *Content Summary*. We entered *ContentSummary* in the **Managed property** field, and selected the green arrow icon.

One search result was returned: *ContentSummaryOWSMTXT*.

Because the **Content Summary** site column is of type *Multiple lines of text*, we knew this was the managed property name we wanted to use.

Repeat the steps of this procedure to find the names of all of the managed properties that you want to display in your search results.

Now that you have found the names of the managed properties that you want to show in your search results, the next step is to change the item display template.

How to change an item display template to show values from custom managed properties - option 1

## How to change an item display template to show values from custom managed properties - option 1

In Understanding how search results are displayed in SharePoint Server we mentioned that there are several ways to change an item display template to show values from custom managed properties. The option explained in this section is very simple. We'll cover the second option in the next article of this series. It doesn't include any if statements, and hit highlighting is not applied.

Here's what you should do:

Open the item display template that belongs to the result type for which you want to customize search results.

In our Search Center scenario, this was *TechNet content*.

In the item display template, in the **ManagedPropertyMapping** tag, use the following syntax to add the custom managed properties that you want to display:

```
'<Current item property name>':<Managed property name>'
```

In our Search Center scenario, we wanted the values from the managed properties *ContentSummaryOWSMTXT* and *owstaxIdTechnicalSubject* to appear in the search result. To make the file easier to maintain, we named the current item properties the same as the managed properties.

- Inside the second <div> tag in the <body>, use the following syntax to add code that will display the value of the custom managed property:

```
_#= ctx.CurrentItem.<Current item property name> =#
```

In our Search Center scenario, we added the following to the item display template:

```
<div>_#= ctx.CurrentItem. ContentSummaryOWSMTXT =#_</div>
<div>_#= ctx.CurrentItem. owstaxIdTechnicalSubject =#></div>
```

Save the item display template.

Note

You don't have to do this step if you are using SharePoint in Microsoft 365. Go to **Site settings** > **Search Result Types**. A **Property Sync** alert appears.

This alert is displayed because we added managed properties to an item display template (what we did in step 2). To update the result types with the newly added managed properties, select **Update**.

Important

If you don't do this update, the newly added managed properties won't display in your search results.

After we made this change, when users entered a query in our Search Center, both the value of *ContentSummaryOWSMTXT* and the value for *owstaxIdTechnicalSubject* appeared in the search results.

Even though two custom properties appeared in the search results, the result wasn't completely right. For example, we wanted to display the two custom properties between the title and the link, and not below the link as was currently the case.

To better understand why the search results were displayed the way that they were, let's take a closer look at the customized item display template:

`ctx.CurrentItem.csr_Icon` points to the location of my custom icon. This variable is used by the *Item_CommonItem_Body* display template.

`_#=ctx.RenderBody(ctx)=#_` calls the *Item_CommonItem_Body* display template. (Remember Understanding how item display templates and hit highlighting work in SharePoint Server. The *Item_CommonItem_Body* display template displays the custom icon, title, and the link to the item.)

`_#= ctx.CurrentItem.ContentSummaryOWSMTXT =#_` and `_#= ctx.CurrentItem.owstaxIdTechnicalSubject =#_` display the values of the two managed properties,  *ContentSummaryOWSMTXT* and *owstaxIdTechnicalSubject*.

To display the custom properties between the title and the link, you could take the  *Item_CommonItem_Body*  display template out of play by deleting the reference  `_#=ctx.RenderBody(ctx)=#_` from your custom display template. You could then add the properties in the order that you want them to display, for example as follows:

The search result would then look like this:

By working a bit more on the styling, you could have a good enough result. But, by deleting the reference to  `_#=ctx.RenderBody(ctx)=#_` ,the *Item_CommonItem_Body* display template is no longer used to display results. The *Item_CommonItem_Body* display template contains some functionality that will automatically improve the relevancy of your classic search results. So, before you delete the  `_#=ctx.RenderBody(ctx)=#_` reference, you should consider whether automatically improved relevancy is something that the users of your search site would benefit from.

About click tracking and automatically improved relevancy

## About click tracking and automatically improved relevancy

The *Item_CommonItem_Body* display template contains an *onlick* method that tracks the click behavior of users. This tracking influences the relevancy of classic search results. For example, a search result that is often clicked by users will automatically be displayed higher up in the search results.

Important

If you want your classic search results to receive automatically improved relevancy based on the click behavior of users, do not delete the reference to `_#=ctx.RenderBody(ctx)=#_` from the item display template.

In the next article, we'll explain how you can keep this reference, display custom properties between the title and link in the classic search results, and also apply hit highlighting to your custom properties.

Next article in this series

### Next article in this series

How to display values from custom managed properties in search results - option 2 in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
