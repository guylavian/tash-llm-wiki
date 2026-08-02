---
title: "Export content and create reports in the eDiscovery Center - SharePoint Server"
type: reference
domain: sharepoint
slug: governance-export-content-and-create-reports-in-the-ediscovery-center
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/governance/export-content-and-create-reports-in-the-ediscovery-center
family: governance
documentKind: "how-to"
abstract: "You export content from a case when you are ready to deliver it to an authority or want to work on it with another legal program. You can also create reports to identify the contents of and any search indexing issues with the export. The export includes a load file based on the Electronic Discovery Reference Model standard."
---

# Export content and create reports in the eDiscovery Center - SharePoint Server

Note

Export content and create reports in the eDiscovery Center

# Export content and create reports in the eDiscovery Center

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You export content from a case when you are ready to deliver it to an authority or want to work on it with another legal program. You can also create reports to identify the contents of and any search indexing issues with the export. The export includes a load file based on the Electronic Discovery Reference Model standard.

Before you export content, the case should already have content sources, such as Web sites, and queries. Also, the computer you use to export content has to meet the following system requirements:

32- or 64-bit version of Windows 7 and later versions

Microsoft .NET Framework 4.5

One of the following supported browsers:

Internet Explorer 10 and later versions

Mozilla Firefox or Google Chrome, with the ClickOnce add-in installed

When you first export content or create a report, the eDiscovery Download Manager is installed, which exports the SharePoint content and reports to the your local computer. When downloading an eDiscovery export, users must log into SharePoint with the same account that they are logged into on their client machine. If you receive a warning asking whether or not to run the Download Manager, accept the warning and continue.

Export eDiscovery content

## Export eDiscovery content

If your case is not already open, in an eDiscovery Center, click **Cases**, and then click the case in which you want to export content.

In the **Search and Export** section, under **Queries**, click the name of the query you want to export. On the query page, you can see the size and contents to be included in the export.

At the bottom of the query page, click **Export**.

Type a name for the export. By default, the export is named the same as the query it's based on, but you can change the name.

On the page that appears, in the **Options** section, select any of the following:

To include versions of documents - if your organization tracks versions - select the **Include versions for SharePoint documents** checkbox.

To include items that are encrypted or have an unrecognizable format, select the **Include items that are encrypted or have an unrecognized format** check box.

Click **OK**.

Click **Download Results**.

If you are exporting content for the first time on a computer, you will be prompted to install the Discovery Download Manager. Click **Yes**.

When you are finished exporting, click **Close**.

Create reports about exported content

## Create reports about exported content

Reports identify the SharePoint content, its location, and other information, as well as any errors, such as content not exported as a result of search indexing issues. The reports are created in comma separated values format, which can be opened in Excel or imported into many types of programs.

In Microsoft Excel, you can examine the contents further by sorting and filtering the columns. For example, you could view only PowerPoint slides or sort by Web address or author.

If your case is not already open, in an eDiscovery Center, click **Cases**, and then click the case in which you want to export content.

In the **Search and Export** section, under **Queries**, click the name of the query you want to export.

At the bottom of the query page, click **Export**.

On the page that appears, in the Options section, select any of the following. The settings won't affect the report itself, but the report will show how the settings would affect your query:

To include versions of documents - if your organization tracks versions - select the **Include versions for SharePoint documents** checkbox. If your exported content contains many libraries that track versions, and many of your authors use versioning, this could significantly increase the file size of the export.

To include items that are encrypted or have an unrecognizable format, select the **Include items that are encrypted or have an unrecognized format** check box.

On the page that appears, click **OK**.

Click **Download Report**.

If you are exporting content for the first time on a computer, you will be prompted to install the Discovery Download Manager. Click **Yes**.

When you are finished exporting the report, click **Close**.

The following reports (Excel CSV files) are downloaded to your computer in a folder named Reports.

**Export Errors** This report lists any errors that occurred during the export process.

**SharePoint Index Errors**

**SharePoint Results** Contains a list of every SharePoint items returned as a search result. This report contains information such as the document type, the document author, the document URL, the URL and name of the site where the document is located, and the date when the document was last modified.

Note

If you don't select the **Include items that are encrypted or have an unrecognized format** option when you export search results or just download the reports, the index error reports are downloaded but they don't have any entries. This doesn't mean there aren't any indexing errors. It just means that unindexed items weren't included in the request to download the reports.

Find more information about eDiscovery

## Find more information about eDiscovery

For more information about eDiscovery cases, see the following articles:

Scenario: eDiscovery in SharePoint Server 2013 and Exchange Server 2013

Plan and manage cases in the eDiscovery Center

Add content to a case and place sources on hold in the eDiscovery Center

Searching and using keywords in the eDiscovery Center

Default crawled file name extensions and parsed file types in SharePoint Server 2013

Overview of crawled and managed properties in SharePoint Server 2013

Create and run queries in the eDiscovery Center

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
