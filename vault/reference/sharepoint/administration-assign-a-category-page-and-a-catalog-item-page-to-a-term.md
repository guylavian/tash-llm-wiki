---
title: "Assign a category page and a catalog item page to a term in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-assign-a-category-page-and-a-catalog-item-page-to-a-term
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/assign-a-category-page-and-a-catalog-item-page-to-a-term
family: administration
documentKind: "how-to"
abstract: "Learn how to assign a category page and a catalog item page to a term in term store management."
---

# Assign a category page and a catalog item page to a term in SharePoint Server - SharePoint Server

Note

Assign a category page and a catalog item page to a term in SharePoint Server

# Assign a category page and a catalog item page to a term in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Category pages and catalog item pages are page layouts that you can use to show structured content consistently across a site. They are often used when displaying catalog content on a site that uses managed navigation. This saves you from having to create many individual pages for content that you want to show in the same manner across your site. You can assign a category page or a catalog item page to all terms in a term set, or to specific terms in a term set. For more information, see "Catalog pages and catalog item pages" in Overview of cross-site publishing in SharePoint Server.

Before you begin

## Before you begin

Note

Because SharePoint Server runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server supports the accessibility features of supported browsers. For more information, see the following resources: > Plan browser support> Accessibility guidelines in SharePoint> Accessibility in SharePoint> Keyboard shortcuts> Touch.

Before you assign a category page and a catalog item page in term store management, verify the following:

The publishing site is using managed navigation. By default, site collections that are created by using the Publishing Portal Site Collection template use managed navigation.

You have created a navigation term set in term store management as described in Create and manage terms in a term set.

You have created a category page and a catalog item page.

Important

If you have connected a publishing site to a catalog and selected to integrate the catalog into the publishing site as described in Connect a publishing site to a catalog in SharePoint Server, the category page and catalog item page configurations that you specified are displayed in term store management.

Assign a category page and a catalog item page to a term

## Assign a category page and a catalog item page to a term

By default, when you assign a category page to a term, the page that you specify will also be assigned to the children of the term unless you specify a different page to be used on all the children of a term.

Note

You should only assign catalog item pages to a term if the term set is used as a tagging term set for catalog content.

**To assign a category page and a catalog item page to a term**

Verify that the user account that performs this procedure is a member of the Owners SharePoint group on the site.

On the site, on the **Settings** menu, click **Site Settings**.

On the **Site Settings** page, in the **Site Administration** section, click **Term store management**.

On the **Term Store Management Tool** page, in the **TAXONOMY TERM STORE** section, click the term to which you want to assign a category page and a catalog item page.

Click the tab **TERM-DRIVEN PAGES**.

To assign a category page to a term, in the **Target Page Settings** section, select the check box **Change target page for this term**, and then type the URL of the category page that you want to assign to the term. Or you can click the **Browse** button, and then go to the category page that you want to assign to the term.

To assign a category page to the children of a term, select the check box **Change target page for the children of this term**, and then type the URL of the category page that you want to assign to the children of the term. Or, you can click the **Browse** button, and then go to the category page that you want to assign to the children of the term.

To assign a catalog item page for catalog items that are tagged with the current term, select **Change Catalog Item Page for this category**, and then type the URL of the catalog item page that you want to assign to catalog items that are tagged with the term. Or you can click the **Browse** button, and then go to the catalog item page that you want to assign to catalog items that are tagged with the term.

To assign a catalog item page for catalog items that are tagged with a child of the current term, select **Change Catalog Item Page**, and then type the URL of the catalog item page that you want to assign to catalog items that are tagged with children of the term. Or you can click the **Browse** button, and then go to the catalog item page that you want to assign to catalog items tagged with children of the term.

See also

## See also

Other Resources

#### Other Resources

Blog post: Assign a category page and a catalog item page to a term

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
