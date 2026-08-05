---
title: "How to add a custom action to the hover panel in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: search-how-to-add-a-custom-action-to-the-hover-panel
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/search/how-to-add-a-custom-action-to-the-hover-panel
family: search
documentKind: "how-to"
abstract: "Learn how to add a custom action to the hover panel in SharePoint Server."
---

# How to add a custom action to the hover panel in SharePoint Server - SharePoint Server

Note

How to add a custom action to the hover panel in SharePoint Server

# How to add a custom action to the hover panel in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

In How to display values from custom managed properties in the hover panel in SharePoint Server, we showed you how to display values from custom managed properties in the hover panel. In this article you'll learn:

What is a hover panel action?

How to add an action to the hover panel

What is a hover panel action?

## What is a hover panel action?

Before we look at how to add a custom action to a hover panel, let's make sure we know what an action is.

At the bottom of the hover panel there are some links that are called *actions*. When we choose one of these, something will occur. For example, in our Search Center scenario, when we choose "SEND"

an email message with a link to the list item will open.

To enable our visitors to do something with the search results, without having to leave the search results page, we can add a custom action.

In our Search Center scenario, we wanted to add a custom action that opens the published article. For example, for the search result "Customize search result types in SharePoint Server", we wanted to add an action that opens this link:<need fwlink? /SharePoint/search/customize-search-result-types>

How to add an action to the hover panel

## How to add an action to the hover panel

In our lists, when an article is published, the URL to the published article is added to the list item. The screen shot below shows how the URL to the article "Customize search result types in SharePoint Server" is maintained in the site column "Content Release URL".

Because this URL is maintained in the list, we can add a custom action to the hover panel that will open the link.

How to display values from custom managed properties in the hover panel in SharePoint Server showed how the hover panel actions are rendered by the *Item_Common_HoverPanel_Actions* display template. So, to add a custom action, you have to edit this file.

But, similar to what we did when we added a custom property to the hover panel, you have to add the managed property that you want to use in your custom action to the item display template.

Confused? Well, this is not easy. It takes a while to understand how things were connected. Let's go through it step-by-step.

Here are the steps to add a custom action to the hover panel:

Find the managed property name of the site column that you want to use. How to display values from custom managed properties in classic search results - option 1 in SharePoint Server showed how to do this.

In your mapped network drive, open an item display template. In the item display template, in the **ManagedPropertyMapping** tag, use the following syntax to add the custom managed property:

```
'<Current item property name>':<Managed property name>'
```

In our Search Center scenario, we added the custom property we wanted to use to the *TechNet content* display template.

Note

You don't have do this step if you are using SharePoint in Microsoft 365.

Go to **Site settings** > **Search Result Types**. A **Property Sync** alert appears.

This alert appears because we have added a new managed property to an item display template (what we did in Step 2). To update the result types with the newly added managed properties, select **Update**.

Important

If you don't do the update, the newly added managed properties won't display in your hover panel.

Open the *Item_Common_HoverPanel_Actions* display template. See how the default actions are created, and use JavaScript and HTML to add your custom action.

In our Search Center scenario, we looked at how the OPEN action (*#= editHmtl =#*) is created. Based on that, we created a new action: *#= viewHtml =#*. The following screen shot shows what we did.

By doing a new search and hovering over a search result, we saw that our new custom action appeared. Nice!

So now that you know how to change the way your classic search results are displayed, there is one more thing we should look at, and that is how you can change the text that appears in the Search Box Web Part.

Next article in this series

### Next article in this series

How to change the text that is displayed in the Search Box Web Part in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
