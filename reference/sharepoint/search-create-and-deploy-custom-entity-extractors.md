---
title: "Create and deploy custom entity extractors in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: search-create-and-deploy-custom-entity-extractors
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/search/create-and-deploy-custom-entity-extractors
family: search
documentKind: "install-set-up-deploy"
abstract: "Learn to create custom entity extractors and how to use them to set up custom refiners. Create one or more custom entity extraction dictionaries and connect them to managed properties."
---

# Create and deploy custom entity extractors in SharePoint Server - SharePoint Server

Note

Create and deploy custom entity extractors in SharePoint Server

# Create and deploy custom entity extractors in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You create and maintain the custom entity extractor file in a system external to SharePoint Server before you import it into SharePoint Server to make the custom entity extractor available to the search system.

To use custom entities as refiners in classic search, you first create a custom entity extraction dictionary and deploy it. Then, you configure a managed property to use a custom entity extractor and run a full crawl. After that, you can configure the Refinement Web Part on the search results page to use the custom entity as a refiner.

Before you begin

## Before you begin

Before you begin this operation, you must have in place:

A Search service application

One or more fully crawled content sources

A search results page

Create a custom entity extraction dictionary

## Create a custom entity extraction dictionary

**To create a custom entity extraction dictionary**

Determine which type of custom entity extraction dictionary you want to create: Word, Word Part, Word exact or Word Part exact. See Overview of custom entity extractor types.

Create a .csv file with the columns **Key** and **Display Form**. Make sure you use a comma as the column separator. If the file contains non-ASCII characters such as diacritics, you must encode it in UTF-8. Save the file to a location that is accessible from the server from which you will run the Microsoft PowerShell cmdlet to deploy the custom entity extraction dictionary.

In the **Key** column, enter the term (single or multiple words) that you want to include as custom entities. You can use more than one line per key. Make sure there are no leading or trailing spaces around the terms.

(Optional) In the **Display form** column, enter a refiner name. If you leave this column empty, the term that is extracted from the content will be displayed as the refiner in the same case as it occurs in the content. Use the **Display Form** column to control and standardize the way in which the refiner is displayed.

For example, an organization named Contoso has a certification system with three levels: Contoso Beginner, Contoso Professional and Contoso Expert. Contoso wants to extract these entities and wants to be able to refine on all of them. Regardless of the case in which the word "Contoso", "beginner", "professional" or "expert" is written, they want to display the refiner as **Contoso Beginner**, **Contoso Professional** and **Contoso Expert**. For this example, the custom entity extraction dictionary file input could look like this:

```
Key,Display form
Contoso Beginner,Contoso Beginner
Contoso B1,Contoso Beginner
Contoso Professional,Contoso Professional
Contoso prof,Contoso Professional
Contoso Expert,Contoso Expert
```

Deploy a custom entity extraction dictionary

## Deploy a custom entity extraction dictionary

To deploy the custom entity extraction dictionary, you must import it into SharePoint Server.

**To import a custom entity extraction dictionary**

Verify that the user account that is importing the custom entity extractor dictionary is an administrator for the Search service application.

Start the SharePoint Management Shell.

At the Windows PowerShell command prompt, type the following command:

```
$searchApp = Get-SPEnterpriseSearchServiceApplication
Import-SPEnterpriseSearchCustomExtractionDictionary -SearchApplication $searchApp -Filename <Path> -DictionaryName <Dictionary name> 
```

Where:

*<Path>* specifies the full UNC path of the .csv file (the custom extraction dictionary) to be imported.

*<Dictionary name>* is the name of the type of the custom extraction dictionary.

Depending on which type of dictionary you are importing, enter one of the following:

Microsoft.UserDictionaries.EntityExtraction.Custom.Word. *n*  [where  *n*  = 1,2,3,4 or 5]

Microsoft.UserDictionaries.EntityExtraction.Custom.ExactWord.1

Microsoft.UserDictionaries.EntityExtraction.Custom.WordPart. *n*  [where  *n*  = 1,2,3,4 or 5]

Microsoft.UserDictionaries.EntityExtraction.Custom.ExactWordPart.1

Configure a managed property for custom entity extraction

## Configure a managed property for custom entity extraction

The following procedure describes how to associate the custom entity extraction dictionary with an existing managed property from which you want to extract custom entities. Typically, this is a managed property that you expect to contain these entities, such as the managed properties **Title** or **Body**. Custom entities are extracted from the full contents of the managed property they are associated with, even if sections in those contents are tagged as **<no index>**.

To specify from which existing managed property custom entities should be extracted, you edit the existing managed property. For more information about managing crawled and managed properties, see Manage the search schema in SharePoint Server.

