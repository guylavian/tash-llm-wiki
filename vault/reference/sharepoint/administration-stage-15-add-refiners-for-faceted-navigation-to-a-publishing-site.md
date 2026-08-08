---
title: "Stage 15 Add refiners for faceted navigation to a publishing site in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-stage-15-add-refiners-for-faceted-navigation-to-a-publishing-site
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/stage-15-add-refiners-for-faceted-navigation-to-a-publishing-site
family: administration
documentKind: "how-to"
abstract: "Learn how to add refiners for faceted navigation to a publishing site in SharePoint Server 2016."
---

# Stage 15 Add refiners for faceted navigation to a publishing site in SharePoint Server - SharePoint Server

Note

Stage 15: Add refiners for faceted navigation to a publishing site in SharePoint Server

# Stage 15: Add refiners for faceted navigation to a publishing site in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Note

Many of the features described in this series are also available for most sites in SharePoint in Microsoft 365.

Quick overview

## Quick overview

Previous stages of this series identified and configured the refiners we want to use for faceted navigation.

In this article, you'll learn:

How to add a Refinement Web Part to a page

How to configure a Refinement Web Part to use refiners for faceted navigation

How to change a refiner display name

How to add counts to refiner values

Start stage 15

## Start stage 15

How to add a Refinement Web Part to a page

### How to add a Refinement Web Part to a page

Browse to the page where you want to add the Refinement Web Part (RWP). In our scenario, let's browse to  *Cameras*  .

Select the **Settings** menu, and then select **Edit Page**.

In the Web Part Zone where you want to add the Web Part, select **Add a Web Part**.

In the **Categories** list, select **Search**.

In the **Parts** list, select **Refinement**, and then select **Add**.

In our scenario, we'll add a RWP to Zone 2.

When you add the RWP to a page, it will display several default properties such as "Author" and "Modified date." We don't want to use these refiners. We want to use the refiners we configured in Stage 14: Configure refiners for faceted navigation in SharePoint Server. Therefore, we'll have to configure the Web Part accordingly.

How to configure a Refinement Web Part to use refiners for faceted navigation

### How to configure a Refinement Web Part to use refiners for faceted navigation

In the Web Part, select the **Web Part Menu**, and then select **Edit Web Part**.

In the Web Part tool pane, in the **Refiners** section, select **Use the refinement configuration defined in the Managed navigation term set**.

Select **OK** and save the page.

And just like that, we've added refiners to our page. Nice, don't you think?

To verify that our refiners actually work, select **Green** and **Orange** from the color refiner, and then click **APPLY**. In an instant, only green and orange cameras display on the page.

So, we've verified that our refiners work. But, we're not completely there with user-friendliness. As things stand, the refiners are displayed as **REFINABLEINT01**, **REFINABLESTRING01**, **REFINABLESTRING03**. and so on Remember, these are the names of the refiner-enabled managed properties we used in in Stage 14: Configure refiners for faceted navigation in SharePoint Server when we configured the refiners. To visitors, these names make no sense at all. Therefore, we must fix them by changing their refiner display names.

How to change a refiner display name

### How to change a refiner display name

To change a refiner display name, you have to change a JavaScript file in the master page gallery. Because we mapped our network drive in Stage 6: Upload and apply a new master page to a publishing site in SharePoint Server, this is a simple process.

In your mapped network drive, go to **Display Templates** > **Language Files**.

Go to the folder that corresponds to the language of your site, which in our scenario is **en-us**.

Open the **CustomStrings.js** file.

For each refiner-enabled managed property that you want to change the display name of, use the following syntax:

`"rf_RefinementTitle_ManagedPropertyName": "Sample Refinement Title for ManagedPropertyName",`

For example, in our Contoso scenario, the refiner-enabled managed property *RefinableInt01* contains a *Price* refiner. To give this refiner a nice display name, we'll add the following line to the java script file:

`"rf_RefinementTitle_RefinableInt01": "Price",`

In our Contoso scenario, for the refiners we have configured for the "Audio" and "Cameras" category, our CustomString.js file will be like this:

Save this file, and refresh the *Cameras* page to verify that our refiners now have nice, user-friendly display names.

If we browse to the Digital cameras category, we can see that the category-specific refiner **MEGA PIXELS** appears.

So, our category-specific refiners now display for the correct category, and they all have user-friendly names. But, there is another small detail that would make our refiners even better. Right now we can't see any numeric details for the refiner values. For example, we can't see how many cameras are of the color *Silver*, or how many cameras have *14* mega-pixels. To see this info, we have to add **counts** to the refiner values.

How to add counts to refiner values

### How to add counts to refiner values

In your mapped network drive, go to **Display Templates --> Filters**.

Open the HTML file **Filter_Default**.

Change the value for **ShowCounts** to **true**.

Save the file, and refresh the *Cameras* page to verify that refiner counts are displayed. You'll see that refiner counts only display for refiners where it's only possible to select one refiner at a time.

To add refiner counts to refiners where it's possible to select multiple refiner values, open the HTML file **Filer_MultiValue**, and repeat Steps 3 and 4.

Now when we refresh the Cameras page, all of the refiner values have counts.

So, when visitors come to our Contoso site, they can use category-specific refiners to find the product they're looking for easily. But there's still one more thing missing: when visitors are on a top level category page, for example *Cameras*, they can't easily see which subcategories are under *Cameras*. Luckily, there is a Web Part that will fix this for us. We'll explore this in detail in the last article of this series.

Next article in this series

#### Next article in this series

Stage 16: Add a Taxonomy Refinement Panel Web Part to a publishing site in SharePoint Server

See also

## See also

Concepts

#### Concepts

Configure Search Web Parts in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
