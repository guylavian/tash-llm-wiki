---
title: "Stage 7 Upload page layouts and create new pages in a publishing site in SharePoint Server - SharePoint Server"
description: "Learn how to upload page layouts and create new pages in a publishing site in SharePoint Server 2016."
ms.topic: how-to
---
Note

Stage 7: Upload page layouts and create new pages in a publishing site in SharePoint Server

# Stage 7: Upload page layouts and create new pages in a publishing site in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Note

Many of the features described in this series are also available for most sites in SharePoint in Microsoft 365.

Quick overview

## Quick overview

Stage 6: Upload and apply a new master page to a publishing site in SharePoint Server explained how to upload and apply a new master page. The next step in giving our site a "Contoso look" is to create new pages.

In this stage, you'll learn:

About page layouts

About pages and rendered pages

How to upload a new page layout

How to turn off versioning for the Pages Library

How to create a page based on a page layout

Note

This article doesn't cover how to create a page layout. It explains how to upload already completed page layouts. These files won't be made available for download.

Start stage 7

## Start stage 7

About page layouts

### About page layouts

A **page layout** is a template for a page in your site. This is where you define the layout and structure for the body of a page.

Page layouts contain page field controls and Web Part zones. Page field controls and Web Part zones are placeholders that define where content can be added by authors. They are added to a page layout at a specific position, for example on the left side of a column, and with specific style elements, such as bold.

Stage 6: Upload and apply a new master page to a publishing site in SharePoint Server explained how SharePoint Server 2016 automatically converts an HTML master page into an ASP.NET page. The same rule applies to page layouts. You can create a page layout in HTML format and SharePoint Server 2016 will automatically convert it to an ASP.NET page for you. This means that you can design your page layout using your favorite HTML editor, and focus on HTML, CSS, and JavaScript. You don't have to worry about ASP.NET or SharePoint specific markup.

For more information, see:

Overview of the SharePoint 2013 page model

How to: Create a page layout in SharePoint 2013

About pages and rendered pages

### About pages and rendered pages

It is important to understand that authors do not add content to a page layout. Content is added to a **page**.

A page is created based on a specific page layout. Once you've created a page, authors can add content that they want to display on their website to the page. Because the page is based on a page layout with page field controls and Web Part zones, authors can't add content outside these areas.

When visitors browse a site, they will see a rendered page. In a rendered page, the master page is merged with the page layout, and the content for the page is displayed in the page fields and Web Part zones.

For more information, see Overview of the SharePoint 2013 page model.

How to upload a new page layout

### How to upload a new page layout

In our Contoso scenario, we have two page layouts: one for the category page, and one for the catalog item page.

Stage 6: Upload and apply a new master page to a publishing site in SharePoint Server explained how to map a network drive. Because we have mapped our network drive, uploading these page layouts becomes very easy. Simply drag-and-drop the files into your **Master Page Gallery**.

In SharePoint, refresh the **Master Page Gallery** page to see that the two page layouts are added. Also notice that an associated ASP.NET file was created for the page layouts.

How to turn off versioning for the Pages Library

### How to turn off versioning for the Pages Library

In our scenario, we are not using SharePoint workflows for approval. The files have already been approved. Therefore, before we create a new page, we want to turn off versioning for the **Pages** library.

To turn off versioning for the **Pages** library:

From the **Site Settings** menu, select **Site contents**.

On the **Site Contents** page, select **Pages**.

In the **Pages** library, on the **LIBRARY** tab, select **Library Settings**.

On the **Settings** page, select **Versioning settings**.

In the **Require Check Out section**, for **Require documents to be checked out before they can be edited**, select **No**.

We are now ready to create our two new pages.

How to create a page based on a page layout

### How to create a page based on a page layout

To create a new page:

On the **Site Contents** page, select **Pages**.

In the **Pages** library, select the **FILES** tab, and then select **New Document**.

On the **Create Page** page, enter a **Title** and a **URL name**. From the **Page Layout** list, select the page layout that you want to apply to the new page. In our scenario, the page layout is the newly uploaded page layout called *ContosoElectronicsCategoryPageLayout*.

After you select **OK**, the newly created page is shown in the **Pages** library.

In our Contoso scenario, we'll also need a catalog item page. To create this page, repeat Steps 3 and 4 from the previous procedure. However for **Page Layout**, select *ContosoElectroniceCatalogItemPageLayout*.

Our **Pages** library now contains two new pages: *ContosoCategoryPage* and *ContosoCatalogItemPage*.

Now that we have created these pages, the next step is to assign them to the terms that drive our site navigation.

Next article in this series

#### Next article in this series

Stage 8: Assign a category page and a catalog item page to a term in SharePoint Server

See also

## See also

Other Resources

#### Other Resources

How to: Create a page layout in SharePoint Server 2013

Add snippets to a master page or a page layout in SharePoint Server 2013

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