**To edit a managed property for custom entity extraction**

Verify that the user account is the administrator of the Search service application.

In Central Administration, in the **Application Management** section, click **Manage service applications**.

Click the Search service application.

On the Search Administration page, in the Quick Launch, under **Queries and Results**, click **Search Schema**.

On the **Managed Properties** page, find the managed property that you want to associate the custom entity extraction dictionary with that contains the single or multiple words (or word parts). You can also enter the name of the managed property in the **Filter** box.

Point to the managed property, click the arrow and then click **Edit/Map property**.

On the Edit Managed Property page, edit the settings under **Custom entity extraction**. Select the custom entity extraction dictionary that you have imported, and then click **OK**.

After the next full crawl has completed, the custom entity extractor is enabled. The original managed property content is saved unchanged in the search index. In addition, depending on the type of custom entity extractor you have enabled, the extracted entities are copied to one or more of the following managed properties:

- WordCustomRefiner1

- WordCustomRefiner2

- WordCustomRefiner3

- WordCustomRefiner4

- WordCustomRefiner5

- WordExactCustomRefiner

- WordPartCustomRefiner1

- WordPartCustomRefiner2

- WordPartCustomRefiner3

- WordPartCustomRefiner4

- WordPartCustomRefiner5

- WordPartExactCustomRefiner

These managed properties are automatically configured to be searchable, queryable, retrievable, sortable and refinable.

Configure a refiner in the Web Part

## Configure a refiner in the Web Part

You can use the extracted custom entities as refiners in the search results page. The refiners based on the custom entities are available in the Refinement Web Part.

**To add a refiner based on a custom entity extractor**

Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the Enterprise Search Center site.

Browse to the page that contains the Refinement Web Part that you want to configure, click the **Settings menu** and then click **Edit Page**.

Edit the Refinement Web Part. Click the **Refinement Web Part Menu** arrow, and then click **Edit Web Part**.

In the Web Part tool pane, in the **Properties for Search Refinement** section, verify that the **Choose Refiners in this Web Part** is selected.

Click **Choose Refiners**.

On the Refinement configuration page, from the Available refiners section, use the buttons to select one or more managed properties containing extracted entities that you want to show as refiners from the list and click **Add**. For example, if you have deployed a word extraction dictionary, choose **WordCustomRefiner1**.

In the **Configure for** section, configure how you want each refiner to appear.

Click **OK**.

Overview of custom entity extractor types

## Overview of custom entity extractor types

The following table shows what type of custom extraction dictionaries you can create and how the dictionary entries are matched with content in the search index, which dictionary name you should use when you deploy the dictionary and which managed property will contain the extracted entities.

| **Custom entity extractor / custom entity extractor dictionary** | **Description** | **Example** | **Dictionary name to use in Windows PowerShell** | **Managed property that will contain the extracted entity** |
| --- | --- | --- | --- | --- |
| Word Extraction | Case-insensitive, dictionary entries matching tokenized content, maximum 5 dictionaries. | The entry "anchor" matches "anchor" and "Anchor," but not "anchorage" | Microsoft.UserDictionaries.EntityExtraction.Custom.Word.n   [where n = 1,2,3,4 or 5] | WordCustomRefiner1   WordCustomRefiner2   WordCustomRefiner3   WordCustomRefiner4   WordCustomRefiner5 |
| Word Part Extraction | Case-insensitive, dictionary entries matching un-tokenized content, maximum 5 dictionaries. | The entry "anchor" matches "anchor," "Anchor" and "anchorage" | Microsoft.UserDictionaries.EntityExtraction.Custom.WordPart.n   [where n = 1,2,3,4 or 5] | WordPartCustomRefiner1   WordPartCustomRefiner2   WordPartCustomRefiner3   WordPartCustomRefiner4   WordPartCustomRefiner5 |
| Word Exact Extraction | Case-sensitive, dictionary entries matching tokenized content, maximum 1 dictionary. | The entry "anchor" matches "anchor," but not "Anchor" or "Anchorage" | Microsoft.UserDictionaries.EntityExtraction.Custom.ExactWord.1 | WordExactCustomRefiner |
| Word Part Exact Extraction | Case-sensitive, dictionary entries matching un-tokenized content, maximum 1 dictionary. | The entry "anchor" matches "anchor" and "anchorage," but not "Anchor" | Microsoft.UserDictionaries.EntityExtraction.Custom.ExactWordPart.1 | WordPartExactCustomRefiner |

See also

## See also

Import-SPEnterpriseSearchCustomExtractionDictionary

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
