---
title: "Manage query spelling correction in SharePoint Server - SharePoint Server"
description: "Learn how to include single words in or exclude single words from query spelling corrections to help correct spelling errors in queries."
ms.topic: how-to
---
Note

Manage query spelling correction in SharePoint Server

# Manage query spelling correction in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

In the classic search experience, if a user enters a word in a search query that appears to be misspelled, the search results page displays query spelling corrections. This is also known as "Did you mean?". For example, if someone enters a query that contains the word "ampitheater", the query spelling correction would be "amphitheater".

These query spelling suggestions are based on the closest matches in the default spelling dictionaries and the Query Spelling Inclusions list. For terms that you enter in the Query Spelling Exclusions list, query spelling suggestions will never be displayed. You can edit the Query Spelling Inclusions and the Query Spelling Exclusions list, but you can't edit the default spelling dictionaries. It takes up to 10 minutes for any changes to the Query Spelling Exclusions or the Query Spelling Inclusions list to take effect.

Important

You can only include or exclude single words.

For more information about linguistic search features for different languages see Linguistic search features in SharePoint Server.

Open the Term Store Management Tool

## Open the Term Store Management Tool

The query spelling exclusions and inclusions lists are managed in the Term Store. Use the Term Store Management Tool to edit the lists.

**To get to the Term Store Management Tool**

Verify that the user account that is performing this procedure is an administrator for the Search service application.

On the home page of the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, click the Search service application.

On the Search Administration Page, in the **Queries and Results** section, click **Search Dictionaries**. The Term Store Management Tool opens.

Exclude terms from query spelling corrections

## Exclude terms from query spelling corrections

To exclude words from query spelling corrections, add terms to the Query Spelling Exclusions list.

Important

Create a separate term for each query spelling correction exclusion. Do not create subterms for terms in the Query Spelling Exclusions list. Term hierarchies will be ignored in this context.

**To add a word to the Query Spelling Exclusions list**

On the Site Settings: Term Store Management Tool page, click the arrow to expand the **Search Dictionaries** menu.

Click Query Spelling Exclusions, click the arrow and then click **Create Term**.

Type the word that you want to exclude in the box that appears.

Click anywhere on the page to add the term to the Query Spelling Exclusions list.

Include terms in query spelling corrections

## Include terms in query spelling corrections

To include words in query spelling corrections, add terms to the Query Spelling Inclusions list.

Important

Create a separate term for each query spelling correction inclusion. Do not create subterms for terms in the Query Spelling Inclusions list. Term hierarchies will be ignored in this context.

**To add a word to the Query Spelling Inclusions list**

On the Site Settings: Term Store Management Tool page, click the arrow to expand the **Search Dictionaries** menu.

Click Query Spelling Inclusions, click the arrow and then click **Create Term**.

Type the word that you want to include in the box that appears.

Click anywhere on the page to add the term to the Query Spelling Inclusions list.

Edit terms

## Edit terms

You can edit the names of terms in the Query Spelling Exclusions and Query Spelling Inclusions lists.

**To edit terms**

On the Site Settings: Term Store Management Tool page, click the arrow to expand the **Search Dictionaries** menu.

Depending on which list the term is in, click either **Query Spelling Exclusions** or **Query Spelling Inclusions**.

Double-click the term that you want to edit.

Type the new name for the term.

Click anywhere on the page to save the edited term.

See also

## See also

Linguistic search features in SharePoint Server

Set-SPEnterpriseSearchQuerySpellingCorrection

Get-SPEnterpriseSearchQuerySpellingCorrection

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
