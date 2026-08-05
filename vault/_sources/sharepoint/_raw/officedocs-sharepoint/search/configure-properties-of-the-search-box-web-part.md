---
title: "Configure properties of the Search Box Web Part in SharePoint Server - SharePoint Server"
description: "Learn how to configure properties of the Search Box Web Part."
ms.topic: how-to
---
Note

Configure properties of the Search Box Web Part in SharePoint Server

# Configure properties of the Search Box Web Part in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

By default, the Search Box Web Part is used on the home page for the Search Center (default.aspx), and all search results pages (results.aspx, peopleresults.aspx, conversationresults.aspx, videoresults.aspx). By changing properties in the Search Box Web Part you can do the following:

Change the Web Part or page where the search results should be displayed—for example, a custom Search Results Web Part or a custom search results page.

Turn off query suggestions and people suggestions. For more information about query suggestions, see Manage query suggestions in SharePoint Server.

Display links to a search preference page and an advanced search page.

Change the display template that is applied to the Web Part.

Before you begin

## Before you begin

Note

Because SharePoint Server runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server supports the accessibility features of supported browsers. For more information, see the following resources:

- Plan browser support

- Accessibility for SharePoint 2013

- Accessibility features in SharePoint 2013 Products

- Keyboard shortcuts

- Touch

Configure properties of the Search Box Web Part

## Configure properties of the Search Box Web Part

**To configure the properties of a Search Box Web Part**

Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the Enterprise Search Center site.

On the Search Center site home page, click the **Settings** menu, and then click **Edit Page**.

In the Web Part, click the **Search Box Web Part Menu** arrow, and then click **Edit Web Part**.

In the Web Part tool pane, in the **Properties for Search Box** section, expand the **Which search results page should queries be sent to** section, and then do the following:

To display the settings that are defined on the Search Settings page, select the **Use this site's Search Settings** check box.

To override the settings that are defined on the Search Settings page, clear the **Use this site's Search Settings** check box, and then do the following:

To display search results in a Web Part on the page, in the section **Send queries to other Web Parts on this page**, select a Web Part.

Note

If there are no other Web Parts on a page, search results will be sent to the search results page as specified on the Search Settings page.

To send queries to a custom search results page, select **Send queries to a custom results page URL**, and then type the URL of the custom search results page.

Note

You can't send queries to a custom search results page that uses a friendly URL.

- In the Web Part tool pane, in the **Properties for Search Box** section, expand the **Query Suggestions** section, and then do the following:

To disable query suggestions, clear the **Show suggestions** check box.

To specify additional properties for query suggestions, change the values in the following fields:

**Number of query suggestions:** How many query suggestions to display.

**Minimum number of characters:** How many characters the user must type before query suggestions are displayed.

**Suggestions delay (in milliseconds):** How many milliseconds elapse before query suggestions are displayed.

**Number of personal favorites:** How many query suggestions are displayed to the user under the text **Are you looking for these again?** in the search results. These suggestions are based on search results that the user has clicked previously. To disable personal favorite results, clear the **Show personal favorite results** check box.

To turn on people name suggestions, select **Show people name suggestions**.

- In the Web Part tool pane, in the **Properties for Search Box** section, expand the **Settings** section, and then do the following:

To show a link to a search preference page, select **Show preferences link**.

To show a link to an advanced search page, select **Show advanced link**, and then in the **Advanced search page URL** box, type the URL of the advanced search page that you want to link to.

To apply another display template, in the **Search box control Display Template** list, select the display template that you want to apply to the Web Part.

Select the **Make the search box have focus when the page is loaded** check box to make it possible for users to immediately type a query in the search box when the page is loaded without first having to click the search box. By default, this is selected.

See also

## See also

How to change the text that is displayed in the Search Box Web Part in SharePoint Server 2013

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
