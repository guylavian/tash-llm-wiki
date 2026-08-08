---
title: "Create and import query suggestions for the classic search experience in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: search-create-and-import-query-suggestions
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/search/create-and-import-query-suggestions
family: search
documentKind: "how-to"
abstract: "Learn how to import query suggestions in SharePoint Server."
---

# Create and import query suggestions for the classic search experience in SharePoint Server - SharePoint Server

Note

Create and import query suggestions for the classic search experience in SharePoint Server

# Create and import query suggestions for the classic search experience in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

An easy way to help users search for information in SharePoint Server is to create *query suggestions*. Query suggestions are words that appear under the search box as users type a query.

SharePoint Server automatically creates a query suggestion when users have clicked a search result for a query at least six times. For example, if users have entered the query word "coffee" and then clicked on a search result six times, then "coffee" automatically becomes a query suggestion. We can also create query spelling suggestions manually. In this article, we'll use a simple example to show how to do this.

How to create a query suggestions file

## How to create a query suggestions file

Open a text editor, for example Notepad.

Enter the query spelling suggestions that you want to add. Add one word or phrase per line.

Save the file as a **.txt** file and encoding **UTF-8**.

Now that you have a query suggestions file, the next task is to import it to SharePoint Server.

How to import a query suggestions file to SharePoint

## How to import a query suggestions file to SharePoint

Go to **More features** in the SharePoint admin center, and sign in with an account that has admin permissions in Microsoft 365.

Under **Search**, select **Open**.

Select **Query Suggestion Settings**.

In the **Language for suggestions phrases** section, select the language of your query suggestions. In the **Always suggest phrases** section, select **Import from text file**.

In the **Text file that has phrases** section, select **Choose File**, and import your query suggestions file.

Select **OK**, and then **Save Settings**.

Important

When you import query suggestions, existing query suggestions are overwritten. If you haven't previously imported any query suggestions, you have nothing to worry about. Automatically created query suggestions will not be overwritten when you import new ones. But, if you want to import additional query suggestions, you should export the existing query suggestions file, update it, and then reimport it.

How to import a query suggestions file to SharePoint Server

## How to import a query suggestions file to SharePoint Server

Go to **Central Administration** --> **Manage service applications** --> **Search Service Application** --> **Query Suggestions**.

On the **Query Suggestion Settings** page, in the **Always suggest phases** section, select **Import from text file**.

On the **Import phrases for query suggestions** page, select **Browse**, and import your query suggestions file.

Select **OK**, and then **Save Settings**.

Important

When you import query suggestions, existing query suggestions are overwritten. If you haven't previously imported any query suggestions, you have nothing to worry about. Automatically created query suggestions won't be overwritten when you import new ones. But, if you want to import additional query suggestions, you should export the existing query suggestions file, update it, and then reimport it.

How to verify that your query suggestions are working

## How to verify that your query suggestions are working

Important

After you have uploaded your query suggestions file, it might take some hours before your query suggestions are displayed.

To verify that your query suggestions are working correctly, in a search box, type two letters of a phrase from your query suggestions file. The query suggestions appear under the search box.

See also

## See also

Concepts

#### Concepts

Manage query suggestions in SharePoint Server

Other Resources

#### Other Resources

Customize query suggestions in SharePoint search

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
