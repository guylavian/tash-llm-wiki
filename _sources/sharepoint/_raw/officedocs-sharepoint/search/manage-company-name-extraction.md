---
title: "Manage company name extraction in SharePoint Server - SharePoint Server"
description: "Learn how to include company names to be extracted from content for classic search results, or how to exclude company names from being extracted."
ms.topic: how-to
---
Note

Manage company name extraction in SharePoint Server

# Manage company name extraction in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The search system can extract company names from content. The following conditions must be met before company names can be extracted:

The managed property setting **Company name extraction** must be enabled on the managed property that you want to extract company names from. Typically, this is a managed property that you expect to contain these entities, such as the managed properties **Title** or **Body**. Company names are extracted from the full contents of the managed property they are associated with, even if sections in those contents are tagged as **<no index>**.

The name of the company that you want to extract should either already exist in the prepopulated company name dictionary or it should be included in the **Company Inclusions** list.

A full crawl must be completed.

For example, if a company name is found in the body of a document, **company name extraction** is enabled on the managed property **Body** and a full crawl has been run, the company name is extracted and mapped to the managed property **companies**. You can then use the **companies** managed property to create refiners based on the extracted company name in the Refinement Web Part on the search results page.

There is a prepopulated dictionary for company name extraction which includes a large number of company names. You can add additional company names to be extracted or prevent particular company names from being extracted using the Company Inclusions or Company Exclusions lists.

This article explains how to maintain these lists. It does not cover how to enable a managed property to use company extraction. For more information on how to enable company extraction on a managed property, see Manage the search schema in SharePoint Server.

Open the Term Store Management Tool

## Open the Term Store Management Tool

The company name exclusion and inclusion lists are managed in the Term Store. Use the Term Store Management Tool to edit the lists.

**To get to the Term Store Management Tool**

Verify that the user account that is performing this procedure is an administrator for the Search service application.

On the home page of the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, click the Search service application.

On the Search Administration Page, in the **Queries and Results** section, click **Search Dictionaries**. The Term Store Management Tool opens.

Exclude company names

## Exclude company names

To exclude company names from being extracted as entities from content, add the company name to the Company Exclusions list.

**To add a company name to the Company Exclusions list**

On the Site Settings: Term Store Management Tool page, click the arrow to expand the **Search Dictionaries** menu.

Click Company Exclusions, click the arrow and then click **Create Term**.

Type the name of the company that you want to exclude in the box that appears.

Click anywhere on the page to add the term to the Company Exclusions list.

Include company names

## Include company names

To include company names to be extracted as entities from content, add the company name to the Company Inclusions list.

**To add a company name to the Company Inclusions list**

On the Site Settings: Term Store Management Tool page, click the arrow to expand the **Search Dictionaries** menu.

Click Company Inclusions, click the arrow and then click **Create Term**.

Type the name of the company that you want to include in the box that appears.

Click anywhere on the page to add the term to the Company Inclusions list.

Edit terms

## Edit terms

You can edit the names of terms in the Company Exclusions and Company Inclusions lists.

**To edit terms**

On the Site Settings: Term Store Management Tool page, click the arrow to expand the **Search Dictionaries** menu.

Depending on which list the term is in, click either **Company Exclusions** or **Company Inclusions**.

Double-click the term that you want to edit.

Type the new name for the term.

Click anywhere on the page to save the edited term.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
