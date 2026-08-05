---
title: "Configure properties of the Search Navigation Web Part in SharePoint Server - SharePoint Server"
description: "Learn how to configure properties of the Search Navigation Web Part, and how to add a link to a new search vertical page."
ms.topic: how-to
---
Note

Configure properties of the Search Navigation Web Part in SharePoint Server

# Configure properties of the Search Navigation Web Part in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The Search Navigation Web Part is configured to display links to the search verticals **Everything**, **People**, **Conversations** and **Videos**. It uses search results from the Search Results Web Part so that when users click a search vertical link, the search results are filtered and displayed following the configuration of the search vertical. You can also create your own search vertical and add it to be displayed in the Search Navigation Web Part.

By changing properties on the Search Navigation Web Part you can do the following:

Specify a different Web Part from which search results are received.

Change the number of search vertical links to display.

The search vertical properties, such as display name and links, are configured on the Search Settings page for the corresponding site.

Before you begin

## Before you begin

Note

Because SharePoint Server runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server supports the accessibility features of supported browsers.

For more information, see the following resources:

Plan browser support

Accessibility for SharePoint 2013

Accessibility features in SharePoint 2013 Products

Keyboard shortcuts

Touch

Configure the properties of the Search Navigation Web Part

## Configure the properties of the Search Navigation Web Part

**To configure the properties of a Search Navigation Web Part**

Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the Enterprise Search Center site.

On the search results page, click the **Settings** menu, and then click **Edit Page**.

In the Search Navigation Web Part, click the **Search Navigation Web Part** menu arrow, and then click **Edit Web Part**.

In the Web Part tool pane, in the **Control** section, do the following:

To receive search results from another Web Part on the page, in the **Use Current Query from** list, select a Web Part.

To change the number of search vertical links to display before overflowing, in the **Maximum Links Before Overflow** box, type a number.

Change the properties of a search vertical in the Search Navigation Web Part

## Change the properties of a search vertical in the Search Navigation Web Part

**To change the properties of a search vertical in the Search Navigation Web Part**

Verify that the user account that performs this procedure is a member of the Owners group on the Enterprise Search Center site.

On the **Settings** menu for the site, click **Site Settings**.

On the **Site Settings** page, in the **Search** section, click **Search Settings**.

On the **Search Settings** page, in the **Configure Search Navigation** section, click to select the search vertical for which you want to change the properties, and then click **Edit**.

In the **Navigation Link** dialog, do the following:

To change the display name of a search vertical, in the **Title** field, type a display name.

To change the URL of the search vertical, in the **URL** field, type a URL.

Note

You can't use a page that uses a friendly URL for your search vertical.

- On the **Search Settings** page, click **OK** to save the changes.

Add a search vertical to the Search Navigation Web Part

## Add a search vertical to the Search Navigation Web Part

Before you start this procedure, verify that you have created a new page for the search vertical. We recommend that you copy one of the existing search vertical pages — for example, **results.aspx**, and then modify the copy to create a new page.

**To add a search vertical to the Search Navigation Web Part**

Verify that the user account that performs this procedure is a member of the Owners group on the Enterprise Search Center site.

On the **Settings** menu for the site, click **Site Settings**.

On the **Site Settings** page, in the **Search** section, click **Search Settings**.

On the **Search Settings** page, in the **Configure Search Navigation** section, click **Add Link**.

In the **Navigation Link** dialog, do the following:

In the **Title** field, type a display name.

In the **URL** field, type the URL to the new search vertical.

Click **OK** to save the new search vertical.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
