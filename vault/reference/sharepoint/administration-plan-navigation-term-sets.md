---
title: "Plan navigation term sets in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-plan-navigation-term-sets
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/plan-navigation-term-sets
family: administration
documentKind: "article"
abstract: "Learn how to create the navigation term set to provide site navigation for SharePoint Server publishing sites."
---

# Plan navigation term sets in SharePoint Server - SharePoint Server

Note

Plan navigation term sets in SharePoint Server

# Plan navigation term sets in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The managed navigation feature in SharePoint Server and SharePoint in Microsoft 365 enables you to build navigation for a publishing site that is derived from a SharePoint Server managed metadata taxonomy. If your publishing site uses managed navigation, then a navigation term set is associated with the site. You can configure the global navigation control and the current navigation control to use the navigation term set to determine what to display. This article explains the information that you will need to provide for each node in the navigation hierarchy, explains how to record this information in a worksheet, and provides links to other articles that explain how to implement your plan.

Before you read this article you should already know whether or not you will be using cross-site publishing. For more information about cross-site publishing, see Overview of cross-site publishing in SharePoint Server and Plan for cross-site publishing in SharePoint Server. If you will use cross-site publishing, you should also know the structure of the tagging term sets, and you should have an idea of which pages will be used to display which catalog items. You should also know the navigation hierarchy that you want to implement for your site.

Note

The cross-site publishing feature is available only in SharePoint Server 2016 Enterprise.

For more information about managed navigation and term sets, see Overview of managed navigation in SharePoint Server and Plan for managed metadata in SharePoint Server.

Plan a navigation term set

## Plan a navigation term set

Download the Navigation term set planning worksheet and use it to record the decisions you make about terms in the navigation term set for your site. You will use one row for each term in the navigation term set.

Note

You will need one worksheet for each publishing site that uses managed navigation.

On the worksheet, in the **Navigation term** column, enter the navigation hierarchy for your site. In the **Level in hierarchy** column, indicate each term's level in the navigation hierarchy. Sample navigation term set represents the structure of the following navigation term set. An example is shown the table.

Products

Cameras

Digital

Film

Computers

Laptop

Gaming

High-performance

Ultra-light

Slate

Desktop

Printers

Inkjet

Laser

Customer service

About us

Company history

Press releases

- Contact us

**Table: Sample navigation term set**

| **Navigation term** | **Level in hierarchy** |
| --- | --- |
| Products | 1 |
| Cameras | 2 |
| Film | 3 |
| Digital | 3 |
| Computers | 2 |
| Laptop | 3 |
| Gaming | 4 |
| High-performance | 4 |
| Ultra-light | 4 |
| Slate | 3 |
| Desktop | 3 |
| Printers | 2 |
| Inkjet | 3 |
| Laser | 3 |
| Customer service | 1 |
| About us | 1 |
| Company history | 2 |
| Press releases | 2 |
| Contact us | 3 |

If the navigation term comes from a tagging term set, fill in the third and fourth columns. In the **Term and term set pinned from** column, enter the name of the term in the tagging term set and the name of the tagging term set itself. In the **Pin or reuse?** column, enter Pin if the term in the navigation term set is pinned from the tagging term set, or enter Reuse if the term is reused from the tagging term set. Leave both of these columns blank if the navigation term is not associated with a tagging term set.

Next, fill in information about how each node should behave in the navigation controls. For each term, enter the following information:

In the **Navigation node title** column, enter the words to display for this term in the navigation controls. This could be the same as the term, a version of the term with different capitalization, or a completely different word or phrase.

In the **Hover text** column, enter the text to display when the site visitor hovers over the node in a navigation control. Don't make the next level in the navigation hierarchy into hover text. The navigation controls themselves manage displaying the next level of the hierarchy. Instead, provide a more detailed description of this node that will help the user determine whether to navigate to the page.

In the **Show in global navigation menu?** column, enter Yes if this term should appear in the global navigation menu. Enter  No  if the term should not appear in the global navigation menu.

In the **Show in current navigation menu?** column, enter Yes if this term should appear in the current navigation menu when the site visitor navigates to the page corresponding to this term's parent term. Enter No if the term should not appear in the current navigation menu.

In the **Navigation node type** column, enter:

**Header**, if this term should display as a header in navigation controls, but should not link to any page.

**URL**, if the term should link to a specific page. If the navigation term is not associated with a tagging term, the navigation node type is likely to be URL.

**Term-driven**, if you want this term to use a target page and a catalog item page as described earlier in this article. Navigation terms that are associated with tagging terms are likely to use term-driven pages.

In the **URL (for simple link)** column, if the navigation node type is URL, enter the URL that the term should link to. Leave this column blank if the navigation node type is not URL.

Finally, fill in additional information if the term is associated with a term-driven page. Leave these columns blank if the term is not associated with a term-driven page. Enter the following information:

In the **Friendly URL** column, enter the friendly URL to be displayed when a site visitor navigates to the page that is associated with this term. If the parent of this term has a friendly URL, then this term's friendly URL must be the parent term's friendly URL with a suffix in the form "  */something*  " appended.

In the **Term target page** column, enter Inherit from parent if the term should use its parent term's target page, or enter the name of the target page if this term has a different target page.

In the **Child term target page** column, enter the name of that target page if you want terms that are children of this term to use a specific target page. Otherwise, leave this column blank. Child terms can override this value.

In the **Category image** column, enter the name of the image if you want to associate an image with items of this type. Otherwise, leave this column blank.

In the **Catalog item page** column, enter Inherit from parent if the term should use its parent term's catalog item page, or enter the name of the catalog item page if this term has a different catalog item page.

In the **Child catalog item page** column, enter the name of that catalog item page if you want terms that are children of this term to use a specific catalog item page. Otherwise, leave this column blank. Child terms can override this value.

Migrating to managed navigation

## Migrating to managed navigation

SharePoint Server provides a shortcut to help you migrate sites that don't use managed navigation to become sites that do use managed navigation. If your site already has web pages organized into folders, you can associate each folder that contains pages with a term in the navigation term set. When a user views one of the pages, the term's node in the navigation hierarchy will appear as if it had been selected. Use the **Associated Folder** field on the **Navigation** tab in the Term Store Management Tool to associate a folder on the site with a navigation term.

Navigation term set planning worksheet

## Navigation term set planning worksheet

Download an Excel version of the Navigation term set planning worksheet.

See also

## See also

Concepts

#### Concepts

Overview of cross-site publishing in SharePoint Server

Overview of managed navigation in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
